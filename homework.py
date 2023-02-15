#print("Hello World")

def checkprime(a):
    for x in range(a):
        if x==0:
            print(str(x)+" is neither a prime nor a composite" )
            continue;
        counter=0
        for y in range(1,x-1):
            if x%y ==0:
                counter=counter+1
        if counter>1:
            print (str(x)+" is not a prime number")
        else:
            print(str(x)+ " is a prime number")

#checkprime(10)
        
