balance = 0
def withdraw(amount):
    global balance
    try:
        if amount>balance:
            raise Exception
        else:
            balance-=amount
            print(f"Succesfully Withdraw\nBalance : {balance}")
    except:
        print("Higher amount not enough !Balace!")



def main():
    withdraw(200)
    print("Balance : ",balance)
if __name__=="__main__":
    main()