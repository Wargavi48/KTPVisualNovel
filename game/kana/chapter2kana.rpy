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
    mcname "Rame juga ya ternyata mall di Jakarta ini."
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
    papah "Ohhh, itu namanya cosplay."
    mcname "Memangnya cosplay itu apa?"
    mama "Cosplay itu costume play. Biasanya dipake sama orang yang suka anime, buat di event atau lomba gitu."
    papah "Kalo Papah sama Mamah biasanya buat malam-malam, hehe."
    mama "Huss jangan ajarin yang aneh-aneh. [mcname] masih kecil."
    papah "Ahahaha. Gapapa, like father like son."
    mama "Udah ihhh."
    papah "Jadi pengen nanti malam, hehe."
    mama "*Blush*"
    "{i}Saat itu aku gak begitu paham dengan apa yang mereka bicarakan...{/i}"
    stop music fadeout 1.0
    #*balik dari flashback”
    #BGM Rumah STOP
    #BG Kamar [mcname] STOP
    #*Transisi Screen Putih 2s*
    #BG Mall Start
    #BGM Mall Start
    $ quick_menu = False
    scene white with Dissolve(2.0)
    # Harusnya ada frame putih atas bawah
    scene mall temp with dissolve
    play music "audio/BGM)Mall Slow.mp3" loop fadein 1.0
    $ quick_menu = True
    mcname "{i}Kalo ada orang yang cosplay, berarti ada event yang sedang berlangsung di mall ini.{/i}"
    mcname "{i}Gak ada salahnya nanti aku mampir sebentar ke sana.{/i}"
    "[mcname] kemudian berkeliling mall untuk melihat-lihat di mall, sampai akhirnya ia sampai ke event jejepangan di mall tersebut."
    mcname "Waaah banyak juga ternyata orang-orang di sini."
    mcname "Kalau papah di sini mungkin bakal kesenengan tuh, hahaha."
    "[mcname] pun mencoba berkeliling melihat-lihat apa saja yang ada di event tersebut."
    "Di dalam event terlihat banyak booth-booth yang dibuka, mulai seperti mencoba kuliner yang ada di sana, melihat merch-merch event, bahkan [mcname] juga foto bersama cosplayer."
    "Tiba-tiba..."
    #*BRUKKK*
    play audio "audio/tabrakan.mp3"
    "Sepertinya [mcname] tidak sengaja menabrak seseorang saat berjalan."
    mcname "Waduh maaf kamu gapapa?"
    "[mcname] mencoba mengulurkan tangannya."
    "???" "Ah iya, aku gapapa."
    "Seakan terkejut melihat [mcname], orang tersebut langsung berdiri tergesa-gesa."
    "???" "Ah, m-maaf!"
    "Setelah mengatakan hal tersebut, orang tadi langsung berlari pergi."
    mcname "......."
    mcname "Buru-buru banget itu orang."
    mcname "{i}Hmmm... Mungkin ada merch yang dia pengen, jadi kayak gitu.{/i}"
    mcname "Jadi ngingetin kayak papah dulu, haha."
    mcname "Hmm..?"
    "[mcname] menyadari ada sesuatu yang jatuh."
    "SHOW ASSET GANTUNGAN KUNCI."
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
            "[mcname] pun memilih untuk menitipkan barang tersebut ke pada panitia yang bertugas"
            "Ahirnya panitia pun membuat pengumuman adanya barang hilang."
    #*SKIP TO SCENE*
    #*BG KELAS PAGI*
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}KEESOKAN HARINYA{/color}" with Pause(2.0)
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    scene kelas with dissolve
    $ quick_menu = True
    "Di kelas Jeketi University, terlihat banyak mahasiswa melakukan aktivitasnya."
    mcname "Haduuhh, barangnya gimana ya..."
    kana "Barang? Barang apaan? Memangnya kamu pesen online [mcname]?"
    mcname "Ah enggak, jadi kemarin ada event jejepangan di mall pas aku lagi jalan-jalan."
    mcname "Di sana gak sengaja tuh aku ketabrak sama orang."
    freya "Ehhh kamunya gapapa tuh?"
    kana "Ah iya, kamunya gapapa?"
    mcname "Gapapa kok."
    mcname "Nah, orang itu gak sengaja jatuhin barang yang dia bawa. Merch limited dari Utaite yang terkenal itu, loh."
    freya "Ehhh, merchnya Utaite yang terkenal itu..."
    "Freya berkata sambil melirik Kana."
    mcname "Aku ga paham sama orang-orang yang suka begituan."
    mcname "Kayak Papahku itu, agak aneh emang."
    kana "Ahahah\n*Tertawa karir*"
    kana "Emang aneh ya, haha."
    stop music fadeout 1.0
    $ quick_menu=False
    scene black with dissolve
    scene kelas with dissolve
    $ quick_menu=True
    play music "audio/BGM_Dosen + Rektor.mp3" fadein 1.0
    "Tidak lama kemudian, dosen pun masuk ke dalam kelas dan waktu mata kuliah pun dimulai."
    show dosen at dosen_center with dissolve
    dosen "Teman-teman, mari kita mulai perkuliahan hari ini."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    scene kelas with dissolve
    $ quick_menu = True
    mcname "Wahh akhirnya selesai juga."
    kana "Kalo gini enaknya ke kantin sih."
    mcname "Aduh, tapi jam segini kantin pasti penuh."
    freya "Hmmm. Gimana kalo bawa makanan dari kantin ke rooftop? Denger-denger tempatnya enak."
    kana "Ehhh, boleh tuh. Tapi jangan makanan berat, nanti ribet bawanya."
    mcname "Yaudah aku ke kantin ya. Sekalian aku beliin makanan buat kalian."
    kana "Okee. Aku sama Freya nunggu di rooftop, ya."
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
    $ quick_menu = True
    "Sesampainya di rooftop, [mcname] hanya melihat Kana yang memandang langit sendirian."
    mcname "Loh, sendirian Kana? Freya mana?"
    kana "Freya tadi mendadak ada urusan. Jadinya dia pulang duluan."
    mcname "Heeee"
    kana "Aku udah chat, tapi keknya gak kebaca sama kamu ya."
    "[mcname] kemudian membuka HPnya."
    "Di sana terlihat banyak notif chat dari Kana dan Freya."
    mcname "Ah iya, sorry banget. Tadi di kantin rame banget, jadi gak kebaca."
    kana "Yaudah. Yuk kita duduk makan dulu."
    mcname "Oke."
    scene black with dissolve
    scene rooftop with dissolve
    mcname "Kamu mau yang cokelat, strawberry, atau keju?"
    kana "Kayaknya aku yang strawberry aja deh."
    "Setelah memberikan Kana roti yang dia pilih, akhirnya [mcname] dan Kana duduk di bangku yang ada di rooftop."
    "Di sana, Kana dan [mcname] menikmati roti sambil memandangi langit biru. Mereka tidak mengeluarkan sepatah kata pun. Suasana hening menjadi terasa sedikit canggung."
    mcname "{i}Duh bingung mau ngomong apaan. Biasanya Freya yang mulai obrolan.{/i}"
    "Ingin mencairkan suasana, [mcname] mencoba memulai percakapan."
    mcname "A-"
    kana "Kamu kabarnya gimana?"
    "Sebelum [mcname] sempat berbicara, Kana tiba-tiba memberikan pertanyaan."
    mcname "E-eeh?"
    kana "Kamu udah makan, belum?"
    mcname "?????"
    mcname "Kan kita lagi makan, Kana..."
    kana "Ah i-iya yah. Hahaha ngomong apa sih aku."
    "Setelah Kana mengatakan hal tersebut, suasananya kembali menjadi hening."
    kana "Biasanya ada Freya ya, yang ngomong mulu."
    mcname "Haha, iya yah."
    kana "Haha."
    mcname "Haha."
    kana "Fufu."
    mcname "Dilihat-lihat kamu emang deket banget ya sama Freya."
    kana "Iya. Dari kecil, emang Freya selalu bareng aku."
    mcname "....."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Rooftop Romance Pia.mp3" fadein 1.0
    #HARUSNYA LAGU SAD KANA
    scene awan with dissolve
    $ quick_menu = True
    kana "Dulu…"
    "Kana menatap ke atas langit seakan mengingat masa lalu."
    "CG Chibi Kana Freya"
    kana "Dulu badanku lemah dan sering sakit, jadinya jarang keluar rumah."
    kana "Waktu yang lain pada main di luar, aku cuma bisa liat mereka dari jendela kamarku."
    kana "Untungnya waktu itu Freya ada dan mau main bareng aku."
    kana "Padahal bisa aja dia main sama anak-anak yang lain, tapi dia malah nemenin aku."
    kana "Jadinya sampe sekarang bareng terus deh aku sama Freya, haha."
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
    freya "Halooooo, sorry. Lama nungguin, ya?"
    kana "Ah! Freyaa."
    mcname "Nggak kok."
    kana "Ayok sini makan."
    freya "Okeee~"
    "Mereka pun menghabiskan waktu dengan berbincang dan makan bersama..."
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}KEESOKAN HARINYA{/color}" with Pause(2.0)
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    scene kelas with dissolve
    $ quick_menu = True
    kana "[mcname]! Freya! Eh liat ini! Lucu banget gak sih? Kemarin aku liat di internet."
    mcname "Hooo aku pernah liat ada toko yang jual boneka ini nih, waktu ke mall kemarin."
    kana "Heee serius? Habis ini kalian free, kan? Yuk ke sana bareng!"
    freya "Ayoook. Aku juga free, sih."
    kana "[mcname] nanti ikut yak, soalnya kamu kan yang tau tempatnya."
    mcname "Bolehh."
    #Narator
    "Dosen pun datang memasuki ruangan kelas."
    
    dosen "Selamat pagi. Pelajaran akan dimulai."
    
    #*Skip Scene*
    
    dosen "Yak. Mata kuliah ini sudah sampai sini dulu. Selanjutnya kalian review masing-masing, ya."
    
    "Para mahasiswa pun mulai merapikan barangnya, bersiap untuk pulang"
    
    kana "Akhirnya selesai juga."
    
    mcname "Jadi? Masih mau ke sana?"
    
    kana "Iya dong"
    
    dosen "Ah iya Freya. Untuk pembahasan kemarin, Ibu tunggu di ruangan Ibu sekarang, ya."
    
    #Freya “Ehhh……”
    #Freya “Baik, Bu.”
    
    "Setelah mendengar hal tersebut, bu dosen pun pergi meninggalkan ruang kelas"
    
    
    #Freya “Yahhh, sorry guys. Kayaknya aku gak bisa ikut nemenin kalian.”
    
    kana "Yahhhh…"
    
    #Freya “Gapapa kok. Kan ada [mcname].”
    #Freya “[mcname]! Kamu jagain Kana, ya.”
    #
    kana "E.. eeeeh"

    #Narator
    "Freya pun menyusul Dosen. Meninggalkan Kana dan [mcname] berdua"

    mcname "Yaudah, yuk."

    kana "I-iya."

    #*Skip Scene*
    #BG Mall
    #BGM Mall

    #Narator
    "Kana dan [mcname] mendatangi Mall yang dimaksud."

    kana "Kamu sering ke mall ini, ya?"

    mcname "Nggak juga, kok. Kemarin kebetulan aja inget."
    mcname "Kalo kamu?"

    kana "Aku biasanya di rumah aja, sih."

    mcname "Weh. Kalo gitu mau coba sekalian jalan-jalan? Mumpung kamu di sini."

    kana "Ehhh, tapi kamu gapapa kah?"

    mcname "Gapapa, kok. Lagi free juga, hehe."

    #Narator
    "Mereka kemudian berjalan bersama sambil berbincang masalah kuliah"

    "Namun saat membahas topik pembicaraan, Kana tidak merespon sehingga [mcname] mencoba untuk menengok ke arah Kana"

    mcname "{i}Loh, Kana ke mana?{/i}"

    #Narator
    "[mcname] pun melihat ke belakang. Di sana terlihat Kana sedang menatap salah satu baju yang dipajang di mall."

    #*Asset Baju Kana yg dipajang*

    mcname "Eh, Kana? Ada apa?"

    kana "..."

    mcname "Kana? Nanti ketinggalan lohhh."

    kana "Ah! Iya."
    "Kana kemudian menghampiri [mcname]"
    kana "BTW, di mana tempat yang jual bonekanya, [mcname]?"

    #*Skip Scene*

    #Pelayan Toko "Maaf Kak. Sepertinya boneka yang Kakak cari itu udh habis stock yang Ready"
    #Pelayan Toko "Kalo mau bisa pre-order, tapi nunggunya sekitar 90 hari"

    mcname "{i}Wah, lama banget. Seperti waktu Papah mau PO merch idol group kesukaannya.{/i}"

    kana "Yahhhh, gimana nih? Kalo PO kayaknya lama banget"

    mcname "Gimana kalo kita jalan, liat-liat yang lain dulu. Siapa tau ada barang lucu lainnya."

    kana "Oke deh"
    "Namun muka Kana terlihat sedikit kecewa"

    "Kana dan [mcname] pun kembali berjalan berkeliling di mall."

    mcname "{i}Sepertinya Kana masih kecewa dengan kejadian tadi{/i}"

    mcname "Kana, Gimana kalo kita ke game center aja?"

    kana "..."

    mcname "Kanaa?"

    kana "Hmmmm? Eh maaf kurang fokus tadi, hahaha"

    mcname "Ya udaah. Ayok ikut aku sini."

    kana "Eeeh? Emangnya mau ke mana?"

    mcname "Udaaah, ikut aja."

    #*Skip scene*

    "MC dan Kana sampai di game center"
    #BGM Game Center (Idol, Robot)

    kana "Heeee? Di sini ada game center ternyata."

    mcname "Mau nyoba game di sini, Kana? Aku lumayan pede loh sama skill Racing aku."

    kana "Bolehhh siapa takut"

    #(.....)

    #*SFX BERMAIN RACING GAME*
    #BGM Game Center + Sound Effect Racing Car

    kana "Liat nih skill Racing aku."

    mcname "Wih jago juga kamu. Udah rank 1 aja."

    kana "Hehe. Kan namaku Kanaia “Resing” Asa."

    #(.....)

    #BGM Game Center + Sound Effect Racing Car + Sound Effect Car Crash

    kana "Eh? Eh? Kok aku ditabrak mulu. Waaaaaa"

    mcname "Eh, gimana ini Kana? Sekarang malah aku yang di depan. Hehe"

    kana "Arrgh. Liat aja nanti."

    #(.....)

    #BGM Game Center + Sound Effect Racing Car

    mcname "Weh aku udah di lap terakhir, nih!"

    #BGM Game Center + Sound Effect Racing Car + Sound Effect Car Crash

    kana "Noooo. Aku nabrak mulu."

    mcname "Inget rem, Kana. Hahahaha."

    kana "Ahhhhh. Jangan tabrak akuuu."

    #(.....)

    mcname "Hahaha gimana nih Kana. Malah aku yang Rank 1"

    #BGM Racing Car STOP

    kana "Sekali lagi laahh, aku masih gak terima."

    "Akhirnya mereka memainkan game tersebut berkali kali."

    #BGM Racing Car START

    #*Skip Scene*

    kana "Hahaha gimana aku, hebat kan bisa Rank 1?"

    mcname "Tapi kan kamu tadi kalah mulu"

    kana "Hmph. Yang penting game terakhir aku menang."

    mcname "Hahaha. Iya kamu jago banget."
    mcname "Gimana? Mau racing lagi?"

    kana "Nggak, ah. Kita ganti game. The last winner wins. Hehe."

    #Narrator
    "Selanjutnya Kana mengajak [mcname] main game Whack-a-mole"

    kana "Aku jago banget kalo mukul-mukul gini."

    mcname "Iya iyaa."

    #SFX 3 2 1 Go…
    #SFX WHACK

    kana "Aduhh banyak yang miss."

    mcname "Ayokk semangat Kanaa."

    kana "Waaaa."

    mcname "Itu yang itu, Kana."

    kana "Ah, kamu backseat muluu."

    mcname "Geregetan soalnyaa."

    #SFX Game beres

    kana "Fiuhh… akhirnya."

    #Narrator
    "Setelah waktunya habis, Kana melihat papan high score"

    kana "Waaah! [mcname] liat! [mcname]! Highest score! Yeayy!"

    mcname "Gils jago bangettz."

    kana "Hehe"

    mcname "Gimana?"

    kana "Haha kayaknya udh cukup ya, soalnya udh lumayan lama kita disini"

    #Narrator
    "Saat [mcname] dan Kana mau pulang, tidak sengaja [mcname] melihat ada boneka yang diinginkan Kana di dalam box Push Claw Machine."

    mcname "Eh. Itu kan boneka yang kamu pengen?"

    kana "Eh, mana? Mana?"

    mcname "Ituuu, di kanan mu."
    "[mcname] menunjuk ke arah crane game"

    kana "Wahhh,crane game ya?"

    mcname "Heee kamu tau crane game Kana"

    kana "Mhm… kalo main gak pernah sih, tapi aku sering denger nya"

    mcname "Mau coba mainin?"

    kana "Bisaa"

    #*CG Chibi Kana Claw Machine*

    #SFX 3 2 1 Go…

    #Narrator
    "Kana mencoba game crane tersebut."
    "Setelah memperkirakan lokasi yang tepat, akhirnya Kana menekan tombol claw."
    "Claw-nya kemudian turun dan menangkap boneka yang diinginkan Kana"
    "Boneka tersebut terangkat sedikit sebelum akhirnya kembali seperti semula."

    mcname "Yaahh~ sayang banget"

    kana "Nooooo"
    kana "Baiklah, Sekali lagi."

    mcname "Ayo coba lagi"
    mcname "Bentar, ku masukin koin nya lagi"

    #SFX 3 2 1 Go…
    "Kana mencoba lagi, tetapi hasilnya tetap sama."

    kana "Huhu. Ternyata gamenya lumayan susah."

    mcname "Sini aku bantuin."

    kana "Wihh. Okeee. Kali ini pasti bisa!"

    #SFX 3 2 1 Go…
    #*CG Chibi Kana Claw Machine (With MC)*

    kana "Gimana? Udah pas belum?"

    mcname "Maju dikit lagi tuh"

    kana "Gimana kalo sekarang?"

    mcname "Ke kanan dikittt."

    kana "Gini?"

    mcname "Oke sekarang!!"

    "Kana akhirnya menekan tombol claw"

    kana "Please, pleasee."

    #SFX Game Clear
    "Terdengar suara boneka jatuh ke kotak hadiah."

    kana "YAAAAAYYY."

    "Kana kemudian mengambil boneka tersebut dari kotak hadiah dan langsung memeluknya. [mcname] melihat pemandangan tersebut sambil tersenyum kecil."

    kana "Hehe makasih banyak ya, [mcname]. Karena kamu ngebantu arahin, jadi bisa dapet boneka ini"

    mcname "Haha gk papa kok, aku seneng juga akhirnya kamu dapet boneka yang kamu pengen"

    #*Skip Scene*
    #BG LANGIT

    "Sepulang dari game arcade"
    "Kana membawa tas belanja dia dan juga boneka yang dia dapat dari claw machine tadi, mukanya terlihat senang"

    kana "Makasih ya [mcname] untuk hari ini"

    mcname "Iya sama-sama Kana"

    kana "Hari ini aku senang banget"

    "Melihat kana tersenyum membuat [mcname] tersenyum juga"

    #*Transisi putih*
    #BG LANGIT

    "Besoknya di kampus"
    "Suasananya sama seperti hari-hari sebelumnya"

    #BG Kelas
    #BGM Kelas

    kana "Pagii [mcname]."

    mcname "Pagi juga."

    kana "Gimana kabarnya hari ini?"

    mcname "Baik. Gimana kemarin pulangnya? Aman gak?"

    kana "Aman kok. Bareng supir soalnya hehe."

    mcname "Wih enak ya punya supir."

    kana "Nanti kapan-kapan kamu mau kan nemenin aku lagi?"
    kana "Nanti pulangnya dianter deh."

    mcname "Wahh. Okee."

    #Narator
    "Saat Kana dan [mcname] sibuk berbincang, Freya datang menghampiri."

    freya "Pagi Kanaa. Pagi [mcname]"
    
    freya "Eh gimana kemarin kalian ngedatenya? Hehehe."
    
    kana "Iiihhh ngedate apaan."
    kana "Yang ninggalin kita kan kamu"
    
    "Kana mengatakan hal tersebut sambil tesipu malu"

    mcname "....."
    
    freya "Hmmm?????"
    "Freya merasakan respons Kana sedikit berbeda dari biasanya"
    
    freya "Seee too… ki wes ra bener ki felling ku mengatakan ada yang mencurigakan."
    
    kana "Apaan sihhh, ga da yang mecurigakan ko"
    
    freya "Yang bener????"
    
    kana "Apaan sihhh ahh Freya, aku malu tau diliatin gitu mulu "
    
    freya "hmmmmm…"
    
    "Suara pintu pun terdengar dan dosen pun datang dengan buru buru berbeda dari biasanya"
    
    kana "Nah Bu dosen udah dateng tuh, nanti lanjut ngobrol lagi ya"
    
    "Mendengar hal tersebut, mereka akhirnya duduk di tempat masing-masing"
    "Disaat duduk [mcname] di tempatnya, [mcname] mendengar sedikit percakapan antara Kana dan Freya"
    
    freya "Ceritain ya, kalian berdua ngapain aja kemarin"
    
    kana "Iya deh iya"
    
    #(.......)
    
    dosen "Baiklah semuanya, ibu hari ini akan mengajar dengan cepat karena ada rapat mendadak, jadi harap perhatikan dengan baik dan nantinya akan ada tugas dari ibu"
    
    #*Skip Scene*
    
    "Dosen pun menjelaskan dan memberikan tugasnya kepada mahasiswa/i semuanya.."
    
    mcname "Tumben juga kali ini cepet kelasnya"
    mcname "Jadi ada waktu free gini "
    "MC melakukan peregangan badan karena lumayan lama telah duduk"
    mcname "Tapi tugas yang dikasih juga lumayan banyak"
    
    kana "iya banyak banget ya tugasnya…"
    
    kana "Jadi buat tugas ini kamu mau ngerjain bareng ga?"
    
    mcname "Eh bisa kok"
    
    "MC bingung tiba-tiba kana langsung mengajak [mcname] untuk mengerjakan tugas, yang mana tidak biasanya"
    
    mcname "Tapi Freya gimana?"
    
    freya "Kalo aku kayaknya bakal besok aja ngerjainnya"
    freya "Soalnya lagi ada barang promo yang mau ku cari"
    freya "Sekalian biar kalian bisa barengan hahaha"
    freya "Byeeeee"
    "Setelah mengatakan hal tersebut Freya langsung pergi meninggalkan kelas"
    
    kana "Apaan sih Freya itu, kan niatnya cuma belajar bareng"
    
    mcname "Ahahaha"
    "[mcname] hanya bisa tertawa canggung mendengar hal tersebut"
    
    kana "Jadi [mcname]"
    "Kana melihat [mcname]"
    
    kana "kita ngerjain tugasnya mau dimana?"
    #*CHOSE*
    menu:
        "Kantin":
            #*IF CHOSE A*
            
            #mcname "Hmmmm di kantin gimana?"
            #mcname "Soalnya juga bisa sambil ngemil"
            
            kana "Okeee"
            
            #*BG Kantin
            
            #Narator
            "[mcname] dan Kana sampai di kantin."
            "Di kantin terlihat sudah dipenuhi orang sehingga tidak ada tempat kosong untuk duduk."
            
            mcname "Kayaknya kantin penuh terus yak"
            
            kana "Haha iya nih"
            kana "Jadinya mau gimana?"
            
        "Rooftop":
            #*IF CHOOSE B*
            
            mcname "Hmmmm mau ke rooftop lagi? Kayaknya disana bakal sepi"
            
            kana "Aku ngikut kamu aja"
            
            mcname "O- Oke"
            mcname "Kalau gitu kana mau nitip apa? Biar nanti aku bawain"
            
            kana "Eh kalo [mcname] gimana?"
            
            
            mcname "kamu duluan aja"
            "[mcname] mengatakan hal tersebut karena tidak ingin membuat Kana terlalu lama menunggu"
            
            kana "Oke deh, kalau gitu aku Roti Strawberry ya"
            
            mcname "Siapppp"
            
            "Setelah mengatakan hal tersebut Kana akhirnya pergi duluan ke Rooftop"
            
            mcname "Hufft"
            mcname "Sebaiknya aku pesen dulu yang dipesen Kana"
            
            "[mcname] kemudian berjalan menuju kasir"
            
            "Disana [mcname] mendengarkan beberapa mahasiswa membicarakan masalah event kampus yang akan segera diadakan"
            
            #Mahasiswa A "Eh Katanya event Kampus nanti bakal ada lomba-lomba pertunjukan"
            
            #Mahasiswa B "Serius, emang ada hadiahnya?"
            
            #Mahasiswa A "Buat hadiahnya kurang tahu sih"
            #Mahasiswa A "Tapi guest star nya nanti katanya sih Sabi Yoi"
            
            #Mahasiswa B "Duh Sabi Yoi, agak bosen sih dengernya tapi gak papa lah"
            
            mcname "Heee menarik juga itu"
            
            #*Skip Scene*
            #*BG Rooftop*
            
            "Selangkah demi selangkah [mcname] menanjaki anak tangga menuju rooftop."
            "Di tangannya ada 2 roti untuk menemani mereka saat mengerjakan tugas nanti." 
            "Saat sampai di disana, Terlihat Kana sudah menunggu [mcname]"
            
            "Menyadari keberadaan [mcname], Kana memanggil [mcname] sambil tersenyum"
            
            kana "Ah [mcname]"
            
            mcname "Maaf ya, bikin nunggu"
            
            "MC dan Kana kemudian makan bersama sambil mengerjakan tugas."
            "Sesekali terdengar canda tawa kecil di pembicaraan mereka."
            
            mcname "Fuuu kayaknya kita istirahat dulu sebentar, soalnya sudah lumayan lama kita ngerjain tugas"
            
            kana "Iya nih, udh lumayan mumet juga"
            
            mcname "Oh iya, denger-denger katanya kampus kita nanti bakal ada event buat ulang tahun kampus nanti"
            
            kana "Ehhh serius…"
            kana "Gak sabar jadinya hehe"
            "Kana terlihat sangat bersemangat, seperti sangat menantikan hal tersebut"
            mcname "Kayaknya kamu suka ya sama event-event kek gitu"
            mcname "sering ke event?"
            
            kana "E-eh"
            "Kana agak terkejut"
            kana "Enggak"
            kana "Soalnya kan dulu waktu aku kecil aku sering sakit, pas ada acara-acara kek gitu aku gk bisa ikut dan cuma dirumah aja"
            kana "Jadi pas ada event-event kek gitu aku suka sama suasananya yang meriah gitu"
            
            mcname "Heeeee"
            mcname "{i}Iya sih kana waktu dulu sering sakit ya….{/i}"
            mcname "Moga aja eventnya nanti berjalan lancar"
    
    #*SKIP TO SCENE*
    #*DEPAN KAMPUS PAGI*
    "Suasana jalan di kampus lebih terasa lebih ramai daripada biasanya"
    "Banyak orang-orang yang sedang lalu lalang dan menyerahkan beberapa flyer yang entah isinya apa."
    "Bahkan ada yang memaksa beberapa  mahasiswa/i untuk menerima flyer tersebut."
    
    mcname "Ehh hari ini kok ramai banget ya? Ga kaya biasanya, lagi ada acara kah ?"
    
    kana "Aduh aku juga ga tauu. Event kampus yang kamu bilang kemarin masih lama, kan?"
    
    "Saat Kana dan [mcname] berjalan bersama menuju kelas, tiba-tiba seseorang datang mendekat." 
    
    #???( TONO ) "Ehhhh brooo bentarr duluuu"
    
    "Terlihat seorang cewek tinggi dengan perawakan tomboy berambut pendek merah yang mengingatkan [mcname] kepada CABE KERING yang sering mamanya jemur di desa."

    "Kana dan [mcname] merasa bingung karena tiba-tiba dihentikan cewek tersebut." 
    
    "Sepertinya sadar dengan orang tersebut, tiba-tiba Kana bersembunyi di belakang [mcname] sambil mencoba menghindar dari tatapan cewek itu." 
    
    mcname "Uumm kenapa ya, Kak?"
    
    #???( TONO ) "Bentar dah, keknya gue pernah liat lu di event-event dah"
    
    mcname "Gue?" 
    "Sambil terheran heran, [mcname] menunjuk dirinya sendiri dan bertanya apakah dia adalah orang yang cewek itu maksud."
    
    #?? (Tono ) "Ahhhh bukan kocak, dia loh"
    "Jari cewek itu menunjuk ke arah belakang [mcname]"
    
    "Saat itu pun Kana mulai gelisah dan menundukkan kepalanya, mencoba menyembunyikan wajahnya dari cewek tersebut."
    
    mcname "Hah? Kana?"
    
    kana "Ehh… uuu k-kenapa ya mba?"
    "Dengan ragu dan perlahan Kana pun melihat ke arah cewek itu"
    
    #???(TONO) "Nahhhh kan benerrr feeling gw tuh. Elu kan yang sering datang ke event jejepangan."
    
    kana "Ehhh, s-salah orang kali. Hahaha"
    
    #???(TONO) "Aahh, ga pernah salah kalau gue mah kocak. Tiap gue ke event jejepangan, keknya selalu ngeliat lu."
    
    mcname "Eh? Kamu sering ke event jejepangan, Kana?"
    
    kana "Haa..masa sih? A-aku ga pernah ikut kaya gituan kok… Aku kan bukan wibu."
    
    tana "Ah masa sih. Kamu kan yang biasanya wotagei paling semangat di event-event jejepangan?"
    
    kana "Ah eh ah eh."
    "Kana pun kabur secepat mungkin, tidak peduli dengan orang yang ada di sekitar."
    
    #???(TONO) "Lah, itu orang napa malah kabur dah. Ya udah ini buat lu aja."
    "Cewek tersebut memberikan flyer ke arah [mcname] dan pergi dari tempat tersebut"
    
    #*SKIP TO SCENE*
    #*KELAS SORE*
    "Tingkah laku Kana tadi pagi masih menjadi tanda tanya yang besar di dalam pikiran [mcname]. Hal ini membuat [mcname] tidak fokus dengan kelas dan melamun sendiri."
    
    mcname "Hmmmmm…. Kana ke mana, ya? Padahal tadi pagi ada… Apa jangan-jangan karena kejadian tadi pagi?"
    
    "Saat memikirkan kejadian pagi tadi, Tiba-tiba ada seseorang yang membuyarkan pikirannya"
    
    #??? "Eh ngapain [mcname], dari tadi asik sendiri."
    
    mcname "Ah? Freya?"
    
    freya "Iya. Btw Kana mana? Tadi pagi kan harusnya bareng kamu."
    
    mcname "Iya tadi pagi kami barengan. Tapi Kana tiba-tiba kabur setelah dikasih flyer ini"
    
    "MC kemudian menunjukkan flyernya kepada Freya."
    
    freya "............."
    "Freya membaca flyer yang diberikan [mcname]"
    
    mcname "Denger denger, emangnya Kana wibu?"
    
    freya "Heeee? Aku kira Naya udah cerita."
    
    mcname "Emang cerita apa?"
    
    freya "Hmmm"
    freya "Ga jadi deh."
    "Seolah tidak ingin membahasnya Freya menghentikan topik tersebut"
    
    "MC semakin kebingungan dengan semua kejadian di hari itu."
    
    #*SKIP TO SCENE*
    #*BG KOS*
    
    "Malamnya setelah pulang dari kampus [mcname] langsung merebahkan diri di kasurnya tanpa berganti pakaian"
    
    mcname "Haaaahhhhh"
    mcname "Hari ini terasa sangat panjang"
    
    "Kepikiran tentang Kana yang tidak masuk kelas hari ini,"
    "Akhirnya [mcname] mencoba menghubungi Kana lewat chat."
    
    mcname "Hmmm Kana ke mana yah?"
    
    "MC kemudian membuka HP nya"
    
    #Mobile Phone
    
    mcname "Kana, kamu gapapa?"
    
    #(......)
    "Tidak ada respon dari Kana"
    
    mcname "*Emoji Mengsedih yg Papah*"
    
    #*Balik BG Kamar*
    
    mcname "Hmmm gak dibales"
    mcname "Semoga besok pagi Kana masuk ke kampus deh."
    
    "Setelah itu [mcname] menutup matanya dan langsung tidur"
    
    #*Skip Scene*
    #BG Langit Pagi
    #BG Kelas
    
    "Pagi itu kelas terlihat ramai oleh mahasiswa"
    "namun Kanaia Asa tidak terlihat di mana pun"
    
    mcname "Kayaknya hari ini Kana gak masuk juga ya"
    "[mcname] mencoba melihat sekitar namun tetap saja hasilnya nihil"
    mcname "Mungkin ku coba tanyakan ke Freya nanti"
    
    "Pintu terbuka dan terlihat dosen memasuki kelas"
    
    dosen "Baiklah anak-anak mari kita mulai kelas hari ini"
    
    #*Skip Scene*
    #Transisi Putih
    
    dosen "Oke terima kasih untuk hari ini, jangan lupa untuk selalu jaga kesehatan ya"
    
    mcname "Oke bu dosen sudah keluar"
    mcname "Mungkin ku coba tanyakan ke Freya masalah Kana"
    
    "[mcname] pun kemudian mendekati Freya"
    
    mcname "Freya kamu tau gak Kana gimana?"
    mcname "Soalnya udah dua hari ini gak masuk kelas"
    mcname "Aku chat juga gak dibales"
    
    freya "Iya nih, aku juga gak dikabarin sama sekali sama dia"
    
    mcname "Duh jadi gimana ya ini, aku agak khawatir"
    
    freya "Mungkin nanti ku coba datengin ke rumahnya nih, kali aja dia kenapa-napa"
    
    mcname "Oke deh Freya, Tolong banget ya"
    
    #*Transisi putih*
    #BG Kampus
    
    mcname "{i}Duh kata Freya nanti dia bakal kerumah Kana buat mastiin kabar Kana{/i}"
    mcname "{i}Tapi tetap aja aku gk bisa ngilangin pikiran ku tentang gimana kabar Kana{/i}"
    
    mcname "Haaaahh……"
    
    mcname "{i}Mungkin ku coba nenangin diri dulu sambil jalan-jalan sebelum balik ke kos{/i}"
    
    #*Skip Scene*
    #BG MALL
    
    "Karena bingung mau kemana, akhirnya [mcname] ke Mall yang pernah ia datangi bersama Kana dulu"
    
    mcname "Duh niatnya pengen nenangin diri tapi ujung-ujungnya malah ke sini"
    mcname "Yah tapi cuma disini sih tempat yang ku tau di Jakarta"
    
    "[mcname] kemudian berkeliling melihat-lihat di mall"

    #*transisi putih (buat nunjukin kalo [mcname] keliling)*
    
    mcname "Eh itu kan"
    "Saat berkeliling, [mcname] melewati toko baju yang pernah ia lewati waktu bersama dengan Kana"
    
    mcname "Kalo gak salah waktu itu Kana ngeliatin baju ini lumayan lama ya"
    #*Flashback pas ngeliat baju di toko*
    
    mcname "Oke lah"
    #*SFX bunyi masuk toko”
    mcname "Permisii"

    #*Skip Scene*
    #BG Langit Pagi
    #BG Kelas
    
    "Paginya di kampus saat bu Dosen lagi menjelaskan kuliah"
    
    dosen "Sepertinya beberapa hari ini Kana absen terus ya"
    
    "Mendengar bu dosen mengatakan nama Kana, [mcname] pun langsung terkejut"
    
    "Tadi ibu sudah dapat informasi dari orang tuanya Kana kalau Kana izin sakit jadi tidak bisa masuk"
    
    mcname "Hah? Kana sakit?"
    mcname "Ku coba tanyakan langsung ke Freya deh, kan dia habis dari rumah Kana kemarin"
    
    #*Skip Scene*
    #Transisi Putih
    
    mcname "Freya, emang bener kalau Kana lagi sakit?"
    "Setelah kelas berakhir, [mcname] langsung mendekati Freya yang membuat Freya terkejut"
    
    freya "Eh [mcname]"
    freya "Ah masalah itu ya"
    
    freya "Mungkin kamu udh tau duluan, tapi Kana itu dulu tubuh nya lemah"
    freya "Jadi gk bisa ngelakuin hal-hal normal yang kayak orang lain"
    freya "Akhirnya dia sering ngehabisin waktunya dirumah, ngewibu"
    freya "Dan mungkin karena hal tesebut, jadinya dia dijauhin temen sekelasnya waktu masih sekolah"
    freya "Sampai akhirnya dia balik nge nutup diri di kamar nya mulu"
    
    freya "Aku gk terlalu tau gimana cerita dia sepenuhnya, soalnya waktu itu aku juga lagi ikut orang tua ku karena masalah kerjaan di luar kota"
    freya "Untung aja waktu aku kembali ke sini Kana jadi mulai membuka diri lagi dan mencoba kembali bersosialisasi"
    freya "Tapi entah kenapa dia malah kembali menjadi seperti dulu"
    
    "Setelah memberikan ringkasan tentang masalalu kana, Freya pun menatap [mcname]"
    
    freya "Oleh karena itu [mcname] tolong"
    "Freya menepuk kedua tangannya seperti memohon"
    freya "Aku gak pengen Kana balik seperti dulu jadi menutup dirinya lagi"
    freya "Jadi bisa gak kalo kamu bujuk dia buat kembali"
    
    mcname "Eh aku??"
    "[mcname] bingung kenapa Freya minta tolong padanya"
    mcname "Bukannya kamu ya, temen deketnya Kana dari dulu"
    
    freya "Soalnya kemarin waktu aku ke sana aku gak dibolehin masuk sama Naya"
    freya "Jadi aku rasa mungkin cuma kamu yang bisa"
    freya "Apalagi beberapa hari ini kalian berdua deket banget, jadi aku yakin pasti berhasil"
    
    "[mcname] sedikit malu karena dibilang dekat dengan Kana"
    "Tapi kemudian menggeleng-gelengkan kepalanya untuk kembali fokus"
    
    mcname "Oke deh bakal ku coba"
    "Kata [mcname] setelah memantapkan dirinya"
    
    freya "Makasih banyak MC"
    "Freya tersenyum senang dengan jawaban [mcname]"
    freya "Ini alamatnya Naya, ya"
    freya "Good luck~"
    
    #*SKIP SCENE*
    #BG LANGIT

    "[mcname] kemudian menuju ke rumah Kana"
    mcname "Uhhh,, belok kanan di sebelah sini"
    
    "Itu perjalanan yang bisa dibilang cukup jauh dari stasiun kereta yang sering [mcname] pakai"
    "Komplek perumahan yang dituju [mcname] katanya dikenal dengan perumahan yang cukup mewah"
    
    mcname "Jadi ini rumah kana"
    "Di sana terlihat rumah yang cukup mewah."
    "Bahkan lebih besar dari rumah [mcname] di kampung"
    
    "Kalau gak salah, pernah denger kalo Kana itu orang kaya"
    "Tapi gak nyangka bakal sebesar ini"
    
    "[mcname] pun kemudian mencoba membunyikan bel yang ada di dekat pintu"
    
    #*DING*
    
    "Tidak lama setelah bel berbunyi, terdengar suara langkah kaki menuju pintu depan"
    
    #???? "Iya cari siapa yaa???"
    
    "Terlihat seorang wanita cantik yang membukakan pintu"
    "Wanita tersebut terlihat cukup muda, mungkin kisaran 20 tahunan"
    mcname "{i}Sepertinya dia kakaknya Kana{/i}"
    
    mcname "Saya [mcname], teman sekampusnya Kana"
    "MC kemudian memperkenalkan diri kepada wanita tersebut"
    mcname "Saya mau menjenguk Kana karena katanya lagi sakit"
    
    #Kayaknya kakak Kana "Ahhh [mcname], Kana sering banget nyeritain tentang kamu hahaha"
    #Kayaknya kakak Kana "Ayo sini masuk dulu"
    
    mcname "Makasih banyak Kak"
    
    #Kayaknya kakak Kana "Loh kok kak?"
    
    mcname "Eh??"
    mcname "Kakaknya Kana kan?"
    "[mcname] bingung takut membuat wanita itu tersinggung"
    
    #Mamah nya Kana "Eehhh memang saya terlihat semuda itu, saya mamah nya Kana"
    
    mcname "Eh maaf tante, saya kira kakaknya Kana soalnya keliatan masih muda"
    
    #Mamahnya Kana "Fufufu bisa aja kamu"
    
    #*SKIP SCENE*
    #BG LANGIT ATAU DEPAN PINTU KAMAR KANA
    
    "Setelah diceritakan sama Mamah nya Kana tentang bagaimana keadaan Kana yang sampai sekarang tidak mau keluar kamar."
    
    "[mcname] akhirnya berada di depan pintu Kamar Kana"
    
    "[mcname] berhenti sebentar, memikirkan cara untuk membujuk Kana"
    "Tapi kemudian menggelengkan kepala"
    
    mcname "{i}Ah, kebanyakan mikir juga ga ngubah keadaan{/i}"
    
    #*SFX ketok pintu*
    
    mcname "Kanaaa, kamu di sana??"
    
    
    #Bawa Strawberry cake (Panjangin)
    "[mcname] menunggu respon dari Kana"
    "Seperti yang diduga, tidak ada jawaban dari Kana"
    "Namun menurut perkataan Mamahnya, Kana mengurung diri di dalam kamarnya selama beberapa hari ini."
    
    #*CHOOSE*
    menu:
        "STOP DISINI":
            #A. STOP DISINI
            #MILIH A
            
            #MC
            mcname "{i}Sepertinya Kana tidak bisa ku ganggu{/i}"
            mcname "{i}Mungkin kubiarkan aja dulu{/i}"
            #
            #*BLACK SCREEN*
            #AKHIRNYA KAMU MUNDUR DARI KAMAR NYA KANA DAN MEMILIH UNTUK MENDEKATI MAMAH NYA
            #
        "\“i gently open the door\”":
            #B. “i gently open the door”
            #MILIH B
            
            mcname "Kana… Aku masuk ke kamar, ya"
            mcname "Kalau kamu gak suka, nanti ngomong aja ya"
            
            "[mcname] kemudian meraih gagang pintu kamar nya Kana"
            "[mcname] rasa jika dia tidak melakukannya sekarang, maka Kana akan mengurung dirinya lebih lama"
            
            "Pintu kamar nya tidak di kunci"
            "[mcname] tahu itu karena sudah diberitahu terlebih dahulu oleh mamahnya Kana"
            "Saat [mcname] menutup pintu kamar, terasa kegelapan menyelimuti kamar itu."
            
            "Dari balik tirai jendela, terlihat sedikit cahaya yang muncul."
            "Membantu mata [mcname] menyesuaikan dengan kegelapan yang pekat."
            
            "Kamarnya Kana terasa berbeda, mengeluarkan aroma khas yang mencerminkan kepribadiannya. Entah kenapa tercium aroma lautan yang segar."
    
    "Saat [mcname] mencoba memperhatikan sekitar, terdengar suara memanggil [mcname]"
    
    kana "[mcname]…."
    
    mcname "Huh, jangan-jangan yang di dalam selimut itu kamu, Kana?"
    
    kana "Umnnn…"
    
    mcname "......."
    mcname "Aku buka tirai nya ya. Mungkin kamu lebih nyaman dalam gelap, tapi sedikit cahaya juga bagus buat kamu."
    
    kana "Mmmmm… iya"
    
    #Transisi kebuka tirai nya, dari hitam ke putih
    
    #*CG KANA nanti kalo sempat bikin*
    
    "Kana terlihat duduk di ranjang nya, menyelimuti dirinya dengan selimut dan memeluk kakinya"
    
    "Kana terlihat sedikit gemetar, seperti anak yang sedang menunggu orang tua nya pulang ke rumah"
    
    mcname "Kana, kamu gapapa? Katanya sakit"
    
    kana "Umnn"
    
    "[mcname] kemudian mengambil kursi dan mendekatkan kursi tersebut ke kasur Kana"
    
    mcname "Aku duduk ya"
    
    "Tanpa menunggu respon dari Kana, [mcname] langsung duduk di kursi tersebut"
    
    mcname ".........."
    kana ".............."
    
    mcname "Kamu gapapa?"
    
    kana "............"
    kana "Kok kamu ke sini?"
    kana "Pasti dikasih tau Freya, ya?"
    
    mcname "Aku khawatir sama kamu, Kana."
    mcname "Soalnya kamu udah gak masuk kuliah berhari hari."
    
    kana "……"
    kana "Kok kamu khawatir sama aku?"
    kana "Gapapa kamu ke sini?"
    
    
    mcname "Eh? Kenapa kamu ngomong begitu?"
    
    kana "Aku ga mau waktumu yang berharga dihabisin kayak gini."
    
    mcname "Nggak kok, kamu lebih berharga dari waktuku."
    
    kana "Eh? Aku pikir…"
    
    "Kana berusaha melanjutkan kalimatnya, namun sepertinya tertahan di ujung lidah"
    
    "Melihat hal tersebut, akhinya [mcname] mencoba memulai percakapan lagi"
    
    mcname "Kana, akhir-akhir ini aku ngerasa kamu menutup diri."
    mcname "Aku ga tau kalo aku ada salah apa atau gimana, tapi…"
    mcname "Maaf, ya Kana. Apa pun itu, aku gak bermaksud."
    
    kana "Eh nggak kok. B-bukan salahmu."
    kana ".........."
    kana "J-jangan benci aku ya"
    kana "T-tapi…"
    kana "S-sebenarnya aku takut"
    kana "Aku takut kalau [mcname] bakal ngejauhin aku, gara-gara aku wibu"
    kana "Pasti kamu ngerasa aneh kan, dengan sifat ku ini?"
    
    "Kana mengatakan hal tersebut sambil gemetar, matanya terlihat berkaca-kaca menahan air mata nya"
    
    "[mcname] yang melihat hal tersebut hanya bisa terdiam"
    
    mcname "Aku tidak merasa seperti itu kok Kana"
    
    kana "Eh??"
    
    mcname "Aku ga tahu kenapa kamu bilang gitu"
    mcname "Tapi aku ga berpikiran begitu kok"
    
    kana "T-Tapi kan, waktu itu kamu bilang kamu ngerasa aneh sama orang yang suka jejepangan"
    
    mcname "Ahhh, masalah ganci kemaren? Waktu itu keinget papahku."
    
    kana "Eh?"
    
    mcname "Iyaa. Papahku juga wibu, bahkan bisa dibilang garis keras."
    mcname "Jadinya, aku sering teringat papahku kalo lagi ngomongin wibu. Padahal aku gk berpikir seperti itu kok."
    
    kana "J- Jadi kamu ga benci sama aku?"
    
    mcname "Seperti yang kubilang, nggak kok."
    
    "[mcname] menatap Kana sambil tersenyum dengan tatapan hangat."
    
    mcname "Aku khawatir sama kamu, Kana."
    mcname "Kamu udah gak masuk kuliah berhari-hari."
    
    kana "Maaf ya, [mcname]."
    
    mcname "Yang penting kamu baik-baik aja."
    mcname "Aku ga mau kehilangan kamu."
    
    kana "[mcname]…."
    
    mcname "Pokoknya kalau ada apa-apa, tolong ingat bahwa aku akan selalu ada. Jangan pendam semuanya sendiri, aku pasti siap mendengarkan."
    
    kana "………………"
    kana "………………"
    
    "[mcname] mengambil gelas yang ada di meja sebelah kasur lalu memberikannya ke Kana."
    
    kana "Makasih, [mcname]."
    
    "[mcname] menganggukkan kepalanya sambil tersenyum."
    
    kana "{b}*glug glug*{/b}"
    kana "………………"
    
    kana "{b}*sigh*{/b}"
    kana "[mcname]…"
    kana "Aku mau cerita"
    kana "Aku ga tau mau mulai dari mana…"
    
    "[mcname] kemudian diam untuk memfokuskan diri ke cerita Kana"
    
    #*Transisi ke BG Langit*
    
    kana "Seperti yang kamu tau, pas kecil aku punya tubuh yang lemah"
    
    kana "Aku tidak bisa melakukan banyak hal yang sering dilakukan anak-anak pada umumnya, jadinya aku cuma bisa di rumah aja"
    kana "Walaupun begitu papah mamahku tetep sayang sama aku"
    kana "Tapi, mereka juga perlu ngurus pekerjaan mereka. Jadinya aku lebih banyak menghabiskan waktu sendirian di kamar."
    kana "Sesekali Freya datang untuk bermain denganku."
    kana "Waktu itu, aku seneeeeeng banget."
    kana "Tapi…"
    kana "Suatu hari, Freya harus ikut orang tuanya yang tugas di luar kota."
    kana "................"
    kana "Akhirnya aku sendirian lagi."
    
    kana "Di tengah kesepian itu, aku menemukan yang namanya anime."
    kana "Anime itu membuat aku melihat dunia dengan cara yang berbeda"
    kana "Mulai dari anime, aku pun mulai mencari-cari juga hal yang berbau jejepangan"
    kana "Hal-hal itulah yang menjadi pelarianku di kamar yang penuh kesendirian."
    
    kana "Tak terasa waktu berlalu, aku pun harus masuk yang namanya sekolah."
    kana "Setelah sekian lama, di sana lah aku mulai mencoba berinteraksi lagi dengan orang lain"
    kana "Karena aku lama tidak berinteraksi dengan orang lain, aku tidak bisa berbicara dengan lancar"
    kana "Teman sekelasku bisa hidup dengan normal, dalam hati ku aku merasa iri dengan mereka"
    kana "Aku juga sering tidak masuk kelas karena sakit"
    kana "Aku tidak bisa belajar atau bahkan membuat teman."
    kana "Kalau terlalu banyak gerak, aku sakit lagi."
    kana "Pada awalnya, banyak teman sekelas yang berusaha mengajakku ngobrol"
    kana "Tapi aku tidak tahu apa yang harus ku katakan pada mereka."
    kana "Kebanyakan aku cuma bisa membalas \"iya\" dan \"emm\""
    kana "Lama kelamaan, orang yang mengajak ku berkurang, hingga akhirnya kelas berlangsung seperti aku tidak ada di ruangan"
    kana "Aku merasa seperti…."
    kana "Orang yang aneh"
    kana "Dan aku hanya bisa melihat teman sekelas ku ngobrol dan bercanda dari jauh"
    kana "Kadang-kadang aku harus menahan rasa ingin menangis karena hal tersebut"
    kana "Mereka dekat, tapi aku merasa ada dinding yang memisahkan."
    
    kana "Aku merasa aku juga tidak ada gunanya di sekolah, jadi aku memutuskan untuk tidak masuk sekolah lagi, cuma menghabiskan waktu di kamar"
    kana "Setahun pun berlalu, kemudian dua, tak terasa aku sudah di kelas 3"
    
    kana "Waktu itu, ternyata Freya kembali setelah mengikuti orang tuanya kerja di luar kota"
    kana "Tentu saja mendengar hal tersebut membuatku senang, namun karena bertahun tahun tidak berinteraksi dengan orang lain, aku tidak tahu harus gimana pas ketemu dia lagi"
    kana "Mungkin karena mendengar bagaimana keadaan ku, Freya kaget dan mencoba untuk mengajakku kembali masuk sekolah"
    kana "Awalnya aku enggan, namun karena desakan terus menerus dari Freya, akhirnya aku kembali mencoba untuk kembali bersekolah"
    
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
    kana "Hari-hari pun berjalan dengan mulus…"
    kana "Setidaknya kebanyakan..."
    kana "............."
    kana "Tapi…….."
    kana "Terkadang aku merasa kalau ini semua hanyalah kebohongan."
    kana "Aku merasa bersalah karena membohongi banyak orang."
    kana "Saat yang lain merasa bahagia, aku tidak merasa begitu, hingga sampai di titik aku merasa tidak yakin dengan pilihanku."
    kana "............"
    kana "Aku tidak ingin kehilangan semua ini, tapi aku juga tidak ingin terlalu bergantung sama Freya."
    kana "Semakin sering aku berpura-pura, semakin aku merasa \"apakah pembohong seperti ku pantas untuk seperti ini.\""
    kana "Apakah aku layak menerima kebahagiaan ini?"
    kana "Apakah aku layak bersama kalian?"
    kana "........"
    
    mcname "............."
    
    kana "Jadi, itu ceritaku."
    
    "Setelah menceritakan ceritanya yang panjang tanpa diganggu, akhirnya Kana berhenti. Badannya gemetar, wajahnya terlihat lelah."
    
    kana "Aku memang orang aneh yang brainrot dan suka jejepangan."
    kana "Aku juga berusaha menjadi orang yang berbeda, membohongi orang-orang, agar mereka menyukaiku."
    
    kana "Jadi makasih ya, udah mau berteman sama aku."
    kana "Walaupun mungkin kamu terpaksa, aku sangat bersyukur kamu mau jadi temanku."
    
    "[mcname] menggaruk kepalanya, bingung dan khawatir kata-kata yang akan dikeluarkan olehnya malah akan membuat luka yang semakin dalam di hati Kana."
    
    mcname "Aku ga bohong. Serius, temenan sama kamu itu hal yang sangat menyenangkan."
    
    kana "Benarkah??"
    
    mcname "Aku gak bohong. Pokoknya berapa kali pun kamu nanya, aku bakal tetap bilang kalo aku juga seneng banget bisa jadi temanmu."
    
    
    #Narrator
    #"Kana blushing"
    
    mcname "…………"
    
    kana "Ini mimpi kah?"
    kana "Aku seneng banget denger kamu suka temenan sama aku."
    
    #Narator
    "[mcname] menatap mata Kana sambil tersenyum."
    
    mcname "Kana, aku ga mau kamu merasa sendirian lagi. Aku gak nyaman kalo kamu jadi hikikomori."
    
    kana "Ga nyaman?? Kenapa?"
    
    mcname "Karena aku juga menikmati waktu yang kita habiskan bersama."
    
    kana "Ummmm"
    
    "[mcname] kemudian memegang pundak Kana dan menatap langsung ke matanya."
    
    mcname "Kamu itu dirimu yang sekarang Kana, jangan biarkan masa lalu menahanmu."
    mcname "Apa yang sudah terjadi tidak bisa diubah."
    mcname "Saat ini kamu adalah kamu."
    
    "Setelah itu [mcname] melepaskan tangannya, Kana terlihat malu dan memalingkan kepala"
    "Setelah mencari kalimat yang pas, Kana kemudian menatap [mcname] sambil tersenyum."
    
    kana "Uhmmm terima kasih, aku senang kamu sudah mau menemaniku."
    kana "Dan MC, aku…"
    "Kana mencoba mengatakan sesuatu, tapi akhirnya tidak jadi"
    kana "Mungkin ini agak memalukan tapi besok aku bakal kembali lagi seperti biasanya."
    "Kana tersenyum"
    
    mcname "Iyah, yang penting sekarang kamu istirahat dulu aja."
    "Karena merasa tugasnya sudah selesai, akhirnya [mcname] pun beranjak untuk keluar kamar"
    
    kana "Ah… oke"
    kana "Sampai jumpa besok, [mcname]"
    "Entah kenapa senyumannya terasa sedikit sedih"
    
    mcname "Oke, sampai jumpa besok"
    
    #*transisi dari hitam ke putih*
    "[mcname] kemudian keluar dari kamar Kana"
    
    "Melihat kejadian ini, [mcname] menjadi lebih mengenal Kanaia Asa dengan lebih dalam"
    
    mcname "Ya… ku rasa aku juga harus pulang"
    
    "Setelah memberikan terima kasih ke Mamahnya Kana akhirnya [mcname] pulang ke kos nya"
    
    #*SKIP SCENE*
    #*BG LANGIT*
    
    "Pagi ini [mcname] merasa lebih ringan dari biasanya, mungkin karena hari ini seseorang yang dia tunggu akhirnya kembali berkuliah lagi"
    
    #*BG kelas*
    
    freya "Jadi [mcname], gimana keadaan kana?"
    
    mcname "Dia udah mendingan dan juga katanya bakal masuk hari ini"
    
    freya "Syukurlah"
    freya "Eh btw [mcname], kamu ngapain jadi Kana mau balik lagi? Hehe"
    "Freya menanyakan hal tersebut sambil nyengir"
    
    mcname "Eh?? Gak ngapa ngapain kok."
    mcname "Aku gak tau kamu berharap apa, tapi aku hanya ngelakuin apa yang ku bisa."
    
    freya "Heeeee,,,,,"
    
    #*Suara Pintu terbuka*
    "Kana memasuki kelas saat Freya dan [mcname] sedang berbincang"
    "Dia tidak berbeda seperti sebelumnya saat dia tidak hadir, sama seperti biasanya"
    
    kana "Pagi [mcname]… Pagi juga Freya"
    
    mcname "Ah, pagi Kana."
    
    freya "Pagi juga Nay"
    freya "Gimana keadaanmu Nay? Udah mendingan?"
    
    kana "Mhm…. udah mendingan kok Frey"
    
    mcname "Ngomong-ngomong katanya UTS bentar lagi ya…"
    
    "MC mencoba mencari topik pembicaraan yang lain,"
    "sepertinya untuk mencegah membahas hal yang kemarin."
    
    freya "Iya yah."
    
    mcname "Kalo kamu gimana Kana?"
    
    kana "Kalo aku bisa aja kok, kayaknya…"
    "Kana mengambil beberapa detik untuk melanjutkan kalimatnya"
    kana "Agak takut soalnya aku sempat beberapa kali gak masuk."
    
    mcname "Kalau ada yang bisa ku bantu bilang ya"
    
    kana "Iya, mohon bantuannya ya…."
    
    #ARC 2
    
    #*SKIP TO SCENE*
    #*BG KELAS*
    
    "Sudah seminggu sejak kejadian itu, semuanya kembali menjadi normal"
    "Suasana kelas ricuh seperti biasa karena dosen belum datang. Tanpa sadar waktu pelajaran pun tiba, lalu terdengar suara pintu terbuka."
    
    dosen "Selamat pagi anak-anak, mata kuliah hari ini akan dimulai dengan - -."
    
    "Mata kuliah telah dimulai dan kondisi kelas pun tiba-tiba menjadi hening, akan tetapi di dalam keheningan tersebut ada yang tertidur pulas, ada yang bermain HP, dan ada yang mencatat."
    
    "[mcname] pun dengan serius mengikuti apa yang disampaikan oleh Dosen"
    "Saat [mcname] memperhatikan pelajaran, di ujung matanya terlihat Kana berkali kali menatap [mcname], seperti ingin mengatakan sesuatu."
    
    "Penasaran akan apa yang dilakukan gadis tersebut, akhirnya [mcname] menanyakannya secara langsung."
    
    mcname "Ada apa, Kana?"
    
    kana "G-gapapa kok."
    
    mcname "......."
    
    "Wajah Kana sedikit memerah sambil mengalihkan pandangan ke Dosen. [mcname] bingung melihat kelakuan Kana, namun akhirnya kembali fokus ke pelajaran."
    
    #*TRANSISI PUTIH*
    
    "Tanpa terasa 50 menit telah berlalu dan dosen pun mengumumkan sesuatu yang terkait dengan UTS" 
    
    dosen "Baiklah mahasiswa/i jangan lupa minggu depan ada UTS dan ini adalah UTS pertama kalian. Saya harap kalian menjunjung tinggi kejujuran dan jangan lupa untuk belajar, sekian terima kasih."
    
    #Mahasiswa/i "Terima kasih banyak Bu"
    
    #*Transisi Putih*
    
    kana "Aduh gimana nih."
    
    "Setelah dosen meninggalkan ruangan Kana memulai pembicaraan"
    
    kana "Aku gak terlalu ngedengerin dosen tadi, tau-tau udah bilang mau UTS."
    kana "Tapi harusnya bisa sih kalo belajar sambil review textbook, kayaknya??"
    
    mcname "Hahaha sama"
    "[mcname] memberikan persetujuan."
    
    kana "Duh tolongin dong [mcname]."
    kana "Bantuin aku belajar, soalnya kalo aku belajar sendiri bisa-bisa gak fokus"
    
    mcname "Bisa sih, lagi pula kalo barengan bisa lebih mudah belajarnya"
    mcname "Kalo Freya gimana? Mau ikut belajar bareng nanti?"
    
    "[mcname] mencoba mengajak Freya ke dalam obrolan"
    
    freya "Kalo aku kayaknya skip nih, soalnya aku kalo rame malah gak bisa fokus"
    freya "Lagian biar kalian bisa barengan, hehe"
    
    kana "Ih apaan sih Freya"

    freya "Hehe oke, aku duluan ya. Soalnya aku lagi ada yang di kerjain."
    "Setelah menggoda Kana, Freya mencoba lari dari ruang kelas"
    
    mcname "Kalo kamu berubah pikiran bisa dateng kok Freya"
    
    freya "Makasih tawarannya [mcname]"
    freya "Nanti aku kabarin kalo berubah pikiran deh"
    
    "Freya pergi meninggalkan Kana dan [mcname]"
    
    "Setelah Freya pergi, Kana terlihat bingung bagaimana memulai pembicaraan"
    "Melihat hal tersebut, akhirnya [mcname] berinisiatif melanjutkan topik yang ada"
    
    mcname "Gimana jadinya? Kita jadi kan buat belajar barengnya?"
    
    kana "JADI!"
    "Menyadari akan suaranya yang bersemangat Kana pun sedikit malu"
    kana "Ah"
    kana "T-tapi… gak ada ide juga sih mau di mana..."
    
    mcname "Hmmmm.."
    "[mcname] kemudian berpikir untuk menentukan tempat untuk belajar bersama"
    mcname "Gimana kalau kita ke cafe?"
    
    kana "Ehhhh boleh tuh"
     
    "Jawab Kana dengan begitu semangat. Keadaaan canggung sebelumnya menghilang, sehingga Kana dan [mcname] kembali mengobrol bersama seperti biasanya."
    
    mcname "Oke, berarti nanti kita ketemuan di sana ya."
    mcname "Nanti aku kabarin lagi kapannya."
    
    #*SKIP TO SCENE*
    #*BG CAFE*
    #*SIANG*

    "Besoknya Kana dan [mcname] janjian untuk belajar bersama di cafe."
    "[mcname] datang 5 menit lebih awal agar mengamankan posisi duduk untuk Kana."
    "Tidak lama, Kana pun datang melalui pintu"
    #*SFX PINTU TERBUKA ( PINTU YANG ADA LONCENGNYA ) 
     
    "Kana mendatangi [mcname], dia terlihat berbeda dari biasanya."
    
    kana "Eh maaf ya, nunggu lama."
    
    mcname "......."
    
    kana "K-kenapa, ada yang aneh ya sama aku"
    
    mcname "Ah aku kaget aja ngeliat kamu make baju itu, kerasa beda dari biasanya."
    
    kana "E-eh, Beneran keliatan ya? Ahahah,"
    
    mcname "Iya, kamu keliatan effort banget."
    
    kana "Ummm,,, kok kamu kepikir begitu?"
    
    mcname "Soalnya kamu pake baju yang berbeda dari yang sering kamu pake di kampus, apalagi rambut kamu keliatan lebih rapih, mungkin abis dari salon?"
    
    "Mungkin rambut nya terlihat sama seperti biasanya, namun entah kenapa [mcname] merasa kalau ada yang berbeda, mungkin itu hanya insting nya saja"
    
    kana "I-iya deh, yuk sekarang kita fokus belajar bareng aja."
    "Dengan wajah yang sedikit memerah Kana pun langsung duduk di dekat [mcname]."
    
    "Mereka berdua pun memulai untuk belajar."
    
    #*Transisi Putih*
    
    "4 jam berlalu~"
    "[mcname] dan Kana mulai merasa bosan dan kurang fokus dengan materi yang ada." 
    "Ingin mengganti suasana, [mcname] menawarkan untuk..."
    
    #*CHOSE*
    menu:
        "Main Game HP Sendiri":
            #*CHOSE A*
            "[mcname] milih untuk main game sendiri dan abaikan Kana seakan dia tidak ada, dunia milik berdua antara [mcname] dan HP, hal ini membuat Kana pun ngambek dan meninggalkan [mcname] yang sedang asik bermain HP."
            #*BROOO KALAU LAGI MAIN SAMA TEMEN, JANGAN KESERINGAN MAIN HP NAPA KAN JADINYA GINI YA ELAH YANG BENER AJA”
        "Tidur":
            #*CHOSE C*
            "[mcname] milih untuk rebahan dan tiduran untuk sejenak di pangkuan Kana dan minta tolong ke Kana buat bangunin dia, tapi ternyata saat Kana mencoba membangunkan kamu, kamu malah keenakan tidur di pangkuan Kana, namun karena kamu merasa nyaman akhirnya tidak bangun lagi."
            #*EH CUY LO NI LAGI DI CAFE BUKAN DI KOS, LAGIAN KAN INI LAGI KERJA KELOMPOK DAH KENAPA MALAH TIDUR MIKIR BRO MIKIR“
        "Ajak Kana main game":
            jump AjakKanaMainGame
    #*CHOSE B*
label AjakKanaMainGame:
    "Sebagai refreshing kamu milih main game yang ada di dalam cafe dan mengajak Kana untuk memainkan game tersebut. Kana yang awalnya ragu pun mulai tertarik saat kamu mulai menjelaskan tentang game yang akan dimainkan tersebut. Mungkin terbawa suasana dan karena mumet saat belajar tadi, Kana dan [mcname] enjoy memainkan game yang ada lebih dari yang mereka duga."
    
    "Kana pun terlihat menjadi lebih terbuka kepada MC"
    
    kana "Aaaaa, iii kok kalah mulu sihhh. [mcname] ngalah napa…"
    
    mcname "Hehehehe, you need 1000 years to defeat me."
    
    #*Transisi Putih*
    
    "Setelah puas bermain game, akhirnya [mcname] dan Kana kembali duduk ke tempat mereka sebelumnya."
    
    kana "Game yang tadi seru banget ya."
    
    mcname "Hahaha iya, apalagi moment pas kamu akhirnya bisa ngalahin aku."
    
    kana "Next game pasti aku menang lagi kok!"
    
    "Selama mereka duduk, Kana dan [mcname] membicarakan game yang mereka mainkan tadi."
    
    mcname "Tapi emang sih, cuma beberapa kali main aja kamu sudah jago gitu mainnya."
    
    kana "Hehehe iya kan."
    
    "Mungkin karena merasa suasananya sedang bagus, [mcname] mencoba untuk membahas hal-hal yang berbau jejepangan."
    
    "Kana pernah bilang kalau dia menyukai hal-hal tersebut dan [mcname] ingin mengenal Kana lebih dalam lagi. Tapi [mcname] teringat, hal-hal itulah yang membuat Kana merasa berbeda dari yang lain."
    
    mcname "Btw Kana, kamu kan tau banyak tentang jejepangan. Kebetulan Papahku wibu, dia suka ngidol dan jejepangan gitu. Tapi aku pengen tau lebih banyak lagi, jadi kalo boleh sih aku mau tanya-tanya tentang hobi kamu."
    
    kana "E-Eh,, b-boleh kok."
    
    mcname "Tenang aja kok. Aku ga bakalan anggep kamu aneh atau apalah lah, jadi santai aja. Aku bener-bener pengen tau lebih banyak sih tentang ini dari kamu."
    
    kana "EEEEEEEH???"
    kana "SERIUS!!???"
    "Nada kana yang begitu bersemangat membuat hampir seluruh orang di cafe tersebut melihat ke arah Kana, sadar akan hal itu Kana pun segera duduk dan memelankan suaranya lagi."
    kana "E-Eh maaf ya, terlalu semangat hehe, tapi janji ya jangan sampe takut sama aku."
    
    mcname "Iya aku JANJI kok, SUMPAH. Kan aku juga yang nanya duluan."
    
    kana "Janji kelingking?"
    
    mcname "Iya. Kelingking kita berjanji. Jari manis jadi saksi?"
    
    kana "Ih apaan sih."
    kana "Yauda deh kalau gitu, jadi kita harus mulai dari yang mana nih? Kamu mau tau soal apa deh?"
    
    mcname "Hmmm, bingung juga sebenernya… Hmmm, dari apa yang kamu lagi suka sekarang deh."
    
    kana "Kalo aku sekarang lagi suka dengerin lagu-lagu idol, jujur aku suka dengan dance sama lagunya"
    
    mcname "Heeee…"
    
    "Kana menjelaskan hal-hal yang dia suka dengan penuh semangat."
    
    #*TRANSISI PUTIH*

    "Tidak terasa Kana membahas hal tersebut lebih dari 1 jam."
    
    kana "E-ehhh, udah 1 jam lebih!?? Maaf ya kayaknya aku kebablasan deh."
    "Kana melihat ke arah [mcname] dengan panik, takut [mcname] merasa aneh atau pun gelisah karena semua hal wibu yang telah diceritakan olehnya."
    mcname "Ga perlu mikir yang aneh-aneh deh Kana. Santai aja, aku kan udah janji."
    mcname "Lagian dengerin kamu cerita kaya gitu seru kok, ternyata banyak ya yang masih belum aku tau dari kamu."
    mcname "Seneng aja bisa tau sisi kamu yang seperti ini."
    
    "Mendengar hal tersebut wajah Kana memerah."
    
    kana "Eh… ya udah nanti ku kasih playlist yang sering kudengar ke kamu deh."
    
    "Kana melihat sekeliling, terlihat suasana cafe berbeda dari saat mereka datang."
    
    kana "Ah, gak kerasa sudah jam segini ya."
    
    mcname "Kayaknya kita malah kebanyakan main daripada belajarnya ya, haha."
    mcname "Tapi gak apa-apa, setidaknya kita sudah nyicil sedikit-sedikit lah ya."
    
    kana "Iya, hehe."
    
    mcname "Gimana kalo kita balik dulu, soalnya takut kemaleman."
    
    kana "Ummmnn…"
    "Kana terlihat ingin mengatakan suatu hal."
    kana "[mcname]"
    kana "Aku rasa kita masih belum cukup belajarnya"
    kana "Jadi… nanti mau belajar bareng lagi?"
    #
    "Kana mengatakan tersebut dengan sedikit gugup, mungkin takut jika [mcname] akan menolaknya."
    
    mcname "Boleh kok. Lagipula aku juga free nanti."
    
    kana "O-oke janji ya."
    kana "Nanti aku kabarin."
    
    #*TRANSISI PUTIH*
    #*BG LANGIT*
    
    "Beberapa hari setelah hari itu, [mcname] dan Kana selalu belajar bersama di cafe."
    "Bahkan pelayan di sana pun terasa seperti teman karena saking seringnya bertemu."
    
    kana "Haaaaahhh…"
    kana "Kayaknya aku mulai bosen deh belajar di sini terus"
    kana "Pengennya mungkin ganti suasana lain"
    mcname "Hmmmm… bisa sih"
    mcname "Tapi mau di mana kira-kira?"
    
    kana "Gimana kalo kita ke Jepang, sekalian nonton konser si M*ku"
    "Karena sudah mumet dengan pelajaran kuliah, Kana mengatakan hal-hal yang tidak masuk akal"
    
    mcname "Kayak agak mustahil kalo sekarang"
    mcname "Bahkan kalau pun bisa, sulit buat dapetin tiket konsernya"
    
    kana "Hahaha iya juga sih"
    kana "Ke pantai deh"
    
    "Mendengar kata pantai membuat [mcname] membayangkan Kana menggunakan swimsuit."
    "Sadar akan apa yang dibayangkan, [mcname] langsung menggeleng-gelengkan kepalanya."
    
    mcname "Pantai pun sekarang lagi rame banget."
    mcname "Jadi walaupun kita ke sana, yang kita liat cuma gerombolan manusia."
    
    kana "Hmmmmmm jadi di mana ya"
    
    "[mcname] dan Kana merenung untuk memikirkan tempat yang lain"
    
    #*SFX notif chat*
    
    kana "Hmmmm?"
    
    "Kana membuka HPnya."
    "Saat membaca pesan yang masuk Kana kemudian tersenyum."
    
    kana "[mcname], kata mamah dia pengen ketemu sama kamu."
    
    mcname "EH?? Kenapa"
    "[mcname] bingung kenapa mamahnya Kana ingin bertemu dengannya."
    
    kana "Hmmm gak tau juga sih."
    kana "Tapi gimana kalau kita belajarnya di rumahku aja?"
    kana "Sekalian ketemu sama Mamah ku, kan. Hehe."
    mcname "Hmmm, kalau itu bisa sih."
    
    #*SKIP TO SCENE*
    #*BG LANGIT*
    
    "[mcname] dan Kana langsung menuju ke rumah Kana setelah pulang dari cafe."
    
    mcname "Gak nyangka aku bakal ke rumah Kana dan ketemu mamahnya lagi."
    
    "Kana kemudian mengetuk pintu rumahnya"
    
    kana "Mamahh, aku pulaaang."
    kana "Ada [mcname] juga nih"
    
    "Terdengar suara pintu terbuka, di sana terlihat Mamahnya Kana"
    
    #Mamahnya Kana "Selamat datang Kana, [mcname]. Terima kasih udah mau datang."
    #Mamahnya Kana "Ayo masuk."
    
    "Setelah diperbolehkan Mamahnya Kana akhirnya [mcname] masuk ke rumahnya Kana, mengikuti di belakang Kana"
    
    #Mamahnya Kana "Anggap rumah sendiri ya."
    
    "Mamahnya Kana kemudian pergi ke dapur"
    
    "Kana dan [mcname] duduk di sofa bersama-sama."
    "Mereka berbincang-bincang sambil mulai belajar kembali tentang kuliah mereka."
    
    #Mamahnya Kana "Ini ya minum buat kalian, sekalian nanti makan siang di sini ya biar bisa fokus belajarnya."
    
    mcname "Gak perlu repot-repot tante"
    
    #Mamahnya Kana "Duh gak papa santai aja."
    
    "Mamahnya Kana pun kembali ke dapur"
    
    kana "Eh kalo gitu aku ikut bantu Mah."
    "Kana pun kemudian pergi ke dapur, meninggalkan [mcname] sendirian di ruang tamu."
    
    "Sambil menunggu Kana, [mcname] pun melihat-lihat ruang tamunya Kana."
    
    "Tidak lama setelah itu, Mamahnya Kana masuk ke ruang tamu."
    "Tapi Kana tidak terlihat mengikutinya."
    
    #Mamahnya Kana "Ini ya [mcname], dimakan"
    "Mamahnya Kana membawakan kue kering."
    
    mcname "Waduh makasih lagi tante, jadi gak enak."
    
    #Mamahnya Kana "Udah gak usah dipikirin."
    #Mamahnya Kana "Lagian ini juga sebagai ucapan terima kasih tante buat kamu."
    #Mamahnya Kana "Soalnya udah banyak membantu Kana."
    
    mcname "Engga kok tante, itu semua berkat usaha dari diri Kana sendiri juga."
    mcname "Saya gak ngelakuin hal yang spesial."
    
    #Mamahnya Kana "Tetap saja karena kamu jadinya Kana beberapa hari ini perasaaannya keliatan lebih baik."
    #Mamahnya Kana "Oleh karena itu, makasih ya."
    #Mamahnya Kana "Sebagai imbalannya, tante bakal ngabulin satu permintaan apa aja deh buat kamu."
    
    mcname "E-Eh"
    "MC bingung dengan perkataan Mamahnya Kana"
    
    kana "MAAHHH!!! Bisa bantu sebentar di sini gak??"
    "Di dapur terdengar suara Kana memanggil."
    
    #Mamahnya Kana "Iyaaa bentarrr"
    
    #Mamahnya Kana "Duh kayaknya Kana manggil nih, maklum Kana jarang ke dapur."
    #Mamahnya Kana "Tapi katanya karena [mcname] dateng, dia jadi pengen nyoba masak untuk makan siang, fufufu."
    
    "Mamahnya Kana kemudian kembali ke dapur."
    
    "[mcname] kembali sendirian lagi di ruang tamu, namun kali ini bingung dengan perkataan yang dikatakan oleh Mamahnya Kana."
    
    #*Transisi Putih*
    #*BG Sore*
    
    "Tak terasa waktu telah menjadi sore. [mcname] melihat Kana sepertinya sudah mulai tidak fokus. Nafasnya mulai tidak beraturan. Mukanya memerah."
    
    mcname "Kamu gapapa Kana?"
    
    kana "Gapapa kok. Aku masih kuat."
    
    mcname "Kalo sampe di sini aja gimana? Kamu kayaknya butuh istirahat."
    
    kana "B-baiklah…"
    
    mcname "Kalo gitu aku pamit dulu ya… Jangan lupa besok UTS."
    
    kana "Kalo gitu aku antar ke depan pintu, deh."
    
    #Narator
    "Sudah lumayan lama [mcname] dan Kana belajar bareng, sehingga sudah waktunya [mcname] untuk pulang. [mcname] membereskan barang-barangnya lalu beranjak pergi ke depan pintu sambil diantar oleh Kana."
    
    mcname "Makasih ya makanannya."
    
    kana "Makasih juga ya, [mcname]. Sudah mau mampir."
    kana "Achoo!!"
    
    "Kana memberikan ucapan selamat tinggal kepada [mcname] di depan pintu."
    "Mamahnya Kana ada urusan pekerjaan jadi tidak ikut mengantar [mcname]."
    
    mcname "Iya Kana, makasih juga udah menjamu."
    mcname "Salam juga untuk mama."
    
    kana "Achoo!!"
    
    mcname "Nah, kan. Jaga kesehatan ya."
    
    kana "Achoo!!"
    kana "Aman kok, aku kuat."
    
    #“..........”
    
    #*Transisi Putih*
    #*BG langit*
    
    "Diperjalanan pulang"
    
    mcname "kira -kira apa yang dimaksud sama Mamahnya Kana tadi ya…"
    "[mcname] mengingat kejadian yang telah terjadi saat [mcname] berkunjung ke tempat Kana."
    
    mcname "Dan juga Kana tadi terlihat sakit."
    mcname "Moga saja dia tidak kenapa-napa."
    
    #*Transisi Gelap*
    
    #*SKIP TO SCENE*
    #*BG KELAS*

    "Hari UTS telah tiba, [mcname] merasa yakin akan dirinya karena sudah belajar bersama Kana cukup lama dan merasa cukup memahami mata kuliah yang telah diberikan."
    
    "[mcname] melihat ke arah Kana dan menyapa. Akan tetapi perhatiannya teralihkan saat melihat muka Kana."
    
    #*SKIP TO SCENE*
    #*Sprite KANA MUKA MERAH PUCAT*
    
    mcname "Pagi Kana"
    
    kana "Ah, P- Pagi, [mcname]."
    
    "Muka kana terlihat lebih pucat daripada kemarin saat [mcname] berkunjung ke rumahnya."
    
    mcname "Kamu gapapa?"
    
    kana "Ga-gapapa kok. Aku masih kuat."
    
    mcname "Kamu yakin???"
    mcname "Soalnya mukamu kayaknya..."
    
    #*SUARA PINTU TERBUKA*
    
    #Narator
    "Pengawas ujian datang dan UTS pun akan dimulai, membuat [mcname] tidak dapat beranjak dari kursinya."
    
    #Dosen Pengawas "Baiklah semuanya, UTS akan dimulai jadi saya harap semuanya menonaktifkan gadgetnya serta mengerjakannya secara mandiri, waktu kalian selama 45 menit dimulai dari sekarang."
    
    #*SKIP TO SCENE*
    #*MINI GAME*
    
    mcname "Ahhh akhirnya beres."
    "[mcname] mengangkat tangannya."
    mcname "Maaf, Pak. Kalau sudah selesai apakah boleh dikumpulkan sekarang?"
    #Dosen Pengawas "Wah, cepat juga. Sepertinya kamu yang pertama selesai."
    #Dosen Pengawas "Hmmm… Baiklah, boleh dikumpulkan kalau sudah yakin."
    
    #Narator
    "[mcname] beranjak dari tempat duduk."
    "Pada saat akan mengumpulkan lembar jawaban, tiba-tiba [mcname] mendengar suara."
    
    #*SFX ORANG JATUH*

    "Pandangan semua orang pun teralihkan dan saat itu juga, [mcname] melihat Kana yang tergeletak di lantai, tanpa ragu-ragu [mcname] berlari menghampiri Kana yang tergeletak lemas dan tidak sadarkan diri."
    
    mcname "Nay!! Kamu kenapa Nay!! Nayyy!"
    
    "Penjaga ujian dan staff pun memberitahukan murid untuk menghubungi pihak kesehatan kampus akan tetapi [mcname] memberitahukan tentang riwayat kesehatan Kana. Para staf pun panik dan segera menghubungi rumah sakit terdekat. Tak lama kemudian, Kana dibawa dengan ambulans sambil ditemani [mcname]. Saat di ambulans, Kana sempat sadar."
    
    kana "[mcname]……"
    
    mcname "Kana! Kana!"
    
    kana "Aku takut…"
    
    mcname "Aku ada di sini. Kamu ga perlu khawatir! Istirahatlah."
    
    "Kana pun kembali memejamkan matanya."
    
    "Setelah sesampainya di rumah sakit, Kana pun diperiksa oleh dokter dan perawat. Di situ [mcname] hanya bisa menunggu jawaban dari pihak dokter, setelah beberapa saat pihak dokter pun keluar dari ruangan."
    
    mcname " DOK!! GIMANA KANA, DOK!??"
    
    #Dokter "Maaf anak muda, tapi kami sudah berusaha semaksimal mungkin, jadi mohon terima kabar ini dengan berlapang dada, tapi Kana…"
    
    mcname "HA!? MAKSUDNYA APAAN DOK!? KANA KENAPA DOK!!?"
    
    #Dokter "Kana… dia… DIA GAPAPA KOKK. Cuma demam kecapekan doang, ga usah khawatir. Soal riwayat kesehatannya, buat sekarang Kana udah diinfus jadinya aman. Harusnya sekarang kamu udah bisa jenguk dia."
    
    mcname "AH ELAH DOK, GA LUCU TAUUUU."
    
    "Marah akan candaan dokter, [mcname] segera pergi ke dalam ruangan perawatan tempat Kana berada."
    
    mcname "Kana! Kamu gpp kan!?"
    
    kana "Kamu kok kaya kecapean gitu sih [mcname]? Kamu kenapa?"
    
    mcname "AHHH ini gara-gara si dokter bercandain kondisi kamu tadi. Btw kok bisa demam tinggi? Kemarin bukannya istirahat tapi lanjut maksain begadang ya?"
    
    kana "Eh… i-iya, soalnya aku ngerasa masih kurang belajarnya. Jadi aku maksain buat belajar lebih sampai subuh. Eh ternyata waktu paginya udah agak pusing."

    mcname "Kana, jujur aku pengen marahin kamu tapi aku ga bisa soalnya kamu lagi sakit."
    
    kana "Huhu maaf. Eh bentar ujian kamu gimana?"
    
    mcname "Kamu ga usah khawatir kok, ujianku dah selesai. Kalo ujianmu, kata pengawas nanti bakal diadain susulan setelah UTS selesai. Sekarang kamu harus fokus sama kesehatanmu dulu aja."
    
    kana "[mcname]................"
    kana "Makasih banyak ya udah mau bantuin aku, maaf ngerepotin yaa."
    
    mcname "Kana, kamu ga ngerepotin kok santai aja. Sekarang kamu gimana rasanya? Udah mendingan?"
    
    kana "Jujur aku juga ga tau, mungkin terasa lebih baik karena kamu ada yang nemenin."
    kana "Tapi… aku takut…"
    kana "Aku takut sendirian lagi…"
    kana "Takut kejadian waktuku kecil terulang kembali dan dirawat sendirian di rumah dengan waktu yang lama."
    
    "Wajah Kana telihat lemas, melihat ke arah [mcname] seakan ingin menangis. Akan tetapi ia tetap berusaha tersenyum."
    
    mcname "Kana… jangan mikir kaya gitu. Aku bakalan selalu temenin kamu apapun yang terjadi oke? Yang penting kamu sehat dulu aja deh, ga usah mikirin yang lain dulu."
    
    kana "Iya…."
    kana "Ini udah mendingan kok. Umm… aku udah boleh pulang gak ya? Soalnya ini lumayan gak enak keringetan, aku pengen ganti baju."
    
    mcname "Eh bentar aku coba tanyakan dulu ke perawatnya."
    
    #*Beberapa menit kemudian*
    
    mcname "Ehh ini bisa katanya, tapi harus ada yang anterin kamu pulang. Mamahmu ke mana?"
    
    kana "Ummm… Kalo kamu bisa ga MC? Nganterin aku pulang…"
    kana "Soalnya Mamahku lagi sibuk jam-jam segini."
    
    mcname "Eh aku !??? "
    mcname "{i}Waduh kok gue? Tapi ga ada siapa-siapa lagi sih di sini. Harus gimana nih gue?{/i}"
    
    #*CHOSE*
    menu:
        "Nolak tawaran Kana":
            #*CHOSE B*
            "[mcname] menolak tawaran Kana. [mcname] terlalu malu untuk menerima ajakan itu, dan akhirnya Kana disuruh pulang sendiri."
            #“BROOO ANAK ORANG LAGI SAKIT MALAH LO SURUH BALIK SENDIRI GA TAKUT DIA KENAPA KENAPA KAH?”
        "Kabur dari tempat":
            #*CHOSE C*
            "[mcname] memilih kabur dari tempat itu saking malunya karena membayangkan berduaan dengan Kana. Setelah itu pun kamu tidak tau Kana pulang atau tidak, tetapi kamu hanya mendapatkan kabar dari Kana melalui HP dengan kata-kata “kamu jahat“."
            #“BROOO KO KABUR SI, APA SIH YANG BIKIN LU MALU TUH GAJELAS BANGET DAH “
        "Terima tawaran Kana":
            jump TerimaTawaranKana
label TerimaTawaranKana:
    #*CHOSE A*
    "[mcname] pun menerima tawaran Kana. Meskipun malu, tapi rasa ingin menjaga Kana lebih besar."
    
    mcname "K-kalau kamu gak keberatan sih boleh, Kana. Nanti aku temenin, tapi aku minta ijin dulu ke perawat ya. Soalnya harus isi surat-surat keterangan dulu, haha."
    
    kana "I-iya, makasih banyak ya sekali lagi."
    #*blush*




    #ARC 3

    #*SKIP TO SCENE*
    #*BG RUMAH KANA*

    "Sesaat setelah datang di rumah Kana, ia menceritakan bahwa Mamahnya sedang pergi kerja sehingga hanya menyisakan Kana dan [mcname] berdua di sana."
    
    #*BG KAMAR KANA*
    "Kana pun istirahat di kasurnya ditemani oleh [mcname] yang sedang duduk di kursi belajar Kana."
    
    mcname "Oke, Kana sekarang kamu tunggu dulu ya. Ini aku beliin makanan tadi pesen online sih, semoga cocok yaa. Bentar aku siapin dulu."
    
    kana "Makasih yaa, maaf ngerepotin."
    
    mcname "Udah lah ga usah kaya gitu kan kita udah jadi temen jadi santai aja Kana"
    
    kana "Yeeeee makasih yaaa akhirnya setelah sekian lama +1 teman."
    
    mcname "LAH!? Kan dah temenan dari lama, gimana sih hahaha."
    
    kana "Gapapa yang penting +1 teman, hehe."
    
    mcname "Hadeh yaudah. Aku siapin makanan dulu ya."
    
    "Setelah [mcname] pergi, Kana pun memeluk bantalnya dengan wajah yang memerah."
    
    "[mcname] pun pergi ke dapur untuk mengambilkan makanan dan obat yang telah disiapkan oleh dokter."
    
    mcname "Kana. Ini makanannya kamu makan dulu ya, obatnya ada di sini. Btw kamu udah kabarin Mamah kamu ?"
    
    kana "Udah kok. Mamah awalnya mau langsung pergi ke rumah sakit, tapi aku bilang ga usah soalnya udah ada kamu yang temenin aku. Aku juga ga mau ganggu waktu kerjanya Mamah."
    
    mcname "Oke deh kalau emang gitu. Btw dipikir pikir dokter tadi udah ngeselin, tapi lucu juga ya."
    
    kana "Kenapa tuh?"
    
    mcname "Iya nih tadi udah bikin drama kaya di TV yang bilang “Kami sudah berusaha semaksimal mungkin." 
    mcname "Eh tapi sekarang obatnya {i}aergiamint-hachu{/i}, nama obatnya aneh banget ya."
    
    kana "Oooo, itu obat yang biasa aku minum kok. Namanya emang aneh kan, tapi itu manjur kok. Kayaknya…"
    
    "Kana pun mencoba makan akan tetapi tangannya terkadang merasa lemas karena terdapat infus di lengan kanannya."
    
    #Sfx prang ( suara sendok jatuh ke piring )
    
    mcname "Kana!!!?? Kamu gapapa?"
    
    kana "Ah.. iya,"
    kana "Gapapa kok, cuma ini tangan kananku agak lemes aja soalnya ada infusan. Terus tadi aku coba makan pake tangan kiri, ternyata susah juga ya."
    
    mcname "Eh… Bentar kalau gitu aku bantu suapin kamu aja."
    
    kana "Eh!!!"
    
    mcname "????"
    mcname "Kenapa?"
    
    kana "E-enggak apa-apa kok. K-kalau kamu emang bersedia, boleh aja sih.."
    
    mcname "Oke dehh, sini aku bantu sua-"
    #*Blush*
    "Tiba-tiba [mcname] terdiam, sadar akan perkataannya yang bisa dibilang cukup berani. Akan tetapi nasi sudah menjadi bubur, [mcname] tidak dapat lagi menarik kata katanya tersebut."
    
    kana "K-k-kenapa [mcname]?"
    
    mcname "Ehhhh enggaa ada apa-apa kok. Sini aku suapin."
    mcname "{i}Aduhhh nyuapin Kana? Kok bisa ya, tiba-tiba tanpa sadar ngomong gitu? Tapi kalau nggak dibantu, nanti dia ga makan. Terus dia ga bisa minum obat, terus nanti dia ga sehat, AAAAA. Oke deh, aku harus bisa!{/i}"
    
    "[mcname] pun mengambil makanan dari piring Kana, mencoba mendekatkan sendoknya ke mulut Kana dengan perlahan. Saat itu pun suara pintu terbuka keras membuat Kana dan [mcname] kaget terdiam."
    #*SFX PINTU TERBUKA KERAS(BRAK)*
    
    freya "KANAAA!!! KAMU GAPAPA KA-"
    "Saat itu juga Freya melihat [mcname] dan Kana yang sedang duduk dengan posisi tangan [mcname] yang membawa sendok makanan ke mulut Kana."
    freya "............."
    mcname "............."
    kana "............."
    freya "Eh sorry ganggu ya. Hehe, silahkan lanjutin."
    
    mcname "Ehhhh Freeeya tungguu!! Aku bisa jelasin!!"
    
    kana "Freeeyy!!! Tunggu dulu sini, cepat ke sini-"
    #(*SFX BATUK BATUK UHUK UHUK)”
    
    "Dengan secepat kilat Freya pun langsung menghampiri Kana yang terbatuk batuk dan menanyakan kondisi Kana saat itu. [mcname] pun menjelaskan situasi tersebut dan akhirnya Freya mengerti dengan apa yang terjadi. Freya memarahi Kana yang memaksakan dirinya untuk belajar hingga sakit, dan Kana pun berjanji untuk beristirahat terlebih dahulu."
    
    freya "Yaudah kamu habisin dulu makanannya, Nay."
    freya "Setelah itu, makan obatnya lalu istirahat."
    
    mcname "Iya, Kana. Pokoknya kesehatan kamu yang paling penting."
    
    kana "I-iya. Maaf ya. Makasih udah mau nemenin aku kayak gini…"
    #*Hiks*
    
    #BG Langit Sore
    
    "Setelah Kana selesai makan dan meminum obat dari dokter, terdengar suara pintu terbuka dan terlihat Mamah Kana datang dari arah pintu."
    
    #*SFX PINTU TERBUKA* 
    
    #Mamah kana "Astaga, kamu gapapa Naya?"
    
    kana "Iya aku udah baikan kok, Mah. Maaf ya kalau bikin mamah khawatir, ini juga udah makan dan minum obat kok. Jadi tinggal istirahat aja."
    
    #Mamah Kana "Eh ya udah kamu istirahat aja yaa. Freya sama [mcname], kita ngobrol di ruang depan aja ya. Biar Kana istirahat."
    
    mcname "Iya, Kana harus istirahat."
    
    freya "Get well soon, Nay."
    
    "[mcname] dan Freya pun meninggalkan Kana untuk beristirahat, dan mengikuti Mamah Kana menuju ruang tengah."

    #*SKIP TO SCENE*
    #*BG RUANG TENGAH SORE*

    #Mamah Kana "Makasih banyak ya udah mau nemenin sama ngerawat Kana. Untung aja ada kalian, kalau engga… Aduhh ga kebayang deh. Sekali lagi makasih banyak ya."
    
    mcname "Eh iya tante sama-sama, kebetulan aku bisa bantu jadi aku bantuin, hehe."
    
    freya "Iya aman aja kok kalau sama kita. Eh udah jam segini, maaf ya tante aku pulang dulu. Udah ditunggu sama orang tua, ada acara soalnya. Hehe."
    
    mcname "Iya tante, aku juga pulang dulu ya. Sekarang Kana udah ada yang jaga, jadi mau pulang ya. Udah jam segini juga."
    
    #Mamah Kana "Eh iya, lupa kalau udah jam segini. Hati hati di jalan yaaa, sekali lagi makasih banyak."
    
    #mcname & Freya “Sama-sama, tante.“
    
    "[mcname] dan Freya pun berpisah menuju ke rumahnya masing-masing. Selagi dalam masa pemulihan, [mcname] dan Freya saling bergantian untuk menjenguk Kana. Setelah Kana benar-benar sehat, Kana pun melakukan ujian susulan untuk mengejar ketertinggalan UTS yang sebelumnya."
    
    #BG Kelas

    "[mcname] dan Freya mengantar Kana yang akan melakukan UTS susulan."
    
    mcname "Good luck, Kana!"
    
    freya "Kamu pasti bisa! Do it, Nay!"
    
    kana "Makasih, teman-teman. Tunggu aku, ya!"
    
    #BG Lorong
    
    "Selagi Kana mengerjakan UTS susulan, [mcname] menyarankan untuk melakukan perayaan dalam rangka merayakan selesainya UTS dan kesembuhan Kana."
    
    freya "Hmmm. Kalo nanti mau makan-makan, gak? Ngerayain kesehatan Kana sama selesainya UTS."
    
    mcname "Weh, boleh tuh! Hmmm kalau kita ngerayain di cafe gimana?"
    
    
    freya "Eh seru juga tuh, cocok nih nanti kita mau rayain gmn?" 
    
    mcname "Eh gimana kalau beli cake gitu? Kana kan suka cake tuh."
    
    freya "Ide bagus tuh! Cocok banget, Si Naya suka strawberry cake sih."
    
    #*SKIP TO SCENE*
    #*BG CAFE SIANG/SORE*
    
    mcname "Sekali lagi, SELAMAT KANAAAAA!!!! "
     
    freya "Selamat yah, udah namatin UKTS kali ini. Meski susulan, setidaknya kamu berhasil. Lain kali jangan sakit lagi ya."
     
    kana "Eeeehh. Makasihh Freey, [mcname], hehehe. Maaf ya udah banyak repotin kalian semua dan maaf juga udah bikin kalian panik."
     
    freya "Santai Nayyy… Lagian kan yang paling dibikin repot tuh…."
    
    "Tanpa melanjutkan perkataannya, Freya melirik ke arahku seakan memberi kode."
    
    kana "Eh… Ummm i-iya... Makasih banyak ya [mcname]."
     
    mcname "Eh…"
    #*Blush*
    kana "K-kalau buat Kana siii…."
    
    #*Dalam pikiran MC*
    kana "{i}Kalau buat kamu mah aku mendaki gunung lewati lembah pun rela, Kanaaa.{/i}" 
    
    #Kana
    #*Blush*
    "Suasananya menjadi canggung, saking canggungnya suara jangkrik pun terdengar untuk beberapa saat hingga Freya membuka obrolan baru." 
    
    freya "Ah elah pada baper gini si, udah kan ini lagi perayaan sembuh dan selesainya UTS KEMATIAN ITU AHAHAHAH…"
    mcname "Seneng banget kamu"
    
    kana "Iya nih, emang ada beberapa yang susah si tapi untungnya aku bisa lah"
    
    mcname "Untuk kita semua yang udah lewatin UTS pertamaaaa CHEERRSS."
    
    #Kana & Freya "CHEERSS"
    
    "Obrolan mereka pun kembali berlanjut, perayaan Kana sembuh dan selesai UTS. Meski hanya dihadiri 3 orang akan tetapi suasana yang ada tetap terasa hidup, ramai, dan penuh keceriaan."
    
    #*PLOT*
    #*BELAJAR DI RUMAH KANA—>UTS—>KANA PINGSAN—>KE RUMAH KANA TERUS SUAPIN BUAH TAPI KE GAP—> NUNGGU FREYA DAN NGOBROL—>KANA SEHAT UTS SUSULAN—>NGERAYAIN
    #—-CHAPTER 2—--
    #==END===
    play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
    jump credits