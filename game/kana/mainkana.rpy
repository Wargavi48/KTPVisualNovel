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
    "disini aku memilih jurusan HI dan hari ini \nhari dimana aku datang di Jakarta"
    scene black with dissolve
    scene depan kampus with dissolve
    play music "audio/kampus.mp3" loop fadein 1.0
    $ quick_menu = True
    mcname "Wahhh, jadi ini namanya kota Jakarta"
    mcname "Buuu, anakmu akhirnya kuliah di sini"
    mcname "DI KOTA JAKARTA!!!"
    mcname "Alhamdulillah mah pah"
    mcname "Doain anakmu bisa kuliah lancar ya mah, pah"
    mcname "OWH IYA!!!!!"
    mcname "Kalau gak salah, barang - barang dari rumah harusnya \nmau datang di kosan"
    mcname "Tapi penasaran dengan kota Jakarta deh..."
    $ quick_menu = False
    menu:
        "Langsung ke kosan abis itu rapihin barang":
            mcname "Jadi ini ya kamarku selama 4 tahun ke depan"
            mcname "Salam kenal ya kamarku moga moga kamu gak ada penunggunya hahaha...."
            "[mcname] merapihkan barang - barang bawaan yang sudah datang duluan oleh mobil pengantar"
            "butuh waktu beberapa jam untuk menyelesaikan semuanya dan mengatur tata letak yang ia rasa nyaman."
            mcname "Okeee barang - barang sudah selesai"
            mcname "Udah ngabarin orang tua juga sekarang saatnya tidur"
            $ quick_menu = False
            jump chapter1kana1
        "Muter - muter Jakarta dan habisin waktu sampai malam":
            "[mcname] malah lupa waktu dan akhirnya lupa kalau harus beresin barang"
            "Akhirnya [mcname] malah ikut ke pergi ke pergaulan bebas"
            $ quick_menu = False
            scene black  with dissolve
            show text "{color=#FFF}LU NGAPAIN IKUTAN PERGAULAN BEBAS INGET TUH ORANG TUA DI DESA{/color}" with Pause(1.0)
            scene black  with dissolve
            show text "{color=#FFF}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
            scene black  with dissolve
            play music "audio/Dreamcatcher.mp3"
            jump credits
        "Nyari cafe biar ga skena ":
            "[mcname] ikut ke dalam cirle orang orang kaya yang haus akan atensi di dunia maya, dan akhirnya malah ngutang sana sini krana kurang atensi"
            $ quick_menu = False
            scene black  with dissolve
            show text "{color=#FFF}ORTU LU DAPET KABAR KALAU LU MASUK PENJARA KRANA PENIPUAN UANG{/color}" with Pause(2.0)
            show text "{color=#FFF}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
            play music "audio/Dreamcatcher.mp3"
            jump credits
        "Ke warteg buat makan":
            mcname "Aduhhh perut gw kroncongan, makan dulu kali lah ya abis itu baru ke kos dari berangkat belum makan"
            "[mcname] pun memilih untuk pergi mencari makan ke warteg warteg yang berada di dekat kosnya"
            "[mcname] bertemu dengan beberapa pedagang yang ramah dan sopan, membuat [mcname] semakin nyaman berada di lingkungan kos nya tersebut"
            $ quick_menu = False
            jump chapter1kana1



    jump utamakana



label utamakana:
    $ renpy.block_rollback()
    
    #This ends the game
    return
