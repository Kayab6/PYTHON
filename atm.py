print("welcome to atm")

amt=5000

pin="1234"
enter_pin=input("enter ur pin:")
if enter_pin==pin:
    print("welcome user")
def menu():
    print("1, DEPOSIT AMT")
    print("2, WITHDRAW AMT")
    print("3, CHANGE PIN")
    print("4, EXIT")
    

def deposit():
    global amt
    deposit_money=int(input("enter amt to be deposited"))
    amt=amt+deposit_money
    print("ur current balance=",amt)

def withdraw():   
    global amt
    withdraw_money=int(input("how much to be withdrawn; Rs."))
    amt=amt-withdraw_money
    print("ur current balance=",amt)

def pin_change():
    #to change pin   
    global pin
    old_pin = input("Enter current PIN: ")
    if old_pin!= pin:
        print("Incorrect PIN!")
        return
    
    new_pin = input("Enter new PIN (4 digits): ")
    if len(new_pin)!= 4 or not new_pin.isdigit():
        print("PIN must be 4 digits!")
        return
    
    confirm_pin = input("Confirm new PIN: ")
    if new_pin == confirm_pin:
        print("PIN changed successfully!")
        pin = new_pin  # Update global pin
    else:
        print("PINs don't match!")


#now here is the main code we have defined functions but do they work

while True:
    menu()
    choice=int(input("wat u want to do"))

    if choice==1:
        deposit()
    elif choice==2:
        withdraw()
    elif choice==3:
        pin_change()
    elif choice == 4:
        print("Thank you for using ATM!")
        break
    else:
        print("Invalid option! Try again.")       




