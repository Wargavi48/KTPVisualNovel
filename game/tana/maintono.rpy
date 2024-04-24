# Deklarasikan backgrounds
image mc bedroom = "images/BG/bedroom.png"
image cursor tana:
    "gui/button/cursor_2.png"

#Definisikan transformasi dan alignments
define small_center = Transform(zoom=0.5, xalign=0.5)
define small_left = Transform(zoom=0.5, xalign=0.0)
define small_right = Transform(zoom=0.5, xalign=1.0)
# define config.mouse_displayable = MouseDisplayable(
#     "gui/button/cursor.png", 0, 0).add("mouse_tana", "cursor tana", 0, 0)

label maintono:
    $ malas_kuliah.grant()
    $ renpy.block_rollback()
    $quick_menu = True
    # $ default_mouse = "mouse_tana"
    show mama at small_center with dissolve
    $ mmama_name = Character("Mamah")
    "mama" "Sekarang mandi, sarapan, abis itu langsung ke stasiun ya buat ke Jeketi University buat daftar ulang."
    "mama" "Mama udah bilang ke temen mama yang di jakarta kalo kamu akan ngekost di tempat dia"
    mcname "Siap mah!"
    hide mama with dissolve

    jump utamatono

label utamatono:
    $ renpy.block_rollback()
    
    #This ends the game
    return
