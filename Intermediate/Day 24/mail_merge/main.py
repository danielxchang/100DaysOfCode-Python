PLACEHOLDER = "[name]"


def create_letter(name, content):
    """
    creates the customized letter for person with name parameter and saves file to Ready to Send folder
    :param name: string
    :param content: string
    """
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as letter:
        letter_txt = content.replace(PLACEHOLDER, name)
        letter.write(letter_txt)


def mail_merge():
    """
    opens names/letters files and calls create_letter function to create customized letters for each person
    """
    with open("Input/Names/invited_names.txt", 'r') as names_file:
        names = names_file.readlines()

    with open("Input/Letters/starting_letter.txt", 'r') as template:
        content = template.read()

    letter_count = 0
    for name in names:
        create_letter(name.rstrip("\n"), content)
        letter_count += 1

    print(f"Created {letter_count} letters!")


if __name__ == "__main__":
    mail_merge()
