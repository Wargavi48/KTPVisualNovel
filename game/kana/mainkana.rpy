# Deklarasikan backgrounds
image mc bedroom = "images/BG/bedroom.png"
# image cursor kana:
#     "gui/button/cursor_3.png"

#Definisikan transformasi dan alignments
define small_center = Transform(zoom=0.5, xalign=0.5)
define small_left = Transform(zoom=0.5, xalign=0.0)
define small_right = Transform(zoom=0.5, xalign=1.0)
# define config.mouse_displayable = MouseDisplayable(
#     "gui/button/cursor.png", 0, 0).add("mouse_kanaia", "cursor asa", 0, 0)

label mainkana:
    $ renpy.block_rollback()
    $quick_menu = False
    # $ default_mouse = "mouse_kanaia"
    scene black with dissolve
    show text "{color=#FFF}Chapter I{/color}" with Pause(1.5)
    "Hari baru sudah dimulai"
    "Lembaran baru di hidupku pun akhirnya terbuka dan akhirnya aku telah memasuki jenjang masuk kuliah"
    "disini aku memilih jurusan HI dan hari ini hari dimana aku datang di Jakarta"

    scene black with dissolve
    scene depan kampus with dissolve
    mcname "Wahhh, jadi ini namanya kota Jakarta"
    mcname "Buuu, anakmu akhirnya kuliah di sini"
    mcname "DI KOTA JAKARTA!!!"
    mcname "Alhamdulillah mah pah"

    jump utamakana

label utamakana:
    $ renpy.block_rollback()
    
    #This ends the game
    return
