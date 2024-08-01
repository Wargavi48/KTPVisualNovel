label goodpia:
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" fadein 1.0 volume (0.8)
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Selesai dari kampus, [mcname!c] pulang ke kostnya."
    $ quick_menu = False
    scene kamar kota mc with Dissolve(2.0)
    $ quick_menu = True
    "Di kost, [mcname!c] duduk di meja belajarnya sambil mulai mengeluarkan buku-buku dan catatan materi ujian esok hari."
    "[mcname!c] bersiap begadang untuk fokus belajar karena besok adalah salah satu ujian mata kuliah tertulis yang paling sulit."
    play sound "ReceiveText.ogg" loop volume (2.0) volume(2.0)
    "Tiba-tiba terdengar notifikasi dari handphone [mcname!c]."
    "[mcname!c]" "...."
    "[mcname!c]" "................."
    stop sound
    "[mcname!c]" "{i}Apaan sihh!{/i}"
    $ quick_menu = False
    nvl clear
    pia_nvl "[mcname!u]!!!!"
    pia_nvl "BUKU MATA KULIAH AKU KETINGGALAN DI KAMPUS. BESOK UJIAN INI PULA. GIMANA INI WEH!"
    pia_nvl "P"
    pia_nvl "P"
    pia_nvl "P"
    pia_nvl "P"
    pia_nvl "P"
    pia_nvl "AKU BODOH BANGET LUPA DIBAWA. MAU NANGIS AJA"
    mc_nvl "Wow, sabar. Kamu di mana?"
    pia_nvl "Kosan. Tapi mau nyoba ke kampus, nih."
    mc_nvl "Mana bisa? Jam 6 sore udah tutup kampus, weh"
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
    $ renpy.block_rollback()
    nvl clear
    scene kamar kota mc with dissolve
    $ quick_menu = True
    "[mcname!c] pun bersiap-siap untuk pergi ke cafe."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Cafe Sore.ogg" fadein 1.0
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Di cafe..."
    $ quick_menu = False
    play sound "audio/cafe-entrance.mp3" fadein 1.0
    scene cafe malam with Dissolve(2.0)
    $ renpy.block_rollback()
    show pia_home at pia_near with dissolve
    show pia_home_talk at pia_near
    show pia_home_side_talk at left
    with dissolve
    $ quick_menu = True
    pia "[mcname!c]!! Sini!!"
    hide pia_home_talk
    hide pia_home_side_talk
    with dissolve
    "[mcname!c]" "Hadeeeeeh, nih bukunya."
    show pia_home_side_talk at left 
    show pia_home_talk at pia_near
    with dissolve
    pia "MAKASIH BANGET!!! HUHUHU~"
    pia "KALO GAK ADA KAMU, AKU GATAU HARUS GIMANA. AKU GAMAU NGULANG MATKUL INI!"
    hide pia_home_talk 
    hide pia_home_side_talk 
    with dissolve
    "[mcname!c]" "Iya Pia, Iya."
    show pia_home_talk at pia_near
    show pia_home_side_talk at left 
    with dissolve
    pia "Aku berhutang budi sama kamu!!!"
    hide pia_home_talk 
    hide pia_home_side_talk 
    with dissolve
    "[mcname!c]" "Halah lebay."
    show pia_home_talk at pia_near 
    show pia_home_side_talk at left 
    with dissolve
    pia "Karena kamu baik, aku kasih kamu 1 golden tiket ini. Muahahaha!"
    show ticket
    show ticket:
        pos (0.31, 0.89) zoom 0.25 
    hide pia_home_talk 
    hide pia_home_side_talk 
    with dissolve
    "[mcname!c]" "Apaan ini?"
    show pia_home_talk at pia_near 
    show pia_home_side_talk at left 
    with dissolve
    pia "Pake ini buat mengabulkan 1 permintaan."
    pia "Apapun, akan kulakukan!"
    hide pia_home_talk 
    hide pia_home_side_talk 
    hide ticket
    with dissolve
    "[mcname!c]" "Oke, aku pake sekarang. Sekarang kamu ke depan cafe ini, tereak \"Aku belom mandi seminggu dan aku bangga\". now!"
    show pia_home_shock at pia_near 
    show pia_home_side_shock at left 
    with dissolve
    pia "Ehh… jangan gitu dong."
    show pia_home_silent at pia_near 
    hide pia_home_shock
    show pia_home_side_silent at left 
    hide pia_home_side_shock
    with dissolve
    pia "Aaah [mcname!c] maaaah. Yang serius, ih."
    hide pia_home_silent 
    hide pia_home_side_silent 
    with dissolve
    "[mcname!c]" "Lah? Ini serius."
    show pia_home_smile at pia_near 
    show pia_home_side_smile at left 
    with dissolve
    pia "Gamau! Weeek~"
    hide pia_home_smile 
    hide pia_home_side_smile 
    with dissolve
    "[mcname!c]" "Dih, yaudah. Kusimpen ya. Buat kapan-kapan."
    show pia_home_talk at pia_near 
    show pia_home_side_talk at left 
    with dissolve
    pia "Yaudah. Okeh! Sekarang saatnya belajar! Ayo!!"
    hide pia_home_talk
    hide pia_home_side_talk
    hide pia_home 
    with dissolve
    "[mcname!c] dan Pia pun belajar bersama di cafe tersebut hingga larut malam [mcname!c] pun memutuskan meminjamkan buku tersebut ke Pia."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Pagi Siang.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya..."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(2.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname!c]" "{i}Duhhh. Hari ini ujian tertulis paling susah. Deg deg an, huhu.{/i}"
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kelas.ogg" fadein 1.0 volume (1.5)
    scene kelas with Dissolve(1.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "Suasana kelas sepi, semua sibuk belajar dan menghapal. Ya, hari ini ada ujian tertulis mata kuliah xxx."
    show pia at pia_near with dissolve
    "[mcname!c]" "Pagi Mbak Pia~"
    show pia_talk at pia_near 
    show pia_side_talk at left 
    with dissolve
    pia "Sssst, diem. Komposisi dan elemen dalam warna—\n*Berbisik sambil menghafal*"
    hide pia_talk 
    hide pia_side_talk 
    with dissolve
    "[mcname!c]" "Ahahahaha!"
    hide pia with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    play music "audio/BGM_Dosen.ogg" fadein 1.0
    scene kelas with Dissolve(1.0)
    show dosen_talk at dosen_center 
    show dosen_side at left 
    with dissolve
    $ quick_menu = True
    dosen "Pagi!!"
    dosen "Semua buku dan HP simpan di depan ya."
    dosen "Di atas meja hanya boleh ada alat tulis."
    dosen "Ujian kita mulai 10 menit lagi."
    "Mahasiswa/i" "Baik buu~"
    $ quick_menu = False
    jump quiz

label goodpiaafterquiz:
    $ renpy.block_rollback()
    $ quick_menu = True
    "Selesai ujian, semua mahasiswa/i mengumpulkan lembar jawaban ke pengawas. Ujian hari itu berakhir."
    "[mcname!c]" "Hueeeee selesai juga ini ujian.\n*Liat kanan kiri*"
    show pia at pia_near with dissolve
    pia "...."
    "[mcname!c]" "Hahahaha gimana? Lancar? Bisa kan jawabnya?"
    show pia_talk at pia_near 
    show pia_side_talk at left 
    with dissolve
    pia "Bisa lah, yang bener aja! Cuma kayak ada yang kurang puas aja weh. Harusnya aku tambahin blablabla-"
    hide pia_talk 
    hide pia_side_talk 
    with dissolve
    "[mcname!c]" "Pia, sepanjang ujian tadi anak-anak lain cuma selembar doang terus dikumpulin, loh. Kamu sampe minta nambah lembar jawaban dua kali."
    "[mcname!c]" "DUA KALI!!"
    "[mcname!c]" "Lu ngisi apa bikin AU?"
    show pia_side_talk at left 
    show pia_talk at pia_near 
    with dissolve
    pia "Dih, aku tuh harus sempurna! Harus nilai 100!"
    hide pia_talk 
    hide pia_side_talk 
    with dissolve
    "[mcname!c]" "Kasian Bu Dosen yang meriksa jawaban kamu. Kayak baca novel, hahaha."
    show pia_shock at pia_near 
    show pia_side_shock at left 
    with dissolve
    pia "Iiiiih!!\n*Mukul-mukul [mcname!c]*"
    hide pia_shock 
    hide pia_side_shock 
    with dissolve
    "[mcname!c]" "Ahahaha, eh hari ini mau ke mana? Pusing gak sih? Mau refreshing gak sih? Huhuhu~"
    show pia_talk at pia_near 
    show pia_side_talk at left 
    with dissolve
    pia "Rooftop yuk! Aku nunggu di sana, kamu ke kantin beli cemilan yang banyaaaaak! Nanti kita makan di rooftop."
    hide pia_talk 
    hide pia_side_talk 
    with dissolve
    "[mcname!c]" "Meeeh, gue yang beli nih?"
    show pia_talk at pia_near 
    show pia_side_talk at left 
    with dissolve
    pia "Yang buat aku pake uangku lah, nih. Aku tunggu di rooftop yaaa."
    pia "Dadaaaah~"
    hide pia
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "Pia pun pergi ke luar kelas."
    "[mcname!c]" "Eeeeehh?"
    "[mcname!c]" "Hadeh, bukan masalah uangnya... Tapi aku beli sendiri nih? Huhuhu kayak piaraan aja gue disuruh suruh. Bener-bener ya, Meameo."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kantin.ogg" fadein 1.0
    scene kantin with Dissolve(1.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname!c] pun ke kantin untuk beli beberapa cemilan untuk dibawa ke rooftop untuk makan bareng Pia."
    "[mcname!c]" "*Sambil bawa plastik berisi beberapa camilan*"
    "[mcname!c]" "Hmmm... apa lagi ya? Kayanya beli snack itu enak."
    show fio_side at left with dissolve
    fio "[mcname!c]!!!!"
    hide fio_side with dissolve
    "[mcname!c]" "Woaaa kaget, Cepio hai~"
    show fio_side at left with dissolve
    fio "Sini!!!\n*Sambil menepuk nepuk kursi kosong sebelah Fiony*"
    hide fio_side with dissolve
    "[mcname!c]" "Halo Cepio~\n*Nyamperin*"
    show kana at kana_near_left_2 
    show freya at freya_near_right 
    show fio_talk at fio_near 
    show fio_side at left 
    with dissolve
    fio "Kenalin, ini Freya, kalo yang sebelahnya Kana."
    show fio at fio_near 
    hide fio_side 
    with dissolve
    "[mcname!c]" "Halo, namaku [mcname!c]. Salam kenal."
    show kana_talk at kana_near_left_2
    show kana_side_talk at left 
    with dissolve
    kana "*Memicingkan mata sambil mengisyaratkan sesuatu*"
    kana "Ehm... Yang Mulia Piaraan?"
    hide kana_talk 
    hide kana_side_talk
    show freya_side_smile at left 
    with dissolve
    freya "Hadeeeh, Naaaaay."
    hide freya_side_smile with dissolve
    "[mcname!c]" "???"
    show kana_talk at kana_near_left_2 
    show kana_side_talk at left 
    with dissolve
    kana "Eh, Kak Fiony, bukan ini orangnya?"
    hide kana_talk
    hide kana_side_talk 
    show fio_side at left 
    hide fio 
    with dissolve
    fio "Meameo? Bukaaaan. Ini mah belahan jiwanya."
    show fio at fio_near 
    hide fio_side 
    with dissolve
    "[mcname!c]" "Whaaat. Cepiooooo~"
    show fio_smile at fio_near 
    show fio_side_smile at left 
    with dissolve
    fio "Ahahaha, gini [mcname!c]. Ini Kana mau banget ketemu Pia. Dia suka banget gambarnya Pia."
    hide fio_smile 
    hide fio_side_smile 
    show kana_talk at kana_near_left_2 
    show kana_side_talk at left 
    with dissolve
    kana "Iya! Aku mau ajak dia join club jejepangan. Kira-kira mau gak, ya?"
    hide kana_talk 
    hide kana_side_talk 
    with dissolve
    "[mcname!c]" "Oh, kamu anak club jejepangan?"
    "[mcname!c]" "Pas itu sempet sih, aku kasih liat flyer yang dibagiin. Tapi kayaknya dia gak terlalu tertarik."
    show kana_talk at kana_near_left_2 
    show kana_side_talk at left 
    with dissolve
    kana "Sasuga Yang Mulia Piaraan, butuh usaha lebih buat rekrut dia!"
    hide kana_talk 
    hide kana_side_talk 
    with dissolve
    "[mcname!c]" "Yang Mulia Piaraan?"
    show kana_talk at kana_near_left_2 
    show kana_side_talk at left 
    with dissolve
    kana "Oh ah, enggak enggak. Nanti aku ajak Tono buat rekrut dia. Harus bisa pokoknya!"
    hide kana_talk 
    hide kana_side_talk
    hide fio 
    with dissolve
    "{size=-5}Freya & Fiony{/size}" "Semangat Naay~"
    show fio at fio_near with dissolve 
    "[mcname!c]" "Ahahaha nanti aku coba tanyain lagi deh ya, semoga berubah pikiran. Aku pergi dulu ya. Duluan semua~"
    "{size=-8}Freya, Fiony, Kana{/size}" "Iya, byeee~"
    hide fio_talk
    hide kana
    hide freya
    hide fio
    with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Rooftop Siang.ogg" fadein 1.0 volume 2.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Di rooftop..."
    $ quick_menu = False
    scene rooftop with Dissolve(2.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "Pia sedang menari diiringi lagu idol di HPnya yang diputar agak keras."
    "[mcname!c]" "*Duduk bersila di belakang Pia*"
    "Pia menoleh ke belakang."
    show pia_shock at pia_near 
    show pia_side_shock at left 
    with dissolve
    pia "Hueeeh kaget!! Udah di sini aja, diem-diem gak ada suara! Bikin jantungan aja."
    hide pia_side_shock with dissolve
    "[mcname!c]" "Mana ada? Kamu aja yang terlalu serius sampe gak perhatiin sekitar, haha."
    show pia_smile at pia_near 
    hide pia_shock
    show pia_side_smile at left 
    with dissolve
    pia "Hehehe~\n*Ikut duduk bersila sebelah [mcname!c]*"
    hide pia_side_smile at left with dissolve
    stop music fadeout 1.0
    "[mcname!c]" "Yang Mulia Piaraan."
    play music "audio/BGM_Funny 1.ogg" fadein 0.5
    # show pia_shock at pia_near 
    hide pia_smile
    show pia nyembur 2
    show pia nyembur 2:
        ypos 0.74 zpos 0.0 zoom 0.25 
    with dissolve
    show pia_side_shock at left with dissolve
    pia "Uhuk uhuk!!! Hoooeeek guuuh!! Uhuk!!!"
    hide pia nyembur 2
    show pia_shock at pia_near 
    with dissolve
    pia "KOK KAMU TAU PEN NAME AKU, TAU DARI MANA?"
    hide pia_side_shock with dissolve
    "[mcname!c]" "Jadi itu beneran kamu? Ahahaha."
    show pia_talk at pia_near 
    hide pia_shock
    show pia_side_talk at left 
    with dissolve
    pia "Eh tau dari mana????"
    show pia at pia_near 
    hide pia_side_talk 
    with dissolve
    "[mcname!c]" "Tadi di kantin aku ketemu fans kamu. Dia nyariin kamu bareng Cepio tuh."
    hide pia 
    show pia_side_talk at left 
    with dissolve
    pia "Heeeeee~"
    show pia at pia_near 
    hide pia_side_talk 
    with dissolve
    "[mcname!c]" "Tapi itu nama apa, dah?"
    hide pia 
    show pia_side_talk at left 
    with dissolve
    pia "Ahahaha itu pen name aku kalo gambar. Aku sering gambar gitu kan, terus diupload di medsos. Nah nama akun gambar aku tuh, Yang Mulia Piaraan."
    show pia at pia_near 
    hide pia_side_talk 
    with dissolve
    "[mcname!c]" "Owalah gitu toh."
    hide pia 
    show pia_side_talk at left 
    with dissolve
    pia "Aku gak nyangka aja ada yg kenal nama itu dan tau. Aku gak nyembunyiin, sih. Cuma malu aja pen name aku kayak gitu, haha."
    show pia at pia_near 
    hide pia_side_talk 
    with dissolve
    "[mcname!c]" "Lah lagian. Kenapa Yang Mulia Piaraan, dah?"
    hide pia 
    show pia_side_talk at left 
    with dissolve
    pia "Ya maap sih, dulu masih wibu wibunya asal ngasih nama. Eh taunya udah nyaman, hahaha."
    pia "Jadi dulu tuh aku suka gambar fanart anime, manga, gitu-gitu. Terus ada beberapa yang aku jual juga di online jadi merch. Mungkin orang itu salah satu yang beli."
    show pia at pia_near 
    hide pia_side_talk 
    with dissolve
    "[mcname!c]" "Oooh gitu toh."
    hide pia 
    show pia_side_talk at left 
    with dissolve
    pia "Iyaaa~"
    $ quick_menu = False
    scene black with Dissolve(1.0)
    stop music fadeout 1.0
    play music "audio/BGM_Rooftop Siang.ogg" fadein 1.0 volume 2.0
    scene rooftop with Dissolve(1.0)
    $ quick_menu = True
    "[mcname!c]" "Btw tadi mereka juga sempet nanyain, mau join club jepang, gak?"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Err… Engga deh. Aku mau lonewolf. Udah gak terlalu jejepangan banget."
    show pia at pia_near 
    hide pia_side_talk 
    with dissolve
    "[mcname!c]" "Hmmm.... gitu."
    hide pia 
    show pia_side_talk at left 
    with dissolve
    pia "Emang kamu ngerti jejepangan?"
    show pia at pia_near 
    hide pia_side_talk 
    with dissolve
    "[mcname!c]" "Beuh, perlu aku jelasin sinopsis 3 episode pertama setiap anime yang airing season ini gak nih?"
    hide pia at pia_near 
    show pia_side_talk at left 
    with dissolve
    pia "IH WIBUUUU!!"
    show pia at pia_near 
    hide pia_side_talk 
    with dissolve
    "[mcname!c]" "Ahahahahah."
    hide pia 
    show pia_side_talk at left 
    with dissolve
    pia "Tapi bener deh, aku tuh gatau kenapa jadi agak kurang buat bersosialisasi gitu... Tapi di sisi lain, aku mau punya banyak temen dan kenal orang baru. Tapi males aja memulai."
    show pia at pia_near 
    hide pia_side_talk 
    with dissolve
    "[mcname!c]" "Wakaru Pia, wakaru…"
    show pia_sad at pia_near 
    show pia_side_sad at left 
    with dissolve
    pia "Aaaah, jangan wibuuu :((("
    hide pia_side_sad with dissolve
    "[mcname!c]" "Ahahaha becandaa~ Tapi bener deh, kamu gamau join? Kalo kamu join, aku juga deh. Gimana?"
    hide pia
    hide pia_sad 
    show pia_side_talk at left 
    with dissolve
    pia "Yeuuu, itu mah emang kamu aja kan yang mau."
    show pia at pia_near 
    hide pia_side_talk 
    with dissolve
    "[mcname!c]" "Gak gituuuuu~"
    hide pia_talk
    hide pia 
    with dissolve
    "[mcname!c] dan Pia pun banyak bercerita sambil menikmati cemilan di rooftop."

    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    $ roadto_rock_idol.grant()
    scene chapter 3 pia with Dissolve (1.0)
    pause(3.0)
    scene black with Dissolve (1.0)
    play music "audio/BGM_UKM.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Di tempat lain..."
    $ quick_menu = False
    scene ruang ukm with Dissolve(2.0)
    show kana_talk at kana_near_left_2
    show tana at tana_right
    show kana_side_talk at left
    with dissolve
    $ quick_menu = True
    kana "Ton! Kita harus rekrut Meameo join club jepang ini! Gambar dia bagus! Cocok jadi ilustrator club kita!"
    show kana at kana_near_left_2 
    hide kana_side_talk 
    show tana_talk at tana_right 
    show tana_side_talk at left 
    with dissolve
    tana "Itu siapa lagi, Nay? Nama dia Meameo? Aneh juga…"
    hide tana_talk 
    hide tana_side_talk 
    hide kana 
    show kana_side_talk at left 
    with dissolve
    kana "Duh aku lupa nama aslinya, tapi sedenger aku dari Kak Fiony nama dia Meameo"
    show kana at kana_near_left_2 
    hide kana_side_talk
    show tana_talk at tana_right 
    show tana_side_talk at left 
    with dissolve
    tana "Err..oke\n*Siapa pula itu Fiony*"
    hide tana_side 
    hide tana_side_talk 
    hide kana 
    show kana_side_talk at left 
    with dissolve
    kana "Dia anak DKV. Besok di gedung DKV ada pameran karya lagi, kita cari dia!"
    hide kana_side_talk with dissolve
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Lorong.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya.."
    $ quick_menu = False
    scene lorong with Dissolve(2.0)
    show tana_talk at tana_right 
    show kana at kana_near_left_2
    show tana_side_talk at left 
    with dissolve
    $ quick_menu = True
    tana "Woaaaa bagus-bagus ya, gambarnya."
    show tana at tana_right 
    hide tana_side_talk 
    show kana_talk at kana_near_left_2 
    show kana_side_talk at left 
    with dissolve
    kana "Ton! Misi kita disini untuk rekrut Meameo"
    hide kana_talk 
    hide kana_side_talk 
    hide tana 
    show tana_side_talk at left 
    with dissolve
    tana "Iye bang. Kayak gimana tuh, orangnya?"
    show tana at tana_right 
    hide tana_side_talk 
    show kana_side at left 
    with dissolve
    kana "......"
    kana "......."
    hide kana_side 
    hide tana 
    show tana_side_talk at left 
    with dissolve
    tana "Nay?"
    show tana at tana_right 
    hide tana_side_talk 
    show kana_talk at kana_near_left_2 
    show kana_side_talk at left 
    with dissolve
    kana "Aku gak tau kayak gimana orangnya…"
    hide kana_talk 
    hide kana_side_talk 
    show tana_side at left 
    with dissolve
    tana "................"
    hide tana_side with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kampus.ogg" fadein 1.0
    scene depan kampus with Dissolve(1.0)
    $ quick_menu = True
    "[mcname!c]" "{i}Akhirnya sampe juga di kampus.{/i}"
    "[mcname!c]" "{i}Ga sabar mau liat pamerah bulan ini!{/i}"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Lorong.ogg" fadein 1.0
    scene lorong with Dissolve(1.0)
    $ quick_menu = True
    play sound "crowd_noise.mp3" loop fadein 1.0 volume (4.0)
    "[mcname!c]" "Wah rame juga yang liat-liat pameran, ya."
    "Tiba-tiba, [mcname!c] melihat ada 2 orang berlari menuju ke arahnya."
    "[mcname!c]" "Waduh, lari ke gue gak sih? Apa belakang gue? Belakang gue ga ada orang sih."
    "*[mcname!c] berjalan meminggir agar tidak menghalangi 2 orang tersebut*"
    play sound "audio/run.mp3" fadein 1.0 volume (10.0)
    "[mcname!c]" "Kayaknya fix lari ke gue"
    stop sound fadeout 1.0
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "[mcname!c]! Nama kamu [mcname!c] kan?"
    show kana at kana_near 
    hide kana_talk
    hide kana_side_talk 
    with dissolve
    "[mcname!c]" "Ooh! Temennya cepio yah, ada apa nih?"
    show kana_talk at kana_near 
    show kana_side_talk at left 
    with dissolve
    kana "Kamu kenal Meameo kan?"
    hide kana_talk 
    hide kana_side_talk 
    with dissolve
    "[mcname!c]" "Pppffftt… Meameo."
    "[mcname!c]" "Iya kenal kok, tadi orangnya lagi selfie depan lukisannya. Mau ketemu?"
    show kana_talk at kana_near 
    show kana_side_talk at left 
    with dissolve
    $ tono_name = "Tana"
    kana "Iya! Oh kenalin, ini Tana."
    hide kana
    hide kana_talk 
    hide kana_side_talk 
    show kana at kana_near_left_2 
    show tana_talk at tana_right
    show tana_side_talk at left 
    with dissolve
    tana "Wazzup bro!"
    show tana at tana_right 
    hide tana_talk
    hide tana_side_talk 
    with dissolve
    "[mcname!c]" "Y-yeah, wazzup.."
    hide kana 
    hide tana 
    with dissolve
    "[mcname!c] pun membawa Kana dan Tana ke Pia yang sedang berfoto dengan lukisannya."
    stop sound fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    scene lorong with dissolve
    $ quick_menu = True
    "[mcname!c]" "Oi MEAMEO, ada yang mau ketemu kamu nih."
    show pia_talk at pia_near 
    show pia_side_talk at left 
    with dissolve
    pia "Geeeeh apalah meameo."
    hide pia_side_talk 
    hide pia_talk 
    show tana at KTP_Tana 
    show pia at KTP_Pia 
    show kana_talk at KTP_Kana 
    show kana_side_talk at left 
    with dissolve
    kana "Meameo!!!"
    kana "Join club jepang yuk!"
    show kana at KTP_Kana 
    hide kana_talk
    hide kana_side_talk
    show pia_shock at KTP_Pia
    show pia_side_shock at left
    with dissolve
    pia "Heeeeeeeee…"
    pia "Tunggu..."
    show pia_silent at KTP_Pia
    hide pia_shock
    show pia_side_silent at left
    hide pia_side_shock
    with dissolve
    pia "Pertama, nama aku Meraleo."
    pia "MERALEO!"
    pia " Bukan Meameo!"
    pia "Kedua, aku gamau masuk club jepang."
    pia "SIBUK!"
    pia "Ketiga."
    pia "Kalian siapa?"
    hide pia_side_silent
    show tana_talk at KTP_Tana
    show tana_side_talk at left
    with dissolve
    tana "Naya, Naya…."
    tana "Minimal perkenalan dulu."
    tana "Halo Kak Meraleo, aku Tana, dia Kana."
    tana "Kita dari club jepang."
    tana "Nah, tujuan kita mau invite kamu ke club jepang nih"
    tana "Kita suka gambar kamu, siapa tau tertarik kan."
    hide tana_talk
    hide tana_side_talk
    show pia_talk at KTP_Pia
    hide pia_silent
    show pia_side_talk at left
    with dissolve
    pia "Oh, panggil aku Pia aja."
    pia "Makasih undangannya, tapi kayaknya enggak dulu deh. Belum tertarik join club."
    hide pia_talk
    hide pia_side_talk
    show kana_talk at KTP_Kana 
    show kana_side_talk at left
    with dissolve
    kana "Yaaah, oke deh. Belum tertarik kan. Bukan tidak tertarik!"
    kana "Oke. Besok aku akan cari kamu lagi buat join"
    show tana:
        subpixel True xpos -1.87 
    hide kana_side_talk
    hide kana_talk
    hide kana
    with dissolve
    show pia:
        subpixel True xpos 0.64 
    show tana_talk:
        subpixel True xpos -1.87 
    hide kana_side_talk
    hide kana_talk
    hide kana
    with dissolve
    show tana_side_talk at left
    show tana_talk at KTP_Tana
    show tana_talk:
        subpixel True xpos -1.87 
    with dissolve
    tana "Lah udah nyerah ngomongnya gitu doang…"
    tana "Pergi dulu ya [mcname!c], Pia. Maap suka aneh emang Kana Kana itu"
    hide tana_talk 
    hide tana
    hide tana_side_talk
    hide pia
    show pia_silent at pia_near
    show pia_side_silent at left
    with dissolve
    pia "Hadeeh..."
    show pia_talk at pia_near
    hide pia_silent
    show pia_side_talk at left
    hide pia_side_silent
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Yaudah, aku juga pulang dulu [mcname!c]. Babayy~"
    hide pia_side_talk
    hide pia_talk
    hide pia
    with dissolve
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "BGM_Kampus.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    show kana_side_talk at left with dissolve
    $ quick_menu = True
    "Keesokan harinya..."
    kana "Ayoook join klub Jepaang~"
    hide kana_side_talk
    show pia_side_silent at left
    with dissolve
    pia "G."
    hide pia_side_silent with dissolve
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "BGM_Kampus Sore.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    show tana_side_talk at left with dissolve
    $ quick_menu = True
    "Tiga hari kemudian..."
    tana "Mau join klub Jepaang gak bro?"
    hide tana_side_talk
    show pia_side_silent at left
    with dissolve
    pia "G."
    hide pia_side_silent with dissolve
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "BGM_Kampus.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    show kana_side_talk at left with dissolve
    $ quick_menu = True
    "Beberapa hari kemudian..."
    kana "Haloo, kamu cantik bangeet~"
    hide kana_side_talk
    show pia_side_silent at left
    with dissolve
    pia "G."
    hide pia_side_silent with dissolve
    "Beberapa kali pun setiap Pia bertemu Tana dan Kana, dia langsung diajak join club."
    "Namun jawaban Pia tetap sama."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Rooftop Siang.ogg" fadein 1.0 volume 2.0
    scene rooftop with Dissolve(1.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "Pia dan [mcname!c] sedang beristirahat sehabis selesai matkul nirmana."
    "[mcname!c]" "Mau muntah aku ngerjain nirmana. Susaaaaah."
    show pia_smile at pia_near
    show pia_side_smile at left
    with dissolve
    pia "Ahahahaha betuuuul"
    hide pia_side_smile with dissolve
    "[mcname!c]" "BTW, kayaknya Si Kana Tana makin sering tuh ngajak kamu join haha."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Iya sih. Gigih banget ya."
    show pia at pia_near
    hide pia_talk
    hide pia_smile
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Kamu ga mau coba dulu? Iseng aja gitu, mampir ato liat liat dulu ruang clubnya."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Jujur nih, sebenernya penasaran juga sih. Cuma ga ah!"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Ara ara, penasaran ya?\n*smug face*"
    show pia_silent at pia_near
    show pia_side_silent at left
    with dissolve
    pia "Heh apalah!"
    hide pia_side_silent with dissolve
    "[mcname!c]" "Kan aku bilang, kamu join aku join. Gimana?"
    pia "*Menghembuskan nafas*"
    hide pia_silent
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Haaaaah….. okeh deal"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Lesgooooo"
    hide pia with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "BGM_UKM.ogg" fadein 1.0
    scene ruang ukm with Dissolve(1.0)
    show kana_confused at FeniKanaTana_Kana
    show tana at FeniKanaTana_Tana
    show feni at FeniKanaTana_Feni
    show kana_side_confused at left
    with dissolve
    $ quick_menu = True
    kana "Haaaah, pake strategi apa lagi ya buat ngajak Pia join ke sini?"
    hide kana_side_confused with dissolve
    show feni_awe at FeniKanaTana_Feni
    show feni_side_awe at left
    with dissolve
    feni "Emang sekeren itu ya desainnya?"
    show feni at FeniKanaTana_Feni
    show kana_talk at FeniKanaTana_Kana
    show kana_side_talk at left
    hide feni_awe
    hide feni_side_awe
    with dissolve
    kana "IYA KAK! SEKEREN ITU"
    show tana at FeniKanaTana_Tana 
    show feni at FeniKanaTana_Feni 
    show kana at FeniKanaTana_Kana 
    hide kana_side_talk
    show tana_talk at FeniKanaTana_Tana
    show tana_side_talk at left
    with dissolve
    tana "Alah, bias aja itu mah Kak"
    hide tana_talk
    hide tana_side_talk
    show kana_cry at FeniKanaTana_Kana
    show kana_side_cry at left
    with dissolve
    kana "Aaah Tono maaah"
    hide kana_side_cry
    with dissolve
    show feni_talk at FeniKanaTana_Feni
    show feni_side_talk at left
    with dissolve
    feni "Eeh udah udah jangan berantem ih."
    feni "Kalo emang gak mau ya, mau gimana atuh."
    hide feni_talk
    hide feni_side_talk
    hide kana_cry
    with dissolve
    play sound "SFX - Knocking.mp3" volume 5.0
    show feni_talk at FeniKanaTana_Feni 
    show feni_side_talk at left
    with dissolve
    feni "Nay, bukain atuh pintunya. Kamu yang paling deket pintu"
    hide feni_talk
    hide feni_side_talk
    with dissolve
    show kana_side_cry at left with dissolve
    kana "Iya kak\n*Nada lemes*"
    hide kana_side_cry with dissolve
    $ quick_menu=False
    scene black with Dissolve(1.0)
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    scene ruang ukm with Dissolve(1.0)
    show kana_shy at kana_near
    hide kana_cry
    show kana_side_shy at left
    with dissolve
    $ quick_menu = True
    kana "Hah [mcname!c]??? Ngapain."
    hide kana_side_shy with dissolve
    "[mcname!c]" "Halo."
    "[mcname!c]" "J-jadi gini…"
    hide kana
    hide tana
    hide feni
    hide kana_shy
    show pia_shock
    show pia_shock:
        pos (1.11, 2.63) rotate -27.0 
    with dissolve
    "dari belakang [mcname!c], Pia menunjukan dirinya dengan malu malu"
    hide pia_shock with dissolve
    show pia_shock at pia_near
    show pia_side_shock at left
    with dissolve
    pia "Aloo~\n*malu malu*"
    hide pia_shock 
    hide pia_side_shock
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "YANG MULIA PIARAAN?????\n*Syok*"
    hide kana_talk
    hide kana_side_talk
    show pia_silent at pia_near
    show pia_side_silent at left
    with dissolve
    pia "Woi -_-"
    hide pia_side_silent with dissolve
    "[mcname!c]" "Jadi gini, kita mutusin untuk ikut join club jepang, masih buka kah?"
    hide pia_silent 
    show kana_smile at kana_near
    show kana_side_smile at left
    with dissolve
    kana "Masih!!! Masuuuuk"
    hide kana_smile
    hide kana_side_smile 
    with dissolve
    "Mereka semua pun masuk dan duduk bersama anggota lain"
    "Sambil berbincang dan perkenalan ke anggota lain"
    show feni_talk at feni_center
    show feni_side_talk at left
    with dissolve
    feni "Welcome, kita gak ada interview interview. Selamat join club jepang yaaa"
    hide feni_talk
    hide feni_side_talk
    show kana_smile at kana_near
    show kana_side_smile at left
    with dissolve
    kana "HOREEEEEEE!!!"
    hide kana_smile
    hide kana_side_smile
    show feni_talk at feni_center
    show feni_side_talk at left
    with dissolve
    feni "Aku ada kelas abis ini. Maaf ya ga bisa nemenin dan bantu jelasin. Kana nanti yang bantu, tolong ya Nay."
    hide feni_talk
    hide feni_side_talk
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    $ feni_name = "Feni"
    kana "Siap Kak Feni!!"
    hide kana_talk
    hide kana_side_talk
    show kana at kana_near_left 
    show pia at pia_near_right
    show kana_talk at kana_near_left
    show kana_side_talk at left
    with dissolve
    kana "Ehm, jadi gini. Di club ini ada banyak divisinya. Pia kita butuhin buat desain. Mau ya? Mau yaaa?"
    hide kana_talk
    hide kana_side_talk
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Iya iya, aku coba ya."
    hide pia_talk
    hide pia_side_talk
    show kana_talk at kana_near_left
    show kana_side_talk at left
    with dissolve
    kana "Terus selain itu kita ada divisi dance / idoling, budaya tradisional jepang, game, dan anime manga tokusatsu"
    hide kana_talk
    hide kana_side_talk
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Ehhh begitu, ya."
    hide pia_talk
    hide pia_side_talk
    show kana_talk at kana_near_left
    show kana_side_talk at left
    with dissolve
    kana "Iyaaaa."
    kana "Pokoknya kalo ada apa-apa, aku siap membantu!"
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Kalo begitu, mohon bantuannya~"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Kampus.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Beberapa hari kemudian..."
    $ quick_menu = False
    scene depan kampus with Dissolve(2.0)
    $ renpy.block_rollback()
    $ quick_menu = True 
    "Pia mendapatkan tugas untuk membuat desain yang diperlukan untuk acara matsuri yang akan diselenggarakan club jejepangannya tersebut"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Lorong.ogg" fadein 1.0
    scene lorong with Dissolve(1.0)
    $ renpy.block_rollback()
    $ quick_menu = True 
    "Saat Pia sedang berjalan menuju ruang UKM, samar-samar terdengar suara candaan anggota club di ruang sebelah."
    show feni_side_talk at left with dissolve
    feni "Gerak ke kiri, Kana... Hahahahaha."
    hide feni_side_talk 
    show tana_side_talk at left 
    with dissolve
    tana "Hahahaha. Jangan kakuuuuu"
    hide tana_side_talk with dissolve
    $ quick_menu = False
    show pia_shock
    show black
    show pia_shock:
        default
        subpixel True 
        parallel:
            Null(1717.0, 2510.0)
            'pia_shock'
        parallel:
            pos (0, 0) rotate 0.0 
            linear 0.04 pos (1260, 2889) rotate -18.0 
    show black:
        default
        subpixel True 
        parallel:
            Null(0.0, 0.0)
            'black'
        parallel:
            xpos 0 
            linear 0.04 xpos -72 
    show black as black2:
        default
        subpixel True 
        parallel:
            Null(0.0, 0.0)
            'black'
        parallel:
            xpos 0 
            linear 0.04 xpos 2007
    with dissolve 
    $ quick_menu = True
    "Pia yang penasaran pun mengintip dibalik pintu yang sedikit terbuka itu"
    show pia_side_shock at left with dissolve
    pia "{i}lagi pada ngapain sih?{/i}"
    hide pia_side_shock with dissolve
    "Terlihat Kana dan Tana sedang berlatih dance"
    show pia_side_talk at left with dissolve
    pia "{size=-10}Woaaaa… Ternyata Kana sama Tana boleh juga ya ngedancenya.{/size}"
    hide pia_side_talk with dissolve
    "Pia pun menatap mereka dengan perasaan iri, namun penasaran sehingga tetap melihat dari balik pintu itu."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "BGM_Kampus Sore.ogg" fadein 1.0
    scene lorong sore with Dissolve(1.0)
    $ quick_menu = True
    "Tak terasa hari telah sore, Pia terus menerus melihat Tana & Kana latihan."
    "Pia melihat dengan tatapan mau tapi malu."
    "[mcname!c]" "Pia..."
    "Saat [mcname!c] meliat Pia yang seperti ini, dia menyadari bahwa di dalam hati kecil Pia, masih ada cita-cita yang sudah lama dikubur."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "BGM_UKM.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya..."
    $ quick_menu = False
    scene ruang ukm with Dissolve(2.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname!c]" "Kana, Tana. Mau tanya dong. Kira-kira kalian masih butuh anggota, gak?"
    show kana at kana_near_left_2 
    show tana at tana_right 
    show tana_talk at tana_right 
    show tana_side_talk at left
    with dissolve
    tana "Jujurly masih bro, kenapa?"
    tana "Kamu mau jadi idol?"
    tana "Coba joget dong."
    hide tana_talk 
    hide tana_side_talk
    with dissolve
    "[mcname!c]" "Bukan akuuuuuuu, tapi Pia."
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "HAH? Serius? Dia mau?"
    hide kana_talk 
    hide kana_side_talk
    hide kana
    hide tana
    with dissolve
    "[mcname!c] pun menceritakan tentang cita-cita yang sebelumnya pernah diceritakan Pia"
    "......."
    show kana at kana_near_left_2 
    show tana at tana_right 
    show kana_cry at kana_near_left_2
    show kana_side_cry at left
    with dissolve
    kana "Wow, aku mau nangis. Kenapa Pia hentiin cita citanya itu, ih?"
    show kana_talk at kana_near_left_2
    hide kana_cry
    show kana_side_talk at left
    hide kana_side_cry
    with dissolve
    kana "Aku mau ngajak dia! Akan aku bujuk!"
    hide kana_talk
    hide kana_side_talk
    with dissolve
    "[mcname!c]" "Sabar, biar aku. Kalian tunggu aja ya. Jangan bilang-bilang Pia dulu."
    show tana_talk at tana_right
    show tana_side_talk at left
    with dissolve
    tana "Aman~"
    hide tana_side_talk
    hide tana
    hide kana
    hide tana_talk
    with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Rooftop Romance Pia.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu=True
    "Sore itu..."
    $ quick_menu = False
    scene rooftop sore with Dissolve(2.0)
    show pia at pia_near
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname!c]" "Pia, aku mau ngomong dong"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Yak, apa nih? Tumben"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Kamu percaya sama aku kan, Pia?"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Err…i-iya..kenapa nih?"
    hide pia_talk
    hide pia_side_talk
    show ticket
    show ticket:
        pos (0.29, 0.89) zoom 0.25 
    with dissolve
    "[mcname!c]" "Aku masih punya 1 tiket permintaan kan? Aku mau pake tiket itu"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Wow, oke. Apa nih?"
    hide ticket
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "JADI IDOL!!!"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "[mcname!c]… Kan aku udah bilang gamau..."
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Hmm.. Padahal katanya mau request apa aja bisa… Hmm"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Tapi ga gitu"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Yaudah aku ganti, kamu nyoba dan ngeliat langsung dari deket"
    "[mcname!c]" "Gimana? Gampang kan?"
    show pia_shock at pia_near
    show pia_side_shock at left
    with dissolve
    pia "Heeeeeh."
    show pia_silent at pia_near
    show pia_side_silent at left
    with dissolve
    pia "Aaaa nyesel sok ngide ngasi gituan ih."
    hide pia_shock
    hide pia_side_shock
    hide pia_side_silent
    with dissolve
    "[mcname!c]" "Hehe gimana? Gampang loh"
    show pia_side_silent at left
    with dissolve
    pia "Iya deh. Iya iya."
    hide pia_side_silent
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Hehehe~"
    hide pia_silent
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Tapi kamu mau nemenin aku kan?"
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Pasti, lah. Aku akan selalu ada di sini, kok."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "[mcname!c]..."
    pia "Baiklah! Aku bakal ngomong ke mereka!"
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Nanti aku temenin kok, santai aja."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Makasih ya, [mcname!c]..."
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Anytime Pia..."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play music "audio/BGM_Sore.ogg" fadein 1.0
    scene lorong sore with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    "Pia sampai di depan ruang club, ditemani [mcname!c] di belakangnya sambil tersenyum."
    pia "Hufff. Tenangkan diri..."
    hide pia_side_talk with dissolve
    "[mcname!c]" "Cemangat Piyak~"
    stop music fadeout 1.0
    $ quick_menu=False
    scene black with Dissolve(1.0)
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    play music "BGM_UKM.ogg" fadein 1.0
    scene ruang ukm sore with Dissolve(1.0)
    show pia at pia_near with dissolve
    $ renpy.block_rollback()
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    $ quick_menu = True
    pia "AKU MAU JADI IDOL! AJAK AKU BAAANG~"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "Kana yang sedang makan kue pun sampai menjatuhkan kuenya ke meja"
    hide pia 
    show kana at kana_near_left_2 
    show tana at tana_right 
    with dissolve
    "Kana & Tana" "*Saling tatap tatapan*"
    show kana_talk at kana_near_left_2
    show tana_talk at tana_right
    with dissolve
    "Kana & Tana" "LESGOOOOO!! YAAAAY!"
    hide kana_talk
    hide tana_talk
    hide kana
    hide tana
    with dissolve
    "Kana dan Tana pun berlari memeluk Pia"
    "[mcname!c]" "Huhu senengnya. Semangat ya, Pia"
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "T-tapi kerjaan Pia siapa yang handle dong ini huhuhu."
    hide kana_talk
    hide kana_side_talk
    with dissolve
    "Tiba tiba terdengar suara seorang gadis cantik dengan rambut ponytail."
    "Wajahnya tegas namun tetap memancarkan kebaikan, memberikan perpaduan unik antara kekuatan dan kehangatan."
    "Pandangannya tajam dengan senyuman yang lembut, memberikan kesan kehangatan yang melindungi."
    show takamina at takamina_center 
    show takamina_talk at takamina_center
    with dissolve
    # Harusnya takamina side
    takamina "Selow. Biar aku yang handle, tapi ajarin dulu ya, mesti gimana ini ngerjainnya."
    hide takamina
    hide takamina_talk 
    show takamina at takamina_left 
    show pia_shock at pia_near_right
    show pia_side_shock at left
    with dissolve
    pia "A-aman. T-tapi…"
    hide pia_side_shock
    show takamina_talk at takamina_left
    with dissolve
    takamina "Salam kenal, kayaknya kita baru pertama ketemu ya. Namaku Takamina."
    hide takamina_talk 
    hide takamina
    hide pia_shock
    show tana at tana_near 
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    $ takamina_name = "Takamina"
    tana "Ah iya. Kenalin, ini Kak Takamina. Anggota klub ini juga."
    hide tana_talk
    hide tana_side_talk
    hide tana
    show pia at pia_near 
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Aaah. Salam kenal Kak Takaminaa."
    hide pia_talk
    hide pia_side_talk
    hide pia 
    show takamina at takamina_center 
    show takamina_talk at takamina_center
    show takamina_side_talk at left
    with dissolve
    "Takamina" "Alooo, salam kenal."
    "Takamina" "Jadi gimana? Kamu lanjut pindah ke divisi bagian idol kah?"
    hide takamina
    hide takamina_talk
    hide takamina_side_talk
    show pia at pia_near 
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Umm… Apa boleh buat"
    hide pia_talk 
    hide pia_side_talk
    hide pia 
    show feni at feni_center 
    show feni_talk at feni_center
    show feni_side_talk at left
    with dissolve
    feni "Mantap, karena jadi rame. Kayaknya susah euy kalo latihan di dalem gini, sempit ga sih?"
    hide feni_talk
    hide feni_side_talk
    hide feni 
    show kana at kana_near_left_2
    show tana at tana_right
    show kana_talk at kana_near_left_2
    show tana_talk at tana_right
    with dissolve
    "Tana & Kana" "Iya juga."
    hide kana_talk
    hide tana_talk
    with dissolve
    "[mcname!c]" "Hmmmm..."
    menu:
        "[mcname!c]" "Hmmmm..."
        "Gapapa, mau gimana lagi. cuma ada di sini kan tempatnya":
            $ renpy.block_rollback()
            $ quick_menu = True
            "[mcname!c]" "Gapapa, mau gimana lagi. Cuma ada disini kan tempatnya."
            show tana_talk at tana_right
            show tana_side_talk at left
            with dissolve
            tana "Iya sih..."
            hide tana_talk
            hide tana_side_talk
            hide kana
            hide tana
            with dissolve
            "Akhirnya mereka pun latihan di ruang club yang sempit itu."
            $ quick_menu = False
            scene black with Dissolve(1.0)
            scene ruang ukm sore with Dissolve(1.0)
            $ quick_menu = True
            play sound "audio/tabrakan.mp3" volume (4.0)
            "*Brukk*"
            show tana_sad at tana_near
            show tana_side_sad at left
            with dissolve
            tana "Eh maap Pia kesikut kepalanya. Gapapa kan? Sempit huhuhu."
            hide tana_sad
            hide tana_side_sad
            show pia_shock at pia_near
            show pia_side_shock at left
            with dissolve
            pia "Err…gapapa Ton. Aman\n*Sambil mengusap keningnya*"
            hide pia_shock
            hide pia_side_shock
            with dissolve
            "Beberapa saat kemudian, tiba-tiba..."
            stop music fadeout 1.0
            play sound "Glass Breaking.mp3"
            "*CRAAAAAASH*"
            play music "BGM_Bad End.ogg" fadein 1.0
            show pia_sad at pia_near
            show pia_side_sad at left
            with dissolve
            pia "AWWWW!!!"
            hide pia_sad
            hide pia_side_sad
            with dissolve
            "Pia pun menyenggol lemari kaca di ruang club tersebut sampai pecah dan mengenai dirinya."
            "Semua Orang" "PIAAAAAAAA!!"
            "Terlihat Pia penuh luka dan darah, kemudan dibawa ke rumah sakit untuk dilakukan penanganan lebih lanjut."
            $ quick_menu = False
            scene black with dissolve
            show text "{color=#FFF}BEBERAPA MINGGU KEMUDIAN{/color}" with Pause(2.0)
            scene ruang ukm with dissolve
            $ renpy.block_rollback()
            $ quick_menu = True
            $ narasi = "Pia memutuskan untuk tidak ikut club jepang dan tidak beraktivitas menjadi idol lagi."
            show text "{color=#FFF}[narasi!u]{/color}" with Pause(2.0)
            $ quick_menu = False
            scene black with dissolve
            show text "{color=#FF0000}BAD END{/color}" with Pause(2.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits
        "Ke rooftop ga sih? Luas.":
            "[mcname!c]" "Ke rooftop ga sih? Luas."
            jump goodendpiarooftop

label goodendpiarooftop:
    hide kana
    hide tana
    show pia at pia_near 
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "AH BENER JUGA, AYO KE ROOFTOP AJA."
    hide pia_talk
    hide pia_side_talk
    hide pia
    with dissolve
    "Semua Orang" "Let's Gooooo~"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Rooftop Sore.ogg" fadein 1.0 volume 2.0
    scene rooftop sore with Dissolve(1.0)
    show kana at kana_near_left_2
    show pia at pia_near_right
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    $ quick_menu = True
    kana "Waaah sepi ya, luas juga."
    hide kana_talk
    hide kana_side_talk
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Hehehe, ini markas aku sama [mcname!c] nih."
    hide pia_talk
    hide pia_side_talk
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Hmmm… berdua?"
    kana "Kalian ngapain aja berduaan di sini? Hayooo~"
    hide kana_talk
    hide kana_side_talk
    show pia_silent at pia_near_right
    show pia_side_silent at left
    with dissolve
    pia "APAAN IH, CUMA NGOBROL SAMA GAMBAR KOK!!!"
    hide pia_side_silent
    with dissolve
    "[mcname!c]" "Betul."
    show pia_side_silent at left with dissolve
    pia "BANTUIN WEH, BETUL BETUL AJA LU!"
    hide pia_side_silent with dissolve
    "[mcname!c]" "Ya apa lagi? Emang, kan? Ahahahaha."
    hide pia
    hide pia_silent
    hide kana
    with dissolve
    "Hari itu berakhir dengan mereka saling bercanda di rooftop sore itu."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "BGM_Kampus.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya.."
    $ quick_menu = False
    scene depan kampus with Dissolve(2.0)
    $ quick_menu = True
    "[mcname!c]" "{i}Hmmm... Besok pertama kalinya mereka latihan bareng.{/i}"
    "[mcname!c]" "{i}Semoga Pia bisa membangkitkan semangat impiannya dulu.{/i}"
    show tana at tana_near 
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    $ quick_menu = True
    tana "Ah. Pagi, [mcname!c]."
    hide tana_talk 
    hide tana_side_talk
    with dissolve
    "[mcname!c]" "Pagi, besok latihan ya?"
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Iya udah gak sabar hehe."
    tana "Oke gua duluan, byee."
    hide tana_talk
    hide tana_side_talk
    with dissolve
    "[mcname!c]" "Okeeeh."
    hide tana with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Lorong.ogg" fadein 1.0
    scene lorong with Dissolve(1.0)
    $ quick_menu = True
    "[mcname!c]" "Pagi, Pia."
    show pia at pia_near 
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Pagi~"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Denger-denger besok latihan ya?"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Iya sih..."
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Hmmm? Kenapa?"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Aku agak gugup, pertama kalinya perform di depan orang..."
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Semangat Pia! Kamu keren banget loh."
    show pia_shock at pia_near
    show pia_side_shock at left
    with dissolve
    pia "Apa sih [mcname!c].\n*Blush*"
    hide pia_side_shock with dissolve
    "[mcname!c]" "Hahaha, yaudah aku ke kelas dulu ya. Byee~"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    hide pia_shock
    pia "Byee~ See you nanti sore!"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "See you."
    hide pia with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Sore.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "[mcname!c]" "Oke, saatnya ke ruang klub."
    $ quick_menu = False
    scene lorong sore with Dissolve(2.0)
    $ quick_menu = True
    "[mcname!c]" "Ah, Takamina?"
    show takamina at takamina_center 
    show takamina_talk at takamina_center
    show takamina_side_talk at left
    with dissolve
    takamina "Halo, [mcname!c]."
    hide takamina_talk
    hide takamina_side_talk
    with dissolve
    "[mcname!c]" "Mau ke ruang klub juga kah?"
    show takamina_talk at takamina_center
    show takamina_side_talk at left
    with dissolve
    takamina "Iya nih, baru beres rapat BEM."
    hide takamina_talk
    hide takamina_side_talk
    with dissolve
    "[mcname!c]" "Ahh, I see."
    hide takamina with dissolve
    "Takamina dan [mcname!c] berjalan menuju ruang klub."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene ruang ukm sore with Dissolve(1.0)
    $ quick_menu = True
    $ renpy.block_rollback()
    $ quick_menu = True
    "Saat [mcname!c] dan Takamina masuk ke ruangan klub, mereka melihat Kana, Tana, dan Pia yang sedang termenung lesu."
    "[mcname!c]" "Loh kok pada lesu gitu?"
    show kana_cry at KTP_Kana
    show pia_sad at KTP_Pia
    show tana_sad at KTP_Tana
    show kana_side_cry at left 
    with dissolve
    kana "Huuuh..."
    hide kana_side_cry
    show tana_side_sad at left 
    with dissolve
    tana "Hmmmmmmmmmmmmmm..."
    hide tana_side_sad 
    hide kana_cry
    hide pia_sad
    hide tana_sad
    show takamina at takamina_center 
    show takamina_talk at takamina_center
    # show takamina_talk at left
    with dissolve
    "Takamina" "Ada apa nih, minna?"
    hide takamina_talk
    hide takamina_side_talk
    hide takamina 
    show pia_sad at pia_near
    show pia_side_sad at left
    with dissolve
    pia "Kita baru ngeh, gedung kampus kalo jam 6 sore dah dikunci."
    hide pia_sad 
    hide pia_side_sad
    show takamina at takamina_center 
    show takamina_talk at takamina_center
    show takamina_side_talk at left
    with dissolve
    "Takamina" "Terus? Terus?"
    hide takamina_talk
    hide takamina_side_talk
    hide takamina 
    show pia_silent at pia_near
    show pia_side_silent at left
    with dissolve 
    pia "Ya besok gimana latihannya bwaaang, telat dikit kekunci di rooftop weh."
    hide pia_silent 
    hide pia_side_silent
    show takamina at takamina_center 
    show takamina_talk at takamina_center
    show takamina_side_talk at left
    with dissolve
    "Takamina" "Ooooh gitu. Bentar ya."
    hide takamina_talk
    hide takamina_side_talk
    with dissolve
    "Takamina" "......."
    "Takamina terlihat sedang merogoh tasnya."
    show key
    show key:
        pos (0.69, 0.7) zoom 0.1 
    play sound "SFX - Key.mp3" volume (5.0)
    show takamina_talk at takamina_center
    show takamina_side_talk at left
    with dissolve
    "Takamina" "Taraaaaaaa~"
    hide takamina_talk
    hide takamina_side_talk
    hide takamina 
    hide key
    show key
    show key:
        xpos 0.47 ypos 0.72 zoom 0.2 
    show pia_side_talk at left
    with dissolve
    pia "Apa itu? Kunci kost kah?"
    hide pia_talk
    hide pia_side_talk
    hide key
    show takamina at takamina_center 
    show takamina_talk at takamina_center
    show takamina_side_talk at left
    with dissolve
    "Takamina" "Kunci pintu rooftop sama kunci pintu utama gedung DKV."
    hide takamina_talk
    hide takamina_side_talk
    "Semua Orang" "HEEEEEEEEEEEEEEEEEEE??!!"
    hide takamina 
    show pia at pia_near 
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Kok bisa punya itu??????"
    pia "Nyolong dari mana???"
    hide pia_talk
    hide pia_side_talk
    hide pia 
    show takamina at takamina_center 
    show takamina_talk at takamina_center
    show takamina_side_talk at left
    with dissolve
    "Takamina" "Sembarangan, aku kan anggota BEM juga."
    "Takamina" "Biasanya kalo rapat atau drop barang ke dalem gedung, bisa sampe malem. Jadi, beberapa anggota BEM dikasih pegang duplikatnya hehe."
    hide takamina_talk
    hide takamina_side_talk
    hide takamina 
    show pia at pia_near 
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "AHHH INI DIAAAAAAAA!"
    hide pia_talk
    hide pia_side_talk
    hide pia 
    show takamina at takamina_center 
    show takamina_talk at takamina_center
    show takamina_side_talk at left
    with dissolve
    "Takamina" "Tapi aku ga bisa kasih ya, enak aja. Nanti takut disalahgunain."
    "Takamina" "Paling kalo mau sampe malem, kabarin aja. Nanti aku ikut juga, biar enak izinnya sama sekuriti."
    hide takamina_talk
    hide takamina_side_talk
    hide takamina 
    show kana at kana_near 
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Amaaaan. Ah mantap lah kalo begini."
    hide kana_talk
    hide kana_side_talk
    hide kana 
    show takamina at takamina_center 
    show takamina_talk at takamina_center
    show takamina_side_talk at left
    with dissolve
    "Takamina" "Hehehehe~"
    hide takamina_talk
    hide takamina_side_talk
    hide takamina 
    with dissolve
    "Hari itu berakhir di ruang club, di mana Pia mengajarkan desain ke Takamina agar tugasnya dapat dihandover selama Pia masih berlatih menjadi idol."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Rooftop Siang.ogg" fadein 1.0 volume 2.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya..."
    $ quick_menu = False
    scene rooftop with Dissolve(2.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname!c], Takamina, dan KTp sedang berkumpul di rooftop."
    show takamina at takamina_center 
    show takamina_talk at takamina_center
    show takamina_side_talk at left
    with dissolve
    "Takamina" "Ayooo~ Ayoo~ Kurang luwes Kana, ahaha."
    hide takamina_talk 
    hide takamina_side_talk
    with dissolve
    "[mcname!c]" "Tapi udah mulai sinkron ya, gerakannya mereka."
    show takamina_talk at takamina_center
    show takamina_side_talk at left
    with dissolve
    "Takamina" "Betuuul. Udah mulai kerasa kompaknya."
    "Takamina" "Cuma feelnya kayak ada yg kurang gitu ga sih."
    hide takamina_talk 
    hide takamina_side_talk
    with dissolve
    "[mcname!c]" "Apalah feel, gimana tuh maksudnya."
    show takamina_talk at takamina_center
    show takamina_side_talk at left
    with dissolve
    "Takamina" "Kayak kurang terbuka aja gitu."
    "Takamina" "Kayak mereka masih ngedance sendiri-sendiri, bukan sebagai grup gitu deh."
    hide takamina_talk
    hide takamina_side_talk
    with dissolve
    "[mcname!c]" "Pakar banget nih, berasa kayak ngobrol sama GM idol grup terkenal gitu."
    show takamina_talk at takamina_center
    show takamina_side_talk at left
    with dissolve
    "Takamina" "Apalah [mcname!c] ini, ahahaha."
    hide takamina_talk 
    hide takamina_side_talk
    hide takamina 
    with dissolve
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Rooftop Sore.ogg" fadein 1.0 volume 2.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Tak terasa waktu telah menjadi sore."
    $ quick_menu = False
    scene rooftop sore with Dissolve(2.0)
    $ renpy.block_rollback()
    show pia at pia_near 
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    $ quick_menu = True
    pia "Istirahat dulu, capeeek!"
    pia "[mcname!c], air dong~"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Nih, tangkep.\n*Melempar air ke Pia*"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Weits~\n*Menangkap air yang dilempar oleh [mcname!c]*."
    pia "Glek! Glek! Glek!"
    hide pia_talk
    show pia nyender rooftop
    show pia nyender rooftop:
        pos (0.55, -0.07) zoom 0.37 
    with dissolve
    pia "Huaaaaa! Capek juga ya..."
    hide pia_talk 
    hide pia_side_talk
    hide pia 
    show tana at tana_near 
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Tapi seru, kan?"
    hide tana_talk
    hide tana_side_talk
    hide tana 
    show pia at pia_near 
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Bangeeet! Btw makasih ya, Kana."
    pia "Udah semangat ngajakin aku..."
    hide pia_talk 
    hide pia_side_talk
    hide pia 
    show kana_confused at kana_near
    show kana_side_confused at left
    with dissolve
    kana "*Teler*"
    kana "Wweeeeeeeeeeeeeeh……"
    kana "Kok kalian masih ada tenaga ya."
    kana "Aku dah lemes banget, mau pulang aja. Showeran terus bobo."
    hide kana_confused
    hide kana_side_confused
    show pia at pia_near 
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Enak aja, banguuuun!"
    pia "Ayo latian lagi!"
    hide pia_talk 
    hide pia_side_talk
    hide pia 
    show kana_confused at kana_near
    show kana_side_confused at left
    with dissolve
    kana "AAAAA.. Tar dulu, baru berapa menit weh istirahatnya. Jahat kalian."
    hide kana_confused
    hide kana_side_confused
    with dissolve
    "Semua Orang" "Hahahahahahahaha."
    show pia at pia_near 
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Btw..."
    pia "Aku mau cerita."
    pia "Baru [mcname!c] yang denger sih..."
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Hah? Apa nih bawa bawa gue?"
    show pia_silent at pia_near
    show pia_side_silent at left
    with dissolve
    pia "Diem!!"
    hide pia_side_silent with dissolve
    "[mcname!c]" "Syappp!"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    hide pia_silent
    pia "Aku mau cerita kenapa aku mau banget jadi idol."
    hide pia_talk
    hide pia_side_talk
    hide pia 
    show takamina at takamina_center 
    show takamina_talk at takamina_center
    show takamina_side_talk at left
    with dissolve
    "Takamina" "Akh ini dia~"
    hide takamina_talk
    hide takamina_side_talk
    hide takamina 
    show pia at pia_near 
    show pia_talk at pia_near 
    show pia_side_talk at left
    with dissolve
    pia "Hehe."
    pia "Yah… Makasih loh, kayak aku selangkah lagi tampil di depan banyak orang."
    pia "Itu mimpi aku dari kecil. Aku suka ngedance, suka nyanyi, dan aku suka dilihat banyak orang."
    pia "Aku selalu nutupin ini karena gak percaya diri, takut gak cocok."
    pia "Tapi kalian dukung aku buat maju terus gitu."
    pia "Kan aku jadi terharu."
    pia "Kayak dream come true banget weh, hehehe~"
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    "{size=-10}Kana, Tana, Takamina{/size}" "Awwwwwwww~\n*Nyamperin pia sambil meluk*"    
    show pia:
        subpixel True 
        ypos -0.01 zoom 1.3 
        linear 0.60 ypos -0.55 zoom 2.6 
    with Pause(0.70)
    hide pia 
    show pia_shock at pia_near
    show pia_side_shock at left
    with dissolve
    pia "Ga usah! Lu ga usah!, \n{i}*nunjuk ke [mcname!c]*{/i}"
    hide pia_side_shock with dissolve
    "[mcname!c]" "Loh? Gue ga ngapa-ngapain padahal. Cih haha."
    hide pia_shock with dissolve
    "Semua Orang" "Hahahahahahahaha."
    "Hari itu bonding +1"
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "BGM_Kampus.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Tak terasa sudah H-1 event..."
    $ quick_menu = False
    scene depan kampus with Dissolve(2.0)
    $ renpy.block_rollback()
    show pia at pia_near with dissolve
    $ quick_menu = True
    "[mcname!c]" "Halo Piaa."
    show pia_shock at pia_near
    show pia_side_shock at left
    with dissolve
    pia "H-halo [mcname!c]!"
    hide pia_side_shock with dissolve
    "[mcname!c]" "Kamu deg-deg an ya?"
    show pia_side_shock at left with dissolve
    pia "LOH?! KOK TAU?"
    hide pia_side_shock with dissolve
    "[mcname!c]" "Yaampun, ga usah teriak juga kali."
    show pia_sad at pia_near
    show pia_side_sad at left
    with dissolve
    hide pia_shock
    pia "Ya maap..."
    "[mcname!c]" "Besok kamu perform, makanya deg-deg an kan?"
    pia "I-iya..."
    show pia_talk at pia_near
    show pia_side_talk at left
    hide pia_sad
    hide pia_side_sad
    with dissolve
    pia "Tapi semangatku lebih besar daripada ketakutanku!"
    hide pia_talk
    hide pia_side_talk
    hide pia_sad
    with dissolve
    "[mcname!c]" "Uoooh, nice!"
    show pia_talk at pia_near
    show pia_side_talk at left 
    with dissolve
    pia "Nanti sore aku akan latihan dengan super semangat!!!!!"
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Wuoh mantab."
    show pia_smile at pia_near
    show pia_side_smile at left
    with dissolve
    pia "Hehehehe~"
    hide pia_smile
    hide pia_side_smile
    with dissolve
    "[mcname!c]" "Oke deh, good luck hari ini!"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Okee, sampai ketemu nanti sore."
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Okeee."
    hide pia with dissolve
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Rooftop Sore.ogg" fadein 1.0 volume 2.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Sore itu..."
    $ quick_menu = False
    scene rooftop sore with Dissolve(2.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "Terlihat KTp sedang berlatih lebih giat."
    "Terlihat [mcname!c] dan Takamina duduk sambil menyemangati dan Feni yang membantu koreografinya."
    show feni at feni_center 
    show feni_talk at feni_center 
    show feni_side_talk at left
    with dissolve
    feni "Nice! Nice! Pia, agak digoyang dikit pinggulnya."
    hide feni_talk
    hide feni_side_talk
    hide feni 
    show pia at pia_near 
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Iya Teh!"
    hide pia_talk 
    hide pia_side_talk
    hide pia 
    show feni at feni_center 
    show feni_talk at feni_center
    show feni_side_talk at left 
    with dissolve
    feni "Good good!!"
    hide feni_talk
    hide feni_side_talk
    hide feni 
    with dissolve
    "Kemudian...."
    # Insert Chibi pia jatoh
    show pia_kepleset
    show pia_kepleset:
        pos (0.5, 0.88) zoom 0.32
    with Dissolve(1.0)
    pause(2.0)
    hide pia_kepleset
    show pia_kepleset_2
    show pia_kepleset_2:
        pos (0.5, 0.88) zoom 0.32
    with Dissolve(1.0)
    hide pia_kepleset_2 with Dissolve(2.0)
    stop music fadeout 1.0
    play sound "audio/tabrakan.mp3" volume (4.0)
    "Pia jatuh"
    "[mcname!c]" "*Reflek langsung bangun dari duduknya dan menghampiri Pia*"
    "[mcname!c]" "Pia!! Kamu gapapa?!"
    show pia_shock at pia_near
    show pia_side_shock at left
    with dissolve
    pia "Aman... G-gapapa kok..."
    hide pia_shock
    hide pia_side_shock
    show kana_cry at kana_near
    show kana_side_cry at left
    with dissolve
    kana "Nooo Pia!"
    hide kana_cry 
    hide kana_side_cry
    show feni_shock at feni_center
    show feni_side_shock at left
    with dissolve
    feni "Pia, kamu beneran gapapa kan?"
    hide feni_shock
    hide feni_side_shock
    show tana at tana_near 
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Sakit gak kakinya?"
    hide tana_talk 
    hide tana_side_talk
    hide tana 
    show pia_shock at pia_near
    show pia_side_shock at left
    with dissolve
    pia "A-aman kok!\n*Muka meringis kesakitan*"
    hide pia_shock 
    hide pia_side_shock
    with dissolve
    play music "audio/BGM_Rooftop Sore.ogg" fadein 1.0 volume 2.0
    show feni at feni_center 
    show feni_talk at feni_center
    show feni_side_talk at left
    with dissolve
    feni "Oke istirahat dulu ya, jangan diforsir."
    feni "Latihan stop sampe sini dulu, jangan lupa besok perform jam 7 ya."
    feni "Jaga kesehatan, pulang all!!!"
    hide feni_talk
    hide feni_side_talk
    hide feni 
    with dissolve
    "KTp" "Oke Tehh!!"
    "[mcname!c] tiba-tiba menghilang dari area rooftop."
    show pia at pia_near 
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Loh, [mcname!c] mana?"
    hide pia_talk 
    hide pia_side_talk
    hide pia 
    show takamina at takamina_center 
    show takamina_talk at takamina_center 
    show takamina_side_talk at left
    with dissolve
    "Takamina" "Tadi lari ke bawah, ga tau ngapain."
    hide takamina_talk 
    hide takamina_side_talk
    hide takamina
    with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    pause (1.0)
    scene rooftop sore with Dissolve(1.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname!c]" "*Datang dengan nafas terengah-engah*"
    "[mcname!c]" "P-piaaa….huft huft..."
    show pia at pia_near 
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "[mcname!c]? Kamu ke mana?"
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Ke bawah bentar.\n*Sambil menunjukan plastik berisi perban dan alat kompres memar*"
    "[mcname!c]" "Aku tau ini sakit kan? Jangan bohong.\n*Memencet kaki Pia*"
    show pia_sad at pia_near 
    show pia_side_sad at left 
    with dissolve
    pia "WOEEEEEEEEEEEEEEE!!!! SAKEEEEEEEEEEEEEEEEEEEEEEEEET!!!!!"
    hide pia_sad
    hide pia
    hide pia_side_sad
    with dissolve
    show kana_cry at kana_near_left_2
    show tana_sad at tana_right
    show kana_cry:
        subpixel True xpos 1.99 
    show tana_sad:
        subpixel True xpos -0.38 
    with dissolve
    "Kana & Tana" "*Muka cemas*"
    "Kana & Tana" "Pi…. Kamu gapapa nih? Besok perform."
    hide kana_cry
    hide tana_sad
    show pia at pia_near 
    show pia_talk at pia_near 
    show pia_side_talk at left
    with dissolve
    pia "Tenang aja, aman laaaah."
    hide pia_talk
    hide pia_side_talk
    hide pia 
    show takamina at takamina_center 
    show takamina_talk at takamina_center 
    show takamina_side_talk at left
    with dissolve
    "Takamina" "Kalo ada apa-apa, kasih tau loh."
    hide takamina_talk
    hide takamina_side_talk
    hide takamina
    with dissolve
    "[mcname!c]" "Dah, sini gue anterin balik.\n*Merangkul Pia*"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Oke, maap ya."
    show pia at pia_near
    hide pia_side_talk 
    with dissolve
    "[mcname!c]" "Aman aja, mau digendong apa gimana?"
    show pia_silent at pia_near
    show pia_side_silent at left 
    with dissolve
    pia "Apaan sih lebay."
    hide pia_side_silent with dissolve
    "[mcname!c]" "Yaudah sini deh gue rangkul aja, takut makin parah kalo jalan sendiri."
    show pia_shock at pia_near
    show pia_side_shock at left 
    with dissolve
    pia "O-oke……"
    hide pia_side_shock
    hide pia_shock
    hide pia_silent
    hide pia_talk
    hide pia
    with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kampus Sore.ogg" fadein 1.0
    scene kampus sore with Dissolve(1.0)
#HARUSNYA KAMPUS SORE
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname!c]" "Mana ya? Katanya udah deket."
    show pia at pia_near 
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Siapa?"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Cepio, tadi aku hubungi Cepio ngabarin kondisi kamu."
    hide pia with dissolve
    "Fiony yang sudah di depan gerbang dengan mobilnya sejak tadi, membuka jendela dan berteriak dari dalam mobil."
    show fio_side at left with dissolve 
    fio "CIEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE~"
    hide fio_side with dissolve
    show pia_dirangkul
    show pia_dirangkul:
        ypos 0.99 zoom 0.29 
    with dissolve
    pia "CEPIOOOOOO~"
    hide pia_side_silent with dissolve
    "[mcname!c]" "Cepio, bantuin weh kasian ini."
    show fio_side at left with dissolve
    fio "Ahahaha. Oke oke wait, aku turun dulu."
    hide fio_side with dissolve
    menu:
        "Yang [mcname!c] lakukan..."
        "Ikut nemenin Pia ke kosan":
            hide pia_dirangkul with dissolve
            jump goodendpiakosan
        "[mcname!c] pun menyerahkan semuanya ke Cepio":
            hide pia_dirangkul 
            show pia at pia_near
            show pia_silent at pia_near
            show pia_side_silent at left
            with dissolve
            $ renpy.block_rollback()
            $ quick_menu = True
            "[mcname!c]" "Cepio, aku tinggal Pia ke Cepio ya. aku ga bisa ikut"
            hide pia
            hide pia_silent
            hide pia_side_silent
            show pia at pia_near_right
            show pia_silent at pia_near_right
            show fio at char_near_left
            show fio_talk at char_near_left
            show fio_side at left
            with dissolve
            fio "Loh kamu gak ikut nemenin Pia dulu?"
            hide fio_talk
            hide fio_side
            with dissolve
            "[mcname!c]" "Umm… kayaknya ga bisa Cepio, ada yang mau aku urus dulu."
            show fio_talk at char_near_left
            show fio_side at left
            with dissolve
            fio "Oh Oke"
            hide fio_talk
            hide fio_side
            show pia_side_silent at left 
            with dissolve
            pia "Oh gitu, ada yang lebih penting dari aku ya hump…."
            pia "Yaudah Cepio gas jalan, [mcname!c] gak mau ikut, sibuk"
            hide pia_side_silent with dissolve
            hide pia_silent
            hide pia
            hide fio
            with dissolve
            "Fiony dan Pia pun pergi tanpa [mcname!c] saat itu."
            "[mcname!c] memutuskan untuk kembali ke rooftop dan mengecek apakah ada yang tertinggal di atas."
            $ quick_menu = False
            stop music fadeout 1.0
            scene black with Dissolve(1.0)
            play music "BGM_Bad End.ogg" fadein 1.0
            scene rooftop malam with Dissolve(1.0)
            "Dalam perjalanan ke rooftop, [mcname!c] yang kelelahan karena sebelumnya harus naik turun tangga menuju rooftop pun mulai kehilangan keseimbangan."
            "[mcname!c] terjatuh di tangga saat menuju ke rooftop tanpa ada seorangpun yang melihatnya saat itu."
            "[mcname!c] pun terjatuh dan mengalami pendarahan di kepala."
            "Dikarenakan tidak ada yang membantu menolongnya saat itu, [mcname!c] pun meninggal karena kehabisan darah."
            $ quick_menu = False
            scene black with dissolve
            show text "{color=#FF0000}BAD END{/color}" with Pause(2.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits

label goodendpiakosan:
    $ renpy.block_rollback()
    $ quick_menu = True
    hide pia_silent with dissolve
    "[mcname!c] yang ditemani Fiony pun akhirnya mengantar Pia kembali ke kosan."
    hide pia with dissolve
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 2.ogg" fadein 1.0
    scene awan malam with Dissolve(1.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname!c] mengantar Pia sampai ke depan pintu kamarnya. Selanjutnya Pia ditemani Cepio."
    "[mcname!c]" "Yaudah aku pulang dulu ya, Pia. Jaga diri, sehat-sehat, banyak istirahat."
    show fio_side at left with dissolve
    fio "Aman, aku nginep di sini, aku bakal jagain dia. Besok langsung ketemuan di venue aja apa gimana?"
    hide fio_side with dissolve
    "[mcname!c]" "Di ruang club dulu aja kali ya Ce?"
    show fio_side at left with dissolve
    fio "Oke aman, besok aku bareng Pia ke sana."
    hide fio_side 
    show pia_side_talk at left 
    with dissolve
    pia "Makasih ya [mcname!c], udah bantuin... See you besooook~"
    hide pia_side_talk with dissolve
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" fadein 1.0 volume (0.8)
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Di kost..."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(1.0)
    $ quick_menu = True
    "[mcname!c]" "{i}Hmmm Pia gimana ya...{/i}"
    "[mcname!c]" "{i}Masih sakit kah?{/i}"
    "[mcname!c]" "{i}Chat aja kali ya?{/i}"
    stop music fadeout 1.0
    nvl clear
    play music "BGM_Happy + HP.ogg" fadein 1.0 volume (2.0)
    $ quick_menu = False
    mc_nvl "Dah Turu?"
    pia_nvl "Beloooom"
    mc_nvl "Weh ngapain aja? Kok belom? Tar kecapean weh."
    pia_nvl "Lah, kamu ngapain ngechat aku?"
    mc_nvl "...."
    mc_nvl "Ngecek aja"
    pia_nvl "Awwww"
    fio_nvl "Cieee"
    mc_nvl "Lohh????"
    $ renpy.block_rollback()
    nvl clear
    stop music fadeout 1.0
    play music "audio/BGM_Kosan 1.ogg" fadein 1.0 volume (0.8)
    scene kamar mc kota with dissolve
    $ quick_menu = True
    "[mcname!c]" "Dah lah, tidur aja."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_UKM.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Hari Matsuri pun tiba."
    $ quick_menu = False
    $ renpy.block_rollback()
    scene ruang ukm with Dissolve(2.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname!c]" "Duh Pia sama Cepio mana ini? Belum dateng."
    show kana at kana_near_left_2
    show tana at tana_right
    show kana:
        subpixel True xpos 1.99 
    show tana:
        subpixel True xpos -0.38
    with dissolve
    "Kana & Tana" "Gimana [mcname!c]? Aman?"
    "[mcname!c]" "Belom bales. Lagi di jalan kali?"
    hide kana
    hide tana
    show pia at pia_near 
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "HOIIIIIIIII!!\n*Memanggil dari kejauhan*"
    hide pia_talk
    hide pia_side_talk
    hide pia
    with dissolve
    "Semua Orang" "*Lari menghampiri Pia dan Cepio*"
    show feni at feni_center 
    show feni_talk at feni_center 
    show feni_side_talk at left 
    with dissolve
    feni "Kaki gimana?"
    hide feni_talk
    hide feni_side_talk
    hide feni 
    show pia at pia_near 
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Aman Teh Mpen! Hehehe~"
    hide pia_talk
    hide pia_side_talk
    hide pia 
    show feni at feni_center 
    show feni_talk at feni_center 
    show feni_side_talk at left
    with dissolve
    feni "Fiuh. Syukurlah. Yaudah sok atuh masuk dulu, ke acaranya bareng aja nanti."
    feni "Jam berapa sekarang?"
    hide feni_talk
    hide feni_side_talk
    hide feni 
    show kana at kana_near 
    show kana_talk at kana_near 
    show kana_side_talk at left 
    with dissolve
    kana "Jam 8, Teh."
    hide kana_talk 
    hide kana_side_talk
    hide kana 
    show feni at feni_center 
    show feni_talk at feni_center
    show feni_side_talk at left
    with dissolve
    feni "Aman lah, eventnya baru buka jam 10."
    feni "Free time ya sampe jam 3an. Jangan grogi. Dibawa santai aja. Nikmatin dulu eventnya ya."
    feni "Kalian perform jaaaam……."
    menu:
        feni "Kalian perform jaaaam……."
        "Jam 7 malem teh":
            jump goodendpiamatsuri
        "Jam 8 malem teh":
            $ renpy.block_rollback()
            hide feni_talk
            hide feni_side_talk
            with dissolve 
            $ quick_menu = False
            stop music fadeout 1.0
            "[mcname!c]" "Jam 8 malem teh."
            play music "BGM_Bad End.ogg" fadein 1.0
            scene black with dissolve
            show text "{color=#FFF}TERNYATA [mcname!c] SALAH MELIHAT JADWAL{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FFF}KALIAN KEASIKAN JALAN DAN MELEWATI JADWAL TAMPIL{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FFF}KTP PUN DIANGGAP TIDAK TAMPIL DALAM PERTUNJUKAN{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FFF}SETELAH PROSES PANJANG INI KALIAN KELEWAT TAMPIL?????{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FFF}YANG BENER AJA BRO BRO{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FF0000}BAD END{/color}" with Pause(2.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits

label goodendpiamatsuri:
    $ renpy.block_rollback()
    hide feni_talk
    hide feni_side_talk
    with dissolve
    $ quick_menu = True
    "[mcname!c]" "Jam 7 malem teh"
    show feni_talk at feni_center
    show feni_side_talk at left
    with dissolve
    feni "Oh iya."
    feni "Oke sana masuk ruangan dulu. Istirahat, jangan terlalu capek."
    hide feni_talk
    hide feni_side_talk
    hide feni 
    with dissolve
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "BGM_Monas.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Beberapa saat kemudian, acara Matsuri pun resmi dimulai"
    $ quick_menu = False
    scene matsuri siang with Dissolve(2.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname!c]" "Let’s go, otw kita!"
    "Semua Orang" "Ikuzoooo~"
    "Mereka pun pergi bersama ke event jejepangan tersebut."
    show pia_idol at pia_near 
    show pia_idol_talk at pia_near
    show pia_idol_side_talk at left
    with dissolve
    pia "Weeeh dah rame, yaaaa~"
    hide pia_idol_talk
    hide pia_idol_side_talk
    with dissolve
    "[mcname!c]" "*Melirik ke kaki pia*"
    show pia_idol_talk at pia_near
    show pia_idol_side_talk at left
    with dissolve
    pia "Kenapa?"
    hide pia_idol_talk
    hide pia_idol_side_talk
    with dissolve
    "[mcname!c]" "Yakin udah baikan?"
    "[mcname!c]" "Kok jalannya kayak agak diseret gitu?"
    show pia_idol_talk at pia_near
    show pia_idol_side_talk at left
    with dissolve
    pia "Engga kok, gapapa nih!\n*Menghentak hentakan kaki*"
    pia "Hiiiingghh…\n*Pia syok menahan sakit*"
    hide pia_idol_talk
    hide pia_idol_side_talk
    with dissolve
    "[mcname!c]" "Kaaaaaaaaaan..."
    show pia_idol_talk at pia_near
    show pia_idol_side_talk at left
    with dissolve
    pia "Sssstt…. Jangan bilang yang lain plis plisssss."
    pia "Aku masih bisa kok."
    pia "Aku ga mau performnya gagal karena aku."
    pia "Plisss, ya ya ya."
    hide pia_idol_talk 
    hide pia_idol_side_talk
    with dissolve
    "[mcname!c]" "........."
    show pia_idol_talk at pia_near
    show pia_idol_side_talk at left
    with dissolve
    pia "Gak begitu sakit kok, aku ga mau bikin yang lain kepikiran."
    pia "Plis, aku mau hari ini sukses. Ya?"
    hide pia_idol_talk
    hide pia_idol_side_talk
    with dissolve
    "[mcname!c]" "Oke, tapi please next jujur ya Pi. Aku khawatir loh, aku tau kamu gimana."
    "[mcname!c]" "Aku tau kalo kamu lagi bohong."
    show pia_idol_talk at pia_near
    show pia_idol_side_talk at left
    with dissolve
    pia "Hehehe maaf..."
    hide pia_idol_talk
    hide pia_idol_side_talk
    hide pia_idol 
    show tana_idol at tana_near 
    show tana_idol_talk at tana_near
    show tana_idol_side_talk at left
    with dissolve
    tana "Brooooo!! Itu tako Nakohayou yang terkenal itu bro. Let’s go antri itu."
    tana "Di mall ngantrinya panjang kalo mau beli itu, loh."
    hide tana_idol_talk 
    hide tana_idol_side_talk
    hide tana_idol 
    show kana_idol at kana_near 
    show kana_idol_talk at kana_near 
    show kana_idol_side_talk at left
    with dissolve
    kana "Oh tako Nakohayou, aku pernah coba. Iya sih enak, ayok"
    hide kana_idol_talk 
    hide kana_idol_side_talk
    hide kana_idol 
    show takamina at takamina_center 
    show takamina_talk at takamina_center
    show takamina_side_talk at left
    with dissolve
    "Takamina" "Aku kayaknya mau ke yakisoba Rin sama Teh Mpen, deh."
    hide takamina_talk
    hide takamina_side_talk
    hide takamina 
    show feni at feni_center 
    show feni_talk at feni_center
    show feni_side_talk at left
    with dissolve
    feni "Aku udah ngidam yakisoba Rin dari semalem."
    feni "Yang mau aku beli pertama pas ke sini, tuh! Let’s go lah yuk."
    hide feni_talk 
    hide feni_side_talk
    hide feni 
    with dissolve
    "[mcname!c]" "Okeh, kita misah deh ya."
    show fio at fio_near 
    show fio_talk at fio_near
    show fio_side_talk at left
    with dissolve
    fio "Aku juga misah deh ya, mau ke section kreator."
    fio "Temen aku jualan di sana."
    hide fio_talk 
    hide fio_side_talk
    with dissolve
    "[mcname!c]" "Oke Cepio."
    show fio_talk at fio_near
    show fio_side_talk at left
    with dissolve
    fio "{size=-5}Ga mau gangguin [mcname!c] ngedate.{/size}\n*Berbisik*"
    hide fio_talk
    hide fio_side_talk
    hide fio_side_talk
    with dissolve
    "[mcname!c]" "WEEEEEEEEEH!"
    hide fio 
    show pia_idol at pia_near 
    show pia_idol_shock at pia_near
    show pia_idol_side_shock at left
    with dissolve
    pia "?"
    hide pia_idol_shock 
    hide pia_idol_side_shock
    hide pia_idol 
    with dissolve
    $ quick_menu = False
    scene black with Dissolve(0.5)
    scene awan with Dissolve(1.5)
    $ quick_menu = True
    "[mcname!c]" "A-ayo Pi, muter-muter. Liat-liat booth."
    show pia_idol at pia_near 
    show pia_idol_talk at pia_near 
    show pia_idol_side_talk at left
    with dissolve
    pia "Ayooooo~"
    hide pia_idol_talk 
    hide pia_idol_side_talk
    hide pia_idol 
    with dissolve
    "[mcname!c] pun mengajak Pia berkeliling di acara jejepangan tersebut sambil mengecek booth dan guest star lain di panggung."
    $ quick_menu = False
    scene black with Dissolve(0.5)
    scene awan with Dissolve(1.5)
    $ quick_menu = True
    stop music fadeout 1.0
    "Tak terasa berjam jam telah berlalu."
    play music "BGM_Happy + HP.ogg" fadein 1.0 volume (2.0)
    $ quick_menu = False
    nvl clear
    feni_nvl "Guys, kumpul di club jam 3 ya"
    kana_nvl "Oke teteh"
    tana_nvl "Sippp"
    pia_nvl "Oke teh"
    mc_nvl "Oke"
    nvl clear
    $ renpy.block_rollback()
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "BGM_UKM.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Di ruang UKM..."
    $ quick_menu = False
    scene ruang ukm sore with Dissolve(2.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname!c]" "Grogi ya?"
    "[mcname!c]" "Semangat semua!"
    show kana_idol_cry at KTP_Kana
    show pia_idol_sad at KTP_Pia
    show tana_idol_sad at KTP_Tana
    with dissolve
    "KTp" "Huhuhu~\n*Muka cemas*"
    show pia_idol_side_sad at left with dissolve
    pia "Udah mulai kerasa deg-deg an, weh."
    hide pia_idol_side_sad with dissolve
    "[mcname!c]" "Bisa bisa!!! Hehe."
    show pia_idol_talk at KTP_Pia
    show pia_idol_side_talk at left
    with dissolve
    pia "Maaci~"
    hide pia_idol_talk 
    hide pia_idol_side_talk
    hide pia_idol
    with dissolve
    "Mereka pun mulai persiapan antri ke backstage."
    hide pia_idol_sad 
    hide kana_idol_cry
    hide tana_idol_sad
    with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Matsuri Malam.ogg" fadein (1.0)
    scene stage with Dissolve(1.0)
    $ quick_menu = True
    "[mcname!c] menunggu di depan stage bersama Feni, Freya, Fiony, dan Takamina."
    "[mcname!c]" "Huhuhu, jadi aku yang deg-degan juga."
    show fio at fio_near 
    show fio_talk at fio_near 
    show fio_side_talk at left
    with dissolve
    fio "Ahaha iya, aku juga."
    fio "Pokoknya semangatin mereka, ya!"
    hide fio_talk 
    hide fio_side_talk
    with dissolve
    "[mcname!c]" "Oh jelaaaas~"
    hide fio with dissolve
    "Announcer" "Ooooy, minna-saaaan! Gimana, seruuuuu?????"
    play sound "SFX - Cheering.ogg" fadein 0.5
    "Penonton" "SERUUUUUUUUUUU!!!!!!"
    stop sound fadeout 1.5
    "Announcer" "Selanjutnya, ada siapa yaaaa?"
    "Announcer" "Ada yang bisa tebaaak??"
    "Announcer" "Kita sambut, idol yang mengawali debutnya hari ini."
    "Announcer" "KTp!!!!!!"
    play sound "SFX - Cheering.ogg" fadein 0.5
    "Penonton" "UWOOOOOOOOOGGGGH!"
    "KTp masuk ke stage"
    stop sound fadeout 1.5
    "Membawakan lagu pertama"
    show pia_sakit_stage
    show pia_sakit_stage:
        xpos 0.53 zoom 0.39 ypos 0.89 
    with Dissolve(1.0)
    pause(2.0)
    hide pia_sakit_stage
    show pia_sakit_stage_2
    show pia_sakit_stage_2:
        xpos 0.53 zoom 0.39 ypos 0.89 
    with Dissolve(1.0)
    hide pia_sakit_stage_2 with Dissolve(4.0)
    "[mcname!c]" "*Melihat raut wajah Pia*"
    "[mcname!c]" "{i}Masih sakit yaaa..{/i}"
    show fio at fio_near 
    show fio_talk at fio_near 
    show fio_side_talk at left 
    with dissolve
    fio "Kasian Pia, kayaknya masih sakit ya kakinya."
    hide fio_talk 
    hide fio_side_talk
    with dissolve
    "[mcname!c]" "Iya Ce, cuma liat deh. Pia semangat banget dan berusaha ga nunjukkin sakitnya."
    "[mcname!c]" "Aku terharu banget liatnya."
    hide fio with dissolve
    "{size=-10}Fiony, Freya, Takamina{/size}" "*Bombastic side eye*"
    "[mcname!c]" "Eh? A-apa?"
    show fio at fio_near 
    show fio_talk at fio_near
    show fio_side_talk at left
    with dissolve
    fio "Gapapa~"
    hide fio_side_talk at left
    show fio_smile_talk at fio_near
    show fio_side_smile at left
    with dissolve
    fio "Hihihi!"
    hide fio_side_smile 
    hide fio_smile_talk
    with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene stage with Dissolve(1.0)
    play sound "SFX - Cheering.ogg" fadein 0.5
    $ renpy.block_rollback()
    show tana_idol_side_talk at left with dissolve
    $ quick_menu = True
    tana "Gimana semua, seru gak?"
    hide tana_idol_side_talk with dissolve
    "Penonton" "SERUUUUUUUUUUUUU!!!!"
    show kana_idol_side_talk at left with dissolve
    stop sound fadeout 1.5
    kana "Tadi kami membawakan lagu Punkish!"
    kana "Sebelum lanjut ke lagu yang selanjutnya, udah pada kenal kita belom nih?"
    hide kana_idol_side_talk with dissolve
    "Penonton" "Beluuuuuuuum~"
    show pia_idol_side_talk at left with dissolve
    pia "Wah, kayaknya belom pada kenal nih. Kita kenalan dulu aja ga sih?"
    pia "Bisa dimulai dari yang sebelah kiri~"
    hide pia_idol_side_talk 
    show tana_idol_side_talk at left 
    with dissolve
    tana "Wassup ma bross!! I'm fresh like a breeze KTp Tana Nona Cool enough to make you freeEeEzZEeE Halo semuanya aku Tana Nona dari KTp!"
    hide tana_idol_side_talk 
    show kana_idol_side_talk at left 
    with dissolve
    kana "Mari bernyanyi, sambil bermain air. Aku dari laut tapi tidak salty!"
    kana "Halo! Aku Kanaia yang akan membuat harimu indah bagai pelangi~"
    hide kana_idol_side_talk 
    show pia_idol_side_talk at left 
    with dissolve
    pia "WE ARE ON FIRE!"
    pia "SEMANGATKU MEMBARA, SIAP MENGHANGATKAN HARI-HARI MU!!"
    pia "HALO AKU PIA MERALEO DARI KTp~"
    play sound "SFX - Large Cheering.mp3" loop fadein 1.0
    pia "SALAM KENAL SEMUAAAAAAAAAA!!!"
    hide pia_idol_side_talk with dissolve
    "[mcname!c]" "Whoaaa..."
    menu:
        "[mcname!c]" "Whoaaa..."
        "Fokus Menyimak":
            $ renpy.block_rollback()
            stop sound fadeout 1.5
            $ quick_menu = False
            stop music fadeout 1.0
            play music "BGM_Bad End.ogg" fadein 1.0
            "[mcname!c] terlalu fokus wotagei dan tidak memperdulikan lagi Pia yang saat itu sedang menahan kesakitan."
            "Pada pertunjukan lagu terakhir, Pia pun terjatuh di stage di depan banyak orang. Tidak sedikit yang menyoraki dan menertawakan moment tersebut."
            "Namun [mcname!c] tidak melihat hal tersebut karena sedang asik wotagei."
            "Fiony ingin memberitahu [mcname!c] yang saat itu ada di sebelahnya namun terpukul lightstick yang sedang diayunkan [mcname!c]."
            "Ketika [mcname!c] sudah tersadar dan kembali ke realita, semua sudah terlambat."
            "[mcname!c] melihat Fiony yang sedang duduk sambil mengusap kepalanya yang berdarah akibat benturan lightstick [mcname!c]."
            "Saat [mcname!c] melihat ke depan, terlihat Pia yang sambil menangis tersungkur jatuh di stage. Lagu pun dihentikan."
            "Pertunjukan hari itu pun selesai."
            "Beberapa hari kemudian, Pia lebih memilih mengurung diri dan tidak banyak interaksi dengan [mcname!c]."
            scene black with dissolve
            show text "{color=#FFF}DI KOSAN PIA{/color}" with Pause(2.0)
            scene kamar pia with dissolve
            $ renpy.block_rollback()
            show pia_side_talk at left with dissolve
            pia "Udah cukup, aku malu. Menjadi idol emang pilihan yang salah. Aku gak mau lagi."
            hide pia_side_talk with dissolve
            nvl clear
            mc_pov_nvl "Piaaaa!"
            mc_pov_nvl "P"
            mc_pov_nvl "P"
            mc_pov_nvl "P"
            mc_pov_nvl "P"
            mc_pov_nvl "Di mana? Gak mau latihan lagi?"
            nvl clear
            $ renpy.block_rollback()
            "Pia memutuskan untuk block [mcname!c] yang tidak peka itu dan mulai menjauhinya."
            "Setelah itu, Pia memutuskan keluar dari club jepang dan tidak beraktivitas menjadi idol lagi."
            scene black with dissolve
            show text "{color=#FF0000}BAD END{/color}" with Pause(2.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits
        "Teriak Menyemangati":
            jump goodendpia

label goodendpia:
    $ renpy.block_rollback()
    stop music fadeout 1.0
    $ quick_menu = True
    stop sound fadeout 3.0
    "[mcname!c]" "PIAAAAAAAAAAAAAAAAAAAAAAA KAMULAH OSHIKU SATU SATUNYAAAAAAAA!!"
    "Semua penonton pun menoleh ke arah [mcname!c] yang dengan lantang mengucapkan kalimat tersebut dengan raut wajah yang terlihat serius sambil menunjukan jari telunjuknya ke arah Pia dengan penuh semangat."
    show fio_talk at fio_near
    show fio_side_talk at left 
    with dissolve
    fio "Yeeeeeeeee~!\n*Ikut menyoraki dengan suara kecilnya*"
    hide fio_side_talk 
    hide fio_talk
    with dissolve
    play sound "SFX - Large Cheering.mp3" loop fadein 0.5
    "Penonton" "UWOOOOOOGGGHH!!!!!!!!! PIAAAAAAAAAAAA!!!"
    "Tidak disangka, teriakan [mcname!c] menyulut semangat penonton lain untuk ikut menyoraki dan menunjukan dukungannya lebih keras lagi."
    "Teriakan tersebutlah yang membuat pengunjung lain yang sedang berkeliling di acara tersebut jadi penasaran dan ikut menonton pertunjukan di stage tersebut."
    show pia_idol_side_talk at left with dissolve 
    pia "*Blushing*"
    pia "A-ah iyaaa makasih~"
    pia "Dengarkanlah lagu terakhir dari kami, Dreamcatcher."
    hide pia_idol_side_talk with dissolve
    "[mcname!c]" "PIAAAAAAAAAAAAA!!!! SEMANGAAAAAAAAAAT!"
    stop sound fadeout 1.5
    scene konser end with Dissolve(1.0)
    play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
    $ quick_menu = False
    scene black with dissolve
    scene konser stage end with dissolve
    $ rock_idol.grant()
    show text "{color=#FFF}THE END{/color}" with Pause(2.0)
    with Pause(20.0)
    jump credits