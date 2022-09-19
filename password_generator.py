# Gerador de Senhas
from random import randint as rd

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
         "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
         "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
specials = ["!", "@", "'", "#", "%", "&", "*", "(", ")", "-", "_", "=", "+",
            "[", "]", "{", "}", "?", ":", ";", ">", ".", "<", ","]
verificador = [True, True, True, True]
senha = ""


def rand(self, i):
    index = rd(0, i)
    global senha
    senha += self[index]


def switch(self):
    global verificador
    match self:
        case 1:
            rand(numbers, len(numbers) - 1)
            verificador[0] = False
        case 2:
            rand(lower, len(lower) - 1)
            verificador[1] = False
        case 3:
            rand(upper, len(upper) - 1)
            verificador[2] = False
        case 4:
            rand(specials, len(specials) - 1)
            verificador[3] = False


def password(self):
    global verificador
    for x in range(1, (self + 1)):
        y = rd(1, 4)
        if x >= (self / 2):
            if verificador[0]:
                rand(numbers, len(numbers) - 1)
                verificador[0] = False
                continue
            elif verificador[1]:
                rand(lower, len(lower) - 1)
                verificador[1] = False
                continue
            elif verificador[2]:
                rand(upper, len(upper) - 1)
                verificador[2] = False
                continue
            elif verificador[3]:
                rand(specials, len(specials) - 1)
                verificador[3] = False
                continue
            else:
                switch(y)
        else:
            switch(y)


print("Bem vindo ao Gerador de Senhas!")
while True:
    print("Quantos caracteres quer em sua senha? (De 8 à 16)")
    try:
        numero = int(input("-> "))
        if numero >= 8 and numero <= 16:
            break
        else:
            print("Digite um número de 8 à 16!")
            continue
    except Exception:
        print("Digite apenas números! Somente números positivos!")
        continue

password(numero)
print("Sua Senha Gerada é\n\n{}\n\n".format(senha))
