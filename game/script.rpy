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
define galaxy_center = Transform(zoom=0.66,xalign=0.5,yalign=-0.1)
define char_left = Transform(zoom=0.9,xalign=0.0,yalign=-0.1,xanchor=0.08)
define char_right = Transform(zoom=0.9,xalign=1.0,yalign=-0.1, xanchor=0.94)
define kana_near = Transform(zoom=1.3,xalign=0.5,yalign=0.02)
define tana_near = Transform(zoom=1.3,xalign=0.5,yalign=0.02)
define tana_right = Transform(zoom=1.3,xalign=-0.5,yalign=0.02)
define kana_near_left = Transform(zoom=1.3,xalign=1.3,yalign=0.02)
define kana_near_left_2 = Transform(zoom=1.3,xalign=2.0,yalign=0.02)
define kana_near_right = Transform(zoom=1.3,xalign=-0.5,yalign=0.02)
define pia_near = Transform(zoom=1.3,xalign=0.5,yalign=-0.01)
define pia_near_right = Transform(zoom=1.0,xalign=1.9,yalign=-0.07)
define char_near_left = Transform(zoom=1.3,xalign=1.3,yalign=0.04)
define feni_right = Transform(zoom=1.3,xalign=-1.0,yalign=0.08)
define feni_center = Transform(zoom=1.3,xalign=0.5,yalign=0.08)
define flora_center = Transform(zoom=1.3,xalign=0.5,yalign=0.08)
define flora_right = Transform(zoom=1.3,xalign=-1.5,yalign=0.08)
define flora_left = Transform(zoom=1.3,xalign=2.0,yalign=0.08)
define fio_near = Transform(zoom=1.3,xalign=0.5,yalign=0.08)
define fio_near_left = Transform(zoom=1.3,xalign=1.3,yalign=0.08)
define fio_near_right = Transform(zoom=1.3,xalign=-0.5,yalign=0.08)
define freya_near = Transform(zoom=1.3,xalign=-0.5,yalign=0.08)
define freya_near_right = Transform(zoom=1.3,xalign=-1.0,yalign=0.08)
define dosen_center = Transform(zoom=0.9,xalign=0.5,yalign=0.1)
define dosen_left = Transform(zoom=0.9,xalign=-0.5,yalign=0.1)



# Game dimulai disini.
label start:
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
    
    scene white
    with fade
    pause(2.0)

    scene dream 
    with fade
    pause(2.0)
    show kana_sh at small_left with dissolve
    kana_sh "cepet ih bangun, sarapan dulu"

    show tono_sh at small_center with dissolve
    tono_sh "bangun kocak, Tidur mulu kayak gue"

    show pia_sh at small_right with dissolve
    pia_sh "ngun.. Bangooon!!! (+70db)"

    hide kana_sh
    hide tono_sh
    hide pia_sh
    play sound "audio/Alarm.mp3" fadein 1.0
    scene black with Dissolve(3.0)
    scene mc bedroom with Dissolve(3.0)
    play music "audio/backsound_kamar.mp3" loop fadein 1.0
    $ quick_menu = True 
    show mama at small_center
    show side mama at left
    $ mama_name = Character("Mamah")
    stop sound fadeout 1.0
    play music "audio/BGM_Rumah Awal.mp3" fadein 1.0
    mama "Bangun nak, udah jam berapa ini... Sarapan dulu, ayo, jangan bangun kesiangan."
    mama "Hari ini kamu harus daftar ulang kuliah kamu, loh! Gimana?"
    mama "Butuh 3 jam buat ke kampus, nanti kamu ketinggalan kereta! Cepet bangun siap-siap!!"
    hide side mama with dissolve
    hide mama with dissolve
    mcname "Iyaah mahh."

    pause(2.0)
    
    "kamu adalah:"
    $quick_menu = False
    # call screen choose_route
    menu:
        "A. Mahasiswa Hubungan Internasional (HI)":
            $ route = "kana"
            $ jurusan = "HI"
            stop music fadeout 1.0
            jump mainStoryBegin
        "B. Mahasiswa Teknik Pertanian (Agroteknologi)":
            $ route = "tana"
            $ jurusan = "Agroteknologi"
            stop music fadeout 1.0
            jump mainStoryBegin
        "C. Mahasiswa Desain Komunikasi Visual (DKV)":
            $ route = "pia"
            $ jurusan = "DKV"
            stop music fadeout 1.0
            jump mainStoryBegin
        "D. Mualass banget kuliah tahun ini, jurusannya ga gue banget cuy":
            stop music fadeout 1.0
            jump ED1
        "E. Tes Mini Game":
            # jump startPiaGame
            jump shooting_game_start

    return