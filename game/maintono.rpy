label maintono:
    $ renpy.block_rollback()
    $quick_menu = True

    show mama with dissolve
    $ mmama_name = Character("Mamah")
    "mama" "oke, sekarang mandi, sarapan, abis itu langsung ke stasiun ya buat ke Jeketi University buat daftar ulang."
    "mama" "Mama udah bilang ke temen mama yang di jakarta kalo kamu akan ngekost di tempat dia"
    mcname "Siap mah!"
    hide mama

    jump utamatono

label utamatono:
    $ renpy.block_rollback()
    
    #This ends the game
    return
