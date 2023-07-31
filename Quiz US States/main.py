import turtle
import pandas

screen = turtle.Screen()
screen.title("US States")
screen.bgpic("blank_states_img.gif")

df = pandas.read_csv("50_states.csv")
all_states = df.state.tolist()
guessed_states = []

while len(guessed_states) < len(all_states):
    answer = screen.textinput(title=f"{len(guessed_states)}/50", prompt='Guess a State. Type "exit" to quit').title()
    
    if answer == "Exit":
        exit_confirmation = screen.textinput(title="Quit", prompt="Are you sure you wanna quit? (y/n)").lower()
        if exit_confirmation == "y":
            missing_states = []
            for state in all_states:
                if state not in guessed_states:
                    missing_states.append(state)
            states_to_learn = pandas.DataFrame(missing_states)
            states_to_learn.to_csv("states_to_learn.csv")
            break
        
    if answer in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df.state == answer]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())
        guessed_states.append(answer)




