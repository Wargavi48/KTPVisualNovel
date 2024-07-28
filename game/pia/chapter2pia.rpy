label chapter2piabegin:
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene chapter 2 pia with Dissolve (1.0)
    pause(3.0)
    scene black with Dissolve (1.0)
    play music "audio/BGM_Pagi Siang.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Berhari hari kemudian..."
    $ quick_menu = False 
    scene kelas with Dissolve(2.0)
    $ quick_menu = True
    "Peralatan menggambar sudah siap, Mahasiswa/i baru DKV pun memulai kelas ujian menggambar pertamanya."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve (1.0)
    play music "audio/BGM_Dosen.ogg" fadein 1.0
    scene kelas with Dissolve(1.0)
    show dosen_talk at dosen_center with dissolve
    show dosen_side at left with dissolve
    $ dosen_name = "Dosen Seni"
    #$ renpy.block_rollback()
    $ quick_menu = True
    dosen "Ya, ujiannya adalah menggambar teman kalian."
    show dosen at dosen_center with dissolve
    hide dosen_side at left with dissolve
    "Mahasiswa/i" "Heeeeeee, waduh bu."
    hide dosen with dissolve
    show dosen_side at left with dissolve
    dosen "Ibu udah buat undiannya, ya. Kita undi nama pasangan gambar kalian."
    dosen "Jadi nanti kalian hadap-hadapan dan gambar teman di depan kalian."
    dosen "Semua karya tugas ini akan dipajang di sepanjang lorong gedung DKV ini, ya! Tunjukan bakat kalian kepada yang lain!"
    hide dosen_side with dissolve
    hide dosen_talk with dissolve
    show pia_talk at pia_near with dissolve
    show pia_side_talk at left with dissolve
    pia "Hueeeee… PRESUREEEEE!!"
    show pia at pia_near with dissolve
    hide pia_side_talk with dissolve
    mcname "Hahaha dapet siapa ya pasangannya~"
    hide pia_talk
    hide pia with dissolve
    show dosen_talk at dosen_center with dissolve
    show dosen_side at left with dissolve
    dosen "[mcname]..."
    show dosen at dosen_center with dissolve
    hide dosen_side with dissolve
    mcname "Hmm…. Yak!"
    hide dosen with dissolve
    show dosen_side at left with dissolve
    dosen "Berpasangan sama Pia, ya."
    hide dosen_talk with dissolve
    hide dosen_side with dissolve
    show pia_smile at pia_near with dissolve
    show pia_side_smile at left with dissolve
    pia "YEEEEES! MUAHAHAHA!"
    hide pia_smile with dissolve
    hide pia_side_smile with dissolve
    show dosen_talk at dosen_center with dissolve
    show dosen_side at left with dissolve
    dosen "Pia! Jangan berisik."
    hide dosen_talk with dissolve
    hide dosen_side with dissolve
    show pia_sad at pia_near with dissolve
    show pia_side_sad at left with dissolve
    pia "Maaf, bu."
    hide pia_side_sad with dissolve
    "Mahasiswa/i" "Hahahahahahahaha."
    hide pia_sad with dissolve
    "Semua maba berpindah posisi berhadapan dengan pasangan yang sudah dipilih oleh Bu Dosen."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Kelas.ogg" fadein 1.0 volume (1.5)
    scene kelas with Dissolve(1.0)
    show pia_talk at pia_near with dissolve
    show pia_side_talk at left with dissolve
    # #$ renpy.block_rollback()
    $ quick_menu = True
    pia "HAI [mcname!u]! HUEHEHEHEH!"
    show pia at pia_near with dissolve
    hide pia_side_talk with dissolve
    mcname "Apalah Pia Pia ini."
    hide pia with dissolve
    show pia_side_talk at left with dissolve
    pia "Mau gambar aku kayak gimana? Cute? Seksi? Cool?"
    show pia at pia_near with dissolve
    hide pia_side_talk with dissolve
    mcname "Halah, kuping gajah gak sih?"
    show pia_silent at pia_near with dissolve
    hide pia
    show pia_side_silent at left with dissolve
    pia "HEEEEH!!!!"
    show pia_smile at pia_near with dissolve
    show pia_side_smile at left with dissolve
    pia "Ahahahaha."
    hide pia_silent
    hide pia_talk
    hide pia_side_silent
    hide pia_side_smile with dissolve
    hide pia_smile with dissolve
    "Mereka pun bergantian setiap 15 menit untuk saling menggambar pasangannya tersebut."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kamar Pia.ogg" fadein 1.0
    scene kelas with Dissolve(1.0)
    show pia at pia_near with dissolve
    $ quick_menu = True
    mcname "*Menggoreskan kuas di atas canvasnya sambil memandang Pia.*"
    mcname "{i}Waduh. Makin diliat, makin imut dan manis ya Pia Pia ini.{/i}"
    mcname "*Melirik dan melihat wajah samping Pia*"
    show pia_shock at pia_near with dissolve
    pia "*Blush*"
    mcname "Sakit, Pia? Ahahaha."
    show pia_side_shock at left with dissolve
    pia "Dieeeeeem! Aku tuh ga biasa dipandangin gini, ih."
    show pia_silent at pia_near with dissolve
    show pia_side_silent at left with dissolve
    hide pia_shock
    hide pia_side_shock
    pia "Buru selesaiin gambarnya!!"
    hide pia
    hide pia_side_silent with dissolve
    hide pia_side_talk
    mcname "Lah sabar, baru sketch weh."
    show pia_side_silent at left with dissolve
    pia "*Huft*"
    $ quick_menu = False
    stop music fadeout 1.0
    jump startPiaGame


label chapter2piaaftergame:
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Dosen.ogg" fadein 1.0
    scene kelas with Dissolve(1.0)
    show dosen_talk at dosen_center
    show dosen_side at left
    with dissolve
    # #$ renpy.block_rollback()
    $ quick_menu = True
    dosen "Yak! Bisa dikumpulkan ya, tugasnya."
    dosen "Besok akan Ibu pajang semua gambar kalian di lorong gedung ini. Nanti Ibu minta BEM (Badan Eksekutif Mahasiswa) untuk bantuin display dan announce pameran ini untuk umum dan dapat dilihat oleh semua fakultas."
    show dosen at dosen_center with dissolve
    hide dosen_side with dissolve
    "Mahasiswa 1" "Heeeeeeeee~ Kok jadi pameran gini bu? Malu bu!!"
    hide dosen with dissolve
    show dosen_side at left with dissolve
    dosen "Hehe, ini disebut element of surprise. Biar kalian terbiasa. BANGGALAH DENGAN HASIL KARYA KALIAN SENDIRI!!"
    show dosen at dosen_center with dissolve
    hide dosen_side with dissolve
    "Mahasiswa 2" "Siaaaaap buuuuuuuu~"
    hide dosen_talk
    hide dosen with dissolve
    show pia at pia_near with dissolve
    mcname "Waaaaa malu weh bakal dilihat banyak orang. Kirain cuma buat DKV doang."
    show pia_talk at pia_near with dissolve
    show pia_side_talk at left with dissolve
    pia "Iya weh. Ya udah lah ya."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Lorong.ogg" fadein 1.0
    scene lorong with Dissolve(1.0)
    #$ renpy.block_rollback()
    $ quick_menu = True
    "Keesokan harinya, semua karya sudah terpajang di sepanjang lorong dan lobby gedung DKV."
    "Banyak sekali Mahasiswa/i dari fakultas lain yang datang untuk sekedar berswafoto atau menikmati hasil karya Maba DKV layaknya mengunjungi pameran seni."
    "Fiony, Freya, dan Kana sedang berjalan bersama mengunjungi pameran ini."
    show kana at kana_near_left_2
    show freya at freya_near_right
    show fio_talk at fio_near
    with dissolve
    show fio_side at left with dissolve
    fio "Sini-sini, nih hasil karya junior-juniorku."
    show fio at fio_near
    hide fio_side
    show freya_side at left
    with dissolve
    freya "Wah bagus baguuuus! Ayo muter-muter, mau liat semua."
    hide freya_side
    hide fio
    show fio_side at left
    with dissolve
    fio "Kamu mau ikut juga gak? \n*Nunjuk Kana*"
    show fio at fio_near
    hide fio_side
    show kana_talk at kana_near_left_2
    show kana_side at left
    with dissolve
    kana "Boleh deh, mauuuu."
    hide kana_talk
    hide kana_side
    hide fio at fio_near
    show fio_side at left
    with dissolve
    fio "Aku harus cari punya [mcname] sama Si Meameo itu. Dipajang sebelah mana punya mereka ya?"
    show fio at fio_near with dissolve
    hide fio_side with dissolve
    "{size=-5}Freya & Kana{/size}" "Meameo?"
    show fio_side at left with dissolve
    hide fio with dissolve
    fio "Oh itu temen aku. Kayaknya kalian ketemu deh pas di cafe. Kalian lupa kali."
    hide fio
    hide fio_talk
    hide fio_side
    hide kana
    hide freya
    with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene lorong with Dissolve(1.0)
    $ quick_menu = True
    "Setelah berkeliling..."
    show kana_talk at kana_near_left_2 with dissolve
    show freya at freya_near_right with dissolve
    show fio at fio_near with dissolve
    show kana at kana_near_left_2 with dissolve
    show kana_side at left with dissolve
    kana "YANG MULIA PIARAAN!!!"
    hide kana_side with dissolve
    hide freya
    show freya at freya_near_right
    show freya_side at left with dissolve
    freya "Kaget, Kana! Apa sih tiba-tiba teriak gitu."
    hide freya_side with dissolve
    hide kana with dissolve
    show kana_side at left with dissolve
    kana "Ini!! Ini!!! Style gambarnya, gak salah lagi! Ini Yang Mulia Piaraan. Aku suka banget style dia, aku ada beberapa koleksi gambar anime buatan orang ini!"
    kana "Dia masuk DKV kampus kita? OMG OMG, aku harus kenal!"
    show kana at kana_near_left_2 with dissolve
    hide kana_side with dissolve
    show freya_side at left with dissolve
    freya "Kana, tenang. Tahan aura wibumu. Ini di tempat umum."
    show kana_shy_smile at kana_near_left_2 with dissolve
    hide freya_side with dissolve
    show kana_side_shy_smile at left with dissolve
    kana "Uhuk… Ehem… Iya makasih, Fre."
    show kana at kana_near_left_2 with dissolve
    hide kana_shy_smile
    hide kana_side_shy_smile with dissolve
    show fio_talk at fio_near with dissolve
    show fio_side at left with dissolve
    fio "Ah! Ini dia gambar Si Meameo itu."
    hide fio_talk with dissolve
    hide fio_side with dissolve
    hide kana with dissolve
    show kana_side at left with dissolve
    kana "Hah? Kak Fiony, ini temen kakak yang dicari dari tadi?"
    show kana at kana_near_left_2 with dissolve
    hide kana_side with dissolve
    show fio_talk at fio_near with dissolve
    show fio_side at left with dissolve
    fio "Iya, nih gambarnya sebelahan ternyata. Ini [mcname], ini Pia."
    hide fio_talk with dissolve
    hide fio_side with dissolve
    hide kana with dissolve
    show kana_side at left with dissolve
    kana "Kak! Kenalin aku sama yang gambar ini!!"
    show kana at kana_near_left_2 with dissolve
    hide kana_side with dissolve
    show fio_talk at fio_near with dissolve
    show fio_side at left with dissolve
    fio "Pia?"
    show fio_smile at fio_near with dissolve
    hide fio_talk with dissolve
    show fio_side_smile at left with dissolve
    hide fio_side with dissolve
    fio "Ahaha oke aman. Orangnya lagi gak ada. Kapan-kapan aku kenalin, ya."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene lorong with Dissolve(1.0)
    # #$ renpy.block_rollback()
    $ quick_menu = True
    "Akhirnya mereka bertiga pun pergi setelah berkeliling melihat hasil karya anak-anak DKV."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    show text "{color=#FFF}DI TEMPAT LAIN{/color}" with Pause(2.0)
    play music "audio/BGM_Kantin.ogg" fadein 1.0
    scene kantin with Dissolve(1.0)
    #$ renpy.block_rollback()
    play sound "ReceiveText.ogg" loop volume (2.0)
    $ quick_menu = True
    "Terdengar suara notifikasi handphone."
    stop sound
    show pia_talk at pia_near with dissolve
    show pia_side_talk at left with dissolve
    pia "Weh [mcname]!!! Cepio ngirim foto dia selfie sama gambar kita!!!!"
    show pia at pia_near with dissolve
    hide pia_side_talk with dissolve
    $ quick_menu = False
    nvl clear
    stop music fadeout 1.0
    play music "BGM_Happy + HP.ogg" fadein 1.0 volume (2.0)
    fio_nvl "P"
    fio_nvl "P"
    fio_nvl "P"
    fio_nvl "P"
    fio_nvl "P"
    fio_nvl "P"
    fio_nvl "{image=cepio selfie.png}"
    stop music fadeout 1.0
    play music "BGM_Kantin.ogg" fadein 1.0
    scene kantin with dissolve
    #$ renpy.block_rollback()
    $ quick_menu = True
    mcname "Wah, iya. Aku juga baru liat di grup nih, ahaha."
    mcname "Mau nyusulin ke sana, gak?"
    hide pia with dissolve
    show pia_side_talk at left with dissolve
    pia "Makanan aku baru sampe weh, baru 1 suap! Lagian gak ah, aku maluuuuu."
    show pia at pia_near with dissolve
    hide pia_side_talk with dissolve
    mcname "Dih kok gitu, inget kata Bu Dosen: \"BANGGALAH DENGAN KARYA KALIAN SENDIRI!\"\n*Niru gaya bicara dan gerakan Bu Dosen*"
    show pia_smile at pia_near with dissolve
    show pia_side_smile at left with dissolve
    pia "Ahahahaha iya iya iya. Nanti aja abis ini."
    hide pia_smile
    hide pia_side_smile with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Lorong.ogg" fadein 1.0
    scene lorong with Dissolve(1.0)
    show pia_talk at pia_near_right
    show fio at char_near_left
    show pia_side_talk at left
    with dissolve
    #$ renpy.block_rollback()
    $ quick_menu = True
    pia "CEPIOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO~"
    show pia at pia_near_right with dissolve
    hide pia_side_talk with dissolve
    show fio_talk at char_near_left with dissolve
    show fio_side at left with dissolve
    fio "Emang ya."
    fio "Kalo gak tereak bukan Meameo."
    hide fio_talk with dissolve
    hide fio_side with dissolve
    hide pia with dissolve
    show pia_side_talk at left with dissolve
    pia "Apalah Cepio ini."
    show pia at pia_near_right with dissolve
    hide pia_side_talk with dissolve
    mcname "Ahahahahaha."
    show fio_talk at char_near_left with dissolve
    show fio_side at left with dissolve
    fio "Ih tadi ada temenku yang mau kenalan sama kamu pas liat gambar kamu, tau."
    hide fio_talk with dissolve
    hide fio_side with dissolve
    hide pia with dissolve
    show pia_side_talk at left with dissolve
    pia "Oh iya, kah? Mana orangnya?"
    show pia at pia_near_right with dissolve
    hide pia_side_talk with dissolve
    show fio_talk at char_near_left with dissolve
    show fio_side at left with dissolve
    fio "Telaaat!"
    fio "Udah pulang mereka."
    hide fio_talk with dissolve
    hide fio_side with dissolve
    show pia_sad at pia_near_right with dissolve
    hide pia
    "{size=-5}[mcname] & Pia{/size}" "Yaaaaaaaaah~"
    show fio_talk at char_near_left with dissolve
    show fio_side at left with dissolve
    fio "Nanti aku kenalin deh, ya."
    hide pia_talk
    hide pia_sad
    hide pia
    hide fio
    hide fio_talk
    hide fio_side at left
    with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Sore.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    # #$ renpy.block_rollback()
    $ quick_menu = True
    "[mcname], Pia, dan Fiony pun berbincang panjang lebar sampai sore hari dan memutuskan untuk mengakhiri hari itu dan pulang."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    show text "{color=#FFF}1 MINGGU KEMUDIAN{/color}" with Pause(2.0)
    play music "audio/BGM_Dosen.ogg" fadein 1.0
    scene kelas with Dissolve(1.0)
    show dosen_talk at dosen_center with dissolve
    show dosen_side at left with dissolve
    #$ renpy.block_rollback()
    $ quick_menu = True
    dosen "--jadi, persiapkan diri kalian. Mulai besok masuk minggu UTS, belajar dan asah skill kalian. Istirahat yang cukup. Semoga hasilnya memuaskan, ya."
    "Mahasiswa/i" "Baik buuuu~"
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "BGM_Kelas.ogg" fadein 1.0 volume (1.5)
    scene kelas with Dissolve(1.0)
    show pia_talk at pia_near with dissolve
    show pia_side_talk at left with dissolve
    # #$ renpy.block_rollback()
    $ quick_menu = True
    pia "Weeeeh besok udah mulai UTS. Tugas menggambar bebas kamu udah selese, [mcname]?"
    show pia at pia_near with dissolve
    hide pia_side_talk with dissolve
    mcname "Belom nih. Stuck gak dapet ide mau gambar apa. Kamu udah, Pi?"
    hide pia with dissolve
    show pia_side_talk at left with dissolve
    pia "Udah jadi dikit sih, hehehe."
    pia "Aku tuh ga suka nunda pekerjaan, mau cepet selese pokoknya."
    show pia at pia_near with dissolve
    hide pia_side_talk with dissolve
    mcname "Mana liat gambarnya?"
    hide pia with dissolve
    show pia_side_talk at left with dissolve
    pia "Gaboleeeee weeeeeks."
    show pia at pia_near with dissolve
    hide pia_side_talk with dissolve
    mcname "Dih."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    show text "{color=#FFF}KEESOKAN HARINYA{/color}" with Pause(2.0)
    play music "audio/BGM_Lorong.ogg" fadein 1.0
    scene lorong with Dissolve(1.0)
    show feni_talk at feni_center with dissolve
    show feni_side at left with dissolve
    # #$ renpy.block_rollback()
    $ quick_menu = True
    feni "Flyernya kakak~"
    hide feni_talk with dissolve
    hide feni_side with dissolve
    mcname "Oh ah. Makasih, kak."
    mcname "{i}Flyer apa ini?{/i}"
    "[mcname] melihat ada 3 flyer yang dibagikan ke orang yang lewat."
    "Flyer 1, acara jejepangan yang berlangsung beberapa bulan lagi.\nFlyer 2, recruitment anggota club jejepangan.\nFlyer 3, recruitment anggota idol dari club jejepangan."
    mcname "{i}Simpen dulu deh. Siapa tau temen ada yg butuh.{/i}"
    mcname "{i}Saatnya ngerjain tugas gambar. Minggu ini dikumpulin buat UTS. Ayo semangat akuuuuu!!!{/i}"
    mcname "{i}Hmmm... Ke dulu rooftop, ah. Nyari inspirasi gambar.{/i}"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    $ quick_menu = True
    mcname "Eh, udah ada orang di rooftop ya…"
    mcname "Gak jadi ke rooftop deh."
    mcname "Apa... ngintip dikit kali, ya? Pengen liat siapa."
    $ quick_menu = False
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    scene black with Dissolve(1.0)
    play music "audio/BGM_Rooftop Romance Pia.ogg" fadein 1.0
    scene rooftop with Dissolve(1.0)
    #$ renpy.block_rollback()
    $ quick_menu = True
    mcname "Woaaa...."
    mcname "P-Pia............."
    show pia_shock at pia_near with dissolve
    show pia_side_shock at left with dissolve
    pia "Kyaaaa... EHHH!!!! [mcname!u]!!!!!! NGAPAIN KAMU!?"
    hide pia_side_shock with dissolve
    mcname "Err.... Maaf ganggu. Aku lagi nyari inspirasi gambar aja sih, hehe."
    show pia_side_shock at left with dissolve
    pia "Udah lama kamu di situ????? Kamu gak liat kan, aku lagi ngapain di sini??"
    hide pia_side_shock with dissolve
    mcname "Ummm...."
    pia "...."
    mcname "G-gak liat, kok~"
    show pia_sad at pia_near with dissolve
    show pia_side_sad at left with dissolve
    pia "Fuih... Good!"
    show pia_talk at pia_near with dissolve
    hide pia_sad
    show pia_side_talk at left with dissolve
    hide pia_side_sad
    pia "Yaudah sini atuh gambar. Punya aku udah selese."
    show pia_smile at pia_near with dissolve
    hide pia_talk
    show pia_side_smile at left with dissolve
    hide pia_side_talk
    pia "Hehehe~"
    hide pia_side_smile with dissolve
    mcname "Weeeh... Rajin ya."
    show pia_talk at pia_near with dissolve
    hide pia_shock 
    hide pia_smile
    show pia_side_talk at left with dissolve
    pia "Ya dong!!"
    pia "Aku gituuu, aku..."
    pia "AKU!!"
    show pia at pia_near with dissolve
    hide pia_side_talk with dissolve
    mcname "Kereeeen!"
    "[mcname] mulai duduk bersila sebelah Pia sambil membuat sketch gambar pemandangan."
    show pia_side_talk at left with dissolve
    hide pia with dissolve
    pia "Umm........ [mcname]. Aku mau cerita dong…"
    show pia at pia_near with dissolve
    hide pia_side_talk with dissolve
    mcname "Ya, cerita apa Pia?\n*Sambil lanjut ngerapihin gambarnya*"
    hide pia with dissolve
    show pia_side_talk at left with dissolve
    pia "Aku.... Aku punya mimpi lain selain jadi seniman, hehe."
    show pia at pia_near with dissolve
    hide pia_side_talk with dissolve
    mcname "Wih mantap, apa tuh?"
    hide pia with dissolve
    show pia_side_talk at left with dissolve
    pia "Aku mau jadi idol! Aku suka nari"
    show pia_sad at pia_near with dissolve
    show pia_side_sad at left with dissolve
    pia "Gak cocok, ya?"
    show pia_smile at pia_near with dissolve
    hide pia_sad
    show pia_side_smile at left with dissolve
    hide pia_side_sad
    hide pia_side_talk
    pia "Ahahaha"
    hide pia_side_smile with dissolve
    mcname "Wah gilaaa! Keren banget! Semangat Pia! Kamu pasti bisa!!"
    show pia_shock at pia_near with dissolve
    show pia_side_shock at left with dissolve
    pia "Ehehe! Huhuhu jadi deg-deg an.\n*Sambil ganti lagu favorit Pia di HPnya*"
    hide pia_side_shock with dissolve
    mcname "Percaya diri aja, Pia! Aku yakin kamu pasti bisa! Joget kamu juga bagus kok tadi."
    show pia_side_shock at left with dissolve
    pia "Ehehehe...."
    hide pia_side_shock with dissolve
    show pia_silent at pia_near with dissolve
    show pia_side_silent at left with dissolve
    pia "EEEEH!!! KAMU NGELIAT AKU JOGET TADI??? KATANYA GAK LIAT! AAAAAAAAAA MALUUUUU!!"
    hide pia_side_silent with dissolve
    mcname "Ups..."
    hide pia_silent with dissolve
    show pia_side_shock at left with dissolve
    pia "Huuuuuuuh!"
    pia "Dah lah, maluuuuu~"
    hide pia_side_shock with dissolve
    mcname "Ngapain malu? Aku yakin kamu bisa jadi idol! Tarian kamu bagus. Suara kamu enak didengar. Kamu juga punya kepribadian yang menyenangkan. Kamu cantik, baik hati, --"
    show pia_silent at pia_near with dissolve
    show pia_side_silent at left with dissolve
    pia "STOOOOOP!!!!!! HEH K-KENAPA JADI MUJI AKU BEGINI!! AKU GA BISA DIGINIIN WEEEH!!"
    hide pia_side_silent with dissolve
    hide pia_silent with dissolve
    mcname "Tapi emang bener, kok! Kamu punya kepribadian yang menurutku cocok jadi inspirasi banyak orang di luar sana!"
    show pia_side_shock at left with dissolve
    pia "Ummm....."
    hide pia_side_shock with dissolve
    hide pia_talk
    hide pia_smile
    mcname "*Menatap Pia lebih dekat*"
    show pia_shock:
        ypos -0.21 zoom 1.8
    with dissolve
    mcname "Aku percaya kamu bisa! Realisasikan ya!"
    pia "*Pia dalam hati*\n{i}KYAAAAAAAAAAA DEKEEEET BAANGET [mcname]! [mcname]! HUH HAH HUH HAH!{/i}"
    show pia_side_shock at left with dissolve
    pia "M-makasih [mcname]! Ehehe aku akan berjuang!"
    hide pia_shock with dissolve
    hide pia_side_shock with dissolve
    show pia_talk at pia_near with dissolve
    show pia_side_talk at left with dissolve
    pia "Tapi ya ini kan cuma mimpi."
    pia "Ketika bangun dari mimpi, ya…"
    show pia_smile at pia_near with dissolve
    show pia_side_smile at left with dissolve
    hide pia_side_talk
    pia "Ngegambar begini deh, haha."
    show pia at pia_near with dissolve
    hide pia_side_smile with dissolve
    mcname "Aku akan jadi fans pertama kamu! Jadi yang akan terus mendukungmu dari belakang untuk mengejar mimpimu itu!"
    mcname "Karena..."
    show pia_shock at pia_near with dissolve
    show pia_side_shock at left with dissolve
    pia "Wooeee stoooop weh. Udah, cuma mimpi. Aku sekarang udah nyaman begini."
    hide pia_side_shock with dissolve
    menu:
        mcname "Pia... Sebenarnya..."
        "Ah! Tadi aku dapet flyer ini. *Kasih semua flyer* mau ikut gak? ada acara jejepangan beberapa bulan lagi nih. terus itu ada 3 flyer, ada yang recruitment jadi idol juga. Mau coba gak?":
            #$ renpy.block_rollback()
            $ quick_menu = True
            mcname "Ah! Tadi aku dapet flyer ini. \n*Kasih semua flyer*"
            mcname "Mau ikut gak? Ada acara jejepangan beberapa bulan lagi nih. Terus itu ada 3 flyer, ada yang recruitment jadi idol juga. Mau coba gak?"
            hide pia_smile
            hide pia_shock with dissolve
            hide pia with dissolve
            show pia_talk at pia_near with dissolve
            show pia_side_talk at left with dissolve
            pia "Wih, apaan nih?"
            pia "Wah matsuri, ya."
            pia "Terus…"
            pia "Ini rekruitmen club, skip."
            pia "Yang ini…."
            pia "J-jadi idol??"
            pia "Wow recruitment jadi idol?"
            show pia at pia_near with dissolve
            hide pia_side_talk with dissolve
            mcname "Gimana, mau coba?"
            hide pia with dissolve
            show pia_side_talk at left with dissolve
            pia "Umm… G-gak deh. Biarlah mimpi tetap jadi mimpi, hehe."
            hide pia_side_talk at left with dissolve
            hide pia_talk with dissolve
            "Akhirnya [mcname] duduk di sebelah Pia sambil melihat pemandangan dari rooftop melihat jauh ke depan."
            "Lalu menuangkan pemandangan indah itu dalam sebuah lukisan."
            "Tugas gambar [mcname] untuk UTS akhirnya selesai."
            $ pia_route = "Good End"
            jump goodpia
        "Ah! Tadi aku dapet flyer ini. *Kasih flyer event jejepangan*. Nonton yuk nanti!":
            #$ renpy.block_rollback()
            $ quick_menu = True
            mcname "Ah! Tadi aku dapet flyer ini. *Kasih flyer event jejepangan*. Nonton yuk nanti!"
            show pia at pia_near with dissolve
            show pia_side_talk at left with dissolve
            pia "Menarik, tapi pasti…"
            pia "Banyak wibu bau bawang, ahahahaha."
            hide pia_side_talk with dissolve
            mcname "Nerbener yee lu."
            mcname "Mau gak? Kalo mau, lesgo beli tiketnya. Nih udah open."
            show pia_side_talk at left with dissolve
            pia "Berapaan harganya?"
            hide pia_side_talk with dissolve
            mcname "100 ribu pre-salenya. Berarti nanti setelah pre-sale bakal lebih mahal."
            show pia_side_talk at left with dissolve
            pia "Walah! Lesgo buruan beli. Keburu abis presalenya. Aku transfer ke kamu sekarang. Buruan beli."
            hide pia_side_talk with dissolve
            mcname "Otw!!! Sabar."
            "*Pembayaran berhasil*"
            mcname "Dah nih, ya."
            show pia_side_talk at left with dissolve
            pia "Lesgoooooo, huahahaha!"
            $ quick_menu = False
            stop music fadeout 1.0
            scene black with dissolve
            show text "{color=#FFF}*Beberapa bulan kemudian, ada gosip beredar bahwa acara jejepangan tersebut gagal dilaksanakan karena promotor acara kabur membawa uang donatur dan sponsor*{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FF0000}BAD END{/color}" with Pause(2.0)
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits
        "Apapun pilihan kamu Pia, aku akan tetap support kamu mau apapun itu.":
            #$ renpy.block_rollback()
            $ quick_menu = True
            mcname "Apapun pilihanmu, Pia, aku akan tetap support kamu. Mau apapun itu."
            show pia_side_shock at left with dissolve
            pia "Aww [mcname]..."
            hide pia_shock
            hide pia
            hide pia_side_shock
            show pia_side_smile at left
            with dissolve
            pia "Okeh!! Support aku, ya."
            pia "Menjadi..."
            pia "Illustrator handal!"
            pia "Siapa tau kan? Jadi komikus handal terus ke Jepang."
            pia "Atau jadi ilustrator terkenal di duniaaa huahahahaha."
            hide pia_smile
            hide pia_side_smile
            with dissolve
            show pia at pia_near
            hide pia_talk at pia_near
            with dissolve
            mcname "Okeee. Siap, Pia!"
            show pia_smile at pia_near
            show pia_side_smile at left
            with dissolve
            pia "Ahahahahaha~"
            hide pia
            hide pia_side_smile
            with dissolve
            $ pia_route = "True End"
            hide pia_smile with dissolve 
            jump truepia