#---CHAPTER 2—---
#ARC 1
label chapter2kanastart:
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene chapter 2 kana with Dissolve (1.0)
    pause(3.0)
    scene black with Dissolve (1.0)
    play music "audio/BGM_Pagi Siang.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya..."
    #$ renpy.block_rollback()
    "Karena hari ini hari libur, jadi [mcname!c] memutuskan untuk menghabiskan waktunya berkeliling di mall yang dekat dengan kostnya."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Mall.ogg" fadein 1.0
    scene mall temp with Dissolve(1.0)
    play sound "audio/crowd_noise.mp3" loop fadein 1.0 volume (4.0)
    $ quick_menu = True
    "[mcname!c]" "Rame juga ya ternyata mall di Jakarta ini..."
    "Di sekeliling banyak orang terlihat, dari keluarga kecil, pasangan muda yang sedang kencan, bahkan seseorang yang terlihat sendirian menikmati waktunya."
    "Namun dari banyaknya orang di sekitar, ada beberapa kumpulan orang yang menarik perhatian [mcname!c]."
    "[mcname!c]" "Lumayan nyentrik pakaian orang-orang itu yah, mungkin itu normal di Jakarta?"
    "[mcname!c]" "Ahhhh! Kayaknya lagi cosplay, yang sering mamah lakuin..."
    stop sound fadeout 1.0
    stop music fadeout 1.0
    #Flashback (ATas bawah putih)
    $ quick_menu = False
    scene white with Dissolve(1.0)
    play music "audio/BGM_Rumah Awal.ogg" loop fadein 1.0
    scene kamar mc desa with Dissolve(2.0)
    show white:
        default
        subpixel True 
        parallel:
            Null(0.0, 0.0)
            'white' with dissolve
        parallel:
            ypos 0 alpha 1.0 
            linear 1.30 ypos 252 alpha 0.7 
    show white as white2:
        default
        subpixel True 
        parallel:
            Null(0.0, 0.0)
            'white' with dissolve
        parallel:
            ypos 2080 alpha 1.0 
            linear 1.30 ypos 1908 alpha 0.7 
    with Pause(1.40)
    $ quick_menu = True
    "[mcname!c]" "Pah, itu apa yang dipakai Mamah?"
    show papah at char_placement_right
    show papah:
        pos (0.94, -0.76) 
    show papah_side at left
    with dissolve
    papah "Ohhh, itu namanya cosplay."
    hide papah_side
    "[mcname!c]" "Memangnya cosplay itu apa?"
    show mama at char_left
    show mama:
        pos (0.11, -0.07) yzoom 1.0 zoom 0.55 
    show side mama at left
    with dissolve
    mama "Cosplay itu costume play. Biasanya dipake sama orang yang suka anime, buat di event atau lomba gitu."
    hide side mama
    show papah_side at left
    with dissolve
    papah "Kalo Papah sama Mamah biasanya buat malam-malam, hehe."
    hide papah_side
    show side mama at left
    with dissolve
    mama "Huss jangan ajarin yang aneh-aneh. [mcname!c] masih kecil."
    hide side mama
    show papah_side at left
    with dissolve
    papah "Ahahaha. Gapapa, biar pinter kayak Papah. Hehehe"
    hide papah_side
    show side mama at left
    with dissolve
    mama "Udah ihhh~"
    hide side mama
    show papah_side at left
    with dissolve
    papah "Jadi pengen nanti malam, hehe."
    hide papah_side
    show side mama at left
    with dissolve
    mama "*Blush*"
    hide side mama
    hide papah
    hide mama
    with dissolve
    "[mcname!c]" "{i}Saat itu aku gak begitu paham dengan apa yang mereka bicarakan...{/i}"
    stop music fadeout 1.0
    stop music fadeout 1.0
    $ quick_menu = False
    scene white with Dissolve(2.0)

    play music "audio/BGM_Mall.ogg" loop fadein 1.0
    scene mall temp with Dissolve(1.0)
    $ quick_menu = True
    "[mcname!c]" "{i}Hmmmm... Kalo ada orang yang cosplay, berarti ada event yang sedang berlangsung di mall ini.{/i}"
    "[mcname!c]" "{i}Gak ada salahnya nanti aku mampir sebentar ke sana.{/i}"
    "[mcname!c] kemudian berkeliling mall untuk melihat-lihat di mall, sampai akhirnya ia sampai ke event jejepangan di mall tersebut."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play sound "audio/crowd_noise.mp3" loop fadein 1.0 volume (4.0)
    scene mall temp with Dissolve(1.0)
    $ quick_menu = True
    "[mcname!c]" "Waaah banyak juga ternyata orang-orang di sini."
    "[mcname!c]" "Kalau papah di sini mungkin bakal kesenengan tuh, hahaha."
    "[mcname!c] pun mencoba berkeliling melihat-lihat apa saja yang ada di event tersebut."
    "Di dalam event terlihat banyak booth-booth yang dibuka, mulai seperti mencoba kuliner yang ada di sana, melihat merch-merch event, bahkan [mcname!c] juga foto bersama cosplayer."
    stop sound fadeout 1.0
    stop music fadeout 1.0
    "Tiba-tiba..."
    play music "BGM_Funny 3.ogg" fadein 0.5
    play sound "audio/tabrakan.mp3" volume (7.0)
    show kana wibu at chibi_tono with dissolve
    "Sepertinya [mcname!c] tidak sengaja menabrak seseorang saat berjalan."
    hide kana wibu
    show kana wibu2 at chibi_tono
    with dissolve
    "[mcname!c]" "Waduh maaf kamu gapapa?"
    "[mcname!c] mencoba mengulurkan tangannya."
    "???" "Ah iya, aku gapapa."
    "Seakan terkejut melihat [mcname!c], orang tersebut langsung berdiri tergesa-gesa."
    "???" "Ah, m-maaf!"
    stop music fadeout 1.0
    hide kana wibu2 with dissolve
#CHIBI NUE OFF
    "Setelah mengatakan hal tersebut, orang tadi langsung berlari pergi."
    play sound "audio/crowd_noise.mp3" loop fadein 1.0 volume (4.0)
    play music "BGM_Mall.ogg" fadein 1.0
    "[mcname!c]" "......."
    "[mcname!c]" "Buru-buru banget itu orang."
    "[mcname!c]" "{i}Hmmm... Mungkin ada merch yang dia pengen, jadi kayak gitu.{/i}"
    "[mcname!c]" "Jadi ngingetin kayak papah dulu, haha."
    "[mcname!c]" "Hmm..?"
    "[mcname!c] menyadari ada sesuatu yang jatuh."
    show kana mafu at mafu with dissolve
    "[mcname!c]" "{i}Kayaknya ini barang orang tadi.{/i}"
    "[mcname!c] pun mengambil barang tersebut untuk memastikannya."
    "Terlihat sebuah merch dari salah satu utaite yang bisa dibilang cukup terkenal."
    "[mcname!c]" "Jangan-jangan ini barang limited, soalnya pernah liat nih di internet."
    hide kana mafu with dissolve
    "[mcname!c] kemudian mencoba melihat ke orang yang baru saja menabraknya."
    "Jarak antara [mcname!c] dan orang tersebut sudah bisa dibilang lumayan jauh."
    "[mcname!c]" "HEYYY!!! HEYYY!! BARANGMU JATUH!!!"
    "Namun karena begitu ramainya orang yang ada di dalam event, suara [mcname!c] tidak terdengar oleh orang tersebut."
    "[mcname!c]" "{i}Hmmm... Sepertinya tidak terdengar.{/i}"
    "[mcname!c]" "Kutitipkan ke penitipan barang sama panitia event atau..."
    "[mcname!c]" "... atau aku kejar ya orang yang tadi?"
    menu:
        "Yang [mcname!c] lakukan..."
        "Kejar orang yang tadi":
            stop music fadeout 1.0
            $ quick_menu=False
            play music "BGM_Bad End.ogg" fadein 1.0
            "[mcname!c]" "Aku harus kejar orang yang tadi! Oke saatnya aku keluarkan jurus lari ninja ku, cyaattt!"
            stop music fadeout 1.0
            scene black with dissolve
            show text "{color=#FFF}*BUKANNYA KETEMU SAMA ORANG YANG JATUHIN MERCH KAMU MALAH DISANGKA LAGI COSPLAY DAN DI SURUH TAMPIL DI PANGGUNG DAN MENANG, DAN AKHIRNYA LU LUPA SAMA ORANG YANG TADI*{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FFF}*YAHAHA, NIAT NGEJAR MALAH JUARA! BAGUS SIH, TAPI KAN SEKARANG LU MALAH LUPA BUAT NGEMBALIIN BARANG TADI.*{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FF0000}BAD END{/color}" with Pause(2.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits
        "Titipkan barang ke panitia event":
            "[mcname!c] pun memilih untuk menitipkan barang tersebut ke pada panitia yang bertugas."
            "Akhirnya panitia pun membuat pengumuman adanya barang hilang."
            jump kanachapter2titippanitia

label kanachapter2titippanitia:
    stop sound fadeout 1.0
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kelas.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya..."
    $ quick_menu = False
    scene kelas with Dissolve(2.0)
    #$ renpy.block_rollback()
    $ quick_menu = True
    "Di kelas Jeketi University, terlihat banyak mahasiswa melakukan aktivitasnya."
    "[mcname!c]" "Haduuhh, barangnya gimana ya..."
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Barang? Barang apaan? Memangnya kamu pesen online, [mcname!c]?"
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near
    with dissolve
    "[mcname!c]" "Ah enggak, jadi kemarin ada event jejepangan di mall pas aku lagi jalan-jalan."
    "[mcname!c]" "Di sana gak sengaja tuh aku ketabrak sama orang."
    hide kana with dissolve
    show freya at char_left
    show kana at char_right
    with dissolve
    show freya_shock at char_left
    show freya_side_shock at left
    with dissolve
    freya "Ehhh kamunya gapapa tuh?"
    show freya at char_left
    hide freya_side_shock with dissolve
    hide kana
    show kana_confused at char_right
    show kana_side_confused at left
    with dissolve
    kana "Ah iya, kamunya gapapa?"
    show kana at char_right
    hide kana_side_confused at left
    with dissolve
    "[mcname!c]" "Gapapa kok."
    "[mcname!c]" "Nah, orang itu gak sengaja jatuhin barang yang dia bawa. Merch limited dari Utaite yang terkenal itu, loh."
    hide kana_confused
    show kana_shy at char_right
    hide freya_shock
    show freya_awe at char_left
    show freya_side_awe at left
    with dissolve
    freya "Ehhh, merchnya Utaite yang terkenal itu..."
    show freya_smug at char_left
    hide freya_side_awe
    with dissolve
    "Freya berkata sambil melirik Kana."
    "[mcname!c]" "Aku ga paham sama orang-orang yang suka begituan."
    show kana_shy_talk at char_right
    with dissolve
    "[mcname!c]" "Kayak Papahku itu, agak aneh emang."
    hide kana_shy
    show kana_shy_smile at char_right
    show kana_side_shy_smile at left
    with dissolve
    kana "Ahahah\n*Tertawa karir*"
    kana "Emang aneh ya, haha."
    hide kana_side_shy_smile
    hide freya_awe 
    hide freya_smug 
    hide kana_shy_talk 
    hide freya 
    hide kana
    hide kana_shy_smile
    with dissolve
    "Tidak lama kemudian..."
    stop music fadeout 1.0
    $ quick_menu=False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Dosen.ogg" fadein 1.0
    scene kelas with Dissolve(1.0)
    show dosen at dosen_center with dissolve
    $ quick_menu=True
    "Dosen pun masuk ke dalam kelas dan waktu mata kuliah pun dimulai."
    hide dosen
    show dosen_talk at dosen_center
    show dosen_side_talk at left
    with dissolve
    dosen "Teman-teman, mari kita mulai perkuliahan hari ini."
    hide dosen_talk
    hide dosen_side_talk
    with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Sore.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Beberapa jam kemudian..."
    $ quick_menu = False 
    scene kelas sore with Dissolve(2.0)
    $ quick_menu = True
    "[mcname!c]" "Wahh akhirnya selesai juga~"
    show kana at char_right
    show freya at char_left
    with dissolve
    "Kana dan Freya datang menghampiri [mcname!c]."
    hide kana
    show kana_talk at char_right
    show kana_side_talk at left
    with dissolve
    kana "Kalo gini enaknya ke kantin sih."
    hide kana_side_talk
    hide kana_talk
    show kana at char_right
    with dissolve
    "[mcname!c]" "Aduh, tapi jam segini kantin pasti penuh."
    hide freya
    show freya_talk at char_left
    show freya_side_talk at left
    with dissolve
    freya "Hmmm. Gimana kalo bawa makanan dari kantin ke rooftop? Denger-denger tempatnya enak."
    hide freya_side_talk with dissolve
    show freya at char_left
    hide freya_talk
    hide kana
    show kana_talk at char_right
    show kana_side_talk at left
    with dissolve
    kana "Ehhh, boleh tuh. Tapi jangan makanan berat, nanti ribet bawanya."
    hide kana_side_talk
    hide kana_talk
    show kana at char_right
    with dissolve
    "[mcname!c]" "Yaudah aku ke kantin ya. Sekalian aku beliin makanan buat kalian."
    hide kana_talk
    hide freya_talk
    show kana_smile at char_right
    show freya_smile at char_left
    with dissolve
    pause(1.0)
    hide kana_smile
    show kana_talk at char_right
    show kana_side_talk at left
    with dissolve
    kana "Okee. Aku sama Freya nunggu di rooftop, ya."
    hide kana_side_talk at left with dissolve
    hide kana_talk
    hide freya_smile
    hide kana
    hide freya
    with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Tak lama kemudian..."
    $ quick_menu = False
    scene lorong sore with Dissolve(2.0)
    $ quick_menu = True
    "Setelah [mcname!c] membeli makanan di kantin, [mcname!c] berjalan menuju tangga ke rooftop."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Rooftop Sore.ogg" fadein 1.0
    scene rooftop sore with Dissolve(1.0)
    #$ renpy.block_rollback()
    $ quick_menu = True
    "Sesampainya di rooftop, [mcname!c] hanya melihat Kana yang memandang langit sendirian."
    show kana at kana_near with dissolve
    "[mcname!c]" "Loh, sendirian Kana? Freya mana?"
    hide kana
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Freya tadi mendadak ada urusan. Jadinya dia pulang duluan."
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near
    with dissolve
    "[mcname!c]" "Heeee~"
    hide kana
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Aku udah chat, tapi keknya gak kebaca sama kamu ya."
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near
    with dissolve
    "[mcname!c] kemudian membuka HPnya."
    "Di sana terlihat banyak notifikasi chat dari Kana dan Freya."
    "[mcname!c]" "Ah iya, sorry banget. Tadi di kantin rame banget, jadi gak kebaca."
    $ quick_menu = False
    window auto hide
    hide kana
    show kana_smile at kana_near
    with dissolve
    pause(1.0)
    hide kana_smile
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    window auto show
    $ quick_menu = True
    kana "Yaudah. Yuk kita duduk, makan dulu."
    hide kana_side_talk
    hide kana_talk
    show kana_smile at kana_near
    with dissolve
    "[mcname!c]" "Oke."
    hide kana_smile with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene rooftop sore with Dissolve(1.0)
    show kana at kana_near with dissolve
    $ quick_menu = True
    "[mcname!c]" "Kamu mau yang cokelat, strawberry, atau keju?"
    hide kana
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Kayaknya aku yang strawberry aja deh."
    hide kana_side_talk
    hide kana_talk
    show kana_smile at kana_near
    with dissolve
    "Setelah memberikan Kana roti yang dia pilih, akhirnya [mcname!c] dan Kana duduk di bangku yang ada di rooftop."
    "Di sana, Kana dan [mcname!c] menikmati roti sambil memandangi langit. Mereka tidak mengeluarkan sepatah kata pun. Suasana hening menjadi terasa sedikit canggung."
    "[mcname!c]" "{i}Duh bingung mau ngomong apaan. Biasanya Freya yang mulai obrolan.{/i}"
    "Ingin mencairkan suasana, [mcname!c] mencoba memulai percakapan."
    hide kana_smile
    show kana_shy at kana_near
    with dissolve
    "[mcname!c]" "A-"
    hide kana_shy
    show kana_shy_smile at kana_near
    show kana_side_shy_smile at left
    with dissolve
    kana "Kamu kabarnya gimana?"
    hide kana_shy_smile
    show kana_shy at kana_near
    hide kana_side_shy_smile at left with dissolve
    "Sebelum [mcname!c] sempat berbicara, Kana tiba-tiba memberikan pertanyaan."
    "[mcname!c]" "E-eeh?"
    hide kana_shy_smile
    show kana_shy_talk at kana_near
    show kana_side_cry at left
    with dissolve
    kana "Kamu udah makan, belum?"
    hide kana_side_cry
    hide kana_shy_talk
    show kana_confused_blush at kana_near
    with dissolve
    "[mcname!c]" "?????"
    "[mcname!c]" "Kan kita lagi makan, Kana..."
    hide kana_confused_blush
    show kana_shy_talk at kana_near
    show kana_side_cry at left
    with dissolve
    kana "Ah i-iya yah. Hahaha ngomong apa sih aku."
    hide kana_side_cry
    hide kana_shy_talk
    show kana_shy_closeeye at kana_near
    with dissolve
    "Setelah Kana mengatakan hal tersebut, suasananya kembali menjadi hening."
    hide kana_shy_closeeye
    show kana_shy_talk at kana_near
    show kana_side_cry at left
    with dissolve
    kana "Biasanya ada Freya ya, yang ngomong mulu."
    #gak_nutup
    hide kana_side_cry with dissolve
    "[mcname!c]" "Haha, iya yah."
    "[mcname!c]" "Haha."
    hide kana_drylaugh
    show kana_shy_smile at kana_near
    show kana_side_shy_smile at left
    with dissolve
    kana "Fufu."
    hide kana_side_shy_smile
    hide kana_shy_smile
    show kana at kana_near
    with dissolve
    "[mcname!c]" "Dilihat-lihat kamu emang deket banget ya sama Freya."
    hide kana
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Iya. Dari kecil, emang Freya selalu bareng aku."
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near
    with dissolve
    "[mcname!c]" "....."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Kana menatap ke atas langit seakan mengingat masa lalu."
    show kana_side_talk at left
    with dissolve
    kana "Dulu…"
    hide kana_side_talk at left
    with dissolve
#CG Chibi Kana Freya
    kana "Dulu badanku lemah dan sering sakit, jadinya jarang keluar rumah."
    kana "Waktu yang lain pada main di luar, aku cuma bisa liat mereka dari jendela kamarku."
    kana "Untungnya waktu itu Freya ada dan mau main bareng aku."
    kana "Padahal bisa aja dia main sama anak-anak yang lain, tapi dia malah nemenin aku."
    kana "Jadinya sampe sekarang bareng terus deh aku sama Freya, haha."
#Hide CG
    show kana_smile at kana_near with dissolve
    "Saat mengatakan hal tersebut, Kanaia tersenyum mengingat teman berharganya."
    show kana_shy at kana_near
    hide kana_smile
    with dissolve
    "[mcname!c]" "Heee gitu ya ternyata…"
    "Mendengar hal tersebut, [mcname!c] merasa sedikit iri kepada Freya yang bisa membuat Kana tersenyum seperti itu."
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    hide kana_shy with dissolve
    "Tiba-tiba dari arah berlawanan terdengar suara pintu terbuka."
    $ quick_menu = False
    scene rooftop sore with Dissolve(2.0)
    show freya at char_left
    show kana at char_right
    with dissolve
    pause(0.5)
    hide freya
    show freya_talk at char_left
    show freya_side_talk at left
    with dissolve
    $ quick_menu = True
    freya "Halooooo, sorry. Lama nungguin, ya?"
    hide freya_side_talk
    hide freya_talk
    show freya_smile at char_left
    with dissolve
    hide kana
    show kana_talk at char_right
    show kana_side_talk at left
    with dissolve
    kana "Ah! Freyaa."
    hide kana_side_talk
    hide kana_talk
    show kana at char_right
    with dissolve
    "[mcname!c]" "Nggak kok."
    hide kana
    show kana_talk at char_right
    show kana_side_talk at left
    with dissolve
    kana "Ayok sini makan."
    hide kana_side_talk
    hide kana_talk
    show kana_smile at char_right
    with dissolve
    hide freya_smile
    show freya_talk at char_left
    show freya_side_talk at left
    with dissolve
    freya "Okeee~"
    show freya_smile at char_left
    hide freya_side_talk
    with dissolve
    "Mereka pun menghabiskan waktu dengan berbincang dan makan bersama..."
    hide freya_smile
    hide freya_talk
    hide kana_smile 
    with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kelas.ogg" fadein 1.0 volume(1.5)
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya..."
    $ quick_menu = False
    scene kelas with Dissolve(2.0)
    #$ renpy.block_rollback()
    show kana at char_right
    show freya at char_left
    with dissolve
    pause(1.0)
    hide kana
    show kana_talk at char_right
    show kana_side_talk at left
    with dissolve
    $ quick_menu = True
    kana "[mcname!c]! Freya! Eh liat ini! Lucu banget gak sih? Kemarin aku liat di internet."
    hide kana_side_talk
    hide kana_talk
    show kana at char_right
    with dissolve
    "[mcname!c]" "Hooo aku pernah liat ada toko yang jual boneka ini nih, waktu ke mall kemarin."
    hide kana
    show kana_talk at char_right
    show kana_side_talk at left
    with dissolve
    kana "Heee serius? Habis ini kalian free, kan? Yuk ke sana bareng!"
    hide kana_side_talk
    hide kana_talk
    show kana_smile at char_right
    with dissolve
    hide freya
    show freya_talk at char_left
    show freya_side_talk at left
    with dissolve
    freya "Ayoook. Aku juga free, sih."
    hide freya_side_talk with dissolve
    hide freya_talk
    show freya_smile at char_left
    hide kana_smile
    show kana_talk at char_right
    show kana_side_talk at left
    with dissolve
    kana "[mcname!c] nanti ikut yak, soalnya kamu kan yang tau tempatnya."
    hide kana_side_talk
    show kana_smile at char_right
    hide kana_talk
    with dissolve
    "[mcname!c]" "Bolehh~"
    hide kana_smile
    hide freya_smile
    with dissolve
    stop music fadeout 1.0
    "Beberapa saat kemudian, dosen pun datang memasuki ruangan kelas."
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    play music "audio/BGM_Dosen.ogg" fadein 1.0
    $ quick_menu = False
    window auto hide
    show dosen at dosen_center with dissolve
    pause(0.5)
    window auto show
    $ quick_menu = True
    show dosen_talk at dosen_center
    show dosen_side_talk at left
    with dissolve
    dosen "Selamat pagi. Pelajaran akan dimulai, ya."
    hide dosen_talk
    hide dosen_side_talk
    with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Sore.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Tak terasa langit menjadi sore..."
    $ quick_menu = False
    scene kelas sore with Dissolve(2.0)
    show dosen_talk at dosen_center
    show dosen_side_talk at left
    with dissolve
    $ quick_menu = True
    dosen "Yak. Mata kuliah ini sudah sampai sini dulu. Selanjutnya kalian review masing-masing, ya."
    dosen "Ah iya Freya. Untuk pembahasan kemarin, Ibu tunggu di ruangan Ibu sekarang."
    hide dosen_side_talk
    hide dosen_talk
    show dosen at dosen_left
    show freya_shock at tana_right
    with dissolve
    show freya_side_shock at left
    with dissolve
    freya "Ehhh……"
    freya "Baik, Bu."
    hide freya_side_shock with dissolve
    hide dosen
    show dosen at dosen_center
    hide freya_shock
    with dissolve
    "Bu Dosen pergi meninggalkan ruang kelas, para mahasiswa pun mulai merapikan barangnya."
    hide dosen with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene kelas sore with Dissolve(1.0)
    show freya at char_left
    show kana at char_right
    with dissolve
    pause(0.5)
    hide kana
    show kana_talk at char_right
    show kana_side_talk at left
    with dissolve
    $ quick_menu = True
    kana "Akhirnya selesai juga~"
    hide kana_side_talk
    hide kana_talk
    show kana at char_right
    with dissolve
    "[mcname!c]" "Jadi? Masih mau ke sana?"
    show kana_talk at char_right
    show kana_side_talk at left
    with dissolve
    kana "Iya dong."
    hide kana_side_talk with dissolve
    hide kana_talk
    hide freya
    show freya_shock at char_left
    show freya_side_shock at left
    with dissolve
    freya "Yahhh, sorry guys. Kayaknya aku gak bisa ikut nemenin kalian."
    hide freya_side_shock with dissolve
    hide freya_shock
    show freya_smug at char_left
    hide kana_talk
    show kana_confused at char_right
    show kana_side_confused at left
    with dissolve
    kana "Yahhhh..."
    hide kana_side_confused with dissolve
    hide kana_confused
    show kana at char_right
    hide freya_shock
    show freya_talk at char_left
    show freya_side_talk at left
    with dissolve
    freya "Gapapa kok. Kan ada [mcname!c]."
    freya "[mcname!c]! Kamu jagain Kana, ya."
    hide freya_side_talk
    hide freya_talk
    show freya_smile at char_left
    hide kana_confused
    show kana_shy_smile at char_right
    show kana_side_shy_smile at left
    with dissolve
    kana "E.. eeeeh."
    hide kana_side_shy_smile
    hide kana_shy_smile
    hide freya_smile
    hide freya_smug
    show kana_shy at char_right
    with dissolve
    "Freya pun menyusul Dosen, meninggalkan Kana dan [mcname!c] berdua."
    "[mcname!c]" "Yaudah, yuk."
    hide kana_shy
    show kana_shy_smile at char_right
    show kana_side_shy_smile at left
    with dissolve
    kana "I-iya."
    hide kana_side_shy_smile at left
    hide kana_shy_smile
    with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Mall.ogg" fadein 1.0
    scene mall temp with Dissolve(1.0)
    #$ renpy.block_rollback()
    show kana_smile at char_center with dissolve
    $ quick_menu = True
    "Sesampainya di mall..."
    hide kana_smile
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Kamu sering ke mall ini, ya?"
    show kana_smile at kana_near
    hide kana_side_talk
    with dissolve
    "[mcname!c]" "Nggak juga, kok. Kemarin kebetulan aja inget."
    "[mcname!c]" "Kalo kamu?"
    hide kana_smile
    show kana_side_talk at left
    show kana_talk at kana_near
    with dissolve
    kana "Aku biasanya di rumah aja, sih."
    hide kana_side_talk
    hide kana_talk
    show kana_smile at kana_near
    with dissolve
    "[mcname!c]" "Weh. Kalo gitu mau coba sekalian jalan-jalan? Mumpung kamu di sini."
    hide kana_smile
    show kana_confused at kana_near
    show kana_side_confused at left
    with dissolve
    kana "Ehhh, tapi kamu gapapa kah?"
    hide kana_side_confused with dissolve
    #gak_nutup_kana
    "[mcname!c]" "Gapapa, kok. Lagi free juga, hehe."
    hide kana_confused
    show kana_smile at kana_near
    with dissolve
    "Mereka kemudian berjalan bersama sambil berbincang."
    hide kana_smile with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene mall temp with Dissolve(1.0)
    $ quick_menu = True
    "Tiba-tiba saat membahas topik pembicaraan, Kana tidak merespon sehingga [mcname!c] mencoba untuk menengok ke arah Kana."
    "[mcname!c]" "{i}Loh, Kana ke mana?{/i}"
#Asset Baju Kana yg dipajang ON
    "[mcname!c] pun melihat ke belakang. Di sana terlihat Kana sedang menatap salah satu baju yang dipajang di mall."
    "[mcname!c]" "Eh, Kana? Ada apa?"
    show kana_side at left with dissolve
    kana "..."
    hide kana_side with dissolve
    "[mcname!c]" "Kana? Nanti ketinggalan lohhh."
    hide kana
    show kana_talk at small_center
    show kana_side_talk at left
    with dissolve
    kana "Ah! Iya."
#HIDE ASSET BAJU KANA YG DIPAJANG
    hide kana_side_talk with dissolve
    hide kana_talk
    show kana_smile at kana_near
    with dissolve
    "Kana kemudian menghampiri [mcname!c]."
    hide kana_smile
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve 
    kana "BTW, di mana tempat yang jual bonekanya [mcname!c]?"
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near
    with dissolve
    "[mcname!c]" "Di situ, ayok."
    hide kana
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Okee."
    hide kana_side_talk
    hide kana_talk
    with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene mall with Dissolve(1.0)
    #MALL SPONSOR
    $ quick_menu = True
    "Sesampainya di toko tersebut..."
    "[mcname!c]" "Permisi, Kak. Kalau boneka yang ini masih ada?"
    "Pelayan Toko" "Maaf Kak. Sepertinya boneka yang Kakak cari itu sudah habis stock yang readynya."
    "Pelayan Toko" "Kalo mau bisa pre-order, tapi nunggunya sekitar 90 hari."
    "[mcname!c]" "{i}Wah, lama banget. Seperti waktu Papah mau PO merch idol group kesukaannya.{/i}"
    show kana_confused at kana_near
    show kana_side_confused at left
    with dissolve
    kana "Yahhhh, gimana nih? Kalo PO kayaknya lama banget."
    hide kana_side_confused with dissolve
    #gak_nutup_kana
    "[mcname!c]" "Gimana kalo kita jalan, liat-liat yang lain dulu. Siapa tau ada barang lucu lainnya."
    hide kana_confused
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Oke deh."
    hide kana_side_talk
    hide kana_talk
    with dissolve
    "Namun muka Kana terlihat sedikit kecewa..."
    "Kana dan [mcname!c] pun kembali berjalan berkeliling di mall."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene mall temp with Dissolve(1.0)
    show kana_confused at kana_near with dissolve
    $ quick_menu = True
    "[mcname!c]" "{i}Sepertinya Kana masih kecewa dengan kejadian tadi.{/i}"
    "[mcname!c]" "Kana, gimana kalo kita ke game center aja?"
    show kana_side_confused at left with dissolve
    kana "..."
    hide kana_side_confused with dissolve
    "[mcname!c]" "Kanaa?"
    hide kana_confused  
    show kana_drylaugh at kana_near
    show kana_side_drylaugh at left
    with dissolve
    kana "Hmmmm? Eh maaf kurang fokus tadi, hahaha."
    hide kana_side_drylaugh at left
    hide kana_drylaugh 
    show kana at kana_near
    with dissolve
    "[mcname!c]" "Ya udaah. Ayok ikut aku sini."
    hide kana
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Eeeh? Emangnya mau ke mana?"
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near
    with dissolve
    "[mcname!c]" "Udaaah, ikut aja."
    hide kana with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Game Center.ogg" fadein 1.0
    scene game center with Dissolve(1.0)
    show kana at kana_near with dissolve
    pause(1.0)
    hide kana
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    $ quick_menu = True
    kana "Heeee? Di sini ada game center ternyata..."
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near
    with dissolve
    "[mcname!c]" "Mau nyoba game di sini, Kana? Aku lumayan pede loh sama skill racing aku."
    hide kana
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Bolehhh, siapa takut?"
    hide kana_talk
    hide kana_side_talk
    with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene game center with Dissolve(1.0)
    play sound "audio/SFX_Racing Game.ogg" loop fadein 1.0 volume(2.0)
    show kana at char_center with dissolve
    pause(1.0)
    hide kana
    show kana_talk at char_center
    show kana_side_talk at left
    with dissolve
    $ quick_menu = True
    kana "Liat nih skill racing aku~"
    hide kana_side_talk
    hide kana_talk
    show kana at char_center
    with dissolve
    "[mcname!c]" "Wih jago juga kamu, udah rank 1 aja."
    hide kana
    show kana_talk at char_center
    show kana_side_talk at left
    with dissolve
    kana "Hehe. Kan namaku Kanaia \"Resing\" Asa."
    hide kana_side_talk
    hide kana_talk
    with dissolve
    play audio "audio/SFX - Car Crash.mp3" volume (3.0)
    $ quick_menu = False
    window auto hide
    with Pause(4.0)
    hide kana_talk
    show kana_shy_talk at char_center
    show side kana_side_shy_talk at left
    with dissolve
    window auto show
    $ quick_menu = True
    kana "Eh? Eh? Kok aku ditabrak mulu. Waaaaaa~"
    #gak_nutup_kana
    hide side kana_side_shy_talk with dissolve
    "[mcname!c]" "Eh, gimana ini Kana? Sekarang malah aku yang di depan. Hehe~"
    show kana_side_confused at left
    show kana_confused at char_center
    with dissolve
    kana "Arrgh! Liat aja nanti."
    hide kana_side_confused with dissolve
    "[mcname!c]" "Weh aku udah di lap terakhir, nih!"
    hide kana_confused
    hide kana_shy_talk
    with dissolve
    play audio "audio/SFX - Car Crash.mp3" volume (3.0)
    $ quick_menu = False
    window auto hide
    with Pause(4.0)
    show kana_side_confused at left
    show kana_confused at char_center
    with dissolve
    window auto show
    $ quick_menu = True
    kana "Noooo~ Aku nabrak mulu."
    hide kana_side_confused with dissolve
    "[mcname!c]" "Inget rem, Kana. Hahahaha!"
    show kana_side_confused at left
    with dissolve
    kana "Ahhhhh! Jangan tabrak akuuu~"
    hide kana_side_confused
    hide kana_confused
    with dissolve
    stop sound fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene game center with Dissolve(1.0)
    show kana_angry at char_center with dissolve
    $ quick_menu = True
    "[mcname!c]" "Hahaha gimana nih Kana? Malah aku yang Rank 1."
    hide kana_angry
    show kana_confused at char_center
    show kana_side_confused at left
    with dissolve
    kana "Sekali lagi laahh, aku masih gak terima."
    #gak_nutup_kana
    hide kana_side_confused
    hide kana_confused
    with dissolve
    play sound "audio/SFX_Racing Game.ogg" loop fadein 1.0 volume 2.0
    "Akhirnya mereka memainkan game tersebut berkali kali..."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    pause (1.0)
    scene game center with Dissolve(1.0)
    stop sound fadeout 1.0  
    show kana_talk at char_center
    show kana_side_talk at left
    with dissolve
    $ quick_menu = True
    kana "Hahaha gimana aku, hebat kan bisa Rank 1?"
    hide kana_side_talk
    hide kana_talk
    show kana_smile at char_center
    with dissolve
    "[mcname!c]" "Tapi kan kamu tadi kalah mulu~"
    hide kana_smile
    show kana_angry at char_center
    with dissolve
    pause(1.0)
    hide kana_angry
    show kana_confused at char_center
    show kana_side_confused at left
    with dissolve
    kana "Hmph. Yang penting game terakhir aku menang."
    hide kana_confused
    hide kana_side_confused
    show kana_smile at char_center
    with dissolve
    "[mcname!c]" "Hahaha. Iya deh kamu jago banget."
    "[mcname!c]" "Gimana? Mau racing lagi?"
    hide kana_smile
    show kana_talk at char_center
    show kana_side_talk at left
    with dissolve
    kana "Nggak, ah. Kita ganti game. The last winner wins. Hehe."
    hide kana_talk
    hide kana_side_talk at left
    with dissolve
    "Selanjutnya Kana mengajak [mcname!c] main game \"Whack-a-mole\"."
    stop sound fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene game center with Dissolve(1.0)
    show kana_talk at char_center
    show kana_side_talk at left
    with dissolve
    $ quick_menu = True
    kana "Aku jago banget kalo mukul-mukul gini."
    hide kana_side_talk
    hide kana_talk
    show kana at char_center
    with dissolve
    "[mcname!c]" "Iya iyaa."
    play sound "audio/SFX - Countdown.mp3" fadein 1.0 volume (2.0)
    $ quick_menu = False
    window auto hide
    with Pause(4.5)
    play sound "audio/SFX - Whack.mp3" loop fadein 1.0 volume (3.0)
    pause(3.0)
    hide kana
    show kana_confused at char_center
    show kana_side_confused at left
    with dissolve
    window auto show
    $ quick_menu = True
    kana "Aduhh banyak yang miss."
    #gak_nutup_kana
    hide kana_side_confused with dissolve
    "[mcname!c]" "Ayokk semangat Kanaa."
    show kana_side_confused at left
    with dissolve
    kana "Waaaa~"
    #gak_nutup_kana
    hide kana_side_confused with dissolve
    "[mcname!c]" "Itu yang itu, Kana."
    hide kana_talk
    show kana_angry at char_center
    with dissolve
    pause (1.0)
    hide kana_angry
    show kana_confused at char_center
    show kana_side_confused at left
    with dissolve
    kana "Ah, kamu backseat muluu!"
    #gak_nutup_kana
    hide kana_side_confused with dissolve
    "[mcname!c]" "Geregetan soalnyaa."
    stop sound fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene game center with Dissolve(1.0)
    show kana_talk at char_center
    show kana_side_talk at left
    with dissolve
    $ quick_menu = True
    kana "Fiuhh... akhirnya."
    hide kana_side_talk
    hide kana_talk
    show kana at char_center
    with dissolve
    play sound "audio/SFX - Finish Game.mp3" fadein 0.5 volume (1.0)
    "Setelah waktunya habis, Kana melihat papan high score."
    hide kana
    show kana_talk at char_center
    show kana_side_talk at left with dissolve
    kana "Waaah! [mcname!c] liat! [mcname!c]! Highest score! Yeayy!"
    hide kana_side_talk
    hide kana_talk
    show kana_smile at char_center
    with dissolve
    "[mcname!c]" "Gils jago bangettz."
    hide kana_smile
    show kana_shy_smile at char_center
    show kana_side_shy_smile at left
    with dissolve
    kana "Hehe~"
    hide kana_side_shy_smile
    hide kana_shy_smile
    show kana_shy at char_center
    with dissolve
    "[mcname!c]" "Gimana?"
    hide kana_shy
    show kana_talk at char_center
    show kana_side_talk at left
    with dissolve
    kana "Haha kayaknya udah cukup ya, soalnya udah lumayan lama kita di sini."
    hide kana_talk
    hide kana_side_talk at left
    with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene game center with Dissolve(1.0)
    $ quick_menu = True
    show kana at kana_near
    "Saat [mcname!c] dan Kana mau pulang, tidak sengaja [mcname!c] melihat ada boneka yang diinginkan Kana di dalam box Push Claw Machine."
    "[mcname!c]" "Eh. Itu kan boneka yang kamu pengen?"
    hide kana
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Eh, mana? Mana?"
    hide kana_side_talk with dissolve
    "[mcname!c]" "Ituuu, di kananmu."
    "[mcname!c] menunjuk ke arah crane game."
    show kana_side_talk at left with dissolve
    kana "Wahhh, crane game ya?"
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near
    with dissolve
    "[mcname!c]" "Heee kamu tau crane game, Kana?"
    hide kana
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Mhm... Kalo main gak pernah sih, tapi aku sering denger."
    hide kana_talk 
    show kana at kana_near
    hide kana_side_talk
    with dissolve
    "[mcname!c]" "Mau coba mainin?"
    hide kana
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Ayook!"
    hide kana_talk
    show kana at kana_near
    hide kana_side_talk
    with dissolve
    "Kana mencoba game crane tersebut."
    hide kana
    show crane at crane
    with dissolve
#CG Chibi Kana Claw Machine TANPA MC
    play sound "audio/SFX - Countdown.mp3" fadein 1.0 volume (2.0)
    $ quick_menu = False
    window auto hide
    with Pause(4.5)
    window auto show
    $ quick_menu = True
    stop sound
    "Setelah memperkirakan lokasi yang tepat, akhirnya Kana menekan tombol claw."
    "Claw-nya kemudian turun dan menangkap boneka yang diinginkan Kana."
    "Boneka tersebut terangkat sedikit, sebelum akhirnya terjatuh dan kembali seperti semula."
    hide crane
    show kana_confused at kana_near
    show kana_side_confused at left
    with dissolve
    kana "Nooooo~"
    hide kana_side_confused with dissolve
    "[mcname!c]" "Yaahh~ Sayang banget."
    "[mcname!c]" "Ayo coba lagi."
    hide kana_confused
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Baiklah, sekali lagi!"
    show crane at crane
    hide kana_side_talk
    hide kana_talk
    with dissolve
#CG Chibi Kana Claw Machine TANPA MC*   
    play sound "audio/SFX - Countdown.mp3" fadein 1.0 volume(2.0)
    $ quick_menu = False
    window auto hide
    with Pause(4.0)
    scene black with Dissolve(1.0)
    scene game center with Dissolve(1.0)
    show kana_confused at kana_near with dissolve
    window auto show
    $ quick_menu = True
    stop sound
    "Kana mencoba lagi dan lagi, tetapi hasilnya tetap sama."
    show kana_shy_talk at kana_near
    show kana_side_cry at left
    with dissolve
    kana "Huhu. Ternyata gamenya lumayan susah."
    hide kana_side_cry with dissolve
    "[mcname!c]" "Sini aku bantuin."
    hide kana_confused
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Wihh, okeee. Kali ini pasti bisa!"
#CG Chibi Kana Claw Machine (With MC) Crane 1
    hide kana_side_talk
    hide kana_talk
    hide kana_shy_talk
    show crane1 at crane
    with dissolve
    play sound "audio/SFX - Countdown.mp3" fadein 1.0 volume(2.0)
    $ quick_menu = False
    window auto hide
    with Pause(4.0)
    window auto show
    $ quick_menu = True
    stop sound
    kana "Gimana? Udah pas belum?"
    "[mcname!c]" "Maju dikit lagi tuh."
    kana "Gimana kalo sekarang?"
    "[mcname!c]" "Ke kanan dikittt."
    kana "Gini?"
    "[mcname!c]" "Oke sekarang!!"
    hide crane1
    show crane2 at crane
    with dissolve
    kana "YOSHH!"
    "Kana akhirnya menekan tombol claw."
    hide crane2
    show crane3 at crane
    with dissolve
    kana "Please!!! Pleasee!!!"
    hide crane3 with dissolve
    play sound "audio/SFX - Finish Game 2.mp3" volume (3.0)
    "Terdengar suara boneka jatuh ke kotak hadiah."
    stop sound
    show kana_smile at kana_near
    show kana_side_smile at left
    with dissolve
    kana "YAAAAAYYY!"
    hide kana_side_smile with dissolve
    "Kana kemudian mengambil boneka tersebut dari kotak hadiah dan langsung memeluknya. [mcname!c] melihat pemandangan tersebut sambil tersenyum kecil."
    hide kana_smile
    show kana_shy_smile at kana_near
    show kana_side_shy_smile at left
    with dissolve
    kana "Hehe makasih banyak ya, [mcname!c]. Karena kamu ngebantu arahin, jadi bisa dapet boneka ini."
    hide kana_side_shy_smile
    hide kana_shy_smile 
    show kana_shy at kana_near
    with dissolve
    "[mcname!c]" "Haha gapapa kok, aku seneng juga akhirnya kamu dapet boneka yang kamu pengen."
    hide kana_shy with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Mall.ogg" fadein 1.0
    scene mall with Dissolve(1.0)
    $ quick_menu = True
    "Sepulang dari game arcade..."
    show kana at char_center with dissolve
    "Kana membawa tas belanja dia dan juga boneka yang dia dapat dari claw machine tadi, wajahnya terlihat senang."
    hide kana
    show kana_talk at char_center
    show kana_side_talk at left
    with dissolve
    kana "Makasih ya [mcname!c] untuk hari ini."
    hide kana_side_talk
    hide kana_talk
    show kana at char_center
    with dissolve
    "[mcname!c]" "Iya, sama-sama Kana."
    hide kana
    show kana_talk at char_center
    show kana_side_talk at left
    with dissolve
    kana "Hari ini aku senang banget."
    hide kana_side_talk
    hide kana_talk
    show kana_smile at char_center
    with dissolve
    "Melihat Kana tersenyum, membuat [mcname!c] tersenyum juga..."
    hide kana_smile with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kelas.ogg" fadein 1.0 volume(1.5)
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya..."
    $ quick_menu = False
    scene kelas with Dissolve(2.0)
    #$ renpy.block_rollback()
    show kana at char_center with dissolve
    hide kana
    show kana_talk at char_center
    show kana_side_talk at left
    with dissolve
    $ quick_menu = True
    kana "Pagii [mcname!c]~"
    hide kana_talk
    show kana at char_center
    hide kana_side_talk at left
    with dissolve
    "[mcname!c]" "Pagi juga~"
    hide kana_talk
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Gimana kabarnya hari ini?"
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near
    with dissolve
    "[mcname!c]" "Baik. Gimana kemarin pulangnya? Aman gak?"
    hide kana
    show kana_talk at kana_near
    show kana_side_talk at left with dissolve
    kana "Aman kok. Bareng supir soalnya, hehe."
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near
    with dissolve
    "[mcname!c]" "Wih enak ya punya supir."
    hide kana
    show kana_shy at kana_near
    with dissolve
    hide kana_shy
    show kana_shy_smile at kana_near
    show kana_side_shy_smile at left with dissolve
    kana "Nanti kapan-kapan kamu mau kan nemenin aku lagi?"
    kana "Nanti pulangnya dianter deh."
    hide kana_side_shy_smile
    hide kana_shy_smile
    show kana_shy_closeeye at kana_near
    with dissolve
    "[mcname!c]" "Wahh, okee."
    "Saat Kana dan [mcname!c] sibuk berbincang, Freya datang menghampiri."
    hide kana_shy_closeeye
    show kana at char_right
    show freya at char_left
    with dissolve
    hide freya
    show freya_shock at char_left
    show freya_side_shock at left
    with dissolve
    freya "Pagi Kanaa~ Pagi [mcname!c]~"
    freya "Eh gimana kemarin kalian ngedatenya? Hehehe."
    hide freya_side_shock
    hide freya_shock
    show freya_smug at char_left
    with dissolve
    hide kana
    show kana_shy_smile at char_right
    show kana_side_shy_smile at left
    with dissolve
    kana "Iiihhh ngedate apaan!"
    kana "Kamu kan yang ninggalin kita..."
    hide kana_side_shy_smile
    hide kana_shy_smile
    show kana_shy at char_right
    with dissolve
    "Kana mengatakan hal tersebut sambil tersipu malu."
    "[mcname!c]" "....."
    show freya_side_smug at left with dissolve
    freya "Hmmm?????"
    hide freya_side_smug
    hide kana_shy
    show kana_confused_blush_sideeye at char_right
    with dissolve
    "Freya merasakan respons Kana sedikit berbeda dari biasanya."
    hide freya_smug
    show freya_talk at char_left
    show freya_side_talk at left
    with dissolve
    freya "Seeek too... Ki wes ra bener ki.\n(Bentar... Ini ada yang ga bener nih.)"
    freya "Feelingku mengatakan ada yang mencurigakan."
    hide freya_side_talk
    hide freya_talk
    show freya_awe at char_left
    with dissolve
    hide kana_confused_blush_sideeye
    show kana_confused_blush at char_right
    show kana_side_shy_smile at left with dissolve
    kana "Apaan sihhh, ga ada yang mencurigakan kok."
    hide kana_side_shy_smile
    hide kana_confused_blush
    show kana_shy at char_right
    with dissolve
    hide freya_awe
    show freya_shock at char_left
    show freya_side_shock at left
    with dissolve
    freya "Yang bener????"
    hide freya_side_shock
    hide freya_shock
    show freya_smug at char_left
    with dissolve
    hide kana_shy
    show kana_shy_smile at char_right
    show kana_side_shy_smile at left
    with dissolve
    kana "Apaan sihhh ahh Freya, aku malu tau diliatin gitu mulu."
    hide kana_side_shy_smile
    hide kana_shy_smile
    show kana_shy at char_right
    with dissolve
    show freya_side_smug at left with dissolve
    freya "Hmmmmm..."
    hide freya_side_smug at left with dissolve
    stop music fadeout 1.0
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    "Suara pintu pun terdengar dan dosen datang dengan terburu-buru, berbeda dari biasanya."
    hide freya_smug 
    hide kana_shy 
    with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Dosen.ogg" fadein 1.0
    scene kelas with Dissolve(1.0)
    show kana_shy at char_right
    show freya_smug at char_left
    with dissolve
    hide kana_shy
    show kana_confused_blush at char_right
    show side kana_side_shy_talk at left
    with dissolve
    $ quick_menu = True
    kana "Nah Bu dosen udah dateng tuh, nanti lanjut ngobrol lagi ya."
    hide kana_confused_blush
    hide freya_smug
    hide side kana_side_shy_talk
    with dissolve
    "Mendengar hal tersebut, mereka akhirnya duduk di tempat masing-masing."
    hide kana_confused_blush
    hide freya_smug
    with dissolve
    "Saat duduk di tempatnya, [mcname!c] mendengar sedikit percakapan antara Kana dan Freya."
    show freya at char_left
    show kana at char_right
    with dissolve
    hide freya
    show freya_talk at char_left
    show freya_side_talk at left with dissolve
    freya "Ceritain ya, kalian berdua ngapain aja kemarin."
    hide freya_side_talk
    hide freya_talk
    show freya at char_left
    with dissolve
    hide kana
    show kana_talk at char_right
    show kana_side_talk at left
    with dissolve
    kana "Iya deh, iya."
    hide freya
    hide kana_talk
    hide kana_side_talk at left
    with dissolve
    show dosen_talk at dosen_center
    show dosen_side_talk at left
    with dissolve
    $ quick_menu = True
    dosen "Baiklah semuanya, ibu hari ini akan mengajar dengan cepat karena ada rapat mendadak, jadi harap perhatikan dengan baik dan nantinya akan ada tugas dari ibu."
    hide dosen_side_talk at left
    hide dosen_talk
    show dosen at dosen_center
    with dissolve
    "Dosen pun menjelaskan dan memberikan tugasnya untuk semua mahasiswa/i.."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kelas.ogg" fadein 1.0
    scene kelas with Dissolve(1.0)
    $ quick_menu = True
    "[mcname!c]" "Tumben juga kali ini cepet kelasnya, jadi ada waktu free gini."
    "[mcname!c] melakukan peregangan badan..."
    "[mcname!c]" "Tapi... Tugas yang dikasih juga lumayan banyak."
    show kana_talk at char_center
    show kana_side_talk at left
    with dissolve
    kana "Iya, banyak banget ya tugasnya..."
    kana "Buat tugas ini kamu mau ngerjain bareng ga?"
    hide kana_side_talk
    hide kana_talk
    show kana at char_center
    with dissolve
    "[mcname!c]" "Eh boleh kok."
    "[mcname!c] bingung karena Kana tiba-tiba mengajak untuk mengerjakan tugas."
    "[mcname!c]" "Tapi Freya gimana?"
    hide kana
    show kana at char_right
    show freya_shock at char_left
    show freya_side_shock at left
    with dissolve
    freya "Kalo aku kayaknya bakal besok aja ngerjainnya, soalnya lagi ada barang promo yang mau kubeli."
    freya "Sekalian biar kalian bisa barengan hahaha! Byeeee~"
    hide freya_side_shock
    hide freya_shock
    show kana_confused_blush_sideeye at char_right
    hide kana
    with dissolve
    "Setelah mengatakan hal tersebut Freya langsung pergi meninggalkan kelas..."
    hide kana_confused_blush_sideeye
    show kana_shy_smile at char_right
    show kana_side_shy_smile at left
    with dissolve
    kana "Apaan sih Freya itu, kan niatnya cuma belajar bareng..."
    hide kana_side_shy_smile
    hide kana_confused_blush
    show kana_shy at char_right
    with dissolve
    "[mcname!c]" "Ahahaha."
    "[mcname!c] hanya bisa tertawa canggung mendengar hal tersebut."
    hide kana_shy
    show kana_shy_smile at kana_near
    show kana_side_shy_smile at left
    with dissolve
    kana "Jadi [mcname!c]..."
    hide kana_side_shy_smile
    hide kana_shy_smile
    show kana_shy at kana_near
    with dissolve
    "Kana melihat [mcname!c]."
    hide kana_shy
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Kita ngerjain tugasnya mau di mana?"
    hide kana_talk
    show kana at kana_near
    hide kana_side_talk
    with dissolve
    menu:
        "[mcname!c] menjawab..."
        "Kantin":
            "[mcname!c]" "Hmmmm di kantin gimana? Soalnya bisa sambil ngemil."
            show kana_side_talk at left
            hide kana
            show kana_talk at kana_near
            with dissolve
            kana "Okeee~"
            hide kana_talk
            show kana at kana_near
            hide kana_side_talk
            with dissolve
            "[mcname!c] dan Kana berjalan menuju ke kantin."
            stop music fadeout 1.0
            $ quick_menu = False
            scene black with Dissolve(1.0)
            play music "audio/BGM_Kantin.ogg" fadein 1.0
            scene kantin with Dissolve(1.0)
            #$ renpy.block_rollback()
            play sound "audio/crowd_noise.mp3" loop fadein 1.0 volume (4.0)
            $ quick_menu = True
            "Di kantin terlihat sudah dipenuhi orang sehingga tidak ada tempat kosong untuk duduk..."
            show kana at char_center with dissolve
            "[mcname!c]" "Kayaknya kantin penuh terus yak..."
            hide kana
            show kana_talk at char_center
            show kana_side_talk at left
            with dissolve
            kana "Haha, iya nih."
            kana "Jadinya mau gimana?"
            hide kana_side_talk
            hide kana_talk
            show kana at char_center
            with dissolve
            "[mcname!c]" "Hmmmm mau ke rooftop lagi? Kayaknya di sana bakal sepi."
            hide kana
            show kana_talk at char_center
            show kana_side_talk at left
            with dissolve
            kana "Aku ngikut kamu aja."
            hide kana_side_talk
            hide kana_talk
            show kana at char_center
            with dissolve
            "[mcname!c]" "O-oke."
            "[mcname!c]" "Kalau gitu Kana mau nitip apa? Biar nanti aku bawain."
            hide kana
            show kana_talk at char_center
            show kana_side_talk at left
            with dissolve
            kana "Eh kalo [mcname!c] gimana?"
            hide kana_side_talk
            hide kana_talk
            show kana at char_center
            with dissolve
            "[mcname!c]" "Kamu duluan aja, gapapa."
            "[mcname!c] mengatakan hal tersebut karena tidak ingin membuat Kana menunggu terlalu lama."
            hide kana
            show kana_talk at char_center
            show kana_side_talk at left
            with dissolve
            kana "Oke deh, kalau gitu aku roti strawberry ya."
            hide kana_side_talk
            hide kana_talk
            show kana at char_center
            with dissolve
            "[mcname!c]" "Siapppp~"
            hide kana with dissolve
            "Setelah mengatakan hal tersebut, Kana akhirnya pergi duluan ke rooftop."
            "[mcname!c]" "Sebaiknya aku pesen dulu yang dipesen Kana."
            "[mcname!c] kemudian berjalan menuju kasir."
            "Di sana, [mcname!c] mendengarkan beberapa mahasiswa membicarakan tentang event kampus yang akan segera diadakan."
            "Mahasiswa A" "Eh, katanya event kampus nanti bakal ada lomba-lomba pertunjukan."   
            "Mahasiswa B" "Serius? Emang ada hadiahnya?"
            "Mahasiswa A" "Buat hadiahnya kurang tahu sih."
            "Mahasiswa A ""Tapi guest starnya nanti katanya sih Sabi Yoi."
            "Mahasiswa B" "Duh Sabi Yoi, agak bosen sih dengernya tapi gapapa lah."
            "[mcname!c]" "Heee menarik juga itu..."  
            jump chapter2kanaA
            
        "Rooftop":
            "[mcname!c]" "Hmmmm mau ke rooftop lagi? Kayaknya di sana bakal sepi."
            show kana_side_talk at left
            show kana_talk at kana_near
            with dissolve
            kana "Aku ngikut kamu aja."
            hide kana_side_talk
            hide kana_talk
            show kana at kana_near
            with dissolve
            "[mcname!c]" "O-oke."
            "[mcname!c]" "Kalau gitu aku ke kantin dulu, Kana mau nitip apa? Biar nanti aku bawain."
            hide kana
            show kana_talk at kana_near
            show kana_side_talk at left
            with dissolve
            kana "Eh kalo [mcname!c] gimana?"
            hide kana_side_talk
            hide kana_talk
            show kana at kana_near
            with dissolve
            "[mcname!c]" "Kamu duluan aja, gapapa."
            "[mcname!c] mengatakan hal tersebut karena tidak ingin membuat Kana menunggu terlalu lama."
            hide kana
            show kana_talk at kana_near
            show kana_side_talk at left
            with dissolve
            kana "Oke deh, kalau gitu aku roti strawberry ya."
            hide kana_side_talk
            hide kana_talk
            show kana at kana_near
            with dissolve
            "[mcname!c]" "Siapppp~"
            hide kana with dissolve
            "Setelah mengatakan hal tersebut, Kana akhirnya pergi duluan ke rooftop."
            "[mcname!c] pun berjalan menuju ke kantin."
            stop music fadeout 1.0
            $ quick_menu = False
            scene black with Dissolve(1.0)
            play music "audio/BGM_Kantin.ogg" fadein 1.0
            scene kantin with Dissolve(1.0)
            #$ renpy.block_rollback()
            play sound "audio/crowd_noise.mp3" loop fadein 1.0 volume (4.0)
            $ quick_menu = True
            "[mcname!c]" "Hmmm, sebaiknya aku pesen dulu yang dipesen Kana."
            "[mcname!c] kemudian berjalan menuju kasir."
            "Di sana, [mcname!c] mendengarkan beberapa mahasiswa membicarakan tentang event kampus yang akan segera diadakan."
            "Mahasiswa A" "Eh, katanya event kampus nanti bakal ada lomba-lomba pertunjukan."   
            "Mahasiswa B" "Serius? Emang ada hadiahnya?"
            "Mahasiswa A" "Buat hadiahnya kurang tahu sih."
            "Mahasiswa A ""Tapi guest starnya nanti katanya sih Sabi Yoi."
            "Mahasiswa B" "Duh Sabi Yoi, agak bosen sih dengernya tapi gapapa lah."
            "[mcname!c]" "Heee menarik juga itu..."
            jump chapter2kanaA

label chapter2kanaA:
    stop sound fadeout 1.0
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Rooftop Siang.ogg" fadein 1.0 volume 2.0
    scene rooftop with Dissolve(1.0)
    #$ renpy.block_rollback()
    $ quick_menu = True
    "Selangkah demi selangkah, [mcname!c] menanjaki anak tangga menuju rooftop."
    "Di tangannya ada 2 roti untuk menemani[mcname!c] dan Kana saat mengerjakan tugas nanti." 
    "Saat sampai di sana, terlihat Kana sudah menunggu [mcname!c]."
    "Menyadari keberadaan [mcname!c], Kana memanggil sambil tersenyum."
    show kana_talk at char_center with dissolve
    show kana_side_talk at left with dissolve
    kana "Ah [mcname!c]."
    hide kana_side_talk
    hide kana_talk
    show kana_smile at char_center
    with dissolve
    "[mcname!c]" "Maaf ya, bikin nunggu."
    hide kana_smile
    show kana_talk at char_center
    show kana_side_talk at left
    with dissolve
    kana "Gapapa kok. Makasih ya udah beliin roti."
    hide kana_side_talk
    hide kana_talk
    show kana at char_center
    with dissolve
    "[mcname!c] dan Kana kemudian makan bersama sambil mengerjakan tugas. Sesekali terdengar canda tawa kecil di pembicaraan mereka."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene rooftop with Dissolve(1.0)
    show kana at char_center with dissolve
    $ quick_menu = True    
    "[mcname!c]" "Fuuu kayaknya kita istirahat dulu sebentar, soalnya sudah lumayan lama ngerjain tugas."
    hide kana
    show kana_confused at char_center
    show kana_side_confused at left
    with dissolve
    kana "Iya nih, udah lumayan mumet juga."
    hide kana_side_confused with dissolve
    "[mcname!c]" "Oh iya, denger-denger katanya kampus kita bakal ada event buat ulang tahun kampus nanti."
    hide kana_confused
    show kana_talk at char_center
    show kana_side_talk at left
    with dissolve
    kana "Ehhh serius? Gak sabar jadinya, hehe."
    hide kana_side_talk
    hide kana_talk
    show kana_smile at char_center
    with dissolve
    "Kana terlihat sangat bersemangat, seperti sangat menantikan hal tersebut."
    "[mcname!c]" "Kayaknya kamu suka ya sama event-event kayak gitu."
    "[mcname!c]" "Sering ke event?"
    hide kana_smile
    show kana_confused_blush at char_center
    show side kana_side_shy_talk at left
    with dissolve
    kana "E-eh??!"
    hide side kana_side_shy_talk with dissolve
    "Kana agak terkejut."
    hide kana_confused_blush
    show kana_confused at char_center
    show kana_side_confused at left
    with dissolve
    kana "E-enggak..."
    kana "Soalnya kan dulu waktu aku kecil sering sakit, pas ada acara-acara kayak gitu aku gak bisa ikut dan cuma di rumah aja..."
    kana "Jadi pas ada event-event begitu, aku suka sama suasananya yang meriah gitu."
    hide kana_side_confused
    with dissolve
    "[mcname!c]" "Heeeee~"
    "[mcname!c]" "{i}Iya sih, Kana waktu dulu sering sakit ya.{/i}"
    "[mcname!c]" "Moga aja eventnya nanti berjalan lancar."
    hide kana_confused
    show kana_drylaugh at char_center
    show kana_side_drylaugh at left
    with dissolve
    kana "Iya, hehe."
    hide kana_drylaugh
    show kana at char_center
    hide kana_side_drylaugh
    with dissolve
    "[mcname!c]" "Okee! Lanjut nugaas~"
    "Kana dan [mcname!c] kembali mengerjakan tugas."
    hide kana with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Rooftop Sore.ogg" fadein 1.0 volume 2.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Tak terasa waktu telah menjadi sore."
    $ quick_menu = False
    scene rooftop sore with Dissolve(2.0)
    show kana at char_center with dissolve
    $ quick_menu = True
    "[mcname!c]" "Gimana Kana? Udah beres?"
    hide kana
    show kana_talk at char_center
    show kana_side_talk at left
    with dissolve
    kana "Udaah. Thank you udah mau ngerjain tugas bareng."
    hide kana_side_talk
    hide kana_talk
    show kana_smile at char_center
    with dissolve
    "[mcname!c]" "Anytime, Kana."
    hide kana_smile
    show kana_talk at char_center
    show kana_side_talk at left
    with dissolve
    kana "Oke, kalo gitu aku pulang dulu ya."
    kana "Lain kali kita ngerjain tugas bareng lagi yaa, dadahh."
    hide kana_side_talk
    hide kana_talk
    with dissolve
    "[mcname!c]" "Okee, daah~"
    "Kana dan [mcname!c] pulang ke rumah masing-masing."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kampus.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya..."
    $ quick_menu = False
    play sound "audio/crowd_noise.mp3" loop fadein 1.0 volume (6.0)
    scene depan kampus with Dissolve(2.0)
    #$ renpy.block_rollback()
    $ quick_menu = True
    "Suasana jalan di kampus lebih terasa lebih ramai daripada biasanya."
    "Banyak orang-orang yang sedang lalu lalang dan menyerahkan beberapa flyer yang entah isinya apa."
    "Bahkan ada yang memaksa beberapa mahasiswa/i untuk menerima flyer tersebut."
    show kana at char_center with dissolve
    "[mcname!c]" "Ehh, hari ini kok ramai banget ya? Ga kaya biasanya, lagi ada acara kah?"
    hide kana
    show kana_talk at char_center
    show kana_side_talk at left
    with dissolve
    kana "Wah aku juga ga tauu. Event kampus yang kamu bilang kemarin masih lama, kan?"
    hide kana_side_talk
    hide kana_talk
    show kana at char_center
    with dissolve
    "[mcname!c]" "Harusnya sih iya. Yaudah, kita ke kelas yuk."
    hide kana
    show kana_talk at char_center
    show kana_side_talk at left
    with dissolve
    kana "Okee."
    hide kana_side at left
    hide kana_talk
    hide kana_side_talk
    with dissolve
    stop sound fadeout 1.0
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Lorong.ogg" fadein 1.0
    scene lorong with Dissolve(1.0)
    $ quick_menu = True
    "Saat Kana dan [mcname!c] berjalan bersama menuju kelas, tiba-tiba seseorang datang mendekat." 
    show tana_shock at char_center
    show tana_side_shock at left
    with dissolve
    tana "Ehhhh brooo bentarr duluuu!!"
    hide tana_side_shock
    hide tana_shock
    show tana_confused at char_center
    with dissolve
    "Terlihat seorang cewek tinggi dengan perawakan tomboy berambut pendek merah yang mengingatkan [mcname!c] kepada CABE KERING yang sering mamanya jemur di desa."
    "Kana dan [mcname!c] merasa bingung karena tiba-tiba dihentikan cewek tersebut." 
    "Seperti sadar dengan orang tersebut, tiba-tiba Kana bersembunyi di belakang [mcname!c] sambil mencoba menghindar dari tatapan cewek itu." 
    "[mcname!c]" "Uumm kenapa ya, Kak?"
    hide tana_confused
    show tana_shock at char_center
    show tana_side_shock at left
    with dissolve
    tana "Bentar dah, kayaknya gue pernah liat lu di event-event dah."
    hide tana_side_shock
    hide tana_shock
    show tana_confused at char_center
    with dissolve
    "[mcname!c]" "Gue?" 
    "Sambil terheran heran, [mcname!c] menunjuk dirinya sendiri dan bertanya apakah dia adalah orang yang cewek itu maksud."
    hide tana_confused
    show tana_shock at char_center
    show tana_side_shock at left
    with dissolve
    tana "Ahhhh bukan kocak, dia loh."
    hide tana_side_shock
    hide tana_shock
    show tana_confused at char_center
    with dissolve
    "Jari cewek itu menunjuk ke arah belakang [mcname!c]."
    "Saat itu pun Kana mulai gelisah dan menundukkan kepalanya, mencoba menyembunyikan wajahnya dari cewek tersebut."
    "[mcname!c]" "Hah? Kana?"
    hide tana_confused
    show tana at char_left
    show kana_confused_blush_sideeye at char_right
    with dissolve
    hide kana_confused_blush_sideeye
    show kana_confused_blush at char_right
    show kana_side_cry at left
    with dissolve
    kana "Ehh... Uuu k-kenapa ya Mba?"
    hide kana_side_cry
    hide kana_confused_blush
    show kana_shy_talk at char_right
    with dissolve
    "Dengan ragu dan perlahan, Kana pun melihat ke arah cewek itu."
    hide tana
    show tana_talk at char_left
    show tana_side_talk at left
    with dissolve
    tana "Nahhhh kan, benerrr feeling gue tuh. Elu kan yang sering dateng ke event jejepangan."
    hide tana_side_talk
    hide tana_talk
    show tana at char_left
    with dissolve
    hide kana_shy_talk
    show kana_drylaugh at char_right
    show kana_side_drylaugh at left
    with dissolve
    kana "Ehhh, s-salah orang kali. Hahaha."
    hide kana_side_drylaugh with dissolve
    hide tana
    show tana_talk at char_left
    show tana_side_talk at left
    with dissolve
    tana "Aahh, ga pernah salah kalau gue mah kocak. Tiap gue ke event jejepangan, keknya selalu ngeliat lu."
    hide tana_side_talk
    hide tana_talk
    show tana at char_left
    hide kana_drylaugh
    show kana_shy_talk at char_right
    with dissolve
    "[mcname!c]" "Eh? Kamu sering ke event jejepangan, Kana?"
    hide kana_shy_talk
    show kana_confused_blush_sideeye at char_right
    show kana_side_cry at left
    with dissolve
    kana "Haa... masa sih? A-aku ga pernah ikut kaya gituan kok... Aku kan bukan wibu."
    hide kana_side_cry at left with dissolve
    hide tana
    show tana_talk at char_left
    show tana_side_talk at left
    with dissolve
    tana "Ah masa sih? Kamu kan yang biasanya wotagei paling semangat di event-event jejepangan."
    hide tana_side_talk
    show tana_confused at char_left
    hide kana_confused_blush_sideeye
    show kana_confused_blush at char_right
    show kana_side_cry at left
    with dissolve
    kana "Ah eh ah eh..."
    hide kana_side_cry
    hide kana_confused_blush
    with dissolve
    play sound "audio/run.mp3" fadein 1.0 volume (10.0)
    "Kana pun kabur secepat mungkin, tidak peduli dengan orang yang ada di sekitar."
    hide tana_confused
    show tana_shock at char_left
    show tana_side_shock at left
    with dissolve
    tana "Lah, itu orang napa malah kabur dah."
    show tana_talk at char_left
    show tana_side_talk at left
    hide tana_shock at char_left
    hide tana_side_shock at left
    with dissolve
    tana "Ya udah ini buat lu aja."
    show poster1 at poster
    hide tana_side_talk
    hide tana_talk
    with dissolve
    "Cewek tersebut memberikan flyer ke arah [mcname!c] dan pergi dari tempat tersebut."
    "[mcname!c]" "??????? Ada apa ini????!!!!"
    hide poster1 with dissolve
    "[mcname!c]" "Ah yaudah lah. Fokus kelas dulu."
    stop sound fadeout 1.0
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_sore.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Setelah kelas selesai, [mcname!c] berjalan ke luar kelas."
    $ quick_menu = False
    scene lorong sore with Dissolve(2.0)
    $ quick_menu = True
    "Tingkah laku Kana tadi pagi masih menjadi tanda tanya yang besar di dalam pikiran [mcname!c]. Hal ini membuat [mcname!c] tidak fokus dengan kelas dan melamun sendiri."
    "[mcname!c]" "{i}Hmmmmm…. Kana ke mana, ya? Padahal tadi pagi ada… Apa jangan-jangan karena kejadian tadi pagi?{/i}"
    "Saat memikirkan kejadian pagi tadi, tiba-tiba ada seseorang yang membuyarkan pikirannya."
    "???" "Eh ngapain [mcname!c], dari tadi asik sendiri."
    show freya at char_center with dissolve
    "[mcname!c]" "Ah? Freya?"
    hide freya
    show freya_talk at char_center
    show freya_side_talk at left
    with dissolve
    freya "Iya. Btw Kana mana? Tadi pagi kan harusnya bareng kamu."
    hide freya_side_talk
    hide freya_talk
    show freya at char_center
    with dissolve
    "[mcname!c]" "Iya tadi pagi barengan. Tapi Kana tiba-tiba kabur sesudah dikasih flyer ini."
    "[mcname!c] kemudian menunjukkan flyernya kepada Freya."
#MUNCUL FLYER RECRUIT ANGGOTA KLUB JEPANG
    show poster1 at poster
    hide freya
    show freya_side_awe at left
    with dissolve
    freya "............."
    hide freya_side_awe with dissolve
    "Freya membaca flyer yang diberikan [mcname!c]."
    "[mcname!c]" "Denger-denger, emangnya Kana wibu?"
#MUNCUL FLYER RECRUIT ANGGOTA KLUB JEPANG HIDE
    hide poster1
    hide freya_awe
    show freya_shock at char_center
    show freya_side_shock at left
    with dissolve
    freya "Heeee? Aku kira Naya udah cerita."
    hide freya_side_shock with dissolve
    "[mcname!c]" "Emang cerita apa?"
    hide freya_shock
    show freya_smug at char_center
    show freya_side_smug at left
    with dissolve
    freya "Hmmm..."
    freya "Ga jadi deh."
    hide freya_side_smug with dissolve
    "Seolah tidak ingin membahasnya Freya menghentikan topik tersebut."
    "[mcname!c] semakin kebingungan dengan semua kejadian hari ini."
    hide freya_smug with dissolve
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" fadein 1.0
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Malam itu di kost..."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(2.0)
    #$ renpy.block_rollback()
    $ quick_menu = True
    "Malamnya setelah pulang dari kampus, [mcname!c] langsung merebahkan diri di kasurnya tanpa berganti pakaian."
    "[mcname!c]" "Haaaahhhhh..."
    "[mcname!c]" "{i}Hari ini terasa sangat panjang.{/i}"
    "[mcname!c]" "{i}Hmmm Kana ke mana yah?{/i}"
    "Kepikiran tentang Kana yang tidak masuk kelas hari ini, akhirnya [mcname!c] mencoba menghubungi Kana lewat chat."
    "[mcname!c]" "{i}Chat ah.{/i}"
    "[mcname!c] kemudian membuka HPnya."
    $ quick_menu = False
    nvl clear
    #Mobile Phone
    mc_nvl "Kana, kamu gapapa?"
    nvl clear
    $ quick_menu = False
    scene kamar mc kota with dissolve
    $ quick_menu=True
    "......"
    "Tidak ada respon dari Kana."
    $ quick_menu = False
    mc_nvl "{image=mengsedih.png}"
    nvl clear
    $ quick_menu = False   
    scene kamar mc kota with dissolve
    $ quick_menu=True
    "[mcname!c]" "Hmmm gak dibales."
    #*Balik BG Kamar*
    "[mcname!c]" "Semoga besok pagi Kana masuk ke kampus deh."
    "Setelah itu [mcname!c] menutup matanya dan langsung tidur."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kelas.ogg" fadein 1.0 volume(1.5)
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya..."
    $ quick_menu = False
    play sound "audio/crowd_noise.mp3" loop fadein 1.0 volume (4.0)
    scene kelas with Dissolve(2.0)
    #$ renpy.block_rollback()
    $ quick_menu = True
    "Pagi itu kelas terlihat ramai oleh mahasiswa/i, namun Kanaia Asa tidak terlihat di mana pun."
    "[mcname!c]" "{i}Kayaknya hari ini Kana gak masuk juga ya.{/i}"
    "[mcname!c] mencoba melihat sekitar namun tetap saja hasilnya nihil."
    "[mcname!c]" "{i}Mungkin aku coba tanyakan ke Freya nanti.{/i}"
    stop sound fadeout 1.0
    stop music fadeout 1.0
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    "Pintu terbuka dan terlihat dosen memasuki kelas."
    play music "audio/BGM_Dosen.ogg" fadein 1.0
    show dosen_talk at dosen_center
    show dosen_side_talk at left
    with dissolve
    $ quick_menu = True
    dosen "Baiklah anak-anak mari kita mulai kelas hari ini."
    hide dosen_side_talk
    hide dosen_talk
    with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Sore.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Beberapa jam kemudian..."
    $ quick_menu = False
    scene kelas sore with Dissolve(2.0)
    show dosen at dosen_center with dissolve
    hide dosen
    show dosen_talk at dosen_center
    show dosen_side at left
    with dissolve
    $ quick_menu = True
    dosen "Oke terima kasih untuk hari ini, jangan lupa untuk selalu jaga kesehatan ya."
    hide dosen_side
    hide dosen_talk
    with dissolve
    "Bu Dosen pun beranjak pergi dari kelas."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene kelas sore with Dissolve(1.0)
    $ quick_menu = True
    "[mcname!c]" "{i}Oke Bu Dosen sudah keluar.{/i}"
    "[mcname!c]" "{i}Mungkin aku coba tanyakan ke Freya tentang masalah Kana.{/i}"
    "[mcname!c] pun kemudian berjalan mendekati Freya."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene lorong sore with Dissolve(1.0)
    show freya at char_center with dissolve
    $ quick_menu = True
    "[mcname!c]" "Freya kamu tau gak Kana di mana?"
    "[mcname!c]" "Soalnya udah dua hari ini gak masuk kelas, aku chat juga gak dibales."
    hide freya
    show freya_talk at char_center
    show freya_side_talk at left
    with dissolve
    freya "Iya nih, aku juga gak dikabarin sama dia."
    hide freya_side_talk
    hide freya_talk
    show freya_pouting at char_center
    with dissolve
    "[mcname!c]" "Duh jadi gimana ya ini? Aku agak khawatir."
    hide freya_pouting
    show freya_talk at char_center
    show freya_side_talk at left
    with dissolve
    freya "Mungkin nanti aku coba datengin ke rumahnya nih, kali aja dia kenapa-napa."
    hide freya_side_talk
    hide freya_talk
    show freya at char_center
    with dissolve
    "[mcname!c]" "Oke deh Freya, tolong banget ya."
    hide freya with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kampus.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Beberapa hari telah berlalu..."
    "Tapi Kana tetap tidak terlihat di kampus..."
    $ quick_menu = False
    scene depan kampus with Dissolve(2.0)
    $ quick_menu = True
    "[mcname!c]" "{i}Duh kata Freya nanti dia bakal ke rumah Kana buat mastiin kabar Kana...{/i}"
    "[mcname!c]" "{i}Tapi tetep aja aku gak bisa berhenti kepikiran tentang Kana.{/i}"
    "[mcname!c]" "Haaaahh..."
    "[mcname!c]" "{i}Mungkin ku coba nenangin diri dulu sambil jalan-jalan sebelum balik ke kost.{/i}"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Mall.ogg" fadein 1.0
    scene mall with Dissolve(1.0)
    $ quick_menu = True
    "Karena bingung mau ke mana, akhirnya [mcname!c] ke mall yang pernah dia datangi bersama Kana dulu."
    "[mcname!c]" "{i}Duh niatnya pengen nenangin diri tapi ujung-ujungnya malah ke sini.{/i}"
    "[mcname!c]" "Yah tapi cuma di sini sih, tempat yang aku tau di Jakarta."
    "[mcname!c] kemudian berkeliling melihat-lihat di mall."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    with Pause (2.0)
    scene mall temp with Dissolve(1.0)
    $ quick_menu = True
    "[mcname!c]" "Eh itu kan?"
    show kana seifuku at seifuku
    "Saat berkeliling, [mcname!c] melewati toko baju yang pernah dia lewati waktu bersama Kana."
    "[mcname!c]" "Kalo gak salah, waktu itu Kana ngeliatin baju ini lumayan lama ya.."
    "[mcname!c]" "Hmmmm..."
    play sound "audio/cafe-entrance.mp3" fadein 1.0 volume(7.0)
    "[mcname!c]" "Permisii~"

    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Kelas.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya..."
    $ quick_menu = False
    scene kelas with Dissolve(2.0)
    $ quick_menu = True
    "[mcname!c]" "Hmmm...."
    "[mcname!c]" "Kana masih nggak masuk kelas juga..."
    stop music fadeout 1.0
    "Saat [mcname!c] termenung, Dosen membuka pintu dan masuk ke kelas."
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    play music "BGM_Dosen.ogg" fadein 1.0
    $ quick_menu = True
    show dosen_talk at dosen_center
    show dosen_side_talk at left
    with dissolve
    dosen "Baik, kelas akan dimulai ya..."
    hide dosen_talk at dosen_center
    hide dosen_side_talk at left
    with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene kelas with Dissolve(1.0)
    $ quick_menu = True
    "Saat Bu Dosen sedang menjelaskan kuliah..."
    show dosen_talk at dosen_center
    show dosen_side_talk at left
    with dissolve
    dosen "Sepertinya beberapa hari ini Kana absen terus ya?"
    hide dosen_side_talk
    hide dosen_talk
    show dosen at dosen_center
    with dissolve
    "Mendengar Bu Dosen mengatakan nama Kana, [mcname!c] pun sedikit terkejut."
    hide dosen
    show dosen_talk at dosen_center
    show dosen_side_talk at left
    with dissolve
    dosen "Tadi saya sudah dapat informasi dari orang tuanya Kana, kalau Kana izin sakit jadi tidak bisa masuk."
    hide dosen_side_talk 
    hide dosen_talk
    with dissolve
    "[mcname!c]" "{i}Hah? Kana sakit?{/i}"
    "[mcname!c]" "{i}Ku coba tanyain langsung ke Freya dah, kan dia habis dari rumah Kana kemarin.{/i}"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Sore.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Setelah kelas selesai..."
    $ quick_menu = False
    scene lorong sore with Dissolve(1.0)
    show freya at char_center with dissolve
    $ quick_menu = True
    "[mcname!c]" "Freya, emang bener kalo Kana lagi sakit?"
    "Setelah kelas berakhir, [mcname!c] langsung mendekati Freya yang membuatnya agak terkejut."
    hide freya
    show freya_awe at char_center
    show freya_side_awe at left
    with dissolve
    freya "Ah, [mcname!c]?"
    freya "Masalah itu ya..."
    freya "Mungkin kamu udah tau duluan, tapi Kana itu dulu tubuhnya lemah."
    freya "Jadi gak bisa ngelakuin hal-hal normal yang kayak orang lain."
    freya "Akhirnya dia sering ngehabisin waktunya dirumah, ngewibu."
    freya "Dan mungkin karena hal tesebut, jadinya dia dijauhin temen sekelasnya waktu masih sekolah."
    freya "Sampai akhirnya dia balik nenutup diri di kamarnya terus."
    freya "Aku gak begitu tau gimana cerita dia sepenuhnya, soalnya waktu itu aku juga lagi ikut orang tuaku karena kerjaan di luar kota."
    freya "Untung aja waktu aku kembali ke sini, Kana jadi mulai membuka diri lagi dan mencoba kembali bersosialisasi."
    freya "Tapi entah kenapa sekarang dia malah kembali menjadi seperti dulu."
    hide freya_side_awe
    hide freya_awe
    show freya at char_center
    with dissolve
    "Setelah memberikan ringkasan tentang masalalu Kana, Freya pun menatap [mcname!c]."
    hide freya
    show freya_shock at tana_near
    show freya_side_shock at left
    with dissolve
    freya "Oleh karena itu [mcname!c], tolong."
    hide freya_side_shock
    hide freya_shock
    show freya_smug at tana_near
    with dissolve
    "Freya menepuk kedua tangannya seperti memohon."
    hide freya_smug
    show freya_shock at tana_near
    show freya_side_shock at left
    with dissolve
    freya "Aku gak pengen Kana balik seperti dulu yang menutup dirinya lagi."
    freya "Jadi bisa gak kalo kamu bujuk dia buat kembali..."
    hide freya_side_shock
    hide freya_shock
    show freya at tana_near
    with dissolve
    "[mcname!c]" "Eh aku??"
    "[mcname!c] bingung kenapa Freya minta tolong padanya."
    "[mcname!c]" "Bukannya kamu ya, temen deketnya Kana dari dulu?"
    hide freya
    show freya_pouting at tana_near
    show freya_side_pouting at left
    with dissolve
    freya "Soalnya kemarin waktu aku ke sana, aku gak dibolehin masuk sama Naya."
    freya "Jadi aku rasa mungkin cuma kamu yang bisa."
    hide freya_side_pouting
    hide freya_pouting
    show freya_talk at tana_near
    show freya_side_talk at left
    with dissolve
    freya "Apalagi beberapa hari ini kalian berdua deket banget, jadi aku yakin pasti berhasil."
    hide freya_talk at tana_near
    hide freya_side_talk at left
    show freya at tana_near
    with dissolve
    "[mcname!c] sedikit malu karena dibilang dekat dengan Kana."
    "Tapi kemudian menggeleng-gelengkan kepalanya untuk kembali fokus."
    "[mcname!c]" "Oke deh bakal ku coba."
    "Kata [mcname!c] setelah memantapkan dirinya."
    hide freya
    show freya_talk at tana_near
    show freya_side_talk at left
    with dissolve
    freya "Makasih banyak [mcname!c]."
    hide freya_side_talk
    hide freya_talk
    show freya_smile at char_center
    with dissolve
    "Freya tersenyum senang dengan jawaban [mcname!c]."
    hide freya_smile
    show freya_talk at char_center
    show freya_side_talk at left
    with dissolve
    freya "Ini alamatnya Naya, ya."
    freya "Good luck~"
    hide freya_side_talk
    hide freya_talk
    with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kampus Sore.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Pulang dari kampus, [mcname!c] menuju ke rumah Kana."
    "[mcname!c]" "Uhhh, belok kanan di sebelah sini."
    "Itu perjalanan yang bisa dibilang cukup jauh dari stasiun kereta yang sering [mcname!c] pakai."
    "Komplek perumahan yang dituju [mcname!c] katanya dikenal dengan perumahan yang cukup mewah."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    pause(1.0)
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Setelah beberapa saat..."
    show pintu_rumah_kana at pintu_rumah_kana
    "[mcname!c]" "Jadi ini rumah Kana."
    "Terlihat rumah yang cukup mewah, bahkan lebih besar dari rumah [mcname!c] di kampung."
    "[mcname!c]" "Kalau gak salah, pernah denger kalo Kana itu orang kaya."
    "[mcname!c]" "Tapi gak nyangka bakal sebesar ini."
    play sound "audio/ding.mp3" volume(3.0)
    "[mcname!c] pun kemudian mencoba membunyikan bel yang ada di dekat pintu."
    "Tidak lama setelah bel berbunyi, terdengar suara langkah kaki menuju pintu depan."
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    hide pintu_rumah_kana at pintu_rumah_kana
    "????" "Iya cari siapa yaa???"
    "Terlihat seorang wanita cantik yang membukakan pintu."
    "Wanita tersebut terlihat cukup muda, terlihat mungkin sekitar 20 tahunan."
    "[mcname!c]" "{i}Sepertinya dia kakaknya Kana.{/i}"
    "[mcname!c]" "Saya [mcname!c], teman sekampusnya Kana."
    "[mcname!c] kemudian memperkenalkan diri kepada wanita tersebut."
    "[mcname!c]" "Saya mau menjenguk Kana karena katanya lagi sakit."
    "????" "Ahhh [mcname!c]? Kana sering banget nyeritain tentang kamu, hahaha."
    "????" "Ayo sini masuk dulu."
    "[mcname!c]" "Makasih banyak Kak."
    "????" "Loh kok \"Kak\"?"
    "[mcname!c]" "Eh??"
    "[mcname!c]" "Kakaknya Kana kan?"
    "[mcname!c] bingung takut membuat wanita itu tersinggung."
    "Mamah Kana" "Eehhh? Emang saya terlihat semuda itu ya? Saya mamahnya Kana, haha."
    "[mcname!c]" "Eh maaf tante, saya kira kakaknya Kana soalnya keliatan masih muda."
    "Mamah Kana" "Fufufu bisa aja kamu. Yaudah, sini masuk dulu."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Ruang Tamu.ogg" fadein 1.0
    scene ruang tamu sore with Dissolve(1.0)
    $ quick_menu = True
    "Di ruang tamu, Mamah Kana bercerita tentang bagaimana keadaan Kana yang sampai sekarang tidak mau keluar kamar."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene ruang tamu sore with Dissolve(1.0)
    $ quick_menu = True
#MUNCUL SPRITE PINTU KAMAR KANA
    show pintu_kamar_kana at pintu_kamar_kana with dissolve
    "Setelah berbincang, [mcname!c] akhirnya berada di depan pintu Kamar Kana."
    "[mcname!c] berhenti sebentar, memikirkan cara untuk membujuk Kana."
    "Tetapi kemudian menggelengkan kepala."
    "[mcname!c]" "{i}Ah, kebanyakan mikir juga ga ngubah keadaan.{/i}"
    "[mcname!c]" "Yosh!"
    play sound "SFX - Knocking.mp3" volume(2.0)
    "[mcname!c]" "Kanaaa, kamu di sana??"
    "[mcname!c] menunggu respon dari Kana."
    "Seperti yang diduga, tidak ada jawaban dari Kana."
    "Namun menurut perkataan Mamahnya, Kana mengurung diri di dalam kamarnya selama beberapa hari ini."
    menu:
        "Yang kamu lakukan..."
        "Stop di sini.":
            stop music fadeout 1.0
            $ quick_menu = False
            play music "BGM_Bad End.ogg" fadein 1.0
            "[mcname!c]" "{i}Sepertinya Kana tidak bisa ku ganggu.{/i}"
            "[mcname!c]" "{i}Mungkin kubiarkan aja dulu.{/i}"
            scene black with dissolve
            show text "{color=#FFF}*AKHIRNYA KAMU MUNDUR DARI KAMARNYA KANA DAN MEMILIH UNTUK MENDEKATI MAMAHNYA*{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FF0000}BAD END(?)\nWIN FOR SOME{/color}" with Pause(2.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits
        "\"Buka pintu.\"":
            "[mcname!c]" "Kana... Aku masuk ke kamar, ya..."
            "[mcname!c]" "Kalau kamu gak suka, nanti ngomong aja ya."
            "[mcname!c] kemudian meraih gagang pintu kamarnya Kana."
            "[mcname!c] rasa jika dia berhenti sekarang, maka Kana akan mengurung dirinya lebih lama."
            "Pintu kamarnya tidak di kunci."
            "[mcname!c] tahu itu karena sudah diberitahu oleh Mamahnya Kana."
            stop music fadeout 1.0
            $ quick_menu = False
            play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
            scene black with Dissolve(1.0)
            $ quick_menu=True
            "Saat [mcname!c] memasuki kamar lalu menutup pintu, terasa kegelapan menyelimuti kamar itu."
            jump chapter2kanaB

label chapter2kanaB:
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Sad Piano.ogg" fadein 1.0
    scene kamar kana sore with Dissolve(2.0)
    $ quick_menu = True
    "Dari balik tirai jendela terlihat ada cahaya yang muncul, membantu mata [mcname!c] menyesuaikan dengan kegelapan sekitar."
    "Kamarnya Kana terasa berbeda, mengeluarkan aroma khas yang mencerminkan kepribadiannya. Entah kenapa tercium aroma lautan yang segar."
    "Saat [mcname!c] mencoba memperhatikan sekitar, terdengar suara memanggil namanya."
    show kana_home_side_shy_ahn at left with dissolve
    kana "[mcname!c]..."
    hide kana_home_side_shy_ahn with dissolve
    "[mcname!c]" "Huh, jangan-jangan yang di dalam selimut itu kamu, Kana?"
    show kana_home_side_shy_hmph at left with dissolve
    kana "Umnnn..."
    hide kana_home_side_shy_hmph with dissolve
    "[mcname!c]" "......."
    "[mcname!c]" "Kana, aku ke sana ya."
    show kana_home_side_shy_ahn at left with dissolve
    kana "Mmmmm... iya."
    hide kana_home_side_shy_ahn with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene kamar kana sore with Dissolve(1.0)
    show kana_home at char_center with dissolve
    $ quick_menu = True
    "Kana terlihat duduk di ranjang, menyelimuti dirinya dengan selimut sambil memeluk kakinya."
    "Kana terlihat sedikit gemetar, seperti anak yang sedang menunggu orang tuanya pulang ke rumah."
    "[mcname!c]" "Kana, kamu gapapa? Katanya sakit."
    hide kana_home
    show kana_home_shy_closeeye_talk at char_center
    show kana_home_side_shy_hmph at left
    with dissolve
    kana "Umnn."
    hide kana_home_side_shy_hmph
    hide kana_home_shy_closeeye_talk
    show kana_home_shy at char_center
    with dissolve
    "[mcname!c] kemudian mengambil kursi dan mendekatkan kursi tersebut ke kasur Kana."
    "[mcname!c]" "Aku duduk ya."
    "Tanpa menunggu respon dari Kana, [mcname!c] langsung duduk di kursi tersebut."
    "[mcname!c]" ".........."
    show kana_home_side_shy_ahn at left with dissolve
    kana ".............."
    hide kana_home_side_shy_ahn with dissolve
    "[mcname!c]" "Kamu gapapa?"
    show kana_home_side_shy_ahn at left with dissolve
    kana "............"
    hide kana_home_side_shy_ahn with dissolve
    "[mcname!c]" "............"
    hide kana_home_shy
    show kana_home_shy_smile at char_center
    show kana_home_side_shy_eh at left
    with dissolve
    kana "Kok kamu ke sini? Pasti dikasih tau Freya, ya?"
    hide kana_home_side_shy_eh
    hide kana_home_shy_smile
    show kana_home_shy at char_center
    with dissolve
    "[mcname!c]" "Aku khawatir sama kamu, Kana. Soalnya kamu udah gak masuk kuliah berhari-hari."
    hide kana_home_shy
    show kana_home_confused_blush at char_center
    show kana_home_side_confused_blush at left
    with dissolve
    kana "........"
    kana "Kok kamu khawatir sama aku? Kamu gapapa ke sini?"
    hide kana_home_side_confused_blush
    hide kana_home_confused_blush
    show kana_home_shy at char_center
    with dissolve
    "[mcname!c]" "Eh? Kenapa kamu ngomong begitu?"
    hide kana_home_shy
    show kana_home_shy_closeeye_talk at char_center
    show kana_home_side_shy_ahn at left
    with dissolve
    kana "Aku ga mau waktumu yang berharga dihabisin kayak gini."
    hide kana_home_side_shy_ahn
    hide kana_home_shy_closeeye_talk
    show kana_home_shy at char_center
    with dissolve
    "[mcname!c]" "Nggak kok, kamu lebih berharga dari waktuku."
    hide kana_home_shy
    show kana_home_confused_blush at char_center
    show kana_home_side_confused_blush at left
    with dissolve
    kana "Eh? Aku pikir..."
    hide kana_home_side_confused_blush with dissolve
    "Kana berusaha melanjutkan kalimatnya, namun sepertinya tertahan di ujung lidah."
    "Melihat hal tersebut, akhinya [mcname!c] mencoba memulai percakapan lagi."
    "[mcname!c]" "Kana, akhir-akhir ini aku ngerasa kamu menutup diri."
    hide kana_home_confused_blush
    show kana_home_shy at char_center
    with dissolve
    "[mcname!c]" "Aku ga tau kalo aku ada salah apa atau gimana, tapi..."
    "[mcname!c]" "Maaf, ya Kana. Apa pun itu, aku gak bermaksud."
    hide kana_home_shy
    show kana_home_cry at char_center
    show kana_home_side_cry at left
    with dissolve
    kana "Eh nggak kok. B-bukan salahmu."
    kana ".........."
    kana "J-jangan benci aku ya."
    kana "T-tapi…"
    kana "S-sebenarnya aku takut..."
    kana "Aku takut kalau kamu bakal ngejauhin aku, gara-gara aku wibu."
    kana "Pasti kamu ngerasa aneh kan, dengan sifat ku ini?"
    hide kana_home_side_cry with dissolve
    "Kana mengatakan hal tersebut sambil gemetar, matanya terlihat berkaca-kaca menahan air mata."
    "[mcname!c] yang melihat hal tersebut hanya bisa terdiam."
    "[mcname!c]" "Aku tidak merasa seperti itu kok, Kana."
    hide kana_home_cry
    show kana_home_shy_smile at char_center
    show kana_home_side_drylaugh at left
    with dissolve
    kana "Eh??"
    hide kana_home_side_drylaugh
    hide kana_home_shy_smile
    show kana_home_shy at char_center
    with dissolve
    "[mcname!c]" "Aku ga tahu kenapa kamu bilang gitu."
    "[mcname!c]" "Tapi aku ga berpikiran begitu kok."
    hide kana_home_shy
    show kana_home_confused_blush at char_center
    show kana_home_side_confused_blush at left
    with dissolve
    kana "T-Tapi kan, waktu itu kamu bilang kamu ngerasa aneh sama orang yang suka jejepangan."
    hide kana_home_side_confused_blush
    hide kana_home_confused_blush
    show kana_home_shy at char_center
    with dissolve
    "[mcname!c]" "Ahhh, masalah ganci kemaren? Waktu itu keinget papahku."
    hide kana_home_shy
    show kana_home_shy_smile at char_center
    show kana_home_side_shy_eh at left
    with dissolve
    kana "Eh?"
    hide kana_home_side_shy_eh
    hide kana_home_shy_smile
    show kana_home_shy at char_center
    with dissolve
    "[mcname!c]" "Iyaa. Papahku juga wibu, bahkan bisa dibilang garis keras."
    "[mcname!c]" "Jadinya, aku sering teringat papahku kalo lagi ngomongin wibu. Padahal aku gak berpikir seperti itu kok."
    hide kana_home_shy
    show kana_home_confused at char_center
    show kana_home_side_confused at left
    with dissolve
    kana "J- Jadi kamu ga benci sama aku?"
    hide kana_home_side_confused with dissolve
    "[mcname!c]" "Seperti yang kubilang, nggak kok."
    hide kana_home_confused
    show kana_home_shy at char_center
    with dissolve
    "[mcname!c] menatap Kana sambil tersenyum dengan tatapan hangat."
    "[mcname!c]" "Aku khawatir sama kamu, Kana."
    "[mcname!c]" "Kamu udah gak masuk kuliah berhari-hari."
    hide kana_home_shy
    show kana_home_shy_closeeye_talk at char_center
    show kana_home_side_shy_ahn at left with dissolve
    kana "Maaf ya, [mcname!c]..."
    hide kana_home_side_shy_ahn
    hide kana_home_shy_closeeye_talk
    show kana_home_shy_closeeye at char_center
    with dissolve
    "[mcname!c]" "Yang penting kamu baik-baik aja."
    "[mcname!c]" "Aku ga mau kehilangan kamu."
    hide kana_home_shy_closeeye
    show kana_home_shy_smile at char_center
    show kana_home_side_talk at left with dissolve
    kana "[mcname!c]..."
    hide kana_home_side_talk
    hide kana_home_shy_smile
    show kana_home_shy at char_center
    with dissolve
    "[mcname!c]" "Pokoknya kalau ada apa-apa, tolong ingat bahwa aku akan selalu ada. Jangan pendam semuanya sendiri, aku pasti siap mendengarkan."
    hide kana_home_shy
    show kana_home_smile at char_center
    show kana_home_side_smile_cry at left
    with dissolve
    kana "......."
    hide kana_home_side_smile_cry with dissolve
    "[mcname!c]" "........."
    "[mcname!c] kemudian mengambil gelas yang ada di meja sebelah kasur lalu memberikannya ke Kana."
    hide kana_home_smile
    show kana_home_shy_smile at char_center
    show kana_home_side_drylaugh at left
    with dissolve
    kana "Makasih [mcname!c]..."
    hide kana_home_side_drylaugh
    hide kana_home_shy_smile
    show kana_home at char_center
    with dissolve
    "[mcname!c] menganggukkan kepalanya sambil tersenyum."
    hide kana_home
    show kana_home_shy_smile at char_center
    show kana_home_side_drylaugh at left
    with dissolve
    kana "*Glug glug*"
    kana "....."
    kana "*Sigh*"
    kana "[mcname!c]..."
    kana "Aku mau cerita."
    kana "Aku ga tau mau mulai dari mana..."
    hide kana_home_side_drylaugh with dissolve
    "[mcname!c] kemudian diam untuk memfokuskan diri ke cerita Kana."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene kamar kana sore with Dissolve(1.0)
    show kana_home at char_center with dissolve
    hide kana_home
    show kana_home_talk at char_center
    show kana_home_side_talk at left
    with dissolve
    $ quick_menu = True
    kana "Seperti yang kamu tau, pas kecil aku punya tubuh yang lemah."
    kana "Aku tidak bisa melakukan banyak hal yang sering dilakukan anak-anak pada umumnya, jadinya aku cuma bisa di rumah aja"
    kana "Walaupun begitu papah mamahku tetep sayang sama aku"
    kana "Tapi, mereka juga perlu ngurus pekerjaan mereka. Jadinya aku lebih banyak menghabiskan waktu sendirian di kamar."
    kana "Sesekali Freya datang untuk bermain denganku."
    kana "Waktu itu, aku seneeeeeng banget."
    kana "Tapi..."
    hide kana_home_side_talk
    hide kana_home_talk
    show kana_home_confused at char_center
    show kana_home_side_confused at left
    with dissolve
    kana "Suatu hari, Freya harus ikut orang tuanya yang tugas di luar kota."
    kana "................"
    kana "Akhirnya aku sendirian lagi."
    kana "Di tengah kesepian itu, aku menemukan yang namanya anime."
    hide kana_home_side_confused
    hide kana_home_confused
    show kana_home_talk at char_center
    show kana_home_side_talk at left
    with dissolve
    kana "Anime itu membuat aku melihat dunia dengan cara yang berbeda"
    kana "Mulai dari anime, aku pun mulai mencari-cari juga hal yang berbau jejepangan"
    kana "Hal-hal itulah yang menjadi pelarianku di kamar yang penuh kesendirian."
    kana "Tak terasa waktu berlalu, aku pun harus masuk yang namanya sekolah."
    kana "Setelah sekian lama, di sana lah aku mulai mencoba berinteraksi lagi dengan orang lain."
    hide kana_home_side_talk
    hide kana_home_talk
    show kana_home_confused at char_center
    show kana_home_side_confused at left
    with dissolve
    kana "Karena aku lama tidak berinteraksi dengan orang lain, aku tidak bisa berbicara dengan lancar."
    kana "Teman sekelasku bisa hidup dengan normal, dalam hati ku aku merasa iri dengan mereka."
    kana "Aku juga sering tidak masuk kelas karena sakit"
    kana "Aku tidak bisa belajar atau bahkan membuat teman."
    kana "Kalau terlalu banyak gerak, aku sakit lagi."
    kana "Pada awalnya, banyak teman sekelas yang berusaha mengajakku ngobrol."
    kana "Tapi aku tidak tahu apa yang harus ku katakan pada mereka."
    kana "Kebanyakan aku cuma bisa membalas \"iya\" dan \"emm\""
    kana "Lama kelamaan, orang yang mengajak ku berkurang, hingga akhirnya kelas berlangsung seperti aku tidak ada di ruangan."
    kana "Aku merasa seperti..."
    kana "Orang yang aneh."
    kana "Dan aku hanya bisa melihat teman sekelasku ngobrol dan bercanda dari jauh."
    kana "Kadang-kadang aku harus menahan rasa ingin menangis karena hal tersebut."
    kana "Mereka dekat, tapi aku merasa ada dinding yang memisahkan."
    kana "Aku merasa aku juga tidak ada gunanya di sekolah, jadi aku memutuskan untuk tidak masuk sekolah lagi, cuma menghabiskan waktu di kamar."
    hide kana_home_side_confused
    hide kana_home_confused
    show kana_home_talk at char_center
    show kana_home_side_talk at left
    with dissolve
    kana "Setahun pun berlalu, kemudian dua, tak terasa aku sudah di kelas 3."
    kana "Waktu itu, ternyata Freya kembali setelah mengikuti orang tuanya kerja di luar kota."
    kana "Tentu saja mendengar hal tersebut membuatku senang, namun karena bertahun tahun tidak berinteraksi dengan orang lain, aku tidak tahu harus gimana pas ketemu dia lagi."
    kana "Mungkin karena mendengar bagaimana keadaan ku, Freya kaget dan mencoba untuk mengajakku kembali masuk sekolah."
    kana "Awalnya aku enggan, namun karena desakan terus menerus dari Freya, akhirnya aku kembali mencoba untuk kembali bersekolah."
    kana "Pada saat kembali ke sekolah, entah kenapa tatapan orang-orang terasa berbeda dari biasanya, mungkin karena waktu itu aku bersama Freya."
    kana "Kali ini pun orang di kelas mulai mencoba mengajakku berbicara lagi. Aku gugup dan takut, tapi Freya membantuku menjawab mereka."
    hide kana_home_side_talk
    hide kana_home_talk
    show kana_home_confused at char_center
    show kana_home_side_confused at left
    with dissolve
    kana "Entah kenapa mereka mulai menganggapku seperti tuan putri yang lemah lembut dengan bodyguardnya."
    kana "Mungkin karena itu, akhirnya pandangan mereka kepadaku berbeda dari sebelumnya."
    kana "Takut menghancurkan pandangan mereka, mulai saat itu aku mencoba memerankan role tersebut."
    hide kana_home_side_confused
    hide kana_home_confused
    show kana_home_talk at char_center
    show kana_home_side_talk at left
    with dissolve
    kana "Berpura-pura seperti itu pun gapapa, setidaknya aku bisa berinteraksi dengan yang lain dan kembali mempunyai makna."
    kana "Tidak ada yang memuji ku sebelumnya karena mereka tidak menyukai diriku yang dulu."
    kana "Lagipula diriku yang wibu ini pun gak ada bagus-bagusnya, jadinya aku gapapa berpura-pura."
    kana "Yang kulakukan hanya mengikuti image mereka tentangku, dan menjadi orang yang membuat mereka senang"
    kana "Aku tetap menjalankan role ku tersebut, aku rasa itu sudah cukup dan ternyata memang benar."
    kana "Hari-hari pun berjalan dengan mulus..."
    kana "Setidaknya kebanyakan..."
    hide kana_home_side_talk
    hide kana_home_talk
    show kana_home_confused at char_center
    show kana_home_side_confused at left
    with dissolve
    kana "............."
    kana "Tapi..."
    kana "Terkadang aku merasa kalau ini semua hanyalah kebohongan."
    kana "Aku merasa bersalah karena membohongi banyak orang."
    kana "Saat yang lain merasa bahagia, aku tidak merasa begitu, hingga sampai di titik aku merasa tidak yakin dengan pilihanku."
    kana "............"
    kana "Aku tidak ingin kehilangan semua ini, tapi aku juga tidak ingin terlalu bergantung sama Freya."
    kana "Semakin sering aku berpura-pura, semakin aku merasa \"apakah pembohong seperti ku pantas untuk seperti ini.\""
    kana "Apakah aku layak menerima kebahagiaan ini?"
    kana "Apakah aku layak bersama kalian?"
    kana "........"
    hide kana_home_side_confused
    hide kana_home_confused
    show kana_home_shy_closeeye_talk at char_center
    with dissolve
    "[mcname!c]" "............."
    hide kana_home_shy_closeeye_talk
    show kana_home_shy_smile at char_center
    show kana_home_side_drylaugh at left
    with dissolve
    kana "Jadi, itu ceritaku..."
    hide kana_home_side_drylaugh
    hide kana_home_shy_smile
    show kana_home_smile at char_center
    with dissolve
    "Setelah menceritakan ceritanya yang panjang tanpa diganggu, akhirnya Kana berhenti. Badannya gemetar, wajahnya terlihat lelah."
    hide kana_home_smile
    show kana_home_shy_smile at char_center
    show kana_home_side_drylaugh at left
    with dissolve
    kana "Aku memang orang aneh yang brainrot dan suka jejepangan."
    kana "Aku juga berusaha menjadi orang yang berbeda, membohongi orang-orang, agar mereka menyukaiku."
    kana "Jadi makasih ya, udah mau berteman sama aku."
    kana "Walaupun mungkin kamu terpaksa, aku sangat bersyukur kamu mau jadi temanku."
    hide kana_home_side_drylaugh
    hide kana_home_shy_smile
    show kana_home_smile at char_center
    with dissolve
    "[mcname!c] menggaruk kepalanya, bingung dan khawatir kata-kata yang akan dikeluarkan olehnya malah akan membuat luka yang semakin dalam di hati Kana."
    hide kana_home_smile
    show kana_home_shy at char_center
    with dissolve
    "[mcname!c]" "Aku ga bohong. Serius, temenan sama kamu itu hal yang sangat menyenangkan."
    hide kana_home_shy
    show kana_home_shy_smile at char_center
    show kana_home_side_drylaugh at left
    with dissolve
    kana "Benarkah??"
    hide kana_home_side_drylaugh
    hide kana_home_shy_smile
    show kana_home_shy at char_center
    with dissolve
    "[mcname!c]" "Aku gak bohong. Pokoknya berapa kali pun kamu nanya, aku bakal tetap bilang kalo aku juga seneng banget bisa jadi temanmu."
    #Narrator
    hide kana_home_shy
    show kana_home_shy_closeeye at char_center
    show kana_home_side_shy_hmph at left
    with dissolve
    kana "*Blush*"
    hide kana_home_side_shy_hmph at left with dissolve
    "[mcname!c]" "...."
    hide kana_home_shy_closeeye
    show kana_home_shy_smile at char_center
    show kana_home_side_drylaugh at left
    with dissolve
    kana "Ini mimpi kah?"
    kana "Aku seneng banget denger kamu suka temenan sama aku."
    hide kana_home_side_drylaugh
    hide kana_home_shy_smile
    show kana_home_shy at char_center
    with dissolve
    "[mcname!c] menatap mata Kana sambil tersenyum."
    "[mcname!c]" "Kana, aku ga mau kamu merasa sendirian lagi. Aku gak nyaman kalo kamu jadi hikikomori."
    hide kana_home_shy
    show kana_home_confused_blush at char_center
    show kana_home_side_confused_blush at left
    with dissolve
    kana "Ga nyaman?? Kenapa?"
    hide kana_home_side_confused_blush with dissolve
    "[mcname!c]" "Karena aku juga menikmati waktu yang kita habiskan bersama."
    hide kana_home_confused_blush
    show kana_home_smile at char_center
    show kana_home_side_smile_cry at left
    with dissolve
    kana "Ummmm.."
    hide kana_home_side_smile_cry at left with dissolve
    "[mcname!c] kemudian memegang pundak Kana dan menatap langsung ke matanya."
    #SPRITE KANA HARUSNYA LEBIH DEKET LAGI
    hide kana_home_smile
    show kana_home_shy at char_center
    with dissolve
    "[mcname!c]" "Kamu itu dirimu yang sekarang Kana, jangan biarkan masa lalu menahanmu."
    "[mcname!c]" "Apa yang sudah terjadi tidak bisa diubah."
    "[mcname!c]" "Saat ini kamu adalah kamu."
    hide kana_home_shy
    show kana_home_shy_closeeye_talk at char_center
    with dissolve
    "Setelah itu [mcname!c] melepaskan tangannya, Kana terlihat malu dan memalingkan kepala."
    hide kana_home_shy_closeeye_talk
    show kana_home at char_center
    with dissolve
    "Setelah mencari kalimat yang pas, Kana kemudian menatap [mcname!c] sambil tersenyum."
    hide kana_home
    show kana_home_talk at char_center
    show kana_home_side_talk at left
    with dissolve
    kana "Uhmmm terima kasih, aku senang kamu sudah mau menemaniku."
    kana "Dan [mcname!c], aku..."
    hide kana_home_side_talk
    hide kana_home_talk
    show kana_home_shy_closeeye at char_center
    with dissolve
    "Kana mencoba mengatakan sesuatu, tapi akhirnya tidak jadi."
    hide kana_home_shy_closeeye
    show kana_home_shy_closeeye_talk at char_center
    show kana_home_side_shy_ahn at left
    with dissolve
    kana "Mungkin ini agak memalukan, tapi besok aku bakal kembali lagi seperti biasanya."
    hide kana_home_side_shy_ahn
    hide kana_home_shy_closeeye_talk
    show kana_home_smile at char_center
    with dissolve
    "Kana tersenyum."
    "[mcname!c]" "Iyah, yang penting sekarang kamu istirahat dulu aja."
    "Karena merasa tugasnya sudah selesai, akhirnya [mcname!c] pun beranjak untuk keluar kamar."
    hide kana_home_smile
    show kana_home_shy_smile at char_center
    show kana_side_drylaugh at left
    with dissolve
    kana "Ah... oke."
    kana "Sampai jumpa besok, [mcname!c]."
    hide kana_side_drylaugh
    hide kana_home_shy_smile
    show kana_home_smile at char_center
    with dissolve
    "Entah kenapa senyumannya terasa sedikit sedih."
    "[mcname!c]" "Oke, sampai jumpa besok."
    "[mcname!c] kemudian keluar dari kamar Kana."
    stop music fadeout 1.0
    $ quick_menu = False
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" fadein 1.0
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Tak terasa langit telah menjadi malam..."
    $ quick_menu = False
    scene ruang tamu malam with Dissolve(2.0)
    $ quick_menu = True
    "Melihat kejadian ini, [mcname!c] menjadi lebih mengenal Kanaia Asa dengan lebih dalam."
    "[mcname!c]" "Ya... ku rasa aku juga harus pulang."
    "Setelah mengucapkan terima kasih ke Mamahnya Kana, akhirnya [mcname!c] pulang ke kostnya."

    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Lorong.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True  
    "Keesokan harinya..."
    $ quick_menu = False
    scene depan kampus with Dissolve(2.0)
    $ quick_menu = True
    "Pagi ini [mcname!c] merasa lebih ringan dari biasanya, mungkin karena hari ini seseorang yang dia tunggu akhirnya kembali berkuliah lagi."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_lorong.ogg" fadein 1.0
    scene lorong with Dissolve(1.0)
    #$ renpy.block_rollback()
    show freya_talk at char_center
    show freya_side_talk at left
    with dissolve
    $ quick_menu = True
    freya "Jadi [mcname!c], gimana keadaan kana?"
    hide freya_side_talk
    hide freya_talk
    show freya at char_center
    with dissolve
    "[mcname!c]" "Dia udah mendingan dan juga katanya bakal masuk hari ini."
    hide freya
    show freya_talk at char_center
    show freya_side_talk at left
    with dissolve
    freya "Syukurlah."
    hide freya_side_talk
    hide freya_talk
    show freya_smile at char_center
    with dissolve
    hide freya_smile
    show freya_shock at char_center
    show freya_side_shock at left
    with dissolve
    freya "Eh btw [mcname!c], kamu ngapain jadi Kana mau balik lagi? Hehe."
    hide freya_side_shock
    hide freya_shock
    show freya_smug at char_center
    with dissolve
    "Freya menanyakan hal tersebut sambil nyengir."
    "[mcname!c]" "Eh?? Gak ngapa ngapain kok."
    "[mcname!c]" "Aku gak tau kamu berharap apa, tapi aku hanya ngelakuin apa yang ku bisa."
    hide freya_smug
    show freya_awe at char_center
    show freya_side_awe at left
    with dissolve
    freya "Hoooooo......"
    hide freya_side_awe with dissolve
    hide freya_awe
    show freya_awe at char_right
    show kana_smile at char_left
    with dissolve
    "Kana terlihat berjalan menuju kelas saat Freya dan [mcname!c] sedang berbincang."
    "Dia tampak bersinar sama seperti biasanya."
    hide kana_smile
    show kana_talk at char_left
    show kana_side_talk at left
    with dissolve
    kana "Pagi [mcname!c]... Pagi juga Frey..."
    hide kana_side_talk
    hide kana_talk
    show kana_smile at char_left
    with dissolve
    "[mcname!c]" "Ah, pagi Kana."
    hide freya_awe
    show freya_talk at char_right
    show freya_side_talk at left
    with dissolve
    freya "Pagi juga Nay"
    freya "Gimana keadaanmu Nay? Udah mendingan?"
    hide freya_side_talk with dissolve
    hide kana_smile
    hide freya_talk
    show freya at char_right
    show kana_talk at char_left
    show kana_side_talk at left
    with dissolve
    kana "Mhm... Udah mendingan kok Frey."
    hide kana_side_talk
    hide kana_talk
    show kana at char_left
    with dissolve
    "[mcname!c]" "Ngomong-ngomong katanya UTS bentar lagi ya?"
    hide kana_talk
    hide freya_talk
    show kana at char_left
    show freya at char_right
    with dissolve
    "[mcname!c] mencoba mencari topik pembicaraan lain, sepertinya untuk mencegah membahas hal yang kemarin."
    hide freya
    show freya_talk at char_right
    show freya_side_talk at left
    with dissolve
    freya "Iya yah."
    hide freya_side_talk
    hide freya_talk
    show freya at char_right
    with dissolve
    "[mcname!c]" "Kalo kamu UTS gimana Kana?"
    hide kana
    show kana_talk at char_left
    show kana_side_talk at left
    with dissolve
    kana "Kalo aku bisa aja kok, kayaknya..."
    hide kana_side_talk
    hide kana_talk
    show kana at char_left
    with dissolve
    hide kana
    show kana_confused at char_left
    hide freya
    show freya_smile at char_right
    with dissolve
    "Kana mengambil beberapa detik untuk melanjutkan kalimatnya."
    show kana_side_confused at left with dissolve
    kana "Agak takut soalnya aku sempat beberapa kali gak masuk."
    hide kana_side_confused with dissolve
    "[mcname!c]" "Heee... Kalo ada yang bisa ku bantu bilang aja ya."
    hide kana_confused
    show kana_drylaugh at char_left
    show kana_side_drylaugh at left
    with dissolve
    kana "Iya, mohon bantuannya ya..."
    hide kana_side_drylaugh
    hide kana_drylaugh
    hide freya_smile
    with dissolve
    #ARC 2
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kelas.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Beberapa hari kemudian..."
    $ quick_menu = False
    scene kelas with Dissolve(2.0)
    #$ renpy.block_rollback()
    play sound "audio/crowd_noise.mp3" loop fadein 1.0 volume (4.0)
    $ quick_menu = True
    "Sudah seminggu sejak kejadian itu, semuanya kembali menjadi normal."
    "Suasana kelas ricuh seperti biasa karena dosen belum datang."
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    "Tanpa sadar waktu pelajaran pun tiba, lalu terdengar suara pintu terbuka."
    stop sound fadeout 1.0
    stop music fadeout 1.0
    play music "audio/BGM_Dosen.ogg" fadein 1.0
    show dosen at dosen_center with dissolve
    hide dosen
    show dosen_talk at dosen_center
    show dosen_side_talk at left
    with dissolve
    $ quick_menu=True
    dosen "Selamat pagi anak-anak, mata kuliah hari ini akan dimulai dengan--"
    hide dosen_side_talk
    hide dosen_talk at dosen_center
    with dissolve
    stop music fadeout 1.0
    $ quick_menu=False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kelas.ogg" fadein 1.0
    scene kelas with Dissolve(1.0)
    $ quick_menu=True
    "Mata kuliah telah dimulai dan kondisi kelas pun tiba-tiba menjadi hening. Di dalam keheningan tersebut ada yang tertidur pulas, ada yang bermain HP, dan ada yang mencatat."
    "[mcname!c] pun dengan serius mengikuti apa yang disampaikan oleh Dosen."
    show kana_shy at kana_near with dissolve
    "Saat [mcname!c] memperhatikan pelajaran, di ujung matanya terlihat Kana yang berkali-kali menatapnya, seperti ingin mengatakan sesuatu."
    "Penasaran akan apa yang dilakukan gadis tersebut, akhirnya [mcname!c] menanyakannya secara langsung."
    "[mcname!c]" "Ada apa, Kana?"
    show kana_shy_talk at kana_near
    show kana_side_cry at left
    with dissolve
    kana "G-gapapa kok."
    hide kana_shy_talk
    hide kana_side_cry
    with dissolve
    "[mcname!c]" "......."
    hide kana_shy
    show kana_confused_blush_sideeye at kana_near
    with dissolve
    "Wajah Kana sedikit memerah sambil mengalihkan pandangan ke Dosen. [mcname!c] bingung melihat kelakuan Kana, namun akhirnya kembali fokus ke pelajaran."
    hide kana_confused_blush_sideeye with dissolve
    stop music fadeout 1.0
    $ quick_menu=False
    scene black with Dissolve(1.0)
    play music "BGM_Sore.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu=True
    "Langit telah menjadi sore..."
    $ quick_menu=False
    scene kelas sore with Dissolve(2.0)
    $ quick_menu=True
    "Tak terasa waktu telah berlalu dan dosen pun mengumumkan sesuatu yang terkait dengan UTS." 
    show dosen_talk at dosen_center
    show dosen_side_talk at left
    with dissolve
    dosen "Baiklah Mahasiswa/i, jangan lupa minggu depan ada UTS dan ini adalah UTS pertama kalian. Saya harap kalian menjunjung tinggi kejujuran dan jangan lupa untuk belajar, sekian terima kasih."
    hide dosen_side_talk
    hide dosen_talk
    show dosen at dosen_center
    with dissolve
    "Mahasiswa/i" "Terima kasih banyak Bu."
    hide dosen with dissolve
    $ quick_menu=False
    scene black with Dissolve(1.0)
    scene kelas sore with Dissolve(1.0)
    $ quick_menu=True
    "Setelah dosen meninggalkan ruangan, Kana memulai pembicaraan."
    show kana_confused at char_center
    show kana_side_confused at left
    with dissolve
    kana "Aduh gimana nih."
    kana "Aku gak terlalu ngedengerin dosen tadi, tau-tau udah bilang mau UTS."
    kana "Tapi harusnya bisa sih kalo belajar sambil review textbook, kayaknya??"
    hide kana_side_confused at left with dissolve
    "[mcname!c]" "Hahaha sama."
    "[mcname!c] memberikan persetujuan."
    show kana_side_confused at left with dissolve
    kana "Duh tolongin dong, [mcname!c]."
    kana "Bantuin aku belajar, soalnya kalo aku belajar sendiri bisa-bisa gak fokus."
    hide kana_side_confused
    hide kana_confused
    show kana at char_center
    with dissolve
    "[mcname!c]" "Bisa sih, lagi pula kalo barengan bisa lebih mudah belajarnya."
    show kana_side_confused at left
    show kana_confused at char_center
    with dissolve
    kana "Kalo kamu gimana Frey? Mau ikut belajar bareng juga kan nanti?"
    hide kana_confused
    hide kana_side_confused
    hide kana
    show kana at char_left
    show freya at char_right
    with dissolve
    "Kana mencoba mengajak Freya untuk belajar bersama."
    hide freya
    show freya_talk at char_right
    show freya_side_talk at left
    with dissolve
    freya "Kalo aku kayaknya skip nih, soalnya aku kalo rame malah gak bisa fokus."
    freya "Lagian biar kalian bisa barengan, hehe."
    hide freya_side_talk
    hide freya_talk
    show freya_smug at char_right
    with dissolve
    hide kana
    show kana_shy_talk at char_left
    show kana_side_cry at left
    with dissolve
    kana "Ih apaan sih Freya."
    hide kana_side_cry with dissolve
    hide freya_smug
    show freya_talk at char_right
    show freya_side_talk at left
    with dissolve
    freya "Hehe oke, aku duluan ya. Soalnya aku lagi ada yang dikerjain."
    hide freya_side_talk
    hide freya_talk
    show kana_confused_blush at char_left
    hide kana_shy_talk
    hide freya at char_right
    with dissolve
    "Setelah menggoda Kana, Freya berlari meninggalkan Kana dan [mcname!c]."
    "Setelah Freya pergi, Kana terlihat bingung bagaimana memulai pembicaraan."
    "Melihat hal tersebut, akhirnya [mcname!c] berinisiatif melanjutkan topik yang ada."
    "[mcname!c]" "Gimana jadinya? Kita jadi kan buat belajar barengnya?"
    hide kana_confused_blush
    show kana_shy_smile at char_left
    show kana_side_shy_smile at left
    with dissolve
    kana "JADI!"
    hide kana_side_shy_smile
    hide kana_shy_smile
    show kana_confused_blush_sideeye at char_left
    with dissolve
    "Menyadari akan suaranya yang bersemangat Kana pun sedikit malu."
    hide kana_confused_blush_sideeye
    show kana_shy_smile at char_left
    show kana_side_shy_smile at left
    with dissolve
    kana "Ah."
    hide kana_shy_smile
    show kana_shy_talk at char_left
    show kana_side_cry at left
    with dissolve
    kana "T-tapi… gak ada ide juga sih mau di mana..."
    hide kana_side_cry
    show kana_shy at char_left
    hide kana_shy_talk
    hide kana_side_shy_smile
    with dissolve
    "[mcname!c]" "Hmmmm..."
    "[mcname!c] kemudian berpikir untuk menentukan tempat untuk belajar bersama."
    "[mcname!c]" "Gimana kalau kita ke cafe?"
    hide kana
    show kana_talk at char_left
    show kana_side_talk at left
    with dissolve
    kana "Ehhhh boleh tuh!!!"
    hide kana_side_talk
    hide kana_talk
    show kana_smile at char_left
    with dissolve
    "Kana menjawab dengan begitu semangat. Keadaaan canggung sebelumnya menghilang, sehingga Kana dan [mcname!c] kembali mengobrol bersama seperti biasanya."
    "[mcname!c]" "Oke, berarti nanti kita ketemuan di sana ya."
    "[mcname!c]" "Nanti aku kabarin lagi kapannya."
    show kana_talk at char_left
    show kana_side_talk at left
    with dissolve
    kana "Okeee~"
    hide kana_smile
    hide kana_talk
    hide kana_side_talk
    with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Cafe Cerah.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya..."
    $ quick_menu = False
    scene cafe with Dissolve(2.0)
    $ quick_menu = True
    "Besoknya Kana dan [mcname!c] janjian untuk belajar bersama di cafe."
    "[mcname!c] datang 5 menit lebih awal agar mengamankan posisi duduk untuk Kana."
    "Tidak lama, Kana pun datang melalui pintu."
    play sound "audio/cafe-entrance.mp3" fadein 1.0
    show kana_date at small_center with dissolve
    "Kana mendatangi [mcname!c], dia terlihat berbeda dari biasanya."
    hide kana_date
    show kana_date_talk at char_center
    show kana_date_side_talk at left
    with dissolve
    kana "Eh maaf ya, nunggu lama."
    hide kana_date_side_talk
    hide kana_date_talk
    show kana_date_smile at char_center
    with dissolve
    "[mcname!c]" "......."
    hide kana_date_smile
    show kana_date_shy_smile at char_center
    show kana_date_side_shy at left
    with dissolve
    kana "K-kenapa? Ada yang aneh ya sama aku."
    hide kana_date_side_shy
    hide kana_date_shy_smile
    show kana_date_shy at char_center
    with dissolve
    "[mcname!c]" "Ah aku kaget aja ngeliat kamu make baju itu, kerasa beda dari biasanya."
    hide kana_date_shy
    show kana_date_shy_smile at char_center
    show kana_date_side_shy at left
    with dissolve
    kana "E-eh, Beneran keliatan ya? Ahahah."
    hide kana_date_side_shy
    hide kana_date_shy_smile
    show kana_date_shy_closeeye at char_center
    with dissolve
    "[mcname!c]" "Iya, kamu keliatan effort banget."
    hide kana_date_shy_closeeye
    show kana_date_shy_smile at char_center
    show kana_date_side_shy at left
    with dissolve
    kana "Ummm... Kok kamu kepikir begitu?"
    hide kana_date_side_shy
    show kana_date_shy at char_center
    hide kana_date_shy_smile
    with dissolve
    "[mcname!c]" "Soalnya kamu pake baju yang berbeda dari yang sering kamu pake di kampus, apalagi rambut kamu keliatan lebih rapih, mungkin abis dari salon?"
    show kana_date_shy_closeeye at char_center
    with dissolve
    "Mungkin rambutnya terlihat sama seperti biasanya, namun entah kenapa [mcname!c] merasa kalau ada yang berbeda, mungkin itu hanya insting nya saja."
    hide kana_date_shy_closeeye
    show kana_date_confused_blush at char_center
    show kana_date_side_shy_confused at left
    with dissolve
    kana "I-iya deh, yuk sekarang kita fokus belajar bareng aja."
    hide kana_date_shy
    hide kana_date_confused_blush
    hide kana_date_side_shy_confused at left
    show kana_date_shy at kana_near
    with dissolve
    "Dengan wajah yang sedikit memerah Kana pun langsung duduk di dekat [mcname!c]."
    "Mereka berdua pun memulai untuk belajar."
    hide kana_date_shy with dissolve
    stop music fadeout 1.0
    $ quick_menu=False
    scene black with Dissolve(1.0)
    play music "BGM_Cafe Sore.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu=True
    "Tak terasa 4 jam berlalu..."
    $ quick_menu=False
    scene cafe sore with Dissolve(2.0)
    show kana_date_confused at kana_near with dissolve
    $ quick_menu=True
    "[mcname!c] dan Kana mulai merasa bosan dan kurang fokus dengan materi yang ada." 
    menu:
        "Ingin mengganti suasana, yang dilakukan [mcname!c]..."
        "Main Game HP Sendiri.":
            stop music fadeout 1.0
            $ quick_menu = False
            play music "BGM_Bad End.ogg" fadein 1.0
            "[mcname!c] memilih untuk main game sendiri dan mengabaikan Kana seakan dia tidak ada. Dunia milik berdua antara [mcname!c] dan HP, hal ini membuat Kana ngambek dan meninggalkan [mcname!c] yang sedang asik bermain HP."
            scene black with dissolve
            show text "{color=#FFF}*BROOO KALAU LAGI MAIN SAMA TEMEN, JANGAN KESERINGAN MAIN HP NAPA?! KAN JADINYA GINI, YA ELAH YANG BENER AJA.*{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FF0000}BAD END{/color}" with Pause(2.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits
        "Ajak Kana main game.":
            jump AjakKanaMainGame
        "Tidur.":
            stop music fadeout 1.0
            $ quick_menu = False
            play music "BGM_Bad End.ogg" fadein 1.0
            "[mcname!c] memilih untuk rebahan dan tiduran untuk sejenak di pangkuan Kana dan minta tolong ke Kana buat bangunin dia. Tapi ternyata saat Kana mencoba membangunkan kamu, kamu malah keenakan tidur di pangkuan Kana. Karena kamu merasa nyaman, akhirnya kamu tidak pernah bangun lagi."
            scene black with dissolve
            show text "{color=#FFF}*EH CUY LO INI LAGI DI CAFE BUKAN DI KOST. LAGIAN KAN INI LAGI KERJA KELOMPOK DAH, KENAPA MALAH TIDUR? MIKIR BRO MIKIR!*{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FF0000}BAD END{/color}" with Pause(2.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits
label AjakKanaMainGame:
    "Untuk refreshing, kamu milih main game yang ada di dalam cafe dan mengajak Kana untuk memainkan game tersebut."
    hide kana_date_confused
    show kana_date at kana_near
    with dissolve
    "Kana yang awalnya ragu pun mulai tertarik saat kamu mulai menjelaskan tentang game yang akan dimainkan tersebut."
    hide kana_date
    show kana_date_smile at kana_near
    with dissolve
    "Mungkin terbawa suasana dan karena mumet saat belajar tadi, Kana dan [mcname!c] enjoy memainkan game yang ada lebih dari yang mereka duga."
    "Kana pun terlihat menjadi sedikit lebih terbuka kepada [mcname!c]."
    $ quick_menu=False
    scene black with Dissolve(1.0)
    scene cafe sore with Dissolve(1.0)
    show kana_date_angry at kana_near
    show kana_date_side_confused at left
    with dissolve
    $ quick_menu=True
    kana "Aaaaa, iii kok kalah mulu sihhh... [mcname!c] ngalah napa..."
    hide kana_date_side_confused with dissolve
    "[mcname!c]" "Hehehehe, you need 1000 years to defeat me."
    $ quick_menu=False
    scene black with Dissolve(1.0)
    scene cafe sore with Dissolve(1.0)
    $ quick_menu=True
    "Setelah puas bermain game, akhirnya [mcname!c] dan Kana kembali duduk ke tempat mereka sebelumnya."
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "Game yang tadi seru banget ya."
    hide kana_date_side_talk
    hide kana_date_talk
    show kana_date at kana_near
    with dissolve
    "[mcname!c]" "Hahaha iya, apalagi moment pas kamu akhirnya bisa ngalahin aku."
    hide kana_date
    show kana_date_confused at kana_near
    show kana_date_side_confused at left
    with dissolve
    kana "Next game pasti aku menang lagi kok!"
    hide kana_date_side_confused
    show kana_date_smile at kana_near
    with dissolve
    "Selama mereka duduk, Kana dan [mcname!c] membicarakan game yang mereka mainkan tadi."
    "[mcname!c]" "Tapi emang sih, cuma beberapa kali main aja kamu sudah jago gitu mainnya."
    hide kana_date_confused
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "Hehehe iya kan."
    hide kana_date_side_talk
    hide kana_date_talk
    show kana_date_smile at kana_near
    with dissolve
    "Karena merasa suasananya sedang baik, [mcname!c] mencoba untuk membahas hal-hal yang berbau jejepangan."
    "Kana pernah bilang kalau dia menyukai hal-hal tersebut dan [mcname!c] ingin mengenal Kana lebih dalam lagi. Tapi [mcname!c] teringat, hal-hal itulah yang membuat Kana merasa berbeda dari yang lain."
    "[mcname!c]" "Btw Kana, kamu kan tau banyak tentang jejepangan. Kebetulan Papahku wibu, dia suka ngidol dan jejepangan gitu. Tapi aku pengen tau lebih banyak lagi, jadi kalo boleh sih aku mau tanya-tanya tentang hobi kamu."
    hide kana_date_smile
    show kana_date_shy_smile at kana_near
    show kana_date_side_shy at left
    with dissolve
    kana "E-Eh,, b-boleh kok."
    hide kana_date_side_shy
    hide kana_date_shy_smile
    show kana_date_shy at kana_near
    with dissolve
    "[mcname!c]" "Tenang aja kok. Aku ga bakalan anggep kamu aneh atau apalah, jadi santai aja. Aku bener-bener pengen tau lebih banyak sih tentang ini dari kamu."
    hide kana_date_shy
    show kana_date_confused_blush at kana_near
    show kana_date_side_shy_confused at left
    with dissolve
    kana "EEEEEEEH???"
    kana "SERIUS!!???"
    hide kana_date_side_shy_confused with dissolve
    "Nada kana yang begitu bersemangat membuat hampir seluruh orang di cafe tersebut melihat ke arah Kana, sadar akan hal itu Kana pun segera duduk dan memelankan suaranya lagi."
    hide kana_date_confused_blush
    show kana_date_shy_smile at kana_near
    show kana_date_side_shy at left
    with dissolve
    kana "E-Eh maaf ya, terlalu semangat hehe, tapi janji ya jangan sampe takut sama aku."
    hide kana_date_side_shy
    hide kana_date_shy_smile
    show kana_date_shy at kana_near
    with dissolve
    "[mcname!c]" "Iya aku JANJI kok, SUMPAH. Kan aku juga yang nanya duluan."
    hide kana_date_shy
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "Janji kelingking?"
    hide kana_date_talk
    show kana_date at kana_near
    hide kana_date_side_talk
    with dissolve
    "[mcname!c]" "Iya. Kelingking kita berjanji, jari manis jadi saksi?"
    hide kana_date_talk
    show kana_date_angry at kana_near
    show kana_date_side_confused at left
    with dissolve
    kana "Ih apaan sih."
    hide kana_date_side_confused
    hide kana_date_angry
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "Yauda deh kalau gitu, jadi kita harus mulai dari yang mana nih? Kamu mau tau soal apa deh?"
    hide kana_date_side_talk
    hide kana_date_talk
    show kana_date at kana_near
    with dissolve
    "[mcname!c]" "Hmmm, bingung juga sebenernya... Hmmm, dari apa yang kamu lagi suka sekarang deh."
    hide kana_date
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "Kalo aku sekarang lagi suka dengerin lagu-lagu idol, jujur aku suka dengan dance sama lagunya."
    hide kana_date_side_talk
    hide kana_date_talk
    show kana_date at kana_near
    with dissolve
    "[mcname!c]" "Heeee..."
    show kana_date_shy_smile at kana_near
    hide kana_date
    with dissolve
    "Kana menjelaskan hal-hal yang dia suka dengan penuh semangat."
    hide kana_date_shy_smile with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" fadein 1.0
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Tidak terasa langit menjadi gelap..."
    $ quick_menu = False
    scene cafe malam with Dissolve(2.0)
    show kana_date_confused at kana_near
    show kana_date_side_confused at left
    with dissolve
    $ quick_menu = True
    kana "E-ehhh, udah gelaap!?? Maaf ya kayaknya aku kebablasan deh."
    hide kana_date_side_confused at left with dissolve
    "Kana melihat ke arah [mcname!c] dengan panik, takut [mcname!c] merasa aneh atau pun gelisah karena semua hal wibu yang telah diceritakan olehnya."
    "[mcname!c]" "Ga perlu mikir yang aneh-aneh deh Kana. Santai aja, aku kan udah janji."
    "[mcname!c]" "Lagian dengerin kamu cerita kaya gitu seru kok, ternyata banyak ya yang masih belum aku tau dari kamu."
    hide kana_date_confused
    show kana_date at kana_near
    with dissolve
    "[mcname!c]" "Seneng aja bisa tau sisi kamu yang seperti ini."
    hide kana_date
    show kana_date_shy at kana_near
    with dissolve
    "Mendengar hal tersebut wajah Kana memerah."
    hide kana_date_shy
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "Eh... ya udah nanti ku kasih playlist yang sering kudengar ke kamu deh."
    hide kana_date_side_talk
    hide kana_date_talk
    show kana_date at kana_near
    with dissolve
    "Kana melihat sekeliling, terlihat suasana cafe berbeda dari saat mereka datang."
    hide kana_date
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "Ah, gak kerasa sudah jam segini ya."
    hide kana_date_side_talk
    hide kana_date_talk
    show kana_date at kana_near
    with dissolve
    "[mcname!c]" "Kayaknya kita malah kebanyakan main daripada belajarnya ya, haha."
    "[mcname!c]" "Tapi gak apa-apa, setidaknya kita sudah nyicil sedikit-sedikit lah ya."
    hide kana_date
    show kana_date_drylaugh at kana_near
    show kana_date_side_drylaugh at left
    with dissolve
    kana "Iya, hehe."
    show kana_date_smile at kana_near
    hide kana_date_side_drylaugh
    with dissolve
    "[mcname!c]" "Gimana kalo kita balik dulu, soalnya takut kemaleman."
    hide kkana_date_smile
    show kana_date_shy at kana_near
    show kana_date_side_shy_smile at left
    with dissolve
    kana "Ummmnn…"
    hide kana_date_side_shy_smile at left with dissolve
    "Kana terlihat ingin mengatakan suatu hal."
    hide kana_date_shy
    show kana_date_shy_smile at kana_near
    show kana_date_side_shy at left
    with dissolve
    kana "[mcname!c]..."
    kana "Aku rasa kita masih belum cukup belajarnya"
    kana "Jadi... nanti mau belajar bareng lagi?"
    hide kana_date_side_shy
    hide kana_date_shy_smile
    show kana_date_shy_closeeye at kana_near
    with dissolve
    "Kana mengatakan tersebut dengan sedikit gugup, mungkin takut jika [mcname!c] akan menolaknya."
    "[mcname!c]" "Boleh kok. Lagipula aku juga free nanti."
    hide kana_date_shy_closeeye
    show kana_date_shy_smile at kana_near
    show kana_date_side_shy at left
    with dissolve
    kana "O-oke janji ya."
    kana "Nanti aku kabarin."
    hide kana_date_side_shy
    hide kana_date_shy_smile
    with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Cafe Cerah.mp3" fadein 1.0 volume (2.0)
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Berhari-hari kemudian, [mcname!c] dan Kana selalu belajar bersama di cafe."
    $ quick_menu = False
    scene cafe with Dissolve(2.0)
    #$ renpy.block_rollback()
    $ quick_menu = True
    "Bahkan pelayan di sana pun terasa seperti teman karena saking seringnya bertemu."
    show kana_date_confused at kana_near
    show kana_date_side_confused at left
    with dissolve
    kana "Haaaaahhh..."
    kana "Kayaknya aku mulai bosen deh belajar di sini terus."
    kana "Pengennya mungkin ganti suasana lain."
    hide kana_date_side_confused with dissolve
    "[mcname!c]" "Hmmmm... bisa sih."
    "[mcname!c]" "Tapi mau di mana kira-kira?"
    hide kana_date_confused
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "Gimana kalo kita ke Jepang, sekalian nonton konser si M*ku?"
    show kana_date_shy_closeeye at kana_near
    hide kana_date_side_talk at left
    with dissolve
    "Karena sudah mumet dengan pelajaran kuliah, Kana mengatakan hal-hal yang tidak masuk akal."
    "[mcname!c]" "Kayaknya agak mustahil kalo sekarang."
    "[mcname!c]" "Bahkan kalau pun bisa, sulit buat dapetin tiket konsernya."
    hide kana_date_shy_closeeye
    show kana_date_drylaugh at kana_near
    show kana_date_side_drylaugh at left
    with dissolve
    kana "Hahaha iya juga sih..."
    kana "Ke pantai deh."
    hide kana_date_side_drylaugh
    hide kana_date_drylaugh
    show kana_date at kana_near
    with dissolve
    "Mendengar kata pantai membuat [mcname!c] membayangkan Kana menggunakan swimsuit."
    "Sadar akan apa yang dibayangkan, [mcname!c] langsung \nmenggeleng-gelengkan kepalanya."
    "[mcname!c]" "Pantai pun sekarang lagi rame banget."
    "[mcname!c]" "Jadi walaupun kita ke sana, yang kita liat cuma gerombolan manusia."
    hide kana_date
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "Hmmmmmm jadi di mana ya."
    hide kana_date_side_talk
    hide kana_date_talk
    show kana_date at kana_near
    with dissolve
    "[mcname!c] dan Kana merenung untuk memikirkan tempat yang lain."
    play sound "ReceiveText.ogg" loop volume (2.0)
    show kana_date_side at left with dissolve
    kana "Hmmmm?"
    hide kana_date_side at left with dissolve
    stop sound
    "Kana membuka HPnya."
    "Saat membaca pesan yang masuk Kana kemudian tersenyum."
    hide kana_date
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "[mcname!c], kata mamah dia pengen ketemu sama kamu."
    hide kana_date_side_talk
    hide kana_date_talk
    show kana_date at kana_near
    with dissolve
    "[mcname!c]" "EH?? Kenapa?"
    "[mcname!c] bingung kenapa mamahnya Kana ingin bertemu dengannya."
    hide kana_date
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "Hmmm gak tau juga sih."
    kana "Tapi gimana kalau kita belajarnya di rumahku aja?"
    kana "Sekalian ketemu sama Mamahku, kan. Hehe."
    hide kana_date_side_talk
    hide kana_date_talk
    show kana_date at kana_near
    with dissolve
    "[mcname!c]" "Hmmm, kalo gitu boleh deh..."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Sore.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Sore itu [mcname!c] dan Kana langsung menuju ke rumah Kana setelah pulang dari cafe."
    "[mcname!c]" "{i}Gak nyangka aku bakal ke rumah Kana dan ketemu mamahnya lagi.{/i}"
    show pintu_rumah_kana at pintu_rumah_kana with dissolve
    "Kana kemudian membunyikan bel yang ada di dekat pintu rumahnya."
    show kana_date_side_talk at left 
    with dissolve
    play sound "audio/ding.mp3"
    kana "Mamaahh, aku pulaaang~"
    kana "Ada [mcname!c] juga nih."
    hide kana_date_side_talk 
    hide pintu_rumah_kana at pintu_rumah_kana
    with dissolve
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    "Terdengar suara pintu terbuka, di sana terlihat Mamahnya Kana."
    "Mamah Kana" "Selamat datang Kana. Terima kasih udah mau datang, [mcname!c]."
    "Mamah Kana" "Ayo masuk."
    "Setelah diperbolehkan Mamahnya Kana, akhirnya [mcname!c] masuk ke rumahnya Kana, mengikuti di belakang Kana."
    stop music fadeout 1.0
    $ quick_menu=False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Ruang Tamu.ogg" fadein 1.0
    scene ruang tamu sore with Dissolve(1.0)
    $ quick_menu=True
    "Mamah Kana" "Anggap rumah sendiri ya."
    "[mcname!c]" "Ah, makasih tante."
    "Mamahnya Kana kemudian pergi ke dapur."
    show kana_date at kana_near with dissolve
    "Kana dan [mcname!c] duduk di sofa bersama-sama."
    hide kana_date
    show kana_date_talk at kana_near
    with dissolve
    "Mereka berbincang-bincang sambil mulai belajar kembali tentang kuliah mereka."
    hide kana_date_talk
    show kana_date at kana_near
    with dissolve
    "Mamah Kana" "Ini ya minum buat kalian, sekalian nanti makan siang di sini ya biar bisa fokus belajarnya."
    "[mcname!c]" "Waah, gak perlu repot-repot tante."
    "Mamah Kana" "Duh gapapa santai aja."
    "Mamahnya Kana pun kembali ke dapur."
    hide kana_date
    show kana_date_talk at char_center
    show kana_date_side_talk at left
    with dissolve
    kana "Eh kalo gitu aku ikut bantu Mah."
    hide kana_date_side_talk
    hide kana_date_talk
    with dissolve
    "Kana pun kemudian pergi ke dapur, meninggalkan [mcname!c] sendirian di ruang tamu."
    "Sambil menunggu Kana, [mcname!c] pun melihat-lihat ruang tamunya Kana."
    "[mcname!c]" "Heeeee..."
    $ quick_menu=False
    scene black with Dissolve(1.0)
    scene ruang tamu sore with Dissolve(1.0)
    $ quick_menu=True
    "Tidak lama setelah itu, Mamahnya Kana masuk ke ruang tamu."
    "Tapi Kana tidak terlihat mengikutinya."
    "Mamah Kana" "Ini ya [mcname!c], dimakan."
    "Mamahnya Kana membawakan kue kering."
    "[mcname!c]" "Waduh makasih lagi tante, jadi gak enak."
    "Mamah Kana" "Udah gak usah dipikirin."
    "Mamah Kana" "Lagian ini juga sebagai ucapan terima kasih tante buat kamu."
    "Mamah Kana" "Soalnya udah banyak membantu Kana."
    "[mcname!c]" "Engga kok tante, itu semua berkat usaha dari diri Kana sendiri juga."
    "[mcname!c]" "Saya gak ngelakuin hal yang spesial."
    "Mamah Kana" "Tetap saja karena kamu, jadinya Kana beberapa hari ini perasaaannya keliatan lebih baik."
    "Mamah Kana" "Oleh karena itu, makasih ya."
    "Mamah Kana" "Sebagai imbalannya, tante bakal ngabulin satu permintaan apa aja deh buat kamu."
    "[mcname!c]" "E-Eh."
    "[mcname!c] bingung dengan perkataan Mamahnya Kana."
    show kana_home_side_talk at left
    with dissolve
    kana "MAAHHH!!! Bisa bantu sebentar di sini gak??"
    hide kana_home_side_talk
    with dissolve
    "Di dapur terdengar suara Kana memanggil."
    "Mamah Kana" "Iyaaa bentarrr."
    "Mamah Kana" "Duh kayaknya Kana manggil nih, maklum Kana jarang ke dapur."
    "Mamah Kana" "Tapi katanya karena [mcname!c] dateng, dia jadi pengen nyoba masak untuk makan siang, fufufu."
    "Mamahnya Kana kemudian kembali ke dapur."
    "[mcname!c] kembali sendirian lagi di ruang tamu, namun kali ini bingung dengan perkataan yang dikatakan oleh Mamahnya Kana."
    stop music fadeout 1.0
    $ quick_menu=False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" fadein 1.0
    scene awan malam with Dissolve(1.0)
    $ quick_menu=True
    "Tak terasa waktu telah menjadi malam."
    $ quick_menu=False
    scene ruang tamu malam with Dissolve(2.0)
    show kana_home_shy_closeeye_talk at kana_near with dissolve
    $ quick_menu=True
    "[mcname!c] melihat Kana sepertinya sudah mulai tidak fokus. Nafasnya mulai tidak beraturan, mukanya memerah."
    hide kana_home_shy_closeeye_talk
    show kana_home_shy_closeeye_talk at kana_near
    with dissolve
    "[mcname!c]" "Kamu gapapa Kana?"
    hide kana_home_shy_closeeye_talk
    show kana_home_shy_smile at kana_near
    show kana_home_side_shy_eh at left
    with dissolve
    kana "Gapapa kok. Aku masih kuat."
    hide kana_home_side_shy_eh
    hide kana_home_shy_smile
    show kana_home_shy at kana_near
    with dissolve
    "[mcname!c]" "Kalo sampe di sini aja gimana? Kamu kayaknya butuh istirahat."
    hide kana_home_shy
    show kana_home_shy_smile at kana_near
    show kana_home_side_shy_eh at left
    with dissolve
    kana "B-baiklah…"
    hide kana_home_side_shy_eh
    hide kana_home_shy_smile
    show kana_home_shy at kana_near
    with dissolve
    "[mcname!c]" "Kalo gitu aku pamit dulu ya... Jangan lupa besok UTS."
    hide kana_home_shy
    show kana_home_talk at kana_near
    show kana_home_side_talk at left
    with dissolve
#"BARU DIREVIEW SAMPE SINI SAMA KOKO JON"
    "BARU DIREVIEW SAMPE SINI SAMA KOKO JON"
    kana "Kalo gitu aku antar ke depan pintu, deh."
    hide kana_home_side_talk with dissolve
    "Sudah lumayan lama [mcname!c] dan Kana belajar bareng, sehingga sudah waktunya [mcname!c] untuk pulang. [mcname!c] membereskan barang-barangnya lalu beranjak pergi ke depan pintu sambil diantar oleh Kana."
    "[mcname!c]" "Makasih ya, makanannya."
    hide kana_home_talk
    show kana_home_smile at char_center
    show kana_home_side_talk at left with dissolve
    kana "Makasih juga ya [mcname!c], sudah mau mampir."
    hide kana_home_side_talk with dissolve
    hide kana_home_smile
    show kana_home_shy_closeeye_talk at char_center
    show kana_home_side_shy_ahn at left
    kana "Achoo!!"
    hide kana_home_side_shy_ahn
    hide kana_home_shy_closeeye_talk
    show kana_home_shy_closeeye at char_center
    with dissolve
    hide kana_home_shy_closeeye with dissolve
#ASSET PINTU RUMAH KANA
    show pintu_rumah_kana at pintu_rumah_kana
    show kana_home_shy_smile at char_center 
    with dissolve
    "Kana memberikan ucapan selamat tinggal kepada [mcname!c] di depan pintu."
    "Mamahnya Kana ada urusan pekerjaan jadi tidak ikut mengantar [mcname!c]."
    "[mcname!c]" "Iya Kana, makasih juga udah menjamu."
    "[mcname!c]" "Salam juga untuk mama."
    hide kana_home_shy_smile
    show kana_home_shy_closeeye_talk at char_center
    show kana_home_side_shy_ahn at left
    kana "Achoo!!"
    hide kana_home_side_shy_ahn
    hide kana_home_shy_closeeye_talk
    show kana_home_shy_closeeye at char_center
    with dissolve
    "[mcname!c]" "Nah, kan. Jaga kesehatan ya."
    hide kana_home_shy_closeeye
    show kana_home_shy_closeeye_talk at char_center
    show kana_home_side_shy_ahn at left
    kana "Achoo!!"
    hide kana_home_side_shy_ahn
    hide kana_home_shy_closeeye_talk
    show kana_home_shy_smile at char_center
    show kana_home_side_drylaugh at left
    with dissolve
    kana "A-aman kok, aku kuat."
    hide kana_home_side_drylaugh with dissolve
    "[mcname!c]" ".........."
    stop music fadeout 1.0
    $ quick_menu=False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" fadein 1.0
    scene awan malam with Dissolve(1.0)
    $ quick_menu=True
    "Di kost..."
    $ quick_menu=False
    scene kamar mc kota with Dissolve(2.0)
    $ quick_menu=True
    "[mcname!c]" "kira -kira apa yang dimaksud sama Mamahnya Kana tadi ya…"
    "[mcname!c] mengingat kejadian yang telah terjadi saat [mcname!c] berkunjung ke tempat Kana."
    "[mcname!c]" "Dan juga Kana tadi terlihat sakit."
    "[mcname!c]" "Moga saja dia gak kenapa-napa."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kelas.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = False   
    "Tak terasa UTS pun tiba."
    $ quick_menu = False
    scene kelas with Dissolve(2.0)
    #$ renpy.block_rollback()
    $ quick_menu = True
    "Hari UTS telah tiba, [mcname!c] merasa yakin akan dirinya karena sudah belajar bersama Kana cukup lama dan merasa cukup memahami mata kuliah yang telah diberikan."
    "[mcname!c] melihat ke arah Kana dan menyapa, akan tetapi perhatiannya teralihkan saat melihat muka Kana."
    #*Sprite KANA MUKA MERAH PUCAT*
    #show kana_sick at char_center with dissolve
    "[mcname!c]" "Pagi Kana"
    #show kana_side_sick at left with dissolve
    show kana_shy_talk at char_center
    show kana_side_cry at left
    with dissolve
    kana "Ah, P- Pagi, [mcname!c]."
    hide kana_side_cry with dissolve
    #hide kana_side_sick at left with dissolve
    hide kana_shy_talk
    show kana_shy_talk at kana_near
    with dissolve
    "Muka kana terlihat lebih pucat daripada kemarin saat [mcname!c] berkunjung ke rumahnya."
    hide kana_shy_talk
    show kana_shy_talk at char_center
    with dissolve
    "[mcname!c]" "Kamu gapapa?"
    #show kana_side_sick at left with dissolve
    show kana_side_cry at left with dissolve
    kana "Ga-gapapa kok. Aku masih kuat."
    hide kana_side_cry with dissolve
    #hide kana_side_sick at left with dissolve
    "[mcname!c]" "Kamu yakin???"
    "[mcname!c]" "Soalnya mukamu kayaknya..."
    stop music fadeout 1.0
    #hide kana_sick at char_center with dissolve
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    play music "BGM_Dosen.ogg" fadein 1.0
    "Pengawas ujian datang dan UTS pun akan dimulai, membuat [mcname!c] tidak dapat beranjak dari kursinya."
    hide kana_shy_talk with dissolve
    "Pengawas" "Baiklah semuanya, UTS akan dimulai jadi saya harap semuanya menonaktifkan gadgetnya serta mengerjakannya secara mandiri. Waktu kalian selama 45 menit, dimulai dari sekarang."
    $ quick_menu = False
    jump kanaafterquiz
#UTS
label kanaafterquiz:
    $ quick_menu = True
    "[mcname!c]" "Ahhh akhirnya beres."
    "[mcname!c] mengangkat tangannya."
    "[mcname!c]" "Maaf, Pak. Kalau sudah selesai apakah boleh dikumpulkan sekarang?"
    "Pengawas" "Wah, cepat juga. Sepertinya kamu yang pertama selesai."
    "Pengawas" "Hmmm... Baiklah, boleh dikumpulkan kalau sudah yakin."
    "[mcname!c] beranjak dari tempat duduk."
    stop music fadeout 1.0
    play sound "SFX - Fall.WAV" fadein 1.0 volume(15.0)
    "Pada saat akan mengumpulkan lembar jawaban, tiba-tiba [mcname!c] mendengar suara."
    play music "BGM_Bad End.ogg" fadein 1.0
    "Pandangan semua orang pun teralihkan dan saat itu juga, [mcname!c] melihat Kana yang tergeletak di lantai. Tanpa ragu-ragu, [mcname!c] berlari menghampiri Kana yang tergeletak lemas dan tidak sadarkan diri."
    #show kana_sick at char_center with dissolve
    show kana_shy_closeeye at char_center with dissolve
    "[mcname!c]" "Nay!! Kamu kenapa Nay?! Nayyy!"
    #hide kana_sick at char_center with dissolve
    "Penjaga ujian dan staff pun memberitahukan murid untuk menghubungi pihak kesehatan kampus akan tetapi [mcname!c] memberitahukan tentang riwayat kesehatan Kana."
    "Para staf pun panik dan segera menghubungi rumah sakit terdekat."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play sound "SFX - Ambulance.wav" loop fadein 1.0
    scene kelas with Dissolve(1.0)
#HARUSNYA STOCK IMAGE AMBULANCE
    $ quick_menu = True
    "Tak lama kemudian, Kana dibawa dengan ambulans sambil ditemani [mcname!c]."
    show kana_shy_closeeye at kana_near with dissolve
    "Saat di ambulans, Kana sempat sadar."
    #show kana_sick at char_center
    #show kana_side_sick at left
    #with dissolve
    show kana_side_cry at left with dissolve
    kana "[mcname!c]..."
    hide kana_side_cry with dissolve
    #hide kana_side_sick at left with dissolve
    "[mcname!c]" "Kana! Kana!"
    #show kana_side_sick at left with dissolve
    hide kana_shy_closeeye
    show kana_shy_talk at kana_near
    show kana_side_cry at left
    with dissolve
    kana "Aku takut..."
    hide kana_side_cry with dissolve
    #hide kana_side_sick at left with dissolve
    "[mcname!c]" "Aku ada di sini. Kamu ga perlu khawatir! Istirahatlah."
    #show kana_side_sick at left with dissolve
    show kana_side_cry at left
    with dissolve
    kana "[mcname!c]..."
    hide kana_side_cry with dissolve
    #hide kana_side_sick at left with dissolve
    hide kana_shy_talk
    show kana_closeeye_talk at kana_near
    with dissolve
    "Kana pun kembali memejamkan matanya."
    stop sound fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    #HARUSNYA BGM SEDIH RUMAH SAKIT
    scene rumah sakit with Dissolve(1.0)
    #HARUSNYA STOCK IMAGE RUMAH SAKIT
    $ quick_menu = True
    "Setelah sesampainya di rumah sakit, Kana pun diperiksa oleh dokter dan perawat."
    "Di situ [mcname!c] hanya bisa menunggu jawaban dari pihak dokter, setelah beberapa saat pihak dokter pun keluar dari ruangan."
    "[mcname!c]" " DOK!! GIMANA KANA, DOK!??"
    "Dokter" "Maaf anak muda, tapi kami sudah berusaha semaksimal mungkin. Jadi mohon terima kabar ini dengan berlapang dada, tapi Kana…"
    "[mcname!c]" "HA!? MAKSUDNYA APAAN DOK!? KANA KENAPA DOK!!?"
    "Dokter" "Kana... dia... "
    stop music
    play music "audio/BGM_Lawak Tana.mp3"
    #HARUSNYA LAWAK YANG SATUNYA
    "Dokter" "DIA GAPAPA KOKK~ Cuma demam kecapekan doang, ga usah khawatir."
    "Dokter" "Soal riwayat kesehatannya, buat sekarang Kana udah diinfus jadinya aman. Harusnya sekarang kamu udah bisa jenguk dia."
    "[mcname!c]" "AH ELAH DOK, GA LUCU TAUUUU."
    "Marah akan candaan dokter, [mcname!c] segera pergi ke dalam ruangan perawatan tempat Kana berada."
    stop sound fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    #HARUSNYA BGM SEDIH RUMAH SAKIT
    scene lorong with dissolve
    #HARUSNYA STOCK IMAGE RUMAH SAKIT
    #show kana_sick at char_center with dissolve
    show kana_shy_closeeye at char_center with dissolve
    $ quick_menu = True
    "[mcname!c]" "Kana! Kamu gapapa kan!?"
    #show kana_side_sick at left with dissolve
    hide kana_shy_closeeye
    show kana_shy_smile at char_center
    show kana_side_shy_smile at left
    with dissolve
    kana "Kamu kok kaya kecapean gitu sih [mcname!c]? Kamu kenapa?"
    hide kana_side_shy_smile
    hide kana_shy_smile
    show kana_shy at char_center
    with dissolve
    #hide kana_side_sick at left with dissolve
    "[mcname!c]" "AHHH ini gara-gara si dokter bercandain kondisi kamu tadi. Btw kok bisa demam tinggi? Kemarin bukannya istirahat tapi lanjut maksain begadang ya?"
    #show kana_side_sick at left with dissolve
    hide kana_shy
    show kana_shy_smile at char_center
    show kana_side_shy_smile at left
    with dissolve
    kana "Eh... i-iya, soalnya aku ngerasa masih kurang belajarnya. Jadi aku maksain buat belajar lebih sampai subuh. Eh ternyata waktu paginya udah agak pusing."
    hide kana_side_shy_smile
    hide kana_shy_smile
    show kana_shy at char_center
    with dissolve
    #hide kana_side_sick at left with dissolve
    "[mcname!c]" "Kana, jujur aku pengen marahin kamu tapi aku ga bisa soalnya kamu lagi sakit."
    #show kana_side_sick at left with dissolve
    hide kana_shy
    show kana_shy_closeeye_talk at char_center
    show kana_side_cry at left
    with dissolve
    kana "Huhu maaf... Eh bentar ujian kamu gimana?"
    hide kana_side_cry
    hide kana_shy_closeeye_talk
    show kana_shy at char_center
    with dissolve
    #hide kana_side_sick at left with dissolve
    "[mcname!c]" "Kamu ga usah khawatir kok, ujianku dah selesai. Kalo ujianmu, kata pengawas nanti bakal diadain susulan setelah UTS selesai. Sekarang kamu harus fokus sama kesehatanmu dulu aja."
    #show kana_side_sick at left with dissolve
    hide kana_shy
    show kana_shy_smile at char_center
    show kana_side_shy_smile at left
    with dissolve
    kana "[mcname!c].."
    kana "Makasih banyak ya udah mau bantuin aku, maaf ngerepotin yaa."
    hide kana_side_shy_smile
    hide kana_shy_smile
    show kana_shy at char_center
    with dissolve
    #hide kana_side_sick at left with dissolve
    #hide kana_sick at char_center with dissolve
    #show kana_scared at char_center with dissolve
    "[mcname!c]" "Kana... Kamu ga ngerepotin kok, santai aja. Sekarang kamu gimana rasanya? Udah mendingan?"
    #show kana_side_scared at left with dissolve
    hide kana_shy
    show kana_shy_talk at char_center
    show kana_side_cry at left
    with dissolve
    kana "Jujur aku juga ga tau, mungkin terasa lebih baik karena kamu ada yang nemenin."
    kana "Tapi... aku takut."
    kana "Aku takut sendirian lagi..."
    kana "Takut kejadian waktuku kecil terulang kembali dan dirawat sendirian di rumah dengan waktu yang lama."
    hide kana_side_cry
    hide kana_shy_talk
    show kana_shy_closeeye at char_center
    with dissolve
    #hide kana_side_scared at left with dissolve
    "Wajah Kana telihat lemas, melihat ke arah [mcname!c] seakan ingin menangis. Akan tetapi ia tetap berusaha tersenyum."
    "[mcname!c]" "Kana... jangan mikir kaya gitu. Aku bakalan selalu temenin kamu apapun yang terjadi oke? Yang penting kamu sehat dulu aja deh, ga usah mikirin yang lain dulu."
    #hide kana_scared at char_center with dissolve
    hide kana_shy_closeeye
    show kana_shy_smile at char_center
    show kana_side_shy_smile at left
    kana "Iya..."
    kana "Ini udah mendingan kok."
    hide kana_side_shy_smile
    hide kana_shy_smile
    show kana_shy at char_center
    with dissolve
    "Kana menatap [mcname!c] sambil tersenyum."
    "[mcname!c] juga tersenyum kepada Kana."
    hide kana_shy
    show kana_shy_smile at char_center
    show kana_side_shy_smile at left
    kana "Umm... aku udah boleh pulang gak ya? Soalnya ini lumayan gak enak keringetan, aku pengen ganti baju."
    hide kana_side_shy_smile
    hide kana_shy_smile
    show kana_shy at char_center
    with dissolve
    "[mcname!c]" "Eh bentar aku coba tanyakan dulu ke perawatnya."
    stop sound fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    scene lorong with dissolve
    #HARUSNYA STOCK IMAGE RUMAH SAKIT
    show kana_shy at char_center with dissolve
    $ quick_menu = True
    "[mcname!c]" "Ehh ini bisa katanya, tapi harus ada yang anterin kamu pulang. Mamahmu ke mana?"
    hide kana_shy
    show kana_shy_talk at char_center
    show kana_side_cry at left
    with dissolve
    kana "Ummm... Kalo kamu bisa ga [mcname!c]? Nganterin aku pulang…"
    kana "Soalnya Mamahku lagi sibuk jam-jam segini."
    hide kana_side_cry
    hide kana_shy_talk
    show kana_shy_closeeye_talk at char_center
    with dissolve
    "[mcname!c]" "Eh aku ??!!"
    "[mcname!c]" "{i}Waduh gapapa nih? Tapi ga ada siapa-siapa lagi sih di sini. Harus gimana nih gue?{/i}"
    hide kana_shy_closeeye_talk with dissolve
    menu:
        "Yang kamu lakukan..."
        "Terima tawaran Kana":
            jump TerimaTawaranKana
        "Nolak tawaran Kana":
            "[mcname!c] menolak tawaran Kana. [mcname!c] terlalu malu untuk menerima ajakan itu, dan akhirnya Kana disuruh pulang sendiri."
            $ quick_menu = False
            stop music fadeout 1.0
            scene black with dissolve
            show text "{color=#FFF}*BROOO ANAK ORANG LAGI SAKIT MALAH LO SURUH BALIK SENDIRI GA TAKUT DIA KENAPA KENAPA KAH?.*{/color}" with Pause(2.0)
            show text "{color=#FF0000}BAD END{/color}" with Pause(2.0)
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits
        "Kabur dari tempat":
            "[mcname!c] memilih kabur dari tempat itu saking malunya karena membayangkan berduaan dengan Kana. Setelah itu pun kamu tidak tau Kana pulang atau tidak, tetapi kamu hanya mendapatkan kabar dari Kana melalui HP dengan kata-kata \"kamu jahat\"."
            $ quick_menu = False
            stop music fadeout 1.0
            scene black with dissolve
            show text "{color=#FFF}*BROOO KO KABUR SIH? APA SIH YANG BIKIN LU MALU TUH, GA JELAS BANGET DAH!*{/color}" with Pause(2.0)
            show text "{color=#FF0000}BAD END{/color}" with Pause(2.0)
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits
label TerimaTawaranKana:
    show kana_shy_closeeye_talk at char_center with dissolve
    "[mcname!c] pun menerima tawaran Kana. Meskipun malu, tapi rasa ingin menjaga Kana lebih besar daripada rasa malunya."
    "[mcname!c]" "K-kalau kamu gak keberatan sih boleh, Kana. Nanti aku temenin, tapi aku minta ijin dulu ke perawat ya. Soalnya harus isi surat-surat keterangan dulu, haha."
    hide kana_shy
    show kana_shy_smile at char_center
    show kana_side_shy_smile at left
    kana "I-iya, makasih banyak ya sekali lagi.\n*Blush*"
    hide kana_side_shy_smile
    hide kana_shy_smile
    show kana_shy at char_center
    with dissolve
    #*SKIP TO SCENE*
    #*BG RUMAH KANA*
    stop sound fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    #HARUSNYA BGM RUANG TAMU KANA
    scene ruang tamu sore with dissolve
    #HARUSNYA BG RUANG TAMU KANA
    #$ renpy.block_rollback()
    $ quick_menu = True
    "Sesaat setelah datang ke rumah Kana, [mcname!c] membawa Kana ke kamarnya."
    stop sound fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Kosan 2.mp3" fadein 1.0
    #HARUSNYA BGM KAMAR KANA
    scene kamar kana with dissolve
    #HARUSNYA BG KAMAR KANA
    $ quick_menu = True
    show kana_shy_closeeye at char_center with dissolve
    "Kana pun istirahat di kasurnya ditemani oleh [mcname!c] yang duduk di kursi belajar Kana."
    "[mcname!c]" "Oke, Kana sekarang kamu tunggu dulu ya. Ini aku beliin makanan pesen online, semoga cocok yaa. Bentar aku siapin dulu."
    hide kana_shy_closeeye
    show kana_shy_closeeye_talk at char_center
    show kana_side_cry at left
    with dissolve
    kana "Makasih yaa, maaf ngerepotin."
    hide kana_side_cry
    hide kana_shy_closeeye_talk
    show kana_shy_closeeye at char_center
    with dissolve
    "[mcname!c]" "Udah lah ga usah kaya gitu, kan kita udah jadi temen. Santai aja Kana."
    hide kana_shy_closeeye
    show kana_shy_smile at char_center
    show kana_side_shy_smile at left
    with dissolve
    kana "Yeeeee makasih yaaa, akhirnya setelah sekian lama +1 teman."
    hide kana_side_shy_smile
    hide kana_shy_smile
    show kana_shy at char_center
    with dissolve
    "[mcname!c]" "LAH!? Kan dah temenan dari lama, gimana sih hahaha."
    hide kana_shy
    show kana_shy_smile at char_center
    show kana_side_shy_smile at left
    with dissolve
    kana "Gapapa yang penting +1 teman, hehe."
    hide kana_side_shy_smile
    hide kana_shy_smile
    show kana_shy at char_center
    with dissolve
    "[mcname!c]" "Hadeh yaudah. Aku siapin makanan dulu ya."
    hide kana_shy
    show kana_shy_closeeye at char_center
    with dissolve
    "Setelah [mcname!c] pergi, Kana pun memeluk bantalnya dengan wajah yang memerah."
    hide kana_shy_closeeye with dissolve
    "[mcname!c] pun pergi ke dapur untuk mengambilkan makanan dan obat yang telah disiapkan oleh dokter."
    $ quick_menu = False
    scene black with dissolve
    #play music
    #HARUSNYA BGM RUANG TAMU KANA
    scene ruang tamu sore with dissolve
    #HARUSNYA BG RUANG TAMU KANA
    show kana_shy_closeeye at char_center with dissolve
    $ quick_menu = True
    "[mcname!c]" "Kana. Ini makanannya kamu makan dulu ya, obatnya ada di sini. Btw kamu udah kabarin Mamah kamu?"
    hide kana_shy_closeeye
    show kana_shy_closeeye_talk at char_center
    show kana_side_shy_smile at left with dissolve
    kana "Udah kok. Mamah awalnya mau langsung pergi ke rumah sakit, tapi aku bilang ga usah soalnya udah ada kamu yang temenin aku. Aku juga ga mau ganggu waktu kerjanya Mamah."
    hide kana_side_shy_smile
    hide kana_shy_closeeye_talk
    show kana_shy_closeeye at char_center
    with dissolve
    "[mcname!c]" "Oke deh kalau begitu. Btw dipikir pikir dokter tadi udah ngeselin, tapi lucu juga ya."
    hide kana_shy_closeeye
    show kana_shy_smile at char_center
    show kana_side_shy_smile at left
    with dissolve
    kana "Kenapa tuh?"
    hide kana_side_shy_smile
    hide kana_shy_smile
    show kana_shy at char_center
    with dissolve
    "[mcname!c]" "Iya nih tadi udah bikin drama kaya di TV yang bilang \"Kami sudah berusaha semaksimal mungkin.\"" 
    "[mcname!c]" "Eh tapi sekarang obatnya {i}aergiamint-hachu{/i}, nama obatnya aneh banget ya."
    hide kana_shy
    show kana_shy_smile at char_center
    show kana_side_shy_smile at left
    with dissolve
    kana "Oooo, itu obat yang biasa aku minum kok. Namanya emang aneh kan, tapi itu manjur kok. Kayaknya..."
    hide kana_side_shy_smile
    hide kana_shy_smile
    show kana_shy at char_center
    with dissolve
    hide kana_shy
    show kana_shy_closeeye_talk at char_center
    with dissolve
    "Kana pun mencoba makan akan tetapi tangannya terkadang merasa lemas karena terdapat infus di lengan kanannya."
    #Sfx prang ( suara sendok jatuh ke piring )
    #play sound "audio/"
    "[mcname!c]" "Kana!!!?? Kamu gapapa?"
    hide kana_shy_closeeye_talk
    show kana_shy_smile at char_center
    show kana_side_shy_smile at left
    with dissolve
    kana "Ah.. iya."
    kana "Gapapa kok, cuma ini tangan kananku agak lemes aja soalnya ada infusan. Terus tadi aku coba makan pake tangan kiri, ternyata susah juga ya."
    hide kana_side_shy_smile
    hide kana_shy_smile
    show kana_shy at char_center
    with dissolve
    "[mcname!c]" "Eh... Bentar kalau gitu aku bantu suapin kamu aja."
    hide kana_shy
    show kana_confused_blush at char_center
    show kana_side_confused at left
    with dissolve
    kana "Eh?!!!"
    hide kana_side_confused with dissolve
    "[mcname!c]" "????"
    "[mcname!c]" "Kenapa?"
    hide kana_confused_blush
    show kana_shy_smile at char_center
    show kana_side_shy_smile at left
    with dissolve
    kana "E-enggak apa-apa kok. K-kalau kamu emang bersedia, boleh aja sih..\n*Blush*"
    hide kana_side_shy_smile
    hide kana_shy_smile
    show kana_shy at char_center
    with dissolve
    "[mcname!c]" "Oke dehh, sini aku bantu sua-"
    hide kana_shy
    show kana_shy_closeeye at char_center
    with dissolve
    "[mcname!c]" "*Blush*"
    "Tiba-tiba [mcname!c] terdiam, sadar akan perkataannya yang bisa dibilang cukup berani. Akan tetapi nasi sudah menjadi bubur, [mcname!c] tidak dapat lagi menarik kata-katanya tersebut."
    hide kana_shy_closeeye
    show kana_shy_smile at char_center
    show kana_side_shy_smile at left
    with dissolve
    kana "K-k-kenapa [mcname!c]?\n*Blush*"
    hide kana_side_shy_smile
    hide kana_shy_smile
    show kana_shy at char_center
    with dissolve
    "[mcname!c]" "Ehhhh enggaa ada apa-apa kok. Sini aku suapin.\n*Blush*"
    "[mcname!c]" "{i}Aduhhh nyuapin Kana? Kok bisa ya tiba-tiba tanpa sadar ngomong gitu? Tapi kalau nggak dibantu, nanti dia ga makan. Terus dia ga bisa minum obat, terus nanti dia ga sehat, AAAAA. Oke deh, aku harus bisa!{/i}"
    "[mcname!c] pun mengambil makanan dari piring Kana, mencoba mendekatkan sendoknya ke mulut Kana dengan perlahan."
    "[mcname!c]" "Aaaaaaa~"
    hide kana_shy
    show kana_shy_closeeye_talk at char_center
    show kana_side_cry at left
    with dissolve
    kana "Aaaaaaaa~"
    hide kana_side_cry
    hide kana_shy_closeeye_talk
    with dissolve
    stop music fadeout 1.0
    #*SFX PINTU TERBUKA KERAS(BRAK)*
    $ quick_menu = False
    window auto hide
    with Pause(2.0)
    play music "audio/BGM_Lawak Tana.mp3" fadein 1.0
    #HARUSNYA YANG NGAKAK SATUNYA
    window auto show
    $ quick_menu = True
    "Saat itu pun suara pintu terbuka keras membuat Kana dan [mcname!c] kaget terdiam."
    show freya_shock at char_center
    show freya_side_shock at left
    with dissolve
    freya "KANAAA!!! KAMU GAPAPA KA-"
    hide freya_side_shock
    hide freya_shock
    show freya_awe at char_center
    with dissolve
    "Saat itu juga Freya melihat [mcname!c] dan Kana yang sedang duduk dengan posisi tangan [mcname!c] yang membawa sendok makanan ke mulut Kana."
    show freya_side_awe at left with dissolve
    freya "............."
    hide freya_side_awe
    hide freya_awe
    show kana_confused at char_right
    with dissolve
    "[mcname!c]" "............."
    show kana_side_confused at left with dissolve
    kana "............."
    hide kana_side_confused with dissolve
    show freya_shock at char_left
    show freya_side_shock at left
    with dissolve
    freya "Eh sorry ganggu ya. Hehe, silahkan lanjutin."
    hide freya_side_shock
    hide freya_shock
    with dissolve
    "[mcname!c]" "Ehhhh Freeeya tungguu!! Aku bisa jelasin!!"
    show kana_side_confused at left with dissolve
    kana "Freeeyy!!! Tunggu dulu sini, cepat ke sini-"
    hide kana_side_confused at left with dissolve
    #(*SFX BATUK BATUK UHUK UHUK)"
    hide kana_confused
    show kana_shy_close_eye_talk at char_center
    show kana_side_cry at left
    with dissolve
    kana "UHUK! UHUK!!"
    hide kana_side_cry with dissolve
    "Dengan secepat kilat Freya pun langsung menghampiri Kana yang terbatuk batuk dan menanyakan kondisi Kana saat itu."
    stop sound fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Kosan 1.mp3" fadein 1.0
    #HARUSNYA BGM KAMAR KANA
    scene kamar kana with dissolve
    #HARUSNYA BG KAMAR KANA
    $ quick_menu = True
    "[mcname!c] pun menjelaskan situasi tersebut dan akhirnya Freya mengerti dengan apa yang terjadi. Freya memarahi Kana yang memaksakan dirinya untuk belajar hingga sakit dan Kana pun berjanji untuk beristirahat terlebih dahulu."
    show freya_talk at char_left
    show freya_side_talk at left
    with dissolve
    freya "Yaudah kamu habisin dulu makanannya, Nay."
    freya "Setelah itu, makan obatnya lalu istirahat."
    hide freya_side_talk
    hide freya_talk
    show freya at char_left
    with dissolve
    show kana_shy_closeeye at char_right with dissolve
    "[mcname!c]" "Iya, Kana. Pokoknya kesehatan kamu yang paling penting."
    hide kana_shy_closeeye
    show kana_shy_smile at char_center
    show kana_side_shy_smile at left
    with dissolve
    kana "I-iya. Maaf ya. Makasih udah mau nemenin aku kayak gini…"
    hide kana_side_shy_smile with dissolve
    #BG Langit Sore
    stop sound fadeout 1.0
    $ quick_menu = False
    scene awan sore with dissolve
    #HARUSNYA LANGIT SORE
    play music "audio/BGM_Kosan 1.mp3" fadein 1.0
    #HARUSNYA BGM KAMAR KANA
    scene kamar kana with dissolve
    #HARUSNYA BG KAMAR KANA
    $ quick_menu = True
    "Setelah Kana selesai makan dan meminum obat dari dokter, terdengar suara pintu terbuka dan terlihat Mamah Kana datang dari arah pintu."
    play sound "audio/open_door.mp3"
    show kana_shy_closeeye at char_center with dissolve
    "Mamah Kana" "Astaga, kamu gapapa Naya?"
    hide kana_shy_closeeye
    show kana_shy_smile at char_center
    show kana_side_shy_smile at left
    with dissolve
    kana "Iya aku udah baikan kok, Mah. Maaf ya kalau bikin mamah khawatir, ini juga udah makan dan minum obat kok. Jadi tinggal istirahat aja."
    hide kana_side_shy_smile
    hide kana_shy_smile
    show kana_shy at char_center
    with dissolve
    "Mamah Kana" "Eh ya udah kamu istirahat aja yaa. Freya sama [mcname!c], kita ngobrol di ruang depan aja ya. Biar Kana istirahat."
    "[mcname!c]" "Iya, Kana harus istirahat."
    hide kana at char_center with dissolve
    show freya_talk at char_center
    show freya_side_talk at left
    with dissolve
    freya "Get well soon, Nay."
    hide freya_side_talk
    hide freya_talk
    with dissolve
    "[mcname!c] dan Freya pun meninggalkan Kana untuk beristirahat, dan mengikuti Mamah Kana menuju ruang tengah."
    stop sound fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Kosan 1.mp3" fadein 1.0
    #HARUSNYA BGM RUANG TENGAH RUMAH KANA
    scene ruang tamu malam with dissolve
    #HARUSNYA BG RUANG TENGAH RUMAH KANA
    show freya at char_center with dissolve
    $ quick_menu = True
    "Mamah Kana" "Makasih banyak ya udah mau nemenin sama ngerawat Kana. Untung aja ada kalian, kalau engga... Aduhh ga kebayang deh."
    "Mamah Kana" "Sekali lagi makasih banyak ya."
    "[mcname!c]" "Eh iya tante sama-sama, kebetulan aku bisa bantu jadi aku bantuin, hehe."
    hide freya
    show freya_talk at char_center
    show freya_side_talk at left
    with dissolve
    freya "Iya aman aja kok kalau sama kita. Eh udah jam segini, maaf ya tante aku pulang dulu. Udah ditunggu sama orang tua, ada acara soalnya hehe."
    hide freya_side_talk at left with dissolve
    "[mcname!c]" "Iya tante, aku juga pulang dulu ya. Sekarang Kana udah ada yang jaga, jadi mau pulang ya. Udah jam segini juga."
    "Mamah Kana" "Eh iya, lupa kalau udah jam segini. Hati hati di jalan yaaa, sekali lagi makasih banyak."
    "[mcname!c]" "Sama-sama, tante."
    show freya_side_talk at left with dissolve
    freya "Sama-sama, tante."
    hide freya_side_talk at left with dissolve
    "[mcname!c] dan Freya pun berpisah menuju ke rumahnya masing-masing."
    stop sound fadeout 1.0
    $ quick_menu = False
    scene awan with dissolve
    play music "audio/BGM_Pagi Siang.ogg" fadein 1.0
    $ quick_menu = True
    "Selagi dalam masa pemulihan, [mcname!c] dan Freya saling bergantian untuk menjenguk Kana."
    "Setelah Kana benar-benar sehat, Kana pun melakukan ujian susulan untuk mengejar ketertinggalan UTS yang sebelumnya."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}HARI UTS SUSULAN{/color}" with Pause(2.0)
    play music "audio/BGM_Kampus.mp3" fadein 1.0
    scene depan kampus with dissolve
    #$ renpy.block_rollback()
    $ quick_menu = True
    show kana at char_right with dissolve
    show freya at char_left with dissolve
    "[mcname!c] dan Freya mengantar Kana yang akan melakukan UTS susulan."
    "[mcname!c]" "Good luck, Kana!"
    hide freya
    show freya_talk at char_left
    show freya_side_talk at left
    with dissolve
    freya "Kamu pasti bisa! Do it, Nay!"
    hide freya_side_talk with dissolve
    hide kana
    show kana_talk at char_right
    show kana_side_talk at left
    with dissolve
    kana "Makasih, teman-teman. Tunggu aku, ya!"
    hide kana_side_talk
    hide kana_talk
    show kana_smile at char_right
    with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Lorong.mp3" fadein 1.0
    scene lorong with dissolve
    $ quick_menu = True
    "Selagi Kana mengerjakan UTS susulan, [mcname!c] menyarankan untuk melakukan perayaan dalam rangka merayakan selesainya UTS dan kesembuhan Kana."
    show freya at char_center with dissolve
    hide freya
    show freya_talk at char_center
    show freya_side_talk at left
    with dissolve
    freya "Hmmm. Kalo nanti mau makan-makan, gak? Ngerayain kesehatan Kana sama selesainya UTS."
    hide freya_side_talk
    hide freya_talk
    show freya at char_center
    with dissolve
    "[mcname!c]" "Weh, boleh tuh! Hmmm kalau kita ngerayain di cafe gimana?"
    hide freya
    show freya_talk at char_center
    show freya_side_talk at left
    with dissolve
    freya "Eh seru juga tuh, cocok nih nanti kita mau rayain gmn?" 
    hide freya_side_talk
    hide freya_talk
    show freya at char_center
    with dissolve
    "[mcname!c]" "Eh gimana kalau beli cake gitu? Kana kan suka cake tuh."
    hide freya
    show freya_shock at char_center
    show freya_side_shock at left
    with dissolve
    freya "Ide bagus tuh! Cocok banget, Si Naya suka strawberry cake sih."
    hide freya_side at left with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Cafe Cerah.mp3" fadein 1.0
    scene cafe with dissolve
    #$ renpy.block_rollback()
    show kana at char_right with dissolve
    show freya at char_left with dissolve
    $ quick_menu = True
    "[mcname!c]" "Sekali lagi, SELAMAT KANAAAAA!!!! "
    hide freya
    show freya_talk at char_left
    show freya_side_talk at left
    with dissolve
    freya "Selamat yah, udah namatin UTS kali ini. Meski susulan, setidaknya kamu berhasil. Lain kali jangan sakit lagi ya."
    hide freya_side_talk
    hide freya_talk
    show freya at char_left
    with dissolve
    hide kana
    show kana_talk at char_right
    show kana_side_talk at left
    with dissolve
    kana "Eeeehh. Makasihh Freey, [mcname!c], hehehe. Maaf ya udah banyak repotin kalian semua dan maaf juga udah bikin kalian panik."
    hide kana_side_talk
    hide kana_talk
    show kana at char_right
    with dissolve
    hide freya
    show freya_shock at char_left
    show freya_side_shock at left
    with dissolve
    freya "Santai Nayyy. Lagian kan yang paling dibikin repot tuh..."
    hide freya_side_shock
    hide freya_shock
    show freya_smug at char_left
    with dissolve
    "Tanpa melanjutkan perkataannya, Freya melirik ke arah [mcname!c] seakan memberi kode."
    hide kana
    show kana_shy_smile at char_right
    show kana_side_shy_smile at left
    with dissolve
    kana "Eh... Ummm i-iya... Makasih banyak ya [mcname!c]."
    hide kana_side_shy_smile at left with dissolve
    "[mcname!c]" "E-eh...\n*Blush*"
    "[mcname!c]" "K-kalau buat Kana siiih..."
    hide kana_shy_smile
    show kana_shy_closeeye at char_right
    show kana_side_shy at left
    with dissolve
    kana "*Blush*"
    hide kana_side_shy at left with dissolve
    "[mcname!c]" "{i}Kalo buat kamu mah, aku mendaki gunung lewati lembah pun rela Kanaaa.{/i}" 
    "Suasana menjadi canggung, saking canggungnya suara jangkrik pun terdengar untuk beberapa saat hingga Freya membuka obrolan baru."
    hide freya_smug
    show freya_shock at char_left
    show freya_side_shock at left
    with dissolve
    freya "Ah elah kok pada baper gini sih. Kan ini lagi perayaan sembuh dan selesainya UTS KEMATIAN ITU AHAHAHAH!!!"
    hide freya_side_shock
    hide kana_shy_closeeye
    show kana at char_right
    with dissolve
    "[mcname!c]" "Seneng banget kamu."
    hide kana
    show kana_talk at char_right
    show kana_side_talk at left
    with dissolve
    kana "Iya nih, emang ada beberapa yang susah sih, tapi untungnya aku bisa lah."
    hide kana_side_talk
    hide kana_talk
    show kana at char_right
    with dissolve
    "[mcname!c]" "Yaudah, untuk kita semua yang udah lewatin UTS pertamaaaa. CHEERRSS!!!"
    hide kana
    hide freya_shock
    show kana_smile at char_right
    show freya_smile at char_left
    show kana_side_smile at left
    with dissolve
    kana "CHEERSS!!"
    hide kana_side_smile
    show freya_side_smile at left
    with dissolve
    freya "CHEERSS!!"
    hide freya_side_smile at left with dissolve
    "Obrolan mereka pun kembali berlanjut, perayaan Kana sembuh dan selesai UTS. Meski hanya dihadiri 3 orang akan tetapi suasana yang ada tetap terasa hidup, ramai, dan penuh keceriaan."
    
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene chapter 3 kana with Dissolve (1.0)
    pause(3.0)
    scene black with Dissolve (1.0)
    play music "audio/BGM_Lorong.mp3" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Berhari-hari telah berlalu"
    "Jarak antara Kana dan [mcname!c] semakin dekat, hampir setiap hari mereka menghabiskan waktu makan siang bersama sama dan terkadang ditemani oleh Freya juga."
    "Hari ini pun sama seperti biasanya, [mcname!c] dan Kana janjian untuk makan siang bersama di kantin."
    $ quick_menu = False
    scene lorong with dissolve(2.0)
    $ quick_menu = True
    "[mcname!c]" "{i}Aduhh, telat nihh, pake mules segala.{/i}"
    "Saat tergesa-gesa, pandangan [mcname!c] tiba-tiba teralihkan dengan sebuah flyer yang menempel di papan pengumuman."
#SHOW PAPAN PENGUMUMAN FLYER
    "[mcname!c]" "{i}Eh apa ini?{/i}"
    "[mcname!c]" "{i}Hmmm ternyata bentar lagi bakal ada acara jejepangan di kampus ini.{/i}"
    "[mcname!c]" "{i}Ehh ini kan flyer yang waktu itu pernah dikasih sama cewek rambut merah ya?{/i}"
    "[mcname!c]" "Hmmmmm... \"Dicari anggota untuk group idol cewek\"."
    "[mcname!c]" "{i}Kayaknya cocok deh buat Kana.{/i}"
    menu:
        "Yang [mcname!c] lakukan..."
        "Ambil flyer event jejepangan.":
            "[mcname!c]" "{i}Ehhh tapi udah kelamaan ini, ga enak sama Kana nunggu lama.{/i}"
            "[mcname!c] pun memilih untuk mengabaikan flyer tersebut, lalu lari agar bisa datang tepat waktu."
            jump truekana
        "Ambil flyer \"Dicari Anggota Klub Jepang\".":
            jump goodkana