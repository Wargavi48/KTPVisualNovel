screen choose_route:
    add "BG/route_bg.png"

    hbox:
        xalign 0.5
        yalign 0.5
        yoffset 30
        spacing 20

        imagebutton:
            auto "images/kana_%s.png"
            action Jump("mainkana")
            sensitive persistent.pia == True

        imagebutton:
            idle "images/pia_idle.png"
            hover "images/pia_hover.png"
            action Jump("mainpia")
            

        imagebutton:
            auto "images/tana_%s.png"
            action Jump("maintono")
            sensitive persistent.pia == True
