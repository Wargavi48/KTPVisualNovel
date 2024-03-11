# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bg blck = "images/blck.png"

# Deklarasikan karakter yang digunakan di game.
define e = Character('Eileen', color="#c8ffc8")

# Game dimulai disini.
label start:
    if config.main_menu_music is not None:
        stop music fadeout 1.0

label intro:

    scene bg black with dissolve

    "Nama kamu siapa?"

    label namemc:
    $ mcname = ""
    $renpy.call_screen("name_input", "Silahkan masukkan nama kamu", ok_action=Jump("processmcname"), output_var="mcname")

    label processmcname:
    if not mcname or mcname == "" : 
        $renpy.call_screen("popup_message","Wajib memasukkan nama!", ok_action=Jump("namemc"))

    scene bg white with dissolve

    "hei, bangun!"

    scene mc dream with dissolve

    pia "ngun.. Bangooon!!!"
    Tana "bangun kocak, Tidur mulu kayak gue"
    Kana "cepet ih bangun, sarapan dulu"

    scene mc kamar with dissolve
    show mama with dissolve
    $ mmama_name = Character("Mamah")
    mama "bangun nak, udah jam berapa ini.. sarapan dulu ayo jangan bangun kesiangan."
    mama "hari ini kamu harus daftar ulang kuliah kamu loh ke Jakarta! gimana?!"
    mama "butuh 3 jam buat ke kampus, nanti kamu ketinggalan kereta! cepet bangun siap-siap!!"
    mcname "iyaah mahh."
    hide mama

    "kamu adalah:"
    $quick_menu = False
    menu:
        "A. Mahasiswa Hubungan Internasional (HI)":
            jump mainkana
        "B. Mahasiswa Teknik Pertanian (Agroteknologi)":
            jump maintono
        "C. Mahasiswa Desain Komunikasi Visual (DKV)":
            jump mainpia
        "D. Mualass banget kuliah tahun ini":
            jump ED1
    return