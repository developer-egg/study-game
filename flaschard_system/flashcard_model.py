import json

class FlashcardModel:
    flashcard_data_filepath = None
    flashcard_data_as_dictionary = None
    flashcard_data_as_objects = []

    def __init__(self):
        pass

    def set_flashcard_data_filepath(self):
        self.flashcard_data_filepath = input()

    def retrieve_flashcard_data(self):
        with open(self.flashcard_data_filepath, mode="r", encoding="utf-8") as flashcard_data_json:
            self.flashcard_data_as_dictionary = json.load(flashcard_data_json)

        print(self.flashcard_data_as_dictionary)