easy_quiz = "Easy quiz __1__, __2__, __3__."
medium_quiz = "Medium quiz __1__, __2__, __3__."
hard_quiz = "Hard quiz __1__, __2__, __3__."
easy_key = ['alpha', 'beta', 'carrot']
medium_key = ['dog', 'echo', 'fox']
hard_key = ['ghost', 'hopper', 'icecream']


def difficulty_level():
#allows user to select difficulty level easy, medium, hard
    difficulty = ""
    while (difficulty != "easy") or (difficulty != "medium") or (difficulty != "hard"):
        difficulty = raw_input("Select your difficulty level: easy, medium or hard. ")
        difficulty = difficulty.lower()
        if difficulty == "easy":
            print "You chose easy."
            return difficulty
        if difficulty == "medium":
            print "You chose medium."
            return difficulty
        if difficulty == "hard":
            print "You chose hard."
            return difficulty
        else:
            print "Please select easy, medium or hard. "
    return quiz_text

def guesses():
    while True:
        try:
            number_of_guesses = int(raw_input('How many guesses would you like'
            ' for each question? '))
        except ValueError:
            print "Please enter a positive integer."
            continue
        if number_of_guesses < 1:
            print "Please enter a positive integer."
            continue
        else:
            print 'You will get ' + str(number_of_guesses) + ' guesses per question.'
        return number_of_guesses

def blank_finder(quiz_string):
    for word in quiz_string:
        if "__" not in word:
            return word
        else:
            None

def play_game():
    quiz_text = []
    quiz_key = []

    difficulty = difficulty_level()
    if difficulty == "easy":
        quiz_text = easy_quiz
        quiz_key = easy_key
    if difficulty == "medium":
        quiz_text = medium_quiz
        quiz_key = medium_key
    if difficulty == "hard":
        quiz_text = hard_quiz
        quiz_key = hard_key

    attempts = guesses()
    print quiz_text
    question_index = 0
    quiz_string = quiz_text.split()

    while (question_index < len(quiz_key)) and attempts > 0:
        answer = raw_input('What word belongs in blank number '
        + str(question_index + 1) + '? ')
        if attempts == 0:
            print 'You are out of guesses. Your game is over.'
            return
        if answer == quiz_key[question_index]:
            print "Correct!"
            print quiz_string
            replace = quiz_string.index('__' + str(question_index + 1) + '__') #fix puctuation error
            quiz_string[replace] = quiz_key[question_index]
            amended_text = " ".join(quiz_string)
            print amended_text
            question_index += 1
        else:
            print "Wrong!"
            attempts = attempts - 1
            if attempts == 1:
                print "It's now or never Sport. This is your last chance."
            if attempts == 0:
                print 'Peace out hombre. Your time here is done.'



play_game()
