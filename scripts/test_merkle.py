from brownie import FRZtoken, MerkleDistributor
from scripts.deploy_main import DEPLOYER

merkle = MerkleDistributor.deploy(
    "0x2823d7df030bc8e00ae6a7b9891c14720a60c3d97d2d639ce68249f57783768a",
    {"from": accounts[0]},
)
token = FRZtoken.deploy(merkle, accounts[6], "FRZ", {"from": accounts[0]})
merkle.initialize(token, {"from": accounts[0]})

proof = [
    "0x3c60e097c59a73bdfc01ec9b48e4931ff32d2fce7d11ece3e97487cfaa600bcf",
    "0xd999846254f1dce87979409b2ce6aa0e4d0106304f9fbf3861f902551b08a226",
]
tx = merkle.claim(
    0,
    "0x96b6de62f4cCb4381937b8446D5F0aA7c153aC29",
    1000000000000000000000,
    proof,
    {"from": DEPLOYER},
)


[
    "0xe1a462aa297a15bee7c9cda75beff5b8370f0da649f653cad8e695110f365573",
    "0xc890c41978ecc1e954766f2fb276ca689a84c15938394aa1bd83693a16de40ef",
    "0x6a478b7238134f11bfe95dd3cda0cc661fa5c0fe13c6d8b9635c8bdf4c87bceb",
    "0x49d70b607f228fa2faf6121dbc687bbad77f56ccbc369f5b77200b6c27f68431",
    "0xe3998a3beb5a41f6e690ca3c99f8cc4cfcc114a7075108989887530313c5e5f9",
    "0xdc4a48050bd754fc8e4e8e278b93da72e311c21caab33300c4c0ca89c68690e1",
    "0x6f8a8c605f4553f0a1b04f6064efaf9f82f8cdb641dcae73237a82906fc5a401",
    "0x57f0768fe496a806164f1512abb94c72b8595535680f2ad374ee74cf1bc06d5c",
    "0x0d1b78459bf0d83897ca76e6936f108281248d2e1ac0fe3651114255d5425b1a",
    "0x525b726d3ce2ff2674ac63f2d040346986df2b7458096d326a07c7032fbc8828",
    "0xd673290a015fdf9d5d1acb03984232839e90217de71b9e6e7e67eb8c9ac96819",
    "0x8fc84781b0716fe921ed7236bace977e9f44c55395911b4dd58f8e902bb9971d",
    "0x130718550a53fa98bb19d7e9f42d8b38a3b9ac91585e8dbc2edb2afab23c4aa5",
    "0x629ed6a4c8cabd07924beb87515ab4336a0df56ba0bbfb8e114cf8ccb68c8cbb",
    "0x603c27bf02a9b12de4bf891d342d724d436608dc3e252eb0b8250e824805fab3",
    "0x355781eb6eee3ae1e24d33408e38db465482e0abe643fa9f44b297dd725bd446",
    "0x50912ffd8d716bb6ddf362b8db936786ef78eaab481b25efa204118ec89cb4ec",
    "0xd5c7e14187a014f156959af981928ac096e8bcb74cca87c86b5ff3bcbaffc294",
]
