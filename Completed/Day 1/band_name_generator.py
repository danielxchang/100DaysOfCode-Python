def generate_band_name():
    print("Welcome to the Band Name Generator")
    city = input("What is the name of the city you grew up in?\n")
    pet = input("What is your pet's name?\n")
    print(f"Your band name could be {city} {pet}")

if __name__ == "__main__":
    generate_band_name()