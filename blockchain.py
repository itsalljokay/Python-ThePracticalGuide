##INITIALIZATION
#Initialize Empty Blockchain
blockchain = []

##FUNCTIONS
#Get The Last Blockchain Value
"""Returns the last value of the blockchain
Arguments:
    None.
"""
def get_last_blockchain_value():
    return blockchain[-1]


#Add Value To The Block Chain
"""Add a new value to the end of the blockchain.
Arguments:
    :transaction_amount: The amount adding to the blockchain.
    :last_transaction: The last blockchain transaction (default value of [1]).
"""  
def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])

#Get User Input
"""Returns the input of the user as a float.
Arguments:
    None
"""
def get_user_input():
    # Get the user input, transform it from a string to a float and store it in user_input
    user_input = float(input("Your transaction amount please: "))
    return user_input

##PROCESS
#Get First Transaction Input And Add To Blockchain
tx_amount = get_user_input()
add_value(tx_amount)

#Get Following Transaction Input(s), Add To Blockchain, And Output To Console
#Get Next Transaction Amounts
while True:
    tx_amount = get_user_input()
    add_value(tx_amount, get_last_blockchain_value())

    #Output Blockchain List To Console
    for block in blockchain:
        print("Outputting Block")
        print(block)

#Show We're Done Here
print("Done!")