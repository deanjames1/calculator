import rating


# Add NumberS

def add(x, y):
    return x + y

# Subtract

def sub(x, y):
    return x - y

# Multiply

def mult(x, y):
    return x * y

# Divide 
def div(x, y):
    return x / y

print("Welcome to another boring calculator!")


breakFlag = False
breakFlagTwo = False
breakFlagThree = False

while True:
    print("Operators:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    operator = input("Select Operator (eg '1'): ")

    if operator in('1','2','3','4'):
        while True:
            try:
                num1 = float(input("Input first number: "))
            except ValueError:
                print("Not a number, please try again.")
                continue

            while True:
                try:
                    num2 = float(input("Input second number: "))
                    breakFlag = True
                except ValueError:
                    print("Not a number, please try again.")
                    continue                

                if (operator == "1"):
                    print(num1, " + ", num2, " = ", add(num1, num2) )

                elif (operator == "2"):
                    result = num1 - num2
                    print(num1, " - ", num2, " = ",  sub(num1, num2) )

                elif (operator == "3"):
                    result = num1 * num2
                    print(num1, " * ", num2, " = ",  mult(num1, num2) )

                elif (operator == "4"):
                    result = num1 / num2
                    print(num1, " / ", num2, " = ",  div(num1, num2) )

                while True:

                    next = input("Do another calculation?(y/n): ")
                    if next!= "n" and next != "y":
                        print("Invalid option!")
                        continue

                    elif next == "n":
                        print("Thanks for using the calculator!")
                        breakFlagTwo = True
                        break

                    if next == "y":
                        breakFlagThree = True
                        print("Great!")
                        break
                                    
                                                        
                if breakFlag:
                    break
            

            if breakFlagTwo:
                breakFlagThree = False
                break
            
            if breakFlagThree:
                break
                            
    if breakFlagThree:
        continue      
                
    elif operator not in ("1","2","3","4"):
        print("Invalid option")
        continue

    else:
        break
        
rating.main()
            


