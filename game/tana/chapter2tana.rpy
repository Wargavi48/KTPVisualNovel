label chapter2tana:
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    $ hidden_gift.grant()
    scene chapter 2 tana with Dissolve (1.0)
    pause(3.0)
    scene black with Dissolve (1.0)
    play music "audio/BGM_Pagi Siang.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan paginya, Tana berangkat menuju kampus seperti biasanya."
    $ quick_menu=False
    scene black with Dissolve(1.0)
    play music "BGM_Kelas.ogg" fadein 1.0 volume (1.5)
    scene kelas with Dissolve(1.0)
    $ quick_menu=True
    "Sesampainya di depan pintu ruang kelas, Tana mendengar keramaian dari dalam kelas."
    show tana_confused at tana_near
    show tana_side_confused at left 
    with dissolve
    tana "Anak-anak rame banget deh di dalam. Ada apa, ya?"
    hide tana_side_confused at left
    hide tana_confused at tana_near 
    with dissolve
    "Penasaran dengan keramaian tersebut, Tana pun membuka pintu kelas."
    "Setelah pintu kelas terbuka dan para Mahasiswa/i melihat Tana di depan pintu, ada beberapa mahasiswa yang berteriak."
    #Sprite RG Hasan
    show tana_confused at tana_near
    show bang_rama at bang_rama_right 
    show rg_hasan_talk at rg_hasan_left
    show hasan_side_talk at left
    with dissolve
    "RG Hasan" "Guys, ini dia dancer andalan kita!"
    "RG Hasan" "Hahahaha!"
    hide hasan_side_talk
    hide rg_hasan_talk at rg_hasan_left
    hide bang_rama at bang_rama_right
    #Sprite Bang Rama
    show rg_hasan at rg_hasan_left
    show bang_rama_talk at bang_rama_right
    show bang_rama_side_talk at left
    with dissolve
    "Bang Rama" "onoT, kamu centil banget sih!"
    "Bang Rama" "Hahahaha!"
    hide bang_rama_side_talk
    hide bang_rama_talk at bang_rama_right
    show bang_rama at bang_rama_right
    with dissolve
    "Tana pun kebingungan dan mencoba memahami kejadian yang sedang terjadi di depan matanya ini."
    # tana bingung
    hide tana_confused at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Hah?! Centil?! Centil apaan kocak! Gausah ngadi-ngadi lu pada!"
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near 
    hide rg_hasan at rg_hasan_left
    show tana_angry at tana_near 
    show rg_hasan_talk at rg_hasan_left
    show hasan_side_talk at left
    with dissolve
    "RG Hasan" "Alah alahh... Sa ae lu, Tana. Kita udah liat videonya."
    "RG Hasan" "Hahahaha!"
    hide hasan_side_talk
    hide rg_hasan_talk at rg_hasan_left
    show rg_hasan at rg_hasan_left
    with dissolve
    "Tana pun semakin bingung dengan video apa yang dimaksud oleh teman-temannya. Dengan wajah bingung dan panik, Tana pun bertanya pada temannya."
    hide tana_angry at tana_near 
    show tana_confused at tana_near 
    show tana_side_confused at left 
    with dissolve
    tana "V-video apa?"
    hide tana_side_confused at left
    hide tana_confused at tana_near 
    hide bang_rama at bang_rama_right
    show bang_rama_talk at bang_rama_right
    show tana_confused at tana_near 
    show bang_rama_side_talk at left
    with dissolve
    "Bang Rama" "Hadeh. Video ini loh."
    hide bang_rama_side_talk
    hide bang_rama_talk at bang_rama_right
    show bang_rama at bang_rama_right
    with dissolve
    "Mahasiswa itu pun menyodorkan handphone nya ke Tana untuk menunjukkan video yang dimaksud."
    "Tana pun mengambil handphone tersebut dan melihat video yang menjadi sumber keramaian di pagi hari ini."
    "Dalam video tersebut, tampak gadis remaja berambut merah, semerah cabe, sedang menari dengan indah gemulai."
    "Tana merasa bahwa ia pernah melihat gadis tersebut. Kemudian ia pun tersadar bahwa gadis yang ada dalam video tersebut adalah dirinya saat bermain di mall kemarin."
    stop music fadeout 1.0
    "Dengan nada pelan dan suara gemetar, Tana pun berkata..."
    play music "BGM_Bad End.ogg" fadein 1.0
    hide tana_confused at tana_near
    show tana_confused at tana_near
    show tana_side_confused at left 
    with dissolve
    tana "I-ini kan aku, t-tapi kok bisa? Siapa yang ngerekam?"
    hide tana_side_confused at left with dissolve
    hide tana_confused at tana_near
    show tana_angry at tana_near
    with dissolve
    "Mata Tana pun tertuju pada bagian pojok kiri atas layar handphone yang menunjukkan username ([mcname!l][random_number]). Di saat yang bersamaan, terdengar bunyi pintu kelas terbuka."
    hide bang_rama
    hide rg_hasan
    with dissolve
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    "[mcname!c]" "Pagi, gais."
    "Melihat [mcname!c] memasuki kelas, mata Tana langsung menatap [mcname!c] dengan tajam dan dengan rasa marah, ia menghampiri [mcname!c] dan berteriak."
    hide tana_angry at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left 
    with dissolve
    tana "MAKSUD LO APA?!"
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana_angry at tana_near
    with dissolve
    "[mcname!c]" "!!??"
    "[mcname!c] pun kaget sekaligus bingung."
    "[mcname!c]" "Lah, gua salah apa? Gua baru masuk, kenapa udah lu marahin aja?"
    hide tana_angry at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left 
    with dissolve
    tana "LO NGAPAIN NGEREKAM GUA NGE-DANCE KEMARIN?! NGAPAIN JUGA LU NYEBARIN VIDEONYA?"
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana_angry at tana_near
    with dissolve
    "[mcname!c]" "Lah? Kan gua udah minta izin ke elu."
    hide tana_angry at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left 
    with dissolve
    tana "MANA ADA LU MINTA IZIN KE GUA?! GA USAH BOONG DEH, LU! MAKSUD LU APAAN?!"
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana_angry at tana_near
    with dissolve
    "[mcname!c]" "Gua serius ga ada maksud apa-apa, Tan."
    hide tana_angry at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left 
    with dissolve
    tana "LAH TERUS KENAPA SEMUANYA PADA TAU? PASTI LU YANG NYEBARIN KAN?"
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana_angry at tana_near
    with dissolve
    "[mcname!c]" "Hah mana ada? Gua cuma bikin Instastory." 
    "[mcname!c]" "Gua juga ga nyangka kalo anak-anak tau Instagram gua dan videonya jadi viral."
    hide tana_angry at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left 
    with dissolve
    tana "GA USAH BOHONG LU, [mcname!u]!"
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana_angry at tana_near
    with dissolve
    "Mendengar Tana yang terus menerus marah, emosi [mcname!c] pun akhirnya juga ikut tersulut."
    "[mcname!c]" "DIBILANGIN GUA GA ADA MAKSUD APA-APA! GUA CUMA NGEREKAM, SOALNYA LU KELIATAN LUCU. UDAH GITU DOANG!"
    hide tana_angry at tana_near
    show tana_confused at tana_near
    show tana_side_confused at left 
    with dissolve
    tana "Eh? L-lucu?"
    hide tana_side_confused at left
    hide tana_confused at tana_near
    show tana_shy at tana_near
    with dissolve
    "Mendengar hal tersebut, Tana pun kaget dan sedikit tersipu malu."
    "Suasana di dalam ruang kelas sudah terlanjur hening. Seluruh mata tertuju pada Tana dan [mcname!c], tidak ada yang berani ikut campur."
    hide tana_shy at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left 
    with dissolve
    tana "HALAH, {i}KAKEHAN ALASAN!{/i} (BANYAK ALASAN!)"
    hide tana_side_angry_2 at left
    hide tana_angry_2 at  char_center
    hide bang_rama at bang_rama_right
    hide rg_hasan at rg_hasan_left
    with dissolve
    "Tana yang sudah terlanjur marah dan merasa malu pun akhirnya memilih untuk keluar dan bolos kelas."
    "[mcname!c]" "Dih, apaan sih Si Tana..."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Kelas.ogg" fadein 1.0 volume (1.5)
    scene kelas with Dissolve(1.0)
    $ quick_menu = True
    "Suasana kelas menjadi hening. Mahasiswa/i merasa canggung karena keributan yang terjadi."
    hide rg_hasan at rg_hasan_left
    show bang_rama at bang_rama_right
    show rg_hasan_talk at rg_hasan_left
    show hasan_side_talk at left
    with dissolve
    "RG Hasan" "Parah, gara-gara lu sih."
    hide hasan_side_talk
    hide rg_hasan_talk at rg_hasan_left
    hide bang_rama at bang_rama_right
    show rg_hasan at rg_hasan_left
    show bang_rama_talk at bang_rama_right
    show bang_rama_side_talk at left
    with dissolve
    "Bang Rama" "Apaan, elu juga padahal."
    hide bang_rama_side_talk
    hide bang_rama_talk at bang_rama_right
    show bang_rama at bang_rama_right
    with dissolve
    "[mcname!c]" "............."
    hide bang_rama at bang_rama_right
    hide rg_hasan at rg_hasan_left
    with dissolve
    "Tidak lama kemudian, dosen pun masuk ke dalam kelas dan waktu mata kuliah pun dimulai."
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    stop music fadeout 1.0
    $ quick_menu=False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Dosen.ogg" fadein 1.0
    scene kelas with Dissolve(1.0)
    show dosen_talk at dosen_center
    show dosen_side_talk at left
    with dissolve
    $ quick_menu = True
    dosen "Selamat pagi, semuanya!"
    dosen "Kelas akan saya mulai ya."
    dosen "Hari ini kita akan membahas tentang..."
    hide dosen_side_talk at left
    hide dosen_talk at dosen_center
    with dissolve
    stop music fadeout 1.0
    $ quick_menu=False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" fadein 1.0 volume (0.8)
    scene awan malam with Dissolve(1.0)
    $ quick_menu=True
    "Malamnya..."
    $ quick_menu=False
    scene kamar mc kota with Dissolve(2.0)
    $ quick_menu=True
    "[mcname!c]" "....."
    "[mcname!c]" "Auk ah."
    $ quick_menu=False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "BGM_Kelas.ogg" fadein 1.0 volume (1.5)
    scene awan with Dissolve(1.0)
    $ quick_menu=True
    "Keesokan harinya..."
    $ quick_menu=False
    scene kelas with Dissolve(2.0)
    $ quick_menu=True
    "Jadwal kuliah hari ini hanya ada satu kelas praktikum jam 8 pagi, tapi seluruh mahasiswa disuruh untuk berkumpul di kelas karena akan ada arahan dari Bu Dosen."
    "[mcname!c] pun datang lebih pagi dan memilih untuk belajar di dalam kelas sembari menunggu kelas dimulai."
    "[mcname!c]" "Hadeh, susah banget deh mata kuliah ini. Kok bisa ada kating yang dapet nilai A. Ini gua yang bodoh atau gimana dah."
    play sound "audio/crowd_noise.mp3" loop fadein 1.0 volume (4.0)
    "Mendekati waktu praktikum dimulai, [mcname!c] semakin banyak Mahasiswa/i yang masuk ke dalam kelas."
    "Tetapi, [mcname!c] tidak melihat adanya Tana di kelas."
    "[mcname!c]" "Kelas udah mau mulai, tapi Tana kok belum datang ya? Nih anak mau bolos lagi, apa?"
    "Tak lama kemudian, terdengar suara orang berlari di lorong yang disusul dengan suara terbukanya pintu kelas."
    stop sound fadeout 1.0
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    # tana capek
    show tana_shock at tana_near
    show tana_side_shock at left 
    with dissolve
    tana "*Terengah-engah*"
    hide tana_side_shock at left
    show tana_side_shock at left
    with dissolve
    tana "Huft, hampir aja gua telat. Dasar jam alarm kocak. Bisa-bisanya bunyinya pelan banget."
    tana "Masih ada bangku kosong ga, ya?"
    hide tana_side_shock at left with dissolve
    with dissolve
    "Tana pun melihat ke seluruh bagian kelas untuk mencari apakah ada bangku yang masih kosong."
    hide tana_shock at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left 
    with dissolve
    tana "Ah, untung ada bangku kosong."
    hide tana_side_talk at left
    hide tana_talk at tana_near 
    with dissolve
    "Tanpa berpikir panjang, Tana pun langsung berjalan menuju kursi tersebut."
    $ quick_menu=False
    scene black with Dissolve(1.0)
    scene kelas with Dissolve(1.0)
    show tana_silent at tana_near with dissolve
    $ quick_menu=True
    "Sesampainya di bangku tersebut, Tana baru menyadari bahwa ternyata di sebelah bangku itu ada [mcname!c] yang sudah duduk terlebih dahulu."
    "[mcname!c] terdiam, menatap Tana yang hendak duduk di bangku kosong tersebut."
    "[mcname!c]" "{i}Nih anak mau duduk sebelah gua?{/i}"
    show tana_side_idle at left with dissolve
    tana "{i}Haduh, gua baru inget kalo dia biasa duduk di situ.{/i}"
    hide tana_side_idle at left with dissolve
    "[mcname!c]" "..."
    show tana_side_idle at left with dissolve
    tana "..."
    hide tana_side_idle at left with dissolve
    "[mcname!c]" "................"
    show tana_side_idle at left with dissolve
    tana "................"
    hide tana_side_idle at left
    hide tana_silent at tana_near 
    with dissolve
    menu:
        "Responmu:"
        "Duduk, Tan":
            "[mcname!c]" "Duduk Ta-"
        ".................":
            "[mcname!c]" "................."
    show tana_silent at tana_near with dissolve
    "Sambil mengalihkan pandangan, Tana menemukan bangku kosong lain yang berada tidak jauh dari tempatnya sekarang."
    "Tanpa berkata apapun, Tana pergi meninggalkan [mcname!c] dan langsung duduk di bangku tersebut."
    hide tana_silent at tana_near with dissolve
    "[mcname!c]" "Dih yaudah. Duduk tempat lain aja sono."
    stop music fadeout 1.0
    $ quick_menu=False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Dosen.ogg" fadein 1.0
    scene kelas with Dissolve(1.0)
    $ quick_menu=True
    "Tak lama kemudian, Bu Dosen pun memasuki kelas."
    show dosen_talk at dosen_center
    show dosen_side_talk at left 
    with dissolve
    dosen "Selamat pagi, semuanya!"
    hide dosen_side_talk at left
    hide dosen_talk at dosen_center
    show dosen at dosen_center
    with dissolve
    "Mahasiswa/i" "Selamat pagi, Bu!"
    hide dosen at dosen_center
    show dosen_talk at dosen_center
    show dosen_side_talk at left 
    with dissolve
    dosen "Udah pada sarapan belum?"
    hide dosen_side_talk at left
    hide dosen_talk at dosen_center
    show rg_hasan_talk at char_center
    show hasan_side_talk at left
    with dissolve
    "RG Hasan" "Belum nih, Bu. Laper, huhu."
    hide hasan_side_talk
    hide rg_hasan_talk at char_center
    show bang_rama_talk at char_center 
    show bang_rama_side_talk at left
    with dissolve
    "Bang Rama" "Udah tadi ngemil {i}Pramog{/i}, Bu."
    hide bang_rama_side_talk
    hide bang_rama_talk at char_center
    show dosen_talk at dosen_center
    show dosen_side_talk at left 
    with dissolve
    dosen "Ada-ada aja kalian ini, hahaha."
    dosen "Yaudah. Kalau ada yang bawa bekal, dimakan aja gapapa."
    dosen "Saya cuma mau menyampaikan beberapa hal terkait materi praktikum yang pertama."
    hide dosen_side_talk at left
    hide dosen_talk at dosen_center
    show dosen at dosen_center
    with dissolve
    "Mahasiswa/i" "Baik, Bu."
    "Sebagian Mahasiswa/i yang membawa bekal pun akhirnya mengeluarkan bekal untuk dimakan sembari mendengarkan penjelasan dari Bu Dosen."
    hide dosen at dosen_center
    show dosen_talk at dosen_center
    show dosen_side_talk at left 
    with dissolve
    dosen "Baik, untuk praktikum minggu depan, masing-masing Mahasiswa dan Mahasiswi harus menyiapkan sampel tanah."
    hide dosen_side_talk at left
    hide dosen_talk at dosen_center
    show dosen at dosen_center
    with dissolve
    "[mcname!c]" "Tanah? Untuk apa kita mengumpulkan tanah, Bu?"
    hide dosen at dosen_center
    show dosen_talk at dosen_center
    show dosen_side_talk at left 
    with dissolve
    dosen "Iya, tanah."
    dosen "Nanti sampel tanah yang telah kalian dapatkan, akan diuji untuk mengetahui index kesuburan dan apa saja kandungan di tanah tersebut."
    dosen "Jadi, kalian nanti akan belajar bagaimana cara menganalisis tanah."
    hide dosen_side_talk at left
    hide dosen_talk at dosen_center
    show dosen at dosen_center
    with dissolve
    "[mcname!c]" "Nanti kita ngambil sampel tanahnya di mana, Bu? Apakah tempatnya bebas?"
    hide dosen at dosen_center
    show dosen_talk at dosen_center
    show dosen_side_talk at left 
    with dissolve
    dosen "Sampel tanah bisa diambil dari sawah di kampus, ya. Kalian sudah ke sana, kan?"
    hide dosen_side_talk at left
    hide dosen_talk at dosen_center
    show dosen at dosen_center
    with dissolve
    "Mahasiswa/i" "Sudah, Bu!"
    hide dosen at dosen_center
    show dosen_talk at dosen_center
    show dosen_side_talk at left 
    with dissolve
    dosen "Nah, kalian ambil dari sana aja."
    dosen "Nanti data yang kalian peroleh bisa dibandingkan dengan data-data milik kakak tingkat kalian untuk mengetahui apakah ada perbedaan antara data yang kalian peroleh dengan data sebelumnya."
    hide dosen_side_talk at left
    hide dosen_talk at dosen_center
    show dosen at dosen_center
    with dissolve
    "Mahasiswa/i" "Baik, Bu!"
    "[mcname!c]" "Bu, akses ke sawah apakah bebas?"
    hide dosen at dosen_center
    show dosen_talk at dosen_center
    show dosen_side_talk at left 
    with dissolve
    dosen "Bebas. Seinget saya, akses pagar sawah diatur oleh kakak tingkatmu yang saya lupa namanya."
    hide dosen_side_talk at left
    hide dosen_talk at dosen_center
    show dosen at dosen_center
    with dissolve
    "Sebelum [mcname!c] sempat menjawab kembali, tiba-tiba Tana yang masih kesal dengan kejadian kemarin pun nyeletuk."
    hide dosen at dosen_center
    show dosen at dosen_left
    show tana_angry_2 at tana_right
    show tana_side_angry_2 at left
    with dissolve
    # Kurang Kanan. Mau di sebelah kanan dosen.
    tana "Nanya mulu lu, [mcname!c]. Kayak wartawan."
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_right
    show tana_angry at tana_right
    with dissolve
    "Mendengar hal tersebut, [mcname!c] pun jadi ikut kesal."
    "[mcname!c]" "Bu, mau tanya lagi. Kalau tanahnya warna merah, boleh ga?"
    hide dosen at dosen_left
    show dosen_talk at dosen_left
    show dosen_side_talk at left 
    with dissolve
    dosen "Tanah merah? Memangnya di sawah kampus ada tanah yang warnanya seperti itu?"
    hide dosen_side_talk at left
    hide dosen_talk at dosen_left
    show dosen at dosen_left
    with dissolve
    "[mcname!c]" "Ada, Bu. Kemarin ada pas tour ke sawah."
    "[mcname!c]" "Tanahnya merah dan putih, terus ada coklat-coklatnya gitu."
    hide dosen at dosen_left
    hide tana_angry at dosen_left
    show bang_rama at bang_rama_right 
    show rg_hasan_talk at rg_hasan_left
    show hasan_side_talk at left
    with dissolve
    "RG Hasan" "[mcname!c], emang kapan ada tanah yang warnanya kayak gitu?"
    hide hasan_side_talk
    hide rg_hasan_talk at rg_hasan_left
    show rg_hasan at rg_hasan_left
    with dissolve
    "[mcname!c]" "Lah, ada tau. Kan pas itu kalian juga liat."
    hide bang_rama at bang_rama_right
    show bang_rama_talk at bang_rama_right
    show bang_rama_side_talk at left
    with dissolve
    "Bang Rama" "Emang tanah apaan? Perasaan ga ada deh."
    hide bang_rama_side_talk
    hide bang_rama_talk at bang_rama_right
    hide bang_rama at bang_rama_right
    hide rg_hasan
    with dissolve
    "[mcname!c]" "Tanah Nona nyemplung ke sawah."
    "Mendengar hal tersebut, seluruh mahasiswa di dalam kelas termasuk Bu Dosen pun tertawa terbahak bahak."
    play sound "SFX - Laughing.mp3" fadein 0.5 volume (3.0)
    "Mahasiswa/i" "HAHAHAHAHAHAHA!"
    stop sound
    hide bang_rama at bang_rama_right
    hide rg_hasan at rg_hasan_left
    show dosen at dosen_left
    show tana_angry_2 at tana_right
    show tana_side_angry_2 at left 
    with dissolve
    tana "Apa sih, kocak! Berisik deh!"
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_right
    hide dosen at dosen_left
    show dosen_talk at dosen_center
    show dosen_side_talk at left 
    with dissolve
    dosen "Hahahaha. Ada-ada saja. Oke, kalau begitu, kalian jangan lupa untuk mengambil sampel, ya."
    dosen "Kalian bebas mau ambil sampelnya kapan, yang penting disimpan di wadah tertutup dan dibawa pada saat praktikum."
    hide dosen_side_talk at left
    hide dosen_talk at dosen_center
    show dosen at dosen_center
    with dissolve
    "Mahasiswa/i" "Baik, Bu!"
    hide dosen at dosen_center
    show dosen_talk at dosen_center
    show dosen_side_talk at left 
    with dissolve
    dosen "Ya udah, itu saja dari saya. Kelas sudah selesai. Terima kasih. Saya duluan, ya."
    hide dosen_side_talk at left
    hide dosen_talk at dosen_center
    show dosen at dosen_center
    with dissolve
    "Mahasiswa/i" "Terima kasih, Bu!"
    hide dosen at dosen_center
    with dissolve
    "Setelah Bu Dosen meninggalkan kelas, seluruh Mahasiswa/i satu per satu pergi meninggalkan kelas karena sudah tidak ada mata kuliah lagi hari ini."
    stop music fadeout 1.0
    $ quick_menu=False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Lorong.ogg" fadein 1.0
    scene lorong with Dissolve(1.0)
    $ quick_menu=True
    "RG Hasan, Bang Rama, dan [mcname!c] berjalan bersama di lorong."
    show bang_rama at bang_rama_right 
    show rg_hasan_talk at rg_hasan_left
    show hasan_side_talk at left
    with dissolve
    "RG Hasan" "Oi, [mcname!c]. Lu ga laper, apa?"
    hide hasan_side_talk
    hide rg_hasan_talk at rg_hasan_left
    show rg_hasan at rg_hasan_left
    with dissolve
    "[mcname!c]" "Laper sih sebenarnya. Gua belum sarapan soalnya."
    hide bang_rama at bang_rama_right
    show bang_rama_talk at bang_rama_right
    show bang_rama_side_talk at left
    with dissolve
    "Bang Rama" "Yaudah, ayok ke kantin dah. Gua juga laper nih."
    hide bang_rama_side_talk
    hide bang_rama_talk at bang_rama_right
    show bang_rama at bang_rama_right
    with dissolve
    "[mcname!c]" "Hayuk."
    hide bang_rama at bang_rama_right
    hide rg_hasan at rg_hasan_left
    with dissolve
    stop music fadeout 1.0
    $ quick_menu=False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kantin.ogg" fadein 1.0
    scene kantin with Dissolve(1.0)
    $ quick_menu=True
    "Sesampainya di kantin, [mcname!c] mencari tempat duduk kosong terlebih dahulu."
    show rg_hasan at rg_hasan_left
    show bang_rama at bang_rama_right 
    with dissolve
    "[mcname!c]" "Tuh ada yang kosong. Di situ aja."
    hide rg_hasan at rg_hasan_left
    show rg_hasan_talk at rg_hasan_left
    show hasan_side_talk at left
    with dissolve
    "RG Hasan" "Yaudah gua aja yang jaga tempatnya, lu cari makan dulu."
    hide hasan_side_talk
    hide rg_hasan_talk at rg_hasan_left
    show rg_hasan at rg_hasan_left
    with dissolve
    "[mcname!c]" "Rama, lu ga nyari sekalian?"
    hide bang_rama at bang_rama_right
    show bang_rama_talk at bang_rama_right
    show bang_rama_side_talk at left
    with dissolve
    "Bang Rama" "Entar deh. Gua lagi ada panggilan, nih."
    hide bang_rama_side_talk
    hide bang_rama_talk at bang_rama_right
    show bang_rama at bang_rama_right
    with dissolve
    "[mcname!c]" "Oke deh."
    hide bang_rama at bang_rama_right
    hide rg_hasan at rg_hasan_left 
    with dissolve
    "[mcname!c] pun berjalan mengelilingi kantin untuk melihat makanan dan minuman apa saja yang dijual di dalam kantin."
    "[mcname!c]" "Enaknya beli apa, ya? Makan yang pedes-pedes kayanya enak nih."
    "[mcname!c]" "Nah, ada yang banyak logo cabenya tuh. Kayanya jual makanan pedes-pedes, deh."
    "[mcname!c] menghampiri penjual tersebut dan mulai memesan makanan."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene kantin with Dissolve(1.0)
    $ quick_menu = True
    "[mcname!c]" "Pak! Pesen mie pedes satu porsi, sama es jeruk."
    "Penjual" "Baik, totalnya 24 ribu, kak."
    "[mcname!c]" "Uang saya 50 ribu, pak. Ada kembalian ga?"
    "Penjual" "Receh gapapa?"
    "[mcname!c]" "Gapapa, Pak. Asal lucu 🙏🏻"
    "Penjual" "Hahahaha. Siap. Mohon ditunggu sebentar, ya."
    "[mcname!c]" "Baik, Pak."
    "[mcname!c] pun menunggu hingga pesanan selesai dibuat."
    $ quick_menu=False
    scene black with Dissolve(1.0)
    pause(1.0)
    scene kantin with Dissolve(1.0)
    $ quick_menu=True
    "Tak lama kemudian, Tana datang berjalan menuju tempat penjual yang sama seperti [mcname!c] dan mata mereka saling bertemu."
    show tana_silent at tana_near
    show tana_side_idle at left 
    with dissolve
    tana "......"
    hide tana_side_idle at left with dissolve
    "[mcname!c]" "......"
    show tana_side_idle at left with dissolve
    tana "..................."
    hide tana_side_idle at left with dissolve
    "[mcname!c]" "..................."
    hide tana_silent at tana_near with dissolve
    "Tana pun langsung berjalan melewati [mcname!c] dan pergi ke luar kantin."
    "[mcname!c]" "Idih, ngambekan."
    "Penjual" "Kak, ini pesenan sama kembaliannya."
    "[mcname!c]" "Oke. Terima kasih, Pak!"
    "[mcname!c]" "Waktunya balik ke meja tadi terus makan, deh."
    $ quick_menu=False
    scene black with Dissolve(1.0)
    scene kantin with Dissolve(1.0)
    $ quick_menu=True
    "Sesampainya di meja..."
    "[mcname!c]" "Lah? Ke mana nih bocah-bocah? Bukannya tadi mereka ngomong kalo mau duduk di sini, ya?"
    "[mcname!c]" "Hmmm kalo sendirian gini, mending gua pulang terus makan di kost."
    "[mcname!c]" "Hadeh..."
    stop music fadeout 1.0
    $ quick_menu=False
    scene black with Dissolve(1.0)
    play music "BGM_Pagi Siang.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu=True
    "Keesokan harinya..."
    $ quick_menu=False
    scene kamar mc kota with Dissolve(2.0)
    $ renpy.block_rollback()
    $ quick_menu=True
    "[mcname!c]" "Aduh. Mules banget nih perut. Kesalahan nih kebanyakan makan pedes-pedes kemarin."
    "[mcname!c]" "Haduuh. Udah pasti telat nih buat mata kuliah pertama. Gua telpon titip izin dosen ke anak-anak dah."
    "[mcname!c] pun membuka daftar kontak di handphone-nya."
    "[mcname!c]" "LAH?! KOK CUMA ADA SI TANA?!"
    "[mcname!c]" "Oh iya, gua lupa minta nomor ke anak-anak. Gua cuma punya Discord mereka. Mana internetnya jelek banget lagi di kost."
    "[mcname!c]" "Bodoh banget sih gua. Masa gua harus minta tolong ke Tana? Males banget."
    "[mcname!c]" "......"
    "[mcname!c]" ".........."
    "[mcname!c]" "................"
    menu:
        "Kamu..."
        "Malas":
            stop music fadeout 1.0
            $ quick_menu=False
            play music "BGM_Bad End.ogg" fadein 1.0
            "[mcname!c]" "Dih, males banget telepon Si Tana. Mending gua meninggoy."
            "[mcname!c] pun menaruh handphone-nya dan berjalan untuk mencari obat."
            "[mcname!c]" "Obat gua di mana ya?"
            #SFX Kepeleset
            "[mcname!c]" "Eh?"
            play sound "SFX - Fall.WAV" fadein 1.0 volume(15.0)
            "[mcname!c]" "AAAAAA!!!!"
            scene black with dissolve
            show text "{color=#FFF}[mcname!u] MENINGGAL TERPELESET GARA-GARA MENGINJAK KRESEK PLASTIK BEKAS MAKANAN SEMALAM YANG TIDAK IA BERESKAN.{/color}" with Pause(5.0)
            scene black with dissolve
            show text "{color=#FF0000}BAD END{/color}"  with Pause(2.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits
        "Telepon Tana":
            "[mcname!c]" "Yaudah lah. Daripada absen gua ngurang, terus ga bisa ikut ulangan."
            show tana_mc_ring at ui_handphone with dissolve
            play sound "SFX - Calling.mp3" loop fadein 1.0
            "[mcname!c] pun mencoba menelpon Tana."
            "[mcname!c]" "Angkat lah."
            stop sound fadeout 1.0
            "Tana tidak mengangkat panggilan telepon dari [mcname!c]."
            hide tana_mc_ring at ui_handphone with dissolve
            "[mcname!c]" "Hadeh. Pasti Tana masih marah gara-gara video kemarin. Kan gua ga maksud apa-apa."
            show tana_mc_ring at ui_handphone with dissolve
            play sound "SFX - Calling.mp3" loop fadein 1.0
            "[mcname!c]" "Coba telepon lagi deh."
            "[mcname!c]" "Angkat lah woy."
            stop sound fadeout 1.0
            play sound "SFX - Angkat Telepon.wav" volume (5.0)
            hide tana_mc_ring at ui_handphone 
            show tana_mc_telpon at ui_handphone
            with dissolve
            show tana_side_angry_2 at left with dissolve
            tana "Ha?"
            hide tana_side_angry_2 at left with dissolve
            "[mcname!c]" "{i}Damn, cuek banget.{/i}"
            show tana_side_idle at left with dissolve
            tana "......"
            hide tana_side_idle at left with dissolve
            "[mcname!c]" "{i}Fix masih marah, tapi untung diangkat.{/i}"
            show tana_side_idle at left with dissolve
            tana "................."
            hide tana_side_idle at left with dissolve
            "[mcname!c]" "{i} Masa gua harus minta maaf dulu? Gua ga salah apa-apa juga.{/i}"
            show tana_side_idle at left with dissolve
            tana ".................................."
            hide tana_side_idle at left with dissolve
            play sound "SFX - End Call.wav" loop volume (2.0)
            hide tana_mc_telpon at ui_handphone with dissolve
            "[mcname!c]" "Waduh kelupaan ngomong."
            stop sound
            "[mcname!c] pun menelepon Tana lagi untuk yang ketiga kalinya."
            play sound "SFX - Calling.mp3" loop fadein 1.0
            show tana_mc_telpon at ui_handphone with dissolve
            stop sound fadeout 1.0
            play sound "SFX - Angkat Telepon.wav" volume (5.0)
            show tana_side_angry_2 at left with dissolve
            tana "LU NGAPAIN SIH?! LU NGEPRANK GUA YA?! GUA MATIIN DAH!"
            hide tana_side_angry_2 at left with dissolve
            "[mcname!c]" "JANGAN! JANGAN! SORI, GUA TADI NGELAMUN."
            show tana_side_angry_2 at left with dissolve
            tana "Terus mau lu apa?"
            hide tana_side_angry_2 at left with dissolve
            "[mcname!c]" "Gua mau minta tolong buat nanti izinin ke dosen kalo gua bakal telat atau bahkan ga ikut kelas. Soalnya gua lagi sakit."
            show tana_side_angry_2 at left with dissolve
            tana "Males banget. Kenapa harus gua coba yang ngasih tau dosen?"
            hide tana_side_angry_2 at left with dissolve
            "[mcname!c]" "Gua cuma nyimpen nomor lu, Tan. Asli gua ga nyimpen nomor anak-anak. Jadinya gua cuma bisa minta tolong ke lu."
            show tana_side_idle at left with dissolve
            tana "........."
            hide tana_side_idle at left with dissolve
            "[mcname!c]" "Tan?"
            show tana_side_angry_2 at left with dissolve
            tana "Ya."
            hide tana_side_angry_2 at left with dissolve
            "[mcname!c]" "Makasih banyak Tan, lu udah mau ngeban-"
            play sound "SFX - End Call.wav" loop volume (2.0)
            hide tana_mc_telpon with dissolve
            stop sound
            "[mcname!c]" "Belom juga kelar ngomong, udah dimatiin aja."
            "[mcname!c]" "Aduh sumpah sakit banget nih perut, sampe pusing kepala gua."
            "[mcname!c] pun meringkuk dengan pasrah di lantai sambil merasa kesakitan."
            "[mcname!c]" "Gua skip kuliah dulu deh. Mending minum obat terus istirahat daripada tambah parah nih perut."
            "[mcname!c]" "Semoga Tana beneran ngizinin ke dosen..."
    
    stop music fadeout 1.0
    $ quick_menu=False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kampus.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu=True
    "Keesokan harinya..."
    $ quick_menu=False
    scene kamar mc kota with Dissolve(2.0)
    $ renpy.block_rollback()
    $ quick_menu=True
    "[mcname!c]" "Akhh, akhirnya perut adem gini kan enak."
    "[mcname!c]" "Btw, ini kenapa kamar gua kotor banget dah?"
    "[mcname!c]" "Hmmm, mumpung kelas hari ini agak siang, gua bersih-bersih kamar dulu dah."
    "[mcname!c] pun membersihkan kamarnya hingga rapi."
    $ quick_menu=False
    scene black with Dissolve(1.0)
    scene kamar mc kota with Dissolve(1.0)
    $ quick_menu=True
    "[mcname!c]" "Kelar juga nih bersih-bersih kamar, tapi gua belum nyuci baju. Gua rendem dulu aja deh. Jemurnya ntar habis balik dari kampus."
    "[mcname!c]" "Sekarang waktunya mandi, terus gas ke kampus!"
    $ quick_menu=False
    scene black with Dissolve(1.0)
    scene depan kampus with Dissolve(1.0)
    $ quick_menu=True
    "Perkuliahan pun berjalan seperti biasa..."
    stop music fadeout 1.0
    $ quick_menu=False
    scene black with Dissolve(1.0)
    play music "audio/BGM_sore.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu=True
    "Tak terasa langit berubah menjadi sore."
    $ quick_menu=False
    scene kelas sore with Dissolve(2.0)
    $ renpy.block_rollback()
    $ quick_menu=True
    "[mcname!c]" "Akh, akhirnya kelar juga nih kelas. Asli ngantuk banget dengerinnya."
    show bang_rama at bang_rama_right
    show rg_hasan_talk at rg_hasan_left 
    show hasan_side_talk at left
    with dissolve
    "RG Hasan" "Mending tadi lu tidur aja."
    hide hasan_side_talk
    hide rg_hasan_talk at rg_hasan_left
    show rg_hasan at rg_hasan_left
    with dissolve
    "[mcname!c]" "Yeuu. Ntar gua jadi bodoh kayak elu dong."
    hide bang_rama at bang_rama_right
    show bang_rama_talk at bang_rama_right
    show bang_rama_side_talk at left
    with dissolve
    "Bang Rama" "Hahahahaha!"
    hide bang_rama_side_talk
    hide bang_rama_talk at bang_rama_right
    hide rg_hasan at rg_hasan_left
    show bang_rama at bang_rama_right
    show rg_hasan_talk at rg_hasan_left
    show hasan_side_talk at left
    with dissolve
    "RG Hasan" "Enak bener tuh mulut kalo ngomong."
    hide hasan_side_talk
    hide rg_hasan_talk at rg_hasan_left
    hide bang_rama at bang_rama_right
    show rg_hasan at rg_hasan_left
    show bang_rama_talk at bang_rama_right
    show bang_rama_side_talk at left
    with dissolve
    "Bang Rama" "Btw kalian udah pada ambil sampel tanah belum?"
    hide bang_rama_side_talk
    hide bang_rama_talk at bang_rama_right
    show bang_rama at bang_rama_right
    with dissolve
    "[mcname!c]" "Ha? Sampel tanah apaan?"
    hide rg_hasan at rg_hasan_left
    show rg_hasan_talk at rg_hasan_left
    show hasan_side_talk at left
    with dissolve
    "RG Hasan" "Itu tuh, bukti nyata kalo lu yang bodoh."
    hide hasan_side_talk
    hide rg_hasan_talk at rg_hasan_left
    show rg_hasan at rg_hasan_left
    with dissolve
    "[mcname!c]" "Hah sumpah, yang mana sih?"
    hide bang_rama at bang_rama_right
    show bang_rama_talk at bang_rama_right
    show bang_rama_side_talk at left
    with dissolve
    "Bang Rama" "Itu, sampel tanah buat praktikum besok lusa."
    hide bang_rama_side_talk
    hide bang_rama_talk at bang_rama_right
    show bang_rama at bang_rama_right
    with dissolve
    "[mcname!c]" "OH IYA! GUA LUPA!"
    hide rg_hasan at rg_hasan_left
    show rg_hasan_talk at rg_hasan_left
    show hasan_side_talk at left
    with dissolve
    "RG Hasan" "Parahh..."
    hide hasan_side_talk
    hide rg_hasan_talk at rg_hasan_left
    hide bang_rama at bang_rama_right
    show rg_hasan at rg_hasan_left
    show bang_rama_talk at bang_rama_right
    show bang_rama_side_talk at left
    with dissolve
    "Bang Rama" "Kurang baik apa coba gua ini, udah ngingetin."
    hide bang_rama_side_talk
    hide bang_rama_talk at bang_rama_right
    show bang_rama at bang_rama_right
    with dissolve
    "[mcname!c]" "Hilih."
    hide rg_hasan at rg_hasan_left
    show rg_hasan_talk at rg_hasan_left
    show hasan_side_talk at left
    with dissolve
    "RG Hasan" "Yaudah, lu mau ikut ngambil sampel bareng kita gak? Soalnya besok terakhir."
    hide hasan_side_talk
    hide rg_hasan_talk at rg_hasan_left
    show rg_hasan at rg_hasan_left
    with dissolve
    "[mcname!c]" "Walah, gua ga bisa kalo sekarang. Gua ambil sampelnya besok aja deh. Soalnya gua harus ngejemur cucian gua."
    hide bang_rama at bang_rama_right
    show bang_rama_talk at bang_rama_right
    show bang_rama_side_talk at left
    with dissolve
    "Bang Rama" "Semangat deh yak anak kosan."
    hide bang_rama_side_talk
    hide bang_rama_talk at bang_rama_right
    show bang_rama at bang_rama_right
    with dissolve
    "[mcname!c]" "Yaudah, gua duluan ya."
    hide rg_hasan at rg_hasan_left
    show rg_hasan_talk at rg_hasan_left
    show hasan_side_talk at left
    with dissolve
    "RG Hasan" "Oke dah."
    hide hasan_side_talk
    hide rg_hasan_talk at rg_hasan_left
    hide bang_rama at bang_rama_right
    show rg_hasan at rg_hasan_left
    show bang_rama_talk at bang_rama_right
    show bang_rama_side_talk at left
    with dissolve
    "Bang Rama" "Tiati."
    hide bang_rama_side_talk
    hide bang_rama_talk at bang_rama_right
    hide rg_hasan at rg_hasan_left 
    with dissolve

    $ quick_menu=False
    scene black with Dissolve(1.0)
    scene lorong sore with Dissolve(1.0)
    $ quick_menu=True
    "[mcname!c]" "Saatnya pulang terus jemur baju."
    "???" "[mcname!c]!"
    "[mcname!c]" "Hmm? Siapa yang manggil gua?"
    "???" "Wooiii!"
    show feni_talk at feni_right
    show flora at flora_left
    show feni_side_talk at left
    with dissolve
    feni "Dipanggil malah celingak celinguk."
    hide feni_side_talk at left
    hide feni_talk at feni_right
    hide flora at flora_left
    show feni at feni_right
    show flora_talk at flora_left
    show flora_side_talk at left 
    with dissolve
    flora "Parahh."
    hide flora_side_talk at left
    hide flora_talk at flora_left
    show flora at flora_left
    with dissolve
    "[mcname!c]" "Ooooh, Kak Feni sama Kak Flora? Ada apa, kak?"
    hide feni at feni_right
    show feni_awe at feni_right
    show feni_side_awe at left 
    with dissolve
    feni "Si Tana mana?"
    hide feni_side_awe at left
    hide feni_awe at feni_right
    show feni at feni_right
    with dissolve
    "[mcname!c]" "Tana?"
    "[mcname!c]" "{i}Oh iya. Gua belum bilang makasih ke Tana udah izinin ke dosen.{/i}"
    hide flora at flora_left
    show flora_talk at flora_left
    show flora_side_talk at left 
    with dissolve
    flora "Nih anak diajak ngomong malah ngelamun."
    hide flora_side_talk at left
    hide flora_talk at flora_left
    show flora at flora_left
    with dissolve
    "[mcname!c]" "Maaf maaf. Aku ga liat Si Tana, Kak. Dia ngambil mata kuliah umum di kelas lain."
    hide feni at feni_right
    show feni_talk at feni_right
    show feni_side_talk at left 
    with dissolve
    feni "Yahh. Padahal kita mau ngasih sesuatu ke dia."
    hide feni_side_talk at left
    hide feni_talk at feni_right
    show feni at feni_right
    with dissolve
    "[mcname!c]" "Ngasih apaan tuh?"
    hide flora at flora_left
    show flora_talk at flora_left
    show flora_side_talk at left 
    with dissolve
    flora "Ini."
    hide flora_side_talk at left
    hide flora_talk at flora_left
    show flora at flora_left
    with dissolve
    "Flora memberikan selembar flyer ke [mcname!c]."
    "[mcname!c]" "Hmm? Lomba dance?"
    hide flora at flora_left
    show flora_talk at flora_left
    show flora_side_talk at left 
    with dissolve
    flora "Iya! Kita liat video Tana yang dance itu."
    hide flora_side_talk at left
    hide flora_talk at flora_left
    hide feni_talk at feni_right
    hide feni at feni_right
    show flora at flora_left
    show feni_talk at feni_right
    show feni_side_talk at left 
    with dissolve
    feni "Terus aku sama Flo mikir kalo Tana bisa nih ikut lomba dance. Ya kan, Flo?"
    hide feni_side_talk at left
    hide flora at flora_left
    hide feni_talk at feni_right
    show feni at feni_right
    show flora_talk at flora_left
    show flora_side_talk at left 
    with dissolve
    flora "Betul banget. Kamu juga setuju kan, [mcname!c]?"
    hide flora_side_talk at left
    hide flora_talk at flora_left
    show flora_smile at flora_left
    with dissolve
    "[mcname!c]" "{i}Walawe. Ternyata videonya udah kesebar sampe angkatan atas.{/i}"
    "[mcname!c]" "Setuju aja sih, tapi Si Tana kayaknya ga mau ikut deh."
    hide flora_smile
    show flora at flora_left
    hide feni at feni_right
    show feni_shock at feni_right
    show feni_side_shock at left 
    with dissolve
    feni "Lah? Emangnya kenapa?"
    hide feni_side_shock at left
    hide feni_shock at feni_right
    show feni at feni_right
    with dissolve
    "[mcname!c]" "Dia aja marah-marah pas videonya kesebar..."
    hide flora at flora_left
    show flora_shock at flora_left
    show flora_side_shock at left 
    with dissolve
    flora "Yah. Gimana dong, Kak mpen? Sayang banget kalo Tana ga ikut."
    hide flora_side_shock at left
    hide flora_shock at flora_left
    hide feni at feni_right
    show flora at flora_left
    show feni_talk at feni_right
    show feni_side_talk at left 
    with dissolve
    feni "Hmmm yaudah. Kamu bawa aja deh flyernya. Nanti tolong kasih ke Tana, ya!"
    hide feni_side_talk at left
    hide feni_talk at feni_right
    show feni at feni_right
    with dissolve
    "[mcname!c]" "Ehh??!"
    hide flora at flora_left
    show flora_talk at flora_left 
    show flora_side_talk at left 
    with dissolve
    flora "Hahahah. Tolong ya, [mcname!c]. Arigatou! Mata ne~"
    hide flora_side_talk at left
    hide flora_talk at flora_left
    hide feni at feni_right 
    with dissolve
    "Feni dan Flora pergi meninggalkan [mcname!c] di lorong."
    "[mcname!c]" "Lah? Kok jadi gua yang disuruh? Hadeehh."
    "[mcname!c]" "Dah lah. Gua harus cepet-cepet balik. Keburu mendung."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Kelas.ogg" fadein 1.0 volume (1.5)
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya..."
    $ quick_menu = False
    scene kelas with Dissolve(2.0)
    $ quick_menu = True
    "Jadwal [mcname!c] hari ini sangat padat sehingga [mcname!c] kewalahan."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_sore.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Tak terasa hari sudah sore."
    $ quick_menu = False
    scene lorong sore with Dissolve(2.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname!c]" "Kelar juga kelas hari ini. Padet banget jadwalnya dari pagi sampe sore."
    "[mcname!c]" "Mana gua belum ngambil sampel tanah lagi. Harusnya jam segini masih dibuka lah ya."
    "[mcname!c] pun bergegas pergi ke sawah."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene sawah sore with Dissolve(1.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname!c]" "Hmm?"
    "[mcname!c]" "Wah, itu kan Si Tana. Dia belum ngambil sample juga kah?"
    "[mcname!c]" "Kenapa dia ngambil di spot itu sih. Gua kan rencananya mau ngambil sampel di situ juga. Kalo gini, kan awkward banget jadinya."
    "[mcname!c]" "Apa gua samperin aja ya? Bilang makasih sekalian minta maaf. Atau ga usah? Gua juga ga salah apa-apa kok!"
    menu:
        "Apa yang kamu lakukan?"
        "Samperin Tana.":
            jump chapter2tanasawah
        "Ambil sampel di spot lainnya.":
            stop music fadeout 1.0
            $ quick_menu = False
            play music "BGM_Bad End.ogg" fadein 1.0
            "[mcname!c]" "Bodo amat lah. Gua ga salah apa-apa kok."
            "[mcname!c] pun mengambil sampel tanah di spot lain."
            "[mcname!c]" "Untung nih sawah gede, jadi banyak spotnya."
            #SFX Kepeleset
            "[mcname!c]" "Eh?"
            play sound "SFX - Fall Water.WAV" volume (4.0)
            "[mcname!c] terpeleset akibat menginjak tanah yang licin."
            scene black with dissolve
            show text "{color=#FFF}WASPADA TERHADAP SEKITAR{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FF0000}BAD END{/color}"  with Pause(2.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits
        "Pulang aja deh.":
            stop music fadeout 1.0
            $ quick_menu = False
            play music "BGM_Bad End.ogg" fadein 1.0
            "[mcname!c]" "Dipikir pikir, ngapain juga ngambil sampel tanah. Besok minta temen aja dah."
            scene black with Dissolve(1.0)
            show text "{color=#FFF}KEESOKAN HARINYA{/color}" with Pause(2.0)
            scene kelas with Dissolve(1.0)
            show dosen_talk at dosen_center
            show dosen_side_talk at left
            with dissolve
            $ renpy.block_rollback()
            dosen "Semuanya baris, ya. Tunjukin sampel tanah kalian, baru kalian boleh masuk ruang praktikum."
            hide dosen_side_talk at left 
            hide dosen_talk
            show dosen
            with dissolve
            "[mcname!c]" "{i}Waduh, gua ga bawa nih. Mana temen-temen pada beda sesi lagi.{/i}"
            hide dosen
            show dosen_talk at dosen_center
            show dosen_side_talk at left 
            with dissolve
            dosen "[mcname!c], mana sampel kamu?"
            hide dosen_side_talk at left 
            hide dosen_talk
            show dosen at dosen_center
            with dissolve
            "[mcname!c]" "I-itu, Bu. Ketinggalan di kos temen."
            hide dosen
            show dosen_talk at dosen_center
            show dosen_side_talk at left 
            with dissolve
            dosen "Oalah, yaudah. Masuk dulu aja."
            hide dosen_side_talk at left 
            hide dosen_talk
            show dosen at dosen_center
            with dissolve
            "[mcname!c]" "Eh? Saya boleh masuk, Bu?"
            hide dosen
            show dosen_talk at dosen_center
            show dosen_side_talk at left 
            with dissolve
            dosen "Masuk? Boleh dong."
            dosen "Masuk daftar mahasiswa yang nilai praktikumnya 0."
            hide dosen_side_talk at left 
            hide dosen_talk
            show dosen at dosen_center
            with dissolve
            "[mcname!c]" "NOOOOOOOOOOOOOOOOOOO~"
            hide dosen with dissolve
            scene black with dissolve
            show text "{color=#FFF}MAKANYA KULIAH YANG BENER!{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FF0000}BAD END{/color}" with Pause(2.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits

label chapter2tanasawah:
    "[mcname!c] pun menghampiri Tana."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Sawah Sore.ogg" fadein 1.0
    scene sawah sore with Dissolve(1.0)
    show tana_angry at tana_near with dissolve
    $ quick_menu = True
    "[mcname!c]" "T-Tan?"
    show tana_side_angry at left with dissolve
    tana "{i}Lah? Ngapain [mcname!c] ada di sini?{/i}"
    hide tana_side_angry at left with dissolve
    "[mcname!c]" "........"
    hide tana_angry at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left 
    with dissolve
    tana "Apa? Mau ngeledekin gua lagi?"
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana_angry at tana_near
    with dissolve
    "[mcname!c]" "Enggak..."
    hide tana_angry at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left 
    with dissolve
    tana "Terus lu mau apa?"
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana_angry at tana_near
    with dissolve
    "[mcname!c]" "Mau ngambil sampel tanah aja."
    hide tana_angry at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left 
    with dissolve
    tana "Oh yauda."
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana_angry at tana_near
    with dissolve
    "[mcname!c]" "......"
    show tana_side_angry at left with dissolve
    tana "......"
    hide tana_side_angry at left with dissolve
    "[mcname!c]" ".............."
    show tana_side_angry at left with dissolve
    tana "................"
    hide tana_side_angry at left with dissolve
    "[mcname!c]" "Tan..."
    hide tana_angry at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left 
    with dissolve
    tana "Apa."
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana_angry at tana_near
    with dissolve
    "[mcname!c]" "Sebenarnya gua mau minta maaf..."
    show tana_side_angry at left with dissolve
    tana "......."
    hide tana_side_angry at left with dissolve
    "[mcname!c]" "Gua mau minta maaf perkara video kemarin. Gua asli ga ada maksud buat nyebarin."
    hide tana_angry at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left 
    with dissolve
    tana "Banyak alasan, lu. Bilang aja lu mau ngeledekin gua, kan?"
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana_angry at tana_near
    with dissolve
    "[mcname!c]" "Nggak, Tan. Serius. Gua cuma ngerasa kalau lu lucu banget pas itu. Jadinya gua rekam."
    hide tana_angry at tana_near
    show tana_confused at tana_near
    show tana_side_confused at left 
    with dissolve
    tana "Eh?"
    hide tana_confused at tana_near
    hide tana_side_confused at left 
    show tana_shock at tana_near
    show tana_side_shock at left
    with dissolve
    tana "EEH????"
    hide tana_side_shock at left with dissolve
    "[mcname!c]" "???"
    hide tana_shock at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left 
    with dissolve
    tana "KAN?! LU NGELEDEKIN GUA LAGI!"
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana_angry at tana_near
    with dissolve
    "[mcname!c]" "{i}Astaga, nih orang ngamuk mulu dah perasaan.{/i}"
    hide tana_angry at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left 
    with dissolve
    tana "LU KE SINI CUMA BUAT NGELEDEKIN GUA DOANG KAN?!"
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana_angry at tana_near
    with dissolve
    "[mcname!c]" "NGGAK, KOCAK. GUA JUJUR KOK INI. GUA SALAH MULU DAH PERASAAN."
    hide tana_angry at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "HALAH. SKEM. LU SKEM!"
    tana "UDAH LAH. GA USAH SOK-SOK AN MINTA MAAF!"
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana_angry at tana_near
    with dissolve
    "[mcname!c]" "Eh, Tana! Tunggu, jangan pergi dulu. Gua belum selesai ngo-"
    hide tana_angry at tana_near
    show tana_confused at tana_near
    show tana_side_confused at left 
    with dissolve
    tana "Eh?"
    hide tana_side_confused at left
    hide tana_confused at tana_near
    show tana kepeleset at chibi_tono
    show tana_side_shock at left 
    with dissolve
    tana "AAAAAAA!!"
    hide tana_side_shock
    hide tana kepeleset
    with dissolve
    play sound "SFX - Fall Water.WAV" volume (4.0)
    show tana_shy at tana_near
    show tana_side_shy at left 
    with dissolve
    tana "........."
    hide tana_side_shy at left with dissolve
    "[mcname!c]" "........."
    show tana_side_shy at left with dissolve
    tana "....................."
    hide tana_side_shy at left with dissolve
    "[mcname!c]" "Pfffft."
    show tana_side_shy at left with dissolve
    tana "...................................."
    hide tana_side_shy at left with dissolve
    "[mcname!c]" "Sini gua bantu."
    hide tana_shy at tana_near with dissolve
    "[mcname!c] mengulurkan tangannya untuk membantu Tana berdiri."
    "Tapi tiba-tiba..."
    show tana narik at chibi_tono with dissolve
    "[mcname!c]" "Eh?"
    hide tana narik with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    $ quick_menu = True
    play sound "SFX - Fall Water.WAV" volume (4.0)
    "[mcname!c]" "AAAAAAAAA!!!"
    $ quick_menu = False
    scene sawah sore with Dissolve(1.0)
    with dissolve
    $ quick_menu = True
    "[mcname!c]" "......."
    show tana_laugh at tana_near 
    show tana_side_laugh at left
    with dissolve
    tana "HAHAHAHAH!!!"
    hide tana_side_laugh at left with dissolve
    "[mcname!c]" "SI KOCAK MALAH KETAWA!"
    "[mcname!c]" "LU KALO NYEMPLUNG SENDIRIAN AJA GA USAH NGAJAK-NGAJAK!"
    show tana_side_laugh at left with dissolve
    tana "HAHAHAHAHHAHAHAAHHAHAH!"
    hide tana_side_laugh at left with dissolve
    "[mcname!c]" "Yah... Udah kena nih otaknya."
    "[mcname!c]" "Tapi lu ga kenapa-kenapa, Tana?"
    hide tana_laugh at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left 
    with dissolve
    tana "Hahahahah. Gua aman, lu gimana?"
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Gua gapapa, tapi baju gua yang apa-apa!"
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left 
    with dissolve
    tana "Sori dah, sori."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "....."
    hide tana at tana_near
    show tana_shy at tana_near
    show tana_side_shy at left 
    with dissolve
    tana "....."
    hide tana_side_shy at left
    with dissolve
    "[mcname!c]" "Nggak, Tan. Gua yang minta maaf. Gua serius ga ada maksud\napa-apa ngerekam lu dance."
    hide tana_shy at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left 
    with dissolve
    tana "Hadehh... Iya iya. Gua percaya deh."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Serius?"
    hide tana at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left 
    with dissolve
    tana "Serius. Masa lu ga percaya sama gua?"
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana_angry at tana_near
    with dissolve
    "[mcname!c]" "Terakhir lu bilang gitu, kita nyasar sampe sore."
    hide tana_angry at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left 
    with dissolve
    tana "NGGAK, KOCAK. ITU GUA CUMA MAU JALAN-JALAN AJA."
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana_angry at tana_near
    with dissolve
    "[mcname!c]" "Hahahah! Iya dah, iya."
    "[mcname!c]" "Tapi seriusan nih. Lu maafin gua apa nggak?"
    hide tana_angry at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left 
    with dissolve
    tana "Iya, kocak. Apa gua ngamuk lagi aja?"
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana_angry at tana_near
    with dissolve
    "[mcname!c]" "Ampun ampun."
    hide tana_angry at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left 
    with dissolve
    tana "Gitu dong~"
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Btw makasih juga ya udah ngizinin gua ke dosen."
    hide tana at tana_near
    show tana_confused at tana_near
    show tana_side_confused at left 
    with dissolve
    tana "Ha? Ngizinin apaan?"
    hide tana_side_confused at left
    hide tana_confused at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Lah? Kan kemari gua minta tolong lu buat sampein izin sakit ke dosen."
    hide tana at tana_near
    show tana_confused at tana_near
    show tana_side_confused at left 
    with dissolve
    tana "Kaga. Gua kagak nyampein apa-apa."
    hide tana_side_confused at left
    hide tana_confused at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "LAHK?! KOK ABSENSI GUA MASIH FULL?"
    hide tana at tana_near
    show tana_laugh at tana_near
    show tana_side_laugh at left 
    with dissolve
    tana "Kemarin kaga ada kelas, kocak. Dosennya ada urusan dadakan."
    hide tana_side_laugh at left
    hide tana_laugh at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "......"
    "[mcname!c]" "Hadeh, yauda lah ya. Terima aja ucapan terima kasih gua."
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left 
    with dissolve
    tana "Iya dehh, iyaa. Gua juga minta maaf soalnya udah berlebihan marah sama lu."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "......."
    hide tana at tana_near
    show tana_shy at tana_near
    show tana_side_shy at left 
    with dissolve
    tana "........."
    hide tana_side_shy at left with dissolve
    "[mcname!c]" ".................."
    hide tana_shy at tana_near
    show tana_shock at tana_near
    show tana_side_shock at left 
    with dissolve
    tana "K-kenapa lu diem aja?"
    hide tana_side_shock at left
    hide tana_shock at tana_near
    show tana_shy at tana_near
    with dissolve
    "[mcname!c]" "T-tan..."
    hide tana_shy at tana_near
    show tana_shock at tana_near
    show tana_side_shock at left 
    with dissolve
    tana "A-apa?"
    hide tana_side_shock at left
    hide tana_shock at tana_near
    show tana_shy at tana_near
    with dissolve
    menu:
        "Kamu ngomong:"
        "Kamu lucu banget di video itu.":
            jump chapter2tanaTRUE
        "Dance lu keren banget di video itu.":
            jump chapter2tanaGOOD
