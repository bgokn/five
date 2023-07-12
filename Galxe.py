import json
import secrets
import time
from datetime import datetime, timedelta
from urllib.parse import urlencode
from uuid import uuid4

import requests
from eth_account.messages import encode_defunct
from web3 import Web3


class AuthHelper:
    def __init__(self, address, key):
        self.address = address
        self.key = key

    def generate_message(self):
        nonce = ''.join(secrets.choice('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(16))
        issued_at = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
        expiration_time = (datetime.utcnow() + timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
        message = f'galxe.com wants you to sign in with your Ethereum account:\n{self.address}\n\nSign in with Ethereum to the app.\n\nURI: https://galxe.com\nVersion: 1\nChain ID: 1\nNonce: {nonce}\nIssued At: {issued_at}\nExpiration Time: {expiration_time}'
        print(message)
        return message

    def get_token(self, message):
        url = "https://graphigo.prd.galaxy.eco/query"
        payload = json.dumps({
            "operationName": "SignIn",
            "variables": {
                "input": {
                    "address": self.address,
                    "message": message,
                    "signature": self.sign_message(message)
                }
            },
            "query": "mutation SignIn($input: Auth) {\n  signin(input: $input)\n}\n"
        })
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'Content-Type': 'application/json',
           # 'Cookie': 'AWSALB=RtJ59ZjiO8xSoeAT3R8u/re/Vxwx5LqGwBEVn8XBTJY81QhbXezQV/WQNvdnKAuS1QsesMuZtLLbAGb76Xh2c/BVAKSceROTXn26tYC/O03rTUlZd13HEHKvqkPh; AWSALBCORS=RtJ59ZjiO8xSoeAT3R8u/re/Vxwx5LqGwBEVn8XBTJY81QhbXezQV/WQNvdnKAuS1QsesMuZtLLbAGb76Xh2c/BVAKSceROTXn26tYC/O03rTUlZd13HEHKvqkPh; auth-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBZGRyZXNzIjoiMHhDNEU1Q2VCQzY2YWU2NjY0MjYxNDY5NjI1M0NFYjRDZUE3RTY1NmRmIiwiTm9uY2UiOiI2U1lOY1ZHUVlHWEdGdFNaciIsImV4cCI6MTY4OTEwMjIwNCwiSnd0RXJyb3IiOm51bGx9.B4QgxGU35oLdmoDDwetNM4-PCyUzUx3z3fgGFC-AszY'
        }
        response = requests.request("POST", url, headers=headers, data=payload).json()
        return response["data"]["signin"]

    def sign_message(self, message):
        web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/'))
        encoded_message = encode_defunct(text=message)
        signature = web3.eth.account.sign_message(encoded_message, self.key).signature.hex()
        return signature

def Verify(address,token):
    url = "https://graphigo.prd.galaxy.eco/query"

    payload = json.dumps({
        "operationName": "VerifyCredentialCondition",
        "variables": {
            "input": {
                "campaignId": "GC3W6UeFoA",
                "credentialGroupId": "1366640000",
                "address": address,
                "conditionIndex": 0
            }
        },
        "query": "mutation VerifyCredentialCondition($input: VerifyCredentialGroupConditionInput!) {\n  verifyCondition(input: $input)\n}\n"
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token,
       # 'Cookie': 'AWSALB=n84S2jNgK6f1bKRkGAajwmF8RJv65249liHQU68fS5Gi9SH9mtaWFh5xvO2tbLvmcRVToTgOT9ZbU700q744qJbnCzBiSrUl861BRcWymr+Z+65BrRuZZ73oJBnY; AWSALBCORS=n84S2jNgK6f1bKRkGAajwmF8RJv65249liHQU68fS5Gi9SH9mtaWFh5xvO2tbLvmcRVToTgOT9ZbU700q744qJbnCzBiSrUl861BRcWymr+Z+65BrRuZZ73oJBnY; auth-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBZGRyZXNzIjoiMHhDNEU1Q2VCQzY2YWU2NjY0MjYxNDY5NjI1M0NFYjRDZUE3RTY1NmRmIiwiTm9uY2UiOiI2U1lOY1ZHUVlHWEdGdFNaciIsImV4cCI6MTY4OTEwMjIwNCwiSnd0RXJyb3IiOm51bGx9.B4QgxGU35oLdmoDDwetNM4-PCyUzUx3z3fgGFC-AszY'
    }

    response = requests.request("POST", url, headers=headers, data=payload).json()

    print(response)

    return response["data"]["verifyCondition"]

def Add(address,token,param):

    url = "https://graphigo.prd.galaxy.eco/query"

    payload = json.dumps({
        "operationName": "AddTypedCredentialItems",
        "variables": {
            "input": {
                "credId": "299968308888379392",
                "operation": "APPEND",
                "items": [
                    address
                ],
                "captcha": param
            }
        },
        "query": "mutation AddTypedCredentialItems($input: MutateTypedCredItemInput!) {\n  typedCredentialItems(input: $input) {\n    id\n    __typename\n  }\n}\n"
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token,
       # 'Cookie': 'AWSALB=QauNG5T+FJwqUvldWHLWJeaGBC9P/S5AhUogvlnAGv1oOZu9EKPSoABcb0xL5ybkOvUpGrJIY8V6DRnvyT7SRA83W2eMxaW3djjWc5CSgplzQSg+a6l32vblSCHP; AWSALBCORS=QauNG5T+FJwqUvldWHLWJeaGBC9P/S5AhUogvlnAGv1oOZu9EKPSoABcb0xL5ybkOvUpGrJIY8V6DRnvyT7SRA83W2eMxaW3djjWc5CSgplzQSg+a6l32vblSCHP; auth-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBZGRyZXNzIjoiMHhDNEU1Q2VCQzY2YWU2NjY0MjYxNDY5NjI1M0NFYjRDZUE3RTY1NmRmIiwiTm9uY2UiOiI2U1lOY1ZHUVlHWEdGdFNaciIsImV4cCI6MTY4OTEwMjIwNCwiSnd0RXJyb3IiOm51bGx9.B4QgxGU35oLdmoDDwetNM4-PCyUzUx3z3fgGFC-AszY'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def get_geetest_v4_captcha(params):



    captcha_id = params['captcha_id']

    proxy = params.get('proxy')

    challenge = str(uuid4())
    client_type = 'web'
    callback = 'geetest_' + str(int(time.time() * 1000))

    query = {
        'captcha_id': captcha_id,
        'challenge': challenge,
        'client_type': client_type,
        'lang': 'en-us',
        'callback': callback
    }

    url = 'https://gcaptcha4.geetest.com/load?' + urlencode(query)
    response = requests.get(url, proxies=proxy)

    data = response.text


    json_data = json.loads(data[data.index('(') + 1:-1])['data']

    query = {
        'lot_number': json_data['lot_number'],
        'payload': json_data['payload'],
        'process_token': json_data['process_token'],
        'payload_protocol': json_data['payload_protocol'],
        'pt': json_data['pt'],
        'callback': 'geetest_' + str(int(time.time() * 1000)),
        'w': 'a529a4ca6ef0513044757ef8891073378872b8f2d9cc08a966b1dcfc3e6b89a98fbfbd07de731acb9c9480d9b976a4c449e215363b08f0a41d3fafd79a15df89fb625fb84936eb68b7989ab5ea8a91fbb7b99835fe2300c001e5c8bd26165a70382a27fe42acce7df0cd3b1924c53ee89c80c0b66c82b95e1f6d34b3b4f4bfeceb3c1b8c39dd604f75218df326ac2d695f410804f7bf9231f831716ecb9770c1057876a73dd0cf68e7bb55ea0ff27ee82d231a4971f88e9ac8ccd8a46a2cfd6d8275354f84c2e69ab50c0f9d27e21b58cc02ef43a1ce72be4b230be5f07961de602a0e26aeead68d1262a41536d2852444d9fcac3960037652f75bd33075a68c13be986b22f503006e81a635c8401a1e3e23637bf56335548f5228ff67b4bb6a02c94ccf5b0b6a279da5214c269357a1da437deacb053cd7212a07ad270b72d2cc3b7acb60a07006fa7b28f63b75213c737e3ef91fa3975e35f160cb81bf696eb49b777697945771e993c1b19eff66190199daba430ea598d0bde75547e84852bb1ac2520d191ea7cf184710392f09b50201fb7ae38d2d61a1ed36c4d3e056229a0ee8bd91fa5ff1ec85a1209a6955f969ed1ef7fba8be2d4145501ec5b6bf7531a25326ee8a1f2eb29a2e7ee056e46b6785f70cadcfaba6f0410e7c5d1d4e592ed0433609775b0ad694bb121686d49e8e0f37636a65fa476d04531c4c8b632822078880954a1d2ac5f6f22075e382f054532f21a8dcb090d87d70041b9abf24',
        'captcha_id': captcha_id,
        'client_type': client_type
    }

    url = 'https://gcaptcha4.geetest.com/verify?' + urlencode(query)
    response = requests.get(url, proxies=proxy)
    data = response.text

    json_data = json.loads(data[data.index('(') + 1:-1])
    json_data = json_data['data']['seccode']

    return {
        'captchaOutput': json_data['captcha_output'],
        'genTime': json_data['gen_time'],
        'lotNumber': json_data['lot_number'],
        'passToken': json_data['pass_token']
    }

address = ''
key = ''

auth_helper = AuthHelper(address, key)
sign_message = auth_helper.generate_message()
token = auth_helper.get_token(sign_message)

print(token)
#Verify(address,token)
params={
"captcha_id" :'244bcb8b9846215df5af4c624a750db4',
"proxy":None}
#299968308888379392
param=get_geetest_v4_captcha(params)
Add(address,token,param)
Verify(address,token)
