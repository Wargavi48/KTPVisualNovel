label mainStoryBegin:
    $ quick_menu = True
    mcname "Iya Pah, aku udah yakin kalo nanti bakal masuk jurusan [jurusan]."
    show papah at small_center with dissolve
    show papah:
        ypos -126 yzoom 1.0 zoom 1.0 
    show side papah at left with dissolve
    papah "Oke Papah percaya sama jurusan yang kamu pilih."
    papah "Papah gak bakal ikut campur sama pilihan kamu, biar kamu bisa ngejar passion yang kamu pengen."
    hide side papah with dissolve
    hide papah with dissolve
    show papah at char_placement_right with dissolve
    show papah:
        pos (1.04, -1.11) zoom 0.79 
    show mama at char_left with dissolve
    show side mama at left with dissolve
    mama "Iya, Mamah juga percaya kok sama pilihan yang adek pilih."
    hide side mama with dissolve
    "Mamah dan Papah telihat tersenyum kepada [mcname]."
    mcname "Makasih Pah, Makasih Mah."
    "[mcname] tentu saja merasa senang karena ia bisa mengejar apa yang dia inginkan."
    show side papah at left with dissolve
    papah "Lagian, mungkin aja adek bawa pulang menantu pas balik dari jakarta nanti, hahaha."
    hide side papah with dissolve
    show side mama at left with dissolve
    mama "Fufufu iya sih, jadinya Mamah bakal cepat punya cucu."
    hide side mama with dissolve
    mcname "A-apaan sih, aku kan ke sana buat nyari ilmu."
    "[mcname] terdengar malu saat Papah dan Mamah membawakan topik pasangan."
    show side papah at left with dissolve   
    papah "Siapa tau kan, hahaha."
    hide side papah with dissolve
    show side mama at left with dissolve
    mama "Ya udh kalo gitu kamu istirahat dulu ya, soalnya besok nanti bakal berangkat."
    mama "Takutnya nanti malah telat."
    hide side mama with dissolve
    show side papah at left with dissolve 
    papah "Oh iya sudah jam segini."
    hide side papah with dissolve
    "Jam terlihat menunjukkan bahwa waktu sudah larut malam."
    show side papah at left with dissolve     
    papah "Kalo begitu istirahat ya Adek, jangan begadang soalnya besok kamu berangkat."
    hide side papah with dissolve
    mcname "Siap, Pah."
    hide papah with dissolve
    hide mama with dissolve
    "Setelah mengucapkan selamat tidur, Papah dan Mamah pun pergi keluar dari kamar [mcname], meninggalkan [mcname] sendiran."
    mcname "Huffttt, akhirnya mereka pergi."
    mcname "{i}Mungkin aku bakal ngecek barang yang dibawa sekali lagi sebelum tidur, takutnya ada yang kelupaan.{/i}"
    $ quick_menu = False
    scene black with Dissolve(1.0)
    pause (1.0)
    scene kamar mc kota with Dissolve(1.0)
    $ quick_menu = True
    mcname "{i}Oke, barang-barang sudah lengkap semua.{/i}"
    mcname "Akhirnya udah bisa tidur nih."
    "[mcname] pun kemudian merebahkan dirinya di kasur."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" fadein 1.0
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    mcname "{i}Besok bakal jadi hari terakhirku di sini ya... {/i}"
    mcname "{i}Nanti bakal jauh dari keluarga dan juga teman-temanku di sini...{/i}"
    mcname "{i}Apalagi sama PC dan beberapa koleksi figureku...{/i}"
    "[mcname] mulai memikirkan pilihannya kembali."
    mcname "{i}Ah! Overthinking juga gak baik, mending langsung tidur aja dah.{/i}"
    "[mcname] pun memejamkan matanya dan langsung tertidur pulas."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    show text "{color=#FFF}KEESOKAN HARINYA{/color}" with Pause(2.0)
    play music "BGM_Pagi Siang.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    play sound "audio/crowd_noise.mp3" loop fadein 1.0 volume (4.0)
    ##$ renpy.block_rollback()
    $ quick_menu = True
    "Pagi ini [mcname] sudah bersiap di stasiun untuk pergi ke Jakarta."
    mcname "Oke Mah, Pah, aku pergi dulu yak."
    show side mama at left with dissolve
    mama "Adeeek hati-hati di jalan ya!"
    hide side mama with dissolve
    mcname "Iya, Mah."
    show side papah at left with dissolve    
    papah "Inget, kalo ada apa-apa kabarin Papah Mamah aja."
    hide side papah with dissolve
    mcname "Siaaap."
    stop music fadeout 1.0
    stop sound fadeout 1.0
    ##$ renpy.block_rollback()
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}CHAPTER I{/color}" with Pause(1.5)
    scene black with dissolve
    $ quick_menu = True
    "Hari baru sudah dimulai."
    "Lembaran baru di hidupku pun akhirnya terbuka dan akhirnya aku telah memasuki jenjang masuk kuliah."
    "Di sini aku memilih jurusan [jurusan]."
    "Dan hari ini adalah hari di mana aku datang ke Jakarta!"
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Pagi Siang.ogg" loop fadein 1.0
    scene monas temporary with Dissolve(1.0)
    play sound "audio/crowd_noise.mp3" loop fadein 1.0 volume (4.0)
    play audio "audio/station_chime.mp3" fadeout 1.0 volume (2.0)
    $ quick_menu = True
    mcname "Wahhh, jadi ini namanya kota Jakarta."
    mcname "Buuu, anakmu akhirnya kuliah di sini."
    mcname "DI KOTA JAKARTA!!!"
    mcname "Alhamdulillah Mah Pah."
    mcname "Doain anakmu bisa kuliah lancar ya Mah, Pah."
    mcname "OWH IYA!!!!!"
    mcname "Kalau gak salah..."
    mcname "Barang-barang dari rumah harusnya mau datang di kosan!"
    mcname "Tapi masih penasaran sama kota Jakarta deh..."
    stop sound fadeout 1.0
    menu:
        "Yang [mcname] lakukan..."
        "Langsung ke kosan abis itu rapikan barang.":
            ##$ renpy.block_rollback()
            $ quick_menu = False
            scene black with Dissolve(1.0)
            scene kamar mc kota with Dissolve(1.0)
            $ quick_menu = True
            mcname "Jadi ini ya kamarku selama 4 tahun ke depan."
            mcname "Salam kenal ya kamarku moga-moga kamu gak ada penunggunya hahaha..."
            "[mcname] merapihkan barang-barang bawaan yang sudah datang duluan oleh mobil pengantar."
            mcname "Hmmm... Banyak juga ya."
            "Sambil melihat tumpukan barang-barang yang dibawa, [mcname] mengatakan hal tersebut dengan nada rendah."
            "Butuh waktu beberapa jam untuk menyelesaikan semuanya dan mengatur tata letak yang ia rasa nyaman."
            jump awalkosan
        "Muter-muter Jakarta dan habisin waktu sampai malam.":
            ##$ renpy.block_rollback()
            $ quick_menu = True
            "[mcname] memilih untuk mengelilingi Jakarta dan menghabiskan waktu sampai malam."
            "Jadinya malah lupa waktu dan akhirnya lupa kalau harus beresin barang."
            "Akhirnya [mcname] malah ikut ke pergi ke pergaulan bebas."
            $ quick_menu = False
            stop music fadeout 1.0
            scene black  with dissolve
            show text "{color=#FFF}LU NGAPAIN IKUTAN PERGAULAN BEBAS INGET TUH ORANG TUA DI DESA!!{/color}" with Pause(2.0)
            scene black  with dissolve
            show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
            scene black  with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits
        "Nyari cafe biar skena.":
            ##$ renpy.block_rollback()
            $ quick_menu = True
            "[mcname] ikut ke dalam cirle orang orang kaya yang haus akan atensi di dunia maya, dan akhirnya malah ngutang sana sini karena kurang atensi."
            $ quick_menu = False
            stop music fadeout 1.0
            scene black  with dissolve
            show text "{color=#FFF}ORTU LU DAPET KABAR KALAU LU MASUK PENJARA KARENA PENIPUAN UANG.{/color}" with Pause(2.0)
            scene black  with dissolve
            show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
            scene black  with dissolve
            play music "audio/Dreamcatcher_v2.mp3"
            jump credits
        "Ke warteg buat makan.":
            #$ renpy.block_rollback()
            $ quick_menu = True
            mcname "Aduhhh perutku keroncongan. Makan dulu kali yah, habis itu baru ke kos. Dari berangkat belum makan soalnya."
            "[mcname] pun memilih untuk pergi mencari makan ke rumah makan padang yang berada di dekat kosnya."
            $ quick_menu = False
            scene black with Dissolve(1.0)
            pause (1.0)
            scene monas temporary with Dissolve(1.0)
            $ quick_menu = True
            "Dia bertemu dengan beberapa pedagang yang ramah dan sopan, membuat [mcname] semakin nyaman berada di lingkungan kosnya tersebut."
            mcname "Mas mau makan mas."
            "Pedagang" "Mau pesen apa?"
            mcname "Nasi,"
            mcname "Rendang,"
            mcname "Sama telor balado 1 ya mas."
            mcname "Sama minta tambah sambal ijo."
            "Pedagang" "Okee."
            "Pedangang" "Totalnya jadi 25.000 ya."
            mcname "Ini ya mas, makasih."
            "Setelah [mcname] mengisi perutnya di rumah makan padang."
            "[mcname] pun pergi ke kosannya untuk merapikan barang bawaan dan beristirahat."
            $ quick_menu = False
            stop music fadeout 1.0
            jump awalkosan


label awalkosan:
        #$ renpy.block_rollback()
        stop music fadeout 1.0
        $ quick_menu = False
        scene black with Dissolve(1.0)
        play music "audio/BGM_Kosan 1.ogg" fadein 1.0
        scene awan malam with Dissolve(1.0)
        $ quick_menu = True
        "Tak terasa hari pun sudah gelap."
        $ quick_menu = False
        scene black with Dissolve (1.0)
        scene kamar mc kota with Dissolve(1.0)
        $ quick_menu = True
        mcname "Okeee barang-barang sudah selesai."
        mcname "Sekarang saatnya tidur."
        "Setelah merapikan barang, [mcname] ingin beristirahat tapi ingat akan sesuatu."
        mcname "Eh, lupa. Belum ngabarin orang tua."
        $ quick_menu = False
        mc_nvl "{size=-5}Mah! Pah! Aku sudah sampai Jakarta. Sudah beres-beres barang juga.{/size}"
        papah_nvl "{size=-5}Kamu genki gk di sana?{/size}"
        papah_nvl "{size=-5}Otou-san khawatir{/size}"
        papah_nvl "{image=mengsedih.png}"
        mamah_nvl "{size=-5}Iya tuh... hati-hati ya nak di sana{/size}"
        mamah_nvl "{size=-5}Jaga diri baik-baik{/size}"
        mamah_nvl "{size=-5}Jangan pilih-pilih makanan. Makan yang banyak biar sehat{/size}"
        mamah_nvl "{size=-5}Jangan lupa mandi tiap hari.{/size}"
        mamah_nvl "{size=-5}Jangan banyak begadang.{/size}"
        mamah_nvl "{size=-5}Tidur yang cukup.{/size}"
        mamah_nvl "{size=-5}Belajar yang baik, ya.{/size}"
        mamah_nvl "{size=-5}Pinter-pinter di sana{/size}"
        mamah_nvl "{size=-5}Kalau ada masalah, bisa cerita ke mamah dan otou-san.{/size}"
        papah_nvl "{image=sip emoji.png}"
        mc_nvl "{size=-5}Iya Mah, Pah.{/size}"
        scene kamar mc kota with dissolve
        $ quick_menu = True
        "Malam pun semakin larut."
        "[mcname] pun memejamkan matanya dengan pikiran penuh harapan akan esok hari."
        stop music fadeout 1.0
        $ quick_menu = False
        scene black with dissolve
        show text "{color=#FFF}KEESOKAN HARINYA{/color}" with Pause(2.0)
        if route == "kana":
            jump chapter1kana1
        elif route == "tana":
            jump chapter1tana
        elif route == "pia":
            jump chapter1pia