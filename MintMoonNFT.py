#
import json
import time

from web3 import Web3




def MintNFT(address,key):

    to_address = '0x6084643ca6210551390c4b6c82807106C00291ed'

    wrapdata='0x1249c58b'
    print(web3.eth.getBalance(address))

    nonce = web3.eth.getTransactionCount(address)

    gas = web3.eth.gasPrice
    txn_dict = {
        "data": wrapdata,

        "chainId": 59140,
        'from': address,

        'nonce': nonce,
        'to': web3.toChecksumAddress(to_address),
        'value': web3.toWei(0, 'ether'),
        'gas': 198442,
        'gasPrice': int(gas*2)
    }

    signed_txn = web3.eth.account.signTransaction(txn_dict, key)
    # 发送交易
    txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

    print(txn_hash.hex())
    return txn_hash.hex()


with open('./NewNFTerror2.json') as a:

    data=json.load(a)

data=[{"address": "0x16768C3C856d6727f66840015B31d5690d24b5DF", "key": "1ced1da24f4be0ec82e3120ea41f96a69798c5d330a51f30dd331b9c20930d1d"}, {"address": "0x0eF09a829d13b9135DcFDE52e34941C8bB189859", "key": "64a1df9f6289c0dfa692d68b6a3e272577f4a94b02d1d232b023a3509fc3ec54"}, {"address": "0x9Af10B9635134B25e50b2846349f55D0d899411d", "key": "103fdb6139ebb76052c1bd92f0d6998a86084e894e67ab988294ec067649053b"}, {"address": "0x05b7674FFA3299610ABC185f474d58DE470105cc", "key": "e7e3d6bec120d7c081625ef08d88044ff3c68281defc46f31000c62725c45a0c"}, {"address": "0x2De049aAC473b38e69C6bFA9988e692a3a89E6e9", "key": "221633a0c6f41e3a6f57e25341faa1447b7d5c0ba44d4cf115192851dd6c1b8a"}, {"address": "0x9B477ab778bE4382Cc232cA1d4B504498Cbb1A92", "key": "30a16959560875692629f99763462fb492ec83348f98c20c37f10d2aba9b05f3"}]
for i in range(len(data)):
    try:
        with open('./errorNFT2_1.json') as b:
            errortemp=json.load(b)

        with open('./NFT2_1.json') as b:
            temp=json.load(b)

        print(i,'+'*100)

        address=data[i]["address"]

        key=data[i]["key"]

        print(address,key)
        web3=Web3(Web3.HTTPProvider('https://rpc.goerli.linea.build'))


        txn_hash=MintNFT(address,key)

        temp.append({"address":address,"key":key,"txn_hash":txn_hash})

        with open('./NFT2_1.json','w') as c:
            json.dump(temp,c)

        time.sleep(15)

        print(i, '-' * 100)

    except Exception as e:
        print(e)

        errortemp.append({"address": address, "key": key})

        with open('./errorNFT2_1.json', 'w') as c:
            json.dump(errortemp, c)

