Input = 0
Balance = 5_000

while True:
    
    print("""
    Enter 1 for Withdraw
    Enter 2 for Deposit
    Enter 3 for Check Balance
    Enter 4 for EXIT
       """)
    
    Input = int(input("Choose the operation: "))
    
    if Input == 1:
        
        Withdraw = int(input("Enter money to be withdrawn: "))
        
        if Balance>=Withdraw:
            
            Balance -= Withdraw
            print("collect your money")
            
        else:
            print("Insufficient funds.")
            
    elif Input == 2:
        
        Deposit = int(input("Enter money to be deposited: "))
        Balance += Deposit
        print("Your money has been deposited successfully")
        
    elif Input == 3:
        print("Balance: ", Balance)
        
    elif Input == 4:
        break