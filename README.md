# True or False Quiz Game

This is a simple quiz game implemented in Python using OOP. It presents a set of random questions to the user and evaluates their answers.

## File Organization

1. **main.py**: This is the main file that should be executed to start the quiz game. It imports the necessary modules and runs the quiz loop.

2. **data.py**: This file contains the data used for generating questions. It provides a list of question data in the `question_data` variable.

3. **question_model.py**: This file defines the `Question` class, which represents a single question in the quiz. The class takes a question string and its corresponding correct answer as arguments.

4. **quiz_brain.py**: This file contains the `QuizBrain` class, which manages the quiz logic. It takes a list of `Question` objects as input and provides methods for progressing through the quiz, checking answers, and keeping track of the score and current question number.

## Usage

To run the quiz game, execute the `main.py` file. The code randomly selects 10 questions from the `question_data` list in `data.py` to create a question bank. Each question is represented as a `Question` object created in the `question_model.py` file. The `QuizBrain` object in `quiz_brain.py` is then initialized with the question bank.

The quiz starts with the first question, and the user is prompted to provide an answer. The program checks the answer and updates the score accordingly. The next question is presented until all the questions in the question bank are exhausted.

Finally, the program prints the completion message along with the user's final score.

## Dependencies

The code relies on the following Python modules:

- `random`: Used to randomly select questions from the `question_data`.
- `question_model`: A custom module defining the `Question` class.
- `data`: A custom module providing the `question_data` list.
- `quiz_brain`: A custom module defining the `QuizBrain` class.

Ensure that all the required files (`main.py`, `data.py`, `question_model.py`, and `quiz_brain.py`) are present in the same directory before executing the code.

## Modification

To modify the quiz, you can make changes to the `question_data` list in the `data.py` file. Add or remove questions from the list to customize the quiz content. Each question should be a dictionary with the keys `"question"` and `"correct_answer"`, representing the question string and its correct answer, respectively.

You can also tweak other aspects of the quiz game by modifying the code in the respective files (`main.py`, `question_model.py`, and `quiz_brain.py`). However, ensure that you maintain the required functionality and data structures for the quiz to work correctly.

Feel free to explore and enhance the code to add features like multiple-choice questions, time limits, or different scoring mechanisms.

## Acknowledgments

Questions in the `data.py` was generated using [Open Trivia Database API](https://opentdb.com/)