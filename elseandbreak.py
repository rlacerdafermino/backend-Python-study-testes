""" else / while"""
#Toda ves que encontramos a parava break no meio do comando else nao e executado
x = 0
while(x <= 10):
    print(x)
    x+=1
else:
    print("else executado")
while (x > 0 ):
    print(x)
    if(x == 4):
        break
    x-=1
print("print fora executado")
