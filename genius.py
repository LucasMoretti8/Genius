import random, time, sys, os, winsound

stream = sys.stdout
level = int
answer = ""
round = 0
turn = ""


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

frequency = 1500  # Set Frequency To 2500 Hertz
duration = 100  # Set Duration To 1000 ms == 1 second
def beep(duration=100):
    winsound.Beep(frequency, duration)



clear()

level = int(input("Selecione o número de fases >> "))
clear()

dif = int(input("Selecione a dificuldade [ 1 - FÁCIL ] // [ 2 - MÉDIO ] // [ 3 - DIFÍCIL ] // >> "))
if dif == 1:
    dif = 2
elif dif == 2:
    dif = 1
elif dif == 3:
    dif = .500


clear()
print("Começando em 3...")
beep()
time.sleep(1)
clear()
print("Começando em 3...2...")
beep()
time.sleep(1)
clear()
print("Começando em 3...2...1...")
beep()
time.sleep(1)
clear()
print("Começando em 3...2...1... JÁ!!")
beep(500)
time.sleep(1)
clear()
game = True


resultList = [] # Imprimir resultado por round
while round < level:
    answer = ""
    n = random.randint(0,9)
    n2 = str(n)
    resultList.append(n2) # Inclui o valor n2 dentro de uma lista

    for x in range(len(resultList)):
        print("[[ " + resultList[x] + " ]]")
        beep()
        time.sleep(dif)
        clear()

    clear()
    answer = input(" >> >> >> ")
    turn += n2
    #print ("Gabarito: ", turn)
    #print("Input: ", ans)
    if answer == turn:
        round += 1
        clear()
    else:
        print("GAME OVER!!","Gabarito: {}".format(turn),"Input: {}".format(answer), sep='\n')
        quit()
print("PARABÉNS!!!","Gabarito: {}".format(turn),"Input: {}".format(answer), sep='\n')
for i in range(10):
  beep(80)