screen gallery_a:
    tag menu
    add "images/extras/cg_bg.png"
    
    fixed:
        use gallery_navigation

        # Posisi grid ditentukan oleh xpos dan ypos
        grid 2 1 spacing 45:
            xpos 400  # Menempatkan grid di tengah horizontal layar
            ypos 125 # Menempatkan grid di tengah vertikal layar
            
            add gallery.make_button("pia_1", unlocked = im.Scale("images/CG/pia_tabrakan_normal.png", 700, 400), locked = "images/extras/locked.png")
            add gallery.make_button("pia_2", unlocked = im.Scale("images/CG/CG Pia Smile.png", 700, 400), locked = "images/extras/locked.png")
