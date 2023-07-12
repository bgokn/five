import random
import socket
import time
import traceback

import socks
from eth_account.messages import encode_defunct
from web3 import Web3
import requests
import json


class AtticcPlatform:
    def __init__(self, ip_file='./IP_BNB.json'):
        with open(ip_file) as p:
            self.ip_list = json.load(p)
        self.web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/'))
        self.url = 'https://atticc.xyz/api/verify'
        self.gql_url = 'https://query.dev.atticc.xyz/v1/graphql'

    def verify(self, address, key):
        time_stamp = str(int(time.time() * 1000))
        message = "\nPurpose: Sign to verify wallet ownership in Atticc platform.\nWallet address: " + address + "\nNonce: " + time_stamp + "\n"
        a = encode_defunct(text=message)
        signmessage = self.web3.eth.account.sign_message(a, key)
        signmessage = str(signmessage)[-135:-3]
        print(signmessage)

        time.sleep(10)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'Content-Type': 'application/json'
        }
        payload = json.dumps({
            "signedMessage": signmessage,
            "message": message,
            "publicAddress": address
        })
        response = requests.request("POST", self.url, headers=headers, data=payload).json()

        print(response)
        return response["token"]

    def create_user(self, address, token):
        payload = json.dumps({
            "query": "\n  mutation createUser($address: String!, $domain: String, $avatar: String) {\n    insert_atticcdev_user_one(object: { address: $address, domain: $domain, avatar: $avatar }) {\n      address\n    }\n  }\n",
            "variables": {
                "address": address
            },
            "operationName": "createUser"
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        response = requests.request("POST", self.gql_url, headers=headers, data=payload)
        print(response.text)
        return response.text

    def join(self, address, token):
        payload = json.dumps({
            "query": "\n  mutation joinCommunity(\n    $communityAddress: String = \"\"\n    $userAddress: String = \"\"\n    $role: atticcdev_COMMUNITY_ROLE_enum = MEMBER\n  ) {\n    insert_atticcdev_community_membership(\n      objects: { communityAddress: $communityAddress, userAddress: $userAddress, role: $role }\n    ) {\n      returning {\n        id\n      }\n    }\n  }\n",
            "variables": {
                "role": "MEMBER",
                "communityAddress": "0xa186D739CA2b3022b966194004C6b01855D59571",
                "userAddress": address
            },
            "operationName": "joinCommunity"
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        response = requests.request("POST", self.gql_url, headers=headers, data=payload)

        print(response.text)
        return response.text

    def set_proxy(self):
        ip = random.choice(self.ip_list)
        socks.set_default_proxy(socks.SOCKS5, ip["ip"], int(ip["port"]), True, ip["user"], ip["password"])
        socket.socket = socks.socksocket


if __name__ == '__main__':


    with open('./NewLineaAccount.json') as a:

        data = json.load(a)
    i=753
    while i < len(data):
        try:

            print(i, '+' * 100)

            address = data[i]["address"]

            key = data[i]["key"]
            print(address, key)
            platform = AtticcPlatform()

            platform.set_proxy()
            time.sleep(3)
            token = platform.verify(address, key)
            time.sleep(15)
            platform.create_user(address, token)
            time.sleep(15)
            platform.join(address, token)
            socks.set_default_proxy(None)


            print(i, '-' * 100)
            i=i+1
        except Exception as e:
            print(e)
            socks.set_default_proxy(None)

            if 'requests.exceptions.ConnectionError' in traceback.format_exc():

                pass
