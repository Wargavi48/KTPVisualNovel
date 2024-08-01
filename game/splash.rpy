image splash_animation:

    "gui/Pictorial.png"
    xalign 0.5 yalign 0.5 alpha 0.0
    zoom 0.1
    ease_quad 7.0 alpha 1.0 zoom 0.2

image wargavi:
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

image disclaimer:
    "gui/disclaimer1.png"
    xalign 1 yalign 1 alpha 0.0
    ease_quad 7.0 alpha 1.0

label splashscreen:

    scene black

    $ persistent.firstlaunch = True
    
    show splash_animation
    show text "{color=#FFF}Warga Virtual 48 Present{/color}":
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

    $ renpy.pause(2.0)

    show disclaimer:
        xalign 1 yalign 1 alpha 0.0
        linear 1.0 alpha 1.0 

    $ renpy.pause(7.0)

    scene black
    with fade

    $ renpy.movie_cutscene('videos/splash-screen-v2.mpeg')

    scene white
    with fade
    pause(2.0)
    return