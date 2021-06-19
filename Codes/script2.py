import script1
def mult(a,b):
    print(f"The mul of {a} and {b} is {a*b}")
    return None
def main():
    x=10
    y=20
    mult(x,y)
    #print(dir(script1))
    script1.addition(x,y)
'''
==> the problem here is we are getting the output of script1 
==> if we want to import another function the output of that is
    also printing on script2
==> how to avoid that?
'''
if __name__ =="__main__":
    main()