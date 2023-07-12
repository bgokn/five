import json
import time

from web3 import Web3


def MintNFT(address,key):

    to_address = '0x82E0b6ADFC1A5d4eF0787Bf941e102D244A393ea'

    wrapdata='0x0d1d7ae50000000000000000000000000000000000000000000000000000000000000001'


    nonce = web3.eth.getTransactionCount(address)

    gas = web3.eth.gasPrice
    txn_dict = {
        "data": wrapdata,

        "chainId": 59140,
        'from': address,

        'nonce': nonce,
        'to': to_address,
        'value': web3.toWei(0, 'ether'),
        'gas': 199549,
        'gasPrice': gas
    }

    signed_txn = web3.eth.account.signTransaction(txn_dict, key)
    # 发送交易
    txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

    print(txn_hash.hex())


    return txn_hash.hex()

def Approve(address,key):

    to_address = '0x82E0b6ADFC1A5d4eF0787Bf941e102D244A393ea'

    wrapdata='0xa22cb465000000000000000000000000b622275862ee88848e89f3c97e3e3b39a7e1e5360000000000000000000000000000000000000000000000000000000000000001'


    nonce = web3.eth.getTransactionCount(address)

    gas = web3.eth.gasPrice
    txn_dict = {
        "data": wrapdata,

        "chainId": 59140,
        'from': address,

        'nonce': nonce,
        'to': to_address,
        'value': web3.toWei(0, 'ether'),
        'gas': 46222,
        'gasPrice': gas
    }

    signed_txn = web3.eth.account.signTransaction(txn_dict, key)
    # 发送交易
    txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

    print(txn_hash.hex())
    return txn_hash.hex()

def Stake(address,key,Mint_hash):

    to_address = '0xb622275862EE88848E89F3c97e3e3B39A7e1E536'
    MintTxn_receipt = web3.eth.getTransactionReceipt(Mint_hash)

    a = MintTxn_receipt.logs[0].topics[3].hex()[2:]

    wrapdata='0x0f48a48200000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000001'+a


    nonce = web3.eth.getTransactionCount(address)

    gas = web3.eth.gasPrice
    txn_dict = {
        "data": wrapdata,

        "chainId": 59140,
        'from': address,

        'nonce': nonce,
        'to': to_address,
        'value': web3.toWei(0, 'ether'),
        'gas': 275720,
        'gasPrice': gas
    }

    print(txn_dict)

    signed_txn = web3.eth.account.signTransaction(txn_dict, key)
    # 发送交易
    txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

    print(txn_hash.hex())
    return txn_hash.hex()

def Redeem(address,key,Mint_hash):


    to_address = '0xb622275862EE88848E89F3c97e3e3B39A7e1E536'
    MintTxn_receipt = web3.eth.getTransactionReceipt(Mint_hash)

    a = MintTxn_receipt.logs[0].topics[3].hex()[2:]

    wrapdata='0xf9afb26a00000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000001'+a

    nonce = web3.eth.getTransactionCount(address)

    gas = web3.eth.gasPrice
    txn_dict = {
        "data": wrapdata,

        "chainId": 59140,
        'from': address,

        'nonce': nonce,
        'to': to_address,
        'value': web3.toWei(0, 'ether'),
        'gas': 261101,
        'gasPrice': int(gas*2)
    }

    signed_txn = web3.eth.account.signTransaction(txn_dict, key)
    # 发送交易
    txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

    print(txn_hash.hex())
    return txn_hash.hex()


with open('./YesNFT3.json') as a:

    data=json.load(a)

for i in range(1,len(data)):
    try:
        with open('./errorNFT3.json') as b:
            errortemp=json.load(b)


        # with open('./Error3.json') as b:
        #     temp=json.load(b)

        print(i,'+'*100)

        address=data[i]["address"]

        key=data[i]["key"]

        print(address,key)
        web3=Web3(Web3.HTTPProvider('https://rpc.goerli.linea.build'))


        txn_hash=MintNFT(address,key)
        #
        # temp.append({"address":address,"key":key,"txn_hash":txn_hash})
        #
        # with open('./Error3.json','w') as c:
        #     json.dump(temp,c)
        #
        time.sleep(15)

        Approve(address, key)

        time.sleep(15)
        Mint_hash=data[i]["txn"]

        print(Mint_hash)
        Stake(address, key, Mint_hash)
        time.sleep(20)

        Redeem(address, key, Mint_hash)

        time.sleep(5)

        print(i, '-' * 100)

    except Exception as e:
        print(e)

        errortemp.append({"address": address, "key": key})

        with open('./errorNFT3.json', 'w') as c:
            json.dump(errortemp, c)
