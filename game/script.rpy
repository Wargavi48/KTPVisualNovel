#  initial routes
default route = ""
default jurusan = ""
# initial phone
define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

#Definisikan transformasi dan alignments
define small_center = Transform(zoom=0.5, xalign=0.5)
define small_left = Transform(zoom=0.5, xalign=0.0)
define small_right = Transform(zoom=0.5, xalign=1.0)
define char_placement = Transform(zoom=0.5,xalign=0.5,yalign=-2.0)
define char_placement_left = Transform(zoom=0.5,xalign=0.2,yalign=-2.0)
define char_placement_right = Transform(zoom=0.5,xalign=1.0,yalign=-0.6)
define char_center = Transform(zoom=0.9,xalign=0.5,yalign=-0.1)
define galaxy_center = Transform(zoom=1.03,xalign=0.5,yalign=-0.1,ypos=-0.39)
define char_left = Transform(zoom=0.9,xalign=0.0,yalign=-0.1,xanchor=0.08)
define char_right = Transform(zoom=0.9,xalign=1.0,yalign=-0.1, xanchor=0.94)
define kana_near = Transform(zoom=1.3,xalign=0.5,yalign=0.02)
define tana_near = Transform(zoom=1.3,xalign=0.5,yalign=0.02,xpos=0.54)
define tana_right = Transform(zoom=1.3,xalign=-0.5,yalign=0.02)
define tana_right_2 = Transform(zoom=1.3,xalign=-1.0,yalign=0.02)
define tana_left = Transform(zoom=1.3,xalign=2.0,yalign=0.02)
define kana_near_left = Transform(zoom=1.3,xalign=1.3,yalign=0.02)
define kana_near_left_2 = Transform(zoom=1.3,xalign=2.0,yalign=0.02,xpos=1.93)
define kana_near_right = Transform(zoom=1.3,xalign=-0.5,yalign=0.02)
define pia_near = Transform(zoom=1.3,xalign=0.5,yalign=-0.01)
define pia_near_right = Transform(zoom=1.0,xalign=1.9,yalign=-0.07,xpos=2.0)
define char_near_left = Transform(zoom=1.3,xalign=1.3,yalign=0.04)
define feni_right = Transform(zoom=1.3,xalign=-1.0,yalign=0.08)
define feni_left = Transform(zoom=1.3,xalign=1.3,yalign=0.08)
define feni_center = Transform(zoom=1.3,xalign=0.5,yalign=0.08)
define flora_center = Transform(zoom=1.3,xalign=0.5,yalign=0.08)
define flora_right = Transform(zoom=1.3,xalign=-1.5,yalign=0.08)
define flora_left = Transform(zoom=1.3,xalign=2.0,yalign=0.08)
define fio_near = Transform(zoom=1.3,xalign=0.5,yalign=0.08)
define fio_near_left = Transform(zoom=1.3,xalign=1.3,yalign=0.08)
define fio_near_right = Transform(zoom=1.3,xalign=-0.5,yalign=0.08)
define freya_near = Transform(zoom=1.3,xalign=-0.5,yalign=0.08)
define freya_near_right = Transform(zoom=1.3,xalign=-1.0,yalign=0.08,xpos=-0.95)
define dosen_center = Transform(zoom=0.9,xalign=0.5,yalign=0.1)
define dosen_left = Transform(zoom=0.9,xalign=-0.5,yalign=0.1)
define rg_hasan_left = Transform(zoom=0.7,xalign=0.0,yalign=-0.1,xpos=-0.07)
define bang_rama_right = Transform(zoom=0.7,xalign=0.0,yalign=-0.1,xpos=0.40)
define FeniKanaTana_Feni = Transform(zoom=1.3,xalign=2.3,yalign=0.08)
define FeniKanaTana_Kana = Transform(zoom=1.3,xalign=0.8,yalign=0.0)
define FeniKanaTana_Tana = Transform(zoom=1.3,xalign=-1.8,yalign=0.0)
define KTP_Kana = Transform(zoom=1.3,xalign=2.5,yalign=0.0)
define KTP_Pia = Transform(zoom=1.3,xalign=0.8,yalign=-0.01)
define KTP_Tana = Transform(zoom=1.3,xalign=-1.8,yalign=0.0)
define takamina_center = Transform(zoom=0.7,xalign=0.5,yalign=-0.1)
define takamina_left = Transform(zoom=0.7,xalign=0.0,yalign=-0.1)
define ui_handphone = Transform(xalign=0.5,yalign=0.5)
define chibi_tono = Transform(zoom=0.3,xalign=0.0,yalign=0.0,xpos=0.15)
define lift_center = Transform(zoom=0.3,xalign=0.0,yalign=0.0,xpos=0.21)
define mafu = Transform(zoom=0.3,xalign=0.0,yalign=0.0,xpos=0.20)
define mading = Transform(zoom=0.35,xalign=0.0,yalign=-0.06,xpos=0.17)
define crane = Transform(zoom=0.2,xalign=0.0,yalign=0.14,xpos=0.28)
define seifuku = Transform(zoom=0.3,xalign=0.0,yalign=-0.5,xpos=0.18)
define pintu_rumah_kana = Transform(zoom=0.3,xalign=0.0,yalign=-0.20,xpos=0.18)
define pintu_kamar_kana = Transform(zoom=0.3,xalign=0.0,yalign=-0.25,xpos=0.19)

define club = Transform(zoom=0.4,xalign=0.0,yalign=0.2,xpos=0.11)
define club2 = Transform(zoom=0.34,xalign=0.0,yalign=-0.4,xpos=0.03)
define matsuri = Transform(zoom=0.18,xalign=0.0,yalign=0.13,xpos=0.55)
define poster = Transform(zoom=0.18,xalign=0.0,yalign=0.2,xpos=0.11)

# Game dimulai disini.
label start:
    init python:
        import random
    $ random_number = ''.join([str(random.randint(0, 9)) for _ in range(4)])
    if config.main_menu_music is not None:
        stop music fadeout 1.0

label intro:
    $ quick_menu = False 
    scene black 
    with dissolve
    pause(2.0)

    label namemc:
        $ mcname = ""
        $renpy.call_screen("name_input", "{size=-5}Silahkan masukkan nama kamu{/size}", ok_action=Jump("processmcname"), output_var="mcname")

    label processmcname:
        if not mcname or mcname == "" : 
            $renpy.call_screen("popup_message","Wajib memasukkan nama!", ok_action=Jump("namemc"))
    
    $ mama_name = Character("Mamah")
    $ papah_name = Character("Papah")
    $ renpy.music.set_volume(1.0)
    $ renpy.music.set_volume(1.0, channel="sound")
    $ renpy.music.set_volume(1.0, channel="audio")
    play music "BGM_Rumah Awal.ogg" fadein 1.0
    scene awan malam with Dissolve(2.0)
    $ quick_menu = True
    "Bintang terlihat bersinar terang di langit pada malam ini."
    "Membuat malam hari terasa lebih terang dari biasanya."
    "Sudah lama berlalu semenjak hari kelulusan, sekarang ini [mcname!c] sedang mempersiapkan diri untuk memasuki jenjang perkuliahan."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene kamar mc desa with Dissolve(1.0)
    $ quick_menu = True
    "[mcname!c]" "Huft."
    "[mcname!c]" "{i}Sepertinya persiapan untuk di sana nanti sudah lengkap semua.{/i}"
    "[mcname!c] memilih untuk memasuki kampus *Nama_Kampus* salah satu kampus unggulan yang ada di Indonesia."
    "Walaupun tempatnya berada jauh dari tempat asalnya, namun [mcname!c] tetap berkeinginan untuk memasuki kampus tersebut."
    show side mama at left with dissolve
    mama "Adeeek. Gimana persiapannya? Sudah semua?"
    hide side mama with dissolve
    "Terdengar suara Mamah memanggil dari luar kamar."
    "[mcname!c]" "Iyaa Mahh, ini baru selesai."
    show side mama at left with dissolve
    mama "Mamah masuk ya."
    hide side mama with dissolve
    play sound "audio/open_door.mp3" volume 3.0
    show mama at small_center
    show side mama at left
    with dissolve
    mama "Sudah siap semua kan barangnya? Gak ada yang kelupaan?"
    hide side mama with dissolve
    "[mcname!c]" "Udah semua kok, Mah. Ga perlu khawatir."
    show side mama at left with dissolve
    mama "Gimana Mamah gak khawatir? Kamu kan bakal merantau ke Jakarta sana."
    mama "Kaget loh Mamah waktu denger kamu ngomong pengen kuliah di *Nama_Kampus*."
    mama "Padahal kamu gak pernah pergi jauh dari rumah, jadinya Mamah khawatir."
    hide side mama with dissolve
    "[mcname!c]" "Kan sekalian nyoba liat-liat dunia luar, Mah."
    show side mama at left with dissolve
    mama "Tapi tetap saja, haahh...."
    hide side mama with dissolve
    "Mamah terdengar masih tidak setuju dengan pilihan anaknya."
    show side mama at left with dissolve
    mama "Kalau gak diyakinkan sama Papah, Mamah jelas gak bakal setuju."
    hide side mama with dissolve
    "Papah" "Denger-denger ada yang manggil nih."
    "Terdengar suara Papah dari depan pintu Kamar."
#Show Sprite Papah
    hide mama
    show papah at char_placement_right
    show papah:
        pos (0.94, -0.76) 
    show mama at char_left
    show mama:
        pos (0.11, -0.07) yzoom 1.0 zoom 0.55 
    show side mama at left
    with dissolve
    mama "Ah, Papah."
    mama "Engga, Mamah cuma masih ngerasa terlalu berlebihan buat adek untuk kuliah di luar kota."
    hide side mama
    show side papah at left
    with dissolve
    papah "Kan kita sudah bahas masalah ini sayang..."
    papah "Biar in aja adek merantau, biar dia bisa mandiri."
    papah "Lagian kan kalo cuma kita berdua kita jadi bebas."
    hide side papah with dissolve
    "Papah mengatakan hal tersebut dengan nada menggoda Mamah."
    show side mama at left with dissolve
    mama "Iya jug-"
    mama "Ih apaan sih pah, adek masih ada di sini loh."
    hide side mama
    show side papah at left
    with dissolve
    papah "Hahahah gapapa kan, lagian adek juga sudah besar."
    hide side papah
    hide papah
    hide mama
    with dissolve
    "Mereka kemudian saling menggoda satu sama lain, melupakan kehadiran [mcname!c]."
    "[mcname!c]" "{i}Hadeh, apa yang dilakukan pasangan yang dimabuk cinta ini di kamar anaknya sendiri...{/i}"
    show papah at char_placement_right
    show papah:
        pos (0.94, -0.76) 
    show side papah at left
    with dissolve
    papah "Ehem-"
    papah "Seperti yang sudah kita setujui, adek jadinya bakal kuliah di *Nama_Kampus*."
    papah "Lagian, adek juga sudah mempersiapkan barang-barangnya buat di sana."
    hide side papah
    show mama at char_left
    show mama:
        pos (0.11, -0.07) yzoom 1.0 zoom 0.55
    with dissolve
    mama "Iya sih, Mamah juga sudah ngabarin temennya Mamah buat di Jakarta nanti."
    hide side mama
    show side papah at left
    with dissolve
    papah "Kan..."
    papah "Jadi untuk masalah ini, Mamah udah oke kan?"
    hide side papah
    show side mama at left
    with dissolve
    mama "Iya deh Mamah ngalah."
    hide side mamah
    hide papah
    hide mama
    with dissolve
    $ quick_menu=False
    window auto hide
    show black:
        default
        subpixel True 
        parallel:
            Null(0.0, 0.0)
            'black' with dissolve
        parallel:
            ypos 0 alpha 1.0 
            linear 1.30 ypos 252 alpha 0.7 
    show black as black2:
        default
        subpixel True 
        parallel:
            Null(0.0, 0.0)
            'black' with dissolve
        parallel:
            ypos 2080 alpha 1.0 
            linear 1.30 ypos 1908 alpha 0.7 
    with Pause(1.40)
    show mama at char_center with dissolve
    with dissolve
    window auto show
    $ quick_menu=True
    show side mama at left with dissolve
    mama "Kalo gitu Mamah peluk dulu deh, sebelum adek bakal pergi nanti."
    hide side mama at left with dissolve

    "[mcname!c]" "E-Eh Mah, tapi kan aku masih di sini. Belum mau pergi ke Jakarta."
    show side mama at left with dissolve
    mama "Kalo itu nanti bakal peluk lagi, ini cuman buat ngobatin rasa kangen yang sekarang."
    hide side mama at left with dissolve
    "[mcname!c]" "I-iya deh."
    "[mcname!c] kemudian memeluk tubuh Mamah kembali."
    "Merasakan hal tersebut, Mamah pun memeluk [mcname!c] dengan lebih erat."
    "Terasa kehangatan dari tubuh mamah mengalir kepada [mcname!c]."
    "Hal itu membuat [mcname!c] ingat kalau dia nanti akan pergi jauh dari keluarganya."
    "Ada sedikit rasa sedih di hati [mcname!c] ketika memikirkan hal tersebut, namun dia sudah kuat dengan pendiriannya."
    hide mama with dissolve
    $ quick_menu=False
    window auto hide
    show black:
        subpixel True 
        ypos 252 
        linear 1.30 ypos -9 
    show black as black2:
        subpixel True 
        ypos 1908 
        linear 1.30 ypos 2169 
    with Pause(1.40)
    show mama at char_left
    show mama:
        pos (0.11, -0.07) yzoom 1.0 zoom 0.55
    with dissolve
    window auto show
    $ quick_menu=True
    "Akhirnya setelah beberapa menit, Mamah pun melepaskan pelukannya sambil tersenyum."
    show papah at char_placement_right
    show papah:
        pos (0.94, -0.76) 
    show side papah at left
    with dissolve
    papah "Jadi adek, untuk persiapan kuliah nanti sudah siap kan?"
    hide side papah with dissolve
    "[mcname!c]" "Iya Pah, sudah lengkap semua kok."
    show side papah at left with dissolve
    papah "Baguslah."
    papah "Untuk jurusannya nanti, kamu sudah pastiin kan mau masuk yang mana?"
    hide papah
    hide mama
    hide side papah
    with dissolve
    "Kamu memilih jurusan..."
    # call screen choose_route
    menu:
        "Kamu memilih jurusan..."
        "A. Mahasiswa Hubungan Internasional (HI)":
            $ route = "kana"
            $ jurusan = "HI"
            jump mainStoryBegin
        "B. Mahasiswa Teknik Pertanian (Agroteknologi)":
            $ route = "tana"
            $ jurusan = "Agroteknologi"
            jump mainStoryBegin
        "C. Mahasiswa Desain Komunikasi Visual (DKV)":
            $ route = "pia"
            $ jurusan = "DKV"
            jump mainStoryBegin
        "D. Mualass banget kuliah tahun ini, jurusannya ga gue banget cuy":
            jump ED1
        "E. Tes Mini Game":
            # jump startPiaGame
            jump shooting_game_start

    return