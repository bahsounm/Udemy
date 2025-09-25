# U.S states Game
import turtle
from state_manager import StateManager
from score import Scoreboard

#------------------------------------------------------------------------------
screen = turtle.Screen()
screen.title("U.S. States Game")
image = ("blank_states_img.gif")
screen.addshape(image)
screen.setup(width=750, height=550)
turtle.shape(image)
screen.tracer(0) # for instant drawing of evetyhing this explain why the game over and tries were so slow to load
#------------------------------------------------------------------------------
state_man = StateManager()
score = Scoreboard()
#------------------------------------------------------------------------------
game_is_on = True
while game_is_on:
    screen.update()
    
    if state_man.get_states_guessed == 50:
        game_is_on = False
        score.winner()
    
    #get the users input for a state
    user_state = screen.textinput("", "Guess a State (Spelling Matters)")

    # if the user indicates exit then we stop the game
    if user_state == "Exit":
        game_is_on = False

    # if the state the user guessed is not correct then we decrement the score
    # if the user runs out of tries they lose
    if not state_man.palce_state_on_map(user_state):
        if score.get_score() > 1:
            score.decrease_score()
        else:
            score.game_over()
            game_is_on = False

# save to a csv the states that the user missed
state_man.generate_csv()