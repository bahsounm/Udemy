import pandas
from turtle import Turtle

class StateManager:
    def __init__(self):
        self.states = None
        self.organize_US_states()
        self.states_guessed = []

    
    def organize_US_states(self):
        organized_states = {}
        data = pandas.read_csv("50_states.csv").to_dict()
        for idx in data["state"]:
            organized_states[data["state"][idx]] = (data["x"][idx], data["y"][idx])
        self.states = organized_states

    def get_states_guessed(self):
        return len(self.states_guessed)

    def palce_state_on_map(self, users_state):
        if users_state in self.states:
            state = Turtle()
            state.penup()
            state.hideturtle()
            state.color("black")
            state.goto(self.states[users_state])
            state.write("{}".format(users_state), font=("Arial", 8, "normal"))
            self.states_guessed.append(users_state)
            return True
        else:
            return False
        
    def generate_csv(self):
        dict_for_csv = {"State": [], "Coordinates" : []}
        for state in self.states:
            if state not in self.states_guessed:
                dict_for_csv["State"].append(state)
                dict_for_csv["Coordinates"].append(self.states[state])
        
        data = pandas.DataFrame(dict_for_csv)
        data.to_csv("States_Left_to_Guess.csv")


        