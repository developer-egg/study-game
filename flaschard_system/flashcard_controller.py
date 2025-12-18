import random
class FlashcardController:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def introduction(self):
        self.view.display_introduction()
        self.model.set_flashcard_data_filepath()
        self.model.retrieve_flashcard_data()

    def ask_question(self, question: str, correct_answer: str):
        self.view.display_question(question)

        # the process_question function here takes the user input
        isAnswerCorrect = self.model.process_question(question, correct_answer)
        self.view.display_answer_result(isAnswerCorrect)

    def question_loop(self, number_of_questions: int, questions_and_answers_list: list):
        for count in range(number_of_questions):
            current_set = random.choice(questions_and_answers_list)
            current_question = current_set.question
            current_correct_answer = current_set.answer
            # print(f"Question: {current_question}, Answer: {current_correct_answer}")

            self.ask_question(current_question, current_correct_answer)