label mainStoryBegin:
    $ renpy.block_rollback()
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}Chapter I{/color}" with Pause(1.5)
    scene black with dissolve

    "Hari baru sudah dimulai"
    "Lembaran baru di hidupku pun akhirnya terbuka dan akhirnya aku telah memasuki jenjang masuk kuliah"
    "Di sini aku memilih jurusan [jurusan]"
    "Dan hari ini adalah hari dimana aku datang di Jakarta!"
    scene black with Dissolve(2.0)
    # scene depan kampus with dissolve
    # nanti diubah jadi scene monas
    scene monas temporary with dissolve
    play music "audio/BGM_MC Pertama Kali ke JKT + BG Pagi.mp3" loop fadein 1.0
    play sound "audio/crowd_noise.mp3" loop fadein 1.0
    play sound "audio/train.mp3" fadeout 1.0
    play sound "audio/station_chime.mp3" fadeout 1.0
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
        "Nyari cafe biar skena ":
            $ renpy.block_rollback()
            $ quick_menu = True
            "[mcname] ikut ke dalam cirle orang orang kaya yang haus akan atensi di dunia maya, dan akhirnya malah ngutang sana sini karena kurang atensi"
            $ quick_menu = False
            scene black  with dissolve
            show text "{color=#FFF}ORTU LU DAPET KABAR KALAU LU MASUK PENJARA KARENA PENIPUAN UANG{/color}" with Pause(2.0)
            show text "{color=#FFF}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
            play music "audio/Dreamcatcher.mp3"
            jump credits
        "Ke warteg buat makan":
            $ renpy.block_rollback()
            $ quick_menu = True
            mcname "Aduhhh perutku keroncongan. Makan dulu kali yah, habis itu baru ke kos. Dari berangkat belum makan soalnya"
            "[mcname] pun memilih untuk pergi mencari makan ke rumah makan padang yang berada di dekat kosnya"
            "Dia bertemu dengan beberapa pedagang yang ramah dan sopan, membuat [mcname] semakin nyaman berada di lingkungan kos nya tersebut"
            mcname "Mas mau makan mas"
            "Pedagang" "Mau pesen apa?"
            mcname "Nasi"
            mcname "Rendang"
            mcname "Sama Telor Balado 1 ya mas"
            mcname "Sama minta tambah sambal ijo"
            "Pedagang" "Okee"
            "Pedangang" "Totalnya jadi 25.000 ya"
            mcname "Ini ya mas, makasih"
            "Setelah [mcname] mengisi perutnya di rumah makan padang"
            "[mcname] pun pergi ke kosannya untuk merapikan barang bawaan dan beristirahat."
            $ quick_menu = False
            stop music fadeout 1.0
            jump awalkosan


label awalkosan:
        $ renpy.block_rollback()
        scene black with dissolve
        scene mc bedroom with Dissolve(2.0)
        $ quick_menu = True
        play music "audio/BGM_Kosan 1.mp3" fadein 1.0
        "Tak terasa hari pun sudah gelap"
        "Setelah merapikan barang, [mcname] ingin beristirahat tapi ingat akan sesuatu."
        mcname "Okeee barang - barang sudah selesai"
        mcname "Sekarang saatnya tidur."
        mcname "Eh, lupa. Belum ngabarin orang tua"
        $ quick_menu = False
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
        scene black with dissolve
        show text "{color=#FFF}Keesokan Harinya{/color}" with Pause(2.0)
        if route == "kana":
            jump chapter1kana1
        elif route == "tana":
            jump chapter1tana
        elif route == "pia":
            jump chapter1pia