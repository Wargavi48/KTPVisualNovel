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
    stop music fadeout 1.0
    scene black with dissolve
    # Harusnya BG Hall
    scene depan kampus with dissolve
    #  Harusnya BGM Hall
    play music "audio/BGM_Kampus.mp3" fadein 1.0
    "Keesokan harinya, semua karya sudah terpajang di sepanjang lorong dan lobby gedung DKV. Banyak sekali Mahasiswa/i dari fakultas lain yang datang untuk sekedar berswafoto atau menikmati hasil karya Maba DKV layaknya mengunjungi pameran seni."
    "Fiony, Freya, dan Kana sedang berjalan bersama mengunjungi pameran ini."
    show kana at char_left with dissolve
    show fio at char_center with dissolve
    show freya at char_right with dissolve
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
    scene black with dissolve
    # Harusnya BG Hall
    scene depan kampus with dissolve
    "Setelah berkeliling"
    show kana at char_left with dissolve
    show fio at char_center with dissolve
    show freya at char_right with dissolve
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
    scene black with dissolve
    # Harusnya BG Hall
    scene depan kampus with dissolve
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
    pia "Weh [mcname]!!! Cepio ngirim foto dia selfie sama gambar kita!!!!"
    nvl clear
    fio_nvl "P"
    fio_nvl "P"
    fio_nvl "P"
    fio_nvl "P"
    fio_nvl "P"
    fio_nvl "P"
    fio_nvl "{image=cepio selfie.png}"
    play music "audio/Dreamcatcher.mp3" fadein 1.0
    jump credits