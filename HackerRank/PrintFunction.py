# https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true
# he end='' argument in the print function ensures that the numbers are printed without any spaces or newlines between them.

if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end='')