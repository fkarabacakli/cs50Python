from random import shuffle
cards = ["jack","quenn",
         "king",]

for card in cards:
    print(card)

print("-------------------------")

shuffle(cards)
for card in cards:
    print(card)