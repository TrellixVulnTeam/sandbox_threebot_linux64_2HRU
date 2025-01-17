from Jumpscale import j

from .ExecutorBase import ExecutorBase


class ExecutorSSH(ExecutorBase):
    def __init__(self, sshclient):

        self.sshclient = sshclient

        self._id = self.sshclient.uid

        self.kosmos = self.sshclient.kosmos
        self.shell = self.sshclient.shell
        self.upload = self.sshclient.upload
        self.download = self.sshclient.download
        self.execute_jumpscale = self.sshclient.execute_jumpscale

        ExecutorBase.__init__(self)

        self.type = "ssh"

    def execute(
        self,
        cmd,
        die=True,
        showout=False,
        timeout=1000,
        env=None,
        sudo=False,
        replace=True,
        interactive=False,
        script=False,
    ):
        """
        @RETURN rc, out, err
        """
        if env or sudo or script:
            raise j.exceptions.NotFound("Not implemented for ssh executor")
        return self.sshclient.execute(cmd, interactive, showout, replace, die, timeout)

    @property
    def uid(self):
        return self.sshclient.uid

    @property
    def config_msgpack(self):
        return self.sshclient.config_msgpack

    @config_msgpack.setter
    def config_msgpack(self, value):
        if value != self.sshclient.config_msgpack:
            self.sshclient.config_msgpack = value
            self._log_info("save config msgpack for:%s" % self)
            self.sshclient.save()

    @property
    def env_on_system_msgpack(self):
        return self.sshclient.env_on_system_msgpack

    @env_on_system_msgpack.setter
    def env_on_system_msgpack(self, value):
        if value != self.sshclient.env_on_system_msgpack:
            self.sshclient.env_on_system_msgpack = value
            self._log_info("save system msgpack for:%s" % self)
            self.sshclient.save()

    def state_reset(self):
        self.config["state"] = {}
        self.sshclient.state_reset()

    def save(self):
        """
        only relevant for ssh
        :return:
        """
        # fill save automatically
        self.config_msgpack = j.data.serializers.msgpack.dumps(self.config)

    # def config_save(self, **kwargs):
    #     self.sshclient.config_save(**kwargs)

    # def save(self, onsystem=False):
    #     self.sshclient.save()
    # if onsystem:
    #     self.config_save_on_system()

    # def config_save_on_system(self):
    #     self.sshclientfile_write("/root/.jsxssh.msgpack", self.executor.config_msgpack)
    #     self.sshclient.save()

    def __repr__(self):
        return "Executor ssh: %s (%s)" % (self.sshclient.addr, self.sshclient.port)

    __str__ = __repr__
