import subprocess

def python_tutorial():
    print("Here is a Python Tutorial")
    print("We will be using the howdoi package in Python to learn how to program in Python\n")

    questions = [
        "howdoi howdoi",
        "howdoi How to print 'Hello World!' in Python?",
        "howdoi What data types are available in Python?",
        "howdoi What math operators are available in Python?"
        "howdoi How to declare a variable in Python?",
        "howdoi How to use if statements in Python?",
        "howdoi How to use a for loop in Python?",
        "howdoi How to write a while loop in Python?",
        "howdoi How to define a function in Python?",
        "howdoi How to read a file line by line in Python?",
        "howdoi How to check if a string contains a substring in Python?",
        "howdoi How to sort a list in Python?",
        "howdoi How to iterate over a dictionary in Python?",
        "howdoi How to install packages using pip in Python?",
        "howdoi exit python",
        "howdoi check if a list is empty in python",
    ]

    for question in questions:
        print(f"Question: {question}\n")
        result = subprocess.run(question, shell=True, capture_output=True, text=True)
        print("Output:\n", result.stdout)


        '''
        You can return all answers instead of the first answer using
        all_answers = howdoi.howdoi(question, all = True)
        print(f"All Answers: {all_answers}\n")

        You can return the URL link to the solutions
        link = howdoi.howdoi(question, link = True)
        print(f"Link to Stack Overflow: {link}\n")

        '''

    print("That is an intro to using howdoi and a beginners Python tutorial. I Hope you find this helpful")
    
python_tutorial()