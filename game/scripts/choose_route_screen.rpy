screen choose_route:
    add "BG/route_bg.png"

    hbox:
        xalign 0.5
        yalign 0.5
        yoffset 30
        spacing 20

        imagebutton:
            idle "images/logo/logo-hi-idle.png"
            hover "images/logo/logo-hi-hover.png"
            # auto "images/kana_%s.png"
            action Jump("mainkana")
            # sensitive persistent.pia == True

        imagebutton:
            idle "images/logo/logo-dkv-idle.png"
            hover "images/logo/logo-dkv-hover.png"
            action Jump("mainpia")
            

        imagebutton:
            idle "images/logo/logo-pertanian-idle.png"
            hover "images/logo/logo-pertanian-hover.png"
            # auto "images/tana_%s.png"
            action Jump("maintono")
            # sensitive persistent.pia == True
        

        imagebutton:
            idle "images/Achievement/malas.jpeg"
            hover "images/Achievement/malas.jpeg"
            action Jump("ED1")