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

