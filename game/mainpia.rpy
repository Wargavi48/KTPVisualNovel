# Deklarasikan backgrounds
image mc bedroom = "images/BG/bedroom.png"

#Definisikan transformasi dan alignments
define small_center = Transform(zoom=0.5, xalign=0.5)
define small_left = Transform(zoom=0.5, xalign=0.0)
define small_right = Transform(zoom=0.5, xalign=1.0)

label mainpia:
    $ renpy.block_rollback()
    $quick_menu = True
    scene black with dissolve
    show text "Chapter I\nThe Choosen One" with Pause(1.5)
    scene black with dissolve
    scene mc bedroom with dissolve
    show mama at small_center with dissolve
    $ mmama_name = Character("Mamah")
    "mama" "Sekarang mandi, sarapan, abis itu langsung ke stasiun ya buat ke Jeketi University buat daftar ulang."
    "mama" "Mama udah bilang ke temen mama yang di jakarta kalo kamu akan ngekost di tempat dia"
    mcname "Siap mah!"
    hide mama with dissolve

    jump chapter1pia


label chapter1pia:
    scene kampus with dissolve
    show text "Jeketi University\nKampus ternama di indonesia dibawah naungan Melody Corps. Merupakan universitas Negeri unggulan di Jakarta. Banyak orang bilang, kampus ini mencetak banyak sekali orang sukses. Artis, politisi, ilmuan, bahkan menjadi Idol terkenal pun bisa diraih disini. orang yang lulus menyandang gelar lulusan dari JU banyak dicari orang, karena kualitas pelajarnya sangat baik. Namun, untuk masuk ke JU ini pun tidak mudah" with Pause (2)
    scene black with dissolve
    scene kampus with dissolve
    mcname "Wah! besar juga ya kampusnya, dan aku bakal berkuliah disini huhuuu beruntungnya aku"
    scene black with dissolve
    show text "BRUKKKK!" with Pause(1)
    scene kampus with dissolve
    show pia with dissolve:
        yalign 2
    pia "Eh maaf kak ketabrak, gak apa - apa kan?"
    pia "Lagi buru-buru maaf ya"
    mcname "Ah gak papa kok."
    mcname "hehe"
    mcname "Maaf juga aku ngelamun ditengah jalan"
    pia "hehe oke maaf bye!"
    jump utamapia


label utamapia:
    $ renpy.block_rollback()
    
    #This ends the game
    return
