#### ilha do tesouro ##########

print(" ************* SEJA BEM, VINDO A ILHA DO TESOURO ************* ")

print('''         ____ _
        /////|\\
        ``````\\\
        `/`    )))
        \`,   (((
         `--- ,\\\
       ,---/ )),)))
      /  , `((  (((
      `--.   ) `__))       ________
      | |   ,-./\ \    _,-'
       \ \__,-.  \ \,-'
       /`.__,-'_,-\ `-.
      /       \____`--'____________
     |         \   Starshine
''')
decisao_1 = input('Youre at a crossroad. Where do you want to go? Type "left" or "right"')
if "left" in decisao_1:
    decisao_2 = input('Youve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.')
    if decisao_2 == "swim":
        print('vadia')
    else:
        print("judeu")
elif "right" in decisao_1:
    print("fall intro a hole.\nGame Over.")

'Youve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.'
"You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?"
"It's a room full of fire. Game Over."
"You found the treasure! You Win!"
"You enter a room of beasts. Game Over."
"You chose a door that doesn't exist. Game Over."
"You get attacked by an angry trout. Game Over."
"You fell into a hole. Game Over."