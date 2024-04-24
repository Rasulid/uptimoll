from amocrm.v2 import tokens

if __name__ == '__main__':
    tokens.default_token_manager(
        client_id="5435ce6f-a7f8-4529-a250-91ac32b6cb46",
        client_secret="KxlfiGRGZv1a4LdH7kxzRLRMdUc98mXLDghBD5zSXkaYrfbdAbpH3sHRmyVWJ5qU",
        subdomain="mitacademycrmuz",
        redirect_url="https://www.mitacademy.uz/home",
        storage=tokens.FileTokensStorage(),  # by default FileTokensStorage
    )
    # tokens.default_token_manager.init(code="def5020001888fce16646ccdfa150aa0626d339ea4521869507b469db70a7cb71f669b5f74f3f943112fc1e4fe1c663327a8a25c681c8f80ce2603c972f144edc7b6e5fe7625d564b74a2212238c82e06cd92aa5002340f291be82d859e7901b67dd37f6988765575574b45b438d5e7ebb8d272a20e1c7014fde1bb45cbe927184f5286145e6cfb7f00a3c11e51c0a1d2d18a190f7546607a90a16f6f9fa8d5546d1136db664bc5cc702b5613f28b76ffb32760446700ee06e894049f806587cd568f5b516bd19b43765c0a50390fa02e874035432631cc39955a9734e29a06100faa631a383f0852a4acad4a7042c9ca678194cfb2c0994042d8606861c3e9f80f15f7c591bb4baeaf45edce4dc8f12a23b6d24e5f0c2098100968af5ee765ed0104f95e9b469d004fbb9efa12ef34002e7dd7ae1c231b54d72bbbbfd3f291441ba3c2735fa608977ae4e9ac83e32fb378c067005640a67561051cabca05ca60bdc0ef23fc4af2046c61e18fe494ad88b2ff4de08ab06e12c771c6aa07864899b33f58e106ca25a3dd147123757b13111bab615392b93fe73577aacc95f8b881e10d71aad65099b7aef7c0b176ae8c4ef3cb9bef79e860c7a9e0cfa86eaa89a44737943ea5421d89ffd17fd8f9699e895df302737585996ec30849395ac9d3256202e0638a2e5e22fc91654c4aff880",
    #                                   skip_error=False)



