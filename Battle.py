from __future__ import print_function
import random
fate = None


def main():
    hold = True

    energy = 0

    op_energy = 0

    over_shield = 0

    shield_durability = 7

    sword_durability = 9

    potion_durability = 12

    while True:

        if hold:
            print("")
            print("You have three options: Sword, Shield, or Potion. The Sword reduces your opponent's life if his shield isn't up. ")
            print("You use one energy each time you use the sword. The Shield protects you from your opponent's sword. ")
            print("The Potion gives you energy to use the Sword. If the opponent uses the sword and you use the potion, you die! ")
            print("Good Luck!")

        if op_energy == 0:
            options = ['Shield', 'Potion']
            opponent_move = random.choice(options)
        elif op_energy != 0:
            options = ['Sword', 'Shield', 'Potion']
            opponent_move = random.choice(options)

        if opponent_move == 'Sword':
            op_energy -= 1

        if opponent_move == 'Potion':
            op_energy += 1

        print("")

        if shield_durability == 0:
            print("Your shield broke! You've used it too much! Because your shield is broken, your opponent")
            print("skips ahead and thrusts his sword into your face. GAME OVER")
            fate = False
            break

        if sword_durability == 0:
            print("Your sword broke! You've used it too much! Because your sword is broken, your opponent")
            print("skips ahead and thrusts his sword into your face. GAME OVER")
            fate = False
            break

        if potion_durability == 0:
            print("You have run out of potion. Seeing this, your opponent")
            print("skips ahead and thrusts his sword into your face. GAME OVER")
            fate = False
            break

        if over_shield != 5:
            if energy == 0:
                move = raw_input("What is your move? Please enter 'Shield', or 'Potion'. ")
                while move != 'Shield' and move != 'Potion':
                    while move == 'Sword':
                        move = raw_input("You are out of energy and can't use your sword! Please only enter 'Shield', or 'Potion'. ")
                    move = raw_input("Please only enter 'Shield', or 'Potion'. ")
            elif energy != 0:
                move = raw_input("What is your move? Please enter 'Sword', 'Shield', or 'Potion'. ")
                while move != 'Sword' and move != 'Shield' and move != 'Potion':
                    move = raw_input("Please only enter 'Sword', 'Shield', or 'Potion'. ")
        elif over_shield == 5:
            if energy == 0:
                move = 'Potion'
                print("Since you have used your shield too many times in a row, and you are out of energy and")
                print("cannot use your sword, the only thing you could do was drink your Potion.")
            elif energy != 0:
                move = raw_input("What is your move? Please enter 'Sword' or 'Potion'. ")
                while move != 'Sword' and move != 'Shield' and move != 'Potion':
                    while move == 'Shield':
                        move = raw_input("You have used your shield too many times in a row! Please only enter 'Sword' or 'Potion'. ")
                    move = raw_input("Please only enter 'Sword' or 'Potion'. ")

        if move == 'Shield':
            over_shield += 1
            shield_durability -= 1

        if move == 'Sword':
            energy -= 1
            over_shield = 0
            sword_durability -= 1

        if move == 'Potion':
            energy += 1
            over_shield = 0
            potion_durability -= 1

        print("")

        print("You picked: ", move)
        print("Your energy level now: ", energy)
        print("Your opponent picked: ", opponent_move)

        print("")

        if energy == 10:
            print("Your energy level is at 10! With the massive amount of energy in your body, you jump up, do a flip, and slice your opponent clean in half. You Win!")
            fate = True
            break
        elif energy == 5:
            charge = raw_input("Your energy level is at 5. You can charge at your opponent and risk either victory or death. Please pick either 'Charge' or 'Stay'. ")
            while charge != 'Charge' and charge != 'Stay':
                charge = raw_input("Please either put in 'Charge' or 'Stay'. ")
            print("")
            if charge == 'Charge':
                chargelist = ['Win', 'Die']
                answer = random.choice(chargelist)
                if answer == 'Die':
                    print("You charge ahead, but the opponent parries your attack and slices your face clean. GAME OVER!")
                    fate = False
                    break
                elif answer == 'Win':
                    print("You charge ahead, catching your opponent off guard. You ram your sword straight into his heart, killing him! You Win!")
                    fate = True
                    break
            elif charge == 'Stay':
                print("Safe Bet, not charging!")
                print("")

        if move == 'Sword' and opponent_move == 'Shield':
            print("You struck with your Sword, but your opponent blocked it!")
        elif move == 'Sword' and opponent_move == 'Sword':
            deadlock = raw_input("You both strike with your Sword, and you enter a Deadlock! Do you fall back or push on? Please enter 'Fall' or 'Push'. ")
            while deadlock != 'Fall' and deadlock != 'Push':
                deadlock = raw_input("Please only enter either 'Push' or 'Fall'. ")
            deadlock_choices = ['Fall', 'Push']
            op_deadlock = random.choice(deadlock_choices)
            print("")
            if deadlock == 'Push' and op_deadlock == 'Fall':
                print("You pushed on while your opponent fell back. In one epic swoop, you slice him with your sword and claim victory. You Win!")
                fate = True
                break
            elif deadlock == 'Push' and op_deadlock == 'Push':
                print("You try to push on, but your opponent jumps ahead and severs your head. GAME OVER!")
                fate = False
                break
            elif deadlock == 'Fall' and op_deadlock == 'Fall':
                print("You both fall back! The deadlock is over!")
            elif deadlock == 'Fall' and op_deadlock == 'Push':
                print("Your opponent pushed on and might have killed you if you had not fallen back. The deadlock is over!")
            print("")
        elif move == 'Sword' and opponent_move == 'Potion':
            print("Bingo! While your opponent was taking a potion, you struck 'em with your sword, killing him! You Win!")
            fate = True
            break
        elif move == 'Shield' and opponent_move == 'Shield':
            print("Cowards! You both used your shield!")
        elif move == 'Shield' and opponent_move == 'Sword':
            print("Your opponent went in for the kill with his sword, but you blocked it with your shield!")
        elif move == 'Shield' and opponent_move == 'Potion':
            print("While you had your shield up, your opponent took a sip of his potion!")
        elif move == 'Potion' and opponent_move == 'Shield':
            print("While your opponent used his shield, you drank some of your potion!")
        elif move == 'Potion' and opponent_move == 'Sword':
            print("Alas! While you were drinking your potion, your opponent killed you with his Sword! GAME OVER!")
            fate = False
            break
        elif move == 'Potion' and opponent_move == 'Potion':
            print("Whew! This fight is tiring! You both took a swig of your potion!")

        hold = False
    return fate