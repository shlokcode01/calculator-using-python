a=int(input("enter the value of no.1 = "))
b=int(input("enter the value of no.2 = "))
c=input("Enter the operator(+,-,*,/) = ")
match c:
    case "+" :
        print("%d + %d = %d" %(a,b,a+b))
    case "-" :
        print("%d - %d = %d" %(a,b,a-b))
    case "*" :
        print("%d * %d = %d" %(a,b,a*b))
    case "/" :
        if b!=0 :
            print("%d / %d = %d" %(a,b,a/b))
        else :
            print("can not divided by 0")
    case _ :
        print("invalid operator")