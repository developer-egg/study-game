For the game management, use the MVC design pattern.

Separate classes for the Model, View, Controller

Controller: Passes data to the model and view layers. Calls the Model and view functions.

Model: Manages data, logic calculations, etc.

View: Displays those changes

Example class:

Battle View:
Several functions that display the battle state.
For example `battle_display.show_options()`
Output: ```1. Attack 2. Defend 3. Use Item 4. Run Away

```
For this project, I can have MVC Classes for each major component (Flashcards, Battle, Story, etc). And then a Game Controller parent class that has high-level control.
```
