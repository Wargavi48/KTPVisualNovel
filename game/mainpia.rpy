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
    "Jeketi University\nKampus ternama di indonesia dibawah naungan Melody Corps. Merupakan universitas Negeri unggulan di Jakarta." 
    "Banyak orang bilang, kampus ini mencetak banyak sekali orang sukses. Artis, politisi, ilmuan, bahkan menjadi Idol terkenal pun bisa diraih disini." 
    "Orang yang lulus menyandang gelar lulusan dari JU banyak dicari orang, karena kualitas pelajarnya sangat baik. Namun, untuk masuk ke JU ini pun tidak mudah"
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
    hide pia 
    mcname "Ah! Aku juga harus buru - buru daftar ulang!"
    "MC pun selesai registrasi daftar ulang ke jurusan DKV"
    scene black with dissolve
    show text "1 MINGGU KEMUDIAN" with Pause(1.5)
    scene black with dissolve
    scene kampus with dissolve
    "Dekan DKV" "Selamat datang di Jeketi University para Mahasiswa dan Mahasiswi baru! raihlah mimpi kalian disini!! selamat berjuang!"
    "Dekan DKV" "Hadirin, dipersilakan untuk pulang"
    mcname "Hueeeee....capek juga duduk doang dengerin orang ngomong. besok mulai masuk kuliah, gak sabar bakal ketemu orang orang baru"
    pia "HEEEEEEEEEEEE!! KAMUUUUUUU"
    mcname "buset, siapa itu tereak tereak"
    mcname "loh kok kayaknya nyamperin aku"
    show pia with dissolve:
        yalign 2
    pia "HEIIIII!!! INGET AKU GAKKK???"
    mcname "iya aku inget, tapi bisa gak tereak gak? malu diliatin banyak orang ini"
    pia "oh iya, maap. hehe OH! INGET AKU? KITA TABRAKAN DEPAN GERBANG MINGGU LALU! KIRAIN KAMU SENIOR! TERNYATA MABA JUGA KAYAK AKU HAHAHAHA"
    mcname "((buset tereak lagi))"
    pia "kamu DKV juga ya! gilak ternyata kita sejurusan. apakah jodoh?"
    pia "candaaaaa ahahaha"
    mcname "ahaha ahaha iya sejurusan ternyata ya kita. oh iya kita belom kenalan. nama aku [mcname]"
    $ pia_name = "Pia"
    pia "LAH IYA BELOM KENALAN. halo, aku Pia Meraleo salam kenal"
    mcname "((wah kalo diliat dari dekat gini, manis juga Pia ini))"
    pia "[mcname], kok bengong? makan bareng yuk, pengen liat kantin kampusnya kayak gimana. laper juga sih"
    mcname "lah, lesgooo, pas banget ini laper"
    jump utamapia


label utamapia:
    $ renpy.block_rollback()
    
    #This ends the game
    return
