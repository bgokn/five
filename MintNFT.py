#
import json
import time

from web3 import Web3




def MintNFT(address,key):

    ABI=[{"type":"constructor","stateMutability":"nonpayable","inputs":[]},{"type":"error","name":"BatchError","inputs":[{"type":"bytes","name":"innerError","internalType":"bytes"}]},{"type":"error","name":"tipping__withdraw__OnlyAdminCanWithdraw","inputs":[]},{"type":"event","name":"OwnershipTransferred","inputs":[{"type":"address","name":"previousOwner","internalType":"address","indexed":'true'},{"type":"address","name":"newOwner","internalType":"address","indexed":'true'}],"anonymous":'false'},{"type":"event","name":"TipMessage","inputs":[{"type":"address","name":"recipientAddress","internalType":"address","indexed":'true'},{"type":"string","name":"message","internalType":"string","indexed":'false'},{"type":"address","name":"sender","internalType":"address","indexed":'true'},{"type":"address","name":"tokenAddress","internalType":"address","indexed":'true'}],"anonymous":'false'},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"MINIMAL_PAYMENT_FEE","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"PAYMENT_FEE_PERCENTAGE","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"PAYMENT_FEE_PERCENTAGE_DENOMINATOR","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"PAYMENT_FEE_SLIPPAGE_PERCENT","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"addAdmin","inputs":[{"type":"address","name":"_adminAddress","internalType":"address"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"admins","inputs":[{"type":"address","name":"","internalType":"address"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"balanceOf","inputs":[{"type":"address","name":"","internalType":"address"}]},{"type":"function","stateMutability":"payable","outputs":[],"name":"batch","inputs":[{"type":"bytes[]","name":"_calls","internalType":"bytes[]"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"changeMinimalPaymentFee","inputs":[{"type":"uint256","name":"_minimalPaymentFee","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"changePaymentFeePercentage","inputs":[{"type":"uint256","name":"_paymentFeePercentage","internalType":"uint256"},{"type":"uint256","name":"_paymentFeeDenominator","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"","internalType":"address"}],"name":"contractOwner","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"deleteAdmin","inputs":[{"type":"address","name":"_adminAddress","internalType":"address"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"getPaymentFee","inputs":[{"type":"uint256","name":"_value","internalType":"uint256"},{"type":"uint8","name":"_assetType","internalType":"enum AssetType"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"","internalType":"address"}],"name":"owner","inputs":[]},{"type":"function","stateMutability":"view","outputs":[],"name":"renounceOwnership","inputs":[]},{"type":"function","stateMutability":"payable","outputs":[],"name":"sendERC1155To","inputs":[{"type":"address","name":"_recipient","internalType":"address"},{"type":"uint256","name":"_assetId","internalType":"uint256"},{"type":"uint256","name":"_amount","internalType":"uint256"},{"type":"address","name":"_assetContractAddress","internalType":"address"},{"type":"string","name":"_message","internalType":"string"}]},{"type":"function","stateMutability":"payable","outputs":[],"name":"sendERC721To","inputs":[{"type":"address","name":"_recipient","internalType":"address"},{"type":"uint256","name":"_tokenId","internalType":"uint256"},{"type":"address","name":"_nftContractAddress","internalType":"address"},{"type":"string","name":"_message","internalType":"string"}]},{"type":"function","stateMutability":"payable","outputs":[],"name":"sendTo","inputs":[{"type":"address","name":"_recipient","internalType":"address"},{"type":"uint256","name":"","internalType":"uint256"},{"type":"string","name":"_message","internalType":"string"}]},{"type":"function","stateMutability":"payable","outputs":[],"name":"sendTokenTo","inputs":[{"type":"address","name":"_recipient","internalType":"address"},{"type":"uint256","name":"_amount","internalType":"uint256"},{"type":"address","name":"_tokenContractAddr","internalType":"address"},{"type":"string","name":"_message","internalType":"string"}]},{"type":"function","stateMutability":"pure","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"supportsInterface","inputs":[{"type":"bytes4","name":"interfaceId","internalType":"bytes4"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"transferOwnership","inputs":[{"type":"address","name":"newOwner","internalType":"address"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"withdraw","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"withdrawToken","inputs":[{"type":"address","name":"_tokenContract","internalType":"address"}]}]

    to_address = '0x0E685e48Bb85285B50E0B6aA9208AaCeaF9147fF'

    #wrapdata='0xa0712d680000000000000000000000000000000000000000000000000000000000000001'
    print(web3.eth.getBalance(address))

    nonce = web3.eth.getTransactionCount(address)

    gas = web3.eth.gasPrice
    txn_dict = {
        "data": wrapdata,

        "chainId": 59140,
        'from': address,

        'nonce': nonce,
        'to': to_address,
        'value': web3.toWei(0, 'ether'),
        'gas': 101158,
        'gasPrice': int(gas*5)
    }

    signed_txn = web3.eth.account.signTransaction(txn_dict, key)
    # 发送交易
    txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

    print(txn_hash.hex())
    return txn_hash.hex()


with open('./NewLineaAccount.json') as a:

    data=json.load(a)

data=[{"address": "0xb9832507DC6Ab88bEDF1D649a8AaCe8DB5A05CD4", "key": "e638b6cf5fa09fd5712993acc532f00306e62c7c58063f40bae2b03c6ee21849"}]
print(len(data))
for i in range(len(data)):
    try:

        # with open('./ErrorMintNFT1_2.json') as a:
        #
        #     temperror=json.load(a)

        with open('./NFT1_2.json') as b:
            temp=json.load(b)

        print(i,'+'*100)

        address=data[i]["address"]

        key=data[i]["key"]

        print(address,key)
        web3=Web3(Web3.HTTPProvider('https://rpc.goerli.linea.build'))


        txn_hash=MintNFT(address,key)

        temp.append({"address":address,"key":key,"txn_hash":txn_hash})

        with open('./NFT1_2.json','w') as c:
            json.dump(temp,c)

        time.sleep(10)

        print(i, '-' * 100)

    except Exception as e:
        print(e)

        # with open('./ErrorMintNFT1_2.json','w') as a:
        #
        #     temperror.append({"address":address,"key":key})
        #
        #     json.dump(temperror,a)

"""
0x16e491450000000000000000000000005abca791c22e7f99237fcc04639e094ffa0ccce9000000000000000000000000000000000000000000000000000221230fc1332f00000000000000000000000000000000000000000000000000000000000000600000000000000000000000000000000000000000000000000000000000000000
"""
"""
0x16e491450000000000000000000000005abca791c22e7f99237fcc04639e094ffa0ccce9000000000000000000000000000000000000000000000000000441d2765ddfc900000000000000000000000000000000000000000000000000000000000000600000000000000000000000000000000000000000000000000000000000000000
"""
"""
0x16e491450000000000000000000000005abca791c22e7f99237fcc04639e094ffa0ccce90000000000000000000000000000000000000000000000000004422cc170d3ae00000000000000000000000000000000000000000000000000000000000000600000000000000000000000000000000000000000000000000000000000000000
"""
"""
0x16e491450000000000000000000000005abca791c22e7f99237fcc04639e094ffa0ccce900000000000000000000000000000000000000000000000000044364c5bb000000000000000000000000000000000000000000000000000000000000000000600000000000000000000000000000000000000000000000000000000000000000

"""