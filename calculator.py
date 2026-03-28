def Add(a,b):
    print('Add:',a+b)

def Subtract(a,b):
    print('Subtract:',a-b)

def Multiply(a,b): 
    print('Multiply:',a*b)

def Divide(a,b):
    print('Divide:',a/b)

while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    num = int(input("Enter your choice: "))
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    if num == 1:
        Add(a,b)
    elif num == 2:
        Subtract(a,b)
    elif num == 3:
        Multiply(a,b)
    elif num == 4:
        Divide(a,b)
    elif num == 5:
        break
    else:
        print("Invaild Input : please input your choice from 1 to 5 only")
  
