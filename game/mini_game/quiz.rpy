init python:
    import random

    questions = [
        {
            "question" : "Kapan Pia berulang tahun ?",
            "a" : "30 Juli",
            "b" : "2 Juni",
            "c" : "28 Juli",
            "d" : "4 Juni",
            "answer" : "30 Juli"
        },
        {
            "question" : "Kapan Kana berulang tahun ?",
            "a" : "2 Maret",
            "b" : "5 Maret",
            "c" : "3 Maret",
            "d" : "1 Maret",
            "answer" : "1 Maret"
        },
        {
            "question" : "Kapan Tana berulang tahun ?",
            "a" : "22 April",
            "b" : "28 April",
            "c" : "27 April",
            "d" : "20 April",
            "answer" : "22 April"
        },
        {
            "question" : "Siapakah member JKT48 diluar JKT48V yang pernah collab dengan Kana ?",
            "a" : "Indira",
            "b" : "Amanda",
            "c" : "Fiony",
            "d" : "Freya",
            "answer" : "Indira"
        },
        {
            "question" : "Berapa Tinggi Pia ?",
            "a" : "1570 mm",
            "b" : "1370 mm",
            "c" : "1600 mm",
            "d" : "1500 mm",
            "answer" : "1570 mm"
        },
    ]

    def select_random_question ():
        return random.sample(questions,3)

label quiz:
    $ random_questions = select_random_question()
    $ user_score = 0
    $ index = 0
    
    while index < 3:
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
                "Kamu menjawab [user_choice]"
                
            "b. [option_b]":
                $ user_choice = option_b
                "Kamu menjawab [user_choice]"

                
            "c. [option_c]":
                $ user_choice = option_c
                "Kamu menjawab [user_choice]"
                
            "d. [option_d]":
                $ user_choice = option_d
                "Kamu menjawab [user_choice]"
        
        if user_choice == random_question["answer"]:
            $ user_score += 10      
        $ index += 1

    if user_score == 30:
        $ all_correct.grant()
    jump chapter2pia2
                

        