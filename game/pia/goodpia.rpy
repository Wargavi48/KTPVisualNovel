label goodpia:
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}MALAM HARINYA{/color}" with Pause(2.0)
    scene mc bedroom with dissolve
    play music "audio/BGM_Kosan 2.mp3" fadein 1.0
    "[mcname] pulang, duduk di meja belajarnya sambil mulai mengeluarkan buku-buku dan catatan materi ujian esok hari."
    "[mcname] bersiap begadang untuk fokus belajar karena besok adalah salah satu ujian mata kuliah tertulis yang paling sulit."
    "Tiba tiba terdengar notifikasi dari handphone [mcname]."
    play sound "audio/ReceiveText.ogg"
    mcname "...."
    play sound "audio/ReceiveText.ogg"
    mcname "...."
    play sound "audio/ReceiveText.ogg"
    mcname "{i}Apaan sihh{/i}"
    stop music fadeout 1.0
    play music "audio/BGM_Happy dan Handphone.mp3" fadein 1.0
    nvl clear
    pia_nvl "[mcname]!!!!"
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
    stop music fadeout 1.0
    "[mcname] pun bersiap siap untuk pergi ke cafe"
    scene black with dissolve
    play sound "audio/cafe-entrance.mp3" fadein 1.0
    show text "{color=#FFF}BEBERAPA MENIT KEMUDIAN{/color}" with Pause(2.0)
    show text "{color=#FFF}DI KAFE{/color}" with Pause(2.0)
    play music "audio/BGM_Cafe Sore.mp3" fadein 1.0
    scene cafe with dissolve
    $ renpy.block_rollback()
    show pia at char_placement with dissolve
    show pia_side at left with dissolve
    $ quick_menu = True
    pia "[mcname] Sini!!"
    hide pia_side with dissolve
    hide pia with dissolve
    show pia at pia_near with dissolve
    mcname "Hadeeeeeh, nih bukunya"
    show pia_side at left with dissolve
    pia "MAKASIH BANGET!!! HUHUHU"
    pia "KALO GAK ADA KAMU, AKU GATAU HARUS GIMANA. AKU GAMAU NGULANG MATKUL INI"
    hide pia_side with dissolve
    mcname "Iya Pia, Iya"
    show pia_side at left with dissolve
    pia "Aku berhutang budi sama kamu!!!"
    hide pia_side with dissolve
    mcname "Halah lebay"
    show pia_side at left with dissolve
    pia "Karena kamu baik, aku kasih kamu 1 golden tiket ini. Muahahaha"
    # Insert aset tiket
    hide pia_side with dissolve
    mcname "Apaan ini?"
    show pia_side at left with dissolve
    pia "Pake ini buat mengabulkan 1 permintaan."
    pia "Apapun, akan kulakukan!"
    hide pia_side with dissolve
    mcname "Oke, aku pake sekarang. Sekarang kamu ke depan cafe ini, tereak \"Aku belom mandi seminggu dan aku bangga\". now!"
    show pia_side at left with dissolve
    pia "Ehh… jangan gitu dong."
    pia "Aaah [mcname] maaaah. Yang serius, ih."
    hide pia_side with dissolve
    mcname "Lah? Ini serius."
    show pia_side at left with dissolve
    pia "Gamau! weeeks"
    hide pia_side with dissolve
    mcname "Dih, yaudah. Kusimpen ya. Buat kapan-kapan"
    show pia_side at left with dissolve
    pia "Okeh! Saatnya belajar! Ayo!!"
    hide pia_side with dissolve
    "[mcname] dan Pia pun belajar bersama di cafe tersebut sampe larut malam [mcname] pun memutuskan meminjamkan buku tersebut ke Pia"
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with dissolve
    show text "{color=#FFF}KEESOKAN HARINYA{/color}" with Pause(2.0)
    play music "audio/BGM_MC Pertama Kali ke JKT + BG Pagi.mp3" fadein 1.0
    scene mc bedroom with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname] ngomong sendiri di kosan."
    mcname "Duhhh. Hari ini ujian tertulis paling susah. Deg deg an, huhu."
    $ quick_menu = False
    stop music fadeout 1.0
    scene kelas with dissolve
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    $ renpy.block_rollback()
    $ quick_menu = True
    "Suasana kelas sepi, semua sibuk belajar dan menghapal. ya, hari ini ujian tertulis mata kuliah xxx."
    show pia at pia_near with dissolve
    mcname "Pagi Mbak Pia"
    show pia_side at left with dissolve
    pia "Sssst, diem. Komposisi dan elemen dalam warna—\n*berbisik sambil menghapal"
    hide pia_side with dissolve
    mcname "Ahahahaha"
    hide pia with dissolve
    stop music fadeout 1.0
    #  Harusnya BG Ujian
    play music "audio/BGM_Dosen + Rektor.mp3" fadein 1.0
    show dosen at dosen_center with dissolve
    show dosen_side at left with dissolve
    dosen "Pagi!!"
    dosen "Semua buku dan HP simpan di depan ya."
    dosen "Di atas meja hanya boleh ada alat tulis"
    dosen "Ujian kita mulai 10 menit lagi."
    "Mahasiswa/i" "Baik buu~"
    $ quick_menu = False
    jump quiz

label goodpiaafterquiz:
    $ renpy.block_rollback()
    $ quick_menu = True
    "Selesai ujian, semua mahasiswa/i mengumpulkan lembar jawaban ke pengawas. Ujian hari itu berakhir."
    mcname "Hueeeee selesai juga ini ujian.\n*Liat kanan kiri*"
    show pia at pia_near with dissolve
    pia "...."
    mcname "Hahahaha gimana? Lancar? Bisa kan jawabnya?"
    show pia_side at left with dissolve
    pia "Bisa lah, yang bener aja! Cuma kayak ada yang kurang puas aja weh. Harusnya aku tambahin blablabla-"
    hide pia_side with dissolve
    mcname "Pia, sepanjang ujian tadi anak-anak lain cuma selembar doang terus dikumpulin, loh. Kamu sampe minta nambah lembar jawaban dua kali."
    mcname "DUA KALI!!"
    mcname "Lu ngisi apa bikin AU?"
    show pia_side at left with dissolve
    pia "Dih, aku tuh harus sempurna! Harus nilai 100!"
    hide pia_side with dissolve
    mcname "Kasian Bu Dosen yang meriksa jawaban kamu. Kayak baca novel, hahaha."
    show pia_side at left with dissolve
    pia "Iiiiih!!\n*Mukul - mukul [mcname]"
    hide pia_side with dissolve
    mcname "Ahahaha, eh hari ini mau ke mana? Pusing gak sih? Mau refreshing gak sih? Huhuhu~"
    show pia_side at left with dissolve
    pia "Rooftop yuk! Aku nunggu di sana, kamu ke kantin beli cemilan yang banyaaaaak! Nanti kita makan di rooftop."
    hide pia_side with dissolve
    mcname "Meeeh, gue yang beli nih?"
    show pia_side at left with dissolve
    pia "Yang buat aku pake uangku lah, nih. Aku tunggu di rooftop yaaa."
    hide pia_side with dissolve
    mcname "Bukan masalah uangnya... Tapi aku beli sendiri nih? Huhuhu kayak piaraan aja gue disuruh suruh. Bener-bener ya, Meameo."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    scene kantin with dissolve
    play music "audio/bgm_kantin.mp3" fadein 1.0
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname] pun ke kantin untuk beli beberapa cemilan untuk dibawa ke rooftop untuk makan bareng Pia."
    mcname "*Sambil bawa plastik berisi beberapa camilan*"
    mcname "Hmmm... apa lagi ya? Kayanya beli snack itu enak."
    show fio at char_placement with dissolve
    show fio_side at left with dissolve
    fio "[mcname]!!!!"
    hide fio_side with dissolve
    mcname "Woaaa kaget, Cepio hai~"
    show fio_side at left with dissolve
    fio "Sini!!!\n*Sambil menepuk nepuk kursi kosong sebelah Fiony*"
    hide fio_side with dissolve
    mcname "Halo Cepio~\n*Nyamperin*"
    hide fio with dissolve
    show kana at kana_near_left_2 with dissolve
    show freya at freya_near_right with dissolve
    show fio at fio_near with dissolve
    show fio_side at left with dissolve
    fio "Kenalin, ini Freya, kalo yang sebelahnya Kana."
    hide fio_side with dissolve
    mcname "Halo, namaku [mcname]. Salam kenal."
    show kana_side at left with dissolve
    kana "*Memicingkan mata sambil mengisyaratkan sesuatu*"
    kana "Ehm... Yang Mulia Piaraan?"
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
    mcname "Whaaat. Cepiooooo~"
    show fio_side at left with dissolve
    fio "Ahahaha, gini [mcname]. Ini Kana mau banget ketemu Pia. Dia suka banget gambarnya Pia."
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
    kana "Oh ah, enggak enggak. Nanti aku ajak Tono buat rekrut dia. Harus bisa pokoknya!"
    hide kana_side with dissolve
    "{size=-5}Freya & Fiony{/size}" "Semangat Naay~"
    mcname "Ahahaha nanti aku coba tanyain lagi deh ya, semoga berubah pikiran. Aku pergi dulu ya. Duluan semua~"
    "{size=-8}Freya, Fiony, Kana{/size}" "Iya, byeee~"
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with dissolve
    show text "{color=#FFF}Di Rooftop{/color}" with Pause(2.0)
    scene rooftop with dissolve
    play music "audio/BGM_Rooftop Romance Pia.mp3" fadein 1.0
    $ renpy.block_rollback()
    $ quick_menu = True
    "Pia sedang menari diiringi lagu idol di HPnya yang diputar agak keras"
    mcname "*Duduk bersila di belakang Pia*"
    "Pia menoleh ke belakang."
    show pia at pia_near with dissolve
    show pia_side at left with dissolve
    pia "Hueeeh kaget!! Udah di sini aja, diem-diem gak ada suara! Bikin jantungan aja."
    hide pia_side with dissolve
    mcname "Mana ada? Kamu aja yang terlalu serius sampe gak perhatiin sekitar, haha."
    show pia_side at left with dissolve
    pia "Hehehe~\n*Ikut duduk bersila sebelah [mcname]*"
    hide pia_side at left with dissolve
    stop music fadeout 1.0
    play music "audio/BGM_Funny Slow Cute.mp3" fadein 1.0
    mcname "Yang Mulia Piaraan."
    "*Pia menyembur minumannya*"
    show pia_side at left with dissolve
    pia "Uhuk uhuk!!! Hoooeeek guuuh!! Uhuk!!!"
    pia "KOK KAMU TAU PEN NAME AKU, TAU DARI MANA?"
    hide pia_side with dissolve
    mcname "Jadi itu beneran kamu? Ahahaha."
    show pia_side at left with dissolve
    pia "Eh tau dari mana????"
    hide pia_side with dissolve
    mcname "Tadi di kantin aku ketemu fans kamu. Dia nyariin kamu bareng Cepio tuh."
    show pia_side at left with dissolve
    pia "Heeeeee~"
    hide pia_side with dissolve
    mcname "Tapi itu nama apa, dah?"
    show pia_side at left with dissolve
    pia "Ahahaha itu pen name aku kalo gambar. Aku sering gambar gitu kan, terus diupload di medsos. Nah nama akun gambar aku tuh, Yang Mulia Piaraan."
    hide pia_side with dissolve
    mcname "Owalah gitu toh."
    show pia_side at left with dissolve
    pia "Aku gak nyangka aja ada yg kenal nama itu dan tau. Aku gak nyembunyiin, sih. Cuma malu aja pen name aku kayak gitu, haha."
    hide pia_side with dissolve
    mcname "Lah lagian. Kenapa Yang Mulia Piaraan, dah?"
    show pia_side at left with dissolve
    pia "Ya maap sih, dulu masih wibu wibunya asal ngasih nama. Eh taunya udah nyaman, hahaha."
    pia "Jadi dulu tuh aku suka gambar fanart anime, manga, gitu-gitu. Terus ada beberapa yang aku jual juga di online jadi merch. Mungkin orang itu salah satu yang beli."
    hide pia_side with dissolve
    mcname "Oooh gitu toh. Tadi sempet nanyain mau join club jepang, gak?"
    show pia_side at left with dissolve
    pia "Err… Engga deh. Aku mau lonewolf. Udah gak terlalu jejepangan banget."
    hide pia_side with dissolve
    mcname "Hmmm.... gitu."
    show pia_side at left with dissolve
    pia "Emang kamu ngerti jejepangan?"
    hide pia_side with dissolve
    mcname "Beuh, perlu aku jelasin sinopsis 3 episode pertama setiap anime yang airing season ini gak nih?"
    show pia_side at left with dissolve
    pia "IH WIBUUUU!!"
    hide pia_side with dissolve
    mcname "Ahahahahah."
    show pia_side at left with dissolve
    pia "Tapi bener deh, aku tuh gatau kenapa jadi agak kurang buat bersosialisasi gitu... Tapi di sisi lain, aku mau punya banyak temen dan kenal orang baru. Tapi males aja memulai."
    hide pia_side with dissolve
    mcname "Wakaru Pia, wakaru…"
    show pia_side at left with dissolve
    pia "Aaaah, jangan wibuuu :((("
    hide pia_side with dissolve
    mcname "Ahahaha becandaa~ Tapi bener deh, kamu gamau join? Kalo kamu join, aku juga deh. Gimana?"
    show pia_side at left with dissolve
    pia "Yeuuu, itu mah emang kamu aja kan yang mau."
    hide pia_side with dissolve
    mcname "Gak gituuuuu..."
    "[mcname] dan Pia pun banyak bercerita sambil menikmati cemilan di rooftop."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with dissolve
    show text "{color=#FFF}CHAPTER III{/color}" with Pause(2.0)
    play music "audio/Dreamcatcher.mp3" fadein 1.0
    jump credits