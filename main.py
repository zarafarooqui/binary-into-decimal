#converting binary into decimal
b=input("enter a number:")
a=0
for i in b:
    a=a*2+int(i)
print(f"decimal number of {a} is {b}")