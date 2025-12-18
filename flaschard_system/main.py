from flashcard_view import FlashcardView
from flashcard_controller import FlashcardController
from flashcard_model import FlashcardModel

view = FlashcardView()
model = FlashcardModel()
controller = FlashcardController(view=view, model=model)

controller.introduction()
# controller.ask_question("What color is the sky?", "blue")
controller.question_loop(3, model.card_objects_list)
