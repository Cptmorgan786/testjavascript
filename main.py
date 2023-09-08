num1= input("please enter your first number:")
num2= input("please enter your second number:")
print("which operation do you want to do")
print ("A.addition")
print ("B. subtraction")
print ("C. Multiplication")
print ("D. Division")
print ("E. exponents")
choice = input("Enter your choice (A/B/C/D/E:")
num1= float(num1)
num2= float(num2)

def addition (add1, add2):
  the_sum=  add1+ add2
  print (the_sum)


def subtraction (sub1, sub2):
  the_diff= sub1 - sub2
  print(f"the difference between {sub1} and {sub2} is the {the_diff}")

subtraction(num1, num2)

def multiplication (mult1, mult2):
  the_prod= mult1 * mult2
  print (the_prod)

def division(div1, div2):
  the_divi= div1 / div2
  print (the_divi)


def exponent(exp1, exp2):
  the_exp= exp1 ** exp2
  print (the_exp)
if choice == 'A':
    addition(num1, num2)
elif choice == 'B':
    subtraction(num1, num2)
elif choice == 'C':
    multiplication(num1, num2)
elif choice == 'D':
    division(num1, num2)
elif choice == 'E':
    exponent(num1, num2)
#this is a calculator teehee
