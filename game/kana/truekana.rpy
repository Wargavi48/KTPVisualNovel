label truekana:
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kantin.ogg" fadein 1.0
    scene kantin with Dissolve(1.0)
    show kana at kana_near
    $ quick_menu = True
    "[mcname!c]" "Huft Huft. Ehh maaf, aku telat dikit gapapa kan?"
    hide kana
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Haha gapapa. Untung kamu cepet datangnya meskipun telat, ini tadi kursimu udah ada yang mau ambil loh."
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near
    with dissolve
    "[mcname!c]" "Hehe sorry yaaa. Tadi beres kelas, perutnya mules dikit. Kemarin abis makan pedes soalnya."
    hide kana
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Ya udah ini, tadi aku udah sekalian pesenin buat kamu juga."
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near
    with dissolve
    "[mcname!c]" "Heeee, okee makasih yaa udah mesenin sekalian amanin tempat duduk juga."
    "[mcname!c] duduk di tempat duduk dan mulai melanjutkan obrolan."
    "[mcname!c]" "Ehh Kana, kamu tau ga siiih?"
    hide kana
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Iya [mcname!c]? Kenapa?"
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near
    with dissolve
    "[mcname!c]" "Aku denger-denger ada event jejepangan yang bakal diadain sama pihak kampus gitu loh."
    hide kana
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "YANG BENER!!??"
    hide kana_side_talk with dissolve
    "Kana pun menjawab dengan penuh semangat, saking semangatnya ia sampai berdiri dari tempat duduknya dan membuatnya diliatin oleh orang-orang sekitar."
    "[mcname!c]" "Semangat banget kamu Kana, ahahah. Sampe diliatin\norang-orang loh."
    hide kana_talk
    show kana_shy_talk at kana_near
    show kana_side_cry at left
    with dissolve
    kana "EH!??? I-iya maaf-maaf, terlalu excited soalnya. Denger-denger sih event jejepangan kampus ini tuh selalu rame gitu, makanya aku excited. Apalagi bareng temen, hehe."
    hide kana_side_cry
    hide kana_shy_talk
    show kana at kana_near
    with dissolve
    "[mcname!c]" "Eh iya Kana, kalau gitu kamu mau ke eventnya bareng aku, gak? Sekalian ajarin aku, soalnya ini kan event pertamaku hehe."
    hide kana
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Ah! Serius? Nanti kita kabar-kabaran ya."
    hide kana_side_talk
    hide kana_talk
    show kana_smile at kana_near
    with dissolve
    "[mcname!c]" "Okeee~"
    "Setelah itu Kana dan [mcname!c] pun menghabiskan makanan mereka sambil mengobrol dan tertawa ringan."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_sore.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Tak terasa waktu telah berlalu."
    "Kana dan [mcname!c] berpisah karena sudah ada kegiatan\nmasing-masing yang harus dilakukan."
    jump truekanakos

label truekanakos:
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" fadein 1.0 volume (0.8)
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Di kost..."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(2.0)
    $ quick_menu = True
    "[mcname!c]" "{i}Kana lagi ngapain ya...{/i}"
    "[mcname!c]" "{i}Chat aja kali ya?{/i}"
    "[mcname!c]" "{i}Hmmmm, tapi mulai chatnya gimana ya? Bingung...{/i}"
    menu:
        "Yang kamu lakukan..."
        "P":
            stop music fadeout 1.0
            $ quick_menu = False
            "P"
            play music "BGM_Bad End.ogg" fadein 1.0
            "[mcname!c] memilih untuk menghubungi Kana dengan awalan “P”, dibandingkan hal lainnya."
            "Kana pun tidak membalas chat tersebut dan meng-ghosting pesan dari [mcname!c] sampai event dimulai."
            scene black with dissolve
            show text "{color=#FFF}*HAHAHAHA DI GHOSTING TUH, MAKANYA JANGAN ASAL P, P, P GA SOPAN TAU*{/color}" with Pause(3.0)
            scene black with dissolve
            show text "{color=#FF0000}BAD END{/color}" with Pause(2.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits
        "Malam Kana, sibuk ga?":
            "[mcname!c] ngechat Kana, di situ [mcname!c] bertanya tentang kabarnya terlebih dahulu dan basa-basi seperti orang yang kehabisan topik."
            jump truekanachat
        "Langsung telepon aja":
            stop music fadeout 1.0
            $ quick_menu = False
            play music "BGM_Bad End.ogg" fadein 1.0
            "[mcname!c] memilih untuk langsung menelepon Kana dan ternyata Kana sedang bersama keluarga."
            "Tanpa sengaja, Kana memblokir nomor [mcname!c] karena [mcname!c] menelepon terus menerus."
            scene black with dissolve
            show text "{color=#FFF}*YAHAHAHA, DIBLOCK KAN? MAKANYA JANGAN LANGSUNG TELPON ORANG AJA, KAN DIBLOCK*{/color}" with Pause(3.0)
            scene black with dissolve
            show text "{color=#FF0000}BAD END{/color}" with Pause(2.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits

label truekanachat:
    stop music fadeout 1.0
    $ quick_menu = False
    nvl clear
    play music "BGM_Happy + HP.ogg" fadein 1.0 volume (2.0)
    mc_nvl "{size=-5}Malam Kana, sibuk nggak ya? Hehe.{/size}"
    kana_nvl "{size=-5}Umm engga kok knp ya?(OVO) {/size}"
    mc_nvl "{size=-5}Aku mau nanya soal event jejepangan itu, jadi kan?{/size}"
    kana_nvl "{size=-5}Maksudnya jadi?{/size}"
    mc_nvl "{size=-5}Yaa jadi kan? Ummm kita berangkat bareng.{/size}"
    kana_nvl "{size=-5}Jadi kok. Mau ketemuan jam berapa? \(^w^)?{/size}"
    mc_nvl "{size=-5}Jam 7 lewat 12 gimana?{/size}"
    kana_nvl "{size=-5}Jam 7 lewat 12? Kaya pernah denger di mana deh (OAO)?{/size}"
    mc_nvl "{size=-5}Ahh perasaan kamu aja kali. Gimana? Ga kemaleman kah?{/size}"
    kana_nvl "{size=-5}Hmmm, oke deh jam segitu aja.{/size}"
    mc_nvl "{size=-5}Btw nanti kita di sana mau ngapain aja ya? Jujur ini event pertamaku.{/size}"
    mc_nvl "{size=-5}Jadi tadi gimana tips and tricknya buat di event, Yang Mulia Kanaia Asa?{/size}"
    kana_nvl "{size=-5}IHHHH apaan sih. Ya udah jadi kalau dulu tuh biasanya aku-{/size}"
    nvl clear
    scene kamar mc kota with Dissolve(0.01)
    play sound "audio/SFX - Telephone.mp3"
    show kana_calling at ui_handphone with dissolve
    $ quick_menu = True
    "Tanpa sengaja Kana menekan tombol voice call dan [mcname!c] pun tanpa pikir panjang menekan tombol jawab."
    stop sound fadeout 1.0
    hide kana_calling
    show kana_connect at ui_handphone
    with dissolve
    stop sound
    show kana_side_cry at left with dissolve
    kana "Ehh maaf kepencet!!! Aduh malu banget, aku matiin aja ya."
    hide kana_side_cry with dissolve
    "[mcname!c]" "JANGAN!!!"
    "Kana terdiam kaget karena mendengar suara [mcname!c] yang tiba-tiba teriak."
    "[mcname!c]" "M-maksudnya ga usah dimatiin kalo boleh, biar lebih seru ngobrolnya."
    show kana_side_drylaugh at left with dissolve
    kana "Uuummm... O-oke deh."
    hide kana_side_drylaugh with dissolve
    "[mcname!c]" "Jadi gimana tadi pengalaman kamu? Aku nungguin loh, kasih tau dong biasanya gimana aja di event jejepangan tuh."
    show kana_side_talk at left with dissolve
    kana "Oh iya lupa, jadi kalau aku dulu ikut event jejepangan tuh biasanya-"
    hide kana_side_talk with dissolve
    hide kana_connect with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    play music "BGM_Kosan 1.ogg" fadein 1.0
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Tanpa sadar Kana dan [mcname!c] pun mengobrol lama, bahkan sampai melewati tengah malam."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(2.0)
    $ quick_menu = True
    "Beberapa kali [mcname!c] mendengar Kana menguap dan menyarankan untuk mengakhiri voice call, tetapi ia tetap melanjutkan ceritanya seakan meluapkan semua cerita yang telah ia simpan sendirian selama ini."
    "Beberapa saat kemudian pun Kana tertidur dengan voice call masih menyala."
    hide kana_connect
    show kana_connected at ui_handphone
    with dissolve
    "Beberapa saat kemudian pun Kana tertidur dengan voice call masih menyala."
    "[mcname!c]" "Kana...? Kana...?"
    "Beberapa kali [mcname!c] menyebutkan nama Kana akan tetapi Kana tetap tidak menjawab."
    "[mcname!c]" "{i}Heeee... Kana ketiduran ya?{/i}"
    "Suara nafas Kana sempat beberapa kali terdengar."
    "Setelah beberapa saat, [mcname!c] pun memilih untuk mengakhiri voice call itu dan tidur agar tidak telat besok."
    hide kana_connected with dissolve
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Pagi Siang.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Tak terasa hari festival pun tiba."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(2.0)
    $ quick_menu = True
    "[mcname!c] bangun beberapa jam lebih awal daripada waktu yang telah dijanjikan, ia tidak sabar untuk pergi ke event tersebut dan menghabiskan waktu dengan Kana."
    "[mcname!c] pun tidak lupa untuk makan, mandi, serta memakai parfum yang menurutnya lebih mahal daripada makannya selama 1 minggu."
    "[mcname!c]" "Oke, sudah siap! Let's go~"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" fadein 1.0 volume (0.8)
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Malam itu..."
    $ quick_menu = False
    scene kampus malam with Dissolve(2.0)
    hide kana_date_confused
    show kana_date_confused_blush at kana_near
    show kana_date_side_shy_confused at left
    with dissolve
    $ quick_menu = True
    kana "[mcname!c]... ha.. ha.."
    kana "Haloo, maaf ya nunggu lama.."
    hide kana_date_side_shy_confused with dissolve
    "Suara Kana terpotong-potong yang menandakan bahwa Kana baru saja berlari."
    "[mcname!c]" "Hahaha santai aja Kana, tarik nafas dulu bentar gitu. Keliatan banget kalau kamu baru lari tuh."
    hide kana_date_confused_blush
    show kana_date_shy_closeeye_talk at kana_near
    show kana_date_side_shy_confused at left
    with dissolve
    kana "Maaf ya tadi lumayan macet di jalan, makanya aku lari. Kukira udah telat, terus aku juga liat kamu udah ada di depan gerbang. Jadi tadi aku lari deh..."
    hide kana_date_side_shy_confused
    hide kana_date_shy_closeeye_talk
    show kana_date_shy at kana_near
    with dissolve
    "[mcname!c]" "Santai aja Kana. Ya udah, nih kamu minum dulu."
    hide kana_date shy
    show kana_date_shy_closeeye_talk at kana_near
    with dissolve
    kana "*Glug* *Glug*"
    hide kana_date_shy_closeeye_talk
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "Makasih ya [mcname!c]. Sekarang udah aman kok, jadi kamu siap gak?"
    hide kana_date_talk 
    show kana_date at kana_near
    hide kana_date_side_talk
    with dissolve
    "[mcname!c]" "Siap dong, ya kali ga siap. Nggak kaya siapa gitu... Yang ketiduran di tengah-tengah call."
    hide kana_date_talk
    show kana_date_shy_talk at kana_near
    show kana_date_side_shy_confused at left
    with dissolve
    kana "IHHHH kamu masih bangun???? Kukira udah dimatiin callnya."
    hide kana_date_side_shy_confused
    hide kana_date_shy_talk
    show kana_date_shy_closeeye at kana_near
    with dissolve
    "[mcname!c]" "Hahaha. Soalnya kamu asik banget, cerita ini itu, eh tiba-tiba diem. Pas dipanggil-panggil, kamu malah tidur. Mana sempet ngigo dikit juga."
    hide kana_date_shy_closeeye
    show kana_date_confused_blush at kana_near
    show kana_date_side_shy_confused at left
    with dissolve
    kana "KAMU DENGER!??? AAAAAA!!!"
    hide kana_date_side_shy_confused
    hide kana_date_confused_blush
    show kana_date_angry at kana_near
    show kana_date_side_confused at left
    with dissolve
    kana "Lupaiin gak? Kalau enggak, aku marah besar nih!"
    hide kana_date_side_confused with dissolve
    "[mcname!c]" "Marah karir, maksudnya?"
    show kana_date_side_confused at left
    with dissolve
    kana "LUPAINNN!!!"
    hide kana_date_side_confused with dissolve
    "[mcname!c]" "Iya iya. Mending sekarang kita masuk yuk, keburu malem banget nanti pada tutup."
    hide kana_date_angry
    show kana_date_shy_closeeye_talk at kana_near
    show kana_date_side_shy_confused at left
    with dissolve
    kana "Awas aja kalo nggak, aku bakal buat kamu lupa dengan paksa! Ya udah deh, ayo masuk. Aku dah ga sabar."
    hide kana_date_side_shy_confused
    hide kana_date_shy_closeeye_talk
    hide kana_date_shy
    hide kana_date
    with dissolve
    "[mcname!c] dan Kana pun pergi ke event tersebut."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Matsuri Malam.ogg" fadein 1.0
    scene matsuri malam with Dissolve(1.0)
    #Harusnya BG Jejepangan malam
    show kana_date_smile at kana_near with dissolve
    $ quick_menu = True
    "Di sana banyak kegiatan, mulai dari event utama sampai event sampingan."
    "Di antaranya ada cosplay event, song cover competition, dan mini game yang terinspirasi dari permainan tradisional Jepang lainnya."
    "[mcname!c]" "Ehhh Kana bentar...\n*Huft huft*"
    "[mcname!c]" "Sabar... Kana... Kamu semangat banget sih... B-bentar aku tarik nafas dulu."
    hide kana_date_smile
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "Ahhh ayooo~ Kamu masa kalah sih sama aku?"
    hide kana_date_side_talk
    hide kana_date_talk
    show kana_date at kana_near
    with dissolve
    "[mcname!c]" "Soalnya kamu cepet banget ke sana ke sininya."
    "[mcname!c]" "Belum ada 10 menit, kita udah pindah tempat mulu. Kamu ga mau liat-liat dulu booth merch yang ada di situ?"
    hide kana_date
    show kana_date_confused at kana_near
    show kana_date_side_confused at left
    with dissolve
    kana "Ihhh kamu semalem ga research dulu tentang booth yang bakalan ada? Aku udah liat-liat listnya."
    kana "Ada beberapa tempat yang pengen aku samperin, jadi aku cuma bentar doang di tempat lainnya gitu..."
    hide kana_date_side_confused
    hide kana_date_confused
    show kana_date at kana_near
    with dissolve
    "[mcname!c]" "Oooo gitu ya ternyata. Maaf deh ini kan event pertama ku, jadi aku ga tau harus research list kaya gitu."
    hide kana_date
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "Ya udah ayo ikutin aku aja."
    hide kana_date_side_talk
    hide kana_date_talk
    show kana_date_smile at kana_near
    with dissolve
    "Kana pun langsung menarik tangan [mcname!c] yang hanya bisa mengikuti ke mana pun Kana pergi, hingga Kana berhenti di suatu tempat."
    hide kana_date_smile
    show kana_date at kana_near
    with dissolve
    "[mcname!c]" "Ummm Kana? Ada apa?"
    "Kana terdiam, di situ ada sebuah event yang sedang berlangsung."
    "[mcname!c] pun melihat event tersebut, di sana ada sing cover competition."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/Dreamcatcher_inst_v2.mp3" fadein 1.0 volume (1.0)
    scene stage with Dissolve(1.0)
    show tana_idol_side_laugh at left
    with dissolve
    $ quick_menu = True
    tana "Ayooo semuanyaa~"
    hide tana_idol_side_laugh
    show pia_idol_side_smile at left
    with dissolve
    pia "Let's go!"
    hide pia_idol_side_smile with dissolve
    "[mcname!c] pun melihat panggung dan mengerti kenapa Kana terdiam. Di situ, terlihat dua orang yang sedang menyanyi dengan suara yang indah."
    hide pia_idol_smile 
    hide tana_idol_laugh
    with dissolve
    "Kurang lebih 3 menit [mcname!c] dan Kana terdiam mendengarkan mereka bernyanyi."
    play sound "SFX - Large Cheering.mp3" loop fadein 0.5
    hide kana_date
    with dissolve
    "Saat selesai, Kana, [mcname!c], dan seluruh penonton pun bertepuk tangan dengan keras."
    hide kana_date_smile with dissolve
    $ quick_menu = False
    stop sound
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Matsuri Malam.ogg" fadein 1.0
    #Harusnya BGM Jejepangan Malam
    scene matsuri malam with Dissolve(1.0)
    #Harusnya BG Jejepangan Malam
    $ quick_menu = True
    play sound "audio/crowd_noise.mp3" loop fadein 1.0 volume (4.0)
    #HARUSNYA SFX Applause
    "[mcname!c]" "Gilaaaa, kereen bangeett sumpah! Iya ga, Kana?"
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "Iyaaa aku sampe terdiem loh, kamu juga dengerin tadi?"
    hide kana_date_side_talk 
    hide kana_date_talk
    show kana_date at kana_near
    with dissolve
    "[mcname!c]" "Iya lah, kamu tiba-tiba diem aja. Gimana aku ga ikutan dengerin? Keren banget, kapan ya aku bisa nyanyi kaya gitu..."
    "[mcname!c]" "Btw, kamu suka nyanyi juga?"
    hide kana_date
    show kana_date_confused_blush at kana_near
    show kana_date_side_shy_confused at left
    with dissolve
    kana "Eee-enggak kok, a-aku..."
    hide kana_date_confused_blush
    show kana_date_confused_blush_sideeye at kana_near 
    with dissolve
    kana "E-ehhh liat deh, di situ ada cosplay yang bagus mending kita ke sana."
    hide kana_date_side_shy_confused
    show kana_date_shy at kana_near
    with dissolve
    "Kana tiba-tiba menghindari dari jawaban [mcname!c] dan berlari ke arah seorang cosplayer."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene matsuri malam with Dissolve(1.0)
    $ quick_menu = True
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "Eh Kaa, permisi~"
    hide kana_date_side_talk
    hide kana_date_talk
    show kana_date_smile at kana_near
    with dissolve
    "Cosplayer" "Iya Ka kenapa?"
    "[mcname!c]" "Kenapa Kana tiba-tiba..."
    hide kana_date_smile
    show kana_date at kana_near 
    with dissolve
    "[mcname!c]" "Ehh kamu cosplay jadi Kamen Driver Den-A ya?"
    "Cosplayer" "Wahhh iya ka, kebetulan aku suka Kamen Driver."
    hide kana_date_smile
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "[mcname!c], kamu juga suka?"
    hide kana_date_side_talk
    hide kana_date_talk
    show kana_date at kana_near
    with dissolve
    "[mcname!c]" "SUKA!!??? Wahhhh aku ngikutin banget semua series Kamen Driver loh Kana."
    hide kana_date
    show kana_date_angry at kana_near
    with dissolve
    "Cosplayer" "Wahh, kukira ga terlalu banyak yang kenal cosplayku. Ternyata ada juga ya yang kenal, makasih ya Kak."
    "Cosplayer" "Eh Kak, mau ngobrol lagi ga? Keknya seru kita ngobrol bareng."
    #*CHOSE*
    menu:
        "Yang [mcname!c] lakukan..."
        "Menghabiskan waktu sama cosplayer.":
            stop music fadeout 1.0
            $ quick_menu = False
            play music "BGM_Bad End.ogg" fadein 1.0
            hide kana_date_angry
            show kana_date_deadeye at kana_near
            with dissolve
            "[mcname!c] tetap mengobrol dengan cosplayer tersebut dan mengabaikan keberadaan Kana untuk beberapa saat."
            hide kana_date_deadeye
            with dissolve
            "Tak lama saat [mcname!c] tersadar, Kana sudah menghilang dan HPnya tidak dapat dihubungi lagi."
            scene black with dissolve
            show text "{color=#FFF}BRO BRO LAGI JALAN BARENG BERDUAAN KO MALAH DITINGGAL NGOBROL SAMA ORANG LAIN SI ADUHHH{/color}" with Pause(4.0)
            scene black with dissolve
            show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3"
            jump credits
        "Menolak ajakan cosplayer tersebut.":
            #*CHOSE B*
            jump truekanajapanfest
    
label truekanajapanfest:
    hide kana_date_angry
    show kana_date_smile at kana_near
    with dissolve
    "[mcname!c]" "Eh maaf ya nanti lagi, aku lagi sama temen soalnya. Kalo boleh minta social medianya aja kak, biar bisa ngobrol."
    hide kana_date_smile
    show kana_date_angry at kana_near
    with dissolve
    "Cosplayer" "Ooh iya kak, ini bisa di add \"@RizukaMiku_[random_number]\". Makasih banyak yaa~"
    hide kana_date_angry
    show kana_date_deadeye at kana_near
    with dissolve
    "[mcname!c]" "Sama-sama kak."
    "[mcname!c]" "Eh Kana maaf lama ya. Tadi hampir aja keasikan, untung aku inget ada kamu yang lagi nungguin aku haha."
    hide kana_date_deadeye
    show kana_date_deadeye_smile at kana_near
    show kana_date_side at left
    with dissolve
    kana "Enggak kok, ga lama. Seru ya."
    show kana_date_deadeye at kana_near
    hide kana_date_deadeye_smile at kana_near
    hide kana_date_side at left
    with dissolve
    "[mcname!c]" "Eh kamu kenapa Kana, marah ya? Tadi kelamaan ya? Sorry..."
    hide kana_date_deadeye
    show kana_date_deadeye_smile at kana_near
    show kana_date_side at left
    with dissolve
    kana "G."
    hide kana_date_side 
    hide kana_date_deadeye_smile
    show kana_date_angry at kana_near
    with dissolve
    "[mcname!c]" "Waduh. Ya udah sebagai permintaan maaf aku ajak main di stand sana deh gimana?"
    hide kana_date_angry
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "BEENER!?? Eh maksudnya... beneran nih?"
    hide kana_date_side_talk
    hide kana_date_talk
    show kana_date at kana_near
    with dissolve
    "[mcname!c]" "Iya, bener kok. Ya udah, ayo."
    hide kana_date
    show kana_date_smile at kana_near
    with dissolve
    pause (1.0)
    hide kana_date_smile
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "Yayyy~"
    hide kana_date_talk at kana_near
    hide kana_date_side_talk at left
    hide kana_date_deadeye
    with dissolve
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Minigame Tana.ogg" fadein 1.0
    scene shooting game with Dissolve(1.0)
#Harusnya BG MINIGAME TANA (Tanpa mainin)
    show kana_date_side_talk at left
    with dissolve
    $ quick_menu = True
    kana "Kamu beneran bisa ga?"
    hide kana_date_side_talk
    hide kana_date_talk
    with dissolve
    "[mcname!c]" "Bener Kana, tenang aja. Kok kamu ga percaya ke aku gitu sih."
    hide kana_date
    show kana_date_side_talk at left
    with dissolve
    kana "Soalnya kamu keliatan ga yakin."
    hide kana_date_side_talk
    hide kana_date_talk
    with dissolve
    "[mcname!c]" "Ini aku lagi fokus, Kana."
    "Tak lama kemudian...\n\n \nP.S.= The minigame is on Tana's route."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play sound "audio/SFX - Finish Game.mp3"
    scene matsuri malam with Dissolve(1.0)
    show kana_date_smile at kana_near with dissolve
    $ quick_menu = True
    "[mcname!c] pun mendapatkan skor tinggi."
    stop sound fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Matsuri Malam.ogg" fadein 1.0
    scene matsuri malam with Dissolve(1.0)
    show kana_date at kana_near with dissolve
    $ quick_menu = True
    "[mcname!c]" "Liat, kan? Aku bisaaa, siapa dulu?"
    hide kana_date
    show kana_date_angry at kana_near
    with dissolve
    "[mcname!c] mendekatkan tangannya ke telinganya dan seolah olah menunggu Kana menjawab."
    "[mcname!c]" "Siapa dulu, hmmmm?"
    hide kana_date_angry
    show kana_date_confused at kana_near
    show kana_date_side_confused at left
    with dissolve
    kana "Iya iya, kamu jago deh."
    hide kana_date_side_confused
    hide kana_date_confused
    show kana_date_angry at kana_near
    with dissolve
    "[mcname!c]" "Nahh gitu dong, hahah~"
    "Setelah mendapatkan hadiah dari mini game di dalam booth, [mcname!c] memberikan hadiahnya kepada Kana."
    hide kana_date_angry
    show kana_date_shy_smile at kana_near
    show kana_date_side_shy at left
    with dissolve
    kana "Eeeh?"
    hide kana_date_side_shy
    hide kana_date_shy_smile
    show kana_date_shy at kana_near
    with dissolve
    "[mcname!c]" "Ini, buat kamu."
    hide kana_date_shy
    show kana_date_shy_smile at kana_near
    show kana_date_side_shy at left
    with dissolve
    kana "Gapapa nih?"
    hide kana_date_side_shy
    hide kana_date_shy_smile
    show kana_date_shy at kana_near
    with dissolve
    "[mcname!c]" "Iyaa, sekarang kamu gak marah lagi kan?"
    hide kana_date_shy
    show kana_date_confused at kana_near
    show kana_date_side_confused at left
    with dissolve
    kana "M-masih, hmph!"
    hide kana_date_side_confused
    hide kana_date_confused
    show kana_date_angry at kana_near
    with dissolve
    "[mcname!c]" "Jadi Yang Muliaaa, kita mau ke mana lagi? Hambamu siap untuk menemanimu ke mana pun dan sampai kapan pun, ahaha."
    hide kana_date_angry
    show kana_date_confused at kana_near
    show kana_date_side_confused at left
    with dissolve
    kana "Apaan sihh Yang Mulia Yang Mulia, mending mulai sekarang kamu panggil aku “Nay” deh."
    hide kana_date_side_confused
    hide kana_date_confused
    show kana_date_angry at kana_near
    with dissolve
    "[mcname!c]" "Okee dehh, Nay."
    "[mcname!c]" "Kalo gitu, kamu mau makan apa? Aku traktir deh, soalnya kamu udah guide sana-sini."
    hide kana_date_angry
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "Hmmmm, apa ya? Kayaknya takoyaki enak deh."
    hide kana_date_side_talk
    hide kana_date_talk
    show kana_date at kana_near
    with dissolve
    "[mcname!c]" "Bolehhh, tunggu bentar yaa."
    hide kana_date
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "Okeeee hati-hati, ya."
    hide kana_date_side_talk
    hide kana_date_talk
    show kana_date_smile at kana_near
    with dissolve
    "[mcname!c] pun pergi meninggalkan Kana sejenak untuk membeli takoyaki."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Ruang Tamu.ogg" fadein 1.0
    scene matsuri malam with Dissolve(1.0)
    $ quick_menu = True
    "Setelah beberapa saat, [mcname!c] kembali sambil membawa takoyaki."
    show kana_date at kana_near with dissolve
    "[mcname!c]" "Yahhh Nay, maaf ini cuma sisa satu porsi lagi. Ini buat kamu aja deh, aku gapapa."
    hide kana_date
    show kana_date_confused at kana_near
    show kana_date_side_confused at left
    with dissolve
    kana "Lah kok gitu sih, kamu juga pasti laper kan?"
    hide kana_date_side_confused
    hide kana_date_confused
    show kana_date at kana_near
    with dissolve
    "[mcname!c]" "Enggak koook."
    play sound "audio/hungry.mp3" volume (10.0)
    hide kana_date
    show kana_date_smile at kana_near
    with dissolve
    "Tiba-tiba, terdengar suara perut [mcname!c] yang berbunyi cukup keras sehingga Kana dapat mendengarnya."
    stop sound
    hide kana_date_smile
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "Hahaha ga bisa bohong tuh perut kalau masalah makanan mah."
    hide kana_date_side_talk
    hide kana_date_talk
    show kana_date_smile at kana_near
    with dissolve
    "Muka [mcname!c] pun memerah, merasa malu dengan perutnya." 
    "[mcname!c]" "Aduuhhhhh…\n*Blush*"
    hide kana_date_smile
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "Sini kita makan bareng aja. Ini kan ada 6, kita bagi aja.\nMasing-masing 3 gimana?"
    hide kana_date_side_talk
    hide kana_date_talk
    show kana_date at kana_near
    with dissolve
    "[mcname!c]" "Tapi kan kamu pengen takoyaki."
    hide kana_date
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "Gak apa-apa kok, lagian aku juga makannya sedikit."
    hide kana_date_side_talk
    hide kana_date_talk
    show kana_date at kana_near
    with dissolve
    "[mcname!c]" "O-oke deh kalau gitu. Eh tapi ini cuma ada satu doang garpu nya, bentar ya aku coba minta lagi ke penjualnya."
    hide kana_date
    show kana_date_shy at kana_near
    with dissolve
    "Sesaat [mcname!c] akan pergi, Kana tiba-tiba menangkap tangan [mcname!c]."
    hide kana_date_shy
    show kana_date_shy_smile at kana_near
    show kana_date_side_shy at left
    with dissolve
    kana "[mcname!c], udah ga usah."
    kana "Keburu takoyakinya dingin, nanti ga enak. Kita makan bareng aja."
    kana "Sini, kita gantian aja."
    hide kana_date_side_shy
    hide kana_date_shy_smile
    show kana_date_shy at kana_near
    with dissolve
    "[mcname!c]" "Nay? Bukannya itu malah…"
    hide kana_date_shy
    show kana_date_shy_talk at kana_near
    show kana_date_side_shy_confused at left
    with dissolve
    kana "Udah cepetan."
    hide kana_date_side_shy_confused
    hide kana_date_shy_talk
    show kana_date_shy at kana_near
    with dissolve
    "[mcname!c]" "I-iya iya. Oke deh."
    "Kana pun memakan takoyakinya, lalu Kana pun menjulurkan tangannya yang memegang garpu serta takoyaki ke arah [mcname!c]."
    hide kana_date_shy
    show kana_date_confused_blush at kana_near
    show kana_date_side_shy_confused at left
    with dissolve
    kana "Nih."
    hide kana_date_side_shy_confused
    hide kana_date_confused_blush
    show kana_date_shy_closeeye at kana_near
    with dissolve
    "Seakan tidak ingin sadar akan peristiwa yang sedang terjadi, [mcname!c] tetap memakan takoyaki yang diberikan Kana. Takoyakinya terasa sedikit manis, padahal takoyaki yang dipesan harusnya pedas asin."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene matsuri malam with Dissolve(1.0)
    show kana_date_shy_closeeye at kana_near
    $ quick_menu = True
    "[mcname!c]" "Ah udah abis lagi aja, ga kerasa ya."
    "[mcname!c]" "Eh Nay, kamu kenapa?"
    "Terlihat muka Kana memerah, mungkin karena baru sadar akan apa yang baru saja terjadi."
    hide kana_date_shy_closeeye
    show kana_date_shy_smile at kana_near
    show kana_date_side_shy at left
    with dissolve
    kana "E-eh iya udah abis aja.\n*Blush*"
    hide kana_date_side_shy
    hide kana_date_shy_smile
    show kana_date_shy at kana_near
    with dissolve
    "[mcname!c]" "Okeeee selesai, jadi kita ke mana, Nay?"
    hide kana_date_shy
    show kana_date_shy_closeeye at kana_near
    with dissolve
    "Sesaat [mcname!c] akan pergi, Kana tiba-tiba mengambil tisu, mengulurkan tangannya, dan mengelap saus yang ada di pipi [mcname!c]."
    "Terkejut dengan tindakan Kana, [mcname!c] hanya bisa diam sambil tersenyum."
    hide kana_date_shy_closeeye
    show kana_date_confused_blush at kana_near
    show kana_date_side_shy_confused at left
    with dissolve
    kana "Eh i-ini, a-aku kebiasaan ngurus sepupuku yang masih kecil. Eh ah, ini kita udah kan makannya? Yuk kita ke sana aja."
    hide kana_date_side_shy_confused
    hide kana_date_confused_blush
    show kana_date_shy at kana_near
    with dissolve
    hide kana_date_shy with dissolve
    "Kana yang malu pun berlari kabur, meninggalkan [mcname!c] yang masih berdiri di situ."
    "[mcname!c]" "Ehhh?? Tungguin Nay."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Kana dan [mcname!c] pun pergi kembali untuk melihat-lihat booth yang ada di event tersebut."
    "Sampai pada akhirnya event utama pada hari itu pun dimulai."
    $ quick_menu = False
    scene matsuri malam with Dissolve(2.0)
    show kana_date at kana_near with dissolve
    $ quick_menu = True
    "[mcname!c]" "Eh Nay, ayoo ini event utamanya udah mau dimulai."
    hide kana_date
    show kana_date_confused at kana_near
    show kana_date_side_confused at left
    with dissolve
    kana "Eeeeh, okaay."
    hide kana_date_confused 
    hide kana_date_side_confused 
    with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene matsuri malam with Dissolve(1.0)
    #Harusnya BG JEJEPANGAN MALAM
    play sound "audio/crowd_noise.mp3" loop fadein 1.0 volume (4.0)
    show kana_date at kana_near with dissolve
    $ quick_menu = True
    "Kana dan [mcname!c] pun pergi ke tempat di mana event utama diadakan. Event tersebut adalah pertunjukan kembang api kecil kecilan yang akan diadakan oleh panitia acara."
    "Terlihat banyak pengunjung yang menantikan pertunjukan kembang api di event tersebut."
    "[mcname!c]" "Bentar lagi nihhh."
    hide kana_date
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "Aaaaa, udah gak sabaar!"
    hide kana_date_side_talk with dissolve
    stop sound fadeout 1.0
    play sound "audio/SFX - Hanabi.WAV" loop
    $ quick_menu = False
    window auto hide
    with Pause(2.0)
    window auto show
    show kana_date_side_talk at left with dissolve
    $ quick_menu = True
    kana "TAMAAYAAAAAA~!"
    hide kana_date_side_talk
    hide kana_date_talk
    show kana_date_smile at kana_near
    with dissolve
    "[mcname!c]" "TAMAYAAAAAA~!"
    "Kana dan [mcname!c] pun menikmati pemandangan kembang api di event tersebut. Meski hanya beberapa menit saja, tapi kenangannya akan tersimpan selamanya."
    stop sound
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Rooftop Romance Pia.ogg" fadein 1.0
    scene kampus malam with Dissolve(1.0)
    show kana_date_smile at kana_near with dissolve
    $ quick_menu = True
    "Kana dan [mcname!c] merasa hangat, senang, dan bahagia. Tanpa sadar event untuk hari ini sudah selesai."
    "[mcname!c]" "Seru banget hari ini Nay! Makasih banyak yaa."
    hide kana_date_smile
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "Hahah, seru banget emang. Makasih juga udah mau nemenin aku, akhirnya aku ada temen yang suka hal-hal gini."
    hide kana_date_side_talk
    hide kana_date_talk
    show kana_date at kana_near
    with dissolve
    "[mcname!c] tersenyum mendengar perkataan Kana."
    "[mcname!c]" "Aku juga seneng banget, soalnya bareng kamu."
    hide kana_date
    show kana_date_shy at kana_near
    show kana_date_side_shy_smile at left
    with dissolve
    kana "*Blush*"
    hide kana_date_side_shy_smile with dissolve
    "[mcname!c]" "Eh ah, kamu pulang naik apa Nay?"
    hide kana_date_shy
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "Aku biasanya dijemput sih, soalnya udah malem. Emangnya kenapa?"
    hide kana_date_side_talk with dissolve
    "[mcname!c]" "Ooo enggak. Tadinya mau ngajak bareng, tapi aku juga baru sadar ternyata ini udah malem banget. Jadi mending naik mobil aja biar ga masuk angin."
    show kana_date_side_talk at left with dissolve
    kana "Hmmm, nanti deh next time gimana? Soalnya mamah ga ijinin aku naik motor kalau udah malem."
    hide kana_date_side_talk
    hide kana_date_talk
    show kana_date at kana_near
    with dissolve
    "[mcname!c]" "Iya aku ngerti kok Nay. Ya udah ya, kamu hati-hati Nay."
    hide kana_date
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "Iya makasih ya buat hari ini, kamu juga hati-hati."
    hide kana_date_side_talk
    hide kana_date_talk
    show kana_date_smile at kana_near
    with dissolve
    "[mcname!c] dan Kana pun pergi. [mcname!c] masih merasa senang dan bahagia karena telah menghabiskan waktu bersama Kana."
    #*SKIP TO SCENE*
    #*BG KOS MALAM*
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" fadein 1.0 volume (0.8)
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Apakah ini date? Mungkin iya, atau mungkin hanya [mcname!c] yang merasa demikian."
    "Meskipun begitu, rasa bahagia dan senang tidak dapat dihilangkan dari hati [mcname!c]."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(2.0)
    $ quick_menu = True
    "Setelah beberapa menit, [mcname!c] datang ke kostnya."
    play sound "ReceiveText.ogg" loop volume (2.0)
    "HP [mcname!c] pun berbunyi."
    "Dia melihat adanya notif chat dari Kana." 
    stop sound
    $ quick_menu = False
    nvl clear
    kana_nvl "{size=-5}H-halooo… ( ^A^)/{/size}"
    mc_nvl "{size=-5}Halo juga Nayyy… Kenapa nih?{/size}"
    kana_nvl "{size=-5}Ee-engga kok, cuma mastiin kamu udah pulang aja… Takut nyasar (~ ^3^)~ Hehehe…{/size}"
    mc_nvl "{size=-5}Hahaha, ini baru aja selesai beres-beres. Kamu nungguin ya?{/size}"
    kana_nvl "{size=-5}K-kata siapa? Aku ga nungguin kamu kok ( OwO)z{/size}"
    mc_nvl "{size=-5}Hahaha, Nay… Kamu emang suka pake emot kayak gitu ya? Sorry kalo tiba-tiba nanya, soalnya aku penasaran. Dari dulu kalo chat kadang pake, kadang engga.{/size}"
    kana_nvl "{size=-5}Ehhh… Sorry ya kebiasaan... Hehe{/size}"
    kana_nvl "{size=-5}A-aneh ya?{/size}"
    mc_nvl "{size=-5}Engga lah, ga aneh kok. Malah keliatannya lucu aja. Kalau emang kamu lebih suka pake emot kaya gitu, pake aja lucu juga liatnya.{/size}"
    kana_nvl "{size=-5}Yeeee (>A<)/{/size}"
    mc_nvl "{size=-5}Hahaha, lucu emang{/size}"
    nvl clear
    scene kamar mc kota with dissolve
    $ quick_menu = True
    "[mcname!c] dan Kana pun menghabiskan waktu mereka berdua dengan membahas kembali apa yang terjadi hari ini."
    "Mulai dari bertemu cosplayer, bermain di booth minigame, bahkan membeli merch-merch yang dijual di booth lainnya."
    "Sampai pada akhirnya mereka tertidur dengan tetap memegang HP masing-masing."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kelas.ogg" fadein 1.0 volume (1.5)
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya..."
    $ quick_menu = False
    scene kelas with Dissolve(2.0)
    $ quick_menu = True
    "Hari dimulai seperti biasanya..."
    "[mcname!c] memasuki kelas dengan keadaan hampir terlambat. Saat mencari tempat kosong, [mcname!c] mendengar seseorang memanggilnya."
    show freya_talk at freya_near
    show freya_side_talk at left
    with dissolve
    freya "[mcname!c]! [mcname!c]! Sini!"
    hide freya_side_talk
    hide freya_talk
    show freya at freya_near
    with dissolve
    "Karena waktu menunjukan bahwa kelas akan segera dimulai, tanpa pikir panjang [mcname!c] pun duduk di sebelah Freya."
    hide freya
    show freya at freya_near
    with dissolve
    "[mcname!c]" "Psstt, Fre. Naya ke mana dah?"
    show freya_shock at freya_near
    show freya_side_shock at left
    with dissolve
    freya "Lah baru aja mau nanyain ke kamu, emang dia ga ngabarin?"
    hide freya_shock
    hide freya_side_shock
    with dissolve
    "[mcname!c]" "Nggak. Terakhir chat tuh waktu malem, abis itu aku ketiduran deh. Ini aja kan hampir telat, emang ke kamu ga ada kabar gitu?"
    hide freya_shock
    show freya_talk at freya_near
    show freya_side_talk at left
    with dissolve
    freya "Ga ada sama sekali, kalian emang sampe jam berapa?"
    hide freya_talk
    hide freya_side_talk
    with dissolve
    "[mcname!c]" "Ga tau aku lupa, seingetku pas jam 1-an masih sadar kayaknya."
    hide freya_talk
    show freya_angrysmile at freya_near
    show freya_side_angrysmile at left
    with dissolve
    freya "Wahhh udah jelas ini mah dia kesiangan, haduhhh."
    hide freya_side_angrysmile
    hide freya_angrysmile
    hide freya
    with dissolve
    stop music fadeout 1.0
    $ quick_menu=False
    scene black with Dissolve(1.0)
    scene kelas with Dissolve(1.0)
    play music "audio/BGM_Dosen.ogg" fadein 1.0
    show dosen at dosen_center with dissolve
    hide dosen
    show dosen_talk at dosen_center
    show dosen_side_talk at left
    with dissolve
    $ quick_menu=True
    dosen "Selamat pagi semuanya."
    dosen "Mohon untuk beberapa menit ke depan perhatikan pelajaran dulu ya. Jadi untuk memahami bahwa-"
    hide dosen_side_talk
    hide dosen_talk
    show dosen at dosen_center
    with dissolve
    stop music fadeout 1.0
    $ quick_menu=False
    scene black with Dissolve(1.0)
    play music "BGM_Sore.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu=True
    "Beberapa jam kemudian..."
    $ quick_menu=False
    scene kelas sore with Dissolve(2.0)
    show dosen_talk at dosen_center
    show dosen_side_talk at left
    with dissolve
    $ quick_menu=True
    dosen "Baik. Pelajaran hari ini sudah selesai. Sampai bertemu di pertemuan selanjutnya."
    hide dosen_side_talk
    hide dosen_talk
    show dosen at dosen_center
    with dissolve
    "Setelah dosen meninggalkan ruangan, kelas pun berakhir."
    $ quick_menu=False
    scene black with Dissolve(1.0)
    scene kelas sore with Dissolve(1.0)
    play sound "audio/SFX - Call.mp3" volume(3.0)
    #HARUSNYA KRIIIIINNNGGGG
    $ quick_menu=True
    "Tiba-tiba HP Freya berbunyi cukup keras sehingga membuat hampir seluruh kelas melihat ke arahnya."
    show freya_shock at freya_near
    show freya_side_shock at left
    with dissolve
    stop sound fadeout 1.0
    freya "Aduhh maaf ya semuanya. Lupa ga disilent tadi, hehe."
    hide freya_side_shock
    hide freya_shock
    show freya_talk at freya_near
    with dissolve
    stop music fadeout 1.0
    play sound "audio/SFX - Angkat Telepon.wav" volume(3.0)
    #HARUSNYA SUARA ANGKAT TELEPON
    $ quick_menu=False
    scene black with Dissolve(1.0)
    play music "BGM_Happy + HP.ogg" fadein 1.0 volume (2.0)
    scene kelas sore with Dissolve(1.0)
    show freya_talk at freya_near
    show freya_side_talk at left
    with dissolve
    $ quick_menu=True
    freya "Apaan?"
    hide freya_side_talk
    hide freya_talk
    show freya_awe at freya_near
    show freya_side_awe at left
    with dissolve
    freya "Oo ini udah selesai. Kamu telat sih, ya udah gimana lagi."
    hide freya_side_awe
    hide freya_awe
    show freya_talk at freya_near
    show freya_side_talk at left
    with dissolve
    freya "Ga ada yang mintain izin ke dosen, orang ga ada kabar..."
    hide freya_side_talk
    show freya_side_talk at left
    with dissolve
    freya "Ya udah, dadah."
    hide freya_side_talk
    hide freya_talk
    show freya at freya_near
    with dissolve
    play sound "audio/SFX - End Call.mp3" volume(3.0)
    #HARUSNYA SUARA TUTUP TELEPON
    stop music fadeout 1.0
    $ quick_menu=False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Sore.ogg" fadein 1.0 volume (1.5)
    scene kelas sore with Dissolve(1.0)
    show freya at freya_near with dissolve
    $ quick_menu=True
    "[mcname!c]" "Itu tadi Naya?"
    hide freya
    show freya_talk at freya_near
    show freya_side_talk at left
    with dissolve
    freya "Iya katanya dia ketiduran, hadeuhh. Ya udah lah gimana lagi."
    hide freya_side_talk
    hide freya_talk
    show freya at freya_near
    with dissolve
    "[mcname!c]" "Hadeeeh..."
    hide freya
    show freya_talk at freya_near
    show freya_side_talk at left
    with dissolve
    freya "Btw kamu udah siapin kado belum buat Naya? Kan dia 4 hari lagi ultah."
    hide freya_side_talk with dissolve
    "[mcname!c]" "EEHHHH!???"
    hide freya
    show freya_annoy at freya_near
    with dissolve
    "[mcname!c] menjawab dengan suara yang cukup keras, hingga terdengar hingga ke ujung kelas dan membuat Mahasiswa/i yang masih ada di dalam kelas terkejut."
    hide freya_annoy
    show freya_angrysmile at freya_near
    show freya_side_angrysmile at left
    with dissolve
    freya "Biasa aja napa sih? Ya udah deh kamu siapin hadiahnya yang bener ya. Awas aja kalau ga ngasih hadiah!"
    hide freya_side_angrysmile
    hide freya_angrysmile
    show freya_talk at freya_near
    show freya_side_talk at left
    with dissolve
    freya "Oke, aku duluan ya. Ada janji sama yang lain, dahhh."
    hide freya_side_talk
    hide freya_talk
    with dissolve
    "[mcname!c]" "Heeeee..."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kampus Sore.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Di kost..."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(2.0)
    $ quick_menu = True
    "Karena hari ini hanya ada satu kelas, [mcname!c] memilih untuk menghabiskan waktunya di kosan sambil memikirkan apa yang cocok sebagai kado ulang tahun untuk Kana."
    "[mcname!c]" "{i}Aduuhhh aku ngasih apa ya buat Kana? Kalau diinget-inget lagi, Kana tuh suka sama jejepangan.{/i}"
    "[mcname!c]" "{i}Tapi masa aku ngasih Naya merch anime? Aku ga pernah liat dia pake pakaian anime-anime gitu sihh.{/i}"
    "[mcname!c]" "{i}Kalau official CD anime atau band? Tapi aku ga tau dia suka band apaan, aaaa bingung banget mau ngasih apa.{/i}"
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" fadein 1.0 volume (0.8)
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Seakan sedang terjadi perang di dalam pikiran [mcname!c], tanpa terasa waktu berubah menjadi malam."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(2.0)
    $ quick_menu = True
    "[mcname!c] hanya bisa kebingungan memilih kado ulang tahun apa yang cocok."
    "Tiba-tiba terdengar bunyi dari HP yang menunjukkan bahwa ada notifikasi dari Kana dan Freya yang mencoba menghubungi [mcname!c] berkali-kali."
    play sound "SFX - Calling.mp3" loop fadein 1.0
    show groupcall at ui_handphone
    show freya_side_shock at left 
    with dissolve
    freya "Nahhh kan kalau gini enak, ga usah ngehubungin satu-satu."
    hide freya_side_shock with dissolve
    "[mcname!c]" "Ah Naya, Freya, maaf ya tadi aku ketiduran."
    show kana_side_smile at left with dissolve
    kana "Iya gapapa. Tadi juga aku terlalu spam, maaf ya."
    hide kana_side_smile with dissolve
    "[mcname!c]" "Enggak apa-apa, aku ga sempet liat semua chatnyaa. Sorry."
    show freya_side_talk at left with dissolve
    freya "Jadi tadi kenapa Nay?"
    hide freya_side_talk with dissolve
    show kana_side_confused at left with dissolve
    kana "Harus aku yang ngejelasin?"
    hide kana_side_confused with dissolve
    "[mcname!c]" "Ya udah, sini deh aku yang jelasin."
    show freya_side_annoy at left with dissolve
    freya "Lah, emang tau ada apa?"
    hide freya_side_annoy with dissolve
    "[mcname!c]" "Ya nggak lah, makanya cepet jelasin."
    show kana_side_talk at left with dissolve
    kana "Hahahaha."
    hide kana_side_talk with dissolve
    show freya_side_annoy at left with dissolve
    freya "Hadeeeh"
    hide freya_side_annoy with dissolve
    show kana_side_talk at left with dissolve
    kana "Oke, jadi TLDR aja nih ya. Lusa tuh bakalan ada event di cafe mall yang udah aku tungguin banget dari beberapa bulan yang lalu."
    kana "Nah di eventnya tuh, bakalan ada cake yang dijual. Sumpah itu enak banget cakenya."
    kana "Terus, yang bikin aku pengen banget tuh cakenya limited edition gitu, jadi aku bisa jamin kalau cakenya itu bakalan ENAKKKKK BANGETTT."
    kana "Aku jamin itu bakalan enak banget. Kalau ga enak, nanti aku traktir makan di all you can eat deh."
    kana "Nahhhh tapi yang jadi masalahnya tuh, di event itu satu orang cuma bisa beli satu buah cake aja."
    kana "Jadi nanti aku pengen ajak Freya sama kamu buat antri dan beli juga."
    kana "Nanti uangnya dari aku kok, santai aja. Tapi nanti ikut antri biar bisa beli juga."
    hide kana_side_talk with dissolve
    show freya_side_shock at left with dissolve
    freya "Kayaknya itu kepanjangan deh buat TLDR, Nay."
    hide freya_side_shock with dissolve
    "[mcname!c]" "Keknya TLDR-mu itu \"Too Long Di Read\", Nay."
    show kana_side_drylaugh at left with dissolve
    kana "Hehehe, maaf terlalu semangat."
    hide kana_side_drylaugh with dissolve
    "[mcname!c]" "Tapi oke, intinya lusa kan?"
    show kana_side_talk at left with dissolve
    kana "Iya lusa."
    hide kana_side_talk with dissolve
    "[mcname!c]" "Oke aku bisa kok."
    show freya_side_talk at left with dissolve
    freya "Yaudah nanti kabarin lagi yaa. Aku mau tidur dulu."
    hide freya_side_talk with dissolve
    show kana_side_talk at left with dissolve
    kana "Okeee, good night minna~"
    hide kana_side_talk with dissolve
    "[mcname!c]" "Oke, good night."
    hide groupcall with dissolve
    play sound "audio/SFX - End Call.mp3"
    "[mcname!c]" "Hmmmmmm."
    "[mcname!c]" "{i}Oke nanti aku harus liat-liat sekalian milih hadiah apa yang kayaknya cocok buat Naya di mall.{/i}"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Mall.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Beberapa hari kemudian..."
    $ quick_menu = False
    scene mall temp with Dissolve(2.0)
    $ quick_menu = True
    "Hari itu [mcname!c] pergi ke mall untuk menemani Kana membeli limited cake."
    "Di sana [mcname!c] berencana untuk melihat gerak-gerik Kana sebagai petunjuk tentang hadiah apa yang cocok untuknya."
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "Ah, halo [mcname!c]. Sorry, lama nunggu ya?"
    hide kana_date_side_talk
    hide kana_date_talk
    show kana_date at kana_near
    with dissolve
    "[mcname!c]" "Enggak, kok. Haha."
    hide kana_date
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "Freya belum dateng ya? Hmmmm..."
    hide kana_date_side_talk
    hide kana_date_talk
    show kana_date at kana_near
    with dissolve
    "[mcname!c]" "Tunggu bentar lagi deh haha."
    hide kana_date
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "Yaudaah."
    hide kana_date_talk 
    hide kana_date_side_talk 
    with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene mall temp with Dissolve(1.0)
    show kana_date_confused at kana_near
    show kana_date_side_confused at left
    with dissolve
    $ quick_menu = True
    kana "Aduhh ini Freya ke mana sih? Jangan bilang dia lupa?"
    hide kana_date_side_confused
    hide kana_date_confused
    show kana_date_angry at kana_near
    with dissolve
    "[mcname!c]" "Waduh aku juga ga tau tuh Nay, coba kamu telepon."
    hide kana_date_angry
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "Oke bentar yaa-"
    hide kana_date_side_talk
    hide kana_date_talk
    show kana_date at kana_near
    with dissolve
    pause(1.0)
    #SFX KRINGGG Telepon*
    play sound "audio/SFX - Call.mp3" loop fadein 1.0
    show kana_date_side_confused at left with dissolve
    kana "Eh?"
    hide kana_date_side_confused
    with dissolve
    show kana_date_side_confused at left
    with dissolve
    stop sound fadeout 1.0
    kana "FREYAAA!! Kamu ke mana??"
    hide kana_date_side_confused
    show kana_date_side_confused at left
    with dissolve
    kana "HA!?? Aduhhh… ya udah deh."
    play sound "audio/SFX - End Call.mp3"
    hide kana_date_side_confused with dissolve
    show kana_date_shy_smile at kana_near
    show kana_date_side_shy_smile at left
    with dissolve
    stop sound
    kana "Umm [mcname!c], ini Freya katanya ada urusan di kampus. Jadinya kita berdua aja nih hehe, kaya waktu itu."
    hide kana_date_side_shy_smile
    hide kana_date_shy_smile
    show kana_date_shy at kana_near
    with dissolve
    "[mcname!c]" "Ahahaha, iya nih. Masih inget aja kamu. Ya udah yuk jalan."
    hide kana_date_shy
    show kana_date_drylaugh at kana_near
    show kana_date_side_drylaugh at left
    with dissolve
    kana "Hahaha, okee deh."
    hide kana_date_side_drylaugh
    hide kana_date_drylaugh
    show kana_date_smile at kana_near
    with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene mall with Dissolve(1.0)
    show kana_date at kana_near with dissolve
    $ quick_menu = True
    "Saat masuk ke dalam mall dan berjalan ke arah cafe, Kana sempat beberapa kali curi-curi pandang ke arah toko perhiasan yang ada di dalam mall."
    "Lalu [mcname!c] pun sempat menanyakan beberapa hal."
    "[mcname!c]" "Eh Nay, tumben kamu ganti sepatu."
    hide kana_date
    show kana_date_drylaugh at kana_near
    show kana_date_side_drylaugh at left
    with dissolve
    kana "Iya nih. Kemarin pas aku coba udah agak sempit gitu sih, jadi ini pake sepatu yang lain haha."
    hide kana_date_side_drylaugh with dissolve
    "[mcname!c]" "Ohhh gitu ya, kamu lagi suka apa belakangan ini?"
    hide kana_date_drylaugh
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "Heee? Kamu kenapa [mcname!c], kok tiba-tiba tanya kayak ginian?"
    show kana_date at kana_near
    hide kana_date_talk
    hide kana_date_side_talk
    with dissolve
    "[mcname!c]" "Gak apa-apa, daripada -1 topik hahaha."
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "Hahaha, iya juga sih. Aku akhir-akhir ini sama sepupuku biasanya main masak-masak gitu sih."
    hide kana_date_side_talk
    hide kana_date_talk
    show kana_date at kana_near
    with dissolve
    "[mcname!c]" "Ohhh gitu ya, eh itu cafenya kan?"
    "[mcname!c]" "{i}Mantep aku dapet beberapa ide kado buat Kana, hehehe.{/i}"
    hide kana_date
    show kana_date_smile at kana_near
    show kana_date_side_closeeye at left
    with dissolve
    kana "Iya, udah ya kita pura-pura ga kenal dulu biar ga dicurigai haha."
    hide kana_date_side_closeeye
    with dissolve
    "[mcname!c]" "Oke dehh."
    hide kana_date_smile with dissolve
    $ quick_menu=False
    scene white with Dissolve(1.0)
    pause(1.0)
    scene mall with Dissolve(1.0)
    $ quick_menu=True
    "Setelah membeli cake tersebut, [mcname!c] dan Kana pun bertemu."
    show kana_date at kana_near with dissolve
    "[mcname!c]" "Ini cakenya Nayy."
    hide kana_date
    show kana_date_confused at kana_near
    show kana_date_side_confused at left
    with dissolve
    kana "Ehhh? Gapapa nih?"
    hide kana_date_side_confused with dissolve
    "[mcname!c]" "Gapapa, soalnya keliatannya kamu suka banget cake ini."
    hide kana_date_confused
    show kana_date_talk at kana_near
    show kana_date_side_talk at left
    with dissolve
    kana "Wihhh thank you [mcname!c]!"
    kana "Kalo gitu aku pulang dulu ya, mau menikmati cakenya ehehehe."
    hide kana_date_side_talk
    hide kana_date_talk
    show kana_date_smile at kana_near
    with dissolve
    "[mcname!c]" "Okeee, hati-hati di jalan."
    hide kana_smile with dissolve
    "Kana pun pulang ke rumahnya, tidak sabar untuk menikmati limited cake yang baru saja dibelinya."
    $ quick_menu = False
    scene black with dissolve
    scene mall temp with dissolve
    $ quick_menu = True
    "Tetapi, [mcname!c] tidak pulang. Dia menghabiskan harinya di Mall dan memikirkan hadiah apa yang cocok untuk Kana."
    "[mcname!c]" "{i}Hmmm dari obrolan dan kode-kode yang Kana kasih, mending aku beliin apa ya?{/i}"
    define kana_present = ""
    #*CHOSE*
    menu:
        "Yang kamu beli..."
        "Kalung":
            $ kana_present = "Kalung"
            jump truekanabuypresent
        "Sepatu":
            $ kana_present = "Sepatu"
            jump truekanabuypresent
        "Alat Masak":
            $ kana_present = "Alat Masak"
            jump truekanabuypresent
        "CD Film Horror":
            $ kana_present = "CD Film Horror"
            jump truekanabuypresent

label truekanabuypresent:
    "[mcname!c]" "{i}Oke kayaknya ini cocok deh buat Kana, sekarang waktunya pulang dan siap-siap buat besok pas ulang tahun Kana.{/i}"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" fadein 1.0 volume (0.8)
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Di kost..."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(2.0)
    $ quick_menu = True
    "Setelah [mcname!c] sampai di kosan, dia menghubungi Freya untuk membahas rencana ulang tahun Kana."
    $ quick_menu = False
    nvl clear
    mc_nvl "{size=-5}Freya.{/size}"
    freya_nvl "{size=-5}Kenapa?{/size}"
    mc_nvl "{size=-5}Ini, mau nanya buat ultah Kana nanti. Kita bakalan gimana nih ngasih suprisenya? Terus mau di mana?{/size}"
    freya_nvl "{size=-5}Kalau tempat mah udah aman aja. Biasanya aku di rumah Kana sih, nanti kamu dateng aja.{/size}"
    mc_nvl "{size=-5}Emangnya boleh ya?{/size}"
    freya_nvl "{size=-5}Ga ada yang ngelarang kok. Nanti ga perlu dekorasi apa-apa, soalnya Si Naya ga suka kalo dirayain gede-gede pake aksesoris gitu.{/size}"
    freya_nvl "{size=-5}Dulu pernah gitu, dia malah bete seharian. Lagian dia juga ga pernah inget hari ultahnya.{/size}"
    mc_nvl "{size=-5}Oke deh kalau emang gitu, nanti aku tinggal dateng aja ke rumah Kana?{/size}"
    freya_nvl "{size=-5}Iya nanti dateng aja, biar aku yang urus hehe.{/size}"
    mc_nvl "{size=-5}Okee. Thanks, Freya.{/size}"
    freya_nvl "{size=-5}Iya sama-sama.{/size}"
    nvl clear
    scene kamar mc kota with dissolve
    #CHATTING APP OFF
    $ quick_menu = True
    "Setelah semua itu, akhirnya [mcname!c] dan Freya setuju untuk melakukan perayaan ulang tahun sederhana di rumah Kana."
    "[mcname!c] pun memutuskan untuk tidur."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Pagi Siang.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Hari ulang tahun Kana..."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(2.0)
    $ quick_menu = True
    "[mcname!c]" "{i}Oke. Hari ini hari yang penting, pokoknya semua harus siap!{/i}"
    "[mcname!c]" "{i}Bentar cek dulu semuanya, pakaian? Oke.{/i}"
    "[mcname!c]" "{i}Hadiah? Oke, ada udah di bungkus juga.{/i}"
    "[mcname!c]" "{i}Wangy? Oke, tadi udah mandi sama pake parfum juga.{/i}"
    "[mcname!c]" "{i}Tinggal berangkat aja nih harusnya. Duh deg degan banget hari ini, mudah-mudahan lancar deh.{/i}"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 2.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "[mcname!c] pun pergi ke rumah Kana pada waktu yang telah ditentukan sebelumnya dengan Freya."
    "Tetapi saat [mcname!c] menghubungi Freya, ia tidak dapat dihubungi."
    "Rasa cemas, gelisah, serta was-was tidak dapat dihapus dari pikiran [mcname!c]."
    "Mungkin ini pertama kalinya [mcname!c] berinisiatif merayakan ulang tahun temannya seperti ini, sehingga ingin memberikan momen bahagia yang selalu dapat diingat oleh Kana."
    show pintu_rumah_kana at pintu_rumah_kana with dissolve
    "[mcname!c]" "{i}Aduhhh masuk ga ya, tapi belum ada Si Freya.{/i}"
    "[mcname!c]" "{i}Tapi kalau di luar terus, nanti takut dicurigain orang-orang. Mending gimana ya...{/i}"
    menu:
        "Yang [mcname!c] lakukan..."
        "{b}MASUK KE DALAM RUMAH.{/b}":
            jump truekanabeforeneutralroute
        "{b}TUNGGUIN FREYA.{/b}":
            #*CHOSE B*
            "[mcname!c] memilih untuk menunggu Freya..."
            hide pintu_rumah_kana with dissolve
            $ quick_menu = False
            scene black with Dissolve(1.0)
            pause(1.0)
            scene awan sore with Dissolve(1.0)
            show pintu_rumah_kana at pintu_rumah_kana with dissolve
            $ quick_menu = True
            "Tak lama kemudian, Freya pun datang."
            hide freya
            show freya_side_talk at left
            with dissolve
            freya "Halo [mcname!c]."
            hide freya_side_talk
            with dissolve
            "[mcname!c]" "Haloo."
            "[mcname!c]" "Yuk?"
            show freya_side_shock at left
            with dissolve
            freya "Gasss!"
            hide freya_side_shock
            with dissolve
            play sound "audio/ding.mp3" volume(3.0)
            "Freya memencet bel rumah Kana."
            play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
            jump trueKanaNungguFreya

label truekanabeforeneutralroute:
    #*CHOSE A*
    "[mcname!c] pun memutuskan untuk menekan bel tanpa menunggu Freya."
    play sound "audio/ding.mp3" volume (3.0)
    with Pause (2.0)
    "Tak lama kemudian..."
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    "Mamah Kana" "Ah [mcname!c]. Ada apa?"
    "[mcname!c]" "Halo Tante, Kana ada di rumah?"
    "Mamah Kana" "Ada kok, kenapa?"
    "[mcname!c]" "Jadi sebenarnya saya sama Freya mau ngadain kejutan untuk ulang tahun Kana."
    "Mamah Kana" "Eeeeh, makasih banyak ya [mcname!c]. Kana pasti bakal seneng banget!"
    "[mcname!c]" "Hehe, ngomong-ngomong tante masih inget waktu itu pernah bilang mau ngabulin satu permintaan?"
    "Mamah Kana" "Iya, kenapa nih tiba-tiba."
    "[mcname!c]" "Kalo bisa, mau minta tolong kejutannya dirahasiakan dari Kana haha."
    "Mamah Kana" "Eeehh, oke oke. Tante gak bakal ganggu, hehe."
    "[mcname!c]" "Terima kasih banyak, tante."
    "Mamah Kana" "Ya sudah, ayok sini masuk dulu."
    hide pintu_rumah_kana with dissolve
    stop music fadeout 1.0
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0) 
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Ruang Tamu.ogg" fadein 1.0
    scene ruang tamu sore with Dissolve(1.0)
    show kana_home_smile at kana_near with dissolve
    $ quick_menu = True
    "[mcname!c]" "Siang Nay, maaf telat ya?"
    hide kana_home_smile
    show kana_home_talk at kana_near
    show kana_home_side_talk at left
    with dissolve
    kana "Engga kok sini masuk aja. Freya belum datang, nanti biasanya dia suka telat dikit."
    hide kana_home_side_talk
    hide kana_home_talk
    show kana_home at kana_near
    with dissolve
    "[mcname!c]" "Eh, i-iya Nay."
    hide kana_home
    show kana_home_talk at kana_near
    show kana_home_side_talk at left
    with dissolve
    kana "Mau minum apa [mcname!c]? Sekalian nunggu Freya nih. Btw kok gugup sih, emang ada apa?"
    show kana_home at kana_near
    hide kana_home_side_talk
    with dissolve
    "[mcname!c]" "E-engga kok, cuma ini kan pertama kali kita berduaan… J-jadi agak gugup dikit."
    hide kana_home_talk
    show kana_home_confused at kana_near
    show kana_home_side_confused at left
    with dissolve
    kana "Lah? Bukannya kemarin pas aku sakit, kamu temenin aku ya?"
    show kana_home_side_shy_eh at left 
    show kana_home_cry at kana_near
    hide kana_home_confused at kana_near
    hide kana_home_side_confused at left
    with dissolve
    kana "Terus kita kan pernah ke cafe bareng, game center bareng, event jejepangan bareng, ke mall kemarin juga kita berduaan."
    hide kana_home_confused at kana_near
    hide kana_home_side_confused at left
    show kana_home_shy_closeeye_talk at kana_near 
    show kana_home_side_shy_ahn at left
    with dissolve
    kana "Kamu ga anggep itu kah? Sedih sih, huhuhu."
    show kana_home_sad at kana_near
    hide kana_home_shy_closeeye_talk
    hide kana_home_side_shy_ahn
    hide kana_home_side_sad
    hide kana_home_side_shy_eh
    hide kana_home_cry
    with dissolve
    "[mcname!c]" "E-eh maksudnya gak gitu. Cuma entah kenapa hari ini aku lebih gugup aja dari biasanya.."
    hide kana_home_confused
    show kana_home_normal_talk at kana_near
    show kana_home_side_normal_talk at left
    with dissolve
    kana "Gugup kenapa?"
    hide kana_home_normal_talk
    hide kana_home_side_normal_talk
    show kana_home_normal at kana_near
    with dissolve
    "[mcname!c]" "E-ehh itu..."
    "[mcname!c]" "{i}Aduhh kok aku gugup ya? Apa gara-gara mau ngasih hadiah ke Naya, terus takut dia gak suka ya?{/i}"
    "[mcname!c]" "Ya gitu deh, haha. Ini Si Freya ke mana ya, tumben lama."
    hide kana_home_talk
    show kana_home_confused at kana_near
    show kana_home_side_confused at left
    with dissolve
    kana "Hmmm... Sebenernya kalian mau ngapain deh? Soalnya Si Freya Freya itu gak ngasih tau mau kumpul buat apaan?"
    hide kana_home_confused
    hide kana_home_side_confused
    with dissolve
    "[mcname!c]" " Eh-"
    "[mcname!c]" "{i}Mampus, harus alesan apa ya biar bisa bohongin Kana?{/i}"
    "[mcname!c]" "Eh itu... Sebenarnya kita mau-"
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    hide kana_home_confused
    hide kana_home_normal
    hide kana_home_sad 
    hide kana_home
    with dissolve 
    pause(1.0)
    show freya at freya_near_right
    show kana_home_smile at kana_near_left_2
    with dissolve
    "Sebelum [mcname!c] sempat menyelesaikan kata katanya, suara Freya terdengar dari arah pintu masuk."
    hide freya
    show freya_shock at freya_near_right
    show freya_side_shock at left
    with dissolve
    freya "HALOOOO SEMUANYAAA!!!"
    hide freya_side_shock with dissolve
    hide kana_home_smile
    hide freya_shock 
    show freya_smug at freya_near_right
    show kana_home_talk at kana_near_left_2
    show kana_home_side_talk at left
    with dissolve
    kana "Ah Frey, kaget."
    hide kana_home_side_talk
    hide kana_home_talk
    show kana_home at kana_near_left_2
    hide freya_smug
    with dissolve
    "[mcname!c]" "Waduh, Freya bikin kaget aja."
    jump truekananeutralroute1

#[Neutral Route 1]
label trueKanaNungguFreya:
    "Mamah Kana" "Ah [mcname!c], Freya. Ada apa?"
    show freya_side_talk at left
    with dissolve
    freya "Halo Tante, Kana ada di rumah?"
    hide freya_side_talk
    with dissolve
    "Mamah Kana" "Ada kok, kenapa?"
    show freya_side_talk at left
    with dissolve
    freya "Jadi sebenarnya kita mau ngadain kejutan untuk ulang tahun Kana."
    hide freya_side_talk
    with dissolve
    "Mamah Kana" "Eeeeh, makasih banyak ya kalian. Kana pasti bakal seneng banget!"
    "[mcname!c]" "Ngomong-ngomong tante masih inget waktu itu pernah bilang mau ngabulin satu permintaan?"
    "Mamah Kana" "Iya, kenapa nih tiba-tiba."
    "[mcname!c]" "Kalo bisa, mau minta tolong kejutannya dirahasiakan dari Kana haha."
    "Mamah Kana" "Eeehh, oke oke. Tante gak bakal ganggu, hehe."
    show freya_side_smile at left
    with dissolve
    freya "Terima kasih banyak, tante."
    hide freya_side_smile
    with dissolve
    "Mamah Kana" "Ya sudah, ayok sini masuk dulu."
    "[mcname!c]" "Baik."
    hide pintu_rumah_kana with dissolve
    stop music fadeout 1.0
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Ruang Tamu.ogg" fadein 1.0
    scene ruang tamu sore with Dissolve(1.0)
    #RUANG TAMU RUMAH KANA

label truekananeutralroute1:
    show freya at freya_near_right
    show kana_home at kana_near_left_2
    with dissolve
    show freya_talk at freya_near_right
    show freya_side_talk at left
    with dissolve
    $ quick_menu = True
    freya "Hehe halo Naya, udah siap kan?"
    hide freya_side_talk with dissolve
    hide kana_home
    hide freya_talk
    show kana_home_confused at kana_near_left_2
    show kana_home_side_confused at left
    with dissolve
    kana "Hah, siap?"
    show kana_home_normal at kana_near_left_2
    hide kana_home_confused
    hide kana_home_side_confused
    with dissolve
    "[mcname!c]" "Waduh Freya."
    hide freya
    show freya_shock at freya_near_right
    show freya_side_shock at left
    with dissolve
    freya "Lahh ini nih, padahal aku dah semangat gini. Dah bawa banyak game-game buat temenin kita sampe malem nih."
    hide freya_side_shock
    hide freya_shock
    show freya_smile at freya_near_right
    with dissolve
    show kana_home_confused at kana_near_left_2
    show kana_home_side_confused at left
    with dissolve
    kana "Ha?? Main game?"
    hide kana_home_confused
    hide kana_home_side_confused with dissolve
    hide freya_smile
    show freya_smug at freya_near_right
    with dissolve
    "Freya melihat ke arahku, seakan memberi kode secara tidak langsung. [mcname!c] mengangguk ke arah Freya."
    "[mcname!c]" "Lah iya Nayy, kamu ga tau? Kita kan bakalan main game lohhh."
    hide freya_smug
    show freya_smile at freya_near_right
    with dissolve
    hide kana_home_confused
    show kana_home_talk at kana_near_left_2
    show kana_home_side_talk at left
    with dissolve
    kana "Hmmm... Ya udah deh, aku ngikut aja."
    hide kana_home_side_talk
    hide kana_home_talk
    show kana_home at kana_near_left_2
    with dissolve
    hide freya_smile
    show freya_shock at freya_near_right
    show freya_side_shock at left
    with dissolve
    freya "Let's gooo!"
    hide kana_home_normal
    hide freya_shock 
    hide freya_side_shock 
    hide kana_home
    with dissolve
    "Mereka pun memainkan semua permainan yang dibawa oleh Freya."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" fadein 1.0
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Tak terasa malam pun tiba."
    $ quick_menu = False
    scene ruang tamu malam with Dissolve(2.0)
    show freya at freya_near_right
    show kana_home at kana_near_left_2
    with dissolve
    hide freya
    show freya_talk at freya_near_right
    show freya_side_talk at left
    with dissolve
    $ quick_menu = True
    freya "Eh kita pindah ke kamarmu aja yuk Nay. Udah malem, takut ganggu Mamahmu sama tetangga."
    hide freya_side_talk
    hide freya_talk
    show freya at freya_near_right
    with dissolve
    hide kana_home
    show kana_home_talk at kana_near_left_2
    show kana_home_side_talk at left
    with dissolve
    kana "Iya sih, ya udah deh ayo."
    hide kana_home_side_talk
    hide kana_home_talk
    show kana_home at kana_near_left_2
    with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kamar Kana.ogg" fadein 1.0
#HARUSNYA BGM KAMAR KANA
    scene kamar kana malam with Dissolve(1.0)
    show freya at freya_near_right
    show kana_home at kana_near_left_2
    with dissolve
    $ quick_menu = True
    "[mcname!c]" "Eh Freya, emang ruangan Naya kedap suara kah? Kok kita pindah ke sini?"
    hide freya
    show freya_talk at freya_near_right
    show freya_side_talk at left
    with dissolve
    freya "Iya mamahnya Naya masangin peredam suara, biar kalau dia berisik main game gak ganggu tetangga."
    hide freya_side_talk
    hide freya_talk
    show freya at freya_near_right
    with dissolve
    hide kana_home
    show kana_home_confused at kana_near_left_2
    show kana_home_side_confused at left
    with dissolve
    kana "Perasaan ini kamarku, tapi kok kamu yang lebih tahu daripada aku."
    hide kana_home_side_confused with dissolve
    "[mcname!c]" "Hahaha."
    hide kana_home_confused
    show kana_home at kana_near_left_2
    with dissolve
    "Ini mungkin ketiga kalinya [mcname!c] ke kamar Kana, akan tetapi kali ini ia bisa melihat ruangan kamar Kana dengan lebih seksama."
    "[mcname!c] melihat ternyata di pojok ruangan kamarnya Kana tersembunyi satu tempat khusus yang dipenuhi kumpulan-kumpulan figur dan merch anime."
    "[mcname!c]" "Wahhhh… Kana ini kan dari anime itu, keren banget kamu punya? Bukannya ini limited-edition ya?"
    hide kana_home
    show kana_home_talk at kana_near_left_2
    show kana_home_side_talk at left
    with dissolve
    kana "Iya, hahaha. Ini aku nabung dari lama, untung dapet."
    hide kana_home_side_talk
    hide kana_home_talk
    show kana_home at kana_near_left_2
    with dissolve
    "[mcname!c]" "Eh kalau ini dari anime itu kan? Boleh diliat dari deket ga?"
    hide kana_home
    show kana_home_talk at kana_near_left_2
    show kana_home_side_talk at left
    with dissolve
    kana "Boleh kok, liat aja. Asal jangan sampai rusak, hahaha."
    hide kana_home_side_talk
    hide kana_home_talk
    show kana_home at kana_near_left_2
    with dissolve
    hide freya
    show freya_talk at freya_near_right
    show freya_side_talk at left
    with dissolve
    freya "Seneng banget tuh diliat-liat."
    hide freya_side_talk
    hide freya_talk
    show freya at freya_near_right
    with dissolve
    "[mcname!c]" "Hehe sorry, soalnya ini kesukaanku juga."
    hide freya
    show freya_talk at freya_near_right
    show freya_side_talk at left
    with dissolve
    freya "Ya udah kalian have fun dulu ya, aku mau ke toilet dulu bentar."
    hide freya_side_talk
    hide freya_talk
    show freya_awe at freya_near_right
    with dissolve
    "Setelah mengatakan itu, Freya memberikan kode kepada [mcname!c] yang langsung mengerti apa yang dimaksud Freya."
    hide freya_awe with dissolve
    "[mcname!c]" "Eh, Nay. Kalau ini kamu beli dari luar negeri? Setauku di Indo belum ada."
    hide kana_home
    show kana_home_talk at kana_near_left_2
    show kana_home_side_talk at left
    with dissolve
    kana "Ehhh kalo itu sih beli di..."
    hide kana_home_side_talk with dissolve
    "[mcname!c] pun terus mengobrol dengan Kana, berusaha untuk mengalihkan perhatian Kana."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Romance Kana.ogg" fadein 1.0
    scene kamar kana malam with Dissolve(1.0)
    show kana_home at kana_near with dissolve
    $ quick_menu = True
    "Tak terasa, jam menunjukan 12 malam yang menandakan bahwa hari telah berganti dan hari ulang tahun Kana pun tiba."
    "[mcname!c]" "Nay..."
    hide kana_home
    show kana_home_shy_smile at kana_near
    show kana_home_side_drylaugh at left
    with dissolve
    kana "Iya [mcname!c]?"
    show kana_home_shy at kana_near
    hide kana_home_shy_smile
    hide kana_home_side_drylaugh
    with dissolve
    "[mcname!c]" "Kamu lagi apa?"
    hide kana_home_shy
    show kana_home_shy_smile at kana_near
    show kana_home_side_drylaugh at left
    with dissolve
    kana "Lagi duduk di kasur doang…"
    hide kana_home_shy_smile
    hide kana_home_side_drylaugh
    show kana_home_cry at kana_near
    show kana_home_side_shy_eh at left
    with dissolve
    kana "Kamu kenapa sih dari tadi kaya ada yang aneh gitu?"
    hide kana_home_side_shy_eh
    hide kana_home_cry 
    show kana_home_shy at kana_near
    with dissolve
    "[mcname!c]" "Eh iya maaf, hehe."
    "[mcname!c]" "Gugup aja sih."
    hide kana_home_shy
    show kana_home_talk at kana_near
    show kana_home_side_talk at left
    with dissolve
    kana "Gugup kenapa?"
    show kana_home_normal at kana_near
    hide kana_home_talk
    hide kana_home_side_talk
    with dissolve
    "[mcname!c]" "Jadi sebenernya... Aku ada hadiah buat kamu."
    "[mcname!c] mendekati Kana yang sedang duduk di kasurnya."
    hide kana_home_normal
    show kana_home_cry at kana_near
    show kana_home_side_shy_eh at left
    with dissolve
    kana "Hadiah?"
    hide kana_home_side_shy_eh with dissolve
    "[mcname!c]" "Iya, tapi kamu harus tutup mata dulu."
    hide kana_home_cry
    show kana_home_confused_blush at kana_near
    show kana_home_side_confused_blush at left
    with dissolve
    kana "Hah? Tutup mata?"
    hide kana_home_side_confused_blush with dissolve
    "[mcname!c]" "Iyaa, udah tutup mata dulu sana."
    hide kana_home_confused_blush
    show kana_home_shy_smile at kana_near
    show kana_home_side_talk at left
    with dissolve
    kana "O-oke."
    hide kana_home_side_talk
    hide kana_home_shy_smile
    show kana_home_shy_closeeye at kana_near
    with dissolve
    "Kana pun menutup matanya."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    $ quick_menu = True
    #Kalau di mall pilih:
    if kana_present == "Kalung":
        jump truekanarightpresent

    elif kana_present == "Sepatu": #Sepatu
        play sound "SFX - Plastic.wav" loop fadein 1.0 volume (5.0)
        $ quick_menu = False
        window auto hide
        with Pause(2.0)
        window auto show
        $ quick_menu = True
        show kana_home_side_shy_ahn at left with dissolve
        kana "Udah boleh buka mata belum?"
        hide kana_home_side_shy_ahn with dissolve
        "[mcname!c]" "Bentar lagi."
        $ quick_menu = False
        window auto hide
        stop sound fadeout 1.0
        with Pause(2.0)
        window auto show
        $ quick_menu = True
        show kana_home_side_shy_ahn at left with dissolve
        kana "[mcname!c]?"
        hide kana_home_side_shy_ahn with dissolve
        "[mcname!c]" "Udah boleh buka matanya Nay."
        show kana_home_side_shy_ahn at left with dissolve
        kana "O-okee."
        hide kana_home_side_shy_ahn with dissolve
        "Perlahan Kana membuka matanya."
        $ quick_menu = False
        scene black with Dissolve(1.0)
        play music "BGM_Bad End.ogg" fadein 1.0
        scene kamar kana malam with Dissolve(1.0)
        show sepatu
        show sepatu:
                pos (0.52, 0.72) zoom 0.18 
        with dissolve
        $ quick_menu = True
        "[mcname!c] memberikan hadiah sepatu."
        hide sepatu with dissolve
        show kana_home_talk at kana_near
        with dissolve
        "Kana terdiam sejenak..."
        hide kana_home_talk
        show kana_home_confused at kana_near
        with dissolve
        "Lagi-lagi Kana terdiam..."
        hide kana_home_confused
        show kana_home_confused_blush_sideeye at kana_near
        with dissolve
        "Kana masih terdiam..."
        "[mcname!c]" "Nay?"
        hide kana_home_confused_blush_sideeye
        show kana_home_confused at kana_near
        show kana_home_side_confused at left
        with dissolve
        kana "Eh i-iya makasih banyak ya. Tapi kok kamu tau ukuran sepatu aku, padahal aku ga pernah bilang ke kamu maupun Freya. Kamu tau dari mana?"
        hide kana_home_side_confused with dissolve
        "[mcname!c]" "....."
        show kana_home_side_confused at left with dissolve
        kana "[mcname!c]...?"
        hide kana_home_side_confused with dissolve
        "Kana pun merasa aneh dengan [mcname!c], semua kedekatan mereka langsung sirna di hati Kana."
        hide kana_home_confused with dissolve
        "Kana langsung kabur sambil memanggil Freya untuk meminta tolong."
        $ quick_menu = False
        scene black with dissolve
        show text "{color=#FFF}ADUHHH BROOO, KOK LU TAU UKURAN SEPATU KANA SIH?? NGERI KALI BROO, LU STALKER YA?{/color}" with Pause(3.0)
        scene black with dissolve
        show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
        stop music fadeout 1.0
        scene black with dissolve
        play music "audio/Dreamcatcher_v2.mp3"
        jump credits

    elif kana_present == "Alat Masak": #Alat Masak
        $ quick_menu = False
        window auto hide
        with Pause(2.0)
        play sound "SFX - Plastic.wav" loop fadein 1.0
        window auto show
        show kana_home_side_shy_ahn at left with dissolve
        $ quick_menu = True
        kana "Udah boleh buka mata belum?"
        hide kana_home_side_shy_ahn with dissolve
        "[mcname!c]" "Bentar lagi."
        $ quick_menu = False
        window auto hide
        stop sound
        with Pause(2.0)
        window auto show
        show kana_home_side_shy_ahn at left with dissolve
        $ quick_menu = True
        kana "[mcname!c]?"
        hide kana_home_side_shy_ahn with dissolve
        "[mcname!c]" "Udah boleh buka matanya Nay."
        show kana_home_side_shy_ahn at left with dissolve
        kana " O-okee."
        hide kana_home_side_shy_ahn with dissolve
        "Perlahan Kana membuka matanya."
        $ quick_menu = False
        scene black with Dissolve(1.0)
        play music "BGM_Bad End.ogg" fadein 1.0
        scene kamar kana malam with Dissolve(1.0)
        show kado at center
        show kado:
                pos (0.51, 0.70) zoom 0.22
        with dissolve
        $ quick_menu = True
        "[mcname!c] memberi hadiah seperangkat alat masak."
        hide kado with dissolve
        show kana_home_talk at kana_near
        with dissolve
        hide kana_home_talk
        show kana_home_confused at kana_near
        with dissolve
        "Raut wajah Kana bingung dan terheran-heran, kenapa [mcname!c] memberikan dia alat masak set lengkap."
        show kana_home_side_confused at left with dissolve
        kana "Ummm ini apa?"
        hide kana_home_side_confused with dissolve
        "[mcname!c]" "Ini alat masak, Nay. Soalnya kamu pernah bilang sepupumu sering datang masak-masakan. Nah aku kasih hadiah buat kamu, siapa tau aku juga bisa cobain masakan kamu hehe."
        hide kana_home_confused
        show kana_home_confused_blush_sideeye at kana_near
        show kana_home_side_blush_sideeye at left
        with dissolve
        kana "Ummm, tapi sepupuku masih TK, jadi dia pake mainan alat masak-masak..."
        hide kana_home_side_blush_sideeye with dissolve
        "[mcname!c]" "...."
        hide kana_home_confused_blush_sideeye
        show kana_home_confused at kana_near
        show kana_home_side_confused at left
        with dissolve
        kana "...."
        hide kana_home_side_confused with dissolve
        hide kana_home_confused
        show kana_home_confused at kana_near_left_2
        show freya_shock at freya_near_right
        with dissolve
        "Kana terdiam tanpa kata-kata, hingga Freya datang dan kaget dengan hadiah yang [mcname!c] berikan."
        hide freya_shock 
        show freya_annoy at freya_near_right 
        with dissolve
        "Pandangan Kana dan Freya terhadap [mcname!c] pun menjadi aneh."
        $ quick_menu = False
        scene black with dissolve
        show text "{color=#FFF}IH BROO, YA KALI AJA NGASIH HADIAH ALAT MASAK KE CEWE YANG TINGGAL SAMA ORTUNYA TERUS MASIH KULIAH, DIKIRA HADIAH ORANG NIKAHAN KALI YA.{/color}" with Pause(7.0)
        scene black with dissolve
        show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
        stop music fadeout 1.0
        scene black with dissolve
        play music "audio/Dreamcatcher_v2.mp3"
        jump credits

    elif kana_present == "CD Film Horror": #CD Film Horror
        $ quick_menu = False
        window auto hide
        with Pause(2.0)
        play sound "SFX - Plastic.wav" loop fadein 1.0
        window auto show
        show kana_home_side_shy_ahn at left with dissolve
        $ quick_menu = True
        kana "Udah boleh buka mata belum?"
        hide kana_home_side_shy_ahn with dissolve
        "[mcname!c]" "Bentar lagi."
        $ quick_menu = False
        window auto hide
        stop sound fadeout 1.0
        with Pause(2.0)
        show kana_home_side_shy_ahn at left with dissolve
        window auto show
        $ quick_menu = True
        kana "[mcname!c]?"
        hide kana_home_side_shy_ahn with dissolve
        "[mcname!c]" "Udah boleh buka matanya Nay."
        show kana_home_side_shy_ahn at left with dissolve
        kana "O-okee."
        hide kana_home_side_shy_ahn with dissolve
        "Perlahan Kana membuka matanya."
        $ quick_menu = False
        scene black with Dissolve(1.0)
        play music "BGM_Bad End.ogg" fadein 1.0
        scene kamar kana malam with Dissolve(1.0)
        show dvd at center
        show dvd:
                ypos 0.72 zoom 0.25 
        with dissolve
        $ quick_menu = True
        "Kana membuka dan melihat bahwa ada CD Blu-ray yang berjudul “The Conjurang” dengan cover yang gelap, mengerikan, dan ada hantunya."
        hide dvd
        hide kana_home_talk
        show kana_home_confused at kana_near
        with dissolve
        "[mcname!c]" "Ini film baru loh, katanya viral dan terinspirasi dari kisah nyata. Bisa kali ya kita nonton bareng-bareng nanti, jadi kita nobar gitu konsepnya hahah."
        show kana_home_side_confused at left with dissolve
        kana "Tapi… Aku ga suka horror. Ini cuma kesukaan kamu aja, kan?"
        hide kana_home_side_confused with dissolve
        "[mcname!c]" "I-iya sih tapi…"
        "Kana pun meminta maaf dan menolak hadiah dari [mcname!c]. Bahkan dia terlalu takut untuk menyimpan CD Blu-ray itu."
        hide kana_home_confused
        with dissolve
        $ quick_menu = False
        scene black with dissolve
        show text "{color=#FFF}ADUH BROOO LAIN KALI KALO MAU NGASIH HADIAH TUH HARUS MIKIRIN JUGA APA YANG DIA SUKA, JANGAN LU DOANG YANG SUKA.{/color}" with Pause(5.0)
        scene black with dissolve
        show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
        stop music fadeout 1.0
        scene black with dissolve
        play music "audio/Dreamcatcher_v2.mp3"
        jump credits

label truekanarightpresent:
    $ quick_menu = False
    window auto hide
    play sound "SFX - Plastic.wav" loop fadein 1.0
    with Pause(2.0)
    window auto show
    $ quick_menu = True
    "[mcname!c] mengambil kalung dan mulai memakaikannya ke leher Kana."
    "Kana yang merasakan sensasi dingin di lehernya, bertanya."
    show kana_home_side_shy_ahn at left with dissolve
    kana "E-eh ini apa?"
    hide kana_home_side_shy_ahn with dissolve
    "[mcname!c]" "Sabar-sabar. Aman kok, bukan yang aneh-aneh."
    show kana_home_side_shy_ahn at left with dissolve
    kana "Udah boleh buka mata belum?"
    hide kana_home_side_shy_ahn with dissolve
    "[mcname!c]" "Bentar lagi."
    $ quick_menu = False
    window auto hide
    stop sound fadeout 1.0
    with Pause(2.0)
    show kana_home_side_shy_ahn at left with dissolve
    window auto show
    $ quick_menu = True
    kana "E-eeeeeh."
    hide kana_home_side_shy_ahn with dissolve
    "[mcname!c]" "Udah boleh buka matanya Nay."
    show kana_home_side_shy_ahn at left with dissolve
    kana " O-okee."
    hide kana_home_side_shy_ahn with dissolve
    "Perlahan Kana membuka matanya."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kado Kana.ogg" fadein 2.0
    scene kana_gift_smile with Dissolve(2.0)
    $ quick_menu = True
    "Saat Kana membuka matanya, dia terlihat kaget dan terkejut karena di lehernya terdapat sebuah kalung cantik bersinar yang berwarna biru."
    "Ternyata sensasi dingin yang sebelumnya terasa, adalah kalung."
    show kana_gift_talk
    show kana_home_side_shy_eh at left
    with dissolve
    kana "EH INI KANN!!??"
    hide kana_gift_talk
    show kana_gift_smile
    hide kana_home_side_shy_eh
    with dissolve
    "[mcname!c]" "Selamat ulang tahun~!"
    hide kana_gift_smile
    show kana_gift_talk
    show kana_home_side_shy_eh at left
    with dissolve
    kana "EHH!!!?? K-kamu tau hari ulang tahun ku?"
    hide kana_gift_talk
    show kana_gift_smile
    hide kana_home_side_shy_eh
    with dissolve
    "[mcname!c]" "Tau doong. Sekali lagi, selamat ulang tahun Kanaia Asa~"
    "[mcname!c]" "Bagiku, kamu orang yang spesial. Jadi, aku pengen ngasih hadiah yang spesial juga."
    show kana_home_side_shy_ahn at left
    with dissolve
    kana "*BLUSH*"
    hide kana_gift_smile
    show kana_gift_talk
    show kana_home_side_shy_eh at left
    with dissolve
    kana "M-makasih banyak ya."
    hide kana_gift_talk
    show kana_home_side_shy_eh at left
    show kana_gift_smile
    hide kana_home_side_shy_ahn
    with dissolve
    "[mcname!c]" "Hehe, gimana Nay kamu suka?"
    hide kana_home_side_shy_eh
    hide kana_gift_smile
    show kana_gift_talk
    show kana_home_side_shy_eh at left
    with dissolve
    kana "BANGETTTT, aku suka pake banget. Kok kamu tau aku lagi pengen kalung sih?"
    hide kana_gift_talk
    show kana_gift_smile
    hide kana_home_side_shy_eh
    with dissolve
    "[mcname!c]" "Kita kan kemarin abis ke mall, terus aku liat kamu merhatiin toko perhiasan gitu."
    "[mcname!c]" "Jadinya aku beli kalung ini sambil bayangin kamu dan aku rasa kalung ini cocok buat kamu."
    hide kana_gift_smile
    show kana_gift_talk
    show kana_home_side_drylaugh at left
    with dissolve
    kana "Iiiiii makasih banyak yaa, [mcname!c]."
    hide kana_gift_talk
    show kana_gift_smile
    hide kana_home_side_drylaugh
    with dissolve
    "[mcname!c]" "Iya Kana..."
    hide kana_gift_smile
    show kana_gift_talk
    show kana_home_side_drylaugh at left
    with dissolve
    kana "Aduhhh. A-aku ga bisa berhenti senyum, ini bagus bangett."
    hide kana_gift_talk
    show kana_gift_smile
    hide kana_home_side_drylaugh
    with dissolve
    "[mcname!c]" "Bagus deh kalo kamu suka. Aku malah takut kamu ga suka dan jadi benci sama aku."
    hide kana_gift_smile
    show kana_gift_talk
    show kana_home_side_drylaugh at left
    with dissolve
    kana "Aku suka banget. Lagian ga usah ngasih pun gapapa kok. A-aku ga bakalan bisa benci kamu."
    hide kana_gift_talk
    hide kana_home_side_drylaugh
    show kana_gift_smile
    with dissolve
    "[mcname!c]" "Eeeehh."
    "[mcname!c]" "*Blush*"
    "[mcname!c]" "Ke-kenapa?"
    hide kana_gift_smile
    show kana_gift_talk
    show kana_home_side_confused_blush at left
    with dissolve
    kana "Soalnya..."
    hide kana_gift_talk
    show kana_gift_smile
    hide kana_home_side_confused_blush
    with dissolve
    "[mcname!c]" "........."
    show kana_gift_smile
    show kana_home_side_shy_hmph at left
    with dissolve
    kana "*Blush*"
    hide kana_gift_smile
    show kana_gift_talk
    hide kana_home_side_shy_hmph
    show kana_home_side_shy_ahn at left
    with dissolve
    kana "[mcname!c]... Sebenarnya aku suk-"
    $ quick_menu = False
    scene black
    hide kana_gift_talk
    hide kana_home_side_shy_ahn
    play sound "audio/SFX - Door Slam.WAV" volume (5.0)
    stop music
    window auto hide
    scene black
    with Pause(2.0)
    play music "audio/BGM_Funny 3.ogg" fadein 1.0
    scene kamar kana malam with Dissolve(2.0)
    show kana_home_confused_blush at kana_near_left_2
    show freya_shock at freya_near_right
    show freya_side_shock at left
    with dissolve
    window auto show
    $ quick_menu = True
    freya "HAPPY BIRTHDAYYY NAYAAAA~!!!!"
    hide freya_side_shock with dissolve
    "Tanpa angin tanpa hujan, tiba-tiba Freya datang membuka pintu kamar Kana."
    hide kana_home_confused_blush
    show kana_home_confused_blush_sideeye at kana_near_left_2
    hide freya_shock
    show freya_awe at freya_near_right
    with dissolve
    "Melihat ke arah Kana dan [mcname!c] yang sedang berduaan dan suasana yang terasa berbeda dari biasanya, membuat Freya pun tersadar."
    hide freya_awe
    show freya_shock at freya_near_right
    show freya_side_shock at left
    with dissolve
    freya "Eh? Sorry kayaknya ganggu, hehe."
    hide freya_side_shock
    hide kana_home_confused_blush_sideeye
    show kana_home_cry at kana_near_left_2
    show freya_side_shock at left
    with dissolve
    freya "Kalian lanjutin aja dulu berdua, hehe."
    show freya_side_smug at left
    hide freya_side_shock 
    hide freya_shock 
    show freya_smug at freya_near_right
    with dissolve
    freya "Hehe, aku pergi dulu baaay~"
    hide freya_side_shock
    hide freya_shock
    hide freya_smug 
    hide freya_side_smug
    with dissolve
    hide kana_home_cry with dissolve
    show kana_home_confused_blush at kana_near
    show kana_home_side_confused_blush at left
    with dissolve
    kana "F-FREEEEYYAAAAAAA~!"
    stop music fadeout 1.0
    kana "*Blush*"
    play music "BGM_Romance Kana.ogg" fadein 1.0
    show kana_home_shy at kana_near
    hide kana_home_side_confused_blush
    with dissolve
    "[mcname!c]" "Hahahahaha!"
    hide kana_home_confused_blush
    show kana_home_smile at kana_near
    show kana_home_side_shy_hmph at left
    with dissolve
    kana "Fufufufufu!!!"
    hide kana_home_side_shy_hmph
    hide kana_home_smile
    show kana_home_shy at kana_near
    with dissolve
    kana "*Blush*"
    "[mcname!c] dan Kana saling memandang sambil berbagi senyuman hangat."
    "Malam itu..."
    hide kana_home_shy
    show kana_home_smile at kana_near
    with dissolve
    "Menjadi malam yang tidak akan terlupakan bagi [mcname!c] dan Kana."
    hide kana_home_smile
    with dissolve
    $ quick_menu = False
    scene kana_gift_smile with Dissolve(1.0)
    stop music fadeout 1.0
    $ necklaces.grant()
    show text "{color=#000}THE END{/color}" with Pause(2.0)
    play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
    jump credits