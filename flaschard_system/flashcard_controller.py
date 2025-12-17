class FlashcardController:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def introduction(self):
        self.view.display_introduction()
        self.model.set_flashcard_data_filepath()
        self.model.retrieve_flashcard_data()

    def ask_question(self, question, correct_answer):
        self.view.display_question(question)
        isAnswerCorrect = self.model.process_question(question, correct_answer)
        self.view.display_answer_result(isAnswerCorrect)