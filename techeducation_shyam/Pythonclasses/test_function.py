def my_function():
# function body
 for i in range(1,10):
         print(i)
my_function()


def add_numbers(x,y):
    return x+y

def multiply_numbers(x,y):
    return x*y

def divide_numbers(x,y):
    return x/y

def subtract_numbers(x,y):
    return x-y


def calculate_square(x,y,operation):
     if operation=="add":
         result=add_numbers(x,y)
     elif operation=="multiply":
         result=multiply_numbers(x,y)
     elif operation=="divide":
         result=divide_numbers(x,y)
     elif operation=="subtract":
         result=subtract_numbers(x,y)
     return result

x=int(input("Enter first number: "))
y=int(input("Enter second number: "))

res=calculate_square(x,y,"add")
print("Addition:",res)

res=calculate_square(x,y,"multiply")
print("Multiplication:",res)

res=calculate_square(x,y,"divide")
print("Division:",res)

res=calculate_square(x,y,"subtract")
print("Subtraction:",res)4
