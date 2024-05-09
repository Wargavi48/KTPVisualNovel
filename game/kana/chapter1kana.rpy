label chapter1kana1:
    $ renpy.block_rollback()
    scene dream with dissolve
    mcname "huuuu, ini hari pertama gw orientasi di Jeketi University"
    mcname "di sini tempat dimana gw bakalan kenal sama orang baru, temen baru, atau bahkan jodoh heheh"
    scene depan kampus with dissolve
    "MC memasuki aula"
    "Saat memasuki ruangan MC mendengar suara aula yang sangat ramai"
    mcname "Seperti yang diharapkan dari kampus ibu kota, orang nya rame banget"
    "Saat memperhartikan sekitar [mcname] mendengar suatu topik yang menarik perhatiannya"
    "Mahasiswa A" "Eh eh liat deh itu kan mahasiswi itu"
    "Mahasiswa B" "Yang mana sih?"
    "Mahasiswa A" "ituuu, yang ituu tuhh"
    "Pembicaraan mereka yang cukup keras membuat MC pun melirik ke arah orang yang menjadi bahan pembicaraan"
    "Mahasiswa B" "Owhhh dia!!, eh bukanya dia mahasiswa yang….bla bla bla"
    "Disaat itupun juga mc terpana  dan mencoba untuk memfokuskan matanya fokus terhadap bahan pembicaraan para mahasiswa itu"
    "seorang wanita muda yang memiliki rambut berwarna biru muda yang mengingatkan nya kepada lautan"
    "dan juga matanya yang seindah batu sapphire, serta tas dan sepatunya yang ber brand membuat [mcname] terdiam"
    mcname "Dia siapa"
    mcname "Ko banyak di gosipin sama mahasiswa baru ya"
    mcname "tapi diliat-liat cantik anggun, kalem banget dah sumpah kalau di liat liat mah"
    mcname "ko ada ya orang se cantik dia, atau emng semua orang dari kota itu kaya gitu"
    mcname "pasti dia orangnya kalem, sopan, pinter dan hobinya juga baca buku"
    "[mcname] pun melihat ke arah sekelilingnya"
    mcname "Hmmm emng si hampir semua keliatan cantik"
    mcname "tapiii ko cuma dia ya yang jadi perhatian orang-orang..ya termasuk aku juga si"
    $ quick_menu = False
    scene black with dissolve
    scene depan kampus with dissolve
    "Rektor" " selamat datang mahasiswa baru yang memasuki Jekiti university bla bla bla…"
    "Perkataan sambutan dari rektor dan jajaran dosen membuat MC dan beberapa mahasiswa/i lain merasa bosan"
    "Seakan mendukung perkatan MC, beberapa mahasiswa pun ada yang bermain hp, mengobrol bahkan bercanda"
    "Mahasiswa A" "eh bosenin bet dah, template banget ini ucapan selamat datangnya tuh, bikin ngatuk ya ga ?"
    "Mahasiswa B" "Iyaa njirr, bener banget dah mending kita login yuk P MOLE MOLE"
    "Mahasiswa C" "Gas kali ya login"
    "Obrolan dari mahasiswa tersebut sesekali mengalihkan perhatian [mcname]"
    "Akan tetapi, pandangannya sekali lagi teralihkan saat kana  tersenyum tipis dan tanganya yang berusaha menutupi senyumannya"
    mcname "Akhirnya selesai juga sambutan dan kegiatan hari ini"
    "[mcname] merengangkan badannya yang terasa kaku akibat duduk terlalu lama"
    mcname "Eh masih jam segini mayan cape juga ya hari ini tapi masih ada energi si"
    # insert cg kana
    mcname "Aduhhh ko gw ga bisa ilangin senyuman itu dari kepala gw ya ?"
    mcname "Apa jangan jangan gw kena santet lagi nih?"
    mcname "Ah masa sih, lagian kan dia emang cantik jadi pantes dong kalau gw suka hehe"
    mcname "Eh masih jam segini nih enaknya buat habisin waktu mending gw"
    $ quick_menu = False
    menu:
        "Mau Kemana?"
        "A. Ke Kosan":
            "Kamu habisin waktu di kosan dan memilih buat istirahatin diri daripada pergi kesana kemari"
        "B. Ke Warteg":
            "Kamu milih makan ke warteg dan di situ ternyata wartegnya pake boraks dan akhirnya kamu masuk rumah sakit"
            scene black with dissolve
            show text "{color=#FFF}MAKANYA JANGAN MAKAN SEMBARANG BROO KAN MASUK RUMAH SAKIT{/color}" with Pause(2.0)
        "C. Ke Cafe":
            $ quick_menu = False
            scene black with dissolve
            jump chapter1kana2Cafe
            
    
label chapter1kana2Cafe:
    "Ramainya orang orang yang lalu lalang di luar cafe dan memasuki cafe pun terkadang menarik perhatian si MC akan tetapi ada satu orang yang membuat dia semakin fokus"
    "Saat orang itu mendekati pintu cafe MC pun menyadari bahwa orang itu adalah Kana"
    mcname "Anjir ko ada CEWEK ITU di sini, bukannya cewek itu yang katanya anak orang kaya, yang sepupunya rektor itu kan"
    mcname "ko dia masuk ke cafe ini anjir anjir dia"
    mcname "CANTIK BANGET CUYYYY"
    mcname "Stay cool…stay cool…eh tapi ko dia liat sana sini dah ?"
    mcname "Kenapa ya?"
    mcname "Samperin kali ya?"
    mcname "Ehhh tapi jangan deh stay cool aja"
    # play music "audio/Dreamcatcher.mp3"
    # jump credits


# label chapter1kana2Campus:
