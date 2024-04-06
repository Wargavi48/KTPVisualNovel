# Kamu dapat taruh script game mu di file ini.
image cursor asa:
    "gui/button/cursor_3.png"
image cursor pia:
    "gui/button/cursor_1.png"
image cursor tana:
    "gui/button/cursor_2.png"


#Definisikan transformasi dan alignments
define small_center = Transform(zoom=0.5, xalign=0.5)
define small_left = Transform(zoom=0.5, xalign=0.0)
define small_right = Transform(zoom=0.5, xalign=1.0)
define char_placement = Transform(zoom=0.5,xalign=1.0,yalign=-2.0)


# Game dimulai disini.
label start:
    if config.main_menu_music is not None:
        stop music fadeout 1.0

label intro:

    scene black with dissolve

    label namemc:
        $ mcname = ""
        $renpy.call_screen("name_input", "Silahkan masukkan nama kamu", ok_action=Jump("processmcname"), output_var="mcname")

    label processmcname:
        if not mcname or mcname == "" : 
            $renpy.call_screen("popup_message","Wajib memasukkan nama!", ok_action=Jump("namemc"))

    scene dream with dissolve

    play music "audio/bgm_harvestmoon_spring.mp3" loop fadein 1.0

    show kana_sh at small_left with dissolve
    kana_sh "cepet ih bangun, sarapan dulu"

    show tono_sh at small_center with dissolve
    tono_sh "bangun kocak, Tidur mulu kayak gue"

    show pia_sh at small_right with dissolve
    pia_sh "ngun.. Bangooon!!! (+70db)"

    hide kana_sh
    hide tono_sh
    hide pia_sh
    with dissolve

    scene mc bedroom with dissolve
    show mama at small_center with dissolve
    $ mama_name = Character("Mamah")
    mama "bangun nak, udah jam berapa ini.. sarapan dulu ayo jangan bangun kesiangan."
    mama "hari ini kamu harus daftar ulang kuliah kamu loh! gimana?!"
    mama "butuh 3 jam buat ke kampus, nanti kamu ketinggalan kereta! cepet bangun siap-siap!!"
    mcname "iyaah mahh."
    hide mama with dissolve

    "kamu adalah:"
    $quick_menu = False
    menu:
        "A. Mahasiswa Hubungan Internasional (HI)":
            jump mainkana
        "B. Mahasiswa Teknik Pertanian (Agroteknologi)":
            jump maintono
        "C. Mahasiswa Desain Komunikasi Visual (DKV)":
            jump mainpia
        "D. Mualass banget kuliah tahun ini, jurusannya ga gue banget cuy":
            jump ED1
    return