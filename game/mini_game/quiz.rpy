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

    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Ujian.ogg" fadein 1.0
    scene kelas with Dissolve(1.0)
    
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
        stop music fadeout 1.0
        $ quick_menu = False
        scene black with Dissolve(1.0)
        play music "BGM_Kelas.ogg" fadein 1.0  volume (1.5)
        scene kelas with Dissolve(1.0)
        $ quick_menu = True
        jump kanaafterquiz
    elif route == "tana":
        if tana_route == "Good End":
            stop music fadeout 1.0
            $ quick_menu = False
            scene black with Dissolve(1.0)
            play music "BGM_Kelas.ogg" fadein 1.0  volume (1.5)
            scene kelas with Dissolve(1.0)
            $ quick_menu = True
            jump goodtanaafterquiz
        elif tana_route == "True End":
            stop music fadeout 1.0
            $ quick_menu = False
            scene black with Dissolve(1.0)
            play music "BGM_Kelas.ogg" fadein 1.0  volume (1.5)
            scene kelas with Dissolve(1.0)
            $ quick_menu = True
            jump truetanaafterquiz
    elif route == "pia":
        if pia_route == "Good End":
            stop music fadeout 1.0
            $ quick_menu = False
            scene black with Dissolve(1.0)
            play music "BGM_Kelas.ogg" fadein 1.0  volume (1.5)
            scene kelas with Dissolve(1.0)
            $ quick_menu = True
            jump goodpiaafterquiz
        elif pia_route == "True End":
            stop music fadeout 1.0
            $ quick_menu = False
            scene black with Dissolve(1.0)
            play music "BGM_Kelas.ogg" fadein 1.0  volume (1.5)
            scene kelas with Dissolve(1.0)
            $ quick_menu = True
            jump truepiaafterquiz
                

        