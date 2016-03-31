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
        difficulty = raw_input("Select your difficulty level: easy, medium or hard.")
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
            print "Please select easy, medium or hard."
    return quiz_text

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
    print quiz_text

play_game()
