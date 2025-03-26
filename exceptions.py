"""
try:
    x =int(input("what is x?"))
    print(f"x is {x}")
   
except ValueError:
    print("x is not an integer")

"""
"""
try:
    x =int(input("what is x?"))
    
   
except ValueError:
    print("x is not an integer")


print(f"x is {x}")  #bu şekildeyken x E int dışıbda bir değer verirsek x tanımlanamamış olarak kalır ve NameError verir
"""
#bunun çıktsıı x is not an integer olur ve name error verir. NameError: name 'x' is not defined.



#try-except-else
"""
try:
    x =int(input("what is x?"))
    
   
except ValueError:
    print("x is not an integer")

else:
    print(f"x is {x}")

"""
"""

while True:
    try:
      x =int(input("what is x?"))
    
   
    except ValueError:
      print("x is not an integer")

    else:
      break  

print(f"x is {x}")"""
"""

while True:
    try:
        x = int(input("What's x? "))
        break # sadece x geçerli bir int değeri aldığında çalışır.
    except ValueError:
        print("x is not an integer")

print(f"x is {x}")
"""
def main():
    x= get_int("what is x?")
    print(f"x is {x}")
"""
def get_int():
    while True:
        try:
            x = int(input("what is x?"))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x

"""
""""
def get_int():
    while True:
        try:
            return int(input("what is x?"))
        except ValueError:
            print("x is not an integer")
       
"""



# what if i want to ignore the error? 
# with "pass" keyword , i still catch the error but i ignore it

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass






main()

