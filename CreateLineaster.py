#
import json
import random
import string
import time

from web3 import Web3




def MintNFT(address,key):


    to_address = '0x407972ca4683803a926a85963f28C71147c6DBdF'


    stringName = ''.join(random.choice(string.ascii_lowercase) for i in range(7))

    hex_string = str(hex(len(stringName))) + ''.join(['{:02x}'.format(ord(char)) for char in stringName])
    string2 = 'https://cdn.stamp.fyi/avatar/eth:'+address.lower()
    hex_string2 = ''.join(['{:02x}'.format(ord(char)) for char in string2])
    wrapdata = '0x07e5f9480000000000000000000000000000000000000000000000000000000000000020000000000000000000000000' + address.lower()[
                                                                                                               2:] + '00000000000000000000000000000000000000000000000000000000000000c000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000018000000000000000000000000000000000000000000000000000000000000001a0000000000000000000000000000000000000000000000000000000000000000' + hex_string[
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         2:] + '0' * (
                    129 - len(
                hex_string)) + '51' + hex_string2 + '3f733d33303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'

    print(wrapdata)
    nonce = web3.eth.getTransactionCount(address)

    gas = web3.eth.gasPrice
    txn_dict = {
        "data": wrapdata,

        "chainId": 59140,
        'from': address,

        'nonce': nonce,
        'to': to_address,
        'value': web3.toWei(0, 'ether'),
        'gas': 366512,
        'gasPrice': int(gas*5)
    }
    print(txn_dict)
    signed_txn = web3.eth.account.signTransaction(txn_dict, key)
    # 发送交易
    txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

    print(txn_hash.hex())
    return txn_hash.hex()


with open('./NewLineaAccount.json') as a:

    data=json.load(a)


for i in range(len(data)):
    try:

        with open('./ErrorMintNFT1_2.json') as a:

            temperror=json.load(a)

        with open('./CreateLineaster.json') as b:
            temp=json.load(b)

        print(i,'+'*100)

        address=data[i]["address"]

        key=data[i]["key"]

        print(address,key)
        web3=Web3(Web3.HTTPProvider('https://rpc.goerli.linea.build'))


        txn_hash=MintNFT(address,key)

        temp.append({"address":address,"key":key,"txn_hash":txn_hash})

        with open('./CreateLineaster.json','w') as c:
            json.dump(temp,c)

        time.sleep(5)

        print(i, '-' * 100)

    except Exception as e:
        print(e)

        with open('./ErrorMintNFT1_2.json','w') as a:

            temperror.append({"address":address,"key":key})

            json.dump(temperror,a)

