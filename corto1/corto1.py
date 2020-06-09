a = 625
temp = 0
lista = []
resultado = []
def Paridad(num):
    if num%2 == 0:
        return int(num/2)
    else:
        return int(3*num+1)

def collatz(num):
    b = num
    c = 0
    while Paridad(b) != 1:
        lista.append(b)
        b = Paridad(b)
        c += 1
        if Paridad(b) == 1:
            break
    return c

for i in range(2, a + 1):
    temp = collatz(a)
    resultado = str(lista)
    fic = open("text.txt", "a")
    fic.write(resultado)
    fic.write("\n")
    fic.close()
    lista = []