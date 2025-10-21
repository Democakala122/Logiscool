import random
import matplotlib.pyplot as plt

def rock_papar_scisors(player = True):
    if player:
        player_choice = int(input("kő(1), papír(2), olló(3)?\n"))
    else:
        player_choice = random.randint(1, 3)
    comp_choice = random.randint(1, 3)
    winner = -1
    if (player_choice == 1 and comp_choice == 3) or (player_choice == 2 and comp_choice == 1) or (player_choice == 3 and comp_choice == 1):
        winner = 1
    if player_choice == comp_choice:
        winner = 0
    return winner

wins = 0
losses = 0
ties = 0
for i in range(100):
    result = rock_papar_scisors(player= False)
    if result == 1:
        wins += 1
        print('nyertél!')
    elif result == 0:
        ties += 1
        print('Döntetlen!')
    else:
        losses += 1
        print('vesztettél!')
print(f"Győzelmek: {wins} Döntetlenek: {ties} Vesztéseg: {losses}")

def show_results_barplot():
    plt.bar(["Győzelmek", "Döntetlenek", "Vereségek"], [wins, ties, losses])
    plt.show()

show_results_barplot()

