def get_add(a,b):
    aresult=a+b
    print("addition is:",aresult)
    return 10+aresult
def main() :
    a=eval(input("Enter your first num: "))
    b=eval(input("Enter your second num: "))
    #get_add(a,b)
    result=get_add(a,b)+10
    print(f"The addition of {a} and {b} is: {result}")
main()