s= True
while s:
    print("Dame la opción que quieres: (A o B)")
    serie = input()
    if serie== "A":
        s= False
        n = int(input("¿Cuántos números vas a sumar?"))
        suma = 0
        while n > 0:
            num = int(input("Dame el número:"))
            suma = suma + num
            n = n-1
            print ("La suma total es:",suma)

        
    if serie== "B":
        s= False
        n = int(input("¿Cuántos números vas a multiplicar?"))
        multi = 1
        while n > 0:
            num = int(input("Dame el número:"))
            multi = multi * num
            n = n-1
            print ("La multiplicación total es:",multi)