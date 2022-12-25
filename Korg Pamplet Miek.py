#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

while True:
    user_action = input("Enter a choice (Korg, Pamplet, or Miek): ")
    possible_actions = ["Korg", "Pamplet", "Miek"]
    computer_action = random.choice(possible_actions)
    print("You chose, {}, computer chose, {}".format(user_action,computer_action))

    if user_action == computer_action:
        print("Both players selected," ,user_action, ", It's a tie!")
    elif user_action == "Korg":
        if computer_action == "Miek":
            print("Korg beats Miek! But only for the sake of the game, they are besties in real life!")
        else:
            print("Pamplet beats Korg! because he didn't print enough of them, and now his mom abandoned him")
    elif user_action == "Pamplet":
        if computer_action == "Korg":
            print("Pamplet covers Korg! Wow, you choose to beat Korg despite knowing the guy")
        else:
            print("Miek cuts Pamplet! Proves it to Korg why he is his bestie. Korg's mom stays.")
    elif user_action == "Miek":
        if computer_action == "Pamplet":
            print("Miek cuts Pamplet! and proves it to Korg why he is is bestie. Korg's mom stays.")
        else:
            print("Korg beats Miek! But only for the sake of the game, they are besties in real life!")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break


# In[ ]:




