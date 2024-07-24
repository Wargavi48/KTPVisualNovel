#---CHAPTER 2—---
#ARC 1
label chapter2kanastart:
    #*SCENE*
    #*BG LANGIT*
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}Chapter II{/color}" with Pause(2.0)
    play music "audio/BGM_MC Pertama Kali ke JKT + BG Pagi.mp3" fadein 1.0
    scene awan with dissolve
    #$ renpy.block_rollback()
    $ quick_menu = True
    "Karena hari ini hari libur, jadi [mcname] memutuskan untuk menghabiskan waktunya berkeliling di mall yang dekat dengan kostnya."
    stop music fadeout 1.0
    $ quick_menu = False
    #*BG MALL*
    #*SFX Kerumunan*
    scene black with dissolve
    play music "audio/BGM_Mall Slow.mp3" fadein 1.0
    scene mall temp with dissolve
    play sound "audio/crowd_noise.mp3" fadein 1.0
    $ quick_menu = True
    mcname "Rame juga ya ternyata mall di Jakarta ini..."
    "Di sekeliling banyak orang terlihat, dari keluarga kecil, pasangan muda yang sedang kencan, bahkan seseorang yang terlihat sendirian menikmati waktunya."
    "Namun dari banyaknya orang di sekitar, ada beberapa kumpulan orang yang menarik perhatian [mcname]."
    mcname "Lumayan nyentrik pakaian orang-orang itu yah, mungkin itu normal di Jakarta?"
    mcname "Ahhhh! Kayaknya lagi cosplay, yang sering mamah lakuin..."
    stop music fadeout 1.0
    #*Transisi Screen Putih 2s*
    #Flashback (ATas bawah putih)
    #BGM Rumah
    #BG Kamar MC
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}DAHULU KALA...{/color}" with Pause(2.0)
    scene white with Dissolve(2.0)
    # Harusnya ada frame putih atas bawah
    play music "audio/backsound_kamar.mp3" loop fadein 1.0
    scene mc bedroom with dissolve
    $ quick_menu = True
    mcname "Pah, itu apa yang dipakai Mamah?"
    show papah at char_left with dissolve
    #show papah_side at left with dissolve
    papah "Ohhh, itu namanya cosplay."
    #hide papah_side with dissolve
    mcname "Memangnya cosplay itu apa?"
    show mama at char_right with dissolve
    #show mama_side at left with dissolve
    mama "Cosplay itu costume play. Biasanya dipake sama orang yang suka anime, buat di event atau lomba gitu."
    #hide mama_side with dissolve
    #show papah_side at left with dissolve
    papah "Kalo Papah sama Mamah biasanya buat malam-malam, hehe."
    #hide papah_side with dissolve
    #show mama at char_center with dissolve
    #show mama_side at left with dissolve
    mama "Huss jangan ajarin yang aneh-aneh. [mcname] masih kecil."
    #hide mama_side with dissolve
    #hide mama at char_center with dissolve
    #show papah_side at left with dissolve
    papah "Ahahaha. Gapapa, like father like son."
    #hide papah_side with dissolve
    #show mama at char_center with dissolve
    #show mama_side at left with dissolve
    mama "Udah ihhh."
    #hide mama_side with dissolve
    #hide mama at char_center with dissolve
    #show papah_side at left with dissolve
    papah "Jadi pengen nanti malam, hehe."
    #hide papah_side with dissolve
    #show mama at char_center with dissolve
    #show mama_side at left with dissolve
    mama "*Blush*"
    #hide mama_side with dissolve
    #hide mama at char_center with dissolve
    mcname "{i}Saat itu aku gak begitu paham dengan apa yang mereka bicarakan...{/i}"
    stop music fadeout 1.0
    #*balik dari flashback"
    #BGM Rumah STOP
    #BG Kamar [mcname] STOP
    #*Transisi Screen Putih 2s*
    #BG Mall Start
    #BGM Mall Start
    $ quick_menu = False
    scene white with Dissolve(2.0)
    # Harusnya ada frame putih atas bawah
    scene mall temp with dissolve
    play music "audio/BGM_Mall Slow.mp3" loop fadein 1.0
    $ quick_menu = True
    mcname "{i}Kalo ada orang yang cosplay, berarti ada event yang sedang berlangsung di mall ini.{/i}"
    mcname "{i}Gak ada salahnya nanti aku mampir sebentar ke sana.{/i}"
    "[mcname] kemudian berkeliling mall untuk melihat-lihat di mall, sampai akhirnya ia sampai ke event jejepangan di mall tersebut."
    mcname "Waaah banyak juga ternyata orang-orang di sini."
    mcname "Kalau papah di sini mungkin bakal kesenengan tuh, hahaha."
    "[mcname] pun mencoba berkeliling melihat-lihat apa saja yang ada di event tersebut."
    "Di dalam event terlihat banyak booth-booth yang dibuka, mulai seperti mencoba kuliner yang ada di sana, melihat merch-merch event, bahkan [mcname] juga foto bersama cosplayer."
    "Tiba-tiba..."
    #Chibi Nue
    #*BRUKKK*
    play audio "audio/tabrakan.mp3"
    "Sepertinya [mcname] tidak sengaja menabrak seseorang saat berjalan."
    mcname "Waduh maaf kamu gapapa?"
    "[mcname] mencoba mengulurkan tangannya."
    show kana_sh at char_center with dissolve
    "???" "Ah iya, aku gapapa."
    "Seakan terkejut melihat [mcname], orang tersebut langsung berdiri tergesa-gesa."
    "???" "Ah, m-maaf!"
    hide kana_sh with dissolve
    "Setelah mengatakan hal tersebut, orang tadi langsung berlari pergi."
    mcname "......."
    mcname "Buru-buru banget itu orang."
    mcname "{i}Hmmm... Mungkin ada merch yang dia pengen, jadi kayak gitu.{/i}"
    mcname "Jadi ngingetin kayak papah dulu, haha."
    mcname "Hmm..?"
    "[mcname] menyadari ada sesuatu yang jatuh."
    #SHOW ASSET GANTUNGAN KUNCI.
    mcname "{i}Kayaknya ini barang orang tadi.{/i}"
    "[mcname] pun mengambil barang tersebut untuk memastikannya."
    "Terlihat sebuah merch dari salah satu utaite yang bisa dibilang cukup terkenal."
    mcname "Jangan-jangan ini barang limited, soalnya pernah liat nih di internet."
    "[mcname] kemudian mencoba melihat ke orang yang baru saja menabraknya."
    "Jarak antara [mcname] dan orang tersebut sudah bisa dibilang lumayan jauh."
    mcname "HEYYY!!! HEYYY!! BARANG MU JATUH!!!"
    "Namun karena begitu ramainya orang yang ada di dalam event, suara [mcname] tidak terdengar oleh orang tersebut."
    mcname "{i}Hmmm... Sepertinya tidak terdengar.{/i}"
    mcname "Kutitipkan ke penitipan barang sama panitia event atau..."
    mcname "... atau aku kejar ya orang yang tadi?"
    menu:
        "Yang [mcname] lakukan..."
        "Kejar orang yang tadi":
            mcname "Aku harus kejar orang yang tadi! Oke saatnya aku keluarkan jurus lari ninja ku, cyaattt!"
            $ quick_menu = False
            stop music fadeout 1.0
            scene black with dissolve
            show text "{color=#FFF}*BUKANNYA KETEMU SAMA ORANG YANG JATUHIN MERCH KAMU MALAH DISANGKA LAGI COSPLAY DAN DI SURUH TAMPIL DI PANGGUNG DAN MENANG, DAN AKHIRNYA LU LUPA SAMA ORANG YANG TADI*{/color}" with Pause(2.0)
            show text "{color=#FFF}*YAHAHA, NIAT NGEJAR MALAH JUARA! BAGUS SIH, TAPI KAN SEKARANG LU MALAH LUPA BUAT NGEMBALIIN BARANG TADI.*{/color}" with Pause(2.0)
            show text "{color=#FF0000}BAD END{/color}"
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits
        "Titipkan barang ke panitia event":
            "[mcname] pun memilih untuk menitipkan barang tersebut ke pada panitia yang bertugas."
            "Ahirnya panitia pun membuat pengumuman adanya barang hilang."
            jump kanachapter2titippanitia

label kanachapter2titippanitia:
    #*SKIP TO SCENE*
    #*BG KELAS PAGI*
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}KEESOKAN HARINYA{/color}" with Pause(2.0)
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    scene kelas with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    "Di kelas Jeketi University, terlihat banyak mahasiswa melakukan aktivitasnya."
    mcname "Haduuhh, barangnya gimana ya..."
    show kana_talk at kana_near with dissolve
    show kana_side_talk at left with dissolve
    kana "Barang? Barang apaan? Memangnya kamu pesen online [mcname]?"
    hide kana_side_talk at left with dissolve
    show kana at kana_near with dissolve
    hide kana_talk
    mcname "Ah enggak, jadi kemarin ada event jejepangan di mall pas aku lagi jalan-jalan."
    mcname "Di sana gak sengaja tuh aku ketabrak sama orang."
    hide kana at kana_near with dissolve
    show freya at char_left with dissolve
    show kana at char_right with dissolve
    show freya_shock at char_left with dissolve
    hide freya
    show freya_side_shock at left with dissolve
    freya "Ehhh kamunya gapapa tuh?"
    hide freya_side_shock at left with dissolve
    show kana_confused at char_right with dissolve
    hide kana
    show kana_side_confused at left with dissolve
    kana "Ah iya, kamunya gapapa?"
    hide kana_side_confused at left with dissolve
    mcname "Gapapa kok."
    mcname "Nah, orang itu gak sengaja jatuhin barang yang dia bawa. Merch limited dari Utaite yang terkenal itu, loh."
    show kana_shy at char_right with dissolve
    hide kana_confused
    show freya_awe at char_left with dissolve
    hide freya_shock
    show freya_side_awe at left with dissolve
    freya "Ehhh, merchnya Utaite yang terkenal itu..."
    hide freya_side_awe at left with dissolve
    "Freya berkata sambil melirik Kana."
    mcname "Aku ga paham sama orang-orang yang suka begituan."
    mcname "Kayak Papahku itu, agak aneh emang."
    show kana_drylaugh at char_right with dissolve
    hide kana_shy
    show kana_side_drylaugh at left with dissolve
    kana "Ahahah\n*Tertawa karir*"
    kana "Emang aneh ya, haha."
    hide kana_side_drylaugh at left with dissolve
    stop music fadeout 1.0
    $ quick_menu=False
    scene black with dissolve
    play music "audio/BGM_Dosen + Rektor.mp3" fadein 1.0
    scene kelas with dissolve
    $ quick_menu=True
    "Tidak lama kemudian, dosen pun masuk ke dalam kelas dan waktu mata kuliah pun dimulai."
    show dosen at dosen_center with dissolve
    show dosen_talk at dosen_center with dissolve
    hide dosen
    show dosen_side at left with dissolve
    dosen "Teman-teman, mari kita mulai perkuliahan hari ini."
    hide dosen_side at left with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    scene kelas with dissolve
    $ quick_menu = True
    mcname "Wahh akhirnya selesai juga~"
    show kana at char_right with dissolve
    show freya at char_left with dissolve
    show kana_talk at char_right with dissolve
    hide kana
    show kana_side_talk at left with dissolve
    kana "Kalo gini enaknya ke kantin sih."
    hide kana_side_talk at left with dissolve
    mcname "Aduh, tapi jam segini kantin pasti penuh."
    show kana at char_right with dissolve
    hide kana_talk
    show freya_talk at char_left with dissolve
    hide freya
    show freya_side_talk at left with dissolve
    freya "Hmmm. Gimana kalo bawa makanan dari kantin ke rooftop? Denger-denger tempatnya enak."
    hide freya_side_talk at left with dissolve
    show kana_talk at char_right with dissolve
    hide kana
    show kana_side_talk at left with dissolve
    kana "Ehhh, boleh tuh. Tapi jangan makanan berat, nanti ribet bawanya."
    hide kana_side_talk at left with dissolve
    mcname "Yaudah aku ke kantin ya. Sekalian aku beliin makanan buat kalian."
    show kana_smile at char_right with dissolve
    hide kana_talk
    show freya_smile at char_left with dissolve
    hide freya_talk
    show kana_side_talk at left with dissolve
    kana "Okee. Aku sama Freya nunggu di rooftop, ya."
    hide kana_side_talk at left with dissolve
    #*Transisi Hitam*
    #BG Hallway
    #BGM Hallway
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Lorong.mp3" fadein 1.0
    scene lorong with dissolve
    $ quick_menu = True
    "Setelah [mcname] membeli makanan di kantin, [mcname] berjalan menuju tangga ke rooftop."
    #BG Rooftop
    #BGM Rooftop
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Rooftop Romance Pia.mp3" fadein 1.0
    scene rooftop with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    "Sesampainya di rooftop, [mcname] hanya melihat Kana yang memandang langit sendirian."
    show kana at kana_near with dissolve
    mcname "Loh, sendirian Kana? Freya mana?"
    show kana_talk at kana_near with dissolve
    hide kana
    show kana_side_talk at left with dissolve
    kana "Freya tadi mendadak ada urusan. Jadinya dia pulang duluan."
    hide kana_side_talk at left with dissolve
    show kana at kana_near with dissolve
    hide kana_talk
    mcname "Heeee~"
    show kana_talk at kana_near with dissolve
    hide kana
    show kana_side_talk at left with dissolve
    kana "Aku udah chat, tapi keknya gak kebaca sama kamu ya."
    hide kana_side_talk at left with dissolve
    show kana at kana_near with dissolve
    hide kana_talk
    "[mcname] kemudian membuka HPnya."
    "Di sana terlihat banyak notif chat dari Kana dan Freya."
    mcname "Ah iya, sorry banget. Tadi di kantin rame banget, jadi gak kebaca."
    show kana_smile at kana_near with dissolve
    hide kana
    show kana_side_talk at left with dissolve
    kana "Yaudah. Yuk kita duduk makan dulu."
    hide kana_side_talk at left with dissolve
    mcname "Oke."
    $ quick_menu = False
    scene black with dissolve
    scene rooftop with dissolve
    show kana at kana_near with dissolve
    $ quick_menu = True
    mcname "Kamu mau yang cokelat, strawberry, atau keju?"
    show kana_talk at kana_near with dissolve
    hide kana
    show kana_side_talk at left with dissolve
    kana "Kayaknya aku yang strawberry aja deh."
    hide kana_side_talk at left with dissolve
    show kana_smile at kana_near with dissolve
    hide kana_talk
    "Setelah memberikan Kana roti yang dia pilih, akhirnya [mcname] dan Kana duduk di bangku yang ada di rooftop."
    "Di sana, Kana dan [mcname] menikmati roti sambil memandangi langit biru. Mereka tidak mengeluarkan sepatah kata pun. Suasana hening menjadi terasa sedikit canggung."
    mcname "{i}Duh bingung mau ngomong apaan. Biasanya Freya yang mulai obrolan.{/i}"
    "Ingin mencairkan suasana, [mcname] mencoba memulai percakapan."
    show kana_confused at kana_near with dissolve
    hide kana_smile
    mcname "A-"
    show kana_side_confused at left with dissolve
    kana "Kamu kabarnya gimana?"
    hide kana_side_confused at left with dissolve
    "Sebelum [mcname] sempat berbicara, Kana tiba-tiba memberikan pertanyaan."
    mcname "E-eeh?"
    show kana_confused_blush_sideeye at kana_near with dissolve
    hide kana_confused
    show kana_side_confused at left with dissolve
    kana "Kamu udah makan, belum?"
    hide kana_side_confused at left with dissolve
    mcname "?????"
    mcname "Kan kita lagi makan, Kana..."
    show kana_shy_talk at kana_near with dissolve
    hide kana_confused_blush_sideeye
    show kana_side_shy_smile at left with dissolve
    kana "Ah i-iya yah. Hahaha ngomong apa sih aku."
    hide kana_side_shy_smile at left with dissolve
    show kana_shy_closeeye at kana_near with dissolve
    hide kana_shy_talk
    "Setelah Kana mengatakan hal tersebut, suasananya kembali menjadi hening."
    show kana_shy_talk at kana_near with dissolve
    hide kana_shy_closeeye
    show kana_side_shy_smile at left with dissolve
    kana "Biasanya ada Freya ya, yang ngomong mulu."
    hide kana_side_shy_smile at left with dissolve
    mcname "Haha, iya yah."
    show kana_drylaugh at kana_near with dissolve
    hide kana_shy_talk
    show kana_side_drylaugh at left with dissolve
    kana "Haha."
    hide kana_side_drylaugh at left with dissolve
    mcname "Haha."
    show kana_shy_smile at kana_near with dissolve
    hide kana_drylaugh
    show kana_side_shy_smile at left with dissolve
    kana "Fufu."
    hide kana_side_shy_smile at left with dissolve
    show kana at kana_near with dissolve
    hide kana_shy_smile at kana_near with dissolve
    mcname "Dilihat-lihat kamu emang deket banget ya sama Freya."
    show kana_talk at kana_near with dissolve
    hide kana
    show kana_side_talk at left with dissolve
    kana "Iya. Dari kecil, emang Freya selalu bareng aku."
    hide kana_side_talk at left with dissolve
    show kana at kana_near with dissolve
    hide kana_talk
    mcname "....."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Rooftop Romance Pia.mp3" fadein 1.0
    #HARUSNYA LAGU SAD KANA
    scene awan with dissolve
    $ quick_menu = True
    show kana at kana_near with dissolve
    show kana_talk at kana_near with dissolve
    hide kana
    show kana_side_talk at left with dissolve
    kana "Dulu…"
    hide kana_side_talk at left with dissolve
    "Kana menatap ke atas langit seakan mengingat masa lalu."
    hide kana_talk with dissolve
    "CG Chibi Kana Freya"
    show kana_side_talk at left with dissolve
    kana "Dulu badanku lemah dan sering sakit, jadinya jarang keluar rumah."
    kana "Waktu yang lain pada main di luar, aku cuma bisa liat mereka dari jendela kamarku."
    kana "Untungnya waktu itu Freya ada dan mau main bareng aku."
    kana "Padahal bisa aja dia main sama anak-anak yang lain, tapi dia malah nemenin aku."
    kana "Jadinya sampe sekarang bareng terus deh aku sama Freya, haha."
    hide kana_side_talk at left with dissolve
    #Hide CG
    show kana_smile at kana_near with dissolve
    "Saat mengatakan hal tersebut, Kanaia tersenyum mengingat teman berharganya."
    mcname "Heee gitu ya ternyata…"
    "Mendengar hal tersebut, [mcname] merasa sedikit iri kepada Freya yang bisa membuat Kana tersenyum seperti itu."
    stop music fadeout 1.0
    $ quick_menu = False
    play audio "audio/open_door.mp3"
    scene black with dissolve
    $ quick_menu = True
    "Tiba-tiba dari arah berlawanan terdengar suara pintu terbuka."
    $ quick_menu = False
    play music "audio/BGM_Rooftop Romance Pia.mp3" fadein 1.0
    scene rooftop with dissolve
    $ quick_menu = True
    show freya at char_left with dissolve
    show kana at char_right with dissolve
    show freya_talk at char_left with dissolve
    hide freya
    show freya_side_talk at left with dissolve
    freya "Halooooo, sorry. Lama nungguin, ya?"
    hide freya_side_talk at left with dissolve
    show freya_smile at char_left with dissolve
    hide freya_talk
    show kana_talk at char_right with dissolve
    hide kana
    show kana_side_talk at left with dissolve
    kana "Ah! Freyaa."
    hide kana_side_talk at left with dissolve
    show kana at char_right with dissolve
    hide kana_talk
    mcname "Nggak kok."
    show kana_talk at char_right with dissolve
    hide kana
    show kana_side_talk at left with dissolve
    kana "Ayok sini makan."
    hide kana_side_talk at left with dissolve
    show kana_smile at char_right with dissolve
    hide kana_talk
    show freya_talk at char_left with dissolve
    hide freya_smile
    show freya_side_talk at left with dissolve
    freya "Okeee~"
    hide freya_side_talk at left with dissolve
    "Mereka pun menghabiskan waktu dengan berbincang dan makan bersama..."
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}KEESOKAN HARINYA{/color}" with Pause(2.0)
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    scene kelas with dissolve
    #$ renpy.block_rollback()
    $ quick_menu = True
    show kana at char_right with dissolve
    show freya at char_left with dissolve
    show kana_talk at char_right with dissolve
    hide kana
    show kana_side_talk at left with dissolve
    kana "[mcname]! Freya! Eh liat ini! Lucu banget gak sih? Kemarin aku liat di internet."
    hide kana_side_talk at left with dissolve
    show kana at char_right with dissolve
    hide kana_talk
    mcname "Hooo aku pernah liat ada toko yang jual boneka ini nih, waktu ke mall kemarin."
    show kana_talk at char_right with dissolve
    hide kana
    show kana_side_talk at left with dissolve
    kana "Heee serius? Habis ini kalian free, kan? Yuk ke sana bareng!"
    hide kana_side_talk at left with dissolve
    show kana_smile at char_right with dissolve
    hide kana_talk
    show freya_talk at char_left with dissolve
    hide freya
    show freya_side_talk at left with dissolve
    freya "Ayoook. Aku juga free, sih."
    hide freya_side_talk at left with dissolve
    show kana_talk at char_right with dissolve
    hide kana_smile
    show kana_side_talk at left with dissolve
    kana "[mcname] nanti ikut yak, soalnya kamu kan yang tau tempatnya."
    hide kana_side_talk at left with dissolve
    mcname "Bolehh~"
    "Beberapa saat kemudian, dosen pun datang memasuki ruangan kelas."
    hide kana_talk with dissolve
    hide freya_talk with dissolve
    stop music fadeout 1.0
    play music "audio/BGM_Dosen + Rektor.mp3" fadein 1.0
    show dosen at dosen_center with dissolve
    show dosen_talk at dosen_center with dissolve
    dosen "Selamat pagi. Pelajaran akan dimulai."
    $ quick_menu = False
    scene black with dissolve
    scene kelas with dissolve
    show dosen_talk at dosen_center with dissolve
    $ quick_menu = True
    show dosen_side at left with dissolve
    dosen "Yak. Mata kuliah ini sudah sampai sini dulu. Selanjutnya kalian review masing-masing, ya."
    dosen "Ah iya Freya. Untuk pembahasan kemarin, Ibu tunggu di ruangan Ibu sekarang, ya."
    hide dosen_side at left with dissolve
    hide dosen_talk at dosen_center with dissolve
    show freya_shock at char_center with dissolve
    show freya_side_shock at left with dissolve
    freya "Ehhh……"
    freya "Baik, Bu."
    hide freya_side_shock at left with dissolve
    "Bu Dosen pergi meninggalkan ruang kelas, para mahasiswa pun mulai merapikan barangnya."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    scene kelas with dissolve
    $ quick_menu = True
    show freya at char_left with dissolve
    show kana_talk at char_right with dissolve
    show kana_side_talk at left with dissolve
    kana "Akhirnya selesai juga~"
    hide kana_side_talk at left with dissolve
    show kana at char_right with dissolve
    hide kana_talk
    mcname "Jadi? Masih mau ke sana?"
    show kana_talk at char_right with dissolve
    hide kana
    show kana_side_talk at left with dissolve
    kana "Iya dong."
    hide kana_side_talk at left with dissolve
    show freya_pouting at char_left with dissolve
    hide freya
    show freya_side_pouting at left with dissolve
    freya "Yahhh, sorry guys. Kayaknya aku gak bisa ikut nemenin kalian."
    hide freya_side_pouting at left with dissolve
    show kana_confused at char_right with dissolve
    hide kana_talk
    show kana_side_confused at left with dissolve
    kana "Yahhhh..."
    hide kana_side_confused at left with dissolve
    show freya_talk at char_left with dissolve
    hide freya_pouting
    show freya_side_talk at left with dissolve
    freya "Gapapa kok. Kan ada [mcname]."
    freya "[mcname]! Kamu jagain Kana, ya."
    hide freya_side_talk at left with dissolve
    show freya_smile at char_left with dissolve
    hide freya_talk
    show kana_shy_smile at char_right with dissolve
    hide kana_confused
    show kana_side_shy_smile at left with dissolve
    kana "E.. eeeeh."
    hide kana_side_shy_smile at left with dissolve
    hide freya_smile
    "Freya pun menyusul Dosen, meninggalkan Kana dan [mcname] berdua."
    mcname "Yaudah, yuk."
    show kana_confused_blush_sideeye at char_right with dissolve
    hide kana_shy_smile
    show kana_side_shy_smile at left with dissolve
    kana "I-iya."
    hide kana_side_shy_smile at left with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Mall Slow.mp3" fadein 1.0
    scene mall temp with dissolve
    #$ renpy.block_rollback()
    $ quick_menu = True
    "Kana dan [mcname] mendatangi mall yang dimaksud."
    show kana_smile at char_center with dissolve
    show kana_talk at char_center with dissolve
    hide kana
    show kana_side_talk at left with dissolve
    kana "Kamu sering ke mall ini, ya?"
    hide kana_side_talk at left with dissolve
    mcname "Nggak juga, kok. Kemarin kebetulan aja inget."
    mcname "Kalo kamu?"
    show kana_side_talk at left with dissolve
    kana "Aku biasanya di rumah aja, sih."
    hide kana_side_talk at left with dissolve
    show kana_smile at char_center with dissolve
    hide kana_talk
    mcname "Weh. Kalo gitu mau coba sekalian jalan-jalan? Mumpung kamu di sini."
    show kana_confused at char_center with dissolve
    hide kana_smile
    show kana_side_confused at left with dissolve
    kana "Ehhh, tapi kamu gapapa kah?"
    hide kana_side_confused at left with dissolve
    mcname "Gapapa, kok. Lagi free juga, hehe."
    "Mereka kemudian berjalan bersama sambil berbincang."
    $ quick_menu = False
    scene black with dissolve
    scene mall temp with dissolve
    $ quick_menu = True
    "Tiba-tiba saat membahas topik pembicaraan, Kana tidak merespon sehingga [mcname] mencoba untuk menengok ke arah Kana."
    mcname "{i}Loh, Kana ke mana?{/i}"
    "[mcname] pun melihat ke belakang. Di sana terlihat Kana sedang menatap salah satu baju yang dipajang di mall."
    #Asset Baju Kana yg dipajang
    show kana at char_center with dissolve
    mcname "Eh, Kana? Ada apa?"
    show kana_side at left with dissolve
    kana "..."
    hide kana_side at left with dissolve
    mcname "Kana? Nanti ketinggalan lohhh."
    show kana_talk at char_center with dissolve
    hide kana
    show kana_side_talk at left with dissolve
    kana "Ah! Iya."
    hide kana_side_talk at left with dissolve
    "Kana kemudian menghampiri [mcname]."
    show kana_smile at char_center with dissolve
    hide kana_talk
    show kana_side_talk at left with dissolve
    kana "BTW, di mana tempat yang jual bonekanya, [mcname]?"
    hide kana_side_talk at left with dissolve
    mcname "Di situ, ayok."
    show kana_talk at char_center with dissolve
    hide kana_smile
    show kana_side_talk at left with dissolve
    kana "Okee."
    $ quick_menu = False
    scene black with dissolve
    scene mall temp with dissolve
    #MALL SPONSOR
    $ quick_menu = True
    "Sesampainya di toko tersebut..."
    mcname "Permisi, Kak. Kalau boneka yang ini masih ada?"
    "Pelayan Toko" "Maaf Kak. Sepertinya boneka yang Kakak cari itu udh habis stock yang ready."
    "Pelayan Toko" "Kalo mau bisa pre-order, tapi nunggunya sekitar 90 hari."
    mcname "{i}Wah, lama banget. Seperti waktu Papah mau PO merch idol group kesukaannya.{/i}"
    show kana_clumsy at char_center with dissolve
    show kana_side_clumsy at left with dissolve
    kana "Yahhhh, gimana nih? Kalo PO kayaknya lama banget."
    hide kana_side_clumsy at left with dissolve
    mcname "Gimana kalo kita jalan, liat-liat yang lain dulu. Siapa tau ada barang lucu lainnya."
    show kana_side_clumsy at left with dissolve
    kana "Oke deh."
    hide kana_side_clumsy at left with dissolve
    "Namun muka Kana terlihat sedikit kecewa."
    "Kana dan [mcname] pun kembali berjalan berkeliling di mall."
    $ quick_menu = False
    scene black with dissolve
    scene mall temp with dissolve
    #MALL SPONSOR
    show kana_clumsy at char_center with dissolve
    $ quick_menu = True
    mcname "{i}Sepertinya Kana masih kecewa dengan kejadian tadi.{/i}"
    mcname "Kana, gimana kalo kita ke game center aja?"
    show kana_side_clumsy at left with dissolve
    kana "..."
    hide kana_side_clumsy at left with dissolve
    mcname "Kanaa?"
    hide kana_clumsy at char_center with dissolve
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    kana "Hmmmm? Eh maaf kurang fokus tadi, hahaha."
    hide kana_side at left with dissolve
    mcname "Ya udaah. Ayok ikut aku sini."
    show kana_side at left with dissolve
    kana "Eeeh? Emangnya mau ke mana?"
    hide kana_side at left with dissolve
    mcname "Udaaah, ikut aja."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Game Center.mp3" fadein 1.0
    scene game center with dissolve
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    $ quick_menu = True
    kana "Heeee? Di sini ada game center ternyata."
    hide kana_side at left with dissolve
    mcname "Mau nyoba game di sini, Kana? Aku lumayan pede loh sama skill racing aku."
    show kana_side at left with dissolve
    kana "Bolehhh siapa takut?"
    hide kana_side at left with dissolve
    $ quick_menu = False
    scene black with dissolve
    scene game center with dissolve
    play sound "audio/SFX_Racing Game.ogg" loop fadein 1.0 volume 0.2
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    $ quick_menu = True
    kana "Liat nih skill racing aku."
    hide kana_side at left with dissolve
    mcname "Wih jago juga kamu. Udah rank 1 aja."
    show kana_side at left with dissolve
    kana "Hehe. Kan namaku Kanaia \"Resing\" Asa."
    hide kana_side at left with dissolve
    play audio "audio/SFX - Car Crash.mp3" volume 0.5
    $ quick_menu = False
    window auto hide
    with Pause(4.0)
    window auto show
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    $ quick_menu = True
    kana "Eh? Eh? Kok aku ditabrak mulu. Waaaaaa~"
    hide kana_side at left with dissolve
    mcname "Eh, gimana ini Kana? Sekarang malah aku yang di depan. Hehe~"
    show kana_side at left with dissolve
    kana "Arrgh! Liat aja nanti."
    hide kana_side at left with dissolve
    mcname "Weh aku udah di lap terakhir, nih!"
    play audio "audio/SFX - Car Crash.mp3" volume 0.5
    $ quick_menu = False
    window auto hide
    with Pause(4.0)
    window auto show
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    $ quick_menu = True
    kana "Noooo~ Aku nabrak mulu."
    hide kana_side at left with dissolve
    mcname "Inget rem, Kana. Hahahaha!"
    show kana_side at left with dissolve
    kana "Ahhhhh! Jangan tabrak akuuu~"
    hide kana_side at left with dissolve
    stop sound fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    scene game center with dissolve
    show kana at char_center with dissolve
    $ quick_menu = True
    mcname "Hahaha gimana nih Kana? Malah aku yang Rank 1."
    show kana_side at left with dissolve
    kana "Sekali lagi laahh, aku masih gak terima."
    hide kana_side at left with dissolve
    "Akhirnya mereka memainkan game tersebut berkali kali."
    play sound "audio/SFX_Racing Game.ogg" loop fadein 1.0 volume 0.2
    $ quick_menu = False
    scene black with Dissolve(1.5)
    with Pause (2.0)
    scene game center with Dissolve(1.5)
    stop sound fadeout 1.0  
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    $ quick_menu = True
    kana "Hahaha gimana aku, hebat kan bisa Rank 1?"
    hide kana_side at left with dissolve
    mcname "Tapi kan kamu tadi kalah mulu."
    show kana_side at left with dissolve
    kana "Hmph. Yang penting game terakhir aku menang."
    hide kana_side at left with dissolve
    mcname "Hahaha. Iya deh kamu jago banget."
    mcname "Gimana? Mau racing lagi?"
    show kana_side at left with dissolve
    kana "Nggak, ah. Kita ganti game. The last winner wins. Hehe."
    hide kana_side at left with dissolve
    "Selanjutnya Kana mengajak [mcname] main game Whack-a-mole."
    stop sound fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    scene game center with dissolve
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    $ quick_menu = True
    kana "Aku jago banget kalo mukul-mukul gini."
    hide kana_side at left with dissolve
    mcname "Iya iyaa."
    play sound "audio/SFX - Countdown.mp3" fadein 1.0
    $ quick_menu = False
    window auto hide
    with Pause(4.5)
    window auto show
    play sound "audio/SFX - Whack.mp3" loop fadein 1.0
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    $ quick_menu = True
    kana "Aduhh banyak yang miss."
    hide kana_side at left with dissolve
    mcname "Ayokk semangat Kanaa."
    show kana_side at left with dissolve
    kana "Waaaa~"
    hide kana_side at left with dissolve
    mcname "Itu yang itu, Kana."
    show kana_side at left with dissolve
    kana "Ah, kamu backseat muluu!"
    hide kana_side at left with dissolve
    mcname "Geregetan soalnyaa."
    stop sound fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    scene game center with dissolve
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    $ quick_menu = True
    kana "Fiuhh... akhirnya."
    hide kana_side at left with dissolve
    play sound "audio/SFX - Finish Game.mp3" fadein 1.0 volume 0.5
    "Setelah waktunya habis, Kana melihat papan high score."
    show kana_side at left with dissolve
    kana "Waaah! [mcname] liat! [mcname]! Highest score! Yeayy!"
    hide kana_side at left with dissolve
    mcname "Gils jago bangettz."
    show kana_side at left with dissolve
    kana "Hehe~"
    hide kana_side at left with dissolve
    mcname "Gimana?"
    show kana_side at left with dissolve
    kana "Haha kayaknya udah cukup ya, soalnya udah lumayan lama kita di sini."
    hide kana_side at left with dissolve
    $ quick_menu = False
    scene black with dissolve
    scene game center with dissolve
    $ quick_menu = True
    "Saat [mcname] dan Kana mau pulang, tidak sengaja [mcname] melihat ada boneka yang diinginkan Kana di dalam box Push Claw Machine."
    show kana at char_center with dissolve
    mcname "Eh. Itu kan boneka yang kamu pengen?"
    show kana_side at left with dissolve
    kana "Eh, mana? Mana?"
    hide kana_side at left with dissolve
    mcname "Ituuu, di kananmu."
    "[mcname] menunjuk ke arah crane game."
    show kana_side at left with dissolve
    kana "Wahhh, crane game ya?"
    hide kana_side at left with dissolve
    mcname "Heee kamu tau crane game, Kana?"
    show kana_side at left with dissolve
    kana "Mhm... Kalo main gak pernah sih, tapi aku sering denger."
    hide kana_side at left with dissolve
    mcname "Mau coba mainin?"
    show kana_side at left with dissolve
    kana "Ayook!"
    hide kana_side at left with dissolve
    "Kana mencoba game crane tersebut."
    #CG Chibi Kana Claw Machine TANPA MC*
    play sound "audio/SFX - Countdown.mp3" fadein 1.0
    $ quick_menu = False
    window auto hide
    with Pause(4.5)
    window auto show
    $ quick_menu = True
    "Setelah memperkirakan lokasi yang tepat, akhirnya Kana menekan tombol claw."
    "Claw-nya kemudian turun dan menangkap boneka yang diinginkan Kana."
    "Boneka tersebut terangkat sedikit, sebelum akhirnya terjatuh dan kembali seperti semula."
    show kana at char_center with dissolve
    mcname "Yaahh~ Sayang banget."
    show kana_side at left with dissolve
    kana "Nooooo~"
    hide kana_side at left with dissolve
    mcname "Ayo coba lagi."
    show kana_side at left with dissolve
    kana "Baiklah, sekali lagi!"
    hide kana_side at left with dissolve
    #CG Chibi Kana Claw Machine TANPA MC*    
    play sound "audio/SFX - Countdown.mp3" fadein 1.0
    $ quick_menu = False
    window auto hide
    with Pause(4.0)
    scene black with dissolve
    scene game center with dissolve
    window auto show
    $ quick_menu = True
    "Kana mencoba lagi, tetapi hasilnya tetap sama."
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    kana "Huhu. Ternyata gamenya lumayan susah."
    hide kana_side at left with dissolve
    mcname "Sini aku bantuin."
    show kana_side at left with dissolve
    kana "Wihh, okeee. Kali ini pasti bisa!"
    hide kana_side at left with dissolve
    hide kana at char_center with dissolve
    #SFX 3 2 1 Go…
    #*CG Chibi Kana Claw Machine (With MC)*
    play sound "audio/SFX - Countdown.mp3" fadein 1.0
    $ quick_menu = False
    window auto hide
    with Pause(4.0)
    window auto show
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    $ quick_menu = True
    kana "Gimana? Udah pas belum?"
    hide kana_side at left with dissolve
    mcname "Maju dikit lagi tuh."
    show kana_side at left with dissolve
    kana "Gimana kalo sekarang?"
    hide kana_side at left with dissolve
    mcname "Ke kanan dikittt."
    show kana_side at left with dissolve
    kana "Gini?"
    hide kana_side at left with dissolve
    mcname "Oke sekarang!!"
    #Chibi Kana API API.
    show kana_side at left with dissolve
    kana "YOSHH!"
    hide kana_side at left with dissolve
    "Kana akhirnya menekan tombol claw."
    show kana_side at left with dissolve
    kana "Please!!! Pleasee!!!"
    hide kana_side at left with dissolve
    #Chibi Kana API API FINAL.
    play sound "audio/SFX - Finish Game 2.mp3"
    "Terdengar suara boneka jatuh ke kotak hadiah."
    show kana_side at left with dissolve
    kana "YAAAAAYYY!"
    hide kana_side at left with dissolve
    "Kana kemudian mengambil boneka tersebut dari kotak hadiah dan langsung memeluknya. [mcname] melihat pemandangan tersebut sambil tersenyum kecil."
    show kana_side at left with dissolve
    kana "Hehe makasih banyak ya, [mcname]. Karena kamu ngebantu arahin, jadi bisa dapet boneka ini."
    hide kana_side at left with dissolve
    mcname "Haha gapapa kok, aku seneng juga akhirnya kamu dapet boneka yang kamu pengen."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Mall Slow.mp3" fadein 1.0
    scene mall temp with dissolve
    $ quick_menu = True
    "Sepulang dari game arcade..."
    "Kana membawa tas belanja dia dan juga boneka yang dia dapat dari claw machine tadi, wajahnya terlihat senang."
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    kana "Makasih ya [mcname] untuk hari ini."
    hide kana_side at left with dissolve
    mcname "Iya, sama-sama Kana."
    show kana_side at left with dissolve
    kana "Hari ini aku senang banget."
    hide kana_side at left with dissolve
    "Melihat Kana tersenyum, membuat [mcname] tersenyum juga."
    #*Transisi putih*
    #BG LANGIT
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}KEESOKAN HARINYA{/color}" with Pause(2.0)
    play music "audio/BGM_Kampus.mp3" fadein 1.0
    scene depan kampus with dissolve
    $ quick_menu = True
    "Suasananya sama seperti hari-hari sebelumnya."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    scene kelas with dissolve
    $ renpy.block_rollback()
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    $ quick_menu = True
    kana "Pagii [mcname]~"
    hide kana_side at left with dissolve
    mcname "Pagi juga~"
    show kana_side at left with dissolve
    kana "Gimana kabarnya hari ini?"
    hide kana_side at left with dissolve
    mcname "Baik. Gimana kemarin pulangnya? Aman gak?"
    show kana_side at left with dissolve
    kana "Aman kok. Bareng supir soalnya, hehe."
    hide kana_side at left with dissolve
    mcname "Wih enak ya punya supir."
    show kana_side at left with dissolve
    kana "Nanti kapan-kapan kamu mau kan nemenin aku lagi?"
    kana "Nanti pulangnya dianter deh."
    hide kana_side at left with dissolve
    mcname "Wahh, okee."
    "Saat Kana dan [mcname] sibuk berbincang, Freya datang menghampiri."
    hide kana at char_center with dissolve
    show freya at char_left with dissolve
    show freya_side at left with dissolve
    freya "Pagi Kanaa~ Pagi [mcname]~"
    freya "Eh gimana kemarin kalian ngedatenya? Hehehe."
    hide freya_side at left with dissolve
    show kana at char_right with dissolve
    show kana_side at left with dissolve
    kana "Iiihhh ngedate apaan."
    kana "Kamu kan yang ninggalin kita."
    hide kana_side at left with dissolve
    "Kana mengatakan hal tersebut sambil tesipu malu."
    mcname "....."
    show freya_side at left with dissolve
    freya "Hmmm?????"
    hide freya_side at left with dissolve
    "Freya merasakan respons Kana sedikit berbeda dari biasanya."
    show freya_side at left with dissolve
    freya "Seee too... Ki wes ra bener ki.\n(Bentar... Ini ada yang ga bener nih.)"
    freya "Fellingku mengatakan ada yang mencurigakan."
    hide freya_side at left with dissolve
    show kana_side at left with dissolve
    kana "Apaan sihhh, ga da yang mecurigakan kok."
    hide kana_side at left with dissolve
    show freya_side at left with dissolve
    freya "Yang bener????"
    hide freya_side at left with dissolve
    show kana_side at left with dissolve
    kana "Apaan sihhh ahh Freya, aku malu tau diliatin gitu mulu."
    hide kana_side at left with dissolve
    show freya_side at left with dissolve
    freya "Hmmmmm..."
    hide freya_side at left with dissolve
    "Suara pintu pun terdengar dan dosen pun datang dengan terburu-buru, berbeda dari biasanya."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Dosen + Rektor.mp3" fadein 1.0
    scene kelas with dissolve
    show kana at char_right with dissolve
    show freya at char_left with dissolve
    show kana_side at left with dissolve
    $ quick_menu = True
    kana "Nah Bu dosen udah dateng tuh, nanti lanjut ngobrol lagi ya."
    hide kana_side at left with dissolve
    "Mendengar hal tersebut, mereka akhirnya duduk di tempat masing-masing."
    "Saat duduk di tempatnya, [mcname] mendengar sedikit percakapan antara Kana dan Freya."
    show freya_side at left with dissolve
    freya "Ceritain ya, kalian berdua ngapain aja kemarin."
    hide freya_side at left with dissolve
    show kana_side at left with dissolve
    kana "Iya deh, iya."
    hide kana_side at left with dissolve
    $ quick_menu = False
    scene black with dissolve
    scene kelas with dissolve
    show dosen at dosen_center with dissolve
    $ quick_menu = True
    show dosen_side at left with dissolve
    dosen "Baiklah semuanya, ibu hari ini akan mengajar dengan cepat karena ada rapat mendadak, jadi harap perhatikan dengan baik dan nantinya akan ada tugas dari ibu."
    hide dosen_side at left with dissolve
    "Dosen pun menjelaskan dan memberikan tugasnya kepada mahasiswa/i semuanya.."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    scene kelas with dissolve
    $ quick_menu = True
    mcname "Tumben juga kali ini cepet kelasnya, jadi ada waktu free gini."
    "[mcname] melakukan peregangan badan."
    mcname "Tapi... Tugas yang dikasih juga lumayan banyak."
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    kana "Iya, banyak banget ya tugasnya..."
    kana "Buat tugas ini kamu mau ngerjain bareng ga?"
    hide kana_side at left with dissolve
    mcname "Eh boleh kok."
    "[mcname] bingung karena Kana tiba-tiba mengajak [mcname] untuk mengerjakan tugas."
    mcname "Tapi Freya gimana?"
    hide kana at char_center with dissolve
    show kana at char_right with dissolve
    show freya at char_left with dissolve
    show freya_side at left with dissolve
    freya "Kalo aku kayaknya bakal besok aja ngerjainnya, soalnya lagi ada barang promo yang mau kubeli."
    freya "Sekalian biar kalian bisa barengan hahaha! Byeeee~"
    hide freya_side at left with dissolve
    hide kana at char_right with dissolve
    hide freya at char_left with dissolve
    "Setelah mengatakan hal tersebutm Freya langsung pergi meninggalkan kelas."
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    kana "Apaan sih Freya itu, kan niatnya cuma belajar bareng."
    hide kana_side at left with dissolve
    mcname "Ahahaha."
    "[mcname] hanya bisa tertawa canggung mendengar hal tersebut."
    show kana_side at left with dissolve
    kana "Jadi [mcname]..."
    hide kana_side at left with dissolve
    "Kana melihat [mcname]."
    show kana_side at left with dissolve
    kana "Kita ngerjain tugasnya mau di mana?"
    hide kana_side at left with dissolve
    menu:
        "[mcname] menjawab..."
        "Kantin":
            mcname "Hmmmm di kantin gimana? Soalnya bisa sambil ngemil."
            show kana_side at left with dissolve
            kana "Okeee~"
            hide kana_side at left with dissolve
            "[mcname] dan Kana berjalan menuju ke kantin."
            stop music fadeout 1.0
            $ quick_menu = False
            scene black with dissolve
            play music "audio/bgm_kantin.mp3" fadein 1.0
            scene kantin with dissolve
            $ renpy.block_rollback()
            $ quick_menu = True
            play sound "audio/crowd_noise.mp3" fadein 1.0
            "Di kantin terlihat sudah dipenuhi orang sehingga tidak ada tempat kosong untuk duduk."
            show kana at char_center with dissolve
            mcname "Kayaknya kantin penuh terus yak..."
            show kana_side at left with dissolve
            kana "Haha, iya nih."
            kana "Jadinya mau gimana?"
            hide kana_side at left with dissolve
            mcname "Hmmmm mau ke rooftop lagi? Kayaknya di sana bakal sepi."
            show kana_side at left with dissolve
            kana "Aku ngikut kamu aja."
            hide kana_side at left with dissolve
            mcname "O-oke."
            mcname "Kalau gitu Kana mau nitip apa? Biar nanti aku bawain."
            show kana_side at left with dissolve
            kana "Eh kalo [mcname] gimana?"
            hide kana_side at left with dissolve
            mcname "Kamu duluan aja, gapapa."
            "[mcname] mengatakan hal tersebut karena tidak ingin membuat Kana menunggu terlalu lama."
            show kana_side at left with dissolve
            kana "Oke deh, kalau gitu aku roti strawberry ya."
            hide kana_side at left with dissolve
            mcname "Siapppp~"
            "Setelah mengatakan hal tersebut, Kana akhirnya pergi duluan ke rooftop."
            mcname "Sebaiknya aku pesen dulu yang dipesen Kana."
            "[mcname] kemudian berjalan menuju kasir."
            "Di sana, [mcname] mendengarkan beberapa mahasiswa membicarakan tentang event kampus yang akan segera diadakan."
            "Mahasiswa A" "Eh, katanya event kampus nanti bakal ada lomba-lomba pertunjukan."   
            "Mahasiswa B" "Serius? Emang ada hadiahnya?"
            "Mahasiswa A" "Buat hadiahnya kurang tahu sih."
            "Mahasiswa A ""Tapi guest starnya nanti katanya sih Sabi Yoi."
            "Mahasiswa B" "Duh Sabi Yoi, agak bosen sih dengernya tapi gapapa lah."
            mcname "Heee menarik juga itu..."  
            jump chapter2kanaA
            
        "Rooftop":
            mcname "Hmmmm mau ke rooftop lagi? Kayaknya di sana bakal sepi."
            show kana_side at left with dissolve
            kana "Aku ngikut kamu aja."
            hide kana_side at left with dissolve
            mcname "O-oke."
            mcname "Kalau gitu aku ke kantin dulu, Kana mau nitip apa? Biar nanti aku bawain."
            show kana_side at left with dissolve
            kana "Eh kalo [mcname] gimana?"
            hide kana_side at left with dissolve
            mcname "Kamu duluan aja, gapapa."
            "[mcname] mengatakan hal tersebut karena tidak ingin membuat Kana menunggu terlalu lama."
            show kana_side at left with dissolve
            kana "Oke deh, kalau gitu aku roti strawberry ya."
            hide kana_side at left with dissolve
            mcname "Siapppp~"
            "Setelah mengatakan hal tersebut, Kana akhirnya pergi duluan ke rooftop."
            "[mcname] pun berjalan menuju ke kantin."
            stop music fadeout 1.0
            $ quick_menu = False
            scene black with dissolve
            play music "audio/bgm_kantin.mp3" fadein 1.0
            scene kantin with dissolve
            $ renpy.block_rollback()
            $ quick_menu = True
            play sound "audio/crowd_noise.mp3" fadein 1.0
            mcname "Hmmm, sebaiknya aku pesen dulu yang dipesen Kana."
            "[mcname] kemudian berjalan menuju kasir."
            "Di sana, [mcname] mendengarkan beberapa mahasiswa membicarakan tentang event kampus yang akan segera diadakan."
            "Mahasiswa A" "Eh, katanya event kampus nanti bakal ada lomba-lomba pertunjukan."   
            "Mahasiswa B" "Serius? Emang ada hadiahnya?"
            "Mahasiswa A" "Buat hadiahnya kurang tahu sih."
            "Mahasiswa A ""Tapi guest starnya nanti katanya sih Sabi Yoi."
            "Mahasiswa B" "Duh Sabi Yoi, agak bosen sih dengernya tapi gapapa lah."
            mcname "Heee menarik juga itu..."
            jump chapter2kanaA
    #*Skip Scene*
    #*BG Rooftop*
label chapter2kanaA:
    stop sound fadeout 1.0
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Rooftop Siang.ogg" fadein 1.0 volume 2.0
    scene rooftop with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    "Selangkah demi selangkah, [mcname] menanjaki anak tangga menuju rooftop."
    "Di tangannya ada 2 roti untuk menemani mereka saat mengerjakan tugas nanti." 
    "Saat sampai di sana, terlihat Kana sudah menunggu [mcname]."
    "Menyadari keberadaan [mcname], Kana memanggil [mcname] sambil tersenyum."
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    kana "Ah [mcname]."
    hide kana_side at left with dissolve
    mcname "Maaf ya, bikin nunggu."
    show kana_side at left with dissolve
    kana "Gapapa kok. Makasih ya udah beliin roti."
    hide kana_side at left with dissolve
    "[mcname] dan Kana kemudian makan bersama sambil mengerjakan tugas. Sesekali terdengar canda tawa kecil di pembicaraan mereka."
    $ quick_menu = False
    scene black with dissolve
    scene rooftop with dissolve
    show kana at char_center with dissolve
    $ quick_menu = True    
    mcname "Fuuu kayaknya kita istirahat dulu sebentar, soalnya sudah lumayan lama ngerjain tugas."
    show kana_side at left with dissolve
    kana "Iya nih, udah lumayan mumet juga."
    hide kana_side at left with dissolve
    mcname "Oh iya, denger-denger katanya kampus kita bakal ada event buat ulang tahun kampus nanti."
    show kana_side at left with dissolve
    kana "Ehhh serius? Gak sabar jadinya, hehe."
    hide kana_side at left with dissolve
    "Kana terlihat sangat bersemangat, seperti sangat menantikan hal tersebut."
    mcname "Kayaknya kamu suka ya sama event-event kayak gitu."
    mcname "Sering ke event?"
    show kana_side at left with dissolve
    kana "E-eh??!"
    hide kana_side at left with dissolve
    "Kana agak terkejut."
    show kana_side at left with dissolve
    kana "E-enggak..."
    kana "Soalnya kan dulu waktu aku kecil sering sakit, pas ada acara-acara kayak gitu aku gak bisa ikut dan cuma di rumah aja..."
    kana "Jadi pas ada event-event begitu, aku suka sama suasananya yang meriah gitu."
    hide kana_side at left with dissolve
    mcname "Heeeee~"
    mcname "{i}Iya sih, Kana waktu dulu sering sakit ya.{/i}"
    mcname "Moga aja eventnya nanti berjalan lancar."
    show kana_side at left with dissolve
    kana "Iya, hehe."
    hide kana_side at left with dissolve
    mcname "Okee! Lanjut nugaas~"
    "Kana dan [mcname] kembali mengerjakan tugas."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Rooftop Siang.ogg" fadein 1.0 volume 2.0
    #Harusnya BGM Rooftop Sore
    scene rooftop with dissolve
    #Harusnya BG Rooftop Sore
    $ quick_menu = True
    "Tak terasa waktu telah menjadi sore."
    show kana at char_center with dissolve
    mcname "Gimana Kana? Udah beres?"
    show kana_side at left with dissolve
    kana "Udaah. Thank you udah mau ngerjain tugas bareng."
    hide kana_side at left with dissolve
    mcname "Anytime, Kana."
    show kana_side at left with dissolve
    kana "Oke, aku pulang dulu ya. Dadahh."
    hide kana_side at left with dissolve
    mcname "Daah~"
    "Kana dan [mcname] pulang ke rumah masing-masing."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}KEESOKAN HARINYA{/color}" with Pause(2.0)
    play music "audio/BGM_Kampus.mp3" fadein 1.0
    scene depan kampus with dissolve
    #$ renpy.block_rollback()
    $ quick_menu = True
    play sound "audio/crowd_noise.mp3" fadein 1.0
    "Suasana jalan di kampus lebih terasa lebih ramai daripada biasanya."
    "Banyak orang-orang yang sedang lalu lalang dan menyerahkan beberapa flyer yang entah isinya apa."
    "Bahkan ada yang memaksa beberapa mahasiswa/i untuk menerima flyer tersebut."
    show kana at char_center with dissolve
    mcname "Ehh, hari ini kok ramai banget ya? Ga kaya biasanya, lagi ada acara kah?"
    show kana_side at left with dissolve
    kana "Wah aku juga ga tauu. Event kampus yang kamu bilang kemarin masih lama, kan?"
    hide kana_side at left with dissolve
    mcname "Harusnya sih iya. Yaudah, kita ke kelas yuk."
    show kana_side at left with dissolve
    kana "Okee."
    hide kana_side at left with dissolve
    stop sound fadeout 1.0
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Lorong.mp3" fadein 1.0
    scene lorong with dissolve
    $ quick_menu = True
    "Saat Kana dan [mcname] berjalan bersama menuju kelas, tiba-tiba seseorang datang mendekat." 
    #MUNCUL SPRITE TONO
    show tana at char_center with dissolve
    show tana_side at left with dissolve
    tana "Ehhhh brooo bentarr duluuu!!"
    hide tana_side at left with dissolve
    "Terlihat seorang cewek tinggi dengan perawakan tomboy berambut pendek merah yang mengingatkan [mcname] kepada CABE KERING yang sering mamanya jemur di desa."
    "Kana dan [mcname] merasa bingung karena tiba-tiba dihentikan cewek tersebut." 
    "Seperti sadar dengan orang tersebut, tiba-tiba Kana bersembunyi di belakang [mcname] sambil mencoba menghindar dari tatapan cewek itu." 
    mcname "Uumm kenapa ya, Kak?"
    show tana_side at left with dissolve
    tana "Bentar dah, kayaknya gue pernah liat lu di event-event dah."
    hide tana_side at left with dissolve
    mcname "Gue?" 
    "Sambil terheran heran, [mcname] menunjuk dirinya sendiri dan bertanya apakah dia adalah orang yang cewek itu maksud."
    show tana_side at left with dissolve
    tana "Ahhhh bukan kocak, dia loh."
    hide tana_side at left with dissolve
    "Jari cewek itu menunjuk ke arah belakang [mcname]."
    "Saat itu pun Kana mulai gelisah dan menundukkan kepalanya, mencoba menyembunyikan wajahnya dari cewek tersebut."
    mcname "Hah? Kana?"
    hide tana at char_center with dissolve
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    kana "Ehh... Uuu k-kenapa ya Mba?"
    hide kana_side at left with dissolve
    hide kana at char_center with dissolve
    "Dengan ragu dan perlahan, Kana pun melihat ke arah cewek itu."
    show tana at char_center with dissolve
    show tana_side at left with dissolve
    tana "Nahhhh kan, benerrr feeling gue tuh. Elu kan yang sering dateng ke event jejepangan."
    hide tana_side at left with dissolve
    hide tana at char_center with dissolve
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    kana "Ehhh, s-salah orang kali. Hahaha."
    hide kana_side at left with dissolve
    hide kana at char_center with dissolve
    show tana at char_center with dissolve
    show tana_side at left with dissolve
    tana "Aahh, ga pernah salah kalau gue mah kocak. Tiap gue ke event jejepangan, keknya selalu ngeliat lu."
    hide tana_side at left with dissolve
    hide tana at char_center with dissolve
    mcname "Eh? Kamu sering ke event jejepangan, Kana?"
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    kana "Haa... masa sih? A-aku ga pernah ikut kaya gituan kok... Aku kan bukan wibu."
    hide kana_side at left with dissolve
    hide kana at char_center with dissolve
    show tana at char_center with dissolve
    show tana_side at left with dissolve
    tana "Ah masa sih? Kamu kan yang biasanya wotagei paling semangat di event-event jejepangan."
    hide tana_side at left with dissolve
    hide tana at char_center with dissolve
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    kana "Ah eh ah eh..."
    hide kana_side at left with dissolve
    hide kana at char_center with dissolve
    play sound "audio/run.mp3"
    "Kana pun kabur secepat mungkin, tidak peduli dengan orang yang ada di sekitar."
    show tana at char_center with dissolve
    show tana_side at left with dissolve
    tana "Lah, itu orang napa malah kabur dah. Ya udah ini buat lu aja."
    hide tana_side at left with dissolve
    "Cewek tersebut memberikan flyer ke arah [mcname] dan pergi dari tempat tersebut."
    mcname "??????? Ada apa ini????!!!!"
    mcname "Ah yaudah lah. Fokus kelas dulu."
    stop sound fadeout 1.0
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}SETELAH KELAS{/color}" with Pause(2.0)
    play music "audio/BGM_Lorong.mp3" fadein 1.0
    scene lorong sore with dissolve
    $ quick_menu = True
    "Setelah kelas selesai, [mcname] berjalan menuju ke luar kelas."
    "Tingkah laku Kana tadi pagi masih menjadi tanda tanya yang besar di dalam pikiran [mcname]. Hal ini membuat [mcname] tidak fokus dengan kelas dan melamun sendiri."
    mcname "{i}Hmmmmm…. Kana ke mana, ya? Padahal tadi pagi ada… Apa jangan-jangan karena kejadian tadi pagi?{/i}"
    "Saat memikirkan kejadian pagi tadi, tiba-tiba ada seseorang yang membuyarkan pikirannya."
    show freya at char_center with dissolve
    show freya_side at left with dissolve
    "???" "Eh ngapain [mcname], dari tadi asik sendiri."
    hide freya_side at left with dissolve
    $ quick_menu = False
    scene black with dissolve
    scene lorong sore with dissolve
    show freya at char_center with dissolve
    $ quick_menu = True
    #SHOW SPRITE FREYA
    mcname "Ah? Freya?"
    show freya_side at left with dissolve
    freya "Iya. Btw Kana mana? Tadi pagi kan harusnya bareng kamu."
    hide freya_side at left with dissolve
    mcname "Iya tadi pagi barengan. Tapi Kana tiba-tiba kabur sesudah dikasih flyer ini."
    "[mcname] kemudian menunjukkan flyernya kepada Freya."
    show freya_side at left with dissolve
    freya "............."
    hide freya_side at left with dissolve
    "Freya membaca flyer yang diberikan [mcname]."
    mcname "Denger-denger, emangnya Kana wibu?"
    show freya_side at left with dissolve
    freya "Heeee? Aku kira Naya udah cerita."
    hide freya_side at left with dissolve
    mcname "Emang cerita apa?"
    show freya_side at left with dissolve
    freya "Hmmm..."
    freya "Ga jadi deh."
    hide freya_side at left with dissolve
    "Seolah tidak ingin membahasnya Freya menghentikan topik tersebut."
    "[mcname] semakin kebingungan dengan semua kejadian hari ini."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Kosan 1.mp3" fadein 1.0
    scene kamar mc kota with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    "Malamnya setelah pulang dari kampus, [mcname] langsung merebahkan diri di kasurnya tanpa berganti pakaian."
    mcname "Haaaahhhhh..."
    mcname "{i}Hari ini terasa sangat panjang.{/i}"
    mcname "{i}Hmmm Kana ke mana yah?{/i}"
    "Kepikiran tentang Kana yang tidak masuk kelas hari ini, akhirnya [mcname] mencoba menghubungi Kana lewat chat."
    mcname "{i}Chat ah.{/i}"
    "[mcname] kemudian membuka HPnya."
    $ quick_menu = False
    nvl clear
    #Mobile Phone
    mc_nvl "Kana, kamu gapapa?"
    #(......)
    "Tidak ada respon dari Kana."
    mc_nvl "{image=mengsedih.png}"
    $ quick_menu=True
    mcname "Hmmm gak dibales."
    #*Balik BG Kamar*
    mcname "Semoga besok pagi Kana masuk ke kampus deh."
    "Setelah itu [mcname] menutup matanya dan langsung tidur"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}KEESOKAN HARINYA{/color}" with Pause(2.0)
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    scene kelas with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    play sound "audio/crowd_noise.mp3" fadein 1.0
    "Pagi itu kelas terlihat ramai oleh mahasiswa/i, namun Kanaia Asa tidak terlihat di mana pun."
    mcname "{i}Kayaknya hari ini Kana gak masuk juga ya.{/i}"
    "[mcname] mencoba melihat sekitar namun tetap saja hasilnya nihil."
    mcname "{i}Mungkin aku coba tanyakan ke Freya nanti.{/i}"
    stop sound fadeout 1.0
    "Pintu terbuka dan terlihat dosen memasuki kelas."
    stop music fadeout 1.0
    $ quick_menu = False
    play music "audio/BGM_Dosen + Rektor.mp3" fadein 1.0
    scene kelas with dissolve
    show dosen at dosen_center with dissolve
    show dosen_side at left with dissolve
    $ quick_menu = True
    dosen "Baiklah anak-anak mari kita mulai kelas hari ini."
    hide dosen_side at left with dissolve
    #*Skip Scene*
    #Transisi Putih
    $ quick_menu = False
    scene black with dissolve
    scene kelas with dissolve
    show dosen at dosen_center with dissolve
    show dosen_side at left with dissolve
    $ quick_menu = True
    dosen "Oke terima kasih untuk hari ini, jangan lupa untuk selalu jaga kesehatan ya."
    hide dosen_side at left with dissolve
    hide dosen with dissolve
    "Bu Dosen pun beranjak pergi dari kelas."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    scene kelas with dissolve
    $ quick_menu = True
    mcname "{i}Oke Bu Dosen sudah keluar.{/i}"
    mcname "{i}Mungkin aku coba tanyakan ke Freya tentang masalah Kana.{/i}"
    "[mcname] pun kemudian berjalan mendekati Freya."
    $ quick_menu = False
    scene black with dissolve
    scene kelas with dissolve
    show freya at char_center with dissolve
    $ quick_menu = True
    mcname "Freya kamu tau gak Kana gimana?"
    mcname "Soalnya udah dua hari ini gak masuk kelas, aku chat juga gak dibales."
    show freya_side at left with dissolve
    freya "Iya nih, aku juga gak dikabarin sama dia."
    hide freya_side at left with dissolve
    mcname "Duh jadi gimana ya ini? Aku agak khawatir."
    show freya_side at left with dissolve
    freya "Mungkin nanti aku coba datengin ke rumahnya nih, kali aja dia kenapa-napa."
    hide freya_side at left with dissolve
    mcname "Oke deh Freya, tolong banget ya."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Kampus.mp3" fadein 1.0
    scene depan kampus with dissolve
    $ quick_menu = True
    mcname "{i}Duh kata Freya nanti dia bakal ke rumah Kana buat mastiin kabar Kana...{/i}"
    mcname "{i}Tapi tetep aja aku gak bisa berhenti kepikiran tentang Kana.{/i}"
    mcname "Haaaahh..."
    mcname "{i}Mungkin ku coba nenangin diri dulu sambil jalan-jalan sebelum balik ke kost.{/i}"
    #*Skip Scene*
    #BG MALL
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Mall Slow.mp3" fadein 1.0
    scene mall temp with dissolve
    $ quick_menu = True
    "Karena bingung mau ke mana, akhirnya [mcname] ke mall yang pernah dia datangi bersama Kana dulu."
    mcname "{i}Duh niatnya pengen nenangin diri tapi ujung-ujungnya malah ke sini.{/i}"
    mcname "Yah tapi cuma di sini sih, tempat yang aku tau di Jakarta."
    "[mcname] kemudian berkeliling melihat-lihat di mall."
    $ quick_menu = False
    scene black with dissolve
    with Pause (2.0)
    scene mall temp with dissolve
    $ quick_menu = True
    mcname "Eh itu kan?"
    "Saat berkeliling, [mcname] melewati toko baju yang pernah dia lewati waktu bersama Kana."
    mcname "Kalo gak salah, waktu itu Kana ngeliatin baju ini lumayan lama ya.."
    #*Flashback pas ngeliat baju di toko
    mcname "Oke lah."
    #*SFX bunyi masuk toko"
    mcname "Permisii~"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}KEESOKAN HARINYA{/color}" with Pause(2.0)
    play music "audio/BGM_Dosen + Rektor.mp3" fadein 1.0
    scene kelas with dissolve
    $ quick_menu = True
    "Paginya di kampus saat Bu Dosen sedang menjelaskan kuliah..."
    show dosen at dosen_center with dissolve
    show dosen_side at left with dissolve
    dosen "Sepertinya beberapa hari ini Kana absen terus ya?"
    hide dosen_side at left with dissolve
    "Mendengar Bu Dosen mengatakan nama Kana, [mcname] pun sedikit terkejut."
    show dosen_side at left with dissolve
    dosen "Tadi saya sudah dapat informasi dari orang tuanya Kana, kalau Kana izin sakit jadi tidak bisa masuk."
    hide dosen_side at left with dissolve
    hide dosen with dissolve
    mcname "{i}Hah? Kana sakit?{/i}"
    mcname "Ku coba tanyain langsung ke Freya dah, kan dia habis dari rumah Kana kemarin."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}SETELAH KELAS{/color}" with Pause(2.0)
    play music "audio/BGM_Lorong.mp3" fadein 1.0
    scene lorong with dissolve
    show freya at char_center with dissolve
    $ quick_menu = True
    mcname "Freya, emang bener kalau Kana lagi sakit?"
    "Setelah kelas berakhir, [mcname] langsung mendekati Freya yang membuatnya agak terkejut."
    show freya_side at left with dissolve
    freya "Ah [mcname]?"
    freya "Ah masalah itu ya..."
    freya "Mungkin kamu udah tau duluan, tapi Kana itu dulu tubuhnya lemah."
    freya "Jadi gak bisa ngelakuin hal-hal normal yang kayak orang lain."
    freya "Akhirnya dia sering ngehabisin waktunya dirumah, ngewibu."
    freya "Dan mungkin karena hal tesebut, jadinya dia dijauhin temen sekelasnya waktu masih sekolah."
    freya "Sampai akhirnya dia balik nenutup diri di kamarnya terus."
    freya "Aku gak begitu tau gimana cerita dia sepenuhnya, soalnya waktu itu aku juga lagi ikut orang tuaku karena kerjaan di luar kota."
    freya "Untung aja waktu aku kembali ke sini, Kana jadi mulai membuka diri lagi dan mencoba kembali bersosialisasi."
    freya "Tapi entah kenapa sekarang dia malah kembali menjadi seperti dulu."
    hide freya_side at left with dissolve
    "Setelah memberikan ringkasan tentang masalalu Kana, Freya pun menatap [mcname]."
    show freya_side at left with dissolve
    freya "Oleh karena itu [mcname], tolong."
    hide freya_side at left with dissolve
    "Freya menepuk kedua tangannya seperti memohon."
    show freya_side at left with dissolve
    freya "Aku gak pengen Kana balik seperti dulu yang menutup dirinya lagi."
    freya "Jadi bisa gak kalo kamu bujuk dia buat kembali..."
    hide freya_side at left with dissolve
    mcname "Eh aku??"
    "[mcname] bingung kenapa Freya minta tolong padanya."
    mcname "Bukannya kamu ya, temen deketnya Kana dari dulu?"
    show freya_side at left with dissolve
    freya "Soalnya kemarin waktu aku ke sana, aku gak dibolehin masuk sama Naya."
    freya "Jadi aku rasa mungkin cuma kamu yang bisa."
    freya "Apalagi beberapa hari ini kalian berdua deket banget, jadi aku yakin pasti berhasil."
    hide freya_side at left with dissolve
    "[mcname] sedikit malu karena dibilang dekat dengan Kana."
    "Tapi kemudian menggeleng-gelengkan kepalanya untuk kembali fokus."
    mcname "Oke deh bakal ku coba."
    "Kata [mcname] setelah memantapkan dirinya."
    show freya_side at left with dissolve
    freya "Makasih banyak [mcname]."
    hide freya_side at left with dissolve
    "Freya tersenyum senang dengan jawaban [mcname]."
    show freya_side at left with dissolve
    freya "Ini alamatnya Naya, ya."
    freya "Good luck~"
    hide freya_side at left with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}SETELAH KELAS{/color}" with Pause(2.0)
    play music "audio/BGM_MC Pertama Kali ke JKT + BG Pagi.mp3" fadein 1.0
    scene awan with dissolve
    $ quick_menu = True
    "[mcname] kemudian menuju ke rumah Kana."
    mcname "Uhhh,, belok kanan di sebelah sini."
    "Itu perjalanan yang bisa dibilang cukup jauh dari stasiun kereta yang sering [mcname] pakai."
    "Komplek perumahan yang dituju [mcname] katanya dikenal dengan perumahan yang cukup mewah."
    mcname "Jadi ini rumah Kana."
    "Di sana terlihat rumah yang cukup mewah, bahkan lebih besar dari rumah [mcname] di kampung."
    #ASSET PINTU RUMAH KANA
    mcname "Kalau gak salah, pernah denger kalo Kana itu orang kaya."
    mcname "Tapi gak nyangka bakal sebesar ini."
    play sound "audio/ding.mp3"
    "[mcname] pun kemudian mencoba membunyikan bel yang ada di dekat pintu."
    "Tidak lama setelah bel berbunyi, terdengar suara langkah kaki menuju pintu depan."
    $ quick_menu = False
    scene black with dissolve
    scene awan with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    "????" "Iya cari siapa yaa???"
    "Terlihat seorang wanita cantik yang membukakan pintu."
    "Wanita tersebut terlihat cukup muda, terlihat mungkin sekitar 20 tahunan."
    mcname "{i}Sepertinya dia kakaknya Kana.{/i}"
    mcname "Saya [mcname], teman sekampusnya Kana."
    "[mcname] kemudian memperkenalkan diri kepada wanita tersebut."
    mcname "Saya mau menjenguk Kana karena katanya lagi sakit."
    "Kakak Kana(?)" "Ahhh [mcname]? Kana sering banget nyeritain tentang kamu, hahaha."
    "Kakak Kana(?)" "Ayo sini masuk dulu."
    mcname "Makasih banyak Kak."
    "Kakak Kana(?)" "Loh kok \"Kak\"?"
    mcname "Eh??"
    mcname "Kakaknya Kana kan?"
    "[mcname] bingung takut membuat wanita itu tersinggung."
    "Mamah Kana" "Eehhh? Emang saya terlihat semuda itu ya? Saya mamahnya Kana, haha."
    mcname "Eh maaf tante, saya kira kakaknya Kana soalnya keliatan masih muda."
    "Mamah Kana" "Fufufu bisa aja kamu. Yaudah, sini masuk dulu."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Lorong.mp3" fadein 1.0
    #HARUSNYA BGM RUANG TAMU RUMAH KANA
    scene lorong with dissolve
    #HARUSNYA BG RUANG TAMU RUMAH KANA
    $ quick_menu = True
    "Di ruang tamu, Mamah Kana bercerita tentang bagaimana keadaan Kana yang sampai sekarang tidak mau keluar kamar."
    $ quick_menu = False
    scene black with dissolve
    scene lorong with dissolve
    #HARUSNYA BG RUANG TAMU RUMAH KANA
    $ quick_menu = True
    #MUNCUL SPRITE PINTU KAMAR KANA
    "Setelah berbincang, [mcname] akhirnya berada di depan pintu Kamar Kana."
    "[mcname] berhenti sebentar, memikirkan cara untuk membujuk Kana."
    "Tetapi kemudian menggelengkan kepala."
    mcname "{i}Ah, kebanyakan mikir juga ga ngubah keadaan.{/i}"
    mcname "Yosh."
    #*SFX ketok pintu*
    mcname "Kanaaa, kamu di sana??"
    "[mcname] menunggu respon dari Kana."
    "Seperti yang diduga, tidak ada jawaban dari Kana."
    "Namun menurut perkataan Mamahnya, Kana mengurung diri di dalam kamarnya selama beberapa hari ini."
    menu:
        "Yang kamu lakukan..."
        "STOP DI SINI.":
            mcname "{i}Sepertinya Kana tidak bisa ku ganggu.{/i}"
            mcname "{i}Mungkin kubiarkan aja dulu.{/i}"
            $ quick_menu = False
            stop music fadeout 1.0
            scene black with dissolve
            show text "{color=#FFF}*AKHIRNYA KAMU MUNDUR DARI KAMARNYA KANA DAN MEMILIH UNTUK MENDEKATI MAMAHNYA*{/color}" with Pause(2.0)
            show text "{color=#FF0000}BAD END(?)\nWIN FOR SOME{/color}"
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits
        "\"BUKA PINTU.\"":
            mcname "Kana... Aku masuk ke kamar, ya."
            mcname "Kalau kamu gak suka, nanti ngomong aja ya."
            "[mcname] kemudian meraih gagang pintu kamarnya Kana."
            "[mcname] rasa jika dia berhenti sekarang, maka Kana akan mengurung dirinya lebih lama."
            #SFX BUKA PINTU
            "Pintu kamarnya tidak di kunci."
            "[mcname] tahu itu karena sudah diberitahu oleh Mamahnya Kana."
            "Saat [mcname] memasuki kamar lalu menutup pintu, terasa kegelapan menyelimuti kamar itu."
            jump chapter2kanaB

label chapter2kanaB:
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Lorong.mp3" fadein 1.0
    #HARUSNYA BGM KAMAR KANA
    scene kamar kana with dissolve
    #HARUSNYA BG KAMAR KANA
    $ quick_menu = True
    "Dari balik tirai jendela, terlihat sedikit cahaya yang muncul, membantu mata [mcname] menyesuaikan dengan kegelapan yang pekat."
    "Kamarnya Kana terasa berbeda, mengeluarkan aroma khas yang mencerminkan kepribadiannya. Entah kenapa tercium aroma lautan yang segar."
    "Saat [mcname] mencoba memperhatikan sekitar, terdengar suara memanggil namanya."
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    kana "[mcname]..."
    hide kana_side at left with dissolve
    mcname "Huh, jangan-jangan yang di dalam selimut itu kamu, Kana?"
    show kana_side at left with dissolve
    kana "Umnnn..."
    hide kana_side at left with dissolve
    mcname "......."
    mcname "Aku buka tirainya ya. Mungkin kamu lebih nyaman dalam gelap, tapi sedikit cahaya juga bagus buat kamu."
    show kana_side at left with dissolve
    kana "Mmmmm... iya."
    hide kana_side at left with dissolve
    #Transisi kebuka tirai nya, dari hitam ke putih
    #*CG KANA nanti kalo sempat bikin*
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    #HARUSNYA BGM KAMAR KANA
    scene kamar kana with dissolve
    #HARUSNYA BG KAMAR KANA
    $ quick_menu = True
    "Kana terlihat duduk di ranjang, menyelimuti dirinya dengan selimut sambil memeluk kakinya."
    "Kana terlihat sedikit gemetar, seperti anak yang sedang menunggu orang tuanya pulang ke rumah."
    show kana at char_center with dissolve
    mcname "Kana, kamu gapapa? Katanya sakit."
    show kana_side at left with dissolve
    kana "Umnn."
    hide kana_side at left with dissolve
    "[mcname] kemudian mengambil kursi dan mendekatkan kursi tersebut ke kasur Kana."
    mcname "Aku duduk ya."
    "Tanpa menunggu respon dari Kana, [mcname] langsung duduk di kursi tersebut."
    mcname ".........."
    show kana_side at left with dissolve
    kana ".............."
    hide kana_side at left with dissolve
    mcname "Kamu gapapa?"
    show kana_side at left with dissolve
    kana "............"
    hide kana_side at left with dissolve
    mcname "............"
    show kana_side at left with dissolve
    kana "Kok kamu ke sini? Pasti dikasih tau Freya, ya?"
    hide kana_side at left with dissolve
    mcname "Aku khawatir sama kamu, Kana. Soalnya kamu udah gak masuk kuliah berhari hari."
    show kana_side at left with dissolve
    kana "........"
    kana "Kok kamu khawatir sama aku? Kamu gapapa ke sini?"
    hide kana_side at left with dissolve
    mcname "Eh? Kenapa kamu ngomong begitu?"
    show kana_side at left with dissolve
    kana "Aku ga mau waktumu yang berharga dihabisin kayak gini."
    hide kana_side at left with dissolve
    mcname "Nggak kok, kamu lebih berharga dari waktuku."
    show kana_side at left with dissolve
    kana "Eh? Aku pikir..."
    hide kana_side at left with dissolve
    "Kana berusaha melanjutkan kalimatnya, namun sepertinya tertahan di ujung lidah."
    "Melihat hal tersebut, akhinya [mcname] mencoba memulai percakapan lagi."
    mcname "Kana, akhir-akhir ini aku ngerasa kamu menutup diri."
    mcname "Aku ga tau kalo aku ada salah apa atau gimana, tapi..."
    mcname "Maaf, ya Kana. Apa pun itu, aku gak bermaksud."
    hide kana at char_center with dissolve
    show kana_scared at char_center with dissolve
    show kana_side_scared at left with dissolve
    kana "Eh nggak kok. B-bukan salahmu."
    kana ".........."
    kana "J-jangan benci aku ya."
    kana "T-tapi…"
    kana "S-sebenarnya aku takut..."
    kana "Aku takut kalau kamu bakal ngejauhin aku, gara-gara aku wibu."
    kana "Pasti kamu ngerasa aneh kan, dengan sifat ku ini?"
    hide kana_side_scared at left with dissolve
    "Kana mengatakan hal tersebut sambil gemetar, matanya terlihat berkaca-kaca menahan air mata."
    "[mcname] yang melihat hal tersebut hanya bisa terdiam."
    mcname "Aku tidak merasa seperti itu kok, Kana."
    hide kana_scared at char_center with dissolve
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    kana "Eh??"
    hide kana_side at left with dissolve
    mcname "Aku ga tahu kenapa kamu bilang gitu."
    mcname "Tapi aku ga berpikiran begitu kok."
    show kana_side at left with dissolve
    kana "T-Tapi kan, waktu itu kamu bilang kamu ngerasa aneh sama orang yang suka jejepangan."
    hide kana_side at left with dissolve
    mcname "Ahhh, masalah ganci kemaren? Waktu itu keinget papahku."
    show kana_side at left with dissolve
    kana "Eh?"
    hide kana_side at left with dissolve
    mcname "Iyaa. Papahku juga wibu, bahkan bisa dibilang garis keras."
    mcname "Jadinya, aku sering teringat papahku kalo lagi ngomongin wibu. Padahal aku gak berpikir seperti itu kok."
    show kana_side at left with dissolve
    kana "J- Jadi kamu ga benci sama aku?"
    hide kana_side at left with dissolve
    mcname "Seperti yang kubilang, nggak kok."
    "[mcname] menatap Kana sambil tersenyum dengan tatapan hangat."
    mcname "Aku khawatir sama kamu, Kana."
    mcname "Kamu udah gak masuk kuliah berhari-hari."
    show kana_side at left with dissolve
    kana "Maaf ya, [mcname]..."
    hide kana_side at left with dissolve
    mcname "Yang penting kamu baik-baik aja."
    mcname "Aku ga mau kehilangan kamu."
    show kana_side at left with dissolve
    kana "[mcname]..."
    hide kana_side at left with dissolve
    mcname "Pokoknya kalau ada apa-apa, tolong ingat bahwa aku akan selalu ada. Jangan pendam semuanya sendiri, aku pasti siap mendengarkan."
    show kana_side at left with dissolve
    kana "......."
    hide kana_side at left with dissolve
    mcname "........."
    "[mcname] kemudian mengambil gelas yang ada di meja sebelah kasur lalu memberikannya ke Kana."
    show kana_side at left with dissolve
    kana "Makasih [mcname]..."
    hide kana_side at left with dissolve
    "[mcname] menganggukkan kepalanya sambil tersenyum."
    show kana_side at left with dissolve
    kana "*Glug glug*"
    kana "....."
    kana "*Sigh*"
    kana "[mcname]..."
    kana "Aku mau cerita."
    kana "Aku ga tau mau mulai dari mana..."
    hide kana_side at left with dissolve
    "[mcname] kemudian diam untuk memfokuskan diri ke cerita Kana."
    #*Transisi ke BG Langit*
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Lorong.mp3" fadein 1.0
    #HARUSNYA BGM KAMAR KANA
    scene kamar kana with dissolve
    #HARUSNYA BG KAMAR KANA
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    $ quick_menu = True
    kana "Seperti yang kamu tau, pas kecil aku punya tubuh yang lemah."
    kana "Aku tidak bisa melakukan banyak hal yang sering dilakukan anak-anak pada umumnya, jadinya aku cuma bisa di rumah aja"
    kana "Walaupun begitu papah mamahku tetep sayang sama aku"
    kana "Tapi, mereka juga perlu ngurus pekerjaan mereka. Jadinya aku lebih banyak menghabiskan waktu sendirian di kamar."
    kana "Sesekali Freya datang untuk bermain denganku."
    kana "Waktu itu, aku seneeeeeng banget."
    kana "Tapi..."
    kana "Suatu hari, Freya harus ikut orang tuanya yang tugas di luar kota."
    kana "................"
    kana "Akhirnya aku sendirian lagi."
    kana "Di tengah kesepian itu, aku menemukan yang namanya anime."
    kana "Anime itu membuat aku melihat dunia dengan cara yang berbeda"
    kana "Mulai dari anime, aku pun mulai mencari-cari juga hal yang berbau jejepangan"
    kana "Hal-hal itulah yang menjadi pelarianku di kamar yang penuh kesendirian."
    kana "Tak terasa waktu berlalu, aku pun harus masuk yang namanya sekolah."
    kana "Setelah sekian lama, di sana lah aku mulai mencoba berinteraksi lagi dengan orang lain."
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
    kana "Setahun pun berlalu, kemudian dua, tak terasa aku sudah di kelas 3."
    kana "Waktu itu, ternyata Freya kembali setelah mengikuti orang tuanya kerja di luar kota."
    kana "Tentu saja mendengar hal tersebut membuatku senang, namun karena bertahun tahun tidak berinteraksi dengan orang lain, aku tidak tahu harus gimana pas ketemu dia lagi."
    kana "Mungkin karena mendengar bagaimana keadaan ku, Freya kaget dan mencoba untuk mengajakku kembali masuk sekolah."
    kana "Awalnya aku enggan, namun karena desakan terus menerus dari Freya, akhirnya aku kembali mencoba untuk kembali bersekolah."
    kana "Pada saat kembali ke sekolah, entah kenapa tatapan orang-orang terasa berbeda dari biasanya, mungkin karena waktu itu aku bersama Freya."
    kana "Kali ini pun orang di kelas mulai mencoba mengajakku berbicara lagi. Aku gugup dan takut, tapi Freya membantuku menjawab mereka."
    kana "Entah kenapa mereka mulai menganggapku seperti tuan putri yang lemah lembut dengan bodyguardnya."
    kana "Mungkin karena itu, akhirnya pandangan mereka kepadaku berbeda dari sebelumnya."
    kana "Takut menghancurkan pandangan mereka, mulai saat itu aku mencoba memerankan role tersebut."
    kana "Berpura-pura seperti itu pun gapapa, setidaknya aku bisa berinteraksi dengan yang lain dan kembali mempunyai makna."
    kana "Tidak ada yang memuji ku sebelumnya karena mereka tidak menyukai diriku yang dulu."
    kana "Lagipula diriku yang wibu ini pun gak ada bagus-bagusnya, jadinya aku gapapa berpura-pura."
    kana "Yang kulakukan hanya mengikuti image mereka tentangku, dan menjadi orang yang membuat mereka senang"
    kana "Aku tetap menjalankan role ku tersebut, aku rasa itu sudah cukup dan ternyata memang benar."
    kana "Hari-hari pun berjalan dengan mulus..."
    kana "Setidaknya kebanyakan..."
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
    hide kana_side at left with dissolve
    mcname "............."
    show kana_side at left with dissolve
    kana "Jadi, itu ceritaku..."
    hide kana_side at left with dissolve
    "Setelah menceritakan ceritanya yang panjang tanpa diganggu, akhirnya Kana berhenti. Badannya gemetar, wajahnya terlihat lelah."
    show kana_side at left with dissolve
    kana "Aku memang orang aneh yang brainrot dan suka jejepangan."
    kana "Aku juga berusaha menjadi orang yang berbeda, membohongi orang-orang, agar mereka menyukaiku."
    kana "Jadi makasih ya, udah mau berteman sama aku."
    kana "Walaupun mungkin kamu terpaksa, aku sangat bersyukur kamu mau jadi temanku."
    hide kana_side at left with dissolve
    "[mcname] menggaruk kepalanya, bingung dan khawatir kata-kata yang akan dikeluarkan olehnya malah akan membuat luka yang semakin dalam di hati Kana."
    mcname "Aku ga bohong. Serius, temenan sama kamu itu hal yang sangat menyenangkan."
    show kana_side at left with dissolve
    kana "Benarkah??"
    hide kana_side at left with dissolve
    mcname "Aku gak bohong. Pokoknya berapa kali pun kamu nanya, aku bakal tetap bilang kalo aku juga seneng banget bisa jadi temanmu."
    #Narrator
    hide kana at char_center with dissolve
    show kana_shy at char_center with dissolve
    show kana_side_shy at left with dissolve
    kana "*Blush*"
    hide kana_side_shy at left with dissolve
    hide kana_shy at char_center with dissolve
    show kana at char_center with dissolve
    mcname "...."
    show kana_side at left with dissolve
    kana "Ini mimpi kah?"
    kana "Aku seneng banget denger kamu suka temenan sama aku."
    hide kana_side at left with dissolve
    "[mcname] menatap mata Kana sambil tersenyum."
    mcname "Kana, aku ga mau kamu merasa sendirian lagi. Aku gak nyaman kalo kamu jadi hikikomori."
    show kana_side at left with dissolve
    kana "Ga nyaman?? Kenapa?"
    hide kana_side at left with dissolve
    mcname "Karena aku juga menikmati waktu yang kita habiskan bersama."
    show kana_side at left with dissolve
    kana "Ummmm.."
    hide kana_side at left with dissolve
    "[mcname] kemudian memegang pundak Kana dan menatap langsung ke matanya."
    mcname "Kamu itu dirimu yang sekarang Kana, jangan biarkan masa lalu menahanmu."
    mcname "Apa yang sudah terjadi tidak bisa diubah."
    mcname "Saat ini kamu adalah kamu."
    "Setelah itu [mcname] melepaskan tangannya, Kana terlihat malu dan memalingkan kepala."
    "Setelah mencari kalimat yang pas, Kana kemudian menatap [mcname] sambil tersenyum."
    show kana_side at left with dissolve
    kana "Uhmmm terima kasih, aku senang kamu sudah mau menemaniku."
    kana "Dan [mcname], aku..."
    hide kana_side at left with dissolve
    "Kana mencoba mengatakan sesuatu, tapi akhirnya tidak jadi."
    show kana_side at left with dissolve
    kana "Mungkin ini agak memalukan, tapi besok aku bakal kembali lagi seperti biasanya."
    hide kana_side at left with dissolve
    "Kana tersenyum."
    mcname "Iyah, yang penting sekarang kamu istirahat dulu aja."
    "Karena merasa tugasnya sudah selesai, akhirnya [mcname] pun beranjak untuk keluar kamar."
    show kana_side at left with dissolve
    kana "Ah... oke."
    kana "Sampai jumpa besok, [mcname]."
    hide kana_side at left with dissolve
    "Entah kenapa senyumannya terasa sedikit sedih."
    mcname "Oke, sampai jumpa besok."
    #*transisi dari hitam ke putih*
    "[mcname] kemudian keluar dari kamar Kana."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Lorong.mp3" fadein 1.0
    #HARUSNYA BGM RUANG TAMU RUMAH KANA
    scene lorong malam with dissolve
    #HARUSNYA BG RUANG TAMU RUMAH KANA
    $ quick_menu = True
    "Melihat kejadian ini, [mcname] menjadi lebih mengenal Kanaia Asa dengan lebih dalam."
    mcname "Ya... ku rasa aku juga harus pulang."
    "Setelah memberikan terima kasih ke Mamahnya Kana, akhirnya [mcname] pulang ke kostnya."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}KEESOKAN HARINYA{/color}" with Pause(2.0)
    play music "audio/BGM_Kampus.mp3" fadein 1.0
    scene depan kampus with dissolve
    $ quick_menu = True
    "Pagi ini [mcname] merasa lebih ringan dari biasanya, mungkin karena hari ini seseorang yang dia tunggu akhirnya kembali berkuliah lagi."
    #*BG kelas*
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    scene kelas with dissolve
    $ renpy.block_rollback()
    show freya at char_center with dissolve
    show freya_side at left with dissolve
    $ quick_menu = True
    freya "Jadi [mcname], gimana keadaan kana?"
    hide freya_side at left with dissolve
    mcname "Dia udah mendingan dan juga katanya bakal masuk hari ini."
    show freya_side at left with dissolve
    freya "Syukurlah."
    freya "Eh btw [mcname], kamu ngapain jadi Kana mau balik lagi? Hehe."
    hide freya_side at left with dissolve
    "Freya menanyakan hal tersebut sambil nyengir."
    mcname "Eh?? Gak ngapa ngapain kok."
    mcname "Aku gak tau kamu berharap apa, tapi aku hanya ngelakuin apa yang ku bisa."
    show freya_side at left with dissolve
    freya "Heeeee......"
    hide freya_side at left with dissolve
    hide freya at char_center with dissolve
    play sound "audio/open_door.mp3"
    "Kana memasuki kelas saat Freya dan [mcname] sedang berbincang."
    "Dia tampak bersinar sama seperti biasanya."
    show kana at char_right with dissolve
    show freya at char_left with dissolve
    show kana_side at left with dissolve
    kana "Pagi [mcname]... Pagi juga Frey..."
    hide kana_side at left with dissolve
    mcname "Ah, pagi Kana."
    show freya_side at left with dissolve
    freya "Pagi juga Nay"
    freya "Gimana keadaanmu Nay? Udah mendingan?"
    hide freya_side at left with dissolve
    show kana_side at left with dissolve
    kana "Mhm... Udah mendingan kok Frey."
    hide kana_side at left with dissolve
    mcname "Ngomong-ngomong katanya UTS bentar lagi ya?"
    "[mcname] mencoba mencari topik pembicaraan lain, sepertinya untuk mencegah membahas hal yang kemarin."
    show freya_side at left with dissolve
    freya "Iya yah."
    hide freya_side at left with dissolve
    mcname "Kalo kamu UTS gimana Kana?"
    show kana_side at left with dissolve
    kana "Kalo aku bisa aja kok, kayaknya..."
    hide kana_side at left with dissolve
    "Kana mengambil beberapa detik untuk melanjutkan kalimatnya."
    show kana_side at left with dissolve
    kana "Agak takut soalnya aku sempat beberapa kali gak masuk."
    hide kana_side at left with dissolve
    mcname "Heee... Kalo ada yang bisa ku bantu bilang aja ya."
    show kana_side at left with dissolve
    kana "Iya, mohon bantuannya ya..."
    hide kana_side at left with dissolve
    #ARC 2
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}BEBERAPA HARI KEMUDIAN{/color}" with Pause(2.0)
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    scene kelas with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    play sound "audio/crowd_noise.mp3" fadein 1.0
    "Sudah seminggu sejak kejadian itu, semuanya kembali menjadi normal."
    "Suasana kelas ricuh seperti biasa karena dosen belum datang."
    "Tanpa sadar waktu pelajaran pun tiba, lalu terdengar suara pintu terbuka."
    stop sound fadeout 1.0
    stop music fadeout 1.0
    $ quick_menu=False
    scene black with dissolve
    play music "audio/BGM_Dosen + Rektor.mp3" fadein 1.0
    scene kelas with dissolve
    show dosen at dosen_center with dissolve
    show dosen_side at left with dissolve
    $ quick_menu=True
    dosen "Selamat pagi anak-anak, mata kuliah hari ini akan dimulai dengan--"
    hide dosen_side at left with dissolve
    hide dosen at dosen_center with dissolve
    "Mata kuliah telah dimulai dan kondisi kelas pun tiba-tiba menjadi hening. Di dalam keheningan tersebut ada yang tertidur pulas, ada yang bermain HP, dan ada yang mencatat."
    "[mcname] pun dengan serius mengikuti apa yang disampaikan oleh Dosen"
    "Saat [mcname] memperhatikan pelajaran, di ujung matanya terlihat Kana yang berkali kali menatapnya, seperti ingin mengatakan sesuatu."
    "Penasaran akan apa yang dilakukan gadis tersebut, akhirnya [mcname] menanyakannya secara langsung."
    show kana at char_center with dissolve
    mcname "Ada apa, Kana?"
    show kana_side at left with dissolve
    kana "G-gapapa kok."
    hide kana_side at left with dissolve
    mcname "......."
    hide kana at char_center with dissolve
    show kana_shy at char_center with dissolve
    "Wajah Kana sedikit memerah sambil mengalihkan pandangan ke Dosen. [mcname] bingung melihat kelakuan Kana, namun akhirnya kembali fokus ke pelajaran."
    hide kana_shy at char_center with dissolve
    $ quick_menu=False
    scene black with dissolve
    scene kelas with dissolve
    $ quick_menu=True
    "Tanpa terasa 50 menit telah berlalu dan dosen pun mengumumkan sesuatu yang terkait dengan UTS." 
    show dosen at dosen_center with dissolve
    show dosen_side at left with dissolve
    dosen "Baiklah mahasiswa/i jangan lupa minggu depan ada UTS dan ini adalah UTS pertama kalian. Saya harap kalian menjunjung tinggi kejujuran dan jangan lupa untuk belajar, sekian terima kasih."
    hide dosen_side at left with dissolve
    "Mahasiswa/i" "Terima kasih banyak Bu."
    stop music fadeout 1.0
    $ quick_menu=False
    scene black with dissolve
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    scene kelas with dissolve
    $ quick_menu=True
    "Setelah dosen meninggalkan ruangan, Kana memulai pembicaraan."
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    kana "Aduh gimana nih."
    kana "Aku gak terlalu ngedengerin dosen tadi, tau-tau udah bilang mau UTS."
    kana "Tapi harusnya bisa sih kalo belajar sambil review textbook, kayaknya??"
    hide kana_side at left with dissolve
    mcname "Hahaha sama."
    "[mcname] memberikan persetujuan."
    show kana_side at left with dissolve
    kana "Duh tolongin dong, [mcname]."
    kana "Bantuin aku belajar, soalnya kalo aku belajar sendiri bisa-bisa gak fokus."
    hide kana_side at left with dissolve
    mcname "Bisa sih, lagi pula kalo barengan bisa lebih mudah belajarnya."
    mcname "Kalo Freya gimana? Mau ikut belajar bareng nanti?"
    hide kana at char_center with dissolve
    show kana at char_right with dissolve
    show freya at char_left with dissolve
    "[mcname] mencoba mengajak Freya untuk belajar bersama."
    show freya_side at left with dissolve
    freya "Kalo aku kayaknya skip nih, soalnya aku kalo rame malah gak bisa fokus."
    freya "Lagian biar kalian bisa barengan, hehe."
    hide freya_side at left with dissolve
    show kana_side at left with dissolve
    kana "Ih apaan sih Freya."
    hide kana_side at left with dissolve
    show freya_side at left with dissolve
    freya "Hehe oke, aku duluan ya. Soalnya aku lagi ada yang dikerjain."
    hide freya_side at left with dissolve
    "Setelah menggoda Kana, Freya mencoba lari dari ruang kelas."
    mcname "Kalo kamu berubah pikiran, bisa dateng kok Freya."
    show freya_side at left with dissolve
    freya "Makasih tawarannya [mcname]."
    freya "Nanti aku kabarin kalo berubah pikiran deh."
    hide freya_side at left with dissolve
    "Freya pergi meninggalkan Kana dan [mcname]."
    $ quick_menu=False
    scene black with dissolve
    scene kelas with dissolve
    $ quick_menu=True
    "Setelah Freya pergi, Kana terlihat bingung bagaimana memulai pembicaraan."
    "Melihat hal tersebut, akhirnya [mcname] berinisiatif melanjutkan topik yang ada."
    show kana at char_center with dissolve
    mcname "Gimana jadinya? Kita jadi kan buat belajar barengnya?"
    show kana_side at left with dissolve
    kana "JADI!"
    hide kana_side at left with dissolve
    "Menyadari akan suaranya yang bersemangat Kana pun sedikit malu."
    show kana_side at left with dissolve
    kana "Ah."
    kana "T-tapi… gak ada ide juga sih mau di mana..."
    hide kana_side at left with dissolve
    mcname "Hmmmm..."
    "[mcname] kemudian berpikir untuk menentukan tempat untuk belajar bersama."
    mcname "Gimana kalau kita ke cafe?"
    show kana_side at left with dissolve
    kana "Ehhhh boleh tuh."
    hide kana_side at left with dissolve
    "Kana menjawab dengan begitu semangat. Keadaaan canggung sebelumnya menghilang, sehingga Kana dan [mcname] kembali mengobrol bersama seperti biasanya."
    mcname "Oke, berarti nanti kita ketemuan di sana ya."
    mcname "Nanti aku kabarin lagi kapannya."
    #*SKIP TO SCENE*
    #*BG CAFE*
    #*SIANG*
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}KEESOKAN HARINYA{/color}" with Pause(2.0)
    play music "audio/BGM_Cafe Cerah.mp3" fadein 1.0
    scene cafe with dissolve
    $ quick_menu = True
    "Besoknya Kana dan [mcname] janjian untuk belajar bersama di cafe."
    "[mcname] datang 5 menit lebih awal agar mengamankan posisi duduk untuk Kana."
    "Tidak lama, Kana pun datang melalui pintu."
    #*SFX PINTU TERBUKA ( PINTU YANG ADA LONCENGNYA ) 
    play sound "audio/cafe-entrance.mp3" fadein 1.0
    "Kana mendatangi [mcname], dia terlihat berbeda dari biasanya."
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    kana "Eh maaf ya, nunggu lama."
    hide kana_side at left with dissolve
    mcname "......."
    show kana_side at left with dissolve
    kana "K-kenapa? Ada yang aneh ya sama aku."
    hide kana_side at left with dissolve
    mcname "Ah aku kaget aja ngeliat kamu make baju itu, kerasa beda dari biasanya."
    show kana_side at left with dissolve
    kana "E-eh, Beneran keliatan ya? Ahahah."
    hide kana_side at left with dissolve
    mcname "Iya, kamu keliatan effort banget."
    show kana_side at left with dissolve
    kana "Ummm... Kok kamu kepikir begitu?"
    hide kana_side at left with dissolve
    mcname "Soalnya kamu pake baju yang berbeda dari yang sering kamu pake di kampus, apalagi rambut kamu keliatan lebih rapih, mungkin abis dari salon?"
    "Mungkin rambutnya terlihat sama seperti biasanya, namun entah kenapa [mcname] merasa kalau ada yang berbeda, mungkin itu hanya insting nya saja."
    show kana_side at left with dissolve
    kana "I-iya deh, yuk sekarang kita fokus belajar bareng aja."
    hide kana_side at left with dissolve
    "Dengan wajah yang sedikit memerah Kana pun langsung duduk di dekat [mcname]."
    "Mereka berdua pun memulai untuk belajar."
    $ quick_menu=False
    scene black with dissolve
    scene kelas with dissolve
    $ quick_menu=True
    "Tak terasa 4 jam berlalu~"
    "[mcname] dan Kana mulai merasa bosan dan kurang fokus dengan materi yang ada." 
    menu:
        "Ingin mengganti suasana, [mcname] menawarkan untuk..."
        "Main Game HP Sendiri.":
            "[mcname] milih untuk main game sendiri dan mengabaikan Kana seakan dia tidak ada. Dunia milik berdua antara [mcname] dan HP, hal ini membuat Kana ngambek dan meninggalkan [mcname] yang sedang asik bermain HP."
            $ quick_menu = False
            stop music fadeout 1.0
            scene black with dissolve
            show text "{color=#FFF}*BROOO KALAU LAGI MAIN SAMA TEMEN, JANGAN KESERINGAN MAIN HP NAPA?! KAN JADINYA GINI, YA ELAH YANG BENER AJA.*{/color}" with Pause(2.0)
            show text "{color=#FF0000}BAD END{/color}"
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits
        "Ajak Kana main game.":
            jump AjakKanaMainGame
        "Tidur.":
            "[mcname] milih untuk rebahan dan tiduran untuk sejenak di pangkuan Kana dan minta tolong ke Kana buat bangunin dia. Tapi ternyata saat Kana mencoba membangunkan kamu, kamu malah keenakan tidur di pangkuan Kana. Karena kamu merasa nyaman, akhirnya kamu tidak pernah bangun lagi."
            $ quick_menu = False
            stop music fadeout 1.0
            scene black with dissolve
            show text "{color=#FFF}*EH CUY LO INI LAGI DI CAFE BUKAN DI KOST. LAGIAN KAN INI LAGI KERJA KELOMPOK DAH, KENAPA MALAH TIDUR? MIKIR BRO MIKIR!*{/color}" with Pause(2.0)
            show text "{color=#FF0000}BAD END{/color}"
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits
label AjakKanaMainGame:
    "Untuk refreshing, kamu milih main game yang ada di dalam cafe dan mengajak Kana untuk memainkan game tersebut."
    "Kana yang awalnya ragu pun mulai tertarik saat kamu mulai menjelaskan tentang game yang akan dimainkan tersebut."
    "Mungkin terbawa suasana dan karena mumet saat belajar tadi, Kana dan [mcname] enjoy memainkan game yang ada lebih dari yang mereka duga."
    "Kana pun terlihat menjadi sedikit lebih terbuka kepada [mcname]."
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    kana "Aaaaa, iii kok kalah mulu sihhh... [mcname] ngalah napa..."
    hide kana_side at left with dissolve
    mcname "Hehehehe, you need 1000 years to defeat me."
    $ quick_menu=False
    scene black with dissolve
    scene cafe with dissolve
    $ quick_menu=True
    "Setelah puas bermain game, akhirnya [mcname] dan Kana kembali duduk ke tempat mereka sebelumnya."
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    kana "Game yang tadi seru banget ya."
    hide kana_side at left with dissolve
    mcname "Hahaha iya, apalagi moment pas kamu akhirnya bisa ngalahin aku."
    show kana_side at left with dissolve
    kana "Next game pasti aku menang lagi kok!"
    hide kana_side at left with dissolve
    "Selama mereka duduk, Kana dan [mcname] membicarakan game yang mereka mainkan tadi."
    mcname "Tapi emang sih, cuma beberapa kali main aja kamu sudah jago gitu mainnya."
    show kana_side at left with dissolve
    kana "Hehehe iya kan."
    hide kana_side at left with dissolve
    "Karena merasa suasananya sedang baik, [mcname] mencoba untuk membahas hal-hal yang berbau jejepangan."
    "Kana pernah bilang kalau dia menyukai hal-hal tersebut dan [mcname] ingin mengenal Kana lebih dalam lagi. Tapi [mcname] teringat, hal-hal itulah yang membuat Kana merasa berbeda dari yang lain."
    mcname "Btw Kana, kamu kan tau banyak tentang jejepangan. Kebetulan Papahku wibu, dia suka ngidol dan jejepangan gitu. Tapi aku pengen tau lebih banyak lagi, jadi kalo boleh sih aku mau tanya-tanya tentang hobi kamu."
    show kana_side at left with dissolve
    kana "E-Eh,, b-boleh kok."
    hide kana_side at left with dissolve
    mcname "Tenang aja kok. Aku ga bakalan anggep kamu aneh atau apalah, jadi santai aja. Aku bener-bener pengen tau lebih banyak sih tentang ini dari kamu."
    show kana_side at left with dissolve
    kana "EEEEEEEH???"
    kana "SERIUS!!???"
    hide kana_side at left with dissolve
    "Nada kana yang begitu bersemangat membuat hampir seluruh orang di cafe tersebut melihat ke arah Kana, sadar akan hal itu Kana pun segera duduk dan memelankan suaranya lagi."
    show kana_side at left with dissolve
    kana "E-Eh maaf ya, terlalu semangat hehe, tapi janji ya jangan sampe takut sama aku."
    hide kana_side at left with dissolve
    mcname "Iya aku JANJI kok, SUMPAH. Kan aku juga yang nanya duluan."
    show kana_side at left with dissolve
    kana "Janji kelingking?"
    hide kana_side at left with dissolve
    mcname "Iya. Kelingking kita berjanji, jari manis jadi saksi?"
    show kana_side at left with dissolve
    kana "Ih apaan sih."
    kana "Yauda deh kalau gitu, jadi kita harus mulai dari yang mana nih? Kamu mau tau soal apa deh?"
    hide kana_side at left with dissolve
    mcname "Hmmm, bingung juga sebenernya... Hmmm, dari apa yang kamu lagi suka sekarang deh."
    show kana_side at left with dissolve
    kana "Kalo aku sekarang lagi suka dengerin lagu-lagu idol, jujur aku suka dengan dance sama lagunya."
    hide kana_side at left with dissolve
    mcname "Heeee..."
    "Kana menjelaskan hal-hal yang dia suka dengan penuh semangat."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Cafe Sore.mp3" fadein 1.0
    scene cafe with dissolve
    #HARUSNYA CAFE SORE
    $ quick_menu = True
    "Tidak terasa Kana membahas hal tersebut lebih dari 1 jam."
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    kana "E-ehhh, udah 1 jam lebih!?? Maaf ya kayaknya aku kebablasan deh."
    hide kana_side at left with dissolve
    "Kana melihat ke arah [mcname] dengan panik, takut [mcname] merasa aneh atau pun gelisah karena semua hal wibu yang telah diceritakan olehnya."
    mcname "Ga perlu mikir yang aneh-aneh deh Kana. Santai aja, aku kan udah janji."
    mcname "Lagian dengerin kamu cerita kaya gitu seru kok, ternyata banyak ya yang masih belum aku tau dari kamu."
    mcname "Seneng aja bisa tau sisi kamu yang seperti ini."
    hide kana at char_center with dissolve
    show kana_shy at char_center with dissolve
    "Mendengar hal tersebut wajah Kana memerah."
    hide kana_shy at char_center with dissolve
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    kana "Eh... ya udah nanti ku kasih playlist yang sering kudengar ke kamu deh."
    hide kana_side at left with dissolve
    "Kana melihat sekeliling, terlihat suasana cafe berbeda dari saat mereka datang."
    show kana_side at left with dissolve
    kana "Ah, gak kerasa sudah jam segini ya."
    hide kana_side at left with dissolve
    mcname "Kayaknya kita malah kebanyakan main daripada belajarnya ya, haha."
    mcname "Tapi gak apa-apa, setidaknya kita sudah nyicil sedikit-sedikit lah ya."
    show kana_side at left with dissolve
    kana "Iya, hehe."
    hide kana_side at left with dissolve
    mcname "Gimana kalo kita balik dulu, soalnya takut kemaleman."
    show kana_side at left with dissolve
    kana "Ummmnn…"
    hide kana_side at left with dissolve
    "Kana terlihat ingin mengatakan suatu hal."
    show kana_side at left with dissolve
    kana "[mcname]..."
    kana "Aku rasa kita masih belum cukup belajarnya"
    kana "Jadi... nanti mau belajar bareng lagi?"
    hide kana_side at left with dissolve
    "Kana mengatakan tersebut dengan sedikit gugup, mungkin takut jika [mcname] akan menolaknya."
    mcname "Boleh kok. Lagipula aku juga free nanti."
    show kana_side at left with dissolve
    kana "O-oke janji ya."
    kana "Nanti aku kabarin."
    hide kana_side at left with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene awan with dissolve
    with Pause(2.0)
    play music "audio/BGM_Cafe Cerah.mp3" fadein 1.0
    scene cafe with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    "Beberapa hari setelah hari itu, [mcname] dan Kana selalu belajar bersama di cafe."
    "Bahkan pelayan di sana pun terasa seperti teman karena saking seringnya bertemu."
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    kana "Haaaaahhh..."
    kana "Kayaknya aku mulai bosen deh belajar di sini terus."
    kana "Pengennya mungkin ganti suasana lain."
    hide kana_side at left with dissolve
    mcname "Hmmmm... bisa sih."
    mcname "Tapi mau di mana kira-kira?"
    show kana_side at left with dissolve
    kana "Gimana kalo kita ke Jepang, sekalian nonton konser si M*ku?"
    hide kana_side at left with dissolve
    "Karena sudah mumet dengan pelajaran kuliah, Kana mengatakan hal-hal yang tidak masuk akal."
    mcname "Kayak agak mustahil kalo sekarang."
    mcname "Bahkan kalau pun bisa, sulit buat dapetin tiket konsernya."
    show kana_side at left with dissolve
    kana "Hahaha iya juga sih..."
    kana "Ke pantai deh."
    hide kana_side at left with dissolve
    "Mendengar kata pantai membuat [mcname] membayangkan Kana menggunakan swimsuit."
    "Sadar akan apa yang dibayangkan, [mcname] langsung menggeleng-gelengkan kepalanya."
    mcname "Pantai pun sekarang lagi rame banget."
    mcname "Jadi walaupun kita ke sana, yang kita liat cuma gerombolan manusia."
    show kana_side at left with dissolve
    kana "Hmmmmmm jadi di mana ya."
    hide kana_side at left with dissolve
    "[mcname] dan Kana merenung untuk memikirkan tempat yang lain."
    #*SFX notif chat*
    show kana_side at left with dissolve
    kana "Hmmmm?"
    hide kana_side at left with dissolve
    "Kana membuka HPnya."
    "Saat membaca pesan yang masuk Kana kemudian tersenyum."
    show kana_side at left with dissolve
    kana "[mcname], kata mamah dia pengen ketemu sama kamu."
    hide kana_side at left with dissolve
    mcname "EH?? Kenapa?"
    "[mcname] bingung kenapa mamahnya Kana ingin bertemu dengannya."
    show kana_side at left with dissolve
    kana "Hmmm gak tau juga sih."
    kana "Tapi gimana kalau kita belajarnya di rumahku aja?"
    kana "Sekalian ketemu sama Mamah ku, kan. Hehe."
    hide kana_side at left with dissolve
    mcname "Hmmm, kalau itu bisa sih."
    #*SKIP TO SCENE*
    #*BG LANGIT*
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_MC Pertama Kali ke JKT + BG Pagi.mp3" fadein 1.0
    scene awan with dissolve
    $ quick_menu = True
    "[mcname] dan Kana langsung menuju ke rumah Kana setelah pulang dari cafe."
    mcname "{i}Gak nyangka aku bakal ke rumah Kana dan ketemu mamahnya lagi.{/i}"
    #ASSET PINTU RUMAH KANA
    "Kana kemudian mengetuk pintu rumahnya."
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    kana "Mamahh, aku pulaaang~"
    kana "Ada [mcname] juga nih."
    hide kana_side at left with dissolve
    hide kana at char_center with dissolve
    "Terdengar suara pintu terbuka, di sana terlihat Mamahnya Kana."
    "Mamah Kana" "Selamat datang Kana. Terima kasih udah mau datang, [mcname]."
    "Mamah Kana" "Ayo masuk."
    "Setelah diperbolehkan Mamahnya Kana, akhirnya [mcname] masuk ke rumahnya Kana, mengikuti di belakang Kana."
    stop music fadeout 1.0
    $ quick_menu=False
    scene black with dissolve
    play music "audio/BGM_Dosen + Rektor.mp3" fadein 1.0
    #HARUSNYA BGM RUANG TAMU KANA
    scene lorong with dissolve
    #HARUSNYA RUANG TAMU KANA
    $ quick_menu=True
    "Mamah Kana" "Anggap rumah sendiri ya."
    mcname "Ah, makasih tante."
    "Mamahnya Kana kemudian pergi ke dapur."
    "Kana dan [mcname] duduk di sofa bersama-sama."
    "Mereka berbincang-bincang sambil mulai belajar kembali tentang kuliah mereka."
    "Mamah Kana" "Ini ya minum buat kalian, sekalian nanti makan siang di sini ya biar bisa fokus belajarnya."
    mcname "Waah, gak perlu repot-repot tante."
    "Mamah Kana" "Duh gapapa santai aja."
    "Mamahnya Kana pun kembali ke dapur."
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    kana "Eh kalo gitu aku ikut bantu Mah."
    hide kana_side at left with dissolve
    "Kana pun kemudian pergi ke dapur, meninggalkan [mcname] sendirian di ruang tamu."
    "Sambil menunggu Kana, [mcname] pun melihat-lihat ruang tamunya Kana."
    mcname "Heeeee..."
    $ quick_menu=False
    scene black with dissolve
    scene kelas with dissolve
    #HARUSNYA RUANG TAMU KANA
    $ quick_menu=True
    "Tidak lama setelah itu, Mamahnya Kana masuk ke ruang tamu."
    "Tapi Kana tidak terlihat mengikutinya."
    "Mamah Kana" "Ini ya [mcname], dimakan."
    "Mamahnya Kana membawakan kue kering."
    mcname "Waduh makasih lagi tante, jadi gak enak."
    "Mamah Kana" "Udah gak usah dipikirin."
    "Mamah Kana" "Lagian ini juga sebagai ucapan terima kasih tante buat kamu."
    "Mamah Kana" "Soalnya udah banyak membantu Kana."
    mcname "Engga kok tante, itu semua berkat usaha dari diri Kana sendiri juga."
    mcname "Saya gak ngelakuin hal yang spesial."
    "Mamah Kana" "Tetap saja karena kamu, jadinya Kana beberapa hari ini perasaaannya keliatan lebih baik."
    "Mamah Kana" "Oleh karena itu, makasih ya."
    "Mamah Kana" "Sebagai imbalannya, tante bakal ngabulin satu permintaan apa aja deh buat kamu."
    mcname "E-Eh."
    "[mcname] bingung dengan perkataan Mamahnya Kana."
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    kana "MAAHHH!!! Bisa bantu sebentar di sini gak??"
    hide kana_side at left with dissolve
    hide kana at char_center with dissolve
    "Di dapur terdengar suara Kana memanggil."
    "Mamah Kana" "Iyaaa bentarrr."
    "Mamah Kana" "Duh kayaknya Kana manggil nih, maklum Kana jarang ke dapur."
    "Mamah Kana" "Tapi katanya karena [mcname] dateng, dia jadi pengen nyoba masak untuk makan siang, fufufu."
    "Mamahnya Kana kemudian kembali ke dapur."
    "[mcname] kembali sendirian lagi di ruang tamu, namun kali ini bingung dengan perkataan yang dikatakan oleh Mamahnya Kana."
    stop music fadeout 1.0
    $ quick_menu=False
    scene black with dissolve
    #HARUSNYA BG SORE
    play music "audio/BGM_Dosen + Rektor.mp3" fadein 1.0
    #HARUSNYA BGM RUANG TAMU KANA
    scene kelas with dissolve
    #HARUSNYA RUANG TAMU KANA
    $ quick_menu=True
    "Tak terasa waktu telah menjadi sore. [mcname] melihat Kana sepertinya sudah mulai tidak fokus. Nafasnya mulai tidak beraturan, mukanya memerah."
    show kana_shy at char_center with dissolve
    mcname "Kamu gapapa Kana?"
    show kana_side_shy at left with dissolve
    kana "Gapapa kok. Aku masih kuat."
    hide kana_side_shy at left with dissolve
    mcname "Kalo sampe di sini aja gimana? Kamu kayaknya butuh istirahat."
    show kana_side_shy at left with dissolve
    kana "B-baiklah…"
    hide kana_side_shy at left with dissolve
    hide kana_shy at char_center with dissolve
    show kana at char_center with dissolve
    mcname "Kalo gitu aku pamit dulu ya... Jangan lupa besok UTS."
    show kana_side at left with dissolve
    kana "Kalo gitu aku antar ke depan pintu, deh."
    hide kana_side at left with dissolve
    "Sudah lumayan lama [mcname] dan Kana belajar bareng, sehingga sudah waktunya [mcname] untuk pulang. [mcname] membereskan barang-barangnya lalu beranjak pergi ke depan pintu sambil diantar oleh Kana."
    mcname "Makasih ya, makanannya."
    show kana_side at left with dissolve
    kana "Makasih juga ya [mcname], sudah mau mampir."
    kana "Achoo!!"
    hide kana_side at left with dissolve
    #ASSET PINTU RUMAH KANA
    "Kana memberikan ucapan selamat tinggal kepada [mcname] di depan pintu."
    "Mamahnya Kana ada urusan pekerjaan jadi tidak ikut mengantar [mcname]."
    mcname "Iya Kana, makasih juga udah menjamu."
    mcname "Salam juga untuk mama."
    show kana_side at left with dissolve
    kana "Achoo!!"
    hide kana_side at left with dissolve
    mcname "Nah, kan. Jaga kesehatan ya."
    show kana_side at left with dissolve
    kana "Achoo!!"
    kana "Aman kok, aku kuat."
    hide kana_side at left with dissolve
    mcname ".........."
    stop music fadeout 1.0
    $ quick_menu=False
    scene black with dissolve
    play music "audio/BGM_Dosen + Rektor.mp3" fadein 1.0
    #HARUSNYA BGM SORE
    scene kelas with dissolve
    #HARUSNYA BG LANGIT SORE
    $ quick_menu=True
    "Diperjalanan pulang..."
    mcname "kira -kira apa yang dimaksud sama Mamahnya Kana tadi ya…"
    "[mcname] mengingat kejadian yang telah terjadi saat [mcname] berkunjung ke tempat Kana."
    mcname "Dan juga Kana tadi terlihat sakit."
    mcname "Moga saja dia gak kenapa-napa."
    #*Transisi Gelap*
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}HARI UTS{/color}" with Pause(2.0)
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    scene kelas with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    "Hari UTS telah tiba, [mcname] merasa yakin akan dirinya karena sudah belajar bersama Kana cukup lama dan merasa cukup memahami mata kuliah yang telah diberikan."
    "[mcname] melihat ke arah Kana dan menyapa, akan tetapi perhatiannya teralihkan saat melihat muka Kana."
    #*Sprite KANA MUKA MERAH PUCAT*
    show kana_sick at char_center with dissolve
    mcname "Pagi Kana"
    show kana_side_sick at left with dissolve
    kana "Ah, P- Pagi, [mcname]."
    hide kana_side_sick at left with dissolve
    "Muka kana terlihat lebih pucat daripada kemarin saat [mcname] berkunjung ke rumahnya."
    mcname "Kamu gapapa?"
    show kana_side_sick at left with dissolve
    kana "Ga-gapapa kok. Aku masih kuat."
    hide kana_side_sick at left with dissolve
    mcname "Kamu yakin???"
    mcname "Soalnya mukamu kayaknya..."
    play music "audio/open_door.mp3" fadein 1.0
    hide kana_sick at char_center with dissolve
    #*SUARA PINTU TERBUKA*
    "Pengawas ujian datang dan UTS pun akan dimulai, membuat [mcname] tidak dapat beranjak dari kursinya."
    "Pengawas" "Baiklah semuanya, UTS akan dimulai jadi saya harap semuanya menonaktifkan gadgetnya serta mengerjakannya secara mandiri. Waktu kalian selama 45 menit, dimulai dari sekarang."
    $ quick_menu = False
    jump kanaafterquiz
#UTS
label kanaafterquiz:
    $ quick_menu = True
    mcname "Ahhh akhirnya beres."
    "[mcname] mengangkat tangannya."
    mcname "Maaf, Pak. Kalau sudah selesai apakah boleh dikumpulkan sekarang?"
    "Pengawas" "Wah, cepat juga. Sepertinya kamu yang pertama selesai."
    "Pengawas" "Hmmm... Baiklah, boleh dikumpulkan kalau sudah yakin."
    "[mcname] beranjak dari tempat duduk."
    "Pada saat akan mengumpulkan lembar jawaban, tiba-tiba [mcname] mendengar suara."
    stop music fadeout 1.0
    #*SFX ORANG JATUH*
    "Pandangan semua orang pun teralihkan dan saat itu juga, [mcname] melihat Kana yang tergeletak di lantai. Tanpa ragu-ragu, [mcname] berlari menghampiri Kana yang tergeletak lemas dan tidak sadarkan diri."
    show kana_sick at char_center with dissolve
    mcname "Nay!! Kamu kenapa Nay?! Nayyy!"
    hide kana_sick at char_center with dissolve
    "Penjaga ujian dan staff pun memberitahukan murid untuk menghubungi pihak kesehatan kampus akan tetapi [mcname] memberitahukan tentang riwayat kesehatan Kana."
    "Para staf pun panik dan segera menghubungi rumah sakit terdekat."
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Kelas.mp3" loop fadein 1.0
    #HARUSNYA SFX AMBULANCE
    scene kelas with dissolve
    #HARUSNYA STOCK IMAGE AMBULANCE
    $ quick_menu = True
    "Tak lama kemudian, Kana dibawa dengan ambulans sambil ditemani [mcname]."
    "Saat di ambulans, Kana sempat sadar."
    show kana_sick at char_center with dissolve
    show kana_side_sick at left with dissolve
    kana "[mcname]..."
    hide kana_side_sick at left with dissolve
    mcname "Kana! Kana!"
    show kana_side_sick at left with dissolve
    kana "Aku takut..."
    hide kana_side_sick at left with dissolve
    mcname "Aku ada di sini. Kamu ga perlu khawatir! Istirahatlah."
    show kana_side_sick at left with dissolve
    kana "[mcname]..."
    hide kana_side_sick at left with dissolve
    "Kana pun kembali memejamkan matanya."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    #HARUSNYA BGM SEDIH RUMAH SAKIT
    scene lorong with dissolve
    #HARUSNYA STOCK IMAGE RUMAH SAKIT
    $ quick_menu = True
    "Setelah sesampainya di rumah sakit, Kana pun diperiksa oleh dokter dan perawat."
    "Di situ [mcname] hanya bisa menunggu jawaban dari pihak dokter, setelah beberapa saat pihak dokter pun keluar dari ruangan."
    mcname " DOK!! GIMANA KANA, DOK!??"
    "Dokter" "Maaf anak muda, tapi kami sudah berusaha semaksimal mungkin. Jadi mohon terima kabar ini dengan berlapang dada, tapi Kana…"
    mcname "HA!? MAKSUDNYA APAAN DOK!? KANA KENAPA DOK!!?"
    "Dokter" "Kana... dia... "
    stop music
    play music "audio/BGM_Lawak Tana.mp3"
    #HARUSNYA LAWAK YANG SATUNYA
    "Dokter" "DIA GAPAPA KOKK~ Cuma demam kecapekan doang, ga usah khawatir."
    "Dokter" "Soal riwayat kesehatannya, buat sekarang Kana udah diinfus jadinya aman. Harusnya sekarang kamu udah bisa jenguk dia."
    mcname "AH ELAH DOK, GA LUCU TAUUUU."
    "Marah akan candaan dokter, [mcname] segera pergi ke dalam ruangan perawatan tempat Kana berada."
    stop sound fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    #HARUSNYA BGM SEDIH RUMAH SAKIT
    scene lorong with dissolve
    #HARUSNYA STOCK IMAGE RUMAH SAKIT
    show kana_sick at char_center with dissolve
    $ quick_menu = True
    mcname "Kana! Kamu gapapa kan!?"
    show kana_side_sick at left with dissolve
    kana "Kamu kok kaya kecapean gitu sih [mcname]? Kamu kenapa?"
    hide kana_side_sick at left with dissolve
    mcname "AHHH ini gara-gara si dokter bercandain kondisi kamu tadi. Btw kok bisa demam tinggi? Kemarin bukannya istirahat tapi lanjut maksain begadang ya?"
    show kana_side_sick at left with dissolve
    kana "Eh... i-iya, soalnya aku ngerasa masih kurang belajarnya. Jadi aku maksain buat belajar lebih sampai subuh. Eh ternyata waktu paginya udah agak pusing."
    hide kana_side_sick at left with dissolve
    mcname "Kana, jujur aku pengen marahin kamu tapi aku ga bisa soalnya kamu lagi sakit."
    show kana_side_sick at left with dissolve
    kana "Huhu maaf... Eh bentar ujian kamu gimana?"
    hide kana_side_sick at left with dissolve
    mcname "Kamu ga usah khawatir kok, ujianku dah selesai. Kalo ujianmu, kata pengawas nanti bakal diadain susulan setelah UTS selesai. Sekarang kamu harus fokus sama kesehatanmu dulu aja."
    show kana_side_sick at left with dissolve
    kana "[mcname].."
    kana "Makasih banyak ya udah mau bantuin aku, maaf ngerepotin yaa."
    hide kana_side_sick at left with dissolve
    hide kana_sick at char_center with dissolve
    show kana_scared at char_center with dissolve
    mcname "Kana... Kamu ga ngerepotin kok, santai aja. Sekarang kamu gimana rasanya? Udah mendingan?"
    show kana_side_scared at left with dissolve
    kana "Jujur aku juga ga tau, mungkin terasa lebih baik karena kamu ada yang nemenin."
    kana "Tapi... aku takut."
    kana "Aku takut sendirian lagi..."
    kana "Takut kejadian waktuku kecil terulang kembali dan dirawat sendirian di rumah dengan waktu yang lama."
    hide kana_side_scared at left with dissolve
    "Wajah Kana telihat lemas, melihat ke arah [mcname] seakan ingin menangis. Akan tetapi ia tetap berusaha tersenyum."
    mcname "Kana... jangan mikir kaya gitu. Aku bakalan selalu temenin kamu apapun yang terjadi oke? Yang penting kamu sehat dulu aja deh, ga usah mikirin yang lain dulu."
    hide kana_scared at char_center with dissolve
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    kana "Iya..."
    kana "Ini udah mendingan kok."
    hide kana_side at left with dissolve
    "Kana menatap [mcname] sambil tersenyum."
    "[mcname] juga tersenyum kepada Kana."
    show kana_side at left with dissolve
    kana "Umm... aku udah boleh pulang gak ya? Soalnya ini lumayan gak enak keringetan, aku pengen ganti baju."
    hide kana_side at left with dissolve
    mcname "Eh bentar aku coba tanyakan dulu ke perawatnya."
    stop sound fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    scene lorong with dissolve
    #HARUSNYA STOCK IMAGE RUMAH SAKIT
    show kana at char_center with dissolve
    $ quick_menu = True
    mcname "Ehh ini bisa katanya, tapi harus ada yang anterin kamu pulang. Mamahmu ke mana?"
    show kana_side at left with dissolve
    kana "Ummm... Kalo kamu bisa ga [mcname]? Nganterin aku pulang…"
    kana "Soalnya Mamahku lagi sibuk jam-jam segini."
    hide kana_side at left with dissolve
    mcname "Eh aku ??!!"
    mcname "{i}Waduh gapapa nih? Tapi ga ada siapa-siapa lagi sih di sini. Harus gimana nih gue?{/i}"
    hide kana at char_center with dissolve
    menu:
        "Yang kamu lakukan..."
        "Terima tawaran Kana":
            jump TerimaTawaranKana
        "Nolak tawaran Kana":
            "[mcname] menolak tawaran Kana. [mcname] terlalu malu untuk menerima ajakan itu, dan akhirnya Kana disuruh pulang sendiri."
            $ quick_menu = False
            stop music fadeout 1.0
            scene black with dissolve
            show text "{color=#FFF}*BROOO ANAK ORANG LAGI SAKIT MALAH LO SURUH BALIK SENDIRI GA TAKUT DIA KENAPA KENAPA KAH?.*{/color}" with Pause(2.0)
            show text "{color=#FF0000}BAD END{/color}"
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits
        "Kabur dari tempat":
            "[mcname] memilih kabur dari tempat itu saking malunya karena membayangkan berduaan dengan Kana. Setelah itu pun kamu tidak tau Kana pulang atau tidak, tetapi kamu hanya mendapatkan kabar dari Kana melalui HP dengan kata-kata "kamu jahat"."
            $ quick_menu = False
            stop music fadeout 1.0
            scene black with dissolve
            show text "{color=#FFF}*BROOO KO KABUR SIH? APA SIH YANG BIKIN LU MALU TUH, GA JELAS BANGET DAH!*{/color}" with Pause(2.0)
            show text "{color=#FF0000}BAD END{/color}"
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits
label TerimaTawaranKana:
    "[mcname] pun menerima tawaran Kana. Meskipun malu, tapi rasa ingin menjaga Kana lebih besar daripada rasa malunya."
    show kana at char_center with dissolve
    mcname "K-kalau kamu gak keberatan sih boleh, Kana. Nanti aku temenin, tapi aku minta ijin dulu ke perawat ya. Soalnya harus isi surat-surat keterangan dulu, haha."
    hide kana at char_center with dissolve
    show kana_shy at char_center with dissolve
    show kana_side_shy at left with dissolve
    kana "I-iya, makasih banyak ya sekali lagi.\n*Blush*"
    hide kana_side_shy at left with dissolve
    #*SKIP TO SCENE*
    #*BG RUMAH KANA*
    stop sound fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    #HARUSNYA BGM RUANG TAMU KANA
    scene lorong with dissolve
    #HARUSNYA BG RUANG TAMU KANA
    $ renpy.block_rollback()
    $ quick_menu = True
    "Sesaat setelah datang ke rumah Kana, [mcname] membawa Kana ke kamarnya."
    stop sound fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Kosan 2.mp3" fadein 1.0
    #HARUSNYA BGM KAMAR KANA
    scene kamar kana with dissolve
    #HARUSNYA BG KAMAR KANA
    $ quick_menu = True
    "Kana pun istirahat di kasurnya ditemani oleh [mcname] yang duduk di kursi belajar Kana."
    show kana at char_center with dissolve
    mcname "Oke, Kana sekarang kamu tunggu dulu ya. Ini aku beliin makanan pesen online, semoga cocok yaa. Bentar aku siapin dulu."
    show kana_side at left with dissolve
    kana "Makasih yaa, maaf ngerepotin."
    hide kana_side at left with dissolve
    mcname "Udah lah ga usah kaya gitu, kan kita udah jadi temen. Santai aja Kana."
    show kana_side at left with dissolve
    kana "Yeeeee makasih yaaa, akhirnya setelah sekian lama +1 teman."
    hide kana_side at left with dissolve
    mcname "LAH!? Kan dah temenan dari lama, gimana sih hahaha."
    show kana_side at left with dissolve
    kana "Gapapa yang penting +1 teman, hehe."
    hide kana_side at left with dissolve
    mcname "Hadeh yaudah. Aku siapin makanan dulu ya."
    hide kana at char_center with dissolve
    show kana_shy at char_center with dissolve
    "Setelah [mcname] pergi, Kana pun memeluk bantalnya dengan wajah yang memerah."
    hide kana_shy at char_center with dissolve
    "[mcname] pun pergi ke dapur untuk mengambilkan makanan dan obat yang telah disiapkan oleh dokter."
    $ quick_menu = False
    scene black with dissolve
    #HARUSNYA BGM RUANG TAMU KANA
    scene lorong with dissolve
    #HARUSNYA BG RUANG TAMU KANA
    show kana at char_center with dissolve
    $ quick_menu = True
    mcname "Kana. Ini makanannya kamu makan dulu ya, obatnya ada di sini. Btw kamu udah kabarin Mamah kamu?"
    show kana_side at left with dissolve
    kana "Udah kok. Mamah awalnya mau langsung pergi ke rumah sakit, tapi aku bilang ga usah soalnya udah ada kamu yang temenin aku. Aku juga ga mau ganggu waktu kerjanya Mamah."
    hide kana_side at left with dissolve
    mcname "Oke deh kalau begitu. Btw dipikir pikir dokter tadi udah ngeselin, tapi lucu juga ya."
    show kana_side at left with dissolve
    kana "Kenapa tuh?"
    hide kana_side at left with dissolve
    mcname "Iya nih tadi udah bikin drama kaya di TV yang bilang \"Kami sudah berusaha semaksimal mungkin.\"" 
    mcname "Eh tapi sekarang obatnya {i}aergiamint-hachu{/i}, nama obatnya aneh banget ya."
    show kana_side at left with dissolve
    kana "Oooo, itu obat yang biasa aku minum kok. Namanya emang aneh kan, tapi itu manjur kok. Kayaknya..."
    hide kana_side at left with dissolve
    "Kana pun mencoba makan akan tetapi tangannya terkadang merasa lemas karena terdapat infus di lengan kanannya."
    #Sfx prang ( suara sendok jatuh ke piring )
    mcname "Kana!!!?? Kamu gapapa?"
    show kana_side at left with dissolve
    kana "Ah.. iya."
    kana "Gapapa kok, cuma ini tangan kananku agak lemes aja soalnya ada infusan. Terus tadi aku coba makan pake tangan kiri, ternyata susah juga ya."
    hide kana_side at left with dissolve
    mcname "Eh... Bentar kalau gitu aku bantu suapin kamu aja."
    hide kana at char_center with dissolve
    show kana_shy at char_center with dissolve
    show kana_side_shy at left with dissolve
    kana "Eh?!!!"
    hide kana_side_shy at left with dissolve
    mcname "????"
    mcname "Kenapa?"
    show kana_side_shy at left with dissolve
    kana "E-enggak apa-apa kok. K-kalau kamu emang bersedia, boleh aja sih..\n*Blush*"
    hide kana_side_shy at left with dissolve
    mcname "Oke dehh, sini aku bantu sua-"
    mcname "*Blush*"
    "Tiba-tiba [mcname] terdiam, sadar akan perkataannya yang bisa dibilang cukup berani. Akan tetapi nasi sudah menjadi bubur, [mcname] tidak dapat lagi menarik kata katanya tersebut."
    show kana_side_shy at left with dissolve
    kana "K-k-kenapa [mcname]?\n*Blush*"
    hide kana_side_shy at left with dissolve
    mcname "Ehhhh enggaa ada apa-apa kok. Sini aku suapin.\n*Blush*"
    mcname "{i}Aduhhh nyuapin Kana? Kok bisa ya tiba-tiba tanpa sadar ngomong gitu? Tapi kalau nggak dibantu, nanti dia ga makan. Terus dia ga bisa minum obat, terus nanti dia ga sehat, AAAAA. Oke deh, aku harus bisa!{/i}"
    "[mcname] pun mengambil makanan dari piring Kana, mencoba mendekatkan sendoknya ke mulut Kana dengan perlahan."
    mcname "Aaaaaaa~"
    show kana_side_shy at left with dissolve
    kana "Aaaaaaaa~"
    hide kana_side_shy at left with dissolve
    hide kana_shy at char_center with dissolve
    stop music fadeout 1.0
    #*SFX PINTU TERBUKA KERAS(BRAK)*
    $ quick_menu = False
    window auto hide
    with Pause(2.0)
    play music "audio/BGM_Lawak Tana.mp3" fadein 1.0
    #HARUSNYA YANG NGAKAK SATUNYA
    window auto show
    $ quick_menu = True
    "Saat itu pun suara pintu terbuka keras membuat Kana dan [mcname] kaget terdiam."
    show freya_shock at char_center with dissolve
    show freya_side_shock at left with dissolve
    freya "KANAAA!!! KAMU GAPAPA KA-"
    hide freya_side_shock at left with dissolve
    "Saat itu juga Freya melihat [mcname] dan Kana yang sedang duduk dengan posisi tangan [mcname] yang membawa sendok makanan ke mulut Kana."
    hide freya_shock at char_center with dissolve
    show freya_awe at char_left with dissolve
    show freya_side_awe at left with dissolve
    freya "............."
    hide freya_side_awe at left with dissolve
    show kana at char_right with dissolve
    mcname "............."
    show kana_side at left with dissolve
    kana "............."
    hide kana_side at left with dissolve
    hide freya_awe at char_left with dissolve
    show freya at char_left with dissolve
    show freya_side at left with dissolve
    freya "Eh sorry ganggu ya. Hehe, silahkan lanjutin."
    hide freya_side at left with dissolve
    mcname "Ehhhh Freeeya tungguu!! Aku bisa jelasin!!"
    show kana_side at left with dissolve
    kana "Freeeyy!!! Tunggu dulu sini, cepat ke sini-"
    hide kana_side at left with dissolve
    #(*SFX BATUK BATUK UHUK UHUK)"
    show kana_side at left with dissolve
    kana "UHUK! UHUK!!"
    hide kana_side at left with dissolve
    "Dengan secepat kilat Freya pun langsung menghampiri Kana yang terbatuk batuk dan menanyakan kondisi Kana saat itu."
    stop sound fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Kosan 1.mp3" fadein 1.0
    #HARUSNYA BGM KAMAR KANA
    scene kamar kana with dissolve
    #HARUSNYA BG KAMAR KANA
    $ quick_menu = True
    "[mcname] pun menjelaskan situasi tersebut dan akhirnya Freya mengerti dengan apa yang terjadi. Freya memarahi Kana yang memaksakan dirinya untuk belajar hingga sakit dan Kana pun berjanji untuk beristirahat terlebih dahulu."
    show freya at char_center with dissolve
    show freya_side at left with dissolve
    freya "Yaudah kamu habisin dulu makanannya, Nay."
    freya "Setelah itu, makan obatnya lalu istirahat."
    hide freya_side at left with dissolve
    hide freya at char_center with dissolve
    show kana at char_center with dissolve
    mcname "Iya, Kana. Pokoknya kesehatan kamu yang paling penting."
    show kana_side at left with dissolve
    kana "I-iya. Maaf ya. Makasih udah mau nemenin aku kayak gini…"
    hide kana_side at left with dissolve
    #BG Langit Sore
    stop sound fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    #HARUSNYA LANGIT SORE
    play music "audio/BGM_Kosan 1.mp3" fadein 1.0
    #HARUSNYA BGM KAMAR KANA
    scene kamar kana with dissolve
    #HARUSNYA BG KAMAR KANA
    $ quick_menu = True
    "Setelah Kana selesai makan dan meminum obat dari dokter, terdengar suara pintu terbuka dan terlihat Mamah Kana datang dari arah pintu."
    play sound "audio/open_door.mp3"
    show kana at char_center with dissolve
    "Mamah Kana" "Astaga, kamu gapapa Naya?"
    show kana_side at left with dissolve
    kana "Iya aku udah baikan kok, Mah. Maaf ya kalau bikin mamah khawatir, ini juga udah makan dan minum obat kok. Jadi tinggal istirahat aja."
    hide kana_side at left with dissolve
    "Mamah Kana" "Eh ya udah kamu istirahat aja yaa. Freya sama [mcname], kita ngobrol di ruang depan aja ya. Biar Kana istirahat."
    mcname "Iya, Kana harus istirahat."
    hide kana at char_center with dissolve
    show freya at char_center with dissolve
    show freya_side at left with dissolve
    freya "Get well soon, Nay."
    hide freya_side at left with dissolve
    "[mcname] dan Freya pun meninggalkan Kana untuk beristirahat, dan mengikuti Mamah Kana menuju ruang tengah."
    stop sound fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Kosan 1.mp3" fadein 1.0
    #HARUSNYA BGM RUANG TENGAH RUMAH KANA
    scene lorong with dissolve
    #HARUSNYA BG RUANG TENGAH RUMAH KANA
    show freya at char_center with dissolve
    $ quick_menu = True
    "Mamah Kana" "Makasih banyak ya udah mau nemenin sama ngerawat Kana. Untung aja ada kalian, kalau engga... Aduhh ga kebayang deh."
    "Mamah Kana ""Sekali lagi makasih banyak ya."
    mcname "Eh iya tante sama-sama, kebetulan aku bisa bantu jadi aku bantuin, hehe."
    show freya_side at left with dissolve
    freya "Iya aman aja kok kalau sama kita. Eh udah jam segini, maaf ya tante aku pulang dulu. Udah ditunggu sama orang tua, ada acara soalnya hehe."
    hide freya_side at left with dissolve
    mcname "Iya tante, aku juga pulang dulu ya. Sekarang Kana udah ada yang jaga, jadi mau pulang ya. Udah jam segini juga."
    "Mamah Kana" "Eh iya, lupa kalau udah jam segini. Hati hati di jalan yaaa, sekali lagi makasih banyak."
    mcname "Sama-sama, tante."
    show freya_side at left with dissolve
    freya "Sama-sama, tante."
    hide freya_side at left with dissolve
    "[mcname] dan Freya pun berpisah menuju ke rumahnya masing-masing."
    stop sound fadeout 1.0
    $ quick_menu = False
    scene awan with dissolve
    play music "audio/BGM_MC Pertama Kali ke JKT + BG Pagi.mp3" fadein 1.0
    $ quick_menu = True
    "Selagi dalam masa pemulihan, [mcname] dan Freya saling bergantian untuk menjenguk Kana."
    "Setelah Kana benar-benar sehat, Kana pun melakukan ujian susulan untuk mengejar ketertinggalan UTS yang sebelumnya."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}HARI UTS SUSULAN{/color}" with Pause(2.0)
    play music "audio/BGM_Kampus.mp3" fadein 1.0
    scene depan kampus with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname] dan Freya mengantar Kana yang akan melakukan UTS susulan."
    show kana at char_right with dissolve
    show freya at char_left with dissolve
    mcname "Good luck, Kana!"
    show freya_side at left with dissolve
    freya "Kamu pasti bisa! Do it, Nay!"
    hide freya_side at left with dissolve
    show kana_side at left with dissolve
    kana "Makasih, teman-teman. Tunggu aku, ya!"
    hide kana_side at left with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Lorong.mp3" fadein 1.0
    scene lorong with dissolve
    $ quick_menu = True
    "Selagi Kana mengerjakan UTS susulan, [mcname] menyarankan untuk melakukan perayaan dalam rangka merayakan selesainya UTS dan kesembuhan Kana."
    show freya at char_center with dissolve
    show freya_side at left with dissolve
    freya "Hmmm. Kalo nanti mau makan-makan, gak? Ngerayain kesehatan Kana sama selesainya UTS."
    hide freya_side at left with dissolve
    mcname "Weh, boleh tuh! Hmmm kalau kita ngerayain di cafe gimana?"
    show freya_side at left with dissolve
    freya "Eh seru juga tuh, cocok nih nanti kita mau rayain gmn?" 
    hide freya_side at left with dissolve
    mcname "Eh gimana kalau beli cake gitu? Kana kan suka cake tuh."
    show freya_side at left with dissolve
    freya "Ide bagus tuh! Cocok banget, Si Naya suka strawberry cake sih."
    hide freya_side at left with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Cafe Cerah.mp3" fadein 1.0
    scene cafe with dissolve
    $ renpy.block_rollback()
    show kana at char_right with dissolve
    show freya at char_left with dissolve
    $ quick_menu = True
    mcname "Sekali lagi, SELAMAT KANAAAAA!!!! "
    show freya_side at left with dissolve
    freya "Selamat yah, udah namatin UTS kali ini. Meski susulan, setidaknya kamu berhasil. Lain kali jangan sakit lagi ya."
    hide freya_side at left with dissolve
    show kana_side at left with dissolve
    kana "Eeeehh. Makasihh Freey, [mcname], hehehe. Maaf ya udah banyak repotin kalian semua dan maaf juga udah bikin kalian panik."
    hide kana_side at left with dissolve
    show freya_side at left with dissolve
    freya "Santai Nayyy. Lagian kan yang paling dibikin repot tuh..."
    hide freya_side at left with dissolve
    "Tanpa melanjutkan perkataannya, Freya melirik ke arah [mcname] seakan memberi kode."
    hide kana at char_right with dissolve
    show kana_shy at char_right with dissolve
    show kana_side_shy at left with dissolve
    kana "Eh... Ummm i-iya... Makasih banyak ya [mcname]."
    hide kana_side_shy at left with dissolve
    mcname "E-eh...\n*Blush*"
    mcname "K-kalau buat Kana siiih..."
    show kana_side_shy at left with dissolve
    kana "*Blush*"
    hide kana_side_shy at left with dissolve
    mcname "{i}Kalo buat kamu mah, aku mendaki gunung lewati lembah pun rela Kanaaa.{/i}" 
    "Suasana menjadi canggung, saking canggungnya suara jangkrik pun terdengar untuk beberapa saat hingga Freya membuka obrolan baru." 
    show freya_side at left with dissolve
    freya "Ah elah kok pada baper gini sih. Kan ini lagi perayaan sembuh dan selesainya UTS KEMATIAN ITU AHAHAHAH!!!"
    hide freya_side at left with dissolve
    hide kana_shy at char_right with dissolve
    show kana at char_right with dissolve
    mcname "Seneng banget kamu."
    show kana_side at left with dissolve
    kana "Iya nih, emang ada beberapa yang susah sih, tapi untungnya aku bisa lah."
    hide kana_side at left with dissolve
    mcname "Yaudah, untuk kita semua yang udah lewatin UTS pertamaaaa. CHEERRSS!!!"
    show kana_side at left with dissolve
    kana "CHEERSS!!"
    hide kana_side at left with dissolve
    show freya_side at left with dissolve
    freya "CHEERSS!!"
    hide freya_side at left with dissolve
    "Obrolan mereka pun kembali berlanjut, perayaan Kana sembuh dan selesai UTS. Meski hanya dihadiri 3 orang akan tetapi suasana yang ada tetap terasa hidup, ramai, dan penuh keceriaan."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with dissolve
    show text "{color=#FFF}CHAPTER III{/color}" with Pause(2.0)
    play music "audio/BGM_MC Pertama Kali ke JKT + BG Pagi.mp3" fadein 1.0
    scene awan with dissolve
    $ quick_menu = True
    "Jarak antara Kana dan [mcname] semakin dekat, hampir setiap hari mereka menghabiskan waktu makan siang bersama sama dan terkadang ditemani oleh Freya juga."
    "Hari ini pun sama seperti biasanya, [mcname] dan Kana janjian untuk makan siang bersama di kantin."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with dissolve
    play music "audio/BGM_Lorong.mp3" fadein 1.0
    scene lorong with dissolve
    $ quick_menu = True
    mcname "{i}Aduhh, telat nihh, pake mules segala.{/i}"
    "Saat tergesa-gesa, pandangan [mcname] tiba-tiba teralihkan dengan sebuah flyer yang menempel di papan pengumuman."
    #SHOW PAPAN PENGUMUMAN FLYER
    mcname "{i}Eh apa ini?{/i}"
    mcname "{i}Hmmm ternyata bentar lagi bakal ada acara jejepangan di kampus ini.{/i}"
    mcname "{i}Ehh ini kan flyer yang waktu itu pernah dikasih sama cewek rambut merah ya?{/i}"
    mcname "Hmmmmm... \"Dicari anggota untuk group idol cewek\"."
    mcname "{i}Kayaknya cocok deh buat Kana.{/i}"
    menu:
        "Yang [mcname] lakukan..."
        "Ambil flyer event jejepangan.":
            mcname "{i}Ehhh tapi udah kelamaan ini, ga enak sama Kana nunggu lama.{/i}"
            "[mcname] pun memilih untuk mengabaikan flyer tersebut, lalu lari agar bisa datang tepat waktu."
            jump truekana
        "Ambil flyer \"Dicari Anggota Klub Jepang\".":
            jump goodkana