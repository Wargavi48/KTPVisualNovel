# Deklarasikan backgrounds
image mc bedroom = "images/BG/bedroom.png"
image cursor kana:
    "gui/button/cursor_3.png"

#Definisikan transformasi dan alignments
define small_center = Transform(zoom=0.5, xalign=0.5)
define small_left = Transform(zoom=0.5, xalign=0.0)
define small_right = Transform(zoom=0.5, xalign=1.0)
define config.mouse_displayable = MouseDisplayable(
    "gui/button/cursor.png", 0, 0).add("mouse_kanaia", "cursor kana", 0, 0)

label mainkana:
    $ renpy.block_rollback()
    $quick_menu = True
    # $ default_mouse = "mouse_kanaia"
    show mama at small_center with dissolve
    $ mmama_name = Character("Mamah")
    "mama" "Sekarang mandi, sarapan, abis itu langsung ke stasiun ya buat ke Jeketi University buat daftar ulang."
    "mama" "Mama udah bilang ke temen mama yang di jakarta kalo kamu akan ngekost di tempat dia"
    mcname "Siap mah!"
    hide mama with dissolve

    jump utamakana

label utamakana:
    $ renpy.block_rollback()
    
    #This ends the game
    return
