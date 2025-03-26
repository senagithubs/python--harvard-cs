def main():
   # print_column(3)
   # print_row(4)

    print_square(3)

def print_column(n):
    print("#\n"*n,end="")

def print_row(width):
    print("?"*width)

def print_square(size):
    for i in range(size):
        for x in range(size):
            print("#",end="")  # pythonda print default olarak end="\n" kullanır. yeni satıra geçmemesi için bunu ezdim

        print() # print otomatik olarak \n içerir tekrar \n yazarsam içine ekstra boşluk olur!

main()
