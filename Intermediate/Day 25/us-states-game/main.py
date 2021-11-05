import pandas
import turtle

STATES_FILE = "50_states.csv"
IMAGE = "blank_states_img.gif"
ALIGNMENT = "center"
FONT = ("Courier", 20, 'normal')
LEARN_CSV_FILE = "states_to_learn.csv"
TOTAL_STATES = 50


def create_states_dictionary():
    """
    creates a states dictionary from the 50_states.csv file
    :return: states dictionary
    """
    data = pandas.read_csv(STATES_FILE)
    states = {}
    for i, state_data in data.iterrows():
        state_data_list = state_data.to_list()
        state, x, y = [val for val in state_data_list]
        states[state] = (x, y)
    return states


def display_state_name(location, state):
    """
    creates a turtle that displays the state name at the location coordinates
    :param location: tuple
    :param state: string
    """
    new_state = turtle.Turtle()
    new_state.penup()
    new_state.hideturtle()
    new_state.goto(location)
    new_state.write(state)


def get_answer(screen, input_title):
    """
    retrieves answer input from player and returns answer
    :param screen: Screen object
    :param input_title: string
    :return: string state answer
    """
    try:
        return screen.textinput(input_title, "What's another state's name? (enter 'exit' to end game)").title()
    except AttributeError:
        return "_"


def show_result(score):
    """
    creates a turtle and writes the result in the center of the screen
    :param score: int
    """
    new_state = turtle.Turtle()
    new_state.hideturtle()
    new_state.penup()
    if score == TOTAL_STATES:
        message = "CONGRATULATIONS! YOU GOT ALL 50 STATES!"
    else:
        message = f"You got {score} out of the {TOTAL_STATES} states correct."
    new_state.write(message, align=ALIGNMENT, font=FONT)


def create_learn_csv(states):
    """
    creates a csv file populating with the missed states as a learning tool
    :param states: dict
    """
    state_dict = {"state": list(states.keys())}
    df = pandas.DataFrame(state_dict)
    df.to_csv(LEARN_CSV_FILE)


def us_states_game():
    """
    core function for running the game
    """
    states = create_states_dictionary()
    screen = turtle.Screen()
    screen.setup(width=725, height=491)
    screen.title("U.S. States Game")
    screen.tracer(0)
    screen.addshape(IMAGE)
    turtle.shape(IMAGE)

    game_is_on = True
    input_title = "Guess the State"
    score = 0
    while game_is_on:
        screen.update()

        if score > 0:
            input_title = f"{score}/{TOTAL_STATES} States Correct"
        answer_state = get_answer(screen, input_title)

        if answer_state == "Exit":
            show_result(score)
            create_learn_csv(states)
            game_is_on = False
        else:
            if location := states.get(answer_state):
                score += 1
                display_state_name(location, answer_state)
                states.pop(answer_state)

        if score == TOTAL_STATES:
            show_result(score)
            game_is_on = False

    screen.exitonclick()


if __name__ == "__main__":
    us_states_game()
