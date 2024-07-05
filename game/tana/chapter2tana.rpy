label chapter2tana:
    $ quick_menu=True
    play music "audio/bgm_harvestmoon_spring.mp3" fadein 1.0
    scene awan with dissolve
    "Keesokan paginya, Tana berangkat menuju kampus seperti biasanya."
    $ quick_menu=False
    scene kelas with dissolve
    $ quick_menu=True
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    "Sesampainya di depan pintu ruang kelas, Tana mendengar keramaian dari dalam kelas."
    show tana at tana_near with dissolve
    show tana_side at left with dissolve
    tana "Anak-anak rame banget deh di dalam. Ada apa, ya?"
    hide tana_side
    "Penasaran dengan keramaian tersebut, Tana pun membuka pintu kelas."
    "Setelah pintu kelas terbuka dan para Mahasiswa/i melihat Tana di depan pintu, ada beberapa mahasiswa yang berteriak."
    #Sprite RG Hasan
    "RG Hasan" "Guys, ini dia dancer andalan kita!"
    "RG Hasan" "Hahahaha!"
    #Sprite Bang Rama
    "Bang Rama" "onoT, kamu centil banget sih!"
    "Bang Rama" "Hahahaha!"
    "Tana pun kebingungan dan mencoba memahami kejadian yang sedang terjadi di depan matanya ini."
    show tana_side at left with dissolve
    tana "Hah?! Centil?! Centil apaan kocak! Gausah ngadi-ngadi lu pada!"
    hide tana_side at left with dissolve
    "RG Hasan" "Alah alahh... Sa ae lu, Tana. Kita udah liat videonya."
    "RG Hasan" "Hahahaha!"
    "Tana pun semakin bingung dengan video apa yang dimaksud oleh teman-temannya. Dengan wajah bingung dan panik, Tana pun bertanya pada temannya."
    show tana_side at left with dissolve
    tana "V-video apa?"
    hide tana_side at left with dissolve
    "Bang Rama" "Hadeh. Video ini loh."
    "Mahasiswa itu pun menyodorkan handphone nya ke Tana untuk menunjukkan video yang dimaksud."
    "Tana pun mengambil handphone tersebut dan melihat video yang menjadi sumber keramaian di pagi hari ini."
    "Dalam video tersebut, tampak gadis remaja berambut merah, semerah cabe, sedang menari dengan indah gemulai."
    "Tana merasa bahwa ia pernah melihat gadis tersebut. Kemudian ia pun tersadar bahwa gadis yang ada dalam video tersebut adalah dirinya saat bermain di mall kemarin."
    "Dengan nada pelan dan suara gemetar, Tana pun berkata..."
    show tana_side at left with dissolve
    tana "I-ini kan aku, t-tapi kok bisa? Siapa yang ngerekam?"
    hide tana_side at left with dissolve
    "Mata Tana pun tertuju pada bagian pojok kiri atas layar handphone yang menunjukkan username (MC+random number). Di saat yang bersamaan, terdengar bunyi pintu kelas terbuka."
    mcname "Pagi, gais."
    "Melihat [mcname] memasuki kelas, mata Tana langsung menatap [mcname] dengan tajam dan dengan rasa marah, ia menghampiri [mcname] dan berteriak."
    show tana_side at left with dissolve
    tana "MAKSUD LO APA?!"
    hide tana_side at left with dissolve
    mcname "!!??"
    "MC pun kaget sekaligus bingung."
    mcname "Lah, gua salah apa? Gua baru masuk, kenapa udah lu marahin aja?"
    tana "LO NGAPAIN NGEREKAM GUA NGE-DANCE KEMARIN?! NGAPAIN JUGA LU NYEBARIN VIDEONYA?"
    mcname "Lah? Kan gua udah minta izin ke elu."
    tana "MANA ADA LU MINTA IZIN KE GUA?! GA USAH BOONG DEH, LU! MAKSUD LU APAAN?!"
    mcname "Gua serius ga ada maksud apa-apa, Tan."
    tana "LAH TERUS KENAPA SEMUANYA PADA TAU? PASTI LU YANG NYEBARIN KAN?"
    mcname "Hah mana ada? Gua cuma bikin Instastory." 
    mcname "Gua juga ga nyangka kalo anak-anak tau Instagram gua dan videonya jadi viral."
    tana "GA USAH BOHONG LU, MC!"
    mcname "DIBILANGIN GUA GA ADA MAKSUD APA-APA! GUA CUMA NGEREKAM, SOALNYA LU KELIATAN LUCU. UDAH GITU DOANG!"
    "Mendengar Tana yang terus menerus marah, emosi MC pun akhirnya juga ikut tersulut."
    tana "Eh?"
    "Mendengar hal tersebut, Tana pun kaget dan sedikit tersipu malu."
    "Suasana di dalam ruang kelas sudah terlanjur hening. Seluruh mata tertuju pada Tana dan [mcname], tidak ada yang berani ikut campur."
    tana "HALAH, {i}KAKEHAN ALASAN!{/i} (BANYAK ALASAN!)"
    #SFX Slam door
    hide tana with dissolve
    "Tana yang sudah terlanjur marah dan merasa malu pun akhirnya memilih untuk keluar dan bolos kelas."
    mcname "Dih, apaan sih Si Tana..."
    "Suasana kelas menjadi hening. Mahasiswa/i merasa canggung karena keributan yang terjadi."
    "RG Hasan" "Parah, gara-gara lu sih."
    "Bang Rama" "Apaan, elu juga padahal."
    mcname "............."
    $ quick_menu=False
    scene black with dissolve
    scene kelas with dissolve
    $ quick_menu=True
    play music "audio/BGM_Dosen + Rektor.mp3" fadein 1.0
    "Tidak lama kemudian, dosen pun masuk ke dalam kelas dan waktu mata kuliah pun dimulai."
    show dosen at dosen_center with dissolve
    dosen "Selamat pagi, semuanya!"
    dosen "Kelas akan saya mulaim ya."
    dosen "Hari ini kita akan membahas tentang..."


    $ quick_menu=False
    scene awan with dissolve
    play music "audio/bgm_harvestmoon_spring.mp3" fadein 0.5
    show text "{size=+10} KEESOKAN HARINYA {/size}" with Pause(2.0)
    scene kelas with Dissolve(2.0)
    $ quick_menu=True
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    "Jadwal kuliah hari ini hanya ada satu kelas praktikum jam 8 pagi, tapi seluruh mahasiswa disuruh untuk berkumpul di kelas karena akan ada arahan dari Bu Dosen."
    "[mcname] pun datang lebih pagi dan memilih untuk belajar di dalam kelas sembari menunggu kelas dimulai."
    mcname "Hadeh, susah banget deh mata kuliah ini. Kok bisa ada kating yang dapet nilai A. Ini gua yang bodoh atau gimana dah."
    "Mendekati waktu praktikum dimulai, [mcname] semakin banyak Mahasiswa/i yang masuk ke dalam kelas."
    "Tetapi, [mcname] tidak melihat adanya Tana di kelas."
    mcname "Kelas udah mau mulai, tapi Tana kok belum datang ya? Nih anak mau bolos lagi, apa?"
    "Tak lama kemudian, terdengar suara orang berlari di lorong yang disusul dengan suara terbukanya pintu kelas."
    show tana at tana_near with dissolve
    tana "*Terengah-engah*"
    tana "Huft, hampir aja gua telat. Dasar jam alarm kocak. Bisa-bisanya bunyinya pelan banget."
    tana "Masih ada bangku kosong ga, ya?"
    "Tana pun melihat ke seluruh bagian kelas untuk mencari apakah ada bangku yang masih kosong."
    tana "Ah, untung ada bangku kosong."
    "Tanpa berpikir panjang, Tana pun langsung berjalan menuju kursi tersebut."
    $ quick_menu=False
    scene black with dissolve
    scene kelas with dissolve
    show tana at tana_near with dissolve
    $ quick_menu=True
    "Sesampainya di bangku tersebut, Tana baru menyadari bahwa ternyata di sebelah bangku itu ada [mcname] yang sudah duduk terlebih dahulu."
    "[mcname] terdiam, menatap Tana yang hendak duduk di bangku kosong tersebut."
    mcname "{i}Nih anak mau duduk sebelah gua?{/i}"
    tana "{i}Haduh, gua baru inget kalo dia biasa duduk di situ.{/i}"
    mcname "..."
    tana "..."
    mcname "................"
    tana "................"
    menu:
        "Responmu:"
        "Duduk Tana":
            mcname "Duduk Ta-"
        ".................":
            mcnamne "................."
    "Sambil mengalihkan pandangan, Tana menemukan bangku kosong lain yang berada tidak jauh dari tempatnya sekarang."
    "Tanpa berkata apapun, Tana pergi meninggalkan MC dan langsung duduk di bangku tersebut."
    mcname "Dih yaudah. Duduk tempat lain aja sono."
    $ quick_menu=False
    scene black with dissolve
    scene kelas with dissolve
    $ quick_menu=True
    play music "audio/BGM_Dosen + Rektor.mp3" fadein 1.0
    "Tak lama kemudian, Bu Dosen pun memasuki kelas."
    show dosen at dosen_center with dissolve
    dosen "Selamat pagi, semuanya!"
    "Mahasiswa/i" "Selamat pagi, Bu!"
    dosen "Udah pada sarapan belum?"
    "RG Hasan" "Belum nih, Bu. Laper, huhu."
    "Bang Rama" "Udah tadi ngemil {i}Pramog{/i}, Bu."
    dosen "Ada-ada aja kalian ini, hahaha."
    dosen "Yaudah. Kalau ada yang bawa bekal, dimakan aja gapapa."
    dosen "Saya cuma mau menyampaikan beberapa hal terkait materi praktikum yang pertama."
    "Mahasiswa/i" "Baik, Bu."
    "Sebagian Mahasiswa/i yang membawa bekal pun akhirnya mengeluarkan bekal untuk dimakan sembari mendengarkan penjelasan dari Bu Dosen."
    dosen "Baik, untuk praktikum minggu depan, masing-masing Mahasiswa dan Mahasiswi harus menyiapkan sampel tanah."
    mcname "Tanah? Untuk apa kita mengumpulkan tanah, Bu?"
    dosen "Iya, tanah."
    dosen "Nanti sampel tanah yang telah kalian dapatkan, akan diuji untuk mengetahui index kesuburan dan apa saja kandungan di tanah tersebut."
    dosen "Jadi, kalian nanti akan belajar bagaimana cara menganalisis tanah."
    mcname "Nanti kita ngambil sampel tanahnya di mana, Bu? Apakah tempatnya bebas?"
    dosen "Sampel tanah bisa diambil dari sawah di kampus, ya. Kalian sudah ke sana, kan?"
    "Mahasiswa/i" "Sudah, Bu!"
    dosen "Nah, kalian ambil dari sana aja."
    dosen "Nanti data yang kalian peroleh bisa dibandingkan dengan data-data milik kakak tingkat kalian untuk mengetahui apakah ada perbedaan antara data yang kalian peroleh dengan data sebelumnya."
    "Mahasiswa/i" "Baik, Bu!"
    mcname "Bu, akses ke sawah apakah bebas?"
    dosen "Bebas. Seinget saya, akses pagar sawah diatur oleh kakak tingkatmu yang saya lupa namanya."
    "Sebelum [mcname] sempat menjawab kembali, tiba-tiba Tana yang masih kesal dengan kejadian kemarin pun nyeletuk."
    show tana at tana_right with dissolve
    #Kurang Kanan. Mau di sebelah kanan dosen.
    tana "Nanya mulu lu, [mcname]. Kayak wartawan."
    "Mendengar hal tersebut, [mcname] pun jadi ikut kesal."
    mcname "Bu, mau tanya lagi. kalau tanahnya warna merah, boleh ga?"
    dosen "Tanah merah? Memangnya di sawah kampus ada tanah yang warnanya seperti itu?"
    mcname "Ada, Bu. Kemarin ada pas tour ke sawah."
    mcname "Tanahnya merah dan putih, terus ada coklat-coklatnya gitu."
    "RG Hasan" "[mcname], emang kapan ada tanah yang warnanya kayak gitu?"
    mcname "Lah, ada tau. Kan pas itu kalian juga liat."
    "Bang Rama" "Emang tanah apaan? Perasaan ga ada deh."
    mcname "Tanah Nona nyemplung ke sawah."
    "Mendengar hal tersebut, seluruh mahasiswa di dalam kelas termasuk Bu Dosen pun tertawa terbahak bahak."
    "Mahasiswa/i" "HAHAHAHAHAHAHA!"
    "RG Hasan" "HAHAHAHAHHA!"
    "Bang Rama" "HAHAHAHAH!"
    tana "Apa sih, kocak! Berisik deh!"
    dosen "Hahahaha. Ada-ada saja. Oke, kalau begitu, kalian jangan lupa untuk mengambil sampel, ya."
    dosen "Kalian bebas mau ambil sampelnya kapan, yang penting disimpan di wadah tertutup dan dibawa pada saat praktikum."
    "Mahasiswa/i" "Baik, Bu!"
    dosen "Ya udah, itu saja dari saya. Kelas sudah selesai. Terima kasih. Saya duluan, ya."
    "Mahasiswa/i" "Terima kasih, Bu!"
    "Setelah Bu Dosen meninggalkan kelas, seluruh Mahasiswa/i satu per satu pergi meninggalkan kelas karena sudah tidak ada mata kuliah lagi hari ini."

    $ quick_menu=False
    scene black with Dissolve(1.5)
    play music "audio/BGM_Lorong.mp3" fadein 1.0
    scene lorong with dissolve
    $ quick_menu=True
    "RG Hasan, Bang Rama, dan [mcname] berjalan bersama di lorong."
    "RG Hasan" "Oi, [mcname]. Lu ga laper, apa?"
    mcname "Laper sih sebenarnya. Gua belum sarapan soalnya."
    "Bang Rama" "Yaudah, ayok ke kantin dah. Gua juga laper nih."
    mcname "Hayuk~"

    $ quick_menu=False
    play music "audio/bgm_kantin.mp3" fadein 1.0
    scene kantin with dissolve
    $ quick_menu=True
    "Sesampainya di kantin, [mcname] mencari tempat duduk kosong terlebih dahulu."
    mcname "Tuh ada yang kosong. Di situ aja."
    "RG Hasan" "Yaudah gua aja yang jaga tempatnya, lu cari makan dulu."
    mcname "Bang Rama, lu ga nyari sekalian?"
    "Bang Rama" "Entar deh. Gua lagi ada panggilan, nih."
    mcname "Oke deh."
    "[mcname] pun berjalan mengelilingi kantin untuk melihat makanan dan minuman apa saja yang dijual di dalam kantin."
    mcname "Enaknya beli apa, ya? Makan yang pedes-pedes kayanya enak nih."
    mcname "Nah, ada yang banyak logo cabenya tuh. Kayanya jual makanan pedes-pedes, deh."
    "[mcname] menghampiri penjual tersebut dan mulai memesan makanan."
    mcname "Pak! Pesen mie pedes satu porsi, sama es jeruk."
    "Penjual" "Baik, totalnya 24 ribu, kak."
    mcname "Uang saya 50 ribu, pak. Ada kembalian ga?"
    "Penjual" "Receh gapapa?"
    mcname "Gapapa, Pak. Asal lucu 🙏🏻"
    "Penjual" "Hahahaha. Siap. Mohon ditunggu sebentar, ya."
    mcname "Baik, Pak."
    "MC pun menunggu hingga pesanan selesai dibuat."
    $ quick_menu=False
    scene black with dissolve
    scene kantin with dissolve
    $ quick_menu=True
    "Tak lama kemudian, Tana datang berjalan menuju tempat penjual yang sama seperti [mcname] dan mata mereka saling bertemu."
    show tana at tana_near with dissolve
    tana "......"
    mcname "......"
    tana "..................."
    mcname "..................."
    hide tana with dissolve
    "Tana pun langsung berjalan melewati [mcname] dan pergi ke luar kantin."
    mcname "Idih, ngambekan."
    "Penjual" "Kak, ini pesenan sama kembaliannya."
    mcname "Oke. Terima kasih, Pak!"
    mcname "Wwaktunya balik ke meja tadi terus makan, deh."
    $ quick_menu=False
    scene black with dissolve
    scene kantin with dissolve
    $ quick_menu=True
    "Sesampainya di meja..."
    mcname "Lah? Ke mana nih bocah-bocah? Bukannya tadi mereka ngomong kalo mau duduk di sini, ya?"
    mcname "Hmmm kalo sendirian gini, mending gua pulang terus makan di kos."
    mcname "Hadeh..."

    $ quick_menu=False
    scene black with dissolve
    scene awan with dissolve
    show text "{size=+10}KEESOKAN HARINYA{/size}" with Pause(2.0)
    play music "audio/bgm_harvestmoon_spring.mp3" fadein 0.5
    scene mc bedroom with dissolve
    play music "audio/backsound_kamar.mp3" fadein 0.5
    $ quick_menu=True
    mcname "Aduh. Mules banget nih perut. Kesalahan nih kebanyakan makan pedes-pedes kemarin."
    mcname "Haduuh. Udah pasti telat nih buat mata kuliah pertama. Gua telpon titip izin dosen ke anak-anak dah."
    "MC pun membuka daftar kontak di handphone-nya."
    mcname "LAH?! KOK CUMA ADA SI TANA?!"
    mcname "Oh iya, gua lupa minta nomor ke anak-anak. Gua cuma punya Discord mereka. Mana internetnya jelek banget lagi di Kos."
    mcname "Bodoh banget sih gua. Masa gua harus minta tolong ke Tana? Males banget."
    mcname "......"
    mcname ".........."
    mcname "................"

    menu:
        "Kamu..."
        "Malas":
            mcname "Dih, males banget telepon Si Tana. Mending gua meninggoy."
            "[mcname] pun menaruh handphone-nya dan berjalan untuk mencari obat."
            mcname "Obat gua di mana ya?"
            #SFX Kepeleset
            mcname "Eh?"
            #SFX Bruk (Jatuh)
            stop music fadeout 1.0
            scene black with dissolve
            show text "{color=#FFF}[mcname] MENINGGAL TERPELESET GARA-GARA MENGINJAK KRESEK PLASTIK BEKAS MAKANAN SEMALAM YANG TIDAK IA BERESKAN.{/color}" with Pause(2.0)
            show text "{color=#FF0000}BAD END{/color}"
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits
        "Telepon Tana":
            mcname "Yaudah lah. Daripada absen gua ngurang, terus ga bisa ikut ulangan."
            "#Show UI Telepon"
            "MC pun mencoba menelpon Tana."
            #SFX Kring Kring (Telepon)
            "Memanggil di UI Telepon HP"
            mcname "Angkat lah woy."
            "Tana tidak mengangkat panggilan telepon dari [mcname]."
            mcname "Hadeh. Pasti Tana masih marah gara-gara video kemarin. Kan gua ga maksud apa-apa. Coba telepon lagi deh."
            #SFX Kring Kring
            "Memanggil di UI Telepon HP"
            "Lagi telepon di UI Telepon HP"
            show tana_side at left
            tana "Ha?"
            mcname "{i}Damn, cuek banget.{/i}"
            tana "......"
            mcname "{i}Fix masih marah, tapi untung diangkat.{/i}"
            tana "................."
            mcname "{i} Masa gua harus minta maaf dulu? Gua ga salah apa-apa juga.{/i}"
            tana ".................................."
            "#Tit... tit... \nUI Telepon diputus"
            "MC pun menelepon Tana lagi untuk yang ketiga kalinya."
            #SFX Kring Kring
            "Memanggil di UI Telepon HP"
            "Lagi telepon di UI Telepon HP"
            tana "LU NGAPAIN SIH?! LU NGEPRANK GUA YA?! GUA MATIIN DAH!"
            mcname "JANGAN! JANGAN! SORI, GUA TADI NGELAMUN."
            tana "Terus mau lu apa?"
            mcname "Gua mau minta tolong buat nanti izinin ke dosen kalo gua bakal telat atau bahkan ga ikut kelas. Soalnya gua lagi sakit."
            tana "Males banget. Kenapa harus gua coba yang ngaish tau dosen?"
            mcname "Gua cuma nyimpen nomor lu, Tan. Asli gua ga nyimpen nomor anak-anak. Jadinya gua cuma bisa minta tolong ke lu."
            tana "........."
            mcname "Tan?"
            tana "Ya."
            mcname "Makasih banyak Tan, lu udah mau ngeban-"
            "#Tit... tit... \nUI Telepon diputus"
            mcname "Belom juga kelar ngomong. Udah dimatiin aja."
            mcname "Aduh sumpah sakit banget nih perut. Sampe pusing kepala gua."
            "[mcname] pun meringkuk dengan pasrah di lantai sambil merasa kesakitan."
            mcname "Gua skip kuliah dulu deh. Mending minum obat terus istirahat daripada tambah parah nih perut."
            mcname "Semoga Tana beneran ngizinin ke dosen..."
    
    $ quick_menu=False
    scene black with dissolve
    scene awan with dissolve
    show text "{size=+10}KEESOKAN HARINYA{/size}" with Pause(2.0)
    play music "audio/bgm_harvestmoon_spring.mp3" fadein 0.5
    scene mc bedroom with dissolve
    play music "audio/backsound_kamar.mp3" fadein 0.5
    $ quick_menu=True
    mcname "Akhh, akhirnya. Perut adem gini kan enak."
    mcname "Btw, ini kenapa kamar gua kotor banget dah?"
    mcname "Hmmm, mumpung kelas hari ini agak siang, gua bersih-bersih kamar dulu dah."
    "MC pun membersihkan kamarnya hingga rapi."
    mcname "Kelar juga nih bersih-bersih kamar, tapi gua belum nyuci baju. Gua rendem dulu aja deh. Jemurnya ntar habis balik dari kampus."
    mcname "Sekarang waktunya mandi, terus gas ke kampus!"

    $ quick_menu=False
    scene black with dissolve 
    with Pause(1.0)
    scene kelas with dissolve
    with Pause(1.0)
    $ quick_menu=True
    "MC memasuki kelas."
    $ quick_menu=False
    scene black with dissolve
    show text "{color=#FFF}SETELAH KELAS SELESAI{/color}" with Pause(2.0)
    scene kelas with dissolve
    $ quick_menu=True
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    mcname "Akh, akhirnya kelar juga nih kelas. Asli ngantuk banget dengerinnya."
    "RG Hasan" "Mending tadi lu tidur aja."
    mcname "Yeuu. Ntar gua jadi bodoh kayak elu dong."
    "Bang Rama" "Hahahahaha!"
    "RG Hasan" "Enak bener tuh mulut kalo ngomong."
    "Bang Rama" "Btw kalian udah pada ambil sampel tanah belum?"
    mcname "Ha? Sampel tanah apaan?"
    "RG Hasan" "Itu tuh, bukti nyata kalo lu yang bodoh."
    mcname "Hah sumpah, yang mana sih?"
    "Bang Rama" "Itu, sampel tanah buat praktikum besok lusa."
    mcname "OH IYA! GUA LUPA!"
    "RG Hasan" "Parahh..."
    "Bang Rama" "Kurang baik apa coba gua ini, udah ngingetin."
    mcname "Hilih."
    "RG Hasan" "Yaudah, lu mau ikut ngambil sampel bareng kita gak? Soalnya besok terakhir."
    mcname "Walah, gua ga bisa kalo sekarang. Gua ambil sampelnya besok aja deh. Soalnya gua harus ngejemur cucian gua."
    "Bang Rama" "Semangat deh anak kos-kosan."
    mcname "Yaudah, gua duluan ya."
    "RG Hasan" "Oke dah."
    "Bang Rama" "Tiati."

    $ quick_menu=False
    play music "audio/BGM_Lorong.mp3" fadein 1.0
    scene lorong with Dissolve(2.0)
    $ quick_menu=True
    mcname "Saatnya pulang terus jemur baju."
    "???" "MC!"
    mcname "Hmm? Siapa yang manggil gua?"
    "???" "Wooiii!"
    $ quick_menu=False
    scene black with dissolve
    scene lorong with dissolve
    $ quick_menu=True
    feni "Dipanggil malah celingak celinguk."
    flora "Parahh."
    mcname "Ah. Kak Feni sama Kak Flora? Ada apa, kak?"
    feni "Si Tana mana?"
    mcname "Tana?"
    mcname "{i}Oh iya. Gua belum bilang makasih ke Tana udah izinin ke dosen.{/i}"
    flora "Nih anak diajak ngomong malah ngelamun."
    mcname "Maaf maaf. Aku ga liat Si Tana, Kak. Dia ngambil mata kuliah umum di kelas lain."
    feni "Yahh. Padahal kita mau ngasih sesuatu ke dia."
    mcname "Ngasih apaan tuh?"
    flora "Ini."
    "Flora memberikan selembar flyer ke [mcname]."
    mcname "Hmm? Lomba dance?"
    flora "Iya! Kita liat video Tana yang dance itu."
    feni "Terus aku sama Flo mikir kalo Tana bisa nih ikut lomba dance. Ya ga, Flo?"
    flora "Betul banget. Kamu juga setuju kan, [mcname]?"
    mcname "{i}Walawe. Ternyata videonya udah kesebar sampe angkatan atas.{/i}"
    mcname "Setuju aja sih, tapi Si Tana kayaknya ga mau ikut deh."
    feni "Lah? Emangnya kenapa?"
    mcname "Dia aja marah-marah pas videonya kesebar..."
    flora "Yah. Gimana dong, Kak mpen? Sayang banget kalo Tana ga ikut."
    feni "Hmmm yaudah. Kamu bawa aja deh flyernya. Nanti tolong kasih ke Tana, ya!"
    mcname "Ehh??!"
    flora "Hahahah. Tolong ya, Mc. Arigatou! Mata ne~"
    "Feni dan Flora pergi meninggalkan MC di lorong."
    mcname "Lah? Kok jadi gua yang disuruh? Hadeehh."
    mcname "Dah lah. Gua harus cepet-cepet balik. Keburu mendung."
    stop music fadeout 1.0

    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}KEESOKAN HARINYA{/color}" with Pause(2.0)
    play music "BGM_Kelas.mp3" fadein 1.0
    scene kelas with dissolve
    $ quick_menu = True
    "Keesokan harinya, [mcname] di kelas. Jadwal [mcname] hari ini sangat padat sehingga [mcname] kewalahan."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with dissolve
    play music "BGM_Lorong.mp3" fadein 1.0
    with Pause(1.0)
    scene lorong sore with dissolve
    $ quick_menu = True
    "Tak terasa hari sudah sore."
    mcname "Kelar juga kelas hari ini. Padet banget jadwalnya dari pagi sampe sore."
    mcname "Mana gua belum ngambil sampel tanah lagi. Harusnya jam segini masih dibuka lah ya."
    "MC pun bergegas pergi ke sawah."
    stop music fadeout 1.0

    $ quick_menu = False
    scene black with dissolve
    play music "bgm_harvestmoon_spring.mp3" fadein 1.0
    scene sawah with dissolve
    $ quick_menu = True
    mcname "Hmm? Itu kan Si Tana. Dia belum ngambil sample juga kah?"
    mcname "Kenapa dia ngambil di spot itu sih. Gua kan rencananya mau ngambil sampel di situ juga. Kalo gini, kan awkward banget jadinya."
    mcname "Apa gua samperin aja ya? Bilang makasih sekalian minta maaf. Atau ga usah? Gua juga ga salah apa-apa kok!"
    
    menu:
        "Apa yang kamu lakukan?"
        "Samperin Tana.":
            "MC pun menghampiri Tana."
            mcname "T-Tan?"
            tana "{i}Lah? Ngapain [mcname] ada di sini?{/i}"
            mcname "........"
            tana "Apa? Mau ngeledekin gua lagi?"
            mcname "Enggak..."
            tana "Terus lu mau apa?"
            mcname "Mau ngambil sampel tanah aja."
            tana "Oh yauda."
            mcname "......"
            tana "......"
            mcname ".............."
            tana "................"
            mcname "Tan..."
            tana "Apa."
            mcname "Sebenarnya gua mau minta maaf..."
            tana "......."
            mcname "Gua mau minta maaf perkara video kemarin. Gua asli ga ada maksud buat nyebarin."
            tana "Banyak alasan, lu. Bilang aja lu mau ngeledekin gua, kan?"
            mcname "Nggak, Tan. Serius. Gua cuma ngerasa kalau lu lucu banget pas itu. Jadinya gua rekam."
            tana "Eh?"
            tana "EEH????"
            mcname "???"
            tana "KAN?! LU NGELEDEKIN GUA LAGI!"
            mcname "{i}Astaga, nih orang ngamuk mulu dah perasaan.{/i}"
            tana "LU KE SINI CUMA BUAT NGELEDEKIN GUA DOANG KAN?!"
            mcname "NGGAK, KOCAK. GUA JUJUR KOK INI. GUA SALAH MULU DAH PERASAAN."
            tana "HALAH. SKEM. LU SKEM!"
            tana "UDAH LAH. GA USAH SOK-SOK AN MINTA MAAF!"
            mcname "Eh, Tana! Tunggu, jangan pergi dulu. Gua belum selesia ngo-"
            tana "Eh?"
            #SFX Kepeleset
            tana "AAAAAAA!!"
            #Chibi Nue Tono Kepeleset
            "*Sret"
            "*Bruk"
            tana "........."
            mcname "........."
            tana "....................."
            mcname "Pfffft."
            tana "...................................."
            mcname "Sini gua bantu."
            "[mcname] mengulurkan tangannya untuk membantu Tana berdiri."
            "Tapi tiba-tiba..."
            mcname "Eh?"
            #Chibi Nue Tono narik MC
            mcname "AAAAAAAAA!!!"
            "*Brukk*"
            mcname "......."
            tana "HAHAHAHAH!!!"
            mcname "SI KOCAK MALAH KETAWA!"
            mcname "LU KALO NYEMPLUNG SENDIRIAN AJA GA USAH NGAJAK-NGAJAK!"
            tana "HAHAHAHAHHAHAHAAHHAHAH!"
            mcname "Yah... Udah kena nih otaknya. Lu ga kenapa-kenapa, Tana?"
            tana "Hahahahah. Gua aman, lu gimana?"
            mcname "Gua gapapa, tapi baju gua yang apa-apa!"
            tana "Sori dah, sori."
            mcname "....."
            tana "....."
            mcname "Nggak, Tan. Gua yang minta maaf. Gua serius ga ada maksud apa-apa ngerekam lu dance."
            tana "Hadehh... Iya iya. Gua percaya deh."
            mcname "Serius?"
            tana "Serius. Masa lu ga percaya sama gua?"
            mcname "Terakhir lu bilang gitu, kita nyasar sampe sore."
            tana "NGGAK, KOCAK. ITU GUA CUMA MAU JALAN-JALAN AJA."
            mcname "Hahahah! Iya dah, iya"
            mcname "Tapi seriusan nih. Lu maafin gua apa nggak?"
            tana "Iya, kocak. Apa gua ngamuk lagi aja?"
            mcname "Ampun ampun."
            tana "Gitu dong."
            mcname "Btw makasih juga ya udah ngizinin gua ke dosen."
            tana "Ha? Ngizinin apaan?"
            mcname "Lah? Kan kemari gua minta tolong lu buat sampein izin sakit ke dosen."
            tana "Kaga. Gua kagak nyampain apa-apa."
            mcname "LAHK?! KOK ABSENSI GUA MASIH FULL?"
            tana "Kemarin kaga ada kelas, kocak. Dosennya ada urusan dadakan."
            mcname "......"
            mcname "Hadeh, yauda lah ya. Terima aja ucapan terima kasih gua."
            tana "Iya dehh, iyaa. Gua juga mionta maaf soalnya udah berlebihan marah sama lu."
            mcname "......."
            tana "........."
            mcname ".................."
            tana "K-kenapa lu diem aja?"
            mcname "T-tan..."
            tana "A-apa?"
            menu:
                "Kamu ngomong:"
                "Kamu lucu banget di video itu.":
                    jump chapter2tanaTRUE
                "Dance lu keren banget di video itu.":
                    jump chapter2tanaGOOD
        "Ambil sampel di spot lainnya.":
            mcname "Bodo amat lah. Gua ga salah apa-apa kok."
            "[mcname] pun mengambil sampel tanah di spot lain."
            mcname "Untung nih sawah gede, jadi banyak spotnya."
            #SFX Kepeleset
            mcname "Eh?"
            #SFX Bruk (Jatuh)
            "[mcname] terpeleset akibat menginjak tanah yang licin."
            stop music fadeout 1.0
            scene black with dissolve
            show text "{color=#FFF}WASPADA TERHADAP SEKITAR{/color}" with Pause(2.0)
            show text "{color=#FF0000}BAD END{/color}"
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits
        "Pulang aja deh.":
            mcname "Dipikir pikir, ngapain juga ngambil sampel tanah. Besok minta temen aja dah."
            $ quick_menu = False
            scene black with dissolve
            show text "{color=#FFF}KEESOKAN HARINYA{/color}" with Pause(2.0)
            play music "BGM_Dosen + Rektor.mp3" fadein 1.0
            scene kelas with dissolve
            $ quick_menu = True
            dosen "Semuanya baris, ya. Tunjukin sampel tanah kalian, baru kalian boleh masuk ruang praktikum."
            mcname "{i}Waduh, gua ga bawa nih. Mana temen-temen pada beda sesi lagi.{/i}"
            dosen "[mcname], mana sampel kamu?"
            mcname "I-itu, Bu. Ketinggalan di kos temen."
            dosen "Oalah, yaudah. Masuk dulu aja."
            mcname "Eh? Saya boleh masuk, Bu?"
            dosen "Masuk? Boleh dong."
            dosen "Masuk daftar mahasiswa yang nilai praktikumnya 0."
            mcname "NOOOOOOOOOOOOOOOOOOO~"
            stop music fadeout 1.0
            scene black with dissolve
            show text "{color=#FFF}MAKANYA KULIAH YANG BENER!{/color}" with Pause(2.0)
            show text "{color=#FF0000}BAD END{/color}"
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits       

label chapter2tanaTRUE:
    tana "L-lucu? Lu bilang kalo gua lucu?"
    mcname "I-iya. Kamu lucu, imut, cantik banget pas itu. Makanya aku rekam."
    tana "L-lu ngeledekin gua lagi, ya?"
    mcname "Yaelah. Masa balik ke awal lagi? Kamu tuh emang selucu itu."
    tana "........."
    tana "M-makasih."
    mcname "{i}Aduh, lucu banget nih anak.{/i}"
    tana "Btw, kamu udah sembuh?"
    mcname "Hmm? Kenapa nih kok nanya? Kamu aslinya peduli kan sama aku?"
    tana "A-apa sih? Aku cuma nanya, kocak!"
    mcname "Hahahaha"
    mcname "Aku udah sehat, kok. Makasih udah nanya."
    "[mcname] mengulurkan tangannya ke kepala Tana."
    tana "????"
    mcname "*Pat-pat Tana*"
    tana "....."
    tana "*Blush*"
    tana "EEH??? N-NGAPAIN LUU?"
    mcname "Hahahaha. Kamu kenapa lucu banget sih jadi orang. Mukanya sampe merah kaya cabe gitu."
    tana "Tangan lu kotor, kocak."
    mcname "Halah. Udah kotor semua ini. Nanggung."
    mcname "*Gosok-gosok kepala Tana*"
    tana "DIH?! AWAS LU YA!!"
    "Tana menyipratkan lumpur ke arah MC."
    mcname "LOH?! NGAJAK PERANG?! AYO!"
    "MC dan Tana saling menyipratkan lumpur layaknya anak kecil yang sedang bermain di sawah."
    tana "Hahahaha!"
    mcname "Hahahahah!"
    mcname "Udah... udah... ampun. Lu yang menang."
    tana "Tana kok dilawan. Gua paling jaog kalo masalah beginian."
    mcname "Dasar anak kampung."
    tana "APA LU BILANG?"
    "Tana melempar lumpur ke arah MC."
    mcname "IYA IYA. AMPUN. GUA CUMA BERCANDA."
    tana "Hmph!"
    mcname "...."
    tana "...."
    "MC dan Tana saling menatap mata satu sama lain sambil tersenyum."
    stop music fadeout 1.0
    scene black with dissolve
    show text "{color=#FFF}CHAPTER III{/color}" with Pause(2.0)
    play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
    jump credits
label chapter2tanaGOOD:
    tana "Keren? Gua?"
    mcname "Iya."
    tana "Lu bilang gua keren?"
    mcname "Hooh."
    tana "HAHAHAHAHA!"
    tana "Iya gua emang sekeren itu."
    mcname "Iya dah, iya."
    tana "Gua udah ngedance dari dulu soalnya."
    mcname "Dari dulu?"
    tana "Eh!"
    stop music fadeout 1.0
    scene black with dissolve
    show text "{color=#FFF}CHAPTER III{/color}" with Pause(2.0)
    play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
    jump credits