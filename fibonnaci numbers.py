## Printing fibonacci numbers

loop_num = input("Enter how many numbers in the fibonnaci number sequence you want: ")
loop_num = int(loop_num)

def fib_seq(n):
    if n<= 1:
        return n
    else:
        return(fib_seq(n-1) + fib_seq(n-2))


for i in range(loop_num):
    print(fib_seq(i))
    
