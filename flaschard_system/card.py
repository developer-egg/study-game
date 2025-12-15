class Card:
    last_reviewed = None
    correct_count = 0
    incorrect_count = 0
    # other statuses are learning, review
    status = "new"
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer