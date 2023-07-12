import random
import socket
import time

import eth_account
import requests
import json

import socks
from web3 import Web3

def Route(address):
    url = "https://api.catalyst.exchange/prices"

    payload = json.dumps({
      "fromChainId": "534353",
      "fromAsset": "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE",
      "toChainId": "7701",
      "toAsset": "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE",
      "fromAmount": "100000000000000",
      "toAccount": address,
      "depth": 4,
      "slippage": 0.001,
      "fastQuote": True
    })
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.status_code)

    return response.json()["executionInstructions"]["inputs"]

def Tx(wrapData,key):
    w3 = Web3(Web3.HTTPProvider('https://alpha-rpc.scroll.io/l2'))

    txn_dict = {
        "data": wrapData,
        "chainId": 534353,
        'from': address,
        'nonce': w3.eth.get_transaction_count(w3.to_checksum_address(address)),
        'to': w3.to_checksum_address("0x024d061E6F6F62A744Ca816D5556cCEF8855d517"),
        'value': w3.to_wei(0.0001, 'ether'),
        'gas': 300000,
        'gasPrice': w3.eth.gas_price
    }

    signed_txn = w3.eth.account.sign_transaction(txn_dict, key)
    txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    print(txn_receipt)

with open('./NewLineaAccount.json') as a:

    data=json.load(a)
for i in range(len(data)):
    try:
        with open('./IP_BNB.json') as p:
            IPb = json.load(p)
        IP = random.choice(IPb)

        socks.set_default_proxy(socks.SOCKS5, IP["ip"], int(IP["port"]), True, IP["user"], IP["password"])
        socket.socket = socks.socksocket
        address=data[i]["address"]
        key=data[i]["key"]

        print(i,'+++++++',address)
        TempData=Route(address=address)
        wrapData='0x24856bc300000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000080000000000000000000000000000000000000000000000000000000000000000208010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000a00000000000000000000000000000000000000000000000000000000000000040'+TempData[0][2:]+'0000000000000000000000000000000000000000000000000000000000000354'+TempData[1][2:]+'000000000000000000000000'
        Tx(wrapData,key)
        print(i, '------', address)
        socks.set_default_proxy(None)

        time.sleep(5)
    except Exception as e:
        print(e)

        with open('./Error.json') as b:

            data2=json.load(b)
        data2.append(data[i])

        with open('./Error.json','w') as b:

            json.dump(data2,b)
