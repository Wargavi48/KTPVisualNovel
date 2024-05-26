label chapter2kanastart:
    $ renpy.block_rollback()
    scene black with dissolve
    show text "{color=#FFF}Chapter II{/color}" with Pause(2.0)
    scene dream with dissolve
    play music "audio/Dreamcatcher.mp3" fadein 1.0
    jump credits