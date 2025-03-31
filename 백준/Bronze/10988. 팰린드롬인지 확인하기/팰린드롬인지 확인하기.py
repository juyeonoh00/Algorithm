import sys
input = sys.stdin.readline

def solution():
    s = input().strip()
    d = s[::-1]
    if d == s :
        print("1")
    else : 
        print("0")

solution()