easy_quiz = "Easy quiz __1__, __2__, __3__."
medium_quiz = "Medium quiz __1__, __2__, __3__."
hard_quiz = "Hard quiz __1__, __2__, __3__."
easy_key = [a, b, c]
medium_key = [d, e, f]
hard_key = [g, h, i]

def difficulty_level(level):
#allows user to select difficulty level easy, medium, hard
    difficulty = ""
    while (difficulty != "easy") or (difficulty != "medium") or (difficulty != "hard"):
        difficulty = raw_input("Select your difficulty level: easy, medium or hard.")
        if difficulty == "easy":
            quiz_text = easy_quiz
            quiz_key = easy_key
            print "You chose easy."
        if difficulty == "medium":
            quiz_text = medium_quiz
            quiz_key = medium_key
            print "You chose medium."
        if difficulty == "hard":
            quiz_text = hard_quiz
            quiz_key = hard_key
            print "You chose hard."
        else:
            print "Please select easy, medium or hard."
    return quiz_text

def guesses(number):
    number_of_guesses = ""
    while number_of_guesses %% 1 != 0:
        number_of_guesses = raw_input('''How many guesses would you like for
        each question?''')
        return number_of_guesses

def blank_finder(quiz_string):
    for word in quiz_string:
        if "__" not in word:
            return word
        else:
            None

def play_game(quiz_string, answers):
    quiz_text = difficulty_level(level)
    number_of_guesses = guesses(number)
    print quiz_text
    quiz_string = quiz_text.split()

    for word in quiz_string:
        i = 0
        blank_number = 1
        question = blank_finder(quiz_string)
        if question == None:
            remaining_guesses = number_of_guesses
            user_guess = raw_input("What word belongs in " + str(blank_number) + "?"
            while user_guess != quiz_key[i]:
                if remaining_guesses > 1:
                    print "That's not what I was looking for."
                    remaining_guesses = remaining_guesses - 1
                    print "You have " + str(remaining_guesses) + "tries remaining."
                    ####### I'm working here!!!!! ish
                    print quiz_text
                    user_guess = raw_input("What word belongs in " + str(blank_number) + "?"
                if remaining_guesses == 1:
                    print "It's now or never Sport. This is your last chance."
                    user_guess = raw_input("What word belongs in " + str(blank_number) + "?"


            if user_guess == quiz_key[i]:
                print "You're correct!"
                quiz_string[i] = user_guess
                i = i + 1
            if (user_guess != quiz_key[i]) and remaining_guesses > 1:





    #        word = word.replace(replacement, user_input)
    #        replaced.append(word)
    #    else:
            replaced.append(word)
    #replaced = " ".join(replaced)
    #return replaced
