n = True
suma = 0
while n :
    print ("Dame un número")
    num = int(input())
    suma = suma + num
    print ("La suma es:", suma)

    if suma >= 1000:
        n = False