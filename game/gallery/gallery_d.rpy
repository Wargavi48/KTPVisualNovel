screen gallery_d:
    tag menu
    add "images/extras/cg_bg.png"
    
    fixed:
        use gallery_navigation

        # Posisi grid ditentukan oleh xpos dan ypos
        grid 2 1 spacing 45:
            xpos 400  # Menempatkan grid di tengah horizontal layar
            ypos 125 # Menempatkan grid di tengah vertikal layar

            add gallery.make_button("true", unlocked = im.Scale("images/CG/CG_Konser.png",1447, 817), locked = "images/extras/lockedout.png")