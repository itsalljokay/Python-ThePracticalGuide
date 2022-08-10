##INITIALIZATION
#Initialize Empty Blockchain
blockchain = []

##FUNCTIONS
#Get The Last Blockchain Value
def get_last_blockchain_value():
    """
Returns the last value of the blockchain
Arguments:
    None.
"""
    #If The Blockchain Is Empty
    if len(blockchain) < 1:
        return 0

    #If Blockchain Is Not Empty (Implicit Else Statement Because Indentation)
    return blockchain[-1]

#Add Value To The Block Chain  
def add_transaction(transaction_amount, last_transaction=[1]):
    """
Add a new value to the end of the blockchain.
Arguments:
    :transaction_amount: The amount adding to the blockchain.
    :last_transaction: The last blockchain transaction (default value of [1]).
"""
    #If Blockchain Is Empty, Last Value Is Just Default Value
    if get_last_blockchain_value == None:
        last_transaction = [1]

    #If Blockchain Is Not Empty, Add Value
    blockchain.append([last_transaction, transaction_amount])

#Get Transaction Value
def get_transaction_value():
    """
Returns the input of the user as a float. Input is the next value in the blockchain.
Arguments:
    None
"""
    # Get the user input, transform it from a string to a float and store it in user_input
    user_input = float(input("Your transaction amount please: "))
    return user_input

#Get User Input
def get_user_choice():
    """
Returns the input of the user as a float.
Arguments:
    None
"""
    #Get the user's choice for the menu.
    user_input = input ("Please input your choice: ")
    return user_input

#Print Blockchain Elements
def print_blockchain_elements():
    """
Outputs the elements in blockchain list to console.
Arguments:
    None
"""
    #Output Blockchain List To Console
    for block in blockchain:
        print("Outputting Block")
        print(block)

##PROCESS

#Get Following Transaction Input(s), Add To Blockchain, And Output To Console
#Get Next Transaction Amounts
while True:
    print("Please choose an option...")
    print("1: Enter transaction amount")
    print("2: Print blockchain values")
    print("q: Quit Program")
    user_choice = get_user_choice()
    if user_choice == "1":
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())

    elif user_choice == "2":
        print_blockchain_elements()

    elif user_choice == "q":
        break

    else:
        print("Input was invalid. Please pick a value from the list.")

#Show We're Done Here
print("Done!")