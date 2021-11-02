class QuizBrain:
    """
    models the quiz brain and its functionality
    """
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        """
        checks if there are any more questions
        :return: bool True or False
        """
        return self.question_number < len(self.question_list)

    def retrieve_answer(self, q):
        """
        retrieves and ensures user's answer is valid
        :param q: Question object
        :return: string user answer 'true' or 'false'
        """
        while True:
            answer = input(f"Question #{self.question_number}: {q.text} True or False? ").lower()
            if answer in ['true', 'false']:
                return answer

    def next_question(self):
        """
        presents next question to the user
        """
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = self.retrieve_answer(current_q)
        self.check_answer(user_answer, current_q.answer)

    def check_answer(self, user_answer, correct_answer):
        """
        checks the user's answer by comparing to correct answer and updates score if correct
        :param user_answer: string
        :param correct_answer: string
        """
        if correct_answer.lower() == user_answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
