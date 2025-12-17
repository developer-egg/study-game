class FlashcardView:
    def __init__(self):
        pass

    def display_introduction(self):
        print("Welcome to the flashcard program. To import your flashcard data, provide your JSON file path: \n")

    def display_question(self, question):
        print("Input the answer/meaning of this: \n")
        print(question)

    def display_answer_result(self, isCorrect):
        if isCorrect:
            print("Nice! That was the correct answer")
        else:
            print(f"Not quite! Try again.")