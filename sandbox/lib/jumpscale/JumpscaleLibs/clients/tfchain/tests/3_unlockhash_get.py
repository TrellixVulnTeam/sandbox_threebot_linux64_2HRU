from Jumpscale import j

from JumpscaleLibs.clients.tfchain.stub.ExplorerClientStub import TFChainExplorerGetClientStub
from JumpscaleLibs.clients.tfchain.test_utils import cleanup


def main(self):
    """
    to run:

    kosmos 'j.clients.tfchain.test(name="unlockhash_get")'
    """

    cleanup("test_unittest_client")

    # create a tfchain client for devnet
    c = j.clients.tfchain.new("test_unittest_client", network_type="TEST")

    # (we replace internal client logic with custom logic as to ensure we can test without requiring an active network)
    explorer_client = TFChainExplorerGetClientStub()
    explorer_client.hash_add(
        "01d1c4dd242e3badf45004be9a3b86c613923c6d872bab5ec92e4f076114d4c3a15b7b43e1c00f",
        '{"hashtype":"unlockhash","block":{"minerpayoutids":null,"transactions":null,"rawblock":{"parentid":"0000000000000000000000000000000000000000000000000000000000000000","timestamp":0,"pobsindexes":{"BlockHeight":0,"TransactionIndex":0,"OutputIndex":0},"minerpayouts":null,"transactions":null},"blockid":"0000000000000000000000000000000000000000000000000000000000000000","difficulty":"0","estimatedactivebs":"0","height":0,"maturitytimestamp":0,"target":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"totalcoins":"0","arbitrarydatatotalsize":0,"minerpayoutcount":0,"transactioncount":0,"coininputcount":0,"coinoutputcount":0,"blockstakeinputcount":0,"blockstakeoutputcount":0,"minerfeecount":0,"arbitrarydatacount":0},"blocks":null,"transaction":{"id":"0000000000000000000000000000000000000000000000000000000000000000","height":0,"parent":"0000000000000000000000000000000000000000000000000000000000000000","rawtransaction":{"version":0,"data":{"coininputs":[],"minerfees":null}},"coininputoutputs":null,"coinoutputids":null,"coinoutputunlockhashes":null,"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false},"transactions":[{"id":"0add5d695e01525be854a3c404503e60fd1245b4602cad9608c5d5fdfb3e028e","height":1873,"parent":"ba6dcf696aff09f5b558e63dde2554edf948e66c1295b11324951647e9ad467a","rawtransaction":{"version":0,"data":{"coininputs":[{"parentid":"6c97c4e0bf832133ad370b9a5daff1309b00b570484a922329ef91e9f7ffa7fe","unlocker":{"type":1,"condition":{"publickey":"ed25519:b86e9efbf7442e353ad7f98f159eb23fe66a1722e11f547876f55b5521d6e350"},"fulfillment":{"signature":"89e6f578416c0db8c399bc8010cd3f11c936931007b1299bb6e436e933f1b7e26702ecb58a04c2d81802d13737e73745fb7657cc4b5c8e0c1d0fddfb6c71ef05"}}}],"coinoutputs":[{"value":"10000000000000000","unlockhash":"015df22a2e82a3323bc6ffbd1730450ed844feca711c8fe0c15e218c171962fd17b206263220ee"},{"value":"89839999300000000","unlockhash":"01d1c4dd242e3badf45004be9a3b86c613923c6d872bab5ec92e4f076114d4c3a15b7b43e1c00f"}],"minerfees":["100000000"]}},"coininputoutputs":[{"value":"99839999400000000","condition":{"type":1,"data":{"unlockhash":"01c389c2b8e097bc4970754b440a962326340eba85dff7a8dd96f7b14bbe0be8e79318c4b6c564"}},"unlockhash":"01c389c2b8e097bc4970754b440a962326340eba85dff7a8dd96f7b14bbe0be8e79318c4b6c564"}],"coinoutputids":["113e7113a436aaa3d43f29afa382706e820e2747ca74bec62646bc35049e68d6","c1df239aba64ca0c6a241ddf18f3dd18b75e2c650874dd4c8c7dbbb56bd73683"],"coinoutputunlockhashes":["015df22a2e82a3323bc6ffbd1730450ed844feca711c8fe0c15e218c171962fd17b206263220ee","01d1c4dd242e3badf45004be9a3b86c613923c6d872bab5ec92e4f076114d4c3a15b7b43e1c00f"],"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false},{"id":"513f3542c91f1be112ea4b36d3204afea9bb43d5c32295896d94cae96078714c","height":1878,"parent":"cd00da19a01822ad5c73279775a06c902832835c865ae7c5aa6bbbc01c8882f7","rawtransaction":{"version":0,"data":{"coininputs":[{"parentid":"113e7113a436aaa3d43f29afa382706e820e2747ca74bec62646bc35049e68d6","unlocker":{"type":1,"condition":{"publickey":"ed25519:ef8c1f52aa64f837b50b9bfb85106906d05f43a5768dbf8320b87bce14dc00cc"},"fulfillment":{"signature":"8bcb889b30735b546cbbe6328d38f130f77e7c93b07d6cfdd09124bbda589c61a444d0e8126d614031237d85b8995476cb02c756f860ef3c57f1d48722426408"}}}],"coinoutputs":[{"value":"9999989999990000","unlockhash":"01d1c4dd242e3badf45004be9a3b86c613923c6d872bab5ec92e4f076114d4c3a15b7b43e1c00f"},{"value":"9900010000","unlockhash":"015df22a2e82a3323bc6ffbd1730450ed844feca711c8fe0c15e218c171962fd17b206263220ee"}],"minerfees":["100000000"]}},"coininputoutputs":[{"value":"10000000000000000","condition":{"type":1,"data":{"unlockhash":"015df22a2e82a3323bc6ffbd1730450ed844feca711c8fe0c15e218c171962fd17b206263220ee"}},"unlockhash":"015df22a2e82a3323bc6ffbd1730450ed844feca711c8fe0c15e218c171962fd17b206263220ee"}],"coinoutputids":["9101b35ad291ba03ec16699abaf2422ef3f11d82b7e20e4921af05274f8495a4","440f6d91460143162d55a732e48ab3ab179a2375af8317b37b28f8d4a66de2e4"],"coinoutputunlockhashes":["01d1c4dd242e3badf45004be9a3b86c613923c6d872bab5ec92e4f076114d4c3a15b7b43e1c00f","015df22a2e82a3323bc6ffbd1730450ed844feca711c8fe0c15e218c171962fd17b206263220ee"],"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false},{"id":"96df1e34533ffcd42ee1db995e165538edd275ba0c065ef9293ead84ff923eec","height":2662,"parent":"b69bc0a12308938cbc8207483f39df63a2295142875944d6a2db3930d5c2564f","rawtransaction":{"version":0,"data":{"coininputs":[{"parentid":"c1df239aba64ca0c6a241ddf18f3dd18b75e2c650874dd4c8c7dbbb56bd73683","unlocker":{"type":1,"condition":{"publickey":"ed25519:25b6aae78d545d64746f4a7310230e7b7bce263dcaa9dd5b3b6dd614d0f46413"},"fulfillment":{"signature":"7453f27cca1381f0cc05a6142b8d4ded5c1f84132742ba359df99ea7c17b2f304f8b9c8f3722da9ceb632fb7f526c8022c71e385bb75df9542cf94a7f3f3cc06"}}}],"coinoutputs":[{"value":"1000000000000000","unlockhash":"0199f4f21fc13ceb22da91d4b1701e67556a7c23f118bc5b1b15b132433d07b2496e093c4f4cd6"},{"value":"88839999200000000","unlockhash":"0175c11c8124e325cdba4f6843e917ba90519e9580adde5b10de5a7cabcc3251292194c5a0e6d2"}],"minerfees":["100000000"]}},"coininputoutputs":[{"value":"89839999300000000","condition":{"type":1,"data":{"unlockhash":"01d1c4dd242e3badf45004be9a3b86c613923c6d872bab5ec92e4f076114d4c3a15b7b43e1c00f"}},"unlockhash":"01d1c4dd242e3badf45004be9a3b86c613923c6d872bab5ec92e4f076114d4c3a15b7b43e1c00f"}],"coinoutputids":["90513506d1216f89e73a361b6306d8543c81aff092e376ee8d8bb9b7ea024de6","7daf8035a6697701aeed36b4d6fe8de6ff4bbf9fd1ba9b0933d87e260f924783"],"coinoutputunlockhashes":["0199f4f21fc13ceb22da91d4b1701e67556a7c23f118bc5b1b15b132433d07b2496e093c4f4cd6","0175c11c8124e325cdba4f6843e917ba90519e9580adde5b10de5a7cabcc3251292194c5a0e6d2"],"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false},{"id":"ace08f4a5977c281db617fa48409ff9207357e851ddfd30f89c5edb783a03199","height":48274,"parent":"c4589dfd355674cfe58edb52234b76c262d615673b97edb8231723287af0581d","rawtransaction":{"version":1,"data":{"coininputs":[{"parentid":"9101b35ad291ba03ec16699abaf2422ef3f11d82b7e20e4921af05274f8495a4","fulfillment":{"type":1,"data":{"publickey":"ed25519:25b6aae78d545d64746f4a7310230e7b7bce263dcaa9dd5b3b6dd614d0f46413","signature":"fc5dbfcd29683f194bc2dd231d978189eb5e0ca049cc75e24cc72bdde36c7ed985c7bf271e6c946a58b23ef53193fb0cc754d6b4764e7637cfbff34581170f08"}}}],"coinoutputs":[{"value":"9999989899990000","condition":{"type":1,"data":{"unlockhash":"0135e3b63e97352539b99d3517629b1ba1f80ae5753a14558e9ed53e067372257689de877a8669"}}}],"blockstakeinputs":[{"parentid":"72ca786c954c743345895ca8e077d47fb90e8df03cd10511b6a53e19218e5761","fulfillment":{"type":1,"data":{"publickey":"ed25519:947363721019b146de2830fb94e00203568e93fa9c0f18d7c4196619d7209716","signature":"3b7add54388b416239004ca1f5676c3dffcfc8f585dc54477c77d299bd9f5e016d122746943883a4b1590c3aa27ef8bdaf9ab7284a12cc9e0f36061085b6dd01"}}}],"blockstakeoutputs":[{"value":"100","condition":{"type":1,"data":{"unlockhash":"01046b3927877c8f0482e32b5bdd99a021fc32dd0fce980c4bab454502534dbe91ddec7867a91d"}}},{"value":"100","condition":{"type":1,"data":{"unlockhash":"010fc30ec4ea7441424fc2e9ca061c7c0ed3a1a3b0bb756c1c0a4d296a2b45414443e1927ecd8a"}}},{"value":"100","condition":{"type":1,"data":{"unlockhash":"01019557b45c1644454b81568c6f640058f95bf1d6b82b13f4f5607a35a2a7e87c77df68aa59fb"}}},{"value":"100","condition":{"type":1,"data":{"unlockhash":"010027e8215ddc5ccbaa2968f3c02efb3f6c96da53aca30b6c20af29a8db83c6f0dae5ceca3914"}}},{"value":"100","condition":{"type":1,"data":{"unlockhash":"010b375bef59fd7cc40ace960c81323e2b2ea052408a210126655081a75b801bbc82706fb18e5b"}}},{"value":"100","condition":{"type":1,"data":{"unlockhash":"01011b823090c865dfc4d227194b48931cfc06049ed4bf3581ef31c5340e9e1eb3ce5926139186"}}},{"value":"100","condition":{"type":1,"data":{"unlockhash":"010e23596270ca9ca9fdef5ec9460e5ae2985e7fd523221c7ba49c1fe86d8049513ef2701bf3b0"}}},{"value":"100","condition":{"type":1,"data":{"unlockhash":"01054edb99d92d73b63a89cee82e6b5326e5b12477f70d3983d87a14199aa3752877f1cfe30325"}}},{"value":"100","condition":{"type":1,"data":{"unlockhash":"010ac443f407ed17620471d8533bb0c119dd6068960b96f5b5e67da7dba716e0fc922365b6db3f"}}},{"value":"100","condition":{"type":1,"data":{"unlockhash":"01009a4409b0aa789cbe3b38ae54268557201eb0439c68b61603685794c4a5d024dd1de070a113"}}}],"minerfees":["100000000"]}},"coininputoutputs":[{"value":"9999989999990000","condition":{"type":1,"data":{"unlockhash":"01d1c4dd242e3badf45004be9a3b86c613923c6d872bab5ec92e4f076114d4c3a15b7b43e1c00f"}},"unlockhash":"01d1c4dd242e3badf45004be9a3b86c613923c6d872bab5ec92e4f076114d4c3a15b7b43e1c00f"}],"coinoutputids":["512923b5fab87d2fe56e5a6560d699edb489b2fa55d2d23d9637ae0b79b803a8"],"coinoutputunlockhashes":["0135e3b63e97352539b99d3517629b1ba1f80ae5753a14558e9ed53e067372257689de877a8669"],"blockstakeinputoutputs":[{"value":"1000","condition":{"type":1,"data":{"unlockhash":"01e34588bee49b2cbd53f2198cd5022fbbe78aecb8125a39efb8699720b946e84ead718daf0cd6"}},"unlockhash":"01e34588bee49b2cbd53f2198cd5022fbbe78aecb8125a39efb8699720b946e84ead718daf0cd6"}],"blockstakeoutputids":["7e3bff69d2df91b096ffa2b7850492d7fbe6b97d898383d5901b8668e78b06a3","6cb28b29a22cb1f7c091bf9d301715b69a4eb9de94ba4326d448f74c326aac4b","a080392691d4600f1befade214fe58c8ad400fd675508123268a84df47acd378","1ad0bb99aebb90003d00d577b4ca6a2b09f23f83a157d8594b23b0d49cf3db73","dcdff507fa3286f9ad34851e0e652a7ec5cd7a733d510e98637db4cb81c0f3c0","8960cd3603b72604970be8b3e67d6408a3acf5525f183204ecddcccd17502488","dbe17310db33d643f059854d688ffa00ca77e62760bd11444c58406c8e94e3dd","021629a2b93a1d0200e21419cdedd41d115dc66e2e8323259eec4b7ae7c72393","aaccae5d65a5552bc0541830069c07ca8e4f048296e53c9a16cd237a01339845","9daf6b9f2a053f3d3340a8f10b3ec82fd581ebc3b3a9fccb1ab06a4db005fbf6"],"blockstakeunlockhashes":["01046b3927877c8f0482e32b5bdd99a021fc32dd0fce980c4bab454502534dbe91ddec7867a91d","010fc30ec4ea7441424fc2e9ca061c7c0ed3a1a3b0bb756c1c0a4d296a2b45414443e1927ecd8a","01019557b45c1644454b81568c6f640058f95bf1d6b82b13f4f5607a35a2a7e87c77df68aa59fb","010027e8215ddc5ccbaa2968f3c02efb3f6c96da53aca30b6c20af29a8db83c6f0dae5ceca3914","010b375bef59fd7cc40ace960c81323e2b2ea052408a210126655081a75b801bbc82706fb18e5b","01011b823090c865dfc4d227194b48931cfc06049ed4bf3581ef31c5340e9e1eb3ce5926139186","010e23596270ca9ca9fdef5ec9460e5ae2985e7fd523221c7ba49c1fe86d8049513ef2701bf3b0","01054edb99d92d73b63a89cee82e6b5326e5b12477f70d3983d87a14199aa3752877f1cfe30325","010ac443f407ed17620471d8533bb0c119dd6068960b96f5b5e67da7dba716e0fc922365b6db3f","01009a4409b0aa789cbe3b38ae54268557201eb0439c68b61603685794c4a5d024dd1de070a113"],"unconfirmed":false}],"multisigaddresses":null,"unconfirmed":false}',
    )
    c._explorer_get = explorer_client.explorer_get

    # get a transaction
    result = c.unlockhash_get("01d1c4dd242e3badf45004be9a3b86c613923c6d872bab5ec92e4f076114d4c3a15b7b43e1c00f")

    # you can go through all transactions that are somehow linked to the given transactions
    assert isinstance(result.transactions, list) and len(result.transactions) > 0
    txn = None
    for rtxn in result.transactions:
        if str(rtxn.id) == "96df1e34533ffcd42ee1db995e165538edd275ba0c065ef9293ead84ff923eec":
            txn = rtxn
            break
    assert txn is not None

    # from the transaction you can get all kind of info
    assert str(txn.id) == "96df1e34533ffcd42ee1db995e165538edd275ba0c065ef9293ead84ff923eec"
    assert txn.height == 2662
    assert (
        txn.version == 1
    )  # in reality it is 0, but the JSX tfchain client converts v0 transactions automatically to v1 transactions
    assert len(txn.coin_inputs) == 1
    assert str(txn.coin_inputs[0].parentid) == "c1df239aba64ca0c6a241ddf18f3dd18b75e2c650874dd4c8c7dbbb56bd73683"
    assert len(txn.coin_outputs) == 2
    assert str(txn.coin_outputs[0].value) == "1000000"
    assert (
        str(txn.coin_outputs[1].condition.unlockhash)
        == "0175c11c8124e325cdba4f6843e917ba90519e9580adde5b10de5a7cabcc3251292194c5a0e6d2"
    )
    assert str(txn.miner_fees[0]) == "0.1"
    assert len(txn.miner_fees) == 1

    # the explorer provides us also with info that is not part of a tfchain txn,
    # the tfchain client injects this into the txn as well for easy look-up
    assert str(txn.coin_inputs[0].parent_output.value) == "89839999.3"
    assert (
        str(txn.coin_inputs[0].parent_output.condition.unlockhash)
        == "01d1c4dd242e3badf45004be9a3b86c613923c6d872bab5ec92e4f076114d4c3a15b7b43e1c00f"
    )
    assert str(txn.coin_outputs[0].id) == "90513506d1216f89e73a361b6306d8543c81aff092e376ee8d8bb9b7ea024de6"
    assert str(txn.coin_outputs[1].id) == "7daf8035a6697701aeed36b4d6fe8de6ff4bbf9fd1ba9b0933d87e260f924783"
    assert txn.unconfirmed == False

    # you can also get multisig addresses linked to the looked up unlockhash
    assert isinstance(result.multisig_addresses, list)

    c.delete()
