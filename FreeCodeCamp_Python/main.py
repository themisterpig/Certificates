def result(operator,number1,number2):
    match operator:
        case "+":
            return number1 + number2
        case "-":
            return number1 - number2

def arithmeticFormatter(lista):
    number = ["",""]
    number1=""
    lista2=[]
    operator = ""

    #print(result(operator,number1,number2))

    if len(lista) < 5:
        for count in lista:
            i=0
            number1 = ""
            for digit in count:
                if digit!= " ":
                    if digit.isdigit():
                        number1=number1+digit
                        number[i]=number1
                        if len(number1)>4:
                            print("Error: Numbers cannot be more than four digits")
                            exit()

                        continue

                    elif digit=="+" or digit =="-":
                        operator=digit
                        i=i+1
                    else:
                        if digit == "*" or digit== "/":
                            print("Error Operator must be '+' or '-'")
                        elif not digit.isdigit():
                            print("Error: Numbers must only contain digits")
                        exit()

                number1=""

            lista2.extend([number[0],operator,number1,result(operator,int(number[0]),int(number[1]))])
        x=0
        lenght = len(lista2)
        while x < len(lista2):
            for x in range(0,lenght,4):
                print(lista2[x], end="      ")
            print()
            for x in range(1,lenght,4):
                i = x + 1
                print(lista2[x] + " " + lista2[i], end= "    ")
            print()
            for x in range(0,lenght,4):
                print("-----", end="   ")
            print()
            for x in range(3,lenght,4):
                print(lista2[x], end= "      ")
            x = lenght



    else:
        print("Error: Too many problems")



arithmeticFormatter(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
