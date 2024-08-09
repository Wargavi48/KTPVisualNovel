screen gallery_navigation:
    fixed:
        #style_prefix "gallery"
        #spacing 20
        #xoffset -10

        #textbutton "Love Interest A" action ShowMenu("gallery_a")
        imagebutton auto "images/extras/b_pia_%s.png" xpos 35 ypos 125 focus_mask True action ShowMenu("gallery_a") hovered [ Play("sound","audio/click.wav") ]
        #textbutton "Love Interest B" action ShowMenu("gallery_b") 
        imagebutton auto "images/extras/b_tana_%s.png" xpos 35 ypos 290 focus_mask True action ShowMenu("gallery_b") hovered [ Play("sound","audio/click.wav") ]
        #textbutton "Love Interest C" action ShowMenu("gallery_c")
        imagebutton auto "images/extras/b_kanaia_%s.png" xpos 35 ypos 455 focus_mask True action ShowMenu("gallery_c") hovered [ Play("sound","audio/click.wav") ]
        #textbutton "Love Interest D" action ShowMenu("gallery_d")
        imagebutton auto "images/extras/b_true_%s.png" xpos 35 ypos 620 focus_mask True action ShowMenu("gallery_d") hovered [ Play("sound","audio/click.wav") ]

        imagebutton auto "images/extras/achievement_%s.png" xpos 35 ypos 785 focus_mask True action ShowMenu("achievement_gallery") hovered [ Play("sound","audio/click.wav") ]
        
        imagebutton auto "gui/button/back_ico_%s.png" xpos 40 ypos 1010 focus_mask True action Return()

#style gallery_button_text:
    #idle_color "#808080"
    #hover_color "#E17BA2"
    #selected_color "#AA1945"
    #size 33