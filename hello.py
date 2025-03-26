#ask user for their name
#name = input("what is your name?")
#input otomatik olarak string türde alır , diğer türde istiyorsak inputun önünde tür değiştirme yapılır
#say hello to the user
"""
print("hello,",name)
"""
"""
yorum paragrafı
"""
#docs.python.org
""""
print("hello,",end="") # enf default olarak \n olarak tanımlı , burada olduğu gibi farklı şekilde de sonlandırabiliriz
print(name)
"""


#print("hello",name,sep="???") 
#print(f"hello,{name}")

# using " " in the print 
#print('hello,"friend"')


#name = name.strip() #remove whitespace from str

#capitalize users name
#name = name.title() # yazdığın her şeyin ilk harfiini büyük  yapar

# name=name.capitalize()  #sadece ilk kelimenin ilk harfini büyük yapar

#remove whitespace from str and capitalize users namw
#name= name.strip().title()  # bu şekilde ikisini bir araada kullanabiliriz
# peki bunların hepsini input kısmında tek satırda halledersek?
"""
name= input ("what is your name?").strip().title()
#split users name into first name and last name #split:seperates
first,last = name.split("")  

print(f"hello,{first}")

"""

#FUNCTIONS
"""

def hello(to):
    print("hello",to)

name= input("what is your name?")
hello(name)

 """
""""
def hello (to="world"):
    print("hello",to)

hello()
name=input("what is ur name")
hello(name)
"""
# daha aşağıda tanımladığımız fonksiyonu fonksiyonun içinde çağırıp kullanabiliyoruz.

""""
Fonksiyonlar tanımlandığında hemen çalışmaz, sadece belleğe alınır.
Fonksiyonlar çağrıldığında, Python onları yukarıda ya da aşağıda fark etmeksizin bellekte bulur ve çalıştırır.
Önemli olan, çağrıldığında fonksiyonun tanımlı olmasıdır.
"""
# burada sorun nerede?
#bu kod hello fonk içinde name olmadığı için çalışmaz , name i global tanımlarsan çalışır
"""
def main():
    name=input("what is your name?")
    hello(name)

def hello():
    print("hello,",name)

main()
"""



