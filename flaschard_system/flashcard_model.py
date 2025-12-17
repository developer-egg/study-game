import json

class FlashcardModel:
    flashcard_data_filepath = None
    flashcard_data_as_dictionary = None
    flashcard_data_as_list = None

    def __init__(self):
        pass

    def set_flashcard_data_filepath(self):
        self.flashcard_data_filepath = input()

    def retrieve_flashcard_data(self):
        with open(self.flashcard_data_filepath, mode="r", encoding="utf-8") as flashcard_data_json:
            self.flashcard_data_as_dictionary = json.load(flashcard_data_json)

        # this makes a list with one item, a tuple. The tuple looks like this:
        # ('vocabulary', [{}, {}, {}])
        # the second item in the tuple is a list with the question/answer objects
        self.flashcard_data_as_list = list(self.flashcard_data_as_dictionary.items())
        
        # clean the list up to be only a list with the question/answer objects
        self.flashcard_data_as_list = self.flashcard_data_as_list[0][1]

    def process_question(self, question, correct_answer):
        user_answer = input()

        if correct_answer == user_answer:
            return True
        else:
            return False

        