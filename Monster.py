import json
import random
import socket

import requests

import  threading

import socks

from urllib3.exceptions import NewConnectionError, ProxyError
from web3 import Web3


def move(begin,last):
    while begin < last:
        try:
            i=begin
            with open("./ipnn.json") as js:
               ips = json.load(js)

            proxy = random.choice(ips)

            proxy1={
                'http':proxy["ip"]+':'+proxy["port"],
                'https': proxy["ip"] + ':' + proxy["port"]
            }
            # socks.set_default_proxy(socks.SOCKS5, proxy['ip'], int(proxy['port']))
            # socket.socket = socks.socksocket
            address=dataMonster[i]["address"]


            print("第"+str(i)+"组开始",proxy)
            Useragent={

                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
                "Accept":"application/json,text/plain.*/*",
                "Connection":"keep-alive"
            }
            r=requests.get('https://api.fusionx.finance/getfaucet?address='+address,proxies=proxy1,headers=Useragent)
            if r.status_code != 200 :
                raise  ProxyError
            text=r.text
            print(text)
            if "Transferred successfully"  in text:
                print("第"+str(i)+"组结束")

            begin=begin+1

        except ProxyError:
            pass

        except NewConnectionError:
            pass

        except Exception as e:
            begin=begin+1
            print(e)
            pass

def Select(len):
    templist = []
    for i in range(len):
        try:


            with open('./ERRORFusionXMAX.json') as a:
                data = json.load(a)
            address = data[i]["address"]
            key = data[i]["key"]

            print(address)
            # 创建web3实例
            web3 = Web3(Web3.HTTPProvider("https://rpc.testnet.mantle.xyz"))
            # 获取metamask钱包地址的BNB测试币数量
            balance = web3.eth.get_balance(address, 'latest')
            print('BIT', i, balance)

            if int(balance) == 0:
                a = {"address": address,
                     "key": key,
                     "numb": i}
                templist.append(a)
        except:
            pass
    with open("./ERRORFusionXMAX.json", 'w') as js:
        # data = json.load(js)['users']

        json.dump(templist, js)

while True:
    with open('./ERRORFusionXMAX.json') as monster:
        dataMonster=json.load(monster)

    arg1=len(dataMonster)//5
    arg2=len(dataMonster)//5*2
    arg3=len(dataMonster)//5*3
    arg4=len(dataMonster)//5*4

    # move(6781,6786)
    threading1 = threading.Thread(name='move1',target= move  , args=(0 , arg1))
    threading2 = threading.Thread(name='move2',target= move  , args=(arg1 , arg2))
    threading3 = threading.Thread(name='move3',target= move  , args=(arg2 , arg3))
    threading4 = threading.Thread(name='move4',target= move , args=(arg3 , arg4))

    threading5 = threading.Thread(name='move5',target= move  , args=(arg4 , len(dataMonster)))
    threading1.start()
    threading2.start()
    threading3.start()
    threading4.start()
    threading5.start()


    print("又一次领水完成")


    if len(dataMonster) < 4 :
        break

    Select(len(dataMonster))

    print("还有" + str(len(dataMonster)) + "没有领到水")

print("终于完成了！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！")









