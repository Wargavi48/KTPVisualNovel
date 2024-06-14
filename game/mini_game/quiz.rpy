init python:
    import random
    import json

    questions = json.load(renpy.file("mini_game/quiz.json"))

    def select_random_question ():
        return random.sample(questions,10)

label quiz:
    $ random_questions = select_random_question()
    $ user_score = 0
    $ index = 0
    scene kelas with dissolve
    play music "audio/BGM_Kelas.mp3" fadein 1.0

    
    while index < 10:
        $ user_choice = ""
        $ random_question = random_questions[index]
        $ question_text = random_question["question"]
        $ option_a = random_question["a"]
        $ option_b = random_question["b"]
        $ option_c = random_question["c"]
        $ option_d = random_question["d"]

        "[question_text]"
        menu:
            "a. [option_a]":
                $ user_choice = option_a
                
            "b. [option_b]":
                $ user_choice = option_b

                
            "c. [option_c]":
                $ user_choice = option_c
                
            "d. [option_d]":
                $ user_choice = option_d
        
        if user_choice == random_question["answer"]:
            $ user_score += 10      
        $ index += 1

    if user_score == 100:
        $ all_correct.grant()
    if route == "kana":
        jump chapter1kana1
    elif route == "tana":
        jump chapter1tana
    elif route == "pia":
        jump chapter2piaafterquiz
                

        