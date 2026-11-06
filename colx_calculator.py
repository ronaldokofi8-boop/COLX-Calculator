print(".........WELCOME TO COLX CALCULATOR.........")

running = input("True/False:")
while running == "True":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operators =input("enter operator(+,-,/,*) ")
    if operators =="+":
     print(num1+num2)
    elif operators =="-":
     print(num1-num2)
    elif operators == "*":
     print(num1*num2)
    elif operators =="/":
     if num2 != 0:
        print(num1/num2) 
     else:
       print("cannot divide")
    choice = input("calculate again? (yes or no): ").lower()
    if choice =="yes":
      running = "True"
    else:
        choice == "no"
        running = "False"
        print("THANKS FOR USING MY CALCULATOR")
        import sys
        sys.exit()  






