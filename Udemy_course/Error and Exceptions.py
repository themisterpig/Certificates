try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print("Cant use ** on strings")

x = 5
y = 0

try:
    z = x/y
except ZeroDivisionError:
    print("The devisor cant be 0")
finally:
    print("Finaly")

def ask():
    while True:
        try:
            n = int(input("Input an integer: "))
        except:
            print('An error ocurred! Please try again')
            continue
        else:
            break
    print("Thank you, your number squared is: ",n**2)
ask()