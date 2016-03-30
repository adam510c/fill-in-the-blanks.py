easy_quiz = "Easy quiz __1__, __2__, __3__."
medium_quiz = "Medium quiz __1__, __2__, __3__."
hard_quiz = "Hard quiz __1__, __2__, __3__."

def difficulty_level(level):
#allows user to select difficulty level easy, medium, hard
    diff = ""
    while (diff != "easy") or (diff != "medium") or (diff != "hard"):
        diff = raw_input("Select your difficulty level: easy, medium or hard.")
        if diff == "easy":
            quiz_text = easy_quiz
            print "You chose easy."
        if diff == "medium":
            quiz_text = medium_quiz
            print "You chose medium."
        if diff == "hard":
            quiz_text = hard_quiz
            print "You chose hard."
        else:
            print "Please select easy, medium or hard."
    return quiz_text

def guesses(number):
    while number_of_guesses :
        pass

def blank_finder(quiz_string):
    i = 0
    for word in quiz_string:
        if "__" not in word:
            return word
        else:
            i = i + 1
            return i


def play_game(quiz_string, answers):
    quiz_text = difficulty_level(level)
    #replaced = []
    quiz_string = quiz_text.split()
    for word in quiz_string:
        replacement = word_in_pos(word, parts_of_speech)
    #    if replacement != None:
    #        user_input = raw_input("Type in a: " + replacement + " ")
    #        word = word.replace(replacement, user_input)
    #        replaced.append(word)
    #    else:
            replaced.append(word)
    #replaced = " ".join(replaced)
    #return replaced
