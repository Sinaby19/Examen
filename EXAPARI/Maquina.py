s=True
while s:
    print("Dame la serie que quieres: (A,B,C,D)")
    serie = input()
    if serie== "A":
        s=False
        n = True
        moneda = 0
        suma = 0
        while n:
            print ("Dame las monedas")
            moneda = int(input())            
            if moneda == 10 or moneda == 50 or moneda == 100:
                suma = suma + moneda
            else:
                print("Moneda no válida")
                n = False
            if suma == 270:
                print("Compra completada")
                n = False
    
    if serie== "B":
        s=False
        n = True
        moneda = 0
        suma = 0
        while n:
            print ("Dame las monedas")
            moneda = int(input())            
            if moneda == 10 or moneda == 50 or moneda == 100:
                suma = suma + moneda
            else:
                print("Moneda no válida")
                n = False
            if suma == 340:
                print("Compra completada")
                n = False
    
    if serie== "A":
        s=False
        n = True
        moneda = 0
        suma = 0
        while n:
            print ("Dame las monedas")
            moneda = int(input())            
            if moneda == 10 or moneda == 50 or moneda == 100:
                suma = suma + moneda
            else:
                print("Moneda no válida")
                n = False
            if suma == 390:
                print("Compra completada")
                n = False