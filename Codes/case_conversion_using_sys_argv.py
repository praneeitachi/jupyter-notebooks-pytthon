import sys 
if len(sys.argv) != 3:
   print("usage :")
   print("arg[1] ===> pass a string i,e 'enter the content'")
   print("arg[2] ==> must pass either lower,upper or title")
   sys.exit()
string=sys.argv[1]
string_case=sys.argv[2]
if string_case=="lower":
    print(string.lower())
elif string_case=="upper":
    print(string.upper())
else:
    print(string.title())