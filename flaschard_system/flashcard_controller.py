class FlashcardController:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def introduction(self):
        self.view.display_introduction()
        self.model.set_flashcard_data_filepath()
        self.model.retrieve_flashcard_data()