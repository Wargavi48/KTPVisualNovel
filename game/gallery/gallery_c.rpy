screen gallery_c:
    tag menu
    add "images/extras/cg_bg.png"
    
    fixed:
        use gallery_navigation

        # Posisi grid ditentukan oleh xpos dan ypos
        grid 2 2 spacing 45:
            xpos 400  # Menempatkan grid di tengah horizontal layar
            ypos 125 # Menempatkan grid di tengah vertikal layar

            add gallery.make_button("kana_1", unlocked = im.Scale("images/CG/kana_awal_resize.png",700, 400), locked = "images/extras/locked.png")
            add gallery.make_button("kana_2", unlocked = im.Scale("images/CG/kana_awal_resize2.png",700, 400), locked = "images/extras/locked.png")
            
            add gallery.make_button("kana_3", unlocked = im.Scale("images/CG/kana_gift_talk.png",700, 400), locked = "images/extras/locked.png")
            add gallery.make_button("kana_4", unlocked = im.Scale("images/CG/kana_gift_smile.png",700, 400), locked = "images/extras/locked.png")