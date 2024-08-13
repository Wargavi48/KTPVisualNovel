label ED1:
    $ renpy.block_rollback()
    $quick_menu = True
    scene black with dissolve
    play music "audio/Dreamcatcher_v2.mp3"
    $ malas_kuliah.grant()
    "Kamu memutuskan untuk menunda kuliah di tahun ini."

    call credits from _call_credits
    return

label ending:
    $ renpy.block_rollback()
    $ quick_menu = False 
    play music "audio/Dreamcatcher_v2.mp3"
    jump credits


label credits:
    $ renpy.block_rollback()
    ## for hide quickmenu for the last part, so they don't appear at bottom
    $quick_menu = False
    $config.main_menu_music = "audio/Dreamcatcher_v2.mp3"
    # hide the textbox
    window hide

    scene background with fade

    # play music "audio/list_music/ost.mp3" fadeout 1.0

    # Find "End Credits Scroll" in extras.rpy to change text.
    
    call screen credits(123.0)

    $ persistent.credits_seen = True

    # Player can skip the credits

    label skip_credits:

        pass

    ## Re-enable the quick screen as the credits are over
    $ quick_menu = True

    #This ends the game
    return