#!/usr/bin/env python
# coding: utf-8

# In[8]:


import random
name= input("What is your name?")
print("Good Luck!!! ", name)  
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', ' air', 'apple','banana', 'bollywood']
word = random.choice(words)
print("Guess the character")
guesses= ' '
turn = 15
while turn > 0:
    failed=0
    for char in word:
        if char in guesses:
            print(char, end = "  ")
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("  You win")
        print("The word is" , word)
        break
        
    print()
    guess = input("guess the character:")
    guesses += guess
    if guess not in word:
        turns -=1
        print("Wrong")
        print("You have", + turns, "more guesses")
        if turns == 0:
            print("You loose")
        
    

