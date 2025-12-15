from flashcard_view import FlashcardView
from flashcard_controller import FlashcardController
from flashcard_model import FlashcardModel

view = FlashcardView()
model = FlashcardModel()
controller = FlashcardController(view=view, model=model)

controller.introduction()
