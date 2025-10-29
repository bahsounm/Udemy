print('''
                                                 ::
                                .'`""::..       ::
                              :        `""::..  ::
                            :               `""::..
                          :                      `""::..
                         :                            `""::..
                        :                                 `""::..
                       :                                       .'
                      :                                      .'
                      :                                    .'
     :.              :                                   .'
     ::              :                                 .'
     |:             :                                 :
     ||             :       ____                     :
     |:.            :   ..""    ""-.                :
     ||:.           : .'            `.             :
     || `:.          :                `.          :
   __||  `""::..     :                 :.         :
.-"  :|       `""::..`:                ::.       :
     ::            `""::..            ::  .      :
     `:.                `""::..       ::   :     :           __
      `:.                    `""::.. ::_____:____:__    _.--'
   ___.-`::..                  _.-"""""             """"----....
      `--._`"::.          _.-'
               `"":: ___.-'                       
            ____--"""
            
            ''')
print("Welcome to Treasure Island!\nYour Mission is to find the trasure")

direction = input("Which direction shall we start heading? left or right:\n")

if direction == "left":
    nxt_move = input("You now have to choose between swimming accross the river or waiting for the boat? swim or wait:\n")

    if nxt_move == "wait":
        door = input("Pick precisily. Which door do you walk through? red, blue or yellow:\n")
        if door == 'red':
            print("Your were burned by fire and are now dead. GAME OVER")
        elif door == 'blue':
            print("you were eaten by beasts. GAME OVER")
        elif door == 'yellow':
            print("You Win")
        else:
            print("GAME OVER")
    else:
        print("You were sadly attacked by Trout and ar Dead. GAME OVER")
else:
    print("it seems you have fallen into a hole. GAME OVER")