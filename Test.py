import config
from web3 import Web3

w3 = Web3(Web3.HTTPProvider(config.INFURA_URL))

print(w3.eth.block_number())


chs_adress = w3.toChecksumAddress('0xa6b9d0aa5cc6d9867c0e1ec99fbeae5d43705805')
balance = w3.eth.getBalance(chs_adress)
print(balance)

ether_balance = w3.fromWei(balance,'ether')
print(ether_balance)

transaction = w3.eth.getTransaction('0x6fc976f4d51a661360c895861cb6909a19892a9e5ed487f7d7f25f94acbc8ccc')
print(transaction)