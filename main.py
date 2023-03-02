



def printimprimeMat(n):
#valida si pasa por el rango
    if num > 9 or num < 1:
        print("no pasa")
    else:
        #incrementacion del numero insertado para que llegue a la cantidad x
        for i in range(num + 1):

            for j in range(1, i + 1):
                print(i, end="")
            print("")

        for i in range(num - 1, 0, -1):

            for j in range(i, 0, -1):
                print(i, end="")
            print("")

num = int(input("Digite un numero con rango de 1 a 9"))
printimprimeMat(num)

