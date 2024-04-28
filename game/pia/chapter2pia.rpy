label chapter2pia:
    scene black with dissolve
    show text "Chapter II\nThe Art Is You" with Pause(1.5) 
    scene black with dissolve
    play music "audio/kampus.mp3" loop fadein 1.0
    scene kampus with dissolve
    "*1 minggu kemudian"
    show pia at char_center with dissolve
    show pia_side at left with dissolve
    pia "pagiiiiiii [mcname]!!! sendirian aja. aku duduk sebelah kamu ya"
    mcname "uhh..pagi pia, oke sini"
    # insert mini game quiz
    hide pia with dissolve
    hide pia_side with dissolve
    scene black with dissolve
    show text "QUIZ TIME" with Pause(1.5) 
    scene black with dissolve
    jump quiz

label chapter2pia2:
    "Selesai ujian"
    play music "audio/ost_vocal.mp3" noloop
    jump credits