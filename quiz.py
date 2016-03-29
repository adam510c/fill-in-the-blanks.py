quiz_text

def difficulty_level():
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
difficulty_level()
