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
    $ quick_menu = False
    # $ default_mouse = "mouse_kanaia"
    scene black with dissolve
    show text "{color=#FFF}Chapter I{/color}" with Pause(1.5)
    scene black with dissolve

    "Hari baru sudah dimulai"
    "Lembaran baru di hidupku pun akhirnya terbuka dan akhirnya aku telah memasuki jenjang masuk kuliah"
    "Di sini aku memilih jurusan HI"
    "Dan hari ini adalah hari dimana aku datang di Jakarta!"
    scene black with Dissolve(2.0)
    scene depan kampus with dissolve
    play music "audio/BGM_MC Pertama Kali ke JKT + BG Pagi.mp3" loop fadein 1.0
    $ quick_menu = True
    mcname "Wahhh, jadi ini namanya kota Jakarta"
    mcname "Buuu, anakmu akhirnya kuliah di sini"
    mcname "DI KOTA JAKARTA!!!"
    mcname "Alhamdulillah Mah Pah"
    mcname "Doain anakmu bisa kuliah lancar ya Mah, Pah"
    mcname "OWH IYA!!!!!"
    mcname "Kalau gak salah"
    mcname "Barang - barang dari rumah harusnya mau datang di kosan"
    mcname "Tapi penasaran dengan kota Jakarta deh..."
    $ quick_menu = False
    menu:
        "Langsung ke kosan abis itu rapikan barang":
            $ renpy.block_rollback()
            scene mc bedroom with Dissolve(2.0)
            $ quick_menu = True
            mcname "Jadi ini ya kamarku selama 4 tahun ke depan"
            mcname "Salam kenal ya kamarku moga moga kamu gak ada penunggunya hahaha...."
            "[mcname] merapihkan barang - barang bawaan yang sudah datang duluan oleh mobil pengantar"
            mcname "Hmmm.. Banyak juga ya"
            "Sambil melihat tumpukan barang-barang yang dibawa, [mcname] mengatakan hal tersebut dengan nada rendah."
            "Butuh waktu beberapa jam untuk menyelesaikan semuanya dan mengatur tata letak yang ia rasa nyaman."
            scene black with dissolve
            scene mc bedroom with Dissolve(2.0)
            $ quick_menu = False
            stop music fadeout 1.0
            jump awalkosan
        "Muter - muter Jakarta dan habisin waktu sampai malam":
            $ renpy.block_rollback()
            $ quick_menu = True
            "[mcname] malah lupa waktu dan akhirnya lupa kalau harus beresin barang"
            "Akhirnya [mcname] malah ikut ke pergi ke pergaulan bebas"
            $ quick_menu = False
            scene black  with dissolve
            show text "{color=#FFF}LU NGAPAIN IKUTAN PERGAULAN BEBAS INGET TUH ORANG TUA DI DESA{/color}" with Pause(2.0)
            scene black  with dissolve
            show text "{color=#FFF}{size=+10}BAD END{/size}{/color}" with Pause(2.0)
            scene black  with dissolve
            play music "audio/Dreamcatcher.mp3"
            jump credits
        "Nyari cafe biar ga skena ":
            $ renpy.block_rollback()
            $ quick_menu = True
            "[mcname] ikut ke dalam cirle orang orang kaya yang haus akan atensi di dunia maya, dan akhirnya malah ngutang sana sini krana kurang atensi"
            $ quick_menu = False
            scene black  with dissolve
            show text "{color=#FFF}ORTU LU DAPET KABAR KALAU LU MASUK PENJARA KRANA PENIPUAN UANG{/color}" with Pause(2.0)
            show text "{color=#FFF}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
            play music "audio/Dreamcatcher.mp3"
            jump credits
        "Ke warteg buat makan":
            $ renpy.block_rollback()
            $ quick_menu = True
            mcname "Aduhhh perutku kroncongan. Makan dulu kali yah, habis itu baru ke kos. Dari berangkat belum makan soalnya"
            "[mcname] pun memilih untuk pergi mencari makan ke warteg yang berada di dekat kosnya"
            "Dia bertemu dengan beberapa pedagang yang ramah dan sopan, membuat [mcname] semakin nyaman berada di lingkungan kos nya tersebut"
            mcname "Mas mau makan mas"
            "Pedagang" "Mau pesen apa?"
            mcname "Nasi"
            mcname "Rendang"
            mcname "Sama Telor 1 ya mas"
            mcname "Sama minta tambah sambal"
            "Pedagang" "Okee"
            "Pedangang" "Totalnya jadi 25.000 ya"
            mcname "Ini ya mas, makasih"
            "Setelah [mcname] mengisi perutnya di warteg"
            "[mcname] pun pergi ke kosannya untuk merapikan barang bawaan dan beristirahat."
            $ quick_menu = False
            stop music fadeout 1.0
            jump awalkosan



    jump utamakana


label awalkosan:
        $ renpy.block_rollback()
        $ quick_menu = True
        play music "audio/BGM_Kosan 1.mp3" fadein 1.0
        "Tak terasa hari pun sudah gelap"
        "Setelah merapikan barang, [mcname] ingin beristirahat tapi ingat akan sesuatu."
        mcname "Okeee barang - barang sudah selesai"
        mcname "Sekarang saatnya tidur."
        mcname "Eh, lupa. Belum ngabarin orang tua"
        $ quick_menu = False
        stop music fadeout 1.0
        mc_nvl "{size=-5}Mah! Pah! Aku sudah sampai Jakarta. Sudah beres beres barang juga.{/size}"
        papah_nvl "{size=-5}Kamu genki gk disana?{/size}"
        papah_nvl "{size=-5}Otou-san khawatir{/size}"
        papah_nvl "{image=mengsedih.png}"
        mamah_nvl "{size=-5}Iya tuh...hati-hati ya nak disana{/size}"
        mamah_nvl "{size=-5}Jaga diri baik-baik{/size}"
        mamah_nvl "{size=-5}Jangan pilih - pilih makanan. Makan yang banyak biar sehat{/size}"
        mamah_nvl "{size=-5}Jangan lupa mandi tiap hari.{/size}"
        mamah_nvl "{size=-5}Jangan banyak begadang.{/size}"
        mamah_nvl "{size=-5}Tidur yang cukup.{/size}"
        mamah_nvl "{size=-5}Belajar yang baik, ya.{/size}"
        mamah_nvl "{size=-5}Pinter pinter di sana{/size}"
        mamah_nvl "{size=-5}Kalau ada masalah, bisa cerita ke mamah dan otou-san.{/size}"
        papah_nvl "{image=sip emoji.png}"
        mc_nvl "{size=-5}Iya Mah, Pah.{/size}"
        "Malam pun semakin larut"
        "[mcname] pun memejamkan matanya dengan pikiran penuh harapan akan esok hari"
        stop music fadeout 1.0
        jump chapter1kana1


label utamakana:
    $ renpy.block_rollback()
    
    #This ends the game
    return
