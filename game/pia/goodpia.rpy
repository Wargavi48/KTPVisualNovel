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
    scene ruang ukm with dissolve
    show kana at kana_near_left_2 with dissolve
    show tana at tana_right with dissolve
    show kana_side at left with dissolve
    kana "Ton! Kita harus rekrut Meameo join club jepang ini! Gambar dia bagus! Cocok jadi ilustrator club kita!"
    hide kana_side with dissolve
    show tana_side at left with dissolve
    tana "Itu siapa lagi, Nay? Nama dia Meameo? Aneh juga…"
    hide tana_side with dissolve
    show kana_side at left with dissolve
    kana "Duh aku lupa nama aslinya, tapi sedenger aku dari Kak Fiony nama dia Meameo"
    hide kana_side with dissolve
    show tana_side at left with dissolve
    tana "Err..oke\n*Siapa pula itu Fiony*"
    hide tana_side with dissolve
    show kana_side at left with dissolve
    kana "Dia anak DKV. Besok di gedung DKV ada pameran karya lagi, kita cari dia!"
    hide kana_side with dissolve
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}KEESOKAN HARINYA{/color}" with Pause(2.0)
    scene ruang ukm with dissolve
    show tana at tana_right with dissolve
    show kana at kana_near_left_2 with dissolve
    show tana_side at left with dissolve
    tana "Woaaaa bagus-bagus ya, gambarnya."
    hide tana_side with dissolve
    show kana_side at kana_near_left_2 with dissolve
    kana "Ton! Misi kita disini untuk rekrut Meameo"
    hide kana_side with dissolve
    show tana_side at left with dissolve
    tana "Iye bang. Kayak gimana tuh, orangnya?"
    hide tana_side with dissolve
    show kana_side at left with dissolve
    kana "......"
    kana "......."
    hide kana_side with dissolve
    show tana_side at left with dissolve
    tana "Nay?"
    hide tana_side with dissolve
    show kana_side at left with dissolve
    kana "Aku gak tau kayak gimana orangnya…"
    hide kana_side with dissolve
    show tana_side at left with dissolve
    tana "................"
    hide tana_side with dissolve
    $ quick_menu = False
    scene black with dissolve
    scene lorong with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    mcname "Wah rame banget yang liat-liat lukisan bulan ini"
    "[mcname] melihat ada 2 orang berlari menuju kearahnya"
    mcname "Waduh, lari ke gue gak sih, apa belakang gue? Belakang gue ga ada orang sih"
    "*[mcname] berjalan meminggir agar tidak menghalangi 2 orang tersebut*"
    mcname "Kayaknya fix lari ke gue"
    show kana at kana_near with dissolve
    show kana_side at left with dissovle
    kana "[mcname]! Nama kamu [mcname] kan?"
    hide kana_side with dissolve
    mcname "Ooh! Temennya cepio, iya, ada apa nih?"
    show kana_side at left with dissolve
    kana "Kamu kenal Meameo kan?"
    hide kana_side with Dissolve
    mcname "Pppffftt… Meameo"
    mcname "Iya kenal kok, tadi orangnya lagi selfie depan lukisannya. Mau ketemu?"
    show kana_side at left with dissolve
    $ tono_name = "Tana"
    kana "Iya! Oh kenalin, ini Tana"
    hide kana with dissolve
    show kana at kana_near_left_2 with dissolve
    show tana at tana_right with dissolve
    show tana_side at left with dissolve
    tana "Wazzup bro"
    hide tana_side with dissolve
    mcname "Y-yeah, wazzup……"
    hide kana with dissolve
    hide tana with dissolve
    "[mcname] pun membawa Kana Tana ke Pia yang sedang berfoto dengan lukisannya"
    mcname "Oi MEAMEO, ada yang mau ketemu kamu nih"
    show pia at pia_near with dissolve
    show pia_side at left with dissolve
    pia "Geeeeh apalah meameo"
    hide pia_side with dissolve
    hide pia with dissolve
    show kana at kana_near_left_2 with dissolve
    show tana at tana_right with dissolve
    show pia at pia_near with dissolve
    show kana_side at left with dissolve
    kana "Meameo!!!"
    kana "Join club jepang yuk!"
    hide kana_side with dissolve
    show pia_side at left with dissolve
    pia "Heeeeeeeee…"
    pia "Tunggu"
    pia "Pertama, nama aku Meraleo"
    pia "MERALEO"
    pia " Bukan Meameo"
    pia "Kedua, aku gamau masuk club jepang"
    pia "SIBUK!"
    pia "Ketiga"
    pia "Kalian siapa?"
    hide pia_side with dissolve
    show tana_side at left with dissolve
    tana "Naya, Naya…."
    tana "Minimal perkenalan dulu"
    tana "Halo Kak Meraleo, aku Tana, dia Kana."
    tana "Kita dari club jepang"
    tana "Nah, tujuan kita mau invite kamu ke club jepang nih"
    tana "Kita suka gambar kamu, siapa tau tertarik kan."
    hide tana_side with dissolve
    show pia_side at left with dissolve
    pia "Oh, panggil aku Pia aja."
    pia "Makasih undangannya, tapi kayaknya enggak dulu deh. Belum tertarik join club."
    hide pia_side with dissolve
    show kana_side at left with dissolve
    kana "Yaaah, oke deh. Belum tertarik kan. Bukan tidak tertarik!"
    kana "Oke. Besok aku akan cari kamu lagi buat join"
    hide kana_side with dissolve
    "*Kana pergi*"
    hide kana with dissolve
    show tana_side at left with dissolve
    tana "Lah udah nyerah ngomongnya gitu doang…"
    tana "Pergi dulu ya [mcname], Pia. Maap suka aneh emang Kana Kana itu"
    hide tana with dissolve
    "Beberapa kali pun setiap Pia bertemu Tana dan Kana, dia langsung diajak join club."
    "Namun jawaban Pia tetap sama, Pia menolak join club"
    $ quick_menu = False
    scene black with dissolve
    scene rooftop with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    "Pia dan [mcname] sedang beristirahat sehabis selesai matkul nirmana"
    mcname "Mau muntah aku ngerjain nirmana. Susaaaaah"
    show pia at pia_near with dissolve
    show pia_side at left with dissolve
    pia "Ahahahaha betuuuul"
    hide pia_side with dissolve
    mcname "BTW, kayaknya Si Kana Tana makin sering tuh ngajak kamu join haha."
    show pia_side at left with dissolve
    pia "Iya sih. Gigih banget ya."
    hide pia_side with dissolve
    mcname "Kamu ga mau coba dulu? Iseng aja gitu, mampir ato liat liat dulu ruang clubnya."
    show pia_side at left with dissolve
    pia "Jujur nih, sebenernya penasaran juga sih. Cuma ga ah!"
    hide pia_side with dissolve
    mcname "Ara ara, penasaran ya?\n*smug face*"
    show pia_side at left with dissolve
    pia "Heh apalah!"
    hide pia_side with dissolve
    mcname "Kan aku bilang, kamu join aku join. Gimana?"
    show pia_side at left with dissolve
    pia "*Menghembuskan nafas*"
    pia "Haaaaah….. okeh deal"
    hide pia_side with dissolve
    mcname "Lesgooooo"
    $ quick_menu = False
    scene black with dissolve
    scene ruang ukm with dissolve
    show kana_near_left_2 at left with dissolve
    show feni at feni_right with dissolve
    show kana_side at left with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    kana "Haaaah, pake strategi apa lagi ya buat ngajak Pia join ke sini?"
    hide kana_side with dissolve
    show feni_side at left with dissolve
    feni "Emang sekeren itu ya desainnya?"
    hide feni_side with dissolve
    show kana_side at left with dissolve
    kana "IYA KAK! SEKEREN ITU"
    hide kana_side with dissolve
    show tana_side at left with dissolve
    tana "Alah, bias aja itu mah Kak"
    hide tana_side with dissolve
    show kana_side at left with dissolve
    kana "Aaah Tono maaah\n*sad face*"
    hide kana_side with dissolve
    show feni_side at left with dissolve
    feni "Eeh udah udah jangan berantem ih."
    feni "Kalo emang gak mau ya, mau gimana atuh."
    hide feni_side with dissolve
    "*suara orang mengetuk pintu*"
    show feni_side at left with dissolve
    feni "Nay, bukain atuh pintunya. Kamu yang paling deket pintu"
    hide feni_side with dissolve
    show kana_side at left with dissolve
    kana "Iya kak\n*Nada lemes*"
    hide kana_side with dissolve
    play sound "audio/open_door" fadein 1.0
    mcname "Halo Kana"
    show kana_side at left with dissolve
    kana "Hah [mcname]??? Ngapain"
    hide kana_side with dissolve
    mcname "J-jadi gini…"
    "dari belakang [mcname], Pia menunjukan dirinya dengan malu malu"
    show pia_side at left with dissolve
    pia "Aloo~\n*malu malu*"
    hide pia_side with dissolve
    show kana_side at left with dissolve
    kana "YANG MULIA PIARAAN?????\n*Syok*"
    hide kana_side with dissolve
    show pia_side at left with dissolve
    pia "Woi -_-"
    hide pia_side with dissolve
    mcname "Jadi gini, kita mutusin untuk ikut join club jepang, masih buka kah?"
    show kana_side at left with dissolve
    kana "Masih!!! Masuuuuk"
    "Mereka semua pun masuk dan duduk bersama anggota lain"
    "Sambil berbincang dan perkenalan ke anggota lain"
    show feni_side at left with dissolve
    feni "Welcome, kita gak ada interview interview. Selamat join club jepang yaaa"
    hide feni_side with dissolve
    show kana_side at left with dissolve
    kana "HOREEEEEEE!!!"
    hide kana_side with dissolve
    show feni_side at left with dissolve
    feni "Aku ada kelas abis ini. Maaf ya ga bisa nemenin dan bantu jelasin. Kana nanti yang bantu, tolong ya Nay."
    hide feni_side with dissolve
    hide feni with dissolve
    show kana_side at left with dissolve
    kana "Siap Kak Feni!!"
    kana "Ehm, jadi gini. Di club ini ada banyak divisinya. Pia kita butuhin buat desain. Mau ya? Mau yaaa?"
    show pia_side at left with dissolve
    pia "Iya iya, aku coba ya."
    hide pia_side with dissolve
    show kana_side at left with dissolve
    kana "Terus selain itu kita ada divisi dance / idoling, budaya tradisional jepang, game, dan anime manga tokusatsu"
    hide kana_side with dissolve
    show pia_side at left with dissolve
    pia "Ehhh begitu, ya."
    hide pia_side with dissolve
    show kana_side at left with dissolve
    kana "Iyaaaa."
    hide kana_side with dissolve
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}BEBERAPA HARI KEMUDIAN{/color}" with Pause(2.0)
    scene ruang ukm with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True 
    "Pia mendapatkan tugas untuk membuat desain yang diperlukan untuk acara matsuri yang akan diselenggarakan club jejepangannya tersebut"
    "Di tengah pengerjaannya, samar-samar terdengar suara candaan anggota club di ruang sebelah"
    show feni_side at left with dissolve
    feni "Gerak ke kiri, Kana….hahahahaha"
    hide feni_side with dissolve
    show tana_side at left with dissolve
    tana "Hahahaha. Jangan kakuuuuu"
    hide tana_side with dissolve
    "Pia yang penasaran pun mengintip dibalik pintu yang sedikit terbuka itu"
    show pia_side at left with dissolve
    pia "{i}lagi pada ngapain sih?{/i}"
    hide pia_side with dissolve
    "Terlihat Kana dan Tana sedang berlatih dance"
    show pia_side at left with dissolve
    pia "{size=-10}Woaaaa… Ternyata Kana sama Tana boleh juga ya ngedancenya{/size}"
    hide pia_side with dissolve
    "Pia pun menatap mereka dengan perasaan iri, namun penasaran sehingga tetap melihat dari balik pintu itu."
    "Beberapa hari kemudian, Pia terus menerus melihat Tana & Kana latihan."
    "Pia melihat dengan tatapan mau tapi malu."
    "[mcname] pun menyadari bahwa di dalam hati kecil Pia, masih ada cita-cita yang sudah lama dikubur."
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}KEESOKAN HARINYA{/color}" with Pause(2.0)
    scene ruang ukm with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    mcname "Kana, Tana. Mau tanya dong. Kira-kira kalian masih butuh anggota, gak?"
    show tana_side at left with dissolve
    tana "Jujurly masih bro, kenapa?"
    tana "Kamu mau jadi idol?"
    tana "Coba joget dong."
    hide tana_side with dissolve
    mcname "Bukan akuuuuuuu, tapi Pia."
    show kana_side at left with dissolve
    kana "HAH? Serius? Dia mau?"
    hide kana_side with dissolve
    "[mcname] pun menceritakan tentang cita-cita yang sebelumnya pernah diceritakan Pia"
    "......."
    show kana_side at left with dissolve
    kana "Wow, aku mau nangis. Kenapa Pia hentiin cita citanya itu, ih?"
    kana "Aku mau ngajak dia! Akan aku bujuk!"
    hide kana_side with dissolve
    mcname "Sabar, biar aku. Kalian tunggu aja ya. Jangan bilang-bilang Pia dulu."
    show tana_side at left with dissolve
    tana "Aman~"
    hide tana_side with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}DI ROOFTOP{/color}" with Pause(2.0)
    play music "audio/BGM_Rooftop Romance Pia.mp3" fadein 1.0
    scene rooftop with dissolve
    show pia at pia_near with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    mcname "Pia, aku mau ngomong dong"
    show pia_side at left with dissolve
    pia "Yak, apa nih? Tumben"
    hide pia_side with dissolve
    mcname "Kamu percaya sama aku kan, Pia?"
    show pia_side with dissolve
    pia "Err…i-iya..kenapa nih?"
    hide pia_side with dissolve
    mcname "Aku masih punya 1 tiket permintaan kan? Aku mau pake tiket itu”"
    show pia_side at left with dissolve
    pia "Wow, oke. Apa nih?"
    hide pia_side with dissolve
    mcname "JADI IDOL!!!"
    show pia_side at left with dissolve
    pia "[mcname]… Kan aku udah bilang gamau"
    hide pia_side with dissolve
    mcname "Hmm.. Padahal katanya mau request apa aja bisa… Hmm"
    show pia_side at left with dissolve
    pia "Tapi ga gitu"
    hide pia_side with dissolve
    mcname "Yaudah aku ganti, kamu nyoba dan ngeliat langsung dari deket"
    mcname "Gimana? Gampang kan?"
    show pia_side at left with dissolve
    pia "Heeeeeh. Aaaa nyesel sok ngide ngasi gituan ih."
    hide pia_side with dissolve
    mcname "Hehe gimana? Gampang loh"
    show pia_side at left with dissolve
    pia "Iya deh. Iya iya."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}SORE HARINYA{/color}" with Pause(2.0)
    play music "audio/BGM_Lorong.mp3" fadein 1.0
    scene lorong with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    "Pia sampai di depan ruang club, ditemani [mcname] di belakangnya sambil tersenyum"
    show pia at pia_near with dissolve
    show pia_side at left with dissolve
    pia "Hufff. Tenangkan diri"
    hide pia_side with dissolve
    mcname "Cemangat Piyak~"
    pia "*Membuka Pintu*"
    scene black with dissolve
    play sound "audio/open_door.mp3" fadein 1.0
    scene ruang ukm with dissolve
    show pia at pia_near with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    show pia_side at left with dissolve
    pia "AKU MAU JADI IDOL! AJAK AKU BAAANG~"
    hide pia_side with dissolve
    "Kana yang sedang makan kue pun sampai menjatuhkan kuenya ke meja"
    hide pia with dissolve
    show kana at kana_near_left_2 with dissolve
    show tana at tana_right with dissolve
    "Kana & Tana" "*Saling tatap tatapan*"
    "Kana & Tana" "LESGOOOOO!! YAAAAY!"
    "Kana dan Tana pun berlari memeluk Pia"
    mcname "Huhu senengnya. Semangat ya, Pia"
    show kana_side at left with dissolve
    kana "T-tapi kerjaan Pia siapa yang handle dong ini huhuhu."
    hide kana_side with dissolve
    "Tiba tiba terdengar suara seorang gadis cantik dengan rambut ponytail."
    "Wajahnya tegas namun tetap memancarkan kebaikan, memberikan perpaduan unik antara kekuatan dan kehangatan."
    "Pandangannya tajam dengan senyuman yang lembut, memberikan kesan kehangatan yang melindungi."
    "???" "Selow. Biar aku yang handle, tapi ajarin dulu ya, mesti gimana ini ngerjainnya."
    show pia_side at left with dissolve
    pia "A-aman. T-tapi…"
    hide pia_side with dissolve
    "Takamina" "Salam kenal, kayaknya kita baru pertama ketemu ya. Namaku Takamina."
    show tana_side at left with dissolve
    tana "Ah iya. Kenalin, ini Kak Takamina. Anggota klub ini juga."
    hide tana_side with dissolve
    show pia_side at left with dissolve
    pia "Aaah. Salam kenal Kak Takaminaa."
    hide pia_side with dissolve
    "Takamina" "Alooo, salam kenal."
    "Takamina" "Jadi gimana? Kamu lanjut pindah ke divisi bagian idol kah?"
    show pia_side at left with dissolve
    pia "Umm… Apa boleh buat"
    hide pia_side with dissolve
    show feni_side at left with dissolve
    feni "Mantap, karena jadi rame. Kayaknya susah euy kalo latihan di dalem gini, sempit ga sih?"
    hide feni_side with dissolve
    "Tana & Kana" "Iya juga."
    $ quick_menu = False
    menu:
        "Gapapa, mau gimana lagi. cuma ada disini kan tempatnya":
            $ renpy.block_rollback()
            $ quick_menu = True
            mcname "Gapapa, mau gimana lagi. Cuma ada disini kan tempatnya"
            "Akhirnya mereka pun latihan di ruang club yang sempit itu."
            "*Brukk*"
            show tana_side at left with dissolve
            tana "Eh maap Pia kesikut kepalanya. Gapapa kan? Sempit huhuhu"
            hide tana_side with dissolve
            show pia_side at left with dissolve
            pia "Err…gapapa Ton. Aman\n*Sambil mengusap keningnya*"
            hide pia_side with dissolve
            "Tak lama kemudian"
            "PRAAAAAANK"
            show pia_side at left with dissolve
            pia "Awwww"
            hide pia_side with dissolve
            "Pia pun menyenggol lemari kaca di ruang club tersebut sampai pecah dan mengenai dirinya"
            "Semua Orang" "PIAAAAAAAA"
            "Terlihat Pia penuh luka dan darah, kemudan dibawa ke rumah sakit untuk dilakukan penanganan lebih lanjut."
            $ quick_menu = False
            scene black with dissolve
            show text "{color=#FFF}BEBERAPA MINGGU KEMUDIAN{/color}" with Pause(2.0)
            scene ruang ukm with dissolve
            $ renpy.block_rollback()
            $ quick_menu = True
            "Pia memutuskan untuk tidak lagi ikut club jepang dan beraktivitas menjadi idol"
            stop music fadeout 1.0
            $ quick_menu = False
            scene black with dissolve
            show text "{color=#FF0000}BAD END{/color}" with Pause(2.0)
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits
        "Ke rooftop ga sih? Luas":
            mcname "Ke rooftop ga sih? Luas"
            jump goodendpiarooftop

    play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
    jump credits

label goodendpiarooftop:
    show pia_side at left with dissolve
    pia "AH BENER JUGA, AYO KE ROOFTOP AJA."
    hide pia_side with dissolve
    "Semua Orang" "Let's Gooooo"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}DI ROOFTOP{/color}" with Pause(2.0)
    play music "audio/BGM_Rooftop Romance Pia.mp3" fadein 1.0
    scene rooftop with dissolve
    show kana at kana_near_left_2 with dissolve
    show pia at pia_near_right with dissolve
    show kana_side at left with dissolve
    kana "Waaah sepi ya, luas juga."
    hide kana_side with dissolve
    show pia_side at left with dissolve
    pia "Hehehe, ini markas aku sama [mcname] nih"
    hide pia_side with dissolve
    show kana_side at left with dissolve
    kana "Hmmm… berdua?"
    kana "Kalian ngapain aja berduaan di sini? Hayooo"
    hide kana_side with dissolve
    show pia_side at left with dissolve
    pia "APAAN IH, CUMA NGOBROL SAMA GAMBAR KOK!!!"
    hide pia_side with dissolve
    mcname "Betul"
    show pia_side at left with dissolve
    pia "BANTUIN WEH, BETUL BETUL AJA LU"
    hide pia_side with dissolve
    mcname "Ya apa lagi? Emang, kan? Ahahahaha"
    "Hari itu berakhir dengan mereka saling bercanda di rooftop sore itu"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}KEESOKAN HARINYA DI RUANG CLUB{/color}" with Pause(2.0)
    scene ruang ukm with dissolve
    # Harusnya BGM Ruang UKM 
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname] dan Takamina masuk ke ruangan klub dan melihat Kana Tana Pia sedang termenung lesu"
    mcname "Loh kok pada lesu gitu"
    

