s= True
while s:
    print("Dame la opción que quieres: (A o B)")
    serie = input()
    if serie== "A":
        s= False
        suma = 0
        print ("Dime el primer número")
        n1 = int (input())
        print ("Dime el segundo número")
        n2 = int (input())
        while n1<=n2:
            print(n1);
        n1=n1+1
        
    if serie== "B":
        s= False
        suma = 0
        print ("Dime el primer número")
        n1 = int (input())
        print ("Dime el segundo número")
        n2 = int (input())

