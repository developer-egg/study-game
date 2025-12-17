class FlashcardView:
    def __init__(self):
        pass

    def display_introduction(self):
        print("Welcome to the flashcard program. To import your flashcard data, provide your JSON file path: \n")

    def display_question(self, question: str):
        print("Input the answer/meaning of this: \n")
        print(question + "\n")

    def display_answer_result(self, isCorrect: bool):
        if isCorrect:
            print("\nNice! That was the correct answer\n")
        else:
            print(f"\nNot quite! Try again next time. \n")