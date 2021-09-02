from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# File:    main.py
# Project: PyQuizApp
# Purpose: This application presents a series of true-or-false quiz question to the user
#          Questions are gathered from the API at opentdb.com
# Author:  This application is part of Angela Yu's 100 Days of Code course on udemy.
#          This instance was written and modified by Thomas Franz


# Set up our series of questions
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Set up the UI
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
