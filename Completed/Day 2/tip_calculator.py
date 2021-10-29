def calculate_tip(bill, n_people, tip):
    return (bill * (1 + (tip/100))) / n_people

def get_inputs():
    bill = float(input("What was the total bill? $"))
    n_people = int(input("How many people to split the bill? "))
    tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
    return bill, n_people, tip

if __name__ == "__main__":
    print('Welcome to the tip calculator!')
    bill, party_size, tip = get_inputs()
    print(f"Each person should pay: ${round(calculate_tip(bill, party_size, tip), 2)}")