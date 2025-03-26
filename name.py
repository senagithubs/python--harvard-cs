import sys

#print("hello, my name is",sys.argv[0])  # terminalde python name.py dan sonra yazdığım ilk klimeyi print içindeki ifadeyle birleştirip döndürür. 1den başlayrak yazr. 0 yazarsak list index out of ragne hatasını almayız  ve hello,my name is name.py çıktısını alırız.
"""
try:
    print("hello my name is",sys.argv[1])
except IndexError:
    print("too few arguments") # list index our of range error mesajı yerine daha anlaşılır olması için bunu gönerdik"""
"""
if len(sys.argv) <2: #en az 2 keline istiyoruz
    print("too few arguments") 

print("hello my name is ",sys.argv[1])  # yine de sadece ilkini alacak
"""
"""

if len(sys.argv) <2:
    sys.exit("too few arguments" ) 
elif len(sys.argv)>2:
     sys.exit("too many arguments")

print("hello my name is",sys.argv[1])  # dosya adından sonra 1 kelime girdiğimizde çalıışır çünkü zaten default olarak sys.argv[0]da var biz buna  ek olark girdiğimiz 2. kelimeyle len() =2 şartını sağlamış olduk.


"""

if len (sys.argv) <2:
    sys.exit("too few arguments")
for arg  in sys.argv[1:]:  #ilk eleman hariç diğer elemanları alıyoruz
    print("hello my name is",arg)


#pip is a programme that allows us to download packages.
