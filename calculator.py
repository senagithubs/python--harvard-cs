"""
x=1
y=2
z=x+y
print(z)"""


#python has interactive mode. usable especially when u dont care about save ur code
#just write python to terminal to open interactive mode
""""
x=input("what is x?")
y=input("what is y?")
z =  x + y   # u can not add them in that way. computer treat them as str
print(z)"""

#we should cnovert str to int
""""
x=input("what is x?")
y=input("what is y?")
z=int(x)+int(y)   # do i really need z variable?
print(z)"""
"""

x=int(input("what is x?"))
y=int(input("what is y?"))
print(x+y)

"""

#FLOAT : number with a decimal point  # ondalıklı,kesirli sayı demek


""""
x=float(input("what isx?"))

y=float(input( "what is y?" ))

print(x+y)


# what if ı want to round to result to the nearest integer?
# round(number[, ndigits])   we will use this function # round func just takes 1 number. it s a period

# u will use ndigit part when u want to round deccimal point to nearest exc.

print(round(x+y))

"""
"""
x=float(input("what isx?"))

y=float(input( "what is y?" ))

z=round(x+y)
print(f"{z:,}") # sonucu basamaklarına virgülle ayırır.

x=float(input("what isx?"))

y=float(input( "what is y?" ))
"""
#z=round(x/y,2)   # bölme sonucunu virgülden sonra  2 basamağa yuvarlar . örneğin 0.666666 iken 0.67 yapar
#print(z)
""""
"""
"""
z= x/y
print(f"{z:.2f}")  # bu ifade de virgülden sonnrasını 2 basamağa yuvarlar
"""

#RETURN FUNCTION:


def main():
    x=int(input("whar is x?"))
    print("x squared is ", square(x))


def square(n):
    return n  * n

main()
              

              