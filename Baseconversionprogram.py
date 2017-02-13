# CALCULATOR FOR BASE CONVEWRSION OF NUMBERS.


print("1.Binary to decimal")
print("2.octal to decimal")
print("3.Hexadecimal to decimal")
print("4.Decimal to binary")
print("5.Decimal to octal")
print("6.Decimal to Hexadecimal")
print("7.Octal to Hexadecimal")
print("8.Hexadecimal to octal")
print("9.Octal to binary")
print("10.Binary to octal")
print("11.Binary to Hexadecimal")
print("12.Hexadecimal to binary")


#1.BINARY TO DECIMAL
def bnToD(x):
    flo=list(str(x).split('.')[1])
    dec=0
    q=int(x)
    j=len(str(q))
    for i in range(0, j):
        dec= dec+(q%10)*(2**(i))
        q=q//10
    flot=0
    
    le=len(flo)
    for i in range(1, le+1):
         flot=flot+ int(flo[i-1])*(2**(-i))
    if(flot!=0):
        y=str(flot).split('.')[1]
        b=str(dec)+'.'+y
    else:
        b=str(dec)
    if(x-int(x)==0):            #true means x does not contain exponent part.
        return int(float(b))
    else:                       #false, means it has.hence print whole b
        return b
    

#2.OCTAL TO DECIMAL
def ocToD(x):
    
    dec=0
    for i in range(0,len(str(x))):
        dec= dec+ ((x%10)*(8**(i)))
        x=x//10
    return dec

#3.HEXADECIMAL TO DECIMAL    
def heToD(x):
    D={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}

    a=list(x[::-1])
    summ=0; count=0
    for i in a:
        if i.isdigit():
            summ=summ+(int(i)*(16**count))
            count+=1
        else:
            summ=(summ)+(int(D.get(i))*(16**count))
            count+=1
    return summ

#4. DECIMAL TO BINARY

#So, you can either input bin nums. with decimal or without it.


def deToB(x):
    pos=abs(x)
    p= int(pos)
    b=''
    flo= pos-p
    while p>0:
        b=b+str(p%2)
        p=p//2
    b=b[::-1]
    b=b+'.'
    for i in range(5):
        b=b+ str(int(flo*2))
        flo=(flo*2)-int(flo*2)
    if(pos-int(pos)==0):
        out=int(float(b))
    else:
        out=b
    if(int(x)>0):
        return out
    else:
        return 0-out
    

    
#5. DECIMAL TO OCTAL
def deToO(x):
    b=''
    while x>0:
        b=b+str(x%8)
        x=x//8
    b=b[::-1]
    return int(b)

#6.DECIMAL TO HEXADECIMAL
def deToH(x):
    a=''
    D={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    while x>=16:
        b=x%16
        if b in D:
            a+=D.get(b)
        else:
            a+=str(b)
        x=x//16
    if x<10:
        a=a+str(x)
    else:
        a=a+D.get(x)
    a=a[::-1]
    return a

#7.OCTAL TO HEXADECIMAL 
def ocToH(x):
    a=ocToD(x)
    b=deToH(a)
    return b

#8. HEXADECIMAL TO OCTAL
def heToO(x):
    a=heToD(x)
    b=deToO(a)
    return b

#9.OCTAL TO BINARY
def ocToB(x):
    bin=''
    while x>0:
        c=x%10
        
        bin=bin+str(deToB(c))
        x=x//10
    return int(bin[::-1])

#10. BINARY TO OCTAL
def bnToO(x):
    a=bnToD(x)
    b=deToO(a)
    return b

#11.BINARY TO HEXADECIMAL
def bnToH(x):
    a=bnToD(x)
    b=deToH(a)
    return b



#12.HEXADECIMAL TO BINARY
def heToB(x):
    a=heToD(x)
    b=deToB(a)
    return b



        
        


X = int(input("\n\nEnter your choice:"))
if X==1:
    a=float(input("Enter number in binary:"))
    print("Decimal value of input is ",bnToD(a))
elif X==2:
    b=int(input("Enter number in octal:"))
    print("Decimal value of input is ",ocToD(b))
elif X==3:
    b=input("Enter number in Hexadecimal:")
    print("Decimal value of input is ",heToD(b))
elif X==4:
    a=float(input("Enter number in decimal:"))
    print("Binary value of input is ",deToB(a))
elif X==5:
    c=int(input("Enter number in decimal:"))
    print("octal value of input is ",deToO())
elif X==6:
    b=int(input("Enter number in Decimal:"))
    print("HexaDecimal value of input is ",deToH(b))
elif X==7:
    b=int(input("Enter number in octal:"))
    print("HexaDecimal value of input is ",ocToH(b))
elif X==8:
    b=input("Enter number in Hexadecimal :")
    print("Octal value of input is ",heToO(b))
elif X==9:
    a=int(input("Enter number in octal:"))
    print("Binary value of input is",ocToB(a))
elif X==10:
    a=int(input("Enter number in binary:"))
    print("Octal value of input is",bnToO(a))
elif X==11:
    b=int(input("Enter number in Binary:"))
    print("HexaDecimal value of input is ",bnToH(b))
elif X==12:
    b=input("Enter number in Hexadecimal:")
    print("Binary value of input is ",heToB(b))
