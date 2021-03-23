import random, time, sys, os
stream = sys.stdout

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

lvl = int
ans = ""
l = str
lvl = int(input("Selecione o número de fases >> "))
os.system('cls' if os.name == 'nt' else 'clear')

dif = int(input("Selecione a dificuldade [ 1 - FÁCIL ] // [ 2 - MÉDIO ] // [ 3 - DIFÍCIL ] // >> "))
if dif == 1:
    dif = 2
elif dif == 2:
    dif = 1
elif dif == 3:
    dif = .500


round = 0
turn = ""

clear()
print("Começando em 3...")
time.sleep(1)
clear()
print("Começando em 3...2...")
time.sleep(1)
clear()
print("Começando em 3...2...1...")
time.sleep(1)
clear()
print("Começando em 3...2...1... JÁ!!")
time.sleep(1)
clear()

resultList = [] # Imprimir resultado por round
while round < lvl:
    ans = ""
    n = random.randint(0,9)
    n2 = str(n)
    resultList.append(n2) # Inclui o valor n2 dentro de uma lista
    # print("[[ " + n2 + " ]]")
    print(*resultList) # Imprime o resultado
    time.sleep(dif)
    os.system('cls' if os.name == 'nt' else 'clear')
    ans = input(" >> >> >> ")
    turn += n2
    #print ("Gabarito: ", turn)
    #print("Input: ", ans)
    if ans == turn:
        round += 1
        clear()
    else:
        print("GAME OVER!!")
        print("Gabarito: ", turn)
        print("Input: ", ans)
        quit()
print("PARABÉNS!!!")
print ("Gabarito: ", turn)
print("Input: ", ans)
