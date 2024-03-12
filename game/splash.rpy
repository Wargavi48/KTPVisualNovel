image splash_animation:

    "gui/Pictorial.png"
    xalign 0.5 yalign 0.5 alpha 0.0
    zoom 0.1
    ease_quad 7.0 alpha 1.0 zoom 0.2

image marsha_oshi:
    "gui/Logo_Kombinasi.png"
    xalign 0.5 yalign 0.5 alpha 0.0
    zoom 0.5
    ease_quad 7.0 alpha 1.0 zoom 0.2

default persistent.firstlaunch = False

image game_logo:
    "gui/Wordmark.png"
    xalign 0.5 yalign 1.0 alpha 0.0
    zoom 0.1
    ease_quad 4.0 alpha 1.0 zoom 0.2


label splashscreen:

    scene black

    $ persistent.firstlaunch = True
    
    show splash_animation
    show text "Warga Virtual 48 Present":
        xalign 0.5 yalign 0.8 alpha 0.0
        pause 5.0
        linear 1.0 alpha 1.0

    if not persistent.seen_splash:
    
        $ renpy.pause(8.5, hard = True)

        $ persistent.seen_splash = True

    else:
        
        if renpy.pause(8.5):
            jump skip_splash

    label skip_splash:

        pass
    
    scene black
    with fade

    show game_logo:
        xalign 0.5 yalign 0.0

    $ renpy.pause(2.0)

    show marsha_oshi:
        xalign 0.5 yalign 0.75 alpha 0.0
        pause 1.5
        linear 1.0 alpha 1.0 

    $ renpy.pause(6.0)

    scene black
    with fade

    $ renpy.movie_cutscene('videos/Splash_screen_hagavi_teaser.webm')

    scene white
    with fade

    return