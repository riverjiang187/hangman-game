import random

with open('wordlist.txt', 'r') as file:
    list = file.readlines()
wordbank = []
for i in list:
    wordbank.append(i[0: -1])
word = random.choice(wordbank)
guess = ['_' for i in range(len(word))]
at = 10

while at > 0:
    for i in guess:
        print(i, end=' ')
    print()
    l = input('Guess a letter: ')
    if l in word:
        for i in range(len(word)):
            if l == word[i]:
                guess[i] = l
        print('Great guess!')
    else:
        print('Wrong guess!')
        at -= 1
    print(f'Attempts left: {at}')
    if not '_' in guess:
        print(f'You win! The word is {word}!')
        exit()
print(f'You lose! The word is {word}!')