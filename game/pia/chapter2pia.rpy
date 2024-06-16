label chapter2piabegin:
    scene black with dissolve
    show text "{color=#FFF}Chapter II{/color}" with Pause(2.0)
    scene black with dissolve
    "Peralatan menggambar sudah siap, Mahasiswa/i baru DKV pun memulai kelas ujian menggambar pertamanya"
    scene kelas with dissolve
    play music "audio/BGM_Dosen + Rektor.mp3" fadein 1.0
    show dosen at dosen_center with dissolve
    show dosen_side at left with dissolve
    $ dosen_name = "Dosen Seni"
    $ quick_menu = True
    dosen "Ya, ujiannya adalah menggambar teman kalian."
    hide dosen_side at left with dissolve
    "Mahasiswa/i" "Heeeeeee, waduh bu"
    show dosen_side at left with dissolve
    dosen "Ibu udah buat undiannya, ya. Kita undi nama pasangan gambar kalian"
    dosen "Jadi nanti kalian hadap-hadapan dan gambar teman di depan kalian"
    dosen " Semua karya tugas ini akan dipajang di sepanjang lorong gedung DKV ini, ya! Tunjukan bakat kalian kepada yang lain!"
    hide dosen_side with dissolve
    hide dosen with dissolve
    show pia at pia_near with dissolve
    show pia_side at left with dissolve
    pia "Hueeeee…..PRESUREEEEE"
    hide pia_side with dissolve
    mcname "Hahaha dapet siapa ya pasangannya~"
    hide pia with dissolve
    show dosen at dosen_center with dissolve
    show dosen_side at left with dissolve
    dosen "[mcname]"
    hide dosen_side with dissolve
    mcname "Hmm…. Yak"
    show dosen_side at left with dissolve
    dosen "Berpasangan sama Pia, ya."
    hide dosen with dissolve
    hide dosen_side with dissolve
    show pia at pia_near with dissolve
    show pia_side at left with dissolve
    pia "YEEEEES! MUAHAHAHA."
    hide pia with dissolve
    hide pia_side with dissolve
    show dosen at dosen_center with dissolve
    show dosen_side at left with dissolve
    dosen "Pia! Jangan berisik."
    hide dosen with dissolve
    hide dosen_side with dissolve
    show pia_sad at pia_near with dissolve
    show pia_side_sad at left with dissolve
    pia "Maaf, bu"
    hide pia_side_sad with dissolve
    "Mahasiswa/i" "Hahahahahahahaha"
    "Semua maba berpindah posisi berhadapan dengan pasangan yang sudah dipilih oleh Bu Dosen."
    $ quick_menu = False
    scene black with dissolve
    scene kelas with dissolve
    show pia at pia_near with dissolve
    show pia_side at left with dissolve
    $ quick_menu = True
    pia "HAI [mcname]! HUEHEHEHEH"
    hide pia_side with dissolve
    mcname "Apalah Pia Pia ini"
    show pia_side at left with dissolve
    pia "Mau gambar aku kayak gimana? Cute? Seksi? Cool?"
    hide pia_side with dissolve
    mcname "Halah, kuping gajah gak sih?"
    show pia_angry at pia_near with dissolve
    show pia_side_angry at left with dissolve
    pia "HEEEEH!!!! Ahahahaha."
    hide pia_side_angry with dissolve
    hide pia_angry with dissolve
    "Mereka pun bergantian setiap 15 menit untuk saling menggambar pasangannya tersebut."
    $ quick_menu = False
    scene black with dissolve
    scene kelas with dissolve
    show pia at pia_near with dissolve
    $ quick_menu = True
    mcname "*Sedang menggoreskan kuas di atas canvasnya sambil memandang Pia.*"
    stop music fadeout 1.0
    play music "audio/BGM_Romance Pia Kamar.mp3" fadein 1.0
    mcname "*dalam hati*"
    mcname "{i}Waduh. Makin diliat, makin imut dan manis ya Pia Pia ini.{/i}"
    mcname "*Sambil melirik melihat wajah samping Pia*"
    show pia_shy at pia_near with dissolve
    pia "*Muka memerah*"
    mcname "Sakit, Pia? ahahaha"
    show pia_side_shy at left with dissolve
    pia "Dieeeeeem! Aku tuh ga biasa dipandangin gini, ih"
    pia "Buru selesaiin gambarnya!!"
    hide pia_side_shy with dissolve
    show pia_angry at pia_near with dissolve
    hide pia_shy with dissolve
    hide pia_side with dissolve
    mcname "Lah sabar, baru sketch weh."
    show pia_side_angry at left with dissolve
    pia "*Huft*"
    $ quick_menu = False
    stop music fadeout 1.0
    jump startPiaGame


label chapter2piaaftergame:
    stop music fadeout 1.0
    scene black with dissolve
    scene kelas with dissolve
    play music "audio/BGM_Dosen + Rektor.mp3" fadein 1.0
    show dosen at dosen_center with dissolve
    show dosen_side at left with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    dosen "Yak! Bisa dikumpulkan ya, tugasnya"
    dosen "Besok akan Ibu pajang semua gambar kalian di lorong gedung ini. Nanti Ibu minta BEM (Badan Eksekutif Mahasiswa) untuk bantuin display dan announce pameran ini untuk umum dan dapat dilihat oleh semua fakultas."
    hide dosen_side with dissolve
    "Mahasiswa 1" "Heeeeeeeee~ Kok jadi pameran gini bu? Malu bu!!"
    show dosen_side at left with dissolve
    dosen "Hehe, ini disebut element of surprise. Biar kalian terbiasa. BANGGALAH DENGAN HASIL KARYA KALIAN SENDIRI!!"
    hide dosen_side with dissolve
    "Mahasiswa 2" "Siaaaaap buuuuuuuu~"
    hide dosen with dissolve
    show pia at pia_near with dissolve
    mcname "Waaaaa malu weh bakal dilihat banyak orang. Kirain cuma buat DKV doang."
    show pia_side at left with dissolve
    pia "Iya weh. Yaudah lah ya"
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with dissolve
    # Harusnya BG Hall
    scene depan kampus with dissolve
    #  Harusnya BGM Hall
    play music "audio/BGM_Kampus.mp3" fadein 1.0
    $ renpy.block_rollback()
    $ quick_menu = True
    "Keesokan harinya, semua karya sudah terpajang di sepanjang lorong dan lobby gedung DKV. Banyak sekali Mahasiswa/i dari fakultas lain yang datang untuk sekedar berswafoto atau menikmati hasil karya Maba DKV layaknya mengunjungi pameran seni."
    "Fiony, Freya, dan Kana sedang berjalan bersama mengunjungi pameran ini."
    show kana at kana_near_left_2 with dissolve
    show freya at freya_near_right with dissolve
    show fio at fio_near with dissolve
    show fio_side at left with dissolve
    fio "Sini-sini, nih hasil karya junior-juniorku."
    hide fio_side with dissolve
    show freya_side at left with dissolve
    freya "Wah bagus baguuuus! Ayo muter-muter mau liat semua."
    hide freya_side with dissolve
    show fio_side at left with dissolve
    fio "Kamu mau ikut juga gak? \n*nunjuk Kana*"
    hide fio_side with dissolve
    show kana_side at left with dissolve
    kana "Boleh deh, mauuuu."
    hide kana_side with dissolve
    show fio_side at left with dissolve
    fio "Aku harus cari punya [mcname] sama Si Meameo itu. Dipajang sebelah mana punya mereka ya?"
    hide fio_side with dissolve
    "{size=-5}Freya & Kana{/size}" "Meameo?"
    show fio_side at left with dissolve
    fio "Oh itu temen aku. Kayaknya kalian ketemu deh pas di cafe. Kalian lupa kali."
    $ quick_menu = False
    scene black with dissolve
    # Harusnya BG Hall
    scene depan kampus with dissolve
    $ quick_menu = True
    "Setelah berkeliling"
    show kana at kana_near_left_2 with dissolve
    show freya at freya_near_right with dissolve
    show fio at fio_near with dissolve
    show kana_side at left with dissolve
    kana "YANG MULIA PIARAAN!!!"
    hide kana_side with dissolve
    show freya_side at left with dissolve
    freya "Kaget, Kana! Apa sih tiba-tiba teriak gitu."
    hide freya_side with dissolve
    show kana_side at left with dissolve
    kana "Ini!! Ini!!! Style gambarnya, gak salah lagi! Ini Yang Mulia Piaraan. Aku suka banget style dia, aku ada beberapa koleksi gambar anime buatan orang ini!"
    kana "Dia masuk DKV kampus kita? OMG OMG, aku harus kenal!"
    hide kana_side with dissolve
    show freya_side at left with dissolve
    freya "Kana, tenang. Tahan aura wibumu. Ini di tempat umum."
    hide freya_side with dissolve
    show kana_side at left with dissolve
    kana "Uhuk… Ehem… Iya makasih, Fre"
    hide kana_side with dissolve
    show fio_side at left with dissolve
    fio "Ah! Ini dia gambar Si Meameo itu"
    hide fio_side with dissolve
    show kana_side at left with dissolve
    kana "Hah? Kak Fiony, ini temen kakak yang dicari dari tadi?"
    hide kana_side with dissolve
    show fio_side at left with dissolve
    fio "Iya, nih gambarnya sebelahan ternyata. Ini [mcname], ini Pia."
    hide fio_side with dissolve
    show kana_side at left with dissolve
    kana "Kak! Kenalin aku sama yang gambar ini!!"
    hide kana_side with dissolve
    show fio_side at left with dissolve
    fio "Pia?"
    fio "Ahaha oke aman. Orangnya lagi gak ada. Kapan-kapan aku kenalin, ya."
    hide fio_side with dissolve
    $ quick_menu = False
    scene black with dissolve
    # Harusnya BG Hall
    scene depan kampus with dissolve
    $ quick_menu = True
    "Akhirnya mereka bertiga pun pergi setelah berkeliling melihat hasil karya anak-anak DKV"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}DITEMPAT LAIN{/color}" with Pause(2.0)
    scene kantin with dissolve
    play music "audio/bgm_kantin.mp3" fadein 1.0 
    "(Suara notif berkali kali)"
    show pia at pia_near with dissolve
    show pia_side at left with dissolve
    $ renpy.block_rollback()
    pia "Weh [mcname]!!! Cepio ngirim foto dia selfie sama gambar kita!!!!"
    hide pia_side with dissolve
    nvl clear
    fio_nvl "P"
    fio_nvl "P"
    fio_nvl "P"
    fio_nvl "P"
    fio_nvl "P"
    fio_nvl "P"
    fio_nvl "{image=cepio selfie.png}"
    $ quick_menu = True
    mcname "Wah, iya. Aku juga baru liat di grup nih, ahaha."
    mcname "Mau nyusulin ke sana, gak?"
    show pia_side at left with dissolve
    pia "Makanan aku baru sampe weh, baru 1 suap! Lagian gak ah, aku maluuuuu."
    hide pia_side with dissolve
    mcname "Dih kok gitu, inget kata Pak Dosen. \"BANGGALAH DENGAN KARYA KALIAN SENDIRI\"\n*niru gaya bicara dan gerakan bu dosen*"
    show pia_side at left with dissolve
    pia "Ahahahaha iya iya iya. Nanti aja abis ini"
    hide pia_side with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    # Harusnya BG Hall
    scene depan kampus with dissolve
    play music "audio/BGM_Kampus.mp3" fadein 1.0
    show pia at pia_near_right with dissolve
    show fio at char_near_left with dissolve
    show pia_side at left with dissolve
    $ quick_menu = True
    pia "CEPIOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
    hide pia_side with dissolve
    show fio_side at left with dissolve
    fio "Emang ya."
    fio "Kalo gak tereak bukan Meameo"
    hide fio_side with dissolve
    show pia_side at left with dissolve
    pia "Apalah Cepio ini."
    hide pia_side with dissolve
    mcname "Ahahahahaha"
    show fio_side at left with dissolve
    fio "Ih tadi ada temenku yang mau kenalan sama kamu pas liat gambar kamu, tau"
    hide fio_side with dissolve
    show pia_side at left with dissolve
    pia "Oh iya, kah? Mana orangnya?"
    hide pia_side with dissolve
    show fio_side at left with dissolve
    fio "Telaaat"
    fio "Udah pulang mereka"
    hide fio_side with dissolve
    "{size=-5}[mcname] & Pia{/size}" "Yaaaaaaaaah"
    show fio_side at left with dissolve
    fio "Nanti aku kenalin deh, ya"
    hide fio_side at left with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    scene depan kampus with dissolve
    "[mcname], Pia, dan Fiony pun berbincang panjang lebar sampai sore hari dan memutuskan untuk mengakhiri hari itu dan pulang."
    scene black with dissolve
    show text "{color=#FFF}1 MINGGU KEMUDIAN{/color}" with Pause(2.0)
    scene kelas with dissolve 
    show dosen at dosen_center with dissolve
    show dosen_side at left with dissolve
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    dosen "--jadi, persiapkan diri kalian. Mulai besok masuk minggu UTS, belajar dan asah skill kalian. Istirahat yang cukup. Semoga hasilnya memuaskan, ya."
    "Mahasiswa/i" "Baik buuuu"
    scene black with dissolve
    scene kelas with dissolve
    show pia at pia_near with dissolve
    show pia_side at left with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    pia "Weeeeh besok udah mulai UTS. Tugas menggambar bebas kamu udah selese, [mcname]?"
    hide pia_side with dissolve
    mcname "Belom nih. Stuck gak dapet ide mau gambar apa. Kamu udah, Pi?"
    show pia_side at left with dissolve
    pia "Udah jadi dikit sih, hehehe."
    pia "Aku tuh gasuka nunda pekerjaan, mau cepet selese pokoknya."
    hide pia_side with dissolve
    mcname "Mana liat gambarnya?"
    show pia_side at left with dissolve
    pia "Gaboleeeee weeeeeks."
    hide pia_side with dissolve
    mcname "Dih"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}Keesokan Harinya{/color}"
    # Harusnya BG Hall
    scene depan kampus with dissolve
    # Harusnya BGM Hall
    play music "audio/BGM_Kampus.mp3" fadein 1.0
    show feni at char_center with dissolve
    show feni_side at left with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    feni "Flyernya kakak\n*sambil bagiin flyer*"
    hide feni_side with dissolve
    mcname "Oh ah. Makasih, kak"
    mcname "{i}Flyer apa ini?{/i}"
    "[mcname] melihat ada 3 flyer yang dibagikan ke orang yang lewat"
    "Flyer 1, acara jejepangan yang akan berlangsung beberapa bulan lagi\nFlyer 2, recruitment anggota club jejepangan\nFlyer 3, recruitment anggota idol dari club jejepangan"
    mcname "Simpen dulu deh. Siapa tau temen ada yg butuh."
    mcname "Saatnya ngerjain tugas gambar. Minggu ini dikumpulin buat UTS. Ayo semangat akuuuuu!!!"
    mcname "Ke rooftop, ah. Nyari inspirasi gambar."
    $ quick_menu = False
    scene black with dissolve
    $ quick_menu = True
    mcname "Eh, udah ada orang di rooftop ya…"
    mcname "Gak jadi ke rooftop deh"
    "*denger suara lagu (migikata)"
    mcname "Hmm ngintip dikit kali, ya? Pengen liat siapa."
    mcname "*buka pintu ke rooftop*"
    $ quick_menu = False
    # Harusnya BG Rooftop
    scene depan kampus with dissolve
    $ quick_menu = True
    mcname "Woaaa...."
    mcname "P-Pia............."
    show pia_shy at pia_near with dissolve
    show pia_side_shy at left with dissolve
    pia "Kyaaaa...eh!!!! [mcname]!!!!!! NGAPAIN KAMU!?\n*blush*"
    hide pia_side_shy with dissolve
    mcname "Err....maaf ganggu. Aku lagi nyari inspirasi gambar aja sih, hehe."
    show pia_side_shy at left with dissolve
    pia "Udah lama kamu di situ????? Kamu gak liat kan, aku lagi ngapain disini??"
    hide pia_side_shy with dissolve
    mcname "Ummm...."
    show pia_side_shy at left with dissolve
    pia "...."
    hide pia_side_shy with dissolve
    mcname "G-gak liat, kok"
    show pia at pia_near with dissolve
    show pia_side at left with dissolve
    pia "Fuih....good! Yaudah sini atuh gambar. Punya aku udah selese, hehehe."
    hide pia_side with dissolve
    mcname "Weeeh... Rajin ya"
    show pia_side at left with dissolve
    pia "Ya dong!!"
    pia "Aku gituuu, aku..aku"
    hide pia_side with dissolve
    mcname "Kereeeen!\n*Mulai duduk bersila sebelah Pia sambil membuat sketch gambar pemandangan*"
    stop music fadeout 1.0
    play music "audio/BGM_Romance Pia Kamar.mp3" fadein 1.0
    show pia_side at left with dissolve
    pia "Umm........[mcname]. Aku mau cerita dong…"
    hide pia_side with dissolve
    mcname "Ya, cerita apa Pia?\n*sambil lanjut ngerapihin gambarnya*"
    hide pia_side with dissolve
    hide pia_shy with dissolve
    show pia_side_shy at left with dissolve
    pia "Aku.... Aku punya mimpi lain selain jadi seniman, hehe."
    hide pia_side_shy with dissolve
    mcname "Wih mantap, apa tuh?"
    show pia_side_shy at left with dissolve
    pia "Aku mau jadi idol! Aku suka nari, ahahaha"
    pia "Gak cocok, ya?"
    hide pia_side_shy with dissolve
    mcname "Wah gilaaa! Keren banget! Semangat Pia! Kamu pasti bisa!!"
    show pia_side_shy at left with dissolve
    pia "Ehehe! Huhuhu jadi deg-deg an.\n*sambil ganti lagu fav pia di HPnya*"
    hide pia_side_shy with dissolve
    mcname "Percaya diri aja, Pia! Aku yakin kamu pasti bisa! Joget kamu juga bagus kok tadi"
    show pia_side_shy at left with dissolve
    pia "Ehehehe...."
    hide pia_side_shy with dissolve
    show pia_angry at pia_near with dissolve
    show pia_side_angry at left with dissolve
    pia "EEEEH!!! KAMU NGELIAT AKU JOGET TADI??? KATANYA GAK LIAT! AAAAAAAAAA MALUUUUU!!"
    hide pia_side_angry with dissolve
    mcname "Ups.."
    hide pia_angry with dissolve
    show pia_side_shy at left with dissolve
    pia "Huuuuuuuh"
    pia "Dah lah, maluuuuu"
    hide pia_side_shy with dissolve
    mcname "Ngapain malu? Aku yakin kamu bisa jadi idol! Tarian kamu bagus. Suara kamu enak didengar. Kamu juga punya kepribadian yang menyenangkan. Kamu cantik, baik hati,--"
    show pia_angry at pia_near with dissolve
    show pia_side_angry at left with dissolve
    pia "STOOOOOP!!!!!! HEH K-KENAPA JADI MUJI AKU BEGINI!! AKU GA BISA DIGINIIN WEEEH!!"
    hide pia_side_angry with dissolve
    hide pia_angry with dissolve
    mcname "Tapi emang bener, kok! Kamu punya kepribadian yang menurutku cocok jadi inspirasi banyak orang lain diluar sana!"
    show pia_side_shy at left with dissolve
    pia "Ummm....."
    hide pia_side_shy with dissolve
    mcname "*menatap pia lebih dekat*"
    mcname "Aku percaya kamu bisa! Wujudin ya!"
    pia "*Pia dalam hati*"
    pia "{i}KYAAAAAAAAAAA DEKEEEET BAANGET [mcname]! [mcname]! HUH HAH HUH HAH!{/i}"
    show pia_side_shy at left with dissolve
    pia "M-makasih [mcname]! Ehehe aku akan berjuang!"
    pia "Tapi ya ini kan cuma mimpi."
    pia "Ketika bangun dari mimpi, ya…"
    pia "Ngegambar begini deh, haha"
    hide pia_side shy with dissolve
    mcname "Aku akan jadi fans pertama kamu! Jadi yang akan terus mendukungmu dari belakang untuk mengejar mimpimu itu!"
    mcname "Karena...."
    show pia_side_shy at left with dissolve
    pia "Wooeee stoooop weh. Udah, cuma mimpi. Aku sekarang udah nyaman begini."
    $ quick_menu = False
    menu:
        "Aksi Kamu"
        "Ah! Tadi aku dapet flyer ini. *kasih semua flyer* mau ikut gak? ada acara jejepangan beberapa bulan lagi nih. terus itu ada 3 flyer, ada yang recruitment jadi idol juga. mau coba gak?":
            $ pia_ending_route = "Good Ending"
            mcname "Ah! Tadi aku dapet flyer ini. *kasih semua flyer* mau ikut gak? ada acara jejepangan beberapa bulan lagi nih. terus itu ada 3 flyer, ada yang recruitment jadi idol juga. mau coba gak"
            show pia at pia_near with dissolve
            show pia_side at left with dissolve
            pia "Wih, apaan nih?"
            pia "Wah matsuri, ya."
            pia "Terus…"
            pia "Ini rekruitmen club, skip."
            pia "Yang ini…."
            pia "J-jadi idol??"
            pia "Wow recruitment jadi idol?"
            hide pia_side with dissolve
            mcname "Gimana, mau coba?"
            show pia_side at left with dissolve
            pia "Umm… G-gak deh. Biarlah mimpi tetap jadi mimpi, hehe."
            hide pia_side at left with dissolve
            jump chapter2piaafterrooftop
        "Ah! tadi aku dapet flyer ini. *kasih cuma flyer event jejepangan*. nonton yuk nanti!":
            mcname "ah! tadi aku dapet flyer ini. *kasih cuma flyer event jejepangan*. nonton yuk nanti!"
            show pia at pia_near with dissolve
            show pia_side at left with dissolve
            pia "Menarik, tapi pasti…"
            pia "Banyak wibu bau bawang, ahahahaha."
            hide pia_side with dissolve
            mcname "Nerbener yee lu."
            mcname "Mau gak? Kalo mau, lesgo beli tiketnya. Nih udah open."
            show pia_side at left with dissolve
            pia "Berapaan harganya?"
            hide pia_side with dissolve
            mcname "100 ribu pre-salenya. Berarti nanti setelah pre-sale bakal lebih mahal."
            show pia_side at left with dissolve
            pia "Walah! Lesgo buruan beli. Keburu abis presalenya. Aku transfer ke kamu sekarang. Buruan beli."
            hide pia_side with dissolve
            mcname "Otw!!! Sabar"
            "*Pembayaran berhasil*"
            mcname "Dah nih, ya"
            show pia_side at left with dissolve
            pia "Lesgoooooo, huahahaha"
            stop music fadeout 1.0
            scene black with dissolve
            show text "{color=#FFF}*beberapa bulan kemudian, ada gosip beredar bahwa acara jejepangan tersebut gagal dilaksanakan karena promotor acara kabur membawa uang donatur dan sponsor*{/color}" with Pause(2.0)
            show text "{color=#FF0000}BAD END{/color}"
            play music "audio/Dreamcatcher.mp3" fadein 1.0
            jump credits
        "Apapun pilihan kamu Pia, aku akan tetap support kamu mau apapun itu.":
            $ pia_ending_route = "True Ending"
            mcname "Apapun pilihanmu, Pia, aku akan tetap support kamu. Mau apapun itu."
            show pia_side_shy at left with dissolve
            pia "Aww [mcname]"
            show pia at pia_near with dissolve
            hide pia_side_shy with dissolve
            show pia_side at left with dissolve
            pia "Okeh!! Support aku, ya."
            pia "Menjadi.."
            pia "Illustrator handal"
            pia "Siapa tau kan? Jadi komikus handal terus ke Jepang"
            pia "Atau jadi ilustrator terkenal di duniaaa huahahahaha"
            hide pia_side with dissolve
            mcname "Okeee. Siap, Pia"
            show pia_side at left with dissolve
            pia "Ahahahahaha"
            jump chapter2piaafterrooftop


label chapter2piaafterrooftop:
    "Akhirnya [mcname] duduk disebelah Pia sambil melihat pemandangan dari rooftop melihat jauh kedepan. Lalu menuangkan pemandangan indah itu dalam sebuah lukisan. tugas gambar [mcname] untuk UTS, selesai."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    scene mc bedroom with dissolve
    play music "audio/BGM_Kosan 2.mp3" fadein 1.0
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname] pulang, duduk di meja belajarnya sambil mulai mengeluarkan buku-buku dan catatan materi ujian esok hari.[mcname] fokus bersiap belajar begadang karena besok adalah salah satu ujian mata kuliah tertulis yang paling sulit. Tiba tiba terdengar notifikasi dari handphone [mcname]."
    play sound "audio/ReceiveText.ogg" 
    mcname "(...)"
    play sound "audio/ReceiveText.ogg"
    mcname "(...)"
    play sound "audio/ReceiveText.ogg"
    mcname "Apaan sihh"
    $ quick_menu = False
    stop music fadeout 1.0
    play music "audio/BGM_Happy dan Handphone.mp3" fadein 1.0
    nvl clear 
    pia_nvl "[mcname]!!!! BUKU MATA KULIAH AKU KETINGGALAN DI KAMPUS"
    pia_nvl "BESOK UJIAN INI PULA. GIMANA INI WEH!"
    pia_nvl "P"
    pia_nvl "P"
    pia_nvl "P"
    pia_nvl "P"
    pia_nvl "P"
    pia_nvl "AKU BODOH BANGET LUPA DIBAWA."
    pia_nvl "MAU NANGIS AJA"
    mc_nvl "Wow, sabar. Kamu di mana?"
    pia_nvl "Kosan. Tapi mau nyoba ke kampus, nih."
    mc_nvl "Mana bisa? Jam 6 sore udah tutup kampus, weh."
    pia_nvl "MAMPUS GUE!"
    pia_nvl "GIMANA INI"
    pia_nvl "P"
    pia_nvl "P"
    pia_nvl "P"
    pia_nvl "P"
    pia_nvl "P"
    mc_nvl "STOP P"
    mc_nvl "Sabar, sabar. Mau pinjem buku aku?"
    pia_nvl "KAMU BELAJARNYA GIMANA?"
    mc_nvl "Bener juga… Gimana kalo belajar bareng?"
    pia_nvl "INGFOKAN TEMPAT!! NOW!"
    mc_nvl "Terserah, mau dimana? Cafe x? atau di mana?"
    pia_nvl "Yaudah OTW!"
    stop music fadeout 1.0
    "[mcname] pun bersiap siap untuk pergi ke cafe"
    scene black with dissolve
    show text "{color=#FFF}Beberapa menit kemudian di cafe X *DONATUR Tier2*{/color}" with Pause(2.0)
    scene cafe with dissolve
    play music "audio/BGM_Cafe Sore.mp3" fadein 1.0
    show pia at char_center with dissolve
    show pia_side at left with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    pia "[mcname]! sini!!!"
    hide pia_side with dissolve
    hide pia with dissolve
    show pia at pia_near with dissolve
    mcname "Hadeeeeeh, nih bukunya"
    show pia_side at left with dissolve
    pia "MAKASIH BANGET!!! HUHUHU"
    pia "KALO GAK ADA KAMU, AKU GATAU HARUS GIMANA. AKU GAMAU NGULANG MATKUL INI"
    hide pia_side with dissolve
    mcname "Iya Pia, iya"
    show pia_smile at pia_near with dissolve
    show pia_side_smile at left with dissolve
    pia "Aku berhutang budi sama kamu!!!"
    hide pia_smile with dissolve
    hide pia_side_smile with dissolve
    mcname "Halah lebay"
    show pia_side at left with dissolve
    pia "Karena kamu baik, aku kasih kamu 1 golden tiket ini. Muahahaha\n*insert asset tiket*"
    hide pia_side with dissolve
    mcname "Apaan ini?"
    show pia_side at left with dissolve
    pia "Pake ini buat mengabulkan 1 permintaan. Apapun, akan kulakukan!"
    hide pia_side with dissolve
    mcname "Oke, aku pake sekarang. Sekarang kamu ke depan cafe ini, tereak aku belom mandi seminggu dan aku bangga. NOW!"
    show pia_side at left with dissolve
    pia "Eh.."
    hide pia_side with dissolve
    show pia_angry at pia_near with dissolve
    show pia_side_angry at left with dissolve
    pia "Ehh… jangan gitu dong. Aaah [mcname] maaaah. Yang serius, ih."
    hide pia_side_angry with dissolve
    mcname "Lah? Ini serius."
    show pia_side at left with dissolve
    pia "Gamau! weeeks"
    hide pia_side with dissolve
    mcname "Dih, yaudah. Kusimpen ya. Buat kapan-kapan"
    hide pia_angry with dissolve
    show pia_side at left with dissolve
    pia "Okeh! Saatnya belajar! Ayo!!"
    "[mcname] dan Pia pun belajar bersama di cafe tersebut sampe larut malam, dan [mcname] pun memutuskan meminjamkan buku tersebut ke Pia"
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with dissolve
    show text "{color=#FFF}KEESOKAN HARINYA{/color}" with Pause(2.0)
    scene mc bedroom with dissolve
    play music "audio/BGM_Kosan 1.mp3" fadein 1.0
    "[mcname] ngomong sendiri di kosan. Deg degan hari ini ujian tertulis mata kuliah paling susah."
    mcname "Duhhh. Hari ini ujian tertulis paling susah. Deg deg an, huhu."
    stop music fadeout 1.0
    scene black with dissolve
    show text "{color=#FFF}Sesampainya di kelas{/color}" with Pause(2.0)
    scene kelas with dissolve
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    "Suasana kelas sepi, semua sibuk belajar dan menghapal. ya, hari ini ujian tertulis mata kuliah xxx."
    show pia at pia_near with dissolve
    mcname "Pagi Mbak Pia"
    show pia_side at left with dissolve
    pia "Sssst, diem. Komposisi dan elemen dalam warna—"
    hide pia_side with dissolve
    mcname "Ahahahahah"
    hide pia with dissolve
    show dosen at dosen_center with dissolve
    show dosen_side at left with dissolve
    dosen "Pagi, semua buku dan HP simpan di depan ya. Di atas meja hanya boleh ada alat tulis. Ujian kita mulai 10 menit lagi."
    "Mahasiswa/i" "Baik buuuu~"
    stop music fadeout 1.0
    scene black with dissolve
    play sound "audio/Alarm.mp3" fadein 1.0
    show text "{color=#FFF}MINI GAME TIME{/color}" with Pause(2.0)
    jump quiz
    
label chapter2piaafterquiz:
    "Selesai ujian, semua mahasiswa/i mengumpulkan lembar jawaban ke pengawas. Ujian hari itu berakhir"
    mcname "Hueeeee selesai juga ini ujian.\n*liat kiri kanan*"
    show pia at pia_near with dissolve
    pia "...."
    mcname "Hahahaha gimana? Lancar? Bisa kan jawabnya?"
    show pia_side at left with dissolve
    pia "Bisa lah! Yang bener aja, cuma kayak ada yang kurang puas aja weh. Harusnya aku tambahin, blablabla"
    hide pia_side with dissolve
    mcname "Pia, sepanjang ujian tadi, anak-anak lain cuma selembar doang, terus dikumpulin, loh. Kamu sampe minta nambah lembar jawaban 2x."
    mcname "DUA KALI"
    mcname "Lu ngisi apa bikin AU lu?"
    show pia_side at left with dissolve
    pia "Dih, aku tuh harus sempurna! Harus nilai 100!"
    hide pia_side with dissolve
    mcname "Kasian Bu Dosen yang meriksa jawaban kamu. Kayak baca novel, hahaha"
    show pia_side at left with dissolve
    pia "Iiiiih\n*mukul - mukul [mcname]"
    hide pia_side with dissolve
    mcname "Ahahaha, eh hari ini mau ke mana? Pusing gak sih? Mau refreshing gak sih? Huhuhu."
    show pia_side at left with dissolve
    pia "Rooftop yuk! Aku nunggu di sana, kamu ke kantin beli cemilan yang banyaaaaak! Nanti kita makan di rooftop."
    hide pia_side with dissolve
    mcname "Meeeh, gue yang beli nih?"
    show pia_side at left with dissolve
    pia "Aku pake uangku lah, nih. Aku tunggu di rooftop yaaa."
    hide pia_side with dissolve
    pia "...bukan masalah uangnya. Aku beli sendiri nih? Huhuhu kayak piaraan aja gue disuruh suruh. Bener bener ya, Meameo."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    scene kantin with dissolve
    play music "audio/bgm_kantin.mp3" fadein 1.0
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname] pun ke kantin untuk beli beberapa cemilan untuk dibawa ke rooftop untuk makan bareng Pia"
    mcname "*Sambil bawa plastik berisi beberapa camilan*"
    mcname "Hmmm... apa lagi ya? Kayanya beli snack itu enak"
    show fio at char_placement with dissolve
    show fio_side at left with dissolve
    fio "[mcname]!!!!"
    hide fio_side with dissolve
    mcname "Woaaa kaget, Cepio hai~"
    show fio_side at left with dissolve
    fio "Sini!!!\n*sambil menepuk nepuk kursi kosong sebelah Fiony*"
    hide fio_side with dissolve
    mcname "Halo Cepio~\n*nyamperin*"
    hide fio with dissolve
    show kana at kana_near_left_2 with dissolve
    show freya at freya_near_right with dissolve
    show fio at fio_near with dissolve
    show fio_side at left with dissolve
    fio "Kenalin, ini Freya, kalo yang sebelahnya Kana."
    hide fio_side with dissolve
    mcname "Halo, namaku [mcname]. Salam kenal"
    show kana_side at left with dissolve
    kana "*Menyipitkan mata sambil mengisyaratkan sesuatu*"
    kana "Ehm..Yang Mulia Piaraan?"
    hide kana_side with dissolve
    show freya_side at left with dissolve
    freya "Hadeeeh, Naaaaay."
    hide freya_side with dissolve
    mcname "???"
    show kana_side at left with dissolve
    kana "Eh, Kak Fiony, bukan ini orangnya?"
    hide kana_side with dissolve
    show fio_side at left with dissolve
    fio "Meameo? Bukaaaan. Ini mah belahan jiwanya."
    hide fio_side with dissolve
    mcname "Whaaat. Cepiooooo"
    show fio_side at left with dissolve
    fio "Ahahaha, gini [mcname]. Ini Kana mau banget ketemu Pia. Dia suka banget gambarnya Pia"
    hide fio_side with dissolve
    show kana_side at left with dissolve
    kana "Iya! Aku mau ajak dia join club jejepangan. Kira-kira mau gak, ya?"
    hide kana_side with dissolve
    mcname "Oh, kamu anak club jejepangan?"
    mcname "Pas itu sempet sih, aku kasih liat flyer yang dibagiin. Tapi kayaknya dia gak terlalu tertarik."
    show kana_side at left with dissolve
    kana "Sasuga Yang Mulia Piaraan, butuh usaha lebih buat rekrut dia!"
    hide kana_side with dissolve
    mcname "Yang Mulia Piaraan?"
    show kana_side at left with dissolve
    kana "Oh ah, enggak enggak. Nanti aku ajak Tono buat rekrut dia. Harus bisa pokoknya"
    hide kana_side with dissolve
    "{size=-5}Freya & Fiony{/size}" "Semangat Naay~"
    mcname "Ahahaha nanti aku coba tanyain lagi deh ya, semoga berubah pikiran. Aku pergi dulu ya. Duluan semua~"
    "{size=-8}Freya, Fiony, Kana{/size}" "Iya, byeee~"
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with dissolve
    show text "{color=#FFF}Di Rooftop{/color}" with Pause(2.0)
    # Harusnya BG Rooftop
    scene depan kampus with dissolve
    play music "audio/BGM_Rooftop Romance Pia.mp3" fadein 1.0
    $ renpy.block_rollback()
    $ quick_menu = True
    "*Pia sedang menari diiringi lagu idol di HPnya yang diputar agak keras*"
    mcname "*Duduk bersila di belakang Pia*"
    "Pia menoleh ke belakang"
    show pia at pia_near with dissolve
    show pia_side at left with dissolve
    pia "Hueeeh kaget!! Udah di sini aja, diem-diem gak ada suara! Bikin jantungan aja"
    hide pia_side with dissolve
    mcname "Mana ada? Kamu aja yang terlalu serius sampe gak perhatiin sekitar, haha"
    show pia_side at left with dissolve
    pia "Hehehe\n*ikut duduk bersila sebelah [mcname]*"
    hide pia_side at left with dissolve
    stop music fadeout 1.0
    play music "audio/BGM_Funny Slow Cute.mp3" fadein 1.0
    mcname "Yang Mulia Piaraan"
    "*Pia menyembur minumannya*"
    show pia_side at left with dissolve
    pia "Uhuk uhuk hoooeeek guuuh uhuk"
    pia "KOK KAMU TAU PEN NAME AKU, TAU DARIMANA?"
    hide pia_side with dissolve
    mcname "Jadi itu beneran kamu? Ahahaha."
    show pia_side at left with dissolve
    pia "Eh tau darimana????"
    hide pia_side with dissolve
    mcname "Tadi di kantin aku ketemu fans kamu nyariin kamu tuh bareng cepio"
    show pia_side at left with dissolve
    pia "Heeeeee"
    hide pia_side with dissolve
    mcname "Tapi itu nama apa, dah?"
    show pia_side at left with dissolve
    pia "Ahahaha itu pen name aku kalo gambar. Aku sering gambar gitu kan, diupload di medsos. Nah nama akun gambar aku tuh, Yang Mulia Piaraan."
    hide pia_side with dissolve
    mcname "Owalah gitu toh"
    show pia_side at left with dissolve
    pia "Aku gak nyangka aja ada yg kenal nama itu dan tau. Aku gak nyembunyiin, sih. Cuma malu aja, pen name aku kayak gitu. Haha"
    hide pia_side with dissolve
    mcname "Lah lagian. Kenapa Yang Mulia Piaraan, dah?"
    show pia_side at left with dissolve
    pia "Ya maap sih, dulu masih wibu wibunya asal ngasih nama. Eh taunya udah nyaman, hahaha."
    pia "Jadi dulu tuh aku suka gambar fanart anime, manga, gitu-gitu lah. Terus ada beberapa yang aku jual juga di online jadi merch. Mungkin orang itu salah satu yang beli"
    hide pia_side with dissolve
    mcname "Oooh gitu toh. Tadi sempet nanyain mau join club jepang, gak?"
    show pia_side at left with dissolve
    pia "Err… engga deh. Aku mau lonewolf. Udah gak terlalu jejepangan banget"
    hide pia_side with dissolve
    mcname "Hmmm.... gitu"
    show pia_side at left with dissolve
    pia "Emang kamu ngerti jejepangan?"
    hide pia_side with dissolve
    mcname "Beuh, perlu aku jelasin sinopsis 3 episode pertama setiap anime yang airing season ini gak nih?"
    show pia_side at left with dissolve
    pia "IH WIBUUUU"
    hide pia_side with dissolve
    mcname "Ahahahahah"
    show pia_side at left with dissolve
    pia "Tapi bener deh, aku tuh gatau kenapa jadi agak kurang buat bersosialisasi gitu... Tapi di sisi lain, aku mau punya banyak temen dan kenal orang baru. Tapi males aja memulai"
    hide pia_side with dissolve
    mcname "Wakaru Pia, wakaru…"
    show pia_side at left with dissolve
    pia "Aaaah, jangan wibuuu :((("
    hide pia_side with dissolve
    mcname "Ahahaha becandaa~ Tapi bener deh, kamu gamau join? Kalo kamu join, aku juga deh. Gimana?"
    show pia_side at left with dissolve
    pia "Yeuuu, itu mah emang kamu aja kan yang mau."
    hide pia_side with dissolve
    mcname "Gak gituuuuu"
    "[mcname] dan Pia pun banyak bercerita sambil menikmati cemilan di rooftop"
    stop music fadeout 1.0
    scene black with dissolve
    show text "{color=#FFF}CHAPTER III{/color}" with Pause(2.0)
    play music "audio/Dreamcatcher.mp3" fadein 1.0
    jump credits
