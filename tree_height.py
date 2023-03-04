# Viktors Valdis Seilis
# 221RDB406  
# python3 

import sys
import threading


def compute_height(parents):
    
    st = {}
    def sk(index):

        if index == -1:
            return 0
        elif index in st:
            return st[index]

        gar  = 1+sk(parents[index])
        st [index]=gar
        return gar

    max_hight = -1
    h = len(parents)
    for f in range(h):
        max_hight=max(max_hight, sk(f))
    return max_hight


def main():
    # implement input form keyboard and from files
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    out = input("Please enter F or I :")
    if "F" in out :
        nosaukums = input()
        with open("./test/" + nosaukums, mode='r') as rinda:
         i = int(rinda.readline())
         h = list(map(int,rinda.readline().split()))
         print(compute_height(h))

    elif "I" in out:
        i = int(input())
        h = list(map(int,input().split()))
        print(compute_height(h))
    else:
        print("Error wrong simbol")
        print("Enter correct symbol F or I")
        return

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()