label truepia:
    "Pia yang mendapat semangat dari [mcname] pun makin membulatkan tekad untuk tetap melanjutkan melukis dan membuat gambar."
    $ renpy.block_rollback()
    $ quick_menu = True
    show pia_side at left with dissolve
    pia "Huahaha! Saatnya kamu kubawa ke dunia ilustrator yang biasa aku jalani selama ini."
    hide pia_side with dissolve
    mcname "Gimana?"
    show pia_side at left with dissolve
    pia "Kamu udah denger nama \"Yang Mulia Piaraan\" kan?"
    hide pia_side with dissolve
    mcname "Gatau kenapa, selalu mau ketawa tiap denger nama itu deh"
    show pia_side at left with dissolve
    pia "HEH! DIEM! AHAHAHA!!"
    hide pia_side with dissolve
    mcname "Yup, sampe sini aku udah tau."
    show pia_side at left with dissolve
    pia "Nah, jadi sebelum aku masuk ke dunia perkuliahan ini, aku aktif banget bikin gambar."
    pia "Nerima commision dari orang-orang buat gambar, sampe jualan hasil karyaku di event-event jejepangan gitu."
    hide pia_side with dissolve
    mcname "Hoooooo, keren juga kamu. Terus kalo sekarang?"
    show pia_side at left with dissolve
    pia "Sekarang lagi vakum dulu. Sibuk kuliah gini, gimana waktu sendirinya weh!"
    hide pia_side with dissolve
    mcname "Hahaha, bener juga."
    show pia_side at left with dissolve
    pia "Padahal di komunitas itu aku cukup dikenal dan menurutku gak sedikit yang tau pen-nameku itu."
    hide pia_side with dissolve
    mcname "Hmmmm???\n*melirik ragu*"
    show pia_side at left with dissolve
    pia "Beneran weh!!! Bukannya narsis yaa! Tapi ya gitu, nih liat.\n*Ngasih liat akun twitternya*"
    hide pia_side with dissolve
    mcname "Woooow gila, artis banget nih! Followernya sampe puluhan ribu gitu. Kamu…."
    show pia_side at left with dissolve
    pia "GAK YA! KAMU MAU BILANG BELI FOLLOWER KAN?! ENGGA!"
    hide pia_side with dissolve
    mcname "Cih ketauan, ahahaha."
    show pia_side at left with dissolve
    pia "Heeeeh… kebaca pikiranmu! Haha."
    pia "…………"
    pia "Ya gitu lah… ilang motivasiku buat lanjut gambar gini…."
    hide pia_side with dissolve
    mcname "Weh kenapa?"
    mcname "Bukannya itu salah satu yang udah ngembangin namamu dan ngebuat kamu jadi yang kayak sekarang ini?"
    mcname "Mau dibuang gitu aja?"
    show pia_side at left with dissolve
    pia "Huhuhu engga sih, kayak art block aja."
    pia "Hilang aja semangatnya."
    hide pia_side with dissolve
    mcname "Hmm... Oke, gimana cara aku bisa semangatin biar kamu bisa kayak dulu lagi?"
    show pia_side at left with dissolve
    pia "Temenin aku"
    hide pia_side with dissolve
    mcname "Ke mana?"
    show pia_side at left with dissolve
    pia "Temenin aku terus sampe sukses. *Blush*"
    hide pia_side with dissolve
    mcname "Ummm… Gak nyangka kamu bakal ngomong gitu, bingung aku balesnya.\n*Blush*"
    show pia_side at left with dissolve
    pia "GIMANA…IH MALU KAN AKU JADINYA"
    hide pia_side with dissolve
    mcname "Oke, deal!"
    show pia_side at left with dissolve
    pia "Hehehe, okeh deal!!!"
    hide pia_side with dissolve
    "[mcname] dan Pia pun pulang ke rumah masing-masing"
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with dissolve
    show text "{color=#FFF}DI KOSAN{/color}" with Pause(2.0)
    scene mc bedroom with dissolve
    play music "audio/BGM_Kosan 2.mp3" fadein 1.0
    $ renpy.block_rollback()
    $ quick_menu = True
    mcname "*Sedang menggambar*"
    $ quick_menu = False
    nvl clear 
    pia_nvl "[mcname]!!"
    pia_nvl "P"
    pia_nvl "P"
    mc_nvl "Ya?"
    pia_nvl "Lagi apa?"
    mc_nvl "Gak ngapa-ngapain, cuma lagi sketch-sketch kecil aja"
    pia_nvl "Iiih mau liaaaat"
    mc_nvl "*Ngirim foto sketch Pia*"
    pia_nvl "!!!!!"
    pia_nvl "itu aku?"
    pia_nvl "AKU???"
    pia_nvl "AWWWWWW CO CWITTT"
    mc_nvl "Bawel"
    pia_nvl "Tumben, lagi mikirin aku ya sampe gambar aku gitu"
    mc_nvl "???"
    pia_nvl "Candaaa~"
    pia_nvl "Tapi beneran deh dalam rangka apa nih."
    mc_nvl "Enggak, cuma pengen aja ngelatih gambarku biar bisa jadi supportnya kamu."
    pia_nvl "AWWWWWW"
    mc_nvl "Gue block nih."
    pia_nvl "Iya iya, engga ngeledekin lagi. Ahahaha"
    mc_nvl "Alias, tumben ngechat duluan."
    mc_nvl "Ada yang mau diomongin kah?"
    pia_nvl "Bosen, mau chatting aja"
    pia_nvl "Ga mau chatting sama aku? UwU"
    menu:
        "Respon Kamu?"
        "Iye iye mau. Nih gue buka obrolan ya. Lagi ngapain Kak Pia?":
            mc_nvl "Iye iye mau."
            mc_nvl "Nih gue buka obrolan ya."
            mc_nvl "Lagi ngapain Kak Pia?"
            pia_nvl "Lagi boboan aja ini di kasur, hehe."
            pia_nvl "[mcname], main game yuk."
            mc_nvl "Game apa?"
            pia_nvl "Umm…"
            pia_nvl "Benar atau bohong."
            mc_nvl "Menarik"
            mc_nvl "Gimana jadinya?"
            pia_nvl "Ya tebak aja, ini beneran apa bohongan."
            mc_nvl "O-oke…"
            pia_nvl "Aku sahabat bestie banget sama Cepio"
            mc_nvl "Benar!"
            pia_nvl "O"
            pia_nvl "Cepio jelek."
            mc_nvl "???"
            mc_nvl "Ada gilanya."
            mc_nvl "Bohong"
            pia_nvl "O"
            pia_nvl "Strawberry cake cafe xxxx enak banget."
            mc_nvl "Benar!"
            pia_nvl "O"
            pia_nvl "Pas aku makan strawberry cake pas itu, kamu ngeliatin aku terus."
            mc_nvl "???"
            mc_nvl "Bohong"
            pia_nvl "X"
            pia_nvl "Aku Imut"
            mc_nvl "Hmm…"
            pia_nvl "???"
            pia_nvl "*send foto*"
            mc_nvl "Waduh."
            pia_nvl "Jadi?"
            mc_nvl "Benar..."
            pia_nvl "Hehehe"
            mc_nvl "Dah aku mau tidur ah"
            pia_nvl "Bohong."
            mc_nvl "O"
            pia_nvl "Hahaha maaci dah nemenin. Met bobo."
            mc_nvl "Iya Pia, met bobo juga."
            "Malam itu terasa panjang sekali, sambil melanjutkan sketsa yang dibuat [mcname] dengan wajah yang memerah."
            "Hari itu berakhir dengan kekalahan [mcname]."
            $ quick_menu = False
            stop music fadeout 1.0
            scene black with dissolve
            show text "KEEESOKAN HARINYA" with Pause(2.0)
            jump trueendrooftoppia
        "Udah kemaleman tapi weh, aku mau tidur juga bentar lagi ini":
            mc_nvl "Udah kemaleman tapi weh"
            mc_nvl "Aku mau tidur juga bentar lagi ini"
            pia_nvl "Ah oke yaudah deh"
            stop music fadeout 1.0
            show text "{color=#FFF}Udah gitu doang aja{/color}" with Pause(2.0)
            show text "{color=#FFF}Kenapa?{/color}" with Pause(2.0)
            show text "{color=#FFF}Soalnya di docs cerita author cuma nulis sampe mau tidur{/color}" with Pause(2.0)
            show text "{color=#FFF}Cerita pun berhenti karena dev gak ada ide{/color}" with Pause(2.0)
            show text "{color=#FF0000}BAD END{/color}"
            play music "audio/Dreamcatcher.mp3" fadein 1.0
label trueendrooftoppia:
    scene rooftop with dissolve
    show pia at pia_near with dissolve
    play music "audio/BGM_Rooftop Romance Pia.mp3" fadein 1.0
    $ renpy.block_rollback()
    $ quick_menu = True
    mcname "Pia, ini aku lupa ngasih ini. Ada flyer acara jejepangan"
    show pia_side at left with dissolve
    pia "Hmm... Menarik"
    pia "Eh."
    pia "EH!! [mcname]!!!"
    hide pia_side with dissolve
    mcname "Apa?"
    show pia_side at left with dissolve
    pia "Ini ada bagian kreator."
    pia "Yuk ikutan jualan!!!"
    hide pia_side with dissolve
    mcname "Heeeeee"
    show pia_side at left with dissolve
    pia "Katanya mau support aku…"
    hide pia_side with dissolve
    mcname "Iya… Tapi aku ga pernah jualan gambar, terus ga tau mau bikin apa."
    show pia_side at left with dissolve
    pia "Tenang, kamu bersama sepuh di sini. 1 booth bareng yuk."
    hide pia_side with dissolve
    mcname "Ya… Oke aja sih."
    show pia_side at left with dissolve
    pia "Hmm acara jejepangannya masih 3 bulan lagi"
    pia "Bisa lah ini 2 bulan buat banyak merch."
    hide pia_side with dissolve
    mcname "Oke"
    show pia_side at left with dissolve
    pia "Kamu daftarin gih cepet."
    hide pia_side with dissolve
    mcname "Nama boothnya?"
    show pia_side at left with dissolve
    pia "Hmmm… Bener juga, apa ya."
    hide pia_side with dissolve
    mcname "Gimana kalo \"Yang Mulia dan Piaraan\"."
    show pia_side at left with dissolve
    pia "Ahahaha kamu jadi peliharaan?"
    hide pia_side with dissolve
    mcname "Biar lucu aja sih"
    show pia_side at left with dissolve
    pia "Selama aku jadi lebih superior dari kamu, aku setuju. Gas!!!"
    hide pia_side with dissolve
    "Akhirnya [mcname] mendaftarkan diri ke event jejepangan tersebut dengan nama circle \nYang Mulia dan Piaraan\n."
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}MALAM HARINYA DI KOS{/color}" with Pause(2.0)
    scene mc bedroom with dissolve
    play music "audio/BGM_Happy dan Handphone.mp3" fadein 1.0
    nvl clear
    pia_nvl "P"
    pia_nvl "P"
    pia_nvl "P"
    pia_nvl "[mcname]!!!"
    mc_nvl "......"
    mc_nvl "Apa?"
    pia_nvl "Hehehe"
    mc_nvl "Apaan?"
    pia_nvl "Besok ke kosan aku sini"
    mc_nvl "HAH? GIMANA?"
    pia_nvl "GAUSAH ANEH ANEH"
    pia_nvl "BANTUIN GAMBAR BUAT MERCH LOOOH."
    mc_nvl "OOOOH"
    pia_nvl "KAMU MIKIR APA??"
    mc_nvl "ENGGA"
    mc_nvl "OKE BESOK SIANGAN YA."
    pia_nvl "OKE, GAK ADA KELAS KAN BESOK."
    mc_nvl "IYA"
    mc_nvl "BTW"
    mc_nvl "KENAPA JADI CAPSLOCK SEMUA"
    pia_nvl "HAHAHAHAHAHAHA"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}KEESOKAN HARINYA{/color}" with Pause(2.0)
    play music "audio/BGM_Happy dan Handphone.mp3" fadein 1.0
    scene mc bedroom with dissolve
    nvl clear
    pia_nvl "[mcname]!!!"
    pia_nvl "{image=location.png}"
    mc_nvl "?"
    pia_nvl "Alamat kosan aku. Buruan sini, bantuin."
    mc_nvl "Sekarang?"
    pia_nvl "Iyaaaaa, mumpung lagi semangat gambar."
    pia_nvl "Bawa laptop, sambil brainstorming kita."
    mc_nvl "O-oke"
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with dissolve
    show text "{color=#FFF}DI DEPAN KOSAN PIA{/color}" with Pause(2.0)
    scene depan kosan with dissolve
    play music "audio/BGM_Happy dan Handphone.mp3" fadein 1.0
    nvl clear
    mc_nvl "Oiii, depan."
    pia_nvl "Okeh wait, aku keluar."
    stop music fadeout 1.0
    play sound "audio/open_door.mp3"
    scene black with dissolve
    show text "{color=#FFF}DI DALEM KOSAN PIA{/color}" with Pause(2.0)
    # Harusnya BG Kosan Pia
    scene mc bedroom with dissolve
    play music "audio/BGM_Romance Pia Kamar.mp3" fadein 1.0
    show pia at pia_near with dissolve
    show pia_side at left with dissolve
    $ quick_menu = True
    pia "Ngapain diem aja, duduk bawah? Keluarin laptop."
    hide pia_side with dissolve
    mcname "OTW"
    show pia_side at left with dissolve
    pia "Jadi gini, aku mau bikin merch gantungan kunci, stiker, poster."
    pia "Kamu ada ide gak?"
    hide pia_side with dissolve
    menu:
        mcname "Ummm...."
        "Pin sama postcard?":
            mcname "Pin sama postcard?"
            jump gambardikosanpia

        "Gak ada ide, ngikut aja.":
            mcname "Gak ada ide, ngikut aja."

label gambardikosanpia:
    show pia_side at left with dissolve
    pia "Hmm… menarik, oke jadi untuk yang mau aku gambar dari fandom anime AK0047 sama dari Keluarga Mata-Mata, ada ide gak?"
    hide pia_side with dissolve
    mcname "Kalo yang lagi rame sih dari anime My Deer Friend Kana-tan, gimana?"
    show pia_side at left with dissolve
    pia "Menarik, boleh. Kamu gambar itu ya."
    hide pia_side with dissolve
    mcname "Bentar, ini gambarnya gimana? Aku full? Gambarku ga bagus weh."
    show pia_side at left with dissolve
    pia "Oh iya, jadi gini. Aku gambar lineart, kamu coloring. nanti finishingnya aku."
    hide pia_side with dissolve
    mcname "Deal!!!"
    show pia_side at left with dissolve
    pia "Nanti kita dibantu Cepio sama temennya, mereka ikut jualan juga di booth kita."
    hide pia_side with dissolve
    mcname "Woaaaaa, baru nih."
    show pia_side at left with dissolve
    pia "Iya, soalnya pas diliat liat harga boothnya kalo kita berdua aja agak mahal."
    pia "Terus nanti terlalu sepi kalo kita doang yang display."
    pia "Jadi Cepio juga ikutan biar rame meja booth kita."
    hide pia_side with dissolve
    mcname "Okeeee, mantaaaaap."
    show pia_side at left with dissolve
    pia "Oke, ini aku konsepin gambar ini ya."
    hide pia_side with dissolve
    "Pia pun mulai membuat sketsa dan memberikan arahan ke MC untuk membantunya"
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}4 JAM KEMUDIAN{/color}" with Pause(2.0)
    # Harusnya Kosan Pia
    scene mc bedroom with dissolve
    show pia at pia_near with dissolve
    show pia_side at left with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    pia "WEEEEH UDAH GELAP AJA INI DI LUAR! GAK SADAR!"
    hide pia_side with dissolve
    mcname "Lah iya udah malem ya, hahaha gak terasa ya. fokus banget kita."
    show pia_side at left with dissolve
    pia "LAPER. MAKAN."
    hide pia_side with dissolve
    mcname "Mau mesen NERUFOOD apa keluar aja kita nyari makan?"
    show pia_side at left with dissolve
    pia "Mesen NERUFOOD aja ah, males keluar keluar lagi."
    hide pia_side with dissolve
    mcname "Okeh, mesen ini gimana?\n*Ngeliatin menu di aplikasi NERUFOOD*"
    show pia_side at left with dissolve
    pia "Hmmm… Enak kayaknya. Oke sung buruaaaan, lapeeer."
    hide pia_side with dissolve
    mcname "Iya sabaaaar."
    show pia_side at left with dissolve
    pia "Huahahahaha"
    pia "Eh aku ke toilet dulu"
    hide pia_side with dissolve
    mcname "Iya"
    hide pia with dissolve
    "[mcname] pun termenung duduk melihat ke sekeliling kamar Pia"
    "[mcname] menyadari bahwa di kosannya banyak sekali pajangan dan merch fanart buatannya."
    mcname "{i}Pia ambis juga ya, keliatan dari schedule kuliah yang terpajang rapih di sticky notes meja belajarnya dan banyaknya sketsa bertumpuk di sudut-sudut ruangan.{/i}"
    mcname "{i}Err… Agak berantakan sih, haha.{/i}"
    "[mcname] pun menyadari betapa mandirinya Pia dalam beberapa situasi, walaupun Pia selalu terlihat sebagai pribadi yang supel, mudah bergaul dengan banyak orang"
    "Namun dibalik itu semua tidak ada yang benar-benar mengenal Pia seutuhnya. Namun dengan adanya [mcname], Pia seperti menemukan cahaya baru untuk memulainya kembali."
    show pia at pia_near with dissolve
    show pia_side at left with dissolve
    pia "Kamu gak buka lemari-lemari aku kan??!!"
    hide pia_side with dissolve
    mcname "Pi, yang bener aja……"
    show pia_side at left with dissolve
    pia "Siapa tau kan?"
    hide pia_side with dissolve
    "???" "NERUFOOD~"
    mcname "Oh dah sampe tuh, aku ambil ya."
    show pia_side at left with dissolve
    pia "Iyaaaaa"
    hide pia_side with dissolve
    "Pia dan [mcname] pun melanjutkan makan di kosan"
    show pia_side at left with dissolve
    pia "WUOHHH!!! Enak."
    hide pia_side with dissolve
    mcname "Ya kan?"
    show pia_side at left with dissolve
    pia "MAO COBA YANG KAMU"
    hide pia_side with dissolve
    "Pia mendadak langsung mengambil sesendok makanan [mcname]."
    show pia_side at left with dissolve
    pia "WUOHHHH ENAKKK JUGAA"
    hide pia_side with dissolve
    mcname "Hadeehh. Pelan-pelan, Pia."
    show pia_side at left with dissolve
    pia "UHUK!! UHUK!! UHUK!!!"
    hide pia_side with dissolve
    mcname "Kaaaaaaaaaaan…"
    mcname "Nih minum dulu."
    show pia_side at left with dissolve
    pia "*Glug Glug*"
    pia "Ahhhhh!"
    pia "Makasih [mcname]"
    hide pia_side with dissolve
    mcname "Iyaaa. Yauda sana lanjut makannya"
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}SESUDAH MAKAN{/color}" with Pause(2.0)
    # Harusnya Kosan Pia
    scene mc bedroom with dissolve
    show pia at pia_near with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    mcname "Udah malem nih. Aku pulang dulu ya."
    show pia_side at left with dissolve
    pia "Yahhh…"
    hide pia_side with dissolve
    mcname "Ga bisa sampe malem banget, soalnya besok UTS."
    show pia_side at left with dissolve
    pia "Yaudaah. Hati-hati di jalan~"
    hide pia_side with dissolve
    "Setelah itu, [mcname] pun kembali ke kosannya."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}DI KOSAN [mcname]{/color}" with Pause(2.0)
    scene mc bedroom with dissolve
    play music "audio/BGM_Kosan 2.mp3" fadein 1.0
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname] pulang, duduk di meja belajarnya sambil mulai mengeluarkan buku-buku dan catatan materi ujian esok hari."
    "[mcname] bersiap begadang untuk fokus belajar karena besok adalah salah satu ujian mata kuliah tertulis yang paling sulit."
    play sound "audio/ReceiveText.ogg" 
    stop music fadeout 1.0
    mcname "......"
    $ quick_menu = False
    play music "BGM_Happy dan Handphone.mp3" fadein 1.0
    nvl clear
    pia_nvl "Tidur?"
    mc_nvl "Gak lah. Begadang, belajar"
    pia_nvl "Asik, sama sih ahahaha"
    pia_nvl "Sambil ngechat dong dikit dikit biar gak sepi :(("
    mc_nvl "Okeeee, sampe ketiduran ya"
    pia_nvl "Pasang alarm dulu!"
    mc_nvl "Siaaap"
    stop music fadeout 1.0
    scene black with dissolve
    show text "{color=#FFF}KEESOKAN HARINYA{/color}" with Pause(2.0)
    scene kelas with dissolve
    play music "audio/BGM_Dosen + Rektor.mp3" fadein 1.0
    show dosen at dosen_center with dissolve
    show dosen_side at left with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    dosen "Pagi!!"
    dosen "Semua buku dan HP simpan di depan ya."
    dosen "Di atas meja hanya boleh ada alat tulis"
    dosen "Ujian kita mulai 10 menit lagi."
    "Mahasiswa/i" "Baik buu~"
    $ quick_menu = False
    jump quiz

label truepiaafterquiz:
    "Setelah Quiz True Ending Route"
    