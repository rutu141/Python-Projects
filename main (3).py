logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)
#Calculator

#to add
def add(n1,n2):
  return n1+n2

#Substract
def sub(n1,n2):
  return n1-n2

#Multiply

def multiply(n1,n2):
  return n1*n2

#Divide
def div(n1,n2):
  return n1/n2

operation_dictionary={
  "+":add,
  "-":sub,
  "*":multiply,
  "/":div,
}
n1=int(input("What is the first number ? "))


for key in operation_dictionary:
  print(key)

operation=input("Pick an operation from the above lines : ")
n2=int(input("what is the second number ? "))
result=operation_dictionary[operation](n1,n2)
print(f"{n1} {operation} {n2} = {result}")

choice=input("Do you want to continue the operation y/n ? :")

while choice=="y":
 
  operation=input("Pick another symbol :")
  num3=int(input("What is the number ? : "))
  f_result=operation_dictionary[operation](result,num3)
  print(f"{result} {operation} {num3} = {f_result}")
  result=f_result
  choice=input("Do you want to continue the operation y/n ? :")
