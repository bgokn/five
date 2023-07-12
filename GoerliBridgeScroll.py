from web3 import Web3


def T(fromAddress,fromKey,Value):
    w2 = Web3(Web3.HTTPProvider('https://eth-goerli.g.alchemy.com/v2/demo'))

    ToAddress = '0xe5E30E7c24e4dFcb281A682562E53154C15D3332'
    value=w2.to_wei(Value, 'ether')


    wrapdata='0x9f8420b3'+(64-len(str(hex(value))[2:]))*'0'+str(hex(value))[2:]+ '0000000000000000000000000000000000000000000000000000000000009c40'
    gaslimit=w2.eth.estimate_gas({"from":fromAddress,"to":ToAddress,"value":w2.to_wei(Value+0.00000004, 'ether'),'data':wrapdata})

    transDict={
        "data":wrapdata,
        "from":fromAddress,
               "to":ToAddress,
               "value":w2.to_wei(Value+0.00000004, 'ether'),
               "gas":gaslimit,
               "gasPrice":w2.eth.gas_price,
               "nonce":w2.eth.get_transaction_count(fromAddress)}
    print(transDict)
    signed_txn = w2.eth.account.sign_transaction(transDict, fromKey)
    # 发送交易
    txn_hash = w2.eth.send_raw_transaction(signed_txn.rawTransaction)
    txn_receipt = w2.eth.wait_for_transaction_receipt(txn_hash)
    print(txn_receipt)



def T2(fromAddress,fromKey,Value):
    w2 = Web3(Web3.HTTPProvider('https://eth-goerli.g.alchemy.com/v2/demo'))

    ToAddress = '0x6d79Aa2e4Fbf80CF8543Ad97e294861853fb0649'
    value=w2.toWei(Value, 'ether')


    wrapdata='0x9f8420b3'+(64-len(str(hex(value))[2:]))*'0'+str(hex(value))[2:]+ '0000000000000000000000000000000000000000000000000000000000009c40'
    gaslimit=w2.eth.estimateGas({"from":fromAddress,"to":ToAddress,"value":w2.toWei(Value+0.00000004, 'ether'),'data':wrapdata})

    transDict={
        "data":wrapdata,
        "from":fromAddress,
               "to":ToAddress,
               "value":w2.toWei(Value+0.00000004, 'ether'),
               "gas":gaslimit,
               "gasPrice":w2.eth.gasPrice,
               "nonce":w2.eth.getTransactionCount(fromAddress)}
    print(transDict)
    signed_txn = w2.eth.account.signTransaction(transDict, fromKey)
    # 发送交易
    txn_hash = w2.eth.sendRawTransaction(signed_txn.rawTransaction)
    txn_receipt = w2.eth.waitForTransactionReceipt(txn_hash)
    print(txn_receipt)

