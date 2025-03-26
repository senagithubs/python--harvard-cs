"""
i =0
while i<3:
    print("meow")
    i +=1"""

"""
for i in [0,1,2]:
    print("meow")
#why might this programme not be the best solution?
# if we want a million meows its really hard to make it with that programme in that way


"""
"""
for i in range(3) : # range() : number of values u want back
    print("meow")
"""
# even if i describe i , as u see i never use it . so it is unnecessary
"""
for _ in range(3) :
    print("meow")"""

#if we really wanna be pythonic
#print("meow\n"*3,end="")    # \n for seperate new lines ,end ="" for stop last blink line


#ask to user for how many times that should meow:

# we want to be sure user gives positive values as input
"""    # 1st code for problem above
while True:
    x = int (input("how many times do u want that cat to meow?"))
    if x > 0:
        print("meow \n"*x,end="")
        break
    else:
         print("please enter a positive value ")
         continue"""

#we keep asking until we got an positive input, then code stops 

#2nd code :
"""
while True:
    n = int(input("what is n?"))
    if n >0: 
        break  # keeps asking until got a n>0  condition
for _ in range(n): 
    print("meow")"""

def main():
    x = get_number()
    meow(x)

def meow(z):
    i=0
    for _ in range(z):
        print("meow")
        

def get_number():
   
    while True:
        n =int (input("what is the number of n?"))
        if n>0:
            return n  # hem return eder hem de döngüden çıkar
        
main()

