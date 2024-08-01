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
    show dosen_talk at dosen_center 
    show dosen_side_talk at left 
    with dissolve
    $ dosen_name = "Dosen Seni"
    #$ renpy.block_rollback()
    $ quick_menu = True
    dosen "Ya, ujiannya adalah menggambar teman kalian."
    show dosen at dosen_center 
    hide dosen_side_talk at left 
    with dissolve
    "Mahasiswa/i" "Heeeeeee, waduh bu."
    hide dosen 
    show dosen_side_talk at left 
    with dissolve
    dosen "Ibu udah buat undiannya, ya. Kita undi nama pasangan gambar kalian."
    dosen "Jadi nanti kalian hadap-hadapan dan gambar teman di depan kalian."
    dosen "Semua karya tugas ini akan dipajang di sepanjang lorong gedung DKV ini, ya! Tunjukan bakat kalian kepada yang lain!"
    hide dosen_side_talk 
    hide dosen_talk 
    show pia_talk at pia_near 
    show pia_side_talk at left 
    with dissolve
    pia "Hueeeee… PRESUREEEEE!!"
    show pia at pia_near 
    hide pia_side_talk 
    with dissolve
    "[mcname!c]" "Hahaha dapet siapa ya pasangannya~"
    hide pia_talk
    hide pia 
    show dosen_talk at dosen_center 
    show dosen_side_talk at left 
    with dissolve
    dosen "[mcname!c]..."
    show dosen at dosen_center 
    hide dosen_side_talk 
    with dissolve
    "[mcname!c]" "Hmm…. Yak!"
    hide dosen 
    show dosen_side_talk at left 
    with dissolve
    dosen "Berpasangan sama Pia, ya."
    hide dosen_talk 
    hide dosen_side_talk 
    show pia_smile at pia_near 
    show pia_side_smile at left 
    with dissolve
    pia "YEEEEES! MUAHAHAHA!"
    hide pia_smile
    hide pia_side_smile 
    show dosen_talk at dosen_center 
    show dosen_side_talk at left 
    with dissolve
    dosen "Pia! Jangan berisik."
    hide dosen_talk 
    hide dosen_side_talk 
    show pia_sad at pia_near 
    show pia_side_sad at left 
    with dissolve
    pia "Maaf, bu."
    play sound "SFX - Laughing.mp3" fadein 0.5 volume (3.0)
    hide pia_side_sad with dissolve
    "Mahasiswa/i" "Hahahahahahahaha."
    hide pia_sad with dissolve
    "Semua maba berpindah posisi berhadapan dengan pasangan yang sudah dipilih oleh Bu Dosen."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Kelas.ogg" fadein 1.0 volume (1.5)
    scene kelas with Dissolve(1.0)
    show pia_talk at pia_near 
    show pia_side_talk at left 
    with dissolve
    # #$ renpy.block_rollback()
    $ quick_menu = True
    pia "HAI [mcname!u]! HUEHEHEHEH!"
    show pia at pia_near 
    hide pia_side_talk 
    with dissolve
    "[mcname!c]" "Apalah Pia Pia ini."
    hide pia 
    show pia_side_talk at left 
    with dissolve
    pia "Mau gambar aku kayak gimana? Cute? Seksi? Cool?"
    show pia at pia_near 
    hide pia_side_talk 
    with dissolve
    "[mcname!c]" "Halah, kuping gajah gak sih?"
    show pia_silent at pia_near 
    hide pia
    show pia_side_silent at left 
    with dissolve
    pia "HEEEEH!!!!"
    show pia_smile at pia_near 
    show pia_side_smile at left 
    with dissolve
    pia "Ahahahaha."
    hide pia_silent
    hide pia_talk
    hide pia_side_silent
    hide pia_side_smile 
    hide pia_smile 
    with dissolve
    "Mereka pun bergantian setiap 15 menit untuk saling menggambar pasangannya tersebut."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kamar Pia.ogg" fadein 1.0
    scene kelas with Dissolve(1.0)
    show pia at pia_near with dissolve
    $ quick_menu = True
    "[mcname!c]" "*Menggoreskan kuas di atas canvasnya sambil memandang Pia.*"
    "[mcname!c]" "{i}Waduh. Makin diliat, makin imut dan manis ya Pia Pia ini.{/i}"
    "[mcname!c]" "*Melirik dan melihat wajah samping Pia*"
    show pia_shock at pia_near with dissolve
    pia "*Blush*"
    "[mcname!c]" "Sakit, Pia? Ahahaha."
    show pia_side_shock at left with dissolve
    pia "Dieeeeeem! Aku tuh ga biasa dipandangin gini, ih."
    show pia_silent at pia_near 
    show pia_side_silent at left
    hide pia_shock
    hide pia_side_shock
    with dissolve
    pia "Buru selesaiin gambarnya!!"
    hide pia
    hide pia_side_silent 
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Lah sabar, baru sketch weh."
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
    show dosen_side_talk at left
    with dissolve
    # #$ renpy.block_rollback()
    $ quick_menu = True
    dosen "Yak! Bisa dikumpulkan ya, tugasnya."
    dosen "Besok akan Ibu pajang semua gambar kalian di lorong gedung ini. Nanti Ibu minta BEM (Badan Eksekutif Mahasiswa) untuk bantuin display dan announce pameran ini untuk umum dan dapat dilihat oleh semua fakultas."
    show dosen at dosen_center 
    hide dosen_side_talk 
    with dissolve
    "Mahasiswa 1" "Heeeeeeeee~ Kok jadi pameran gini bu? Malu bu!!"
    hide dosen 
    show dosen_side_talk at left 
    with dissolve
    dosen "Hehe, ini disebut element of surprise. Biar kalian terbiasa. BANGGALAH DENGAN HASIL KARYA KALIAN SENDIRI!!"
    show dosen at dosen_center 
    hide dosen_side_talk 
    with dissolve
    "Mahasiswa 2" "Siaaaaap buuuuuuuu~"
    hide dosen_talk
    hide dosen 
    show pia at pia_near 
    with dissolve
    "[mcname!c]" "Waaaaa malu weh bakal dilihat banyak orang. Kirain cuma buat DKV doang."
    show pia_talk at pia_near 
    show pia_side_talk at left 
    with dissolve
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
    show fio_side_talk at left 
    with dissolve
    fio "Sini-sini, nih hasil karya junior-juniorku."
    show fio at fio_near
    hide fio_side_talk
    show freya_talk at freya_near_right
    show freya_side_talk at left
    with dissolve
    freya "Wah bagus baguuuus! Ayo muter-muter, mau liat semua."
    hide freya_side_talk
    hide fio
    hide freya_talk at freya_near_right
    show fio_side_talk at left
    with dissolve
    fio "Kamu mau ikut juga gak? \n*Nunjuk Kana*"
    show fio at fio_near
    hide fio_side_talk
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Boleh deh, mauuuu."
    hide kana_talk
    hide kana_side_talk
    hide fio at fio_near
    show fio_side_talk at left
    with dissolve
    fio "Aku harus cari punya [mcname!c] sama Si Meameo itu. Dipajang sebelah mana punya mereka ya?"
    show fio at fio_near 
    hide fio_side_talk
    show freya_talk at freya_near_right 
    show kana_talk at kana_near_left_2
    with dissolve
    "{size=-5}Freya & Kana{/size}" "Meameo?"
    hide freya_talk at freya_near_right 
    hide kana_talk at kana_near_left_2
    show fio_side_talk at left 
    hide fio 
    with dissolve
    fio "Oh itu temen aku. Kayaknya kalian ketemu deh pas di cafe. Kalian lupa kali."
    hide fio
    hide fio_talk
    hide fio_side_talk
    hide kana
    hide freya
    with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene lorong with Dissolve(1.0)
    $ quick_menu = True
    "Setelah berkeliling..."
    show kana_talk at kana_near_left_2 
    show freya at freya_near_right
    show fio at fio_near 
    show kana_talk at kana_near_left_2 
    show kana_side_talk at left 
    with dissolve
    kana "YANG MULIA PIARAAN!!!"
    hide kana_side_talk 
    hide kana_talk at kana_near_left_2 
    show kana at kana_near_left_2
    show freya_shock at freya_near_right
    show freya_side_shock at left 
    with dissolve
    freya "Kaget, Kana! Apa sih tiba-tiba teriak gitu."
    hide freya_shock at freya_near_right
    hide freya_side_shock at left 
    hide freya_side_talk 
    hide kana
    show kana_talk at kana_near_left_2
    show kana_side_talk at left 
    with dissolve
    kana "Ini!! Ini!!! Style gambarnya, gak salah lagi! Ini Yang Mulia Piaraan. Aku suka banget style dia, aku ada beberapa koleksi gambar anime buatan orang ini!"
    kana "Dia masuk DKV kampus kita? OMG OMG, aku harus kenal!"
    show kana at kana_near_left_2 
    hide kana_side_talk
    show freya_talk at freya_near_right
    show freya_side_talk at left 
    with dissolve
    freya "Kana, tenang. Tahan aura wibumu. Ini di tempat umum."
    show kana_shy_smile at kana_near_left_2 
    hide freya_side_talk
    hide freya_talk at freya_near_right
    show kana_side_shy_smile at left 
    with dissolve
    kana "Uhuk… Ehem… Iya makasih, Fre."
    show kana at kana_near_left_2 
    hide kana_shy_smile
    hide kana_side_shy_smile 
    show fio_talk at fio_near
    show fio_side_talk at left 
    with dissolve
    fio "Ah! Ini dia gambar Si Meameo itu."
    hide fio_talk 
    hide fio_side_talk 
    hide kana 
    show kana_side_talk at left 
    with dissolve
    kana "Hah? Kak Fiony, ini temen kakak yang dicari dari tadi?"
    show kana at kana_near_left_2 
    hide kana_side_talk 
    show fio_talk at fio_near 
    show fio_side_talk at left 
    with dissolve
    fio "Iya, nih gambarnya sebelahan ternyata. Ini [mcname!c], ini Pia."
    hide fio_talk 
    hide fio_side_talk 
    hide kana 
    show kana_side_talk at left 
    with dissolve
    kana "Kak! Kenalin aku sama yang gambar ini!!"
    show kana at kana_near_left_2 
    hide kana_side_talk 
    show fio_talk at fio_near 
    show fio_side_talk at left 
    with dissolve
    fio "Pia?"
    show fio_smile at fio_near 
    hide fio_talk 
    show fio_side_grin at left 
    hide fio_side_talk 
    with dissolve
    fio "Ahaha oke aman. Orangnya lagi gak ada. Kapan-kapan aku kenalin, ya."
    hide freya
    hide fio
    hide kana_talk
    hide kana
    hide fio_smile
    hide fio_side_grin
    with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene lorong with Dissolve(1.0)
    # #$ renpy.block_rollback()
    $ quick_menu = True
    "Akhirnya mereka bertiga pun pergi setelah berkeliling melihat hasil karya anak-anak DKV."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kantin.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Di tempat lain..."
    $ quick_menu = False
    scene kantin with Dissolve(2.0)
    #$ renpy.block_rollback()
    $ quick_menu = True
    play sound "ReceiveText.ogg" loop volume (2.0)
    "Terdengar suara notifikasi handphone."
    stop sound
    show pia_talk at pia_near 
    show pia_side_talk at left
    pia "Weh [mcname!c]!!! Cepio ngirim foto dia selfie sama gambar kita!!!!"
    show pia at pia_near 
    hide pia_side_talk 
    with dissolve
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
    fio_nvl "Gemeesshh~"
    nvl clear
    stop music fadeout 1.0
    play music "BGM_Kantin.ogg" fadein 1.0  
    #$ renpy.block_rollback()
    $ quick_menu = True
    "[mcname!c]" "Wah, iya. Aku juga baru liat di grup nih, ahaha."
    "[mcname!c]" "Mau nyusulin ke sana, gak?"
    hide pia 
    show pia_side_talk at left 
    with dissolve
    pia "Makanan aku baru sampe weh, baru 1 suap! Lagian gak ah, aku maluuuuu."
    show pia at pia_near 
    hide pia_side_talk 
    with dissolve
    "[mcname!c]" "Dih kok gitu, inget kata Bu Dosen: \"BANGGALAH DENGAN KARYA KALIAN SENDIRI!\"\n*Niru gaya bicara dan gerakan Bu Dosen*"
    show pia_smile at pia_near 
    show pia_side_smile at left 
    with dissolve
    pia "Ahahahaha iya iya iya. Nanti aja abis ini."
    hide pia_smile
    hide pia_side_smile 
    with dissolve
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
    show pia at pia_near_right 
    hide pia_side_talk 
    show fio_talk at char_near_left 
    show fio_side_talk at left 
    with dissolve
    fio "Emang ya."
    hide fio_talk
    hide fio_side_talk
    show fio_smile at char_near_left
    show fio_side_grin at left 
    fio "Kalo gak tereak bukan Meameo."
    hide fio_smile at char_near_left 
    hide fio_side_grin at left 
    hide fio_talk 
    hide fio_side_talk
    show fio_smile_talk at char_near_left
    hide pia 
    show pia_side_talk at left 
    with dissolve
    pia "Apalah Cepio ini."
    hide fio_smile_talk at char_near_left
    show fio at char_near_left
    show pia at pia_near_right 
    hide pia_side_talk 
    with dissolve
    "[mcname!c]" "Ahahahahaha."
    show fio_talk at char_near_left 
    show fio_side_talk at left 
    with dissolve
    fio "Ih tadi ada temenku yang mau kenalan sama kamu pas liat gambar kamu, tau."
    hide fio_talk 
    hide fio_side_talk 
    hide pia 
    show pia_side_talk at left 
    with dissolve
    pia "Oh iya, kah? Mana orangnya?"
    show pia at pia_near_right 
    hide pia_side_talk 
    hide fio_talk
    hide fio_side_talk 
    show fio_smile at char_near_left
    show fio_side_grin at left 
    with dissolve
    fio "Telaaat!"
    hide fio_smile at char_near_left
    hide fio_side_grin at left 
    show fio_talk at char_near_left 
    show fio_side_talk at left 
    with dissolve
    fio "Udah pulang mereka."
    hide fio_talk 
    hide fio_side_talk 
    show pia_sad at pia_near_right 
    hide pia
    with dissolve
    "{size=-5}[mcname!c] & Pia{/size}" "Yaaaaaaaaah~"
    show fio_talk at char_near_left 
    show fio_side_talk at left 
    with dissolve
    fio "Nanti aku kenalin deh, ya."
    hide pia_talk
    hide pia_sad
    hide pia
    hide fio
    hide fio_talk
    hide fio_side_talk at left
    with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Sore.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    # #$ renpy.block_rollback()
    $ quick_menu = True
    "[mcname!c], Pia, dan Fiony pun berbincang panjang lebar sampai sore hari dan memutuskan untuk mengakhiri hari itu dan pulang."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    show text "{color=#FFF}1 MINGGU KEMUDIAN{/color}" with Pause(2.0)
    play music "audio/BGM_Dosen.ogg" fadein 1.0
    scene kelas with Dissolve(1.0)
    show dosen_talk at dosen_center 
    show dosen_side_talk at left 
    with dissolve
    #$ renpy.block_rollback()
    $ quick_menu = True
    dosen "--jadi, persiapkan diri kalian. Mulai besok masuk minggu UTS, belajar dan asah skill kalian. Istirahat yang cukup. Semoga hasilnya memuaskan, ya."
    hide dosen_talk at dosen_center 
    hide dosen_side_talk at left 
    show dosen at dosen_center
    with dissolve
    "Mahasiswa/i" "Baik buuuu~"
    hide dosen with dissolve
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "BGM_Kelas.ogg" fadein 1.0 volume (1.5)
    scene kelas with Dissolve(1.0)
    show pia_talk at pia_near 
    show pia_side_talk at left
    with dissolve
    # #$ renpy.block_rollback()
    $ quick_menu = True
    pia "Weeeeh besok udah mulai UTS. Tugas menggambar bebas kamu udah selese, [mcname!c]?"
    show pia at pia_near 
    hide pia_side_talk 
    with dissolve
    "[mcname!c]" "Belom nih. Stuck gak dapet ide mau gambar apa. Kamu udah, Pi?"
    hide pia 
    show pia_side_talk at left 
    with dissolve
    pia "Udah jadi dikit sih, hehehe."
    pia "Aku tuh ga suka nunda pekerjaan, mau cepet selese pokoknya."
    show pia at pia_near
    hide pia_side_talk 
    with dissolve
    "[mcname!c]" "Mana liat gambarnya?"
    hide pia 
    show pia_side_talk at left 
    with dissolve
    pia "Gaboleeeee weeeeeks~"
    show pia at pia_near 
    hide pia_side_talk 
    with dissolve
    "[mcname!c]" "Dih."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Lorong.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya..."
    $ quick_menu = False
    scene lorong with Dissolve(2.0)
    show feni_talk at feni_center 
    show feni_side_talk at left 
    with dissolve
    # #$ renpy.block_rollback()
    $ quick_menu = True
    feni "Flyernya kakak~"
    show feni at feni_center
    hide feni_talk
    hide feni_side_talk 
    with dissolve
    "[mcname!c]" "Oh ah. Makasih, kak."
    hide feni
    with dissolve
    "[mcname!c]" "{i}Flyer apa ini?{/i}"
    show matsuri at matsuri 
    show idolrecruit at poster
    show club at club
    show matsuri:
        subpixel True pos (0.64, 0.19) zrotate 18.0 
    show idolrecruit:
        subpixel True pos (0.21, 0.17) xrotate 0.0 yrotate 0.0 zrotate 0.0 orientation (0.0, 0.0, 18.0) 
    show club:
        subpixel True pos (0.13, 0.15)
    with dissolve
    "[mcname!c] melihat ada 3 flyer yang dibagikan ke orang yang lewat."
    "Flyer 1, acara jejepangan yang berlangsung beberapa bulan lagi.\nFlyer 2, recruitment anggota club jejepangan.\nFlyer 3, recruitment anggota idol dari club jejepangan."
    hide matsuri
    hide idolrecruit 
    hide club 
    with dissolve
    "[mcname!c]" "{i}Simpen dulu deh. Siapa tau temen ada yg butuh.{/i}"
    "[mcname!c]" "{i}Saatnya ngerjain tugas gambar. Minggu ini dikumpulin buat UTS. Ayo semangat akuuuuu!!!{/i}"
    "[mcname!c]" "{i}Hmmm... Ke rooftop dulu, ah. Nyari inspirasi gambar.{/i}"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    $ quick_menu = True
    "[mcname!c]" "Eh, udah ada orang di rooftop ya…"
    "[mcname!c]" "Gak jadi ke rooftop deh."
    "[mcname!c]" "Apa... ngintip dikit kali, ya? Pengen liat siapa."
    $ quick_menu = False
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    scene black with Dissolve(1.0)
    play music "audio/BGM_Rooftop Romance Pia.ogg" fadein 1.0
    scene rooftop with Dissolve(1.0)
    $ quick_menu = True
    "[mcname!c] melihat Pia sedang menari-nari di rooftop dengan indahnya."
    #$ renpy.block_rollback()
    "[mcname!c]" "Woaaa...."
    "[mcname!c]" "P-Pia............."
    show pia_shock at pia_near 
    show pia_side_shock at left 
    with dissolve
    pia "KYAAAAA... EHHH!!!! [mcname!u]!!!!!! NGAPAIN KAMU!?"
    hide pia_side_shock with dissolve
    "[mcname!c]" "Err.... Maaf ganggu. Aku lagi nyari inspirasi gambar aja sih, hehe."
    show pia_side_shock at left with dissolve
    pia "Udah lama kamu di situ????? Kamu gak liat kan, aku lagi ngapain di sini??"
    hide pia_side_shock with dissolve
    "[mcname!c]" "Ummm...."
    pia "...."
    "[mcname!c]" "G-gak liat, kok~"
    show pia_sad at pia_near 
    show pia_side_sad at left 
    with dissolve
    pia "Fuih... Good!"
    show pia_talk at pia_near 
    hide pia_sad
    show pia_side_talk at left 
    hide pia_side_sad
    with dissolve
    pia "Yaudah sini atuh gambar. Punya aku udah selese."
    show pia_smile at pia_near 
    hide pia_talk
    show pia_side_smile at left 
    hide pia_side_talk
    with dissolve
    pia "Hehehe~"
    hide pia_side_smile with dissolve
    "[mcname!c]" "Weeeh... Rajin ya."
    show pia_talk at pia_near 
    hide pia_shock 
    hide pia_smile
    show pia_side_talk at left 
    with dissolve
    pia "Ya dong!!"
    pia "Aku gituuu, aku..."
    show pia_smile at pia_near 
    show pia_side_smile at left 
    hide pia_side_talk
    with dissolve
    pia "AKU!!"
    hide pia_side_smile 
    hide pia_smile
    show pia at pia_near 
    hide pia_side_talk 
    with dissolve
    "[mcname!c]" "Kereeeen!"
    "[mcname!c] mulai duduk bersila sebelah Pia sambil membuat sketch gambar pemandangan."
    show pia_side_talk at left 
    hide pia 
    with dissolve
    pia "Umm........ [mcname!c]. Aku mau cerita dong…"
    show pia at pia_near 
    hide pia_side_talk 
    with dissolve
    "[mcname!c]" "Ya, cerita apa Pia?\n*Sambil lanjut ngerapihin gambarnya*"
    hide pia 
    show pia_side_talk at left 
    with dissolve
    pia "Aku.... Aku punya mimpi lain selain jadi seniman, hehe."
    show pia at pia_near 
    hide pia_side_talk 
    with dissolve
    "[mcname!c]" "Wih mantap, apa tuh?"
    hide pia 
    show pia_side_talk at left 
    with dissolve
    pia "Aku mau jadi idol! Aku suka nari"
    show pia_sad at pia_near 
    show pia_side_sad at left 
    with dissolve
    pia "Gak cocok, ya?"
    show pia_smile at pia_near 
    hide pia_sad
    show pia_side_smile at left 
    hide pia_side_sad
    hide pia_side_talk
    with dissolve
    pia "Ahahaha"
    hide pia_side_smile with dissolve
    "[mcname!c]" "Wah gilaaa! Keren banget! Semangat Pia! Kamu pasti bisa!!"
    show pia_shock at pia_near 
    show pia_side_shock at left 
    with dissolve
    pia "Ehehe! Huhuhu jadi deg-deg an.\n*Sambil ganti lagu favorit Pia di HPnya*"
    hide pia_side_shock with dissolve
    "[mcname!c]" "Percaya diri aja, Pia! Aku yakin kamu pasti bisa! Joget kamu juga bagus kok tadi."
    show pia_side_shock at left with dissolve
    pia "Ehehehe...."
    hide pia_side_shock 
    show pia_silent at pia_near 
    show pia_side_silent at left 
    with dissolve
    pia "EEEEH!!! KAMU NGELIAT AKU JOGET TADI??? KATANYA GAK LIAT! AAAAAAAAAA MALUUUUU!!"
    hide pia_side_silent with dissolve
    "[mcname!c]" "Ups..."
    hide pia_silent 
    show pia_side_shock at left 
    with dissolve
    pia "Huuuuuuuh!"
    pia "Dah lah, maluuuuu~"
    hide pia_side_shock with dissolve
    "[mcname!c]" "Ngapain malu? Aku yakin kamu bisa jadi idol! Tarian kamu bagus. Suara kamu enak didengar. Kamu juga punya kepribadian yang menyenangkan. Kamu cantik, baik hati, --"
    show pia_silent at pia_near 
    show pia_side_silent at left 
    with dissolve
    pia "STOOOOOP!!!!!! HEH K-KENAPA JADI MUJI AKU BEGINI!! AKU GA BISA DIGINIIN WEEEH!!"
    hide pia_side_silent 
    hide pia_silent 
    with dissolve
    "[mcname!c]" "Tapi emang bener, kok! Kamu punya kepribadian yang menurutku cocok jadi inspirasi banyak orang di luar sana!"
    show pia_side_shock at left with dissolve
    pia "Ummm....."
    hide pia_side_shock 
    hide pia_talk
    hide pia_smile
    hide pia_shock
    with dissolve
    $ quick_menu=False
    window auto hide
    show black:
        default
        subpixel True 
        parallel:
            Null(0.0, 0.0)
            'black' with dissolve
        parallel:
            ypos 0 alpha 1.0 
            linear 1.30 ypos 252 alpha 0.7 
    show black as black2:
        default
        subpixel True 
        parallel:
            Null(0.0, 0.0)
            'black' with dissolve
        parallel:
            ypos 2080 alpha 1.0 
            linear 1.30 ypos 1908 alpha 0.7 
    with Pause(1.40)
    show pia_shock at pia_near
    show pia_shock:
        pos (0.45, -0.13) zoom 1.52 
    with dissolve
    window auto show
    $ quick_menu=True
    "[mcname!c]" "*Menatap Pia lebih dekat*"
    "[mcname!c]" "Aku percaya kamu bisa! Realisasikan ya!"
    pia "*Pia dalam hati*\n{i}KYAAAAAAAAAAA DEKEEEET BAANGET [mcname!c]! [mcname!c]! HUH HAH HUH HAH!{/i}"
    show pia_side_shock at left with dissolve
    pia "M-makasih [mcname!c]! Ehehe aku akan berjuang!"
    hide pia_shock 
    hide pia_side_shock 
    with dissolve
    $ quick_menu=False
    window auto hide
    show black:
        subpixel True 
        ypos 252 
        linear 1.30 ypos -9 
    show black as black2:
        subpixel True 
        ypos 1908 
        linear 1.30 ypos 2169 
    with Pause(1.40)
    show pia at pia_near
    with dissolve
    show pia_talk at pia_near 
    show pia_side_talk at left
    with dissolve
    window auto show
    $ quick_menu=True
    pia "Tapi ya ini kan cuma mimpi."
    pia "Ketika bangun dari mimpi, ya…"
    show pia_smile at pia_near 
    show pia_side_smile at left 
    hide pia_side_talk
    with dissolve
    pia "Ngegambar begini deh, haha."
    show pia at pia_near 
    hide pia_side_smile 
    with dissolve
    "[mcname!c]" "Aku akan jadi fans pertama kamu! Jadi yang akan terus mendukungmu dari belakang untuk mengejar mimpimu itu!"
    "[mcname!c]" "Karena..."
    show pia_shock at pia_near 
    show pia_side_shock at left 
    with dissolve
    pia "Wooeee stoooop weh. Udah, cuma mimpi. Aku sekarang udah nyaman begini."
    hide pia_talk
    hide pia_smile
    hide pia_shock
    hide pia_side_shock
    with dissolve
    menu:
        "[mcname!c]" "Pia... Sebenarnya..."
        "Ah! Tadi aku dapet flyer ini. *Kasih semua flyer* mau ikut gak? ada acara jejepangan beberapa bulan lagi nih. terus itu ada 3 flyer, ada yang recruitment jadi idol juga. Mau coba gak?":
            #$ renpy.block_rollback()
            $ quick_menu = True
            "[mcname!c]" "Ah! Tadi aku dapet flyer ini."
            hide pia_shock
            hide pia 
            hide pia_talk 
            hide pia_smile
            with dissolve
            show matsuri at matsuri
            show matsuri:
                subpixel True pos (0.64, 0.19) zrotate 18.0
            with dissolve
            show idolrecruit at poster
            show idolrecruit:
                subpixel True pos (0.21, 0.17) xrotate 0.0 yrotate 0.0 zrotate 0.0 orientation (0.0, 0.0, 18.0) 
            with dissolve
            show club at club
            show club:
                subpixel True pos (0.13, 0.15)
            with dissolve
            "[mcname!c]" "Mau ikut gak? Ada acara jejepangan beberapa bulan lagi nih. Terus itu ada 3 flyer, ada yang recruitment jadi idol juga. Mau coba gak?"
            $ quick_menu = False
            window auto hide
            hide matsuri
            hide idolrecruit 
            hide club 
            with dissolve
            hide pia_smile
            hide pia_shock 
            show pia_talk at pia_near 
            show pia_side_talk at left 
            with dissolve
            window auto show
            $ quick_menu = True
            pia "Wih, apaan nih?"
            pia "Wah matsuri, ya."
            show pia at pia_near
            hide pia_talk
            show pia_side at left
            with dissolve
            pia "Terus…"
            hide pia at pia_near
            show pia_silent at pia_near 
            show pia_side_silent at left
            hide pia_side at left
            with dissolve
            pia "Ini rekruitmen club, skip."
            show pia_talk at pia_near
            hide pia_silent at pia_near 
            hide pia_side_silent at left
            show pia_side_talk at left
            with dissolve
            pia "Yang ini…."
            show pia_shock at pia_near
            hide pia_side_talk 
            show pia_side_shock at left
            hide pia_talk 
            with dissolve
            pia "J-jadi idol??"
            pia "Wow recruitment jadi idol?"
            show pia at pia_near 
            hide pia_side_shock
            with dissolve
            "[mcname!c]" "Gimana, mau coba?"
            hide pia 
            show pia_smile at pia_near
            show pia_side_smile at left 
            with dissolve
            pia "Umm… G-gak deh. Biarlah mimpi tetap jadi mimpi, hehe."
            hide pia_shock 
            hide pia_side_smile at left 
            hide pia_smile 
            with dissolve
            "Akhirnya [mcname!c] duduk di sebelah Pia sambil melihat pemandangan dari rooftop melihat jauh ke depan."
            "Lalu menuangkan pemandangan indah itu dalam sebuah lukisan."
            "Tugas gambar [mcname!c] untuk UTS akhirnya selesai."
            stop music fadeout 1.0
            $ quick_menu = False
            scene black with Dissolve(1.0)
            play music "BGM_Sore.ogg" fadein 1.0
            scene awan sore with Dissolve(1.0)
            # #$ renpy.block_rollback()
            $ quick_menu = True
            "Tak terasa hari sudah menjadi sore."
            "[mcname!c] dan Pia pun pulang ke kost masing-masing."
            $ pia_route = "Good End"
            jump goodpia
        "Ah! Tadi aku dapet flyer ini. *Kasih flyer event jejepangan*. Nonton yuk nanti!":
            #$ renpy.block_rollback()
            $ quick_menu = True
            "[mcname!c]" "Ah! Tadi aku dapet flyer ini."
            hide pia_shock
            hide pia 
            hide pia_talk 
            hide pia_smile
            with dissolve
            show matsuri at poster
            show matsuri:
                    xpos 0.4 
            with dissolve
            "[mcname!c]" "Nonton yuk nanti!"
            $ quick_menu = False
            window auto hide
            hide matsuri with dissolve
            show pia_talk at pia_near 
            show pia_side_talk at left 
            with dissolve
            window auto show
            $ quick_menu = True
            pia "Menarik, tapi pasti…..... Banyak wibu bau bawang, ahahahaha."
            show pia at pia_near
            hide pia_side_talk
            with dissolve
            "[mcname!c]" "Nerbener yee lu."
            "[mcname!c]" "Mau gak? Kalo mau, lesgo beli tiketnya. Nih udah open."
            hide pia
            show pia_side_talk at left
            with dissolve
            pia "Berapaan harganya?"
            show pia at pia_near
            hide pia_side_talk
            with dissolve
            "[mcname!c]" "100 ribu pre-salenya. Berarti nanti setelah pre-sale bakal lebih mahal."
            hide pia
            show pia_side_talk at left
            with dissolve
            pia "Walah! Lesgo buruan beli. Keburu abis presalenya. Aku transfer ke kamu sekarang. Buruan beli."
            show pia at pia_near
            hide pia_side_talk
            with dissolve
            "[mcname!c]" "Otw!!! Sabar."
            "*Pembayaran berhasil*"
            "[mcname!c]" "Dah nih, ya."
            show pia_smile at pia_near
            show pia_side_smile at left
            with dissolve
            pia "Lesgoooooo, huahahaha!"
            hide pia_smile 
            hide pia_side_smile 
            hide pia 
            hide pia_talk
            with dissolve
            stop music fadeout 1.0
            $ quick_menu = False
            play music "BGM_Bad End.ogg" fadein 1.0
            scene black with dissolve
            $ narasi = "Beberapa bulan kemudian, ada gosip beredar bahwa acara jejepangan tersebut gagal dilaksanakan karena promotor acara kabur membawa uang donatur dan sponsor."
            show text "{color=#FFF}[narasi!u]{/color}" with Pause(5.0)
            scene black with dissolve
            show text "{color=#FF0000}BAD END{/color}" with Pause(4.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits
        "Apapun pilihan kamu Pia, aku akan tetap support kamu mau apapun itu.":
            #$ renpy.block_rollback()
            $ quick_menu = True
            "[mcname!c]" "Apapun pilihanmu, Pia, aku akan tetap support kamu. Mau apapun itu."
            show pia_side_shock at left with dissolve
            pia "Aww [mcname!c]..."
            hide pia_shock
            hide pia
            hide pia_side_shock
            show pia_side_smile at left
            with dissolve
            pia "Okeh!! Support aku, ya."
            pia "Menjadi..."
            pia "Illustrator handal!"
            pia "Siapa tau kan? Jadi komikus handal terus ke Jepang."
            pia "Atau jadi ilustrator terkenal di duniaaa, huahahahaha."
            hide pia_smile
            hide pia_side_smile
            show pia at pia_near
            hide pia_talk at pia_near
            with dissolve
            "[mcname!c]" "Okeee. Siap, Pia!"
            show pia_smile at pia_near
            show pia_side_smile at left
            with dissolve
            pia "Ahahahahaha~"
            hide pia
            hide pia_side_smile
            hide pia_smile
            with dissolve
            $ pia_route = "True End"
            jump truepia