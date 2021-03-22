import random, time, sys, os
stream = sys.stdout

os.system('cls')

lvl = int
ans = ""
l = str
lvl = int(input("Selecione o número de fases >> "))
os.system('cls')

dif = int(input("Selecione a dificuldade [ 1 - FÁCIL ] // [ 2 - MÉDIO ] // [ 3 - DIFÍCIL ] // >> "))
if dif == 1:
    dif = 2
elif dif == 2:
    dif = 1
elif dif == 3:
    dif = .500


round = 0
turn = ""

os.system('cls')
print("Começando em 3...")
time.sleep(1)
os.system('cls')
print("Começando em 3...2...")
time.sleep(1)
os.system('cls')
print("Começando em 3...2...1...")
time.sleep(1)
os.system('cls')
print("Começando em 3...2...1... JÁ!!")
time.sleep(1)
os.system('cls')

while round < lvl:
    ans = ""
    n = random.randint(0,9)
    n2 = str(n)
    print("[[ " + n2 + " ]]")
    time.sleep(dif)
    os.system('cls')
    ans = input(" >> >> >> ")
    turn += n2
    #print ("Gabarito: ", turn)
    #print("Input: ", ans)
    if ans == turn:
        round += 1
        os.system('cls')
    else:
        print("GAME OVER!!")
        print("Gabarito: ", turn)
        print("Input: ", ans)
        quit()
print("PARABÉNS!!!")
print ("Gabarito: ", turn)
print("Input: ", ans)