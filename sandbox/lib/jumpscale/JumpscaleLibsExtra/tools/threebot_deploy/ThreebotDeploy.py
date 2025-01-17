from Jumpscale import j
import os


class ThreebotDeploy(j.baseclasses.object_config):
    """
    create a threebot deployer instance
    follow readme to know how to deploy
    """

    _SCHEMATEXT = """
    @url = jumpscale.threebot.deploy
    name** = "" (S)
    do_machine_name = "" (S)
    do_token = "" (S)
    do_project_name = "" (S)
    ssh_key = "" (S)
    """

    def _init(self, **kwargs):
        self._do_client = None
        self._machine = None
        self._sshcl = None
        self._container_ssh = None

    @property
    def do_client(self):
        """
        : creats jumpscale digitalocean client using the provided data in init
        : return: jsx client object
        """
        if not self._do_client:
            client = j.clients.digitalocean.get(
                name=self.do_machine_name, token_=self.do_token, project_name=self.do_project_name
            )
            self._do_client = client
        return self._do_client

    def exists(self):
        return self.do_client.droplet_exists(self.do_machine_name)

    def machine_init(self):
        """
        : get digital ocean up machine
        : sets self._machine and self.sshcl
        """
        my_droplet = self.do_client._droplet_get(name=self.do_machine_name)
        j.sal.nettools.waitConnectionTest(my_droplet.ip_address, 22, 180)
        sshcl = j.clients.ssh.get(
            name=self.do_machine_name, addr=my_droplet.ip_address, client_type="paramiko", sshkey_name=self.ssh_key
        )
        self._machine = my_droplet
        self._sshcl = sshcl

    @property
    def do_machine(self):
        """
        : get digital ocean up machine
        : sets self._machine and self.sshcl
        """
        if not self._machine:
            self.machine_init()
        return self._machine

    @property
    def sshcl(self):
        if not self._sshcl:
            self.do_machine
        return self._sshcl

    @property
    def container_ssh(self):
        if not self._container_ssh:
            self._container_ssh = j.clients.ssh.get(
                name=f"{self.do_machine_name}_docker",
                addr=self._machine.ip_address,
                port=9000,
                sshkey_name=self.ssh_key,
            )
        return self._container_ssh

    def wireguard_install(self):
        j.tools.wireguard.new(name=self.do_machine_name, sshclient_name=self.do_machine_name, autosave=False).install()

    def create_new_do_machine(self, size_slug="s-1vcpu-1gb"):
        """
        : get digital ocean up machine
        : param size_slug: pass your machine specs check DO availabe slugs
        : return: digital ocean droplet object and sshclient object
        """
        my_droplet, sshcl = self.do_client.droplet_create(
            name=self.do_machine_name, sshkey=self.ssh_key, size_slug=size_slug, project_name=self.do_project_name
        )

        if not my_droplet and not sshcl:
            raise RuntimeError("Failed to create the machine!")

        self._machine = my_droplet
        self._sshcl = sshcl

    def jsx_install(self, branch="development"):
        """
        : install jumpscale non-interactivly on digital ocean machine
        """
        install_cmd = "export DEBIAN_FRONTEND=noninteractive;"
        install_cmd += f"curl https://raw.githubusercontent.com/threefoldtech/jumpscaleX_core/{branch}/install/jsx.py?$RANDOM > /tmp/jsx;"
        install_cmd += "chmod +x /tmp/jsx;"
        if not os.environ.get("SSH_AUTH_SOCK"):
            install_cmd += "eval `ssh-agent -s`;"
        install_cmd += "rm -rf ~/.ssh/id_rsa ~/.ssh/id_rsa.pub;"
        install_cmd += 'ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa -q -P "";'
        install_cmd += f"/tmp/jsx container-install -s -b {branch} --ports 80:80 --ports 443:443 --ports 8901:8901"

        rc, out, err = self.sshcl.execute(install_cmd)

        if rc > 0:
            raise RuntimeError(out, "Error occured at\n", err)

    def install_tcprouter_coredns(self):
        """
        : deploy tcp router and coredns on digital ocean machine
        """
        install_tcpdns_command = ". /sandbox/env.sh;"
        install_tcpdns_command += "kosmos 'j.builders.network.tcprouter.install()';"
        install_tcpdns_command += "kosmos 'j.builders.network.coredns.install()';"

        rc, out, err = self.container_ssh.execute(install_tcpdns_command)

        if rc > 0:
            raise RuntimeError(out, "Error occured at\n", err)

    def add_dns_record(
        self, subdomain="testwikis", domain="web.grid.tf", wikis_machine_ip=None, wikis_machine_port="443"
    ):
        """
        add dns record on the dns server this will use coredns and tfgateway
        """
        if not wikis_machine_ip:
            wikis_machine_ip = self.do_machine.ip_address
        add_dns_command = ". /sandbox/env.sh;"
        add_dns_command += "kosmos 'j.builders.network.coredns.stop()';"
        add_dns_command += "kosmos 'j.builders.network.tcprouter.stop()';"
        add_dns_command += f'kosmos "redis_client = j.clients.redis.get(); j.tools.tf_gateway.get(redis_client).tcpservice_register(\\"{subdomain}.{domain}\\", \\"{wikis_machine_ip}\\", {wikis_machine_port})";'
        add_dns_command += f'kosmos "redis_client = j.clients.redis.get(); j.tools.tf_gateway.get(redis_client).domain_register_a(\\"{subdomain}\\", \\"{domain}\\", [\\"{wikis_machine_ip}\\"])";'
        add_dns_command += "kosmos 'j.builders.network.coredns.start()';"
        add_dns_command += "kosmos 'j.builders.network.tcprouter.start()';"
        rc, out, err = self.container_ssh.execute(add_dns_command)

        if rc > 0:
            raise RuntimeError(out, "Error occured at\n", err)

    def threebot_start(self, web=True, ssl=True):
        cmd = f". /sandbox/env.sh; kosmos -p 'j.servers.threebot.install(); threefold = j.servers.threebot.default;threefold.web={web};threefold.ssl={ssl};threefold.start(background=True)'"
        self.container_ssh.execute(cmd)
        client = self.threebot_client()
        client.actors.package_manager.package_add(path="/sandbox/code/github/threefoldtech/jumpscaleX_threebot/ThreeBotPackages/threebot/registration/")
        return client

    def threebot_client(self):
        j.sal.nettools.waitConnectionTest(self.do_machine.ip_address, 8901, 600)
        return j.clients.gedis.get(name=self.do_machine.name, port=8901, host=self.do_machine.ip_address)

    def deploy_wikis(self):
        """
        : deploy 3bot and wikis on the wikis machine
        """
        wikis_command = "apt-get install -y graphviz;"
        wikis_command += ". /sandbox/env.sh;"
        wikis_command += "kosmos -p 'j.threebot.package.wikis.install()';"
        wikis_command += "kosmos -p 'j.builders.apps.threebot.install()';"
        wikis_command += "kosmos -p 'cl = j.servers.threebot.local_start_default(web=True)"
        wikis_command += "jsx wiki-load;"
        self.container_ssh.execute(wikis_command)

    def reset_env(self):
        """
        clears bcdb and sonic
        """
        reset_command = ". /sandbox/env.sh;"
        reset_command += "kosmos 'j.data.bcdb.destroy_all()';"
        reset_command += "pkill redis;"
        reset_command += "pkill redis-server;"
        reset_command += "kosmos 'j.application.bcdb_system_destroy()';"
        reset_command += "kosmos 'j.servers.sonic.default.destroy()';"

        rc, out, err = self.container_ssh.execute(reset_command)

        if rc > 0:
            raise RuntimeError(out, "Error occured at\n", err)

    def test_wikis(self):
        """
        : add some wikis tests to test with some macros
        """
        test_command = ". /sandbox/env.sh;"
        test_command += "jsx threebot-test -d -w;"
        rc, out, err = self.container_ssh.execute(test_command)

        if rc > 0:
            raise RuntimeError(out, "Error occured at\n", err)


class ThreebotDeployFactory(j.baseclasses.object_config_collection):
    """
    Factory for threebot deployment
    to deploy you will need a macine for tcp router and another for the packages you want
    """

    __jslocation__ = "j.tools.threebot_deploy"
    _CHILDCLASS = ThreebotDeploy
