# What is this Project?

This project is a console-based study game. Each time users start a new game,they play through a Pokémon-like story (or other type).

Flashcard style questions from their deck are asked during battles and periodically as they progress through the story. Correct answers lead to positive outcomes (such as having an extra attack, receiving money or a gift in the story, etc). Incorrect answers lead to negative outcomes.

Cards marked as as new, or are being learned (as opposed to review cards), lead to less severe negative consequences when wrong. They lead to more positive consequences when correct.
Cards that have been learned already lead to severe consequences when wrong, and slight benefits when correct.

New stories are generated for each new game. These are based on key "event types" and data.
For example, event types could include a beginning conflict, key plot points, a plot twist, and an ending. Key data includes antagonist names and the like. Between these event types, "random" events can happen. Think the Oregon Trail.

One of the easier ways to implement the story generation may be to have a fixed destination that the user is travelling to, with fixed destinations that act as checkpoints. Certain story elements that happen at each of these locations are pre-defined.

# Feature Roadmap

- Turned-Based Battles
- Story Generation
- Story Progressionn
- Shops
- Flashcard between necessary gameplay points.

# Battle System

- Choices
  - Attack
  - Defend
  - Use Item
  - Give up

# Story Generation

Proposed template for a story. Text in brackets indicates a variable.

1. [Bad thing] happens to [Name of the User] or his [Town Name] caused by [the Cause]. User now has to go to the [Final Location] to reverse the [Bad thing] and save the day. In the process he travels across [Road to Place 1], [Place 1], [Road to Place 2], [Place 2], and etc until the final location. The amount of places may be more or less depending on how long the user wants the story to be. Each place that the user goes to (including the roads to them) has data such as types and amount of battles, names of people he will meet, types of shops that are available in that town, village, etc. Certain requirements may be imposed on each place before the user moves on, such as "defeat so and so" or "recruit a member for your team". In this way, each place progresses towards the ending in a meaningful way.

Example story: User's town is struck by a plauge. The User is the only one capable to retrieve the cure, a special flower found only in such and such town. But the path is dangerous, there are many wild animals and fabled monsters along the way.

# How do you Progress through the Story?

User is presented with information on their current situation.
If no action is required, they simply press "proceed". In this mode, when nothing is urgent, they can choose from a list of commands, such as going to a shop, checking on your party status, etc. If action is required, they choose based on the options. This section must be fleshed out, as this mechanism is very important.

# Flashcards

Cards are either new, being learned, or are in review. The category of a card is dependent on how many times the user has gottne them right/wrong. For example, a new card is correct. It moves to the "being learned" category. The user consistently gets this card correct, it moves to the "in review" category. The user gets this card wrong mutliple types, it moves back to the "being learned" category.
