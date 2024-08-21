screen gallery_b:
    tag menu
    add "images/extras/cg_bg.png"
    
    fixed:
        use gallery_navigation

        # Posisi grid ditentukan oleh xpos dan ypos
        grid 2 2 spacing 45:
            xpos 400  # Menempatkan grid di tengah horizontal layar
            ypos 125 # Menempatkan grid di tengah vertikal layar

            add gallery.make_button("tana_1", unlocked = im.Scale("images/CG/awal_tana.png",700, 400), locked = "images/extras/locked.png")
            add gallery.make_button("tana_2", unlocked = im.Scale("images/CG/awal_tana_mc.png",700, 400), locked = "images/extras/locked.png")

            add gallery.make_button("tana_3", unlocked = im.Scale("images/CG/tana_end_smile.png",700, 400), locked = "images/extras/locked.png")
            add gallery.make_button("tana_4", unlocked = im.Scale("images/CG/tana_end_talk.png",700, 400), locked = "images/extras/locked.png")