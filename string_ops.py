
def find_nth_occurrence(substring, string, occurrence=1):
    try:
        #substring= input("Enter substring? ")
        #string=input("Enter substring? ")
        #occurrence=int(input("Enter occurrence? "))
        k=string.find(substring)
        while occurrence>1 and occurrence>1:
            k=string.find(substring,k+1)
            occurrence-=1
        return k
    except Exception as e :
        print("Kindly try again because there is a ",e.__class__,"as",e)
        
import itertools as it
def solve(a,b):
    try:
        #a= input("Enter first input? ")
        #b= input("Enter second input? ")
        if len(a) > len(b)+1:
            return False 
        elif a == "*" :
            return True
        elif a == b:
            return True
        elif "*" not in a:
            return False
        if a != "*":
            x= a.find("*")
            for i in it.chain(range(0,x),range(-1,x-len(a),-1)):
                if a[i]==b[i]:
                    w= True
                else:
                    w=False 
            return w
        else:
            return False
    except Exception as e :
        print("Kindly try again because there is a ",e.__class__,"as",e)

def solve_2(a,b):
    try:
        if len(a) > len(b)+1:
            return False 
        elif a == "*" :
            return True
        elif a == b:
            return True
        elif "*" not in a:
            return False
        else:
            x=a.split("*")
            k = a.replace("*", b[len(x[0]):len(b)-len(x[1])])
            return k == b
    except Exception as e :
        print("Kindly try again because there is a ",e.__class__,"as",e)

def is_palindrome(s):
    try:
        #s= input("Enter something to see if it is palindrome? ")
        return s.upper() == s[::-1].upper()
    except Exception as e :
        print("Kindly try again because there is a ",e.__class__,"as",e)

