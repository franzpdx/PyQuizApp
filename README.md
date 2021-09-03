# PyQuizApp Application
This application presents the user with a series of true-or-false quiz questions. Questions are gathered from the opentdb.com API.

## User Experience

- **Example**: Here's an example of the application's interface:

In the app, the X and Checkmark buttons respond to clicks:

  ![Program Example Image](/doc/PyQuizAppPic.png)
  
## Features

* A set of true/false question are presented to the user one at a time.
* User can click the True or False button for each question.
* If the user was correct, the background behind the text turns blue for several seconds; incorrect guesses turn red instead.
* A score is displayed, showing how many questions the user correctly guessed. When the app is out of questions, the user is given a message congratulating them and stating the final score.
* The set of questions is gathered from opentdb.com using a JSON request object.
* We can modify the parameters of this JSON object to influence the set of questions - including specifying a category or changing the number of questions.
* Use this page to assist in building the JSON object: https://opentdb.com/api_config.php

## Purpose

This was an exercise in learning Python and working with JSON and APIs
This is Day 34 curriculum as part of [Angela Yu's 100 Days of Code](https://www.udemy.com/course/100-days-of-code/) course on Udemy

