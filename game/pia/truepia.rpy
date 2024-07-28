label truepia:
    "Pia yang mendapat semangat dari [mcname] pun makin membulatkan tekad untuk tetap melanjutkan melukis dan membuat gambar."
    #$ renpy.block_rollback()
    $ quick_menu = True
    show pia at pia_near with dissolve
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Huahaha! Saatnya kamu kubawa ke dunia ilustrator yang biasa aku jalani selama ini."
    hide pia_talk 
    hide pia_side_talk
    with dissolve 
    mcname "Gimana?"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve 
    pia "Kamu udah denger nama \"Yang Mulia Piaraan\" kan?"
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    mcname "Gatau kenapa, selalu mau ketawa tiap denger nama itu deh."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "HEH! DIEM! AHAHAHA!!"
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    mcname "Yup, sampe sini aku udah tau."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Nah, jadi sebelum aku masuk ke dunia perkuliahan ini, aku aktif banget bikin gambar."
    pia "Nerima commision dari orang-orang buat gambar, sampe jualan hasil karyaku di event-event jejepangan gitu."
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    mcname "Hoooooo, keren juga kamu. Terus kalo sekarang?"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Sekarang lagi vakum dulu. Sibuk kuliah gini, gimana waktu sendirinya weh!"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    mcname "Hahaha, bener juga."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Padahal di komunitas itu aku cukup dikenal dan menurutku gak sedikit yang tau pen-nameku itu."
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    mcname "Hmmmm???\n*melirik ragu*"
    show pia_talk at pia_near 
    show pia_side_talk at left
    with dissolve
    pia "Beneran weh!!! Bukannya narsis yaa! Tapi ya gitu, nih liat.\n*Ngasih liat akun twitternya*"
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    mcname "Woooow gila, artis banget nih! Followernya sampe puluhan ribu gitu. Kamu…."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "GAK YA! KAMU MAU BILANG BELI FOLLOWER KAN?! ENGGA!"
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    mcname "Cih ketauan, ahahaha."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Heeeeh… kebaca pikiranmu! Haha."
    pia "…………"
    pia "Ya gitu lah… ilang motivasiku buat lanjut gambar gini…."
    hide pia_talk 
    hide pia_side_talk
    hide pia_side
    with dissolve
    mcname "Weh kenapa?"
    mcname "Bukannya itu salah satu yang udah ngembangin namamu dan ngebuat kamu jadi yang kayak sekarang ini?"
    mcname "Mau dibuang gitu aja?"
    show pia_talk at pia_near 
    show pia_side_talk at left
    with dissolve
    pia "Huhuhu engga sih, kayak art block aja."
    pia "Hilang aja semangatnya."
    hide pia_talk
    hide pia_side_talk
    with dissolve
    mcname "Hmm... Oke, gimana cara aku bisa semangatin biar kamu bisa kayak dulu lagi?"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Temenin aku"
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    mcname "Ke mana?"
    show pia_shock at pia_near
    show pia_side_shock at left
    with dissolve
    pia "Temenin aku terus sampe sukses. *Blush*"
    hide pia_shock
    hide pia_side_shock
    with dissolve
    mcname "Ummm… Gak nyangka kamu bakal ngomong gitu, bingung aku balesnya.\n*Blush*"
    show pia_silent at pia_near 
    show pia_side_silent at left
    with dissolve
    pia "GIMANA…IH MALU KAN AKU JADINYA!!"
    hide pia_silent 
    hide pia_side_silent
    with dissolve
    mcname "Oke, deal!"
    show pia_smile at pia_near 
    show pia_side_smile at left
    with dissolve
    pia "Hehehe, okeh deal!!!"
    with dissolve
    hide pia
    hide pia_smile
    hide pia_side_smile
    with dissolve
    "Akhirnya [mcname] duduk di sebelah Pia sambil melihat pemandangan dari rooftop melihat jauh ke depan."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Sore.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    # #$ renpy.block_rollback()
    $ quick_menu = True
    "Tak terasa hari sudah menjadi sore."
    "[mcname] dan Pia pun pulang ke kost masing-masing."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" fadein 1.0 volume (0.8)
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Di kost..."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(2.0)
    #$ renpy.block_rollback()
    $ quick_menu = True
    mcname "*Sedang menggambar*"
    play sound "ReceiveText.ogg" loop volume (2.0)
    "Tiba-tiba terdengar notifikasi chat."
    stop sound
    stop music fadeout 1.0
    mcname "{i}Siapa nih ngespam?{/i}"
    $ quick_menu = False
    play music "BGM_Happy + HP.ogg" fadein 1.0 volume (2.0)
    nvl clear 
    pia_nvl "[mcname!u]!!"
    pia_nvl "P"
    pia_nvl "P"
    mc_nvl "Ya?"
    pia_nvl "Lagi apa?"
    mc_nvl "Gak ngapa-ngapain, cuma lagi sketch-sketch kecil aja"
    pia_nvl "Iiih mau liaaaat"
    mc_nvl "*Ngirim foto sketch Pia*"
    pia_nvl "!!!!!"
    pia_nvl "Itu aku?"
    pia_nvl "AKU???"
    pia_nvl "AWWWWWW CO CWITTT~"
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
    scene kamar mc kota with dissolve
    $ quick_menu = True
    menu:
        "Respon kamu?"
        "Iye iye mau. Nih gue buka obrolan ya. Lagi ngapain Kak Pia?":
            $ quick_menu = False
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
            stop music fadeout 1.0
            play music "audio/BGM_Kosan 1.ogg" fadein 1.0 volume (0.8)
            scene kamar mc kota with dissolve
            $ quick_menu = True
            "Malam itu terasa panjang sekali, sambil melanjutkan sketsa yang dibuat [mcname] dengan wajah yang memerah."
            "Hari itu berakhir dengan kekalahan [mcname]."
            $ quick_menu = False
            stop music fadeout 1.0
            scene black with Dissolve(1.0)
            jump trueendrooftoppia
        "Udah kemaleman tapi weh, aku mau tidur juga bentar lagi ini":
            $ quick_menu = False
            stop music fadeout 1.0
            play music "BGM_Bad End.ogg" fadein 1.0
            mc_nvl "Udah kemaleman tapi weh."
            mc_nvl "Aku mau tidur juga bentar lagi ini."
            pia_nvl "Ah oke yaudah deh."
            scene black with dissolve
            show text "{color=#FFF}Udah gitu doang aja{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FFF}Kenapa?{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FFF}Soalnya di docs cerita author cuma nulis sampe mau tidur{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FFF}Cerita pun berhenti karena dev gak ada ide{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FF0000}BAD END{/color}" with Pause (2.0)
            scene black with dissolve
            stop music fadeout 1.0
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits
label trueendrooftoppia:
    play music "BGM_Pagi Siang.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya..."
    $ quick_menu = False
    scene depan kampus with Dissolve(2.0)
    $ quick_menu = True
    mcname "{i}Hmm? Apa ini di tas?{/i}"
    #SHOW ASSET NUE
    mcname "{i}Oalaah, kemarin aku lupa ngasih flyer ke Pia.{/i}"
    mcname "{i}Ah yaudah, nanti juga ketemu.{/i}"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Sore.ogg" fadein 1.0
    scene lorong sore with Dissolve(1.0)
    show pia at pia_near with dissolve
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    $ quick_menu = True
    pia "Ah! [mcname]!"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    mcname "Pii, udah beres kelasnya?"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Udah, hehe."
    pia "Ke rooftop yuk!"
    hide pia_talk 
    hide pia_side_talk
    mcname "Gasss~"
    hide pia with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Rooftop Sore.ogg" fadein 1.0
    scene rooftop sore with Dissolve(1.0)
    show pia at pia_near with dissolve
    $ quick_menu = True 
    #$ renpy.block_rollback()
    mcname "Pia, ini kemarin aku lupa ngasih ini. Ada flyer acara jejepangan."
    #ASSET FLYER JEJEPANGAN
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Hmm... Menarik."
    pia "Eh."
    pia "EH!! [mcname]!!!"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    mcname "Apa?"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Ini ada bagian kreator."
    pia "Yuk ikutan jualan!!!"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    mcname "Heeeeee"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Katanya mau support aku…"
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    mcname "Iya… Tapi aku ga pernah jualan gambar, terus ga tau mau bikin apa."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Tenang, kamu bersama sepuh di sini. 1 booth bareng yuk."
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    mcname "Ya… Oke aja sih."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Hmm acara jejepangannya masih 3 bulan lagi"
    pia "Bisa lah ini 2 bulan buat banyak merch."
    hide pia_talk
    hide pia_side_talk
    with dissolve
    mcname "Oke"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Kamu daftarin gih cepet."
    hide pia_talk
    hide pia_side_talk
    with dissolve
    mcname "Nama boothnya?"
    show pia_talk at pia_near
    show pia_side_talk at left 
    with dissolve
    pia "Hmmm… Bener juga, apa ya."
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    mcname "Gimana kalo \"Yang Mulia dan Piaraan\"."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Ahahaha kamu jadi piaraan?"
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    mcname "Biar lucu aja sih."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Selama aku jadi lebih superior dari kamu, aku setuju. Gas!!!"
    hide pia
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "Akhirnya [mcname] mendaftarkan diri ke event jejepangan tersebut dengan nama circle: \n~Yang Mulia dan Piaraan~\n"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" fadein 1.0 volume (0.8)
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Malam itu di kosan..."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(2.0)
    play sound "ReceiveText.ogg" loop volume (2.0)
    window auto hide
    pause(1.0)
    window auto show
    $ quick_menu = True
    stop sound
    mcname "{i}Hadeh, yang ngespam gini sih...{/i}"
    stop music fadeout 1.0
    mcname "{i}Pasti Si Pia lagi nih.{/i}"
    $ quick_menu = False
    window auto hide
    stop music fadeout 1.0
    pause(1.0)
    $ quick_menu = False
    play music "BGM_Happy + HP.ogg" fadein 1.0 volume (2.0)
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
    scene black with Dissolve(1.0)
    play music "BGM_Pagi Siang.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya..."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(2.0)
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
    scene black with Dissolve(1.0)
    scene depan kosan with Dissolve(1.0)
    nvl clear
    mc_nvl "Oiii, depan."
    pia_nvl "Okeh wait, aku keluar."
    nvl clear
    stop music fadeout 1.0
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    scene black with Dissolve(1.0)
    play music "BGM_Kamar Pia.ogg" fadein 1.0
    scene kamar pia with Dissolve(1.0)
    show pia at pia_near with dissolve
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    $ quick_menu = True
    pia "Ngapain diem aja, duduk bawah? Keluarin laptop."
    hide pia_talk
    hide pia_side_talk
    with dissolve
    mcname "OTW."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Jadi gini, aku mau bikin merch gantungan kunci, stiker, poster."
    pia "Kamu ada ide gak?"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    menu:
        mcname "Ummm...."
        "Pin sama postcard?":
            mcname "Pin sama postcard?"
            jump gambardikosanpia

        "Gak ada ide, ngikut aja.":
            stop music fadeout 1.0
            play music "BGM_Bad End.ogg" fadein 1.0
            $ quick_menu = False
            mcname "Gak ada ide, ngikut aja."
            #$ renpy.block_rollback()
            scene black with dissolve
            show text "{color=#FFF}GATAU TULISIN APA{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(2.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits    

label gambardikosanpia:
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Hmm… menarik, oke jadi untuk yang mau aku gambar dari fandom anime AK0047 sama dari Keluarga Mata-Mata, ada ide gak?"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    mcname "Kalo yang lagi rame sih dari anime My Deer Friend Kana-tan, gimana?"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve 
    pia "Menarik, boleh. Kamu gambar itu ya."
    hide pia_talk
    hide pia_side_talk
    with dissolve
    mcname "Bentar, ini gambarnya gimana? Aku full? Gambarku ga bagus weh."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Oh iya, jadi gini. Aku gambar lineart, kamu coloring. nanti finishingnya aku."
    hide pia_talk 
    hide pia_side_talk
    with dissolve 
    mcname "Deal!!!"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Nanti kita dibantu Cepio sama temennya, mereka ikut jualan juga di booth kita."
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    mcname "Woaaaaa, baru nih."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve 
    pia "Iya, soalnya pas diliat liat harga boothnya kalo kita berdua aja agak mahal."
    pia "Terus nanti terlalu sepi kalo kita doang yang display."
    pia "Jadi Cepio juga ikutan biar rame meja booth kita."
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    mcname "Okeeee, mantaaaaap."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Oke, ini aku konsepin gambar ini ya."
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    hide pia with dissolve
    "Pia pun mulai membuat sketsa dan memberikan arahan ke [mcname] untuk membantunya."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene awan malam with Dissolve(1.0)
    show pia at pia_near with dissolve
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    #$ renpy.block_rollback()
    $ quick_menu = True
    pia "WEEEEH UDAH GELAP AJA INI DI LUAR! GAK SADAR!"
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    hide pia with dissolve
    $ quick_menu = False
    scene kamar pia with Dissolve(2.0)
    show pia at pia_near with dissolve
    $ quick_menu = True
    mcname "Lah iya udah malem ya, hahaha gak terasa ya. fokus banget kita."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "LAPER. MAKAN."
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    mcname "Mau mesen NERUFOOD apa keluar aja kita nyari makan?"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Mesen NERUFOOD aja ah, males keluar keluar lagi."
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    mcname "Okeh, mesen ini gimana?\n*Ngeliatin menu di aplikasi NERUFOOD*"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Hmmm… Enak kayaknya. Oke sung buruaaaan, lapeeer."
    hide pia_talk 
    hide pia_side_talk
    mcname "Iya sabaaaar."
    show pia_smile at pia_near
    show pia_side_smile at left
    with dissolve
    pia "Huahahahaha"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Eh aku ke toilet dulu"
    hide pia_talk 
    hide pia_smile
    hide pia_side_smile
    hide pia_side_talk
    with dissolve
    mcname "Iya"
    hide pia with dissolve
    "[mcname] pun termenung duduk melihat ke sekeliling kamar Pia"
    "[mcname] menyadari bahwa di kosannya banyak sekali pajangan dan merch fanart buatannya."
    mcname "{i}Pia ambis juga ya, keliatan dari schedule kuliah yang terpajang rapih di sticky notes meja belajarnya dan banyaknya sketsa bertumpuk di sudut-sudut ruangan.{/i}"
    mcname "{i}Err… Agak berantakan sih, haha.{/i}"
    "[mcname] pun menyadari betapa mandirinya Pia dalam beberapa situasi, walaupun Pia selalu terlihat sebagai pribadi yang supel, mudah bergaul dengan banyak orang"
    "Namun dibalik itu semua tidak ada yang benar-benar mengenal Pia seutuhnya. Namun dengan adanya [mcname], Pia seperti menemukan cahaya baru untuk memulainya kembali."
    show pia at pia_near with dissolve
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Kamu gak buka lemari-lemari aku kan??!!"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    mcname "Pi, yang bener aja……"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve 
    pia "Siapa tau kan?"
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    "???" "NERUFOOD~"
    mcname "Oh dah sampe tuh, aku ambil ya."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Iyaaaaa"
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    hide pia with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene kamar pia with Dissolve(1.0)
    $ quick_menu = True
    "Pia dan [mcname] pun melanjutkan makan di kosan."
    show pia at pia_near with dissolve
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "WUOHHH!!! Enak."
    hide pia_talk
    hide pia_side_talk
    with dissolve
    mcname "Ya kan?"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "MAO COBA YANG KAMU!"
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    "Pia mendadak langsung mengambil sesendok makanan [mcname]."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "WUOHHHH ENAKKK JUGAA!"
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    mcname "Hadeehh. Pelan-pelan, Pia."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "UHUK!! UHUK!! UHUK!!!"
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    mcname "Kaaaaaaaaaaan…"
    mcname "Nih minum dulu."
    show pia_talk at pia_near 
    show pia_side_talk at left
    with dissolve
    pia "*Glug Glug*"
    pia "Ahhhhh!"
    pia "Makasih [mcname]!"
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    hide pia with dissolve
    mcname "Iyaaa. Yauda sana lanjut makannya."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene kamar pia with Dissolve(1.0)
    show pia at pia_near with dissolve
    #$ renpy.block_rollback()
    $ quick_menu = True
    mcname "Uaaaah, kenyang banget~"
    mcname "Ah, udah malem nih. Aku pulang dulu ya."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Yahhh…"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    mcname "Ga bisa sampe malem banget, soalnya besok UTS."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Yaudaah. Hati-hati di jalan~"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    hide pia with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" fadein 1.0 volume (0.8)
    scene awan malam with Dissolve(1.0)
    #$ renpy.block_rollback()
    $ quick_menu = True
    "Setelah itu, [mcname] pun kembali ke kosannya."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(2.0)
    #$ renpy.block_rollback()
    $ quick_menu = True
    "[mcname] pulang, duduk di meja belajarnya sambil mulai mengeluarkan buku-buku dan catatan materi ujian esok hari."
    "[mcname] bersiap begadang untuk fokus belajar karena besok adalah salah satu ujian mata kuliah tertulis yang paling sulit."
    stop music fadeout 1.0
    play sound "audio/ReceiveText.ogg" loop volume (2.0)
    $ quick_menu=False
    window auto hide
    pause (1.0)
    window auto show
    $ quick_menu=True
    stop sound
    mcname "......"
    $ quick_menu = False
    play music "BGM_Happy + HP.ogg" fadein 1.0 volume (2.0)
    nvl clear
    pia_nvl "Tidur?"
    mc_nvl "Gak lah. Begadang, belajar"
    pia_nvl "Asik, sama sih ahahaha"
    pia_nvl "Sambil ngechat dong dikit dikit biar gak sepi :(("
    mc_nvl "Okeeee, sampe ketiduran ya"
    pia_nvl "Pasang alarm dulu!"
    mc_nvl "Siaaap"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Dosen.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Tak terasa sekarang sudah sampai hari ujian."
    $ quick_menu = False
    scene kelas with Dissolve(2.0)
    show dosen at dosen_center with dissolve
    show dosen_talk at dosen_center 
    show dosen_side_talk at left
    with dissolve
    #$ renpy.block_rollback()
    $ quick_menu = True
    dosen "Pagi!!"
    dosen "Semua buku dan HP simpan di depan ya."
    dosen "Di atas meja hanya boleh ada alat tulis"
    dosen "Ujian kita mulai 10 menit lagi."
    hide dosen_talk
    hide dosen_side_talk
    with dissolve
    "Mahasiswa/i" "Baik buu~"
    hide dosen with dissolve
    $ quick_menu = False
    jump quiz

label truepiaafterquiz:
    #$ renpy.block_rollback()
    $ quick_menu = True
    "Selesai ujian, semua mahasiswa/i mengumpulkan lembar jawaban ke pengawas."
    "Ujian hari itu berakhir."
    $ quick_menu=False
    scene black with Dissolve(1.0)
    scene kelas with Dissolve(1.0)
    $ quick_menu=True
    mcname "Hueeeee selesai juga ini ujian."
    mcname "*Liat kiri kanan*"
    show pia at pia_near with dissolve
    show pia_side_talk at left
    show pia_talk at pia_near
    with dissolve
    pia ".........."
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    mcname "Hahahaha gimana? Lancar? Bisa kan jawabnya?"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Bisa lah!"
    pia "Yang bener aja, cuma kayak ada yang kurang puas aja weh."
    pia "Harusnya aku tambahin, blablabla-"
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    mcname "Akh ini dia! Pia Pia si ambis itu."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Ya lah! Harus bagus, jangan setengah-setengah."
    pia "Tapi waktunya kurang hueeee~"
    hide pia_side_talk
    hide pia_talk
    with dissolve
    menu:
        "Respon kamu..."
        "Ke kantin kuy":
            #$ renpy.block_rollback()
            stop music fadeout 1.0
            play music "BGM_Bad End.ogg" fadein 1.0
            $ quick_menu = False
            mcname "Ke kantin kuy"
            scene black with dissolve
            show text "{color=#FF0000}PANJANGIN BAD END NYA{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FF0000}BAD END{/color}" with Pause(2.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits
        "Jalan-jalan yuk, keliling Jakarta gitu atau ke mana.":
            jump trueendpiajalanmonas

label trueendpiajalanmonas:
    #$ renpy.block_rollback()
    show pia at pia_near with dissolve
    mcname "Jalan-jalan yuk, keliling Jakarta gitu atau ke mana."
    mcname "Gimana, mau?"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Now banget?"
    pia "Siapa aja?"
    pia "Ajak Cepio kah?"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    mcname "Umm… kalo kita berdua aja gimana?"
    show pia_shock at pia_near
    show pia_side_shock at left
    with dissolve
    pia "Eeeeh??\n*Blush*"
    pia "A-ayo!"
    hide pia_side_shock
    hide pia_shock
    hide pia
    with dissolve
    "[mcname] dan Pia pun menaiki kendaraan umum menuju ke Monas."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Monas.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Di monas..."
    $ quick_menu = False
    scene monas temporary with Dissolve(2.0)
    #$ renpy.block_rollback()
    show pia at pia_near with dissolve
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    $ quick_menu = True
    pia "Hueeeee Monas tuh gede ya."
    pia "Fotooooo!!!!"
    play sound "audio/camera.mp3"
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    mcname "Ih kayak orang baru pertama liat monas aja."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "EMAAAAANG~"
    pia "Kamu gak mau foto di sini apa?"
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    mcname "Iya dah iya, fotoin nih."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Sini HP kamu."
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    "Pengamen" "*Nyanyi lagu*"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Weeeh"
    hide pia_talk
    hide pia_side_talk
    mcname "Gas Pia dueeet."
    show pia_talk at pia_near
    show pia_side_talk at left 
    with dissolve
    pia "*ikut nyanyi*"
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    mcname "Hahaha mantaaaap, digoyang Piaaaa~"
    mcname "Bang, aku kasih 10rb. Bawain lagu ini bang, temen aku ngidam banget."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "WEEEH APAAN!?"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "Pengamen" "Oke kak"
    "Pengamen" "*nyanyi*"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "LESGOOOOOOO~ HAHAHAHA!!!"
    pia "*nyanyi*"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    hide pia with dissolve
    "Ternyata duet Pia dan pengamen menarik banyak perhatian orang dan sukses menghibur pengunjung yang datang ke Monas."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Beberapa saat kemudian..."
    $ quick_menu = False
    scene monas temporary with Dissolve(1.0)
    show pia at pia_near with dissolve
    show pia_side at left with dissolve
    $ quick_menu = True
    show pia at pia_near with dissolve
    show pia_smile at pia_near
    show pia_side_smile at left
    with dissolve
    pia "Hueeeehh~ Ahahahaha!! Seru juga, makasih bang!!!!"
    hide pia_side with dissolve
    "Pengamen" "Makasih neng!!!"
    hide pia_smile
    hide pia_side_smile 
    with dissolve
    "Pia dan [mcname] pun berpisah dengan pengamen tersebut"
    mcname "Klop banget, lucuuuu~"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "HAHAHAHA!! Jadi pengalaman lucu nih."
    hide pia_talk
    hide pia_side_talk
    with dissolve
    mcname "Betuuul."
    hide pia with dissolve
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "BGM_Kelas.ogg" fadein 1.0 volume (1.5)
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Beberapa hari kemudian..."
    $ quick_menu = False
    scene kelas with Dissolve(2.0)
    show pia at pia_near with dissolve
    show pia_talk at pia_near
    show pia_side at left
    with dissolve
    #$ renpy.block_rollback()
    $ quick_menu = True
    pia "Pagi [mcname]."
    hide pia_talk
    hide pia_side_talk
    with dissolve
    mcname "Pagii!!"
    hide pia with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play sound "audio/open_door.mp3" fadein 1.0 volume(15.0)
    play music "BGM_Dosen.ogg" fadein 1.0
    scene kelas with Dissolve(1.0)
    show dosen at dosen_center with dissolve
    show dosen_side at left with dissolve
    #$ renpy.block_rollback()
    $ quick_menu = True
    dosen "Selamat pagi semuanya"
    dosen "Pelajaran hari ini akan dimulai, ya. Hari ini saya berikan tugas untuk menggambar bebas dengan canvas dan cat."
    dosen "Ngerjainnya bebas mau di mana aja, tapi nanti sebelum pelajaran berakhir harus dikumpulkan di sini ya."
    dosen "Nanti saya ke kelas lagi di akhir pelajaran, ya."
    hide dosen_side with dissolve
    "Mahasiswa/i" "Baik buuu~"
    stop music fadeout 1.0
    hide dosen with dissolve
    $ quick_menu=False
    window auto hide
    play music "BGM_Kelas.ogg" fadein 1.0 volume (1.5)
    show pia at pia_near with dissolve
    show pia_side at left with dissolve
    $ quick_menu=True
    pia "Weeeeh tugasnya menggambar bebas!"
    hide pia_side with dissolve
    mcname "Gimana? Mau ngegambar bareng?"
    show pia_side at left with dissolve
    pia "Gassss! Ke rooftop yuk! Sekalian cari inspirasi."
    hide pia_side with dissolve
    mcname "Okeee."
    hide pia with dissolve
    "[mcname] dan Pia pun memutuskan melukis bersama di rooftop."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Rooftop Siang.ogg" fadein 1.0
    scene rooftop with Dissolve(1.0)
    #$ renpy.block_rollback()
    $ quick_menu = True
    "Di tengah saat mereka melukis."
    mcname "Huaaaaaa selesai~"
    mcname "*Merenggangkan pinggang*"
    "[mcname] melirik Pia yang masih serius menggambar"
    mcname "Hmmm"
    mcname "Belum selese Pi?"
    mcname "Mau ke kantin dulu ga nih beli cemilan gitu?"
    show pia_side at left
    show pia at pia_near
    with dissolve
    pia "......"
    hide pia_side with dissolve
    mcname "Serius amat Mbak.\n*Colek pipi Pia pakai kuas yang masih ada catnya*"
    show pia_side at left with dissolve
    pia "AAAAAAAAAAAAAA [mcname!u]!!!!!!"
    hide pia_side with dissolve
    mcname "Hahahahaha lagian serius amat, dipanggil ga nengok."
    show pia_side at left with dissolve
    pia "HAAAAAA!!!! PIPI AKUUUUUUUUUUUU!!!!"
    hide pia_side with dissolve
    mcname "HUAHAHAHAHA!!!!"
    show pia_side at left with dissolve
    pia "Ehehehuehue~\n*Pia mulai mencolekan kuasnya pada pallete catnya*"
    pia "RASAKAN PEMBALASANKU!!!"
    pia "HIAAAAAAAAAAAAT!!!!!\n*Mencoret balik muka [mcname]*"
    hide pia_side with dissolve
    mcname "NOOOOOOOOOOOOOOO~"
    mcname "KAU PIKIR AKU AKAN MENYERAH?"
    mcname "TIDAK SEMUDAH ITU! RASAKAN INI HIAAAAAAAAAAAAAT!!"
    show pia_side at left with dissolve
    pia "KAU PIKIR AKAN MUDAH MENYERANGKU?"
    pia "JURUS SERIBU BAYANGAN!!"
    hide pia_side with dissolve
    mcname "JURUS LARI ZIG ZAG!!! HIAAAAAAT!!"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Dosen.ogg" fadein 1.0
    scene kelas sore with Dissolve(1.0)
    #$ renpy.block_rollback()
    $ quick_menu = True
    "Akhirnya [mcname] dan Pia kembali ke ruang kelas untuk mengumpulkan tugas dengan muka yang penuh coret."
    show dosen at dosen_center with dissolve
    show dosen_side at left with dissolve
    dosen "......"
    dosen "Kalian kenapa?"
    dosen "Berantem?"
    hide dosen_side with dissolve
    "[mcname] & Pia" "E-engga Bu.\n*Sambil menahan tawa*"
    show dosen_side at left with dissolve
    dosen "Oke makasih tugasnya, sana cuci muka terus pulang."
    dosen "Gak malu diliatin orang tadi pas jalan ke sini?"
    hide dosen_side with dissolve
    mcname "Pia mah udah gak punya malu, Bu."
    show pia_side at left with dissolve
    pia "HEH! [mcname!u] BU YANG GAK PUNYA MALU!!"
    hide pia_side with dissolve
    show dosen_side at left with dissolve
    dosen "Heeeeh… iya iya"
    dosen "Sana pergi"
    dosen "Kasian kulit muka kalian rusak nanti."
    hide dosen_side with dissolve
    "[mcname] & Pia" "Iya buuuuu. Makasih buuuuuu."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Sore.ogg" fadein 1.0
    scene lorong sore with Dissolve(1.0)
    #$ renpy.block_rollback()
    show pia at pia_near with dissolve
    $ quick_menu = True
    "[mcname] dan Pia saling senggol."
    show pia_side at left with dissolve
    pia "HAHAHAHAHAHA!!"
    hide pia_side with dissolve
    mcname "HUAHAHAHAHAHAHA!!!"
    jump truendpia

label truendpia:
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene chapter 3 pia with Dissolve (1.0)
    pause(3.0)
    scene black with Dissolve (1.0)
    play music "audio/BGM_Kantin.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Hari demi hari berlalu, minggu demi minggu pun dilewati."
    "[mcname] dan Pia perlahan menunjukan kekompakan dan perkembangan project jualan mereka untuk event jejepangan ini semakin cepat."
    scene kantin with Dissolve(2.0)
    show pia at pia_near with dissolve
    show pia_side at left with dissolve
    pia "[mcname]! Yuk anterin aku nyetak produknya."
    pia "Udah tinggal 2 minggu lagi nih."
    hide pia_side at left with dissolve
    mcname "Sekarang banget?"
    show pia_side at left with dissolve
    pia "Iya ayooooo~\n*Menarik tangan [mcname]*"
    hide pia_side with dissolve
    mcname "I-iyaaa."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Mall.ogg" fadein 1.0
    scene mall with Dissolve(1.0)
    show pia at pia_near with dissolve
    show pia_side at left with dissolve
    $ quick_menu = True
    pia "Itu, di situ. Nyetak di situ."
    hide pia_side with dissolve
    mcname "Oke oke, untung sepi tuh."
    show pia_side at left with dissolve
    pia "Yuk ngantri buat cetaknya."
    hide pia_side with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    pause(1.0)
    scene mall with Dissolve(1.0)
    #$ renpy.block_rollback()
    $ quick_menu = True
    "Beberapa jam kemudian, [mcname] dan Pia pun selesai mencetak merch yang dibutuhkan."
    stop music fadeout 1.0
    $ quick_menu = False
    play music "BGM_Happy + HP.ogg" fadein 1.0 volume (2.0)
    fio_nvl "Pi, udah selese nyetaknya?"
    pia_pov_nvl "Udah Cepio."
    pia_pov_nvl "Punya Cece udah?"
    fio_nvl "Aman, udah semua."
    fio_nvl "Tinggal ke eventnya aja deh ini ahaha."
    pia_pov_nvl "Mantaaaap"
    fio_nvl "Lagi di mana kamu?"
    fio_nvl "Eh ga jadi"
    fio_nvl "Aku tau"
    fio_nvl "Pasti lagi berduaan sama [mcname]"
    fio_nvl "Maaf ganggu"
    fio_nvl "Thx bye"
    stop music fadeout 1.0
    play music "audio/BGM_Mall.ogg" fadein 1.0
    scene mall with dissolve
    show pia at pia_near with dissolve
    #$ renpy.block_rollback()
    $ quick_menu = True
    show pia_side at left with dissolve
    pia "CEPIOOOOOOOOOOOO~"
    hide pia_side with dissolve
    mcname "Cepio?"
    show pia_side at left with dissolve
    pia "I-iya."
    hide pia_side with dissolve
    mcname "Oh oke oke."
    mcname "Dah kelar semua ini."
    mcname "Mau ngapain lagi?"
    mcname "Eh wait, itu kayaknya ada menu cake baru deh di cafe itu."
    show pia_side at left with dissolve
    pia "Lah iya ada 2 rasa baru."
    pia "Gas ga sih?"
    hide pia_side with dissolve
    mcname "Lah buset, lesgooo~"
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play sound "audio/cafe-entrance.mp3" fadein 1.0
    play music "audio/BGM_Cafe Cerah.ogg" fadein 1.0 volume (2.0)
    scene cafe with Dissolve(1.0)
    show pia at pia_near with dissolve
    "Staff" "Haloo. Mau pesan apa?"
    mcname "Hmmm… kamu mesen rasa yang mana, Pi?"
    mcname "Aku yang mangga deh kayaknya."
    show pia_side at left with dissolve
    pia "Yaudah aku yang melon ya."
    hide pia_side with dissolve
    "Staff" "Baik, berarti 1 mango cake dan 1 melon cake."
    "Staff" "Mohon ditunggu, ya."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    pause(1.0)
    scene cafe with Dissolve(1.0)
    show pia at pia_near with dissolve
    #$ renpy.block_rollback()
    $ quick_menu = True
    "Staff" "Ini pesanannya ya, Kak."
    "[mcname] & Pia" "Terima kasih kakk."
    "Pia dan [mcname] mulai menyantap pesanan mereka."
    mcname "Wueeee enaaaak yang mangga"
    show pia_side at left with dissolve
    pia "Iya kah?"
    hide pia_side with dissolve
    mcname "*Menyodorkan garpu yang sudah ada potongan kue*"
    mcname "Aaaaaaaa~"
    show pia_side at left with dissolve
    pia "Eeeh… aaaaaa~"
    hide pia_side with dissolve
    mcname "Enak kan ya?"
    show pia_side at left with dissolve
    pia "{i}Aaaaaaa indirect kiss{/i}\n*blush*"
    hide pia_side with dissolve
    mcname "Kenapa? Kurang enak kah?"
    show pia_side at left with dissolve
    pia "E-engga kok. Enak, aha ha ha."
    hide pia_side with dissolve
    mcname "Ya kan!!! Eh coba minta dong yang punya kamu."
    show pia_side at left with dissolve
    pia "Eeeeeeeeee~"
    pia "Ummm…."
    pia "*Nyodorin garpu dengan potongan kue*"
    pia "*Blush*"
    hide pia_side with dissolve
    mcname "Aaam…"
    "*[mcname] melahap kue dari garpu Pia*"
    mcname "Hmmm…enak juga."
    show pia_side at left with dissolve
    pia "Umm…"
    pia "*Muka memerah*"
    pia "Uuuuuuu i-iya"
    hide pia_side with dissolve
    mcname "Ngapa lu?"
    show pia_side at left with dissolve
    pia "Gapapa"
    hide pia_side with dissolve
    mcname "?????"
    hide pia with dissolve
    "Malam itu berakhir dengan [mcname] yang tidak peka."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Pagi Siang.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Hari Matsuri pun tiba."
    $ quick_menu = False
    #$ renpy.block_rollback()
    scene depan kampus with Dissolve(2.0)
    $ quick_menu = True
    "Pia dan [mcname] sedang merias booth dan merapikan dagangan merch mereka."
    show fio at fio_near_left with dissolve
    show pia at pia_near_right with dissolve
    show fio_side at left with dissolve
    $ quick_menu = True
    fio "Pagiiii~"
    fio "Rajin banget udah sampe nih kalian berdua."
    hide fio_side with dissolve
    show pia_side at left with dissolve
    pia "Cepioooooooooooo~"
    hide pia_side with dissolve
    show fio_side at left with dissolve
    fio "Sini aku bantu rapih-rapih."
    fio "Oh ini, kenalin temen aku yang bantu bantu jaga booth kita nanti."
    hide fio_side with dissolve
    # Harusnya show takamina sprite di sini
    "???" "Halo salam kenal. Aku Takamina."
    "Pia & [mcname]" "Halo, salam kenaaaaal."
    "Takamina" "Kalian temannya Fiony, ya?"
    show pia_side at left with dissolve
    pia "I-iya Kak."
    pia "Uuummm… Kakak cantik banget!"
    hide pia_side with dissolve
    "Takamina" "Aduhhh bisa aja. Kamu juga imut banget deh."
    "Takamina" "Yauda aku bantu beresin merch nya juga yaa."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    pause(1.0)
    scene kampus with Dissolve(1.0)
    # Urutan Sprite Takamina, Pia, Pio
    show fio at fio_near_left with dissolve
    show pia at pia_near_right with dissolve
    mcname "Huaaaa udah rapih nih, tinggal nunggu acaranya buka."
    show pia_side at left with dissolve
    $ quick_menu = True
    pia "MELINGKAR ALL!!!"
    pia "KITA YEL-YEL DULU!"
    hide pia_side with dissolve
    mcname "…………"
    "Takamina" "Gemes juga ya, haha."
    show fio_side at left with dissolve
    fio "Maapin ya, kadang suka aneh emang anak ini."
    hide fio_side with dissolve
    show pia_side at left with dissolve
    pia "Aaaaaaaa~"
    hide pia_side with dissolve
    "[mcname] & Fiony & Takamina" "Hahahaha"
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Monas.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Akhirnya acara matsuri pun dibuka tepat pukul 10 siang."
    $ quick_menu = False
    scene kampus with Dissolve(2.0)
#HARUSNYA MATSURI SIANG
    $ quick_menu = True
    play sound "crowd_noise.mp3" loop fadein 1.0 volume (4.0)
    "Pengunjung mulai berdatangan."
    show pia_side at left with dissolve
    pia "Weeeeeh rameeeeeeee."
    hide pia_side with dissolve
    show fio_side at left with dissolve
    fio "Semangat guys!"
    hide fio_side with dissolve
    "Takamina" "Yoooshaaaaaaaaa!!!"
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Matsuri Malam.ogg" fadein 1.0
    scene kampus sore with Dissolve(1.0)
#HARUSNAY MATSURI SORE
    #$ renpy.block_rollback()
    $ quick_menu = True
    "Pukul 3 sore, semua jualan booth Pia, [mcname], Fiony dan Takamina pun ludes habis semua."
    show pia_side at left with dissolve
    pia "OTSU ALLL, ABIS SEMUA WEEEEH!!!"
    hide pia_side with dissolve
    show fio_side at left with dissolve
    fio "Hahahaha gak nyangka bakal selaku ini. Memang ke push karena nama \"Yang Mulia Piaraan\" sih ini mah."
    fio "Keren banget sih ga ada lawan."
    hide fio_side with dissolve
    "[mcname] & Takamina" "Kelaaaaaaas!!!!"
    show pia_side at left with dissolve
    pia "HEH!! APA SIH AHAHAHA!!"
    hide pia_side with dissolve
    show fio_side at left with dissolve
    fio "Dari tadi kamu sibuk mulu, istirahat dulu"
    fio "[mcname]! Gak peka, ajak Pia jalan-jalan keliling matsuri sana!"
    hide fio_side with dissolve
    mcname "Eeh. Terus gimana rapih-rapihnya…"
    "Takamina" "Aman, aku sama Fiony yang gantian beres-beres."
    "Takamina" "Kalian quality time aja, hehehehe."
    show pia_side at left with dissolve
    pia "Kakaaaaak~\n*Blush*"
    hide pia_side with dissolve
    mcname "Huhuhu oke. Makasih ya Kak Takamina, Cepio."
    "Fiony & Takamina" "*Mengacungkan jempol*"
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene kampus sore with Dissolve(1.0)
#HARUSNYA MATSURI SORE
    show pia at pia_near with dissolve
    #$ renpy.block_rollback()
    $ quick_menu = True
    show pia_side at left with dissolve
    pia "*Menarik tangan [mcname]*"
    pia "Mau ke situuuuuu~"
    hide pia_side with dissolve
    mcname "Eee… a-ayooo."
    "[mcname] dan Pia pun berkeliling sembari membeli banyak jajanan seperti takoyaki, okonomiyaki, dan lain-lain."
    mcname "Abis itu dimakan kamu semua?"
    show pia_side at left with dissolve
    pia "Amaaan. Perut aku ada ruangan tersendiri buat cemilan, huahahaha."
    hide pia_side with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Beberapa menit kemudian..."
    $ quick_menu = False
    scene kampus sore with Dissolve(2.0)
#Harusnya MATSURI SORE
    show pia at pia_near with dissolve
    #$ renpy.block_rollback()
    $ quick_menu = True
    show pia_side at left with dissolve
    pia "......"
    pia "[mcname]....."
    pia "[mcname]......"
    hide pia_side with dissolve
    mcname "Apaan?"
    show pia_side at left with dissolve
    pia "Kenyang…\n*Sambil memegang tusuk takoyaki yang tinggal 1 buah*"
    hide pia_side with dissolve
    mcname "Aaaaaaammm~"
    "*[mcname] langsung memakan takoyaki yang sedang dipegang Pia*"
    show pia_side at left with dissolve
    pia "!!!!\n*Blush*"
    hide pia_side with dissolve
    mcname "Kaaan, pasti ga abis.\n*Sambil ngunyah*"
    show pia_side at left with dissolve
    pia "Hehehe"
    hide pia_side with dissolve
    mcname "Mau ke mana lagi?"
    show pia_side at left with dissolve
    pia "Jalan-jalan bentar, terus balik ke booth aja bantuin Cepio sama Takamina yuk."
    hide pia_side with dissolve
    mcname "Oke"
    stop sound fadeout 1.0
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Sore.ogg" fadein 1.0
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Pukul 6 sore, [mcname] dan Pia kembali ke booth mereka."
    $ quick_menu = False
    scene kampus malam with Dissolve(2.0)
#HARUSNYA MATSURI MALAM
    #$ renpy.block_rollback()
    show pia at pia_near with dissolve
    show pia_side at left with dissolve
    $ quick_menu = True
    pia "Weeeh udah rapih nih, siap pulang~"
    hide pia_side with dissolve
    hide pia with dissolve
    show fio at fio_near_left with dissolve
    show pia at pia_near_right with dissolve
    show fio_side at left with dissolve
    fio "Pulang, enak aja! Mau jalan-jalan dulu."
    hide fio_side with dissolve
    "Takamina" "Gimana kelilingnya?"
    show pia_side at left with dissolve
    pia "Ehehehe..."
    hide pia_side with dissolve
    show fio_side at left with dissolve
    fio "Dari sini mau ke mana lagi deh?"
    hide fio_side with dissolve
    mcname "Gatau, tinggal nunggu acara kembang api aja sih ini."
    show fio_side at left with dissolve
    fio "Pia, sini deh."
    fio "[mcname] kamu jauh-jauh dulu, aku mau ngobrol sama Pia sebentar"
    hide fio_side with dissolve
    mcname "Eeh… okee."
    show fio_side at left with dissolve
    play sound "SFX - Key.mp3"
    fio "Nih\n*Kasih kunci ke Pia* (SAMBIL MUNCUL ASSET KUNCI NNUE)"
    hide fio_side with dissolve
    show pia_side at left with dissolve
    pia "Hah? Ini kunci apa?"
    hide pia_side with dissolve
    show fio_side at left with dissolve
    fio "Kunci pintu gedung DKV sama pintu rooftop, hehe."
    hide fio_side with dissolve
    show pia_side at left with dissolve
    pia "HEEEEEEEEE"
    pia "Kok Cepio bisa punya ini????"
    hide pia_side with dissolve
    show fio_side at left with dissolve
    fio "Takamina anak BEM, dia ada kunci cadangan."
    fio "Ini aku pinjem dari Takamina, katanya gapapa."
    hide fio_side with dissolve
    show pia_side at left with dissolve
    pia "Teruus?"
    hide pia_side with dissolve
    show fio_side at left with dissolve
    fio "Nonton kembang api kayaknya bagus deh dari rooftop, uhuk uhuk!"
    hide fio_side with dissolve
    show pia_side at left with dissolve
    pia "Hahhhh??"
    hide pia_side with dissolve
    show fio_side at left with dissolve
    fio "Sana ajak [mcname], pemandangannya dari atas lebih bagus loh."
    hide fio_side with dissolve
    show pia_side at left with dissolve
    pia "Terus kalian gimana?"
    hide pia_side with dissolve
    show fio_side at left with dissolve
    fio "Udaaaah, bawel Pia. Sana pergi."
    fio "[mcname]!!"
    fio "[mcname]!!"
    fio "Temenin Pia dong."
    hide fio_side with dissolve
    mcname "Ke mana?"
    show fio_side at left with dissolve
    fio "Gatau tuh, ikutin Pia aja.\n*Mendorong Pia*"
    hide fio_side with dissolve
    show pia_side at left with dissolve
    pia "Heeeeeeeeeee~"
    hide pia_side with dissolve
    mcname "Mau ke mana?"
    show pia_side at left with dissolve
    pia "Umm… Ikut aku aja…"
    hide pia_side with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene kampus malam with Dissolve(1.0)
    show pia at pia_near with dissolve
    #$ renpy.block_rollback()
    $ quick_menu = True
    "Pia dan [mcname] pun berjalan masuk ke gedung DKV."
    mcname "Mau ngapain Pi? Kan udah dikunci kalo malem."
    show pia_side at left with dissolve
    pia "Aku ada kuncinya."
    hide pia_side with dissolve
    mcname "Heeeeeee dapet dari mana?"
    show pia_side at left with dissolve
    pia "Dipinjemin Takamina sama Cepio, hehe."
    hide pia_side with dissolve
    mcname "Terus mau ke mana?"
    show pia_side at left with dissolve
    pia "Markas~"
    hide pia_side with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene lorong malam with Dissolve(1.0)
    show pia at pia_near with dissolve
    #$ renpy.block_rollback()
    show pia_side at left with dissolve
    $ quick_menu = True
    pia "Eeeh gelap ya, kalo malem."
    hide pia_side with dissolve
    mcname "Ya kalo terang siang sih Pi."
    show pia_side at left with dissolve
    pia "Bukan gituuuuu. Ini sereeeeem kalo malem weeeeh!\n*Memegang erat tangan [mcname]*"
    hide pia_side with dissolve
    mcname "Lah k-kamu yang ngajak ke sini, kok kamu yg takut?\n*blush*"
    mcname "Ahahaha."
    show pia_side at left with dissolve
    pia "Bawel, buruan ke rooftop ih!"
    hide pia_side with dissolve
    mcname "Kalo aku lari gimana?"
    show pia_side at left with dissolve
    pia "Kalo aku nangis gimana?"
    hide pia_side with dissolve
    mcname "Iya, engga…. Ehehe."
    stop music fadeout 1.0
    $ quick_menu = False
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    scene black with Dissolve(1.0)
    play music "audio/BGM_Rooftop Pia Malam.ogg" fadein 1.0 volume (2.0)
    scene rooftop malam with Dissolve(1.0)
    show pia at pia_near with dissolve
    #$ renpy.block_rollback()
    show pia_side at left with dissolve
    $ quick_menu = True
    pia "HEEEEEEEEEE~"
    pia "KALO MALEM BAGUS JUGA YA PEMANDANGANNYA DARI ROOFTOP!"
    hide pia_side with dissolve
    mcname "Iya, ditambah lagi ada event begini jadi banyak cahaya gitu dari kejauhan."
    show pia_side at left with dissolve
    pia "Awwww… iya cantik bangeeeeet."
    pia "Pia dan [mcname] pun mulai duduk bersila di pinggir pagar sambil melihat acara dari jauh."
    pia "Iiih lagi bon odori tuh di bawah."
    hide pia_side with dissolve
    mcname "Iya…"
    mcname "Nyesel gak tuh ga ikut bon odori?"
    show pia_side at left with dissolve
    pia "Gak lah, enak di sini\n*Blush*"
    hide pia_side with dissolve
# Insert Chibi Pia nyender ke MC
    "Pia bersender ke [mcname]"
    mcname "*Blush*"
    show pia_side at left with dissolve
    pia "[mcname], makasih ya. Berkat kamu, aku jadi banyak ngerasain hal menyenangkan selama kuliah di sini."
    hide pia_side at left with dissolve
    mcname "Ahaha gak gitu, aku yang makasih."
    show pia_side at left with dissolve
    pia "Tapi kamu selalu nurut, ngikutin kemauan anehku, support aku terus…"
    hide pia_side with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene pia end no firework with Dissolve(1.0)
    scene pia end talk no firework
    show pia_side at left
    with dissolve
    $ quick_menu = True
    pia "[mcname]! Makasih ya udah mau nemenin aku terus."
    $ quick_menu = False
    scene pia end no firework
    hide pia_side
    with dissolve
    $ quick_menu = True
    mcname "Sama-sama Pia, makasih udah mau selalu ada buat aku juga."
    $ quick_menu = False
    scene pia end talk no firework
    show pia_side at left
    with dissolve
    $ quick_menu = True
    pia "Iiih harusnya itu kata-kata aku!!!"
    $ quick_menu = False
    scene pia end no firework    
    hide pia_side
    with dissolve
    $ quick_menu = True
    mcname "Akulah si support system kamu itu~"
    mcname "Hahaha"
    $ quick_menu = False
    scene pia end talk no firework
    show pia_side at left
    with dissolve
    $ quick_menu = True
    pia "[mcname]..."
    $ quick_menu = False
    scene pia end no firework    
    hide pia_side
    with dissolve
    $ quick_menu = True
    mcname "Apaan??"
    $ quick_menu = False
    scene pia end talk no firework
    show pia_side at left
    with dissolve
    $ quick_menu = True
    pia "Umm…"
    pia "[mcname], aku suka–"
    play sound "SFX - Hanabi.wav" loop
    $ quick_menu = False
    scene pia end talk with Dissolve(1.0)
    #$ renpy.block_rollback()
    $ quick_menu = True
    "Suara kembang api pun mulai terdengar dan langit pun dipenuhi dengan cahaya indah."
    "Suara mereka pun kalah dengan bisingnya suara kembang api malam itu."
    $ quick_menu = False
    scene pia end smile with dissolve  
    $ quick_menu = True
    "[mcname] dan Pia bertatapan saling tersenyum sambil memandangi langit malam saat itu."
    "Malam itu…"
    "Menjadi malam yang tidak akan terlupakan untuk Pia dan [mcname]."
    stop sound fadeout 1.0
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    show text "{color=#FFF}THE END{/color}" with Pause(4.0)
    play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
    jump credits
