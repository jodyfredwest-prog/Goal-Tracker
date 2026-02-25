Goal Tracker & Manifestation Journal
This is a command-line goal tracker built in Python. The purpose of this project was to practice working with lists, dictionaries, file handling, and user interaction while creating something practical that I would actually use.
The program allows users to add goals, track their progress, and receive daily affirmations.
Features
Add a new goal with a target date
View all saved goals
Mark goals as completed
Receive a random daily affirmation
Save goals to a JSON file so progress is not lost
How It Works
When the program starts, it checks if a goals.json file exists. If it does, the saved goals are loaded into the program. If not, it starts with an empty list.
Users interact with the program through a menu system. Each goal is stored as a dictionary inside a list, including:
Goal description
Target date
Status (In Progress or Completed)
Whenever a goal is added or updated, the program saves the data back to the JSON file.
Concepts Practiced
This project helped me strengthen my understanding of:
Lists and dictionaries
Loops and conditionals
File I/O with JSON
Input validation
Updating data inside a list
Future Improvements
Some ideas I may add later:
Ability to delete or edit goals
Countdown to deadline
Sorting goals by date
A simple GUI version
Why I Built This
I wanted to create a small but functional application that demonstrates real data handling and user interaction. This project reflects my progress in learning Python and building structured programs beyond basic exercises.
