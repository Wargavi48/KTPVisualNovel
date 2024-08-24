label truepia:
    "Pia yang mendapat semangat dari [mcname!c] pun makin membulatkan tekad untuk tetap melanjutkan melukis dan membuat gambar."
    $ renpy.block_rollback()
    $ quick_menu = True
    show pia at pia_near with dissolve
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Huahaha! Saatnya kamu kubawa ke dunia ilustrator yang biasa aku jalani selama ini."
    hide pia_talk 
    hide pia_side_talk
    with dissolve 
    "[mcname!c]" "Gimana?"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve 
    pia "Kamu udah denger nama \"Yang Mulia Piaraan\" kan?"
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Gatau kenapa, selalu mau ketawa tiap denger nama itu deh."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "HEH! DIEM! AHAHAHA!!"
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Yup, sampe sini aku udah tau."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Nah, jadi sebelum aku masuk ke dunia perkuliahan ini, aku aktif banget bikin gambar."
    pia "Nerima commision dari orang-orang buat gambar, sampe jualan hasil karyaku di event-event jejepangan gitu."
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Hoooooo, keren juga kamu. Terus kalo sekarang?"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Sekarang lagi vakum dulu. Sibuk kuliah gini, gimana waktu sendirinya weh!"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Hahaha, bener juga."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Padahal di komunitas itu aku cukup dikenal dan menurutku gak sedikit yang tau pen-nameku itu."
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Hmmmm???\n*Melirik ragu*"
    show pia_talk at pia_near 
    show pia_side_talk at left
    with dissolve
    pia "Beneran weh!!! Bukannya narsis yaa! Tapi ya gitu, nih liat.\n*Ngasih liat akun twitternya*"
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Woooow gila, artis banget nih! Followernya sampe puluhan ribu gitu. Kamu…."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "GAK YA! KAMU MAU BILANG BELI FOLLOWER KAN?! ENGGA!"
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Cih ketauan, ahahaha."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Heeeeh… kebaca pikiranmu! Haha."
    hide pia_talk 
    hide pia_side_talk 
    with dissolve
    pia "…………"
    show pia_sad at pia_near
    show pia_side_sad at left
    with dissolve
    pia "Ya gitu lah… ilang motivasiku buat lanjut gambar gini…."
    hide pia_side_sad
    with dissolve
    "[mcname!c]" "Weh kenapa?"
    "[mcname!c]" "Bukannya itu salah satu yang udah ngembangin namamu dan ngebuat kamu jadi yang kayak sekarang ini?"
    "[mcname!c]" "Mau dibuang gitu aja?"
    show pia_sad at pia_near
    show pia_side_sad at left
    with dissolve
    pia "Huhuhu engga sih, kayak art block aja."
    pia "Hilang aja semangatnya."
    hide pia_side_sad
    with dissolve
    "[mcname!c]" "Hmm... Oke, gimana cara aku bisa semangatin biar kamu bisa kayak dulu lagi?"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Temenin aku."
    hide pia_sad
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Ke mana?"
    show pia_shock at pia_near
    show pia_side_shock at left
    with dissolve
    pia "Temenin aku terus sampe sukses. *Blush*"
    hide pia_shock
    hide pia_side_shock
    with dissolve
    "[mcname!c]" "Ummm… Gak nyangka kamu bakal ngomong gitu, bingung aku balesnya.\n*Blush*"
    show pia_silent at pia_near 
    show pia_side_silent at left
    with dissolve
    pia "GIMANA… IH MALU KAN AKU JADINYA!!"
    hide pia_silent 
    hide pia_side_silent
    with dissolve
    "[mcname!c]" "Oke, deal!"
    show pia_smile at pia_near 
    show pia_side_smile at left
    with dissolve
    pia "Hehehe, okeh deal!!!"
    hide pia
    hide pia_smile
    hide pia_side_smile
    with dissolve
    "Akhirnya [mcname!c] duduk di sebelah Pia sambil melihat pemandangan dari rooftop melihat jauh ke depan."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Sore.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "Tak terasa hari sudah menjadi sore."
    "[mcname!c] dan Pia pun pulang ke kost masing-masing."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" fadein 1.0 volume (0.8)
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Di kost..."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(2.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname!c]" "*Sedang menggambar*"
    play sound "ReceiveText.ogg" loop volume (2.0)
    "Tiba-tiba terdengar notifikasi chat."
    stop sound
    stop music fadeout 1.0
    "[mcname!c]" "{i}Siapa nih ngespam?{/i}"
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
    mc_nvl "{image=pia skets.png}"
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
    $ renpy.block_rollback()
    scene kamar mc kota with Dissolve(0.2)
    $ quick_menu = True
    menu:
        "Respon kamu?"
        "Iye iye mau. Nih gue buka obrolan ya. Lagi ngapain Kak Pia?":
            $ quick_menu = False
            $ renpy.block_rollback()
            mc_nvl "Iye iye mau."
            mc_nvl "Nih gue buka obrolan ya."
            mc_nvl "Lagi ngapain Kak Pia?"
            pia_nvl "Lagi boboan aja ini di kasur, hehe."
            pia_nvl "[mcname!c], main game yuk."
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
            pia_nvl "Strawberry cake cafe AhSae enak banget."
            mc_nvl "Benar!"
            pia_nvl "O"
            pia_nvl "Pas aku makan strawberry cake pas itu, kamu ngeliatin aku terus."
            mc_nvl "???"
            mc_nvl "Bohong"
            pia_nvl "X"
            pia_nvl "Aku Imut"
            mc_nvl "Hmm…"
            pia_nvl "???"
            pia_nvl "{image=turu.png}"
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
            scene kamar mc kota with Dissolve(0.2)
            $ quick_menu = True
            "Malam itu terasa panjang sekali, sambil melanjutkan sketsa yang dibuat [mcname!c] dengan wajah yang memerah."
            "Hari itu berakhir dengan kekalahan [mcname!c]."
            jump trueendrooftoppia
        "Udah kemaleman tapi weh, aku mau tidur juga bentar lagi ini.":
            $ renpy.block_rollback()
            $ quick_menu = False
            stop music fadeout 1.0
            play music "BGM_Bad End.ogg" fadein 1.0
            mc_nvl "Udah kemaleman tapi weh."
            mc_nvl "Aku mau tidur juga bentar lagi ini."
            pia_nvl "Ah oke yaudah deh."
            nvl clear
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
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits
label trueendrooftoppia:
    $ renpy.block_rollback()
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "BGM_Pagi Siang.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya..."
    $ quick_menu = False
    scene depan kampus with Dissolve(2.0)
    $ quick_menu = True
    "[mcname!c]" "{i}Hmm? Apa ini di tas?{/i}"
    $ quick_menu = False 
    window auto hide
    show matsuri at poster
    show matsuri:
            xpos 0.4
    with dissolve
    window auto show
    $ quick_menu = True
    "[mcname!c]" "{i}Oalaah, flyer.{/i}"
    "[mcname!c]" "{i}Kemarin aku lupa ngasih ke Pia.{/i}"
    $ quick_menu = False 
    window auto hide
    hide matsuri with dissolve
    window auto show
    $ quick_menu = True
    "[mcname!c]" "{i}Ah yaudah, nanti juga ketemu.{/i}"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Sore.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Sesudah kelas..."
    $ quick_menu = False
    scene lorong sore with Dissolve(2.0)
    show pia at pia_near with dissolve
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    $ quick_menu = True
    pia "Ah! [mcname!c]!"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Pii, udah beres kelasnya?"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Udah, hehe."
    pia "Ke rooftop yuk!"
    hide pia_talk 
    hide pia_side_talk
    "[mcname!c]" "Gasss~"
    hide pia with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Rooftop Sore.ogg" fadein 1.0 volume 2.0
    scene rooftop sore with Dissolve(1.0)
    show pia at pia_near with dissolve
    $ quick_menu = True 
    $ renpy.block_rollback()
    "[mcname!c]" "Pia, ini kemarin aku lupa ngasih ini."
    $ quick_menu = False
    window auto hide
    hide pia with dissolve
    show matsuri at poster
    show matsuri:
            xpos 0.4
    with dissolve
    window auto show
    $ quick_menu = True
    "[mcname!c]" "Ada flyer acara jejepangan."
    $ quick_menu = False 
    window auto hide
    hide matsuri with dissolve
    show pia at pia_near
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    window auto show
    $ quick_menu = True
    pia "Hmm... Menarik."
    pia "Eh."
    pia "EH!! [mcname!u]!!!"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Apa?"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Ini ada bagian kreator."
    pia "Yuk ikutan jualan!!!"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Heeeeee~"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Katanya mau support aku…"
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Iya… Tapi aku ga pernah jualan gambar, terus ga tau mau bikin apa."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Tenang, kamu bersama sepuh di sini. Bikin booth bareng yuk."
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Ya… Oke aja sih."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Hmm acara jejepangannya masih 3 bulan lagi."
    pia "Bisa lah ini 2 bulan buat banyak merch."
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Oke~"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Kamu daftarin gih cepet."
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Nama boothnya?"
    show pia_talk at pia_near
    show pia_side_talk at left 
    with dissolve
    pia "Hmmm… Bener juga, apa ya..."
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Gimana kalo \"Yang Mulia dan Piaraan\"?"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Ahahaha kamu jadi piaraan?"
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Biar lucu aja sih."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Selama aku jadi lebih superior dari kamu, aku setuju. Gas!!!"
    hide pia
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "Akhirnya [mcname!c] mendaftarkan diri ke event jejepangan tersebut dengan nama circle: \n~Yang Mulia dan Piaraan~\n"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" fadein 1.0 volume (0.8)
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Malam itu di kost..."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(2.0)
    play sound "ReceiveText.ogg" loop volume (2.0)
    window auto hide
    pause(1.0)
    window auto show
    $ quick_menu = True
    "[mcname!c]" "{i}Hadeh, yang ngespam gini sih...{/i}"
    stop sound
    stop music fadeout 1.0
    "[mcname!c]" "{i}Pasti Si Pia lagi nih.{/i}"
    $ quick_menu = False
    play music "BGM_Happy + HP.ogg" fadein 1.0 volume (2.0)
    nvl clear 
    pia_nvl "P"
    pia_nvl "P"
    pia_nvl "P"
    pia_nvl "[mcname!u]!!!"
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
    $ renpy.block_rollback()
    nvl clear
    stop music fadeout 1.0
    scene kamar mc kota with Dissolve(1.0)
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Pagi Siang.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya..."
    $ quick_menu = False
    nvl clear 
    pia_nvl "[mcname!u]!!!"
    pia_nvl "{image=location.png}"
    mc_nvl "?"
    pia_nvl "Alamat kosan aku. Buruan sini, bantuin."
    mc_nvl "Sekarang?"
    pia_nvl "Iyaaaaa, mumpung lagi semangat gambar."
    pia_nvl "Bawa laptop, sambil brainstorming kita."
    mc_nvl "O-oke"
    $ renpy.block_rollback()
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene depan kosan with Dissolve(1.0)
    $ quick_menu = False
    nvl clear 
    mc_nvl "Oiii, depan."
    pia_nvl "Okeh wait, aku keluar."
    nvl clear
    $ renpy.block_rollback()
    stop music fadeout 1.0
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    scene black with Dissolve(1.0)
    play music "BGM_Kamar Pia.ogg" fadein 1.0
    scene kamar pia with Dissolve(1.0)
    show pia_home at pia_near with dissolve
    show pia_home_talk at pia_near
    show pia_home_side_talk at left
    with dissolve
    $ quick_menu = True
    pia "Ngapain diem aja, duduk bawah? Keluarin laptop."
    hide pia_home_talk
    hide pia_home_side_talk
    with dissolve
    "[mcname!c]" "OTW."
    show pia_home_talk at pia_near
    show pia_home_side_talk at left
    with dissolve
    pia "Jadi gini, aku mau bikin merch gantungan kunci, stiker, poster."
    pia "Kamu ada ide gak?"
    hide pia_home_talk
    hide pia_home_side_talk
    with dissolve
    menu:
        "[mcname!c]" "Ummm...."
        "Pin sama postcard?":
            "[mcname!c]" "Pin sama postcard?"
            jump gambardikosanpia

        "Poster dan Sticker pake AI.":
            $ quick_menu = False
            stop music fadeout 1.0
            play music "BGM_Bad End.ogg" fadein 1.0
            show pia_home_silent at pia_near 
            with dissolve
            "[mcname!c]" "Gimana kalo kita bikin poster dan stiker gitu? Kan lagi rame tuh."
            "[mcname!c]" "Buat temanya bisa banyak kok, pake AI aja biar gampang."
            show pia_home_side_silent at left
            with dissolve
            pia "PAKE AIII!!???"
            hide pia_side_silent with dissolve
            "[mcname!c]"" iyaa, kan sekarang lagi banyak tuh biar ga cape juga kita mikirinnya hahaha."
            show pia_home_side_silent at left
            with dissolve
            pia "Jadi kamu tuh suka pke AI gitu, [mcname!c]!? Ga nyaka aku, apa jangan-jangan tugas-tugasmu pake AI juga."
            pia "Aku tuh ya, paling-paling ga suka sama yang gambar/desain pake AI!"
            hide pia_side_silent with dissolve
            "[mcname!c]" "T-tapi kan.."
            show pia_home_side_silent at left
            with dissolve
            pia "Aahhh udahlah, mending aku buat sendirian aja! Sana urusin sendiri tuh sama AI!"
            hide pia_home_silent
            hide pia_home_side_silent
            hide pia_home
            with dissolve
            $ renpy.block_rollback()
            scene black with dissolve
            show text "{color=#FFF}AI MEMANG BANTUIN SIH.. TAPI LIAT SITUASI KONDISI LAGI YA BROK{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(2.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits    

label gambardikosanpia:
    show pia_home_talk at pia_near
    show pia_home_side_talk at left
    with dissolve
    pia "Hmm… menarik, oke jadi untuk yang mau aku gambar dari fandom anime AK0047 sama dari Keluarga Mata-Mata, ada ide gak?"
    hide pia_home_talk
    hide pia_home_side_talk
    with dissolve
    "[mcname!c]" "Kalo yang lagi rame sih dari anime My Deer Friend Kana-tan, gimana?"
    show pia_home_talk at pia_near
    show pia_home_side_talk at left
    with dissolve 
    pia "Menarik, boleh. Kamu gambar itu ya."
    hide pia_home_talk
    hide pia_home_side_talk
    with dissolve
    "[mcname!c]" "Bentar, ini gambarnya gimana? Aku full? Gambarku ga bagus weh."
    show pia_home_talk at pia_near
    show pia_home_side_talk at left
    with dissolve
    pia "Oh iya, jadi gini. Aku gambar lineart, kamu coloring. Nanti finishingnya aku."
    hide pia_home_talk 
    hide pia_home_side_talk
    with dissolve 
    "[mcname!c]" "Deal!!!"
    show pia_home_talk at pia_near
    show pia_home_side_talk at left
    with dissolve
    pia "Nanti kita dibantu Cepio sama temennya, mereka ikut jualan juga di booth kita."
    hide pia_home_talk 
    hide pia_home_side_talk
    with dissolve
    "[mcname!c]" "Woaaaaa, baru nih."
    show pia_home_talk at pia_near
    show pia_home_side_talk at left
    with dissolve 
    pia "Iya, soalnya pas diliat liat harga boothnya kalo kita berdua aja agak mahal."
    pia "Terus nanti terlalu sepi kalo kita doang yang display."
    pia "Jadi Cepio juga ikutan biar rame meja booth kita."
    hide pia_home_talk 
    hide pia_home_side_talk
    with dissolve
    "[mcname!c]" "Okeeee, mantaaaaap."
    show pia_home_talk at pia_near
    show pia_home_side_talk at left
    with dissolve
    pia "Oke, ini aku konsepin gambar ini ya."
    hide pia_home_talk 
    hide pia_home_side_talk
    with dissolve
    hide pia_home with dissolve
    "Pia pun mulai membuat sketsa dan memberikan arahan ke [mcname!c] untuk membantunya."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene awan malam with Dissolve(1.0)
    show pia_home_side_talk at left
    with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    pia "WEEEEH UDAH GELAP AJA INI DI LUAR! GAK SADAR!"
    hide pia_home_talk 
    hide pia_home_side_talk
    with dissolve
    hide pia_home with dissolve
    $ quick_menu = False
    scene kamar pia with Dissolve(2.0)
    show pia_home at pia_near with dissolve
    $ quick_menu = True
    "[mcname!c]" "Lah iya udah malem ya, hahaha gak terasa ya. fokus banget kita."
    show pia_home_talk at pia_near
    show pia_home_side_talk at left
    with dissolve
    pia "LAPER. MAKAN."
    hide pia_home_talk 
    hide pia_home_side_talk
    with dissolve
    "[mcname!c]" "Mau mesen NERUFOOD apa keluar aja kita nyari makan?"
    show pia_home_talk at pia_near
    show pia_home_side_talk at left
    with dissolve
    pia "Mesen NERUFOOD aja ah, males keluar keluar lagi."
    hide pia_home_talk 
    hide pia_home_side_talk
    with dissolve
    "[mcname!c]" "Okeh, mesen ini gimana?\n*Ngeliatin menu di aplikasi NERUFOOD*"
    show pia_home_talk at pia_near
    show pia_home_side_talk at left
    with dissolve
    pia "Hmmm… Enak kayaknya. Oke sung buruaaaan, lapeeer."
    hide pia_home_talk 
    hide pia_home_side_talk
    with dissolve
    "[mcname!c]" "Iya sabaaaar."
    show pia_home_smile at pia_near
    show pia_home_side_smile at left
    with dissolve
    pia "Huahahahaha~"
    show pia_home_talk at pia_near
    show pia_home_side_talk at left
    with dissolve
    pia "Eh aku ke toilet dulu."
    hide pia_home_talk 
    hide pia_home_smile
    hide pia_home_side_smile
    hide pia_home_side_talk
    with dissolve
    "[mcname!c]" "Iya."
    hide pia_home with dissolve
    "[mcname!c] pun termenung duduk melihat ke sekeliling kamar Pia."
    "Terlihat bahwa di kosannya banyak sekali pajangan dan merch fanart buatannya."
    "[mcname!c]" "{i}Pia ambis juga ya, keliatan dari schedule kuliah yang terpajang rapih di sticky notes meja belajarnya dan banyaknya sketsa bertumpuk di sudut-sudut ruangan.{/i}"
    "[mcname!c]" "{i}Err… Agak berantakan sih, haha.{/i}"
    "[mcname!c] pun menyadari betapa mandirinya Pia dalam beberapa situasi, walaupun Pia selalu terlihat sebagai pribadi yang supel, mudah bergaul dengan banyak orang."
    "Namun dibalik itu semua tidak ada yang benar-benar mengenal Pia seutuhnya. Namun dengan adanya [mcname!c], Pia seperti menemukan cahaya baru untuk memulainya kembali."
    show pia_home at pia_near with dissolve
    show pia_home_talk at pia_near
    show pia_home_side_talk at left
    with dissolve
    pia "Kamu gak buka lemari-lemari aku kan??!!"
    hide pia_home_talk
    hide pia_home_side_talk
    with dissolve
    "[mcname!c]" "Pi, yang bener aja……"
    show pia_home_talk at pia_near
    show pia_home_side_talk at left
    with dissolve 
    pia "Siapa tau kan?"
    hide pia_home_talk 
    hide pia_home_side_talk
    with dissolve
    "???" "NERUFOOD~"
    "[mcname!c]" "Oh dah sampe tuh, aku ambil ya."
    show pia_home_talk at pia_near
    show pia_home_side_talk at left
    with dissolve
    pia "Iyaaaaa."
    hide pia_hometalk 
    hide pia_home_side_talk
    with dissolve
    hide pia_home with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene kamar pia with Dissolve(1.0)
    $ quick_menu = True
    "Pia dan [mcname!c] pun melanjutkan makan di kosan."
    show pia_home at pia_near with dissolve
    show pia_home_talk at pia_near
    show pia_home_side_talk at left
    with dissolve
    pia "WUOHHH!!! ENAK."
    hide pia_home_talk
    hide pia_home_side_talk
    with dissolve
    "[mcname!c]" "Ya kan?"
    show pia_home_talk at pia_near
    show pia_home_side_talk at left
    with dissolve
    pia "MAO COBA YANG KAMU!"
    hide pia_home_talk 
    hide pia_home_side_talk
    with dissolve
    "Pia mendadak langsung mengambil sesendok makanan [mcname!c]."
    show pia_home_talk at pia_near
    show pia_home_side_talk at left
    with dissolve
    pia "WUOHHHH ENAKKK JUGAA!"
    hide pia_home_talk 
    hide pia_home_side_talk
    with dissolve
    "[mcname!c]" "Hadeehh. Pelan-pelan, Pia."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    $ quick_menu = True
    pia "UHUK!! UHUK!! UHUK!!!"
    $ quick_menu = False
    scene kamar pia with Dissolve(1.0)
    show pia_home at pia_near 
    show pia_home_sad at pia_near
    with dissolve
    $ quick_menu = True
    "[mcname!c]" "Kaaaaaaaaaaan…"
    "[mcname!c]" "Nih minum dulu."
    show pia_home_side_sad at left
    with dissolve
    pia "*Glug Glug*"
    show pia_home_side_smile at left 
    hide pia_home_side_sad
    hide pia_home_sad 
    show pia_home_smile at pia_near
    with dissolve
    pia "Ahhhhh!"
    show pia_home_talk at pia_near
    show pia_home_side_talk at left 
    hide pia_home_side_small 
    hide pia_home_sad 
    with dissolve
    pia "Makasih [mcname!c]!"
    hide pia_home_talk 
    hide pia_home_side_talk
    hide pia_home_side_smile
    with dissolve
    "[mcname!c]" "Iyaaa. Yauda sana lanjut makannya."
    hide pia_home_smile 
    hide pia_home_side_smile
    hide pia_home
    with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene kamar pia with Dissolve(1.0)
    show pia_home at pia_near with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname!c]" "Uaaaah, kenyang banget~"
    "[mcname!c]" "Ah, udah malem nih. Aku pulang dulu ya."
    show pia_home_talk at pia_near
    show pia_home_side_talk at left
    with dissolve
    pia "Yahhh…"
    hide pia_home_talk
    hide pia_home_side_talk
    with dissolve
    "[mcname!c]" "Ga bisa sampe malem banget, soalnya besok UTS."
    show pia_home_talk at pia_near
    show pia_home_side_talk at left
    with dissolve
    pia "Yaudaah. Hati-hati di jalan~"
    hide pia_home_talk
    hide pia_home_side_talk
    with dissolve
    hide pia_home with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" fadein 1.0 volume (0.8)
    scene awan malam with Dissolve(1.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "Setelah itu, [mcname!c] pun kembali ke kosannya."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(2.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname!c] pulang, duduk di meja belajarnya sambil mulai mengeluarkan buku-buku dan catatan materi ujian esok hari."
    "[mcname!c] bersiap begadang untuk fokus belajar karena besok adalah salah satu ujian mata kuliah tertulis yang paling sulit."
    stop music fadeout 1.0
    play sound "ReceiveText.ogg" loop volume (2.0) volume (2.0)
    $ quick_menu=False
    window auto hide
    pause (1.0)
    window auto show
    $ quick_menu=True
    "[mcname!c]" "......"
    stop sound
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
    $ renpy.block_rollback()
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
    $ renpy.block_rollback()
    $ quick_menu = True
    dosen "Pagi!!"
    dosen "Semua buku dan HP simpan di depan ya."
    dosen "Di atas meja hanya boleh ada alat tulis."
    dosen "Ujian kita mulai 10 menit lagi."
    hide dosen_talk
    hide dosen_side_talk
    with dissolve
    "Mahasiswa/i" "Baik buu~"
    hide dosen with dissolve
    $ quick_menu = False
    jump quiz

label truepiaafterquiz:
    $ renpy.block_rollback()
    $ quick_menu = True
    "Selesai ujian, semua mahasiswa/i mengumpulkan lembar jawaban ke pengawas."
    "Ujian hari itu berakhir."
    $ quick_menu=False
    scene black with Dissolve(1.0)
    scene kelas with Dissolve(1.0)
    $ quick_menu=True
    "[mcname!c]" "Hueeeee selesai juga ini ujian."
    "[mcname!c]" "*Liat kiri kanan*"
    show pia at pia_near with dissolve
    show pia_side_talk at left
    show pia_talk at pia_near
    with dissolve
    pia "[mcname!c]~"
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Hahahaha gimana? Lancar? Bisa kan jawabnya?"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Bisa lah, yang bener aja!"
    pia "Cuma... Kayak ada yang kurang puas aja weh."
    pia "Harusnya aku tambahin, blablabla-"
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Akh ini dia! Pia Pia si ambis itu."
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
        "Ke kantin kuy.":
            $ renpy.block_rollback()
            $ quick_menu = False
            "[mcname!c]" "Ke kantin yuk aku laper nih."
            show pia_talk at pia_near
            show pia_side_talk at left
            pia "Boleh aku juga mayan laper nih."
            stop music fadeout 1.0
            scene black with Dissolve(1.0)
            play music "BGM_Bad End.ogg" fadein 1.0
            scene kantin with Dissolve(1.0)
            #SUARA RICUH KERIBUTAN
            "[mcname!c]" "Loh ada apa ini? Kok rame sih?"
            show pia_shock at pia_near
            show pia_side_shock at left
            with dissolve
            pia "Lohhhh apaan ini, kok banyak yang rusuh sih?"
            hide pia_side_shock
            hide pia_shock
            with dissolve
            "[mcname!c]" "Eh ini ada apaan deh?" 
            "Mahasiswa 2" "Ini yang jualan ternyata pake daging tiren kita lagi demo karena banyak yang ke RS mending lo ikutan dah ayooo."
            show pia_shock at pia_near
            show pia_side_shock at left
            with dissolve
            pia "Waduh, [mcname!c]..."
            hide pia_side_shock
            with dissolve
            "[mcname!c]" "HIDUP MAHASISWAAA!!!!!"
            hide pia_shock
            with dissolve
            scene black with dissolve
            show text "{color=#FF0000}LU MALAH IKUT DEMO DAN TINGGALIN PIA SENDIRIAN{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FF0000}BAD END{/color}" with Pause(2.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits
        "Ke rooftop yuk.":
            $ renpy.block_rollback()
            $ quick_menu = False
            "[mcname!c]" "Eh gimana kalo ke rooftop?"
            show pia_side_talk at left
            show pia_talk at pia_near 
            with dissolve
            pia "Bolehhh keknya seru tuh."
            hide pia
            hide pia_shock
            hide pia_side_talk at left
            hide pia_talk at pia_near 
            with dissolve
            stop music fadeout 1.0
            scene black with Dissolve(1.0)
            play music "BGM_Bad End.ogg" fadein 1.0
            scene rooftop with Dissolve(1.0)
            "[mcname!c]" "Wahhhh udaranya sejuk ya pii "
            show pia_shock at pia_near
            show pia_side_shock at left
            with dissolve
            pia "Iyaa nih dah lama ga ke sini seger juga.. Ehhh kamu mau ke mana [mcname!c]?"
            hide pia_side_shock at left
            with dissolve
            "[mcname!c]" "Ini.. Cuma ke sini doang kok, udaranya lebih besar kalau di sini."
            show pia_shock at pia_near
            show pia_side_shock at left
            with dissolve
            pia "Eh ati ati, jangan nyeder gitu nanti takut ja-"
            hide pia_side_shock at left
            hide pia_shock
            with dissolve
            "[mcname!c]" "EHHHHHH!??? PIAAAAA~~~!"
            scene black with dissolve
            show text "{color=#FF0000}ADUHHH KALAU KE ROOFTOP JANGAN NYEDER GITU DEH BRO, KALAU DI GAME SI BISA LOAD LAH INI...{/color}" with Pause(4.0)
            scene black with dissolve
            show text "{color=#FF0000}LAH INI KAN GAME YA?{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FF0000}BAD END{/color}" with Pause(2.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits
        "Jalan-jalan yuk, keliling Jakarta gitu atau ke mana.":
            jump trueendpiajalanmonas
label trueendpiajalanmonas:
    $ renpy.block_rollback()
    show pia at pia_near with dissolve
    "[mcname!c]" "Jalan-jalan yuk, keliling Jakarta gitu atau ke mana."
    "[mcname!c]" "Gimana, mau?"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Now banget?"
    pia "Siapa aja?"
    pia "Ajak Cepio kah?"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Umm… Kalo kita berdua aja gimana?"
    show pia_shock at pia_near
    show pia_side_shock at left
    with dissolve
    pia "Eeeeh??\n*Blush*"
    pia "A-ayo!"
    hide pia_side_shock
    hide pia_shock
    hide pia
    with dissolve
    "[mcname!c] dan Pia pun menaiki kendaraan umum menuju ke Monas."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Monas.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Di monas..."
    $ quick_menu = False
    scene monas temporary with Dissolve(2.0)
    $ renpy.block_rollback()
    show pia at pia_near with dissolve
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    $ quick_menu = True
    pia "Hueeeee Monas tuh gede ya."
    pia "Fotooooo!!!!"
    play sound "audio/camera.mp3" volume (2.0)
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Ih kayak orang baru pertama liat monas aja."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "EMAAAAANG~"
    pia "Kamu gak mau foto di sini apa?"
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Iya dah iya, fotoin nih."
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
    pia "Weeeh~"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Gas Pia dueeet."
    hide pia
    show piapunk
    show piapunk:
        ypos 0.75 zoom 0.25 
    with dissolve
    pia "*Ikut nyanyi*"
    hide piapunk
    show pia at pia_near
    with dissolve
    "[mcname!c]" "Hahaha mantaaaap, digoyang Piaaaa~"
    "[mcname!c]" "Bang, aku kasih 10rb. Bawain lagu ini bang, temen aku ngidam banget."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "WEEEH APAAN!?"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "Pengamen" "Oke kak."
    "Pengamen" "*Nyanyi*"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "LESGOOOOOOO~ HAHAHAHA!!!"
    hide pia_talk
    hide pia_side_talk
    hide pia
    show piapunk
    show piapunk:
        ypos 0.75 zoom 0.25 
    with dissolve
    pia "*Nyanyi*"
    hide piapunk with dissolve
    "Ternyata duet Pia dan pengamen menarik banyak perhatian orang dan sukses menghibur pengunjung yang datang ke Monas."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Beberapa saat kemudian..."
    $ quick_menu = False
    scene monas temporary with Dissolve(2.0)
    show pia at pia_near with dissolve
    show pia_smile at pia_near
    show pia_side_smile at left
    with dissolve
    $ quick_menu = True
    pia "Hueeeehh~ Ahahahaha!! Seru juga, makasih Bang!!!!"
    hide pia_side with dissolve
    hide pia_smile
    hide pia_side_smile 
    with dissolve
    "Pengamen" "Makasih Neng!!!"
    "Pia dan [mcname!c] pun berpisah dengan pengamen tersebut."
    "[mcname!c]" "Klop banget, lucuuuu~"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "HAHAHAHA!! Jadi pengalaman lucu nih."
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Betuuul~"
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
    show pia_side_talk at left
    with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    pia "Pagi [mcname!c]."
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Pagii!!"
    hide pia with dissolve
    play sound "audio/open_door.mp3" fadein 1.0 volume(15.0)
    play music "BGM_Dosen.ogg" fadein 1.0
    show dosen at dosen_center with dissolve
    show dosen_talk at dosen_center 
    show dosen_side_talk at left
    with dissolve 
    $ renpy.block_rollback()
    $ quick_menu = True
    dosen "Selamat pagi semuanya."
    dosen "Pelajaran hari ini akan dimulai, ya. Hari ini saya berikan tugas untuk menggambar bebas dengan canvas dan cat."
    dosen "Ngerjainnya bebas mau di mana aja, tapi nanti sebelum pelajaran berakhir harus dikumpulkan di sini ya."
    dosen "Nanti saya ke kelas lagi di akhir pelajaran, ya."
    hide dosen_talk
    hide dosen_side_talk
    with dissolve
    stop music fadeout 1.0
    "Mahasiswa/i" "Baik buuu~"
    hide dosen with dissolve
    play music "BGM_Kelas.ogg" fadein 1.0 volume (1.5)
    show pia at pia_near with dissolve
    show pia_talk at pia_near
    show pia_side_talk at left 
    with dissolve
    pia "Weeeeh tugasnya menggambar bebas!"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Gimana? Mau ngegambar bareng?"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Gassss! Ke rooftop yuk! Sekalian cari inspirasi."
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Okeee."
    hide pia with dissolve
    "[mcname!c] dan Pia pun memutuskan melukis bersama di rooftop."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Rooftop Siang.ogg" fadein 1.0 volume 2.0
    scene rooftop with Dissolve(1.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "Di tengah saat mereka melukis."
    "[mcname!c]" "Huaaaaaa selesai~"
    "[mcname!c]" "*Merenggangkan pinggang*"
    "[mcname!c] melirik Pia yang masih serius menggambar."
    show pia at pia_near with dissolve
    "[mcname!c]" "Hmmm..."
    "[mcname!c]" "Belum selese Pi?"
    "[mcname!c]" "Mau ke kantin dulu ga nih beli cemilan gitu?"
    show pia_side at left
    with dissolve
    pia "......"
    hide pia_side with dissolve
    "[mcname!c]" "Serius amat Mbak.\n*Colek pipi Pia pakai kuas yang masih ada catnya*"
    show pia_silent at pia_near
    show pia_side_silent at left with dissolve
    pia "AAAAAAAAAAAAAA [mcname!u]!!!!!!"
    hide pia_side_silent with dissolve
    "[mcname!c]" "Hahahahaha lagian serius amat, dipanggil ga nengok."
    show pia_side_silent at left with dissolve
    pia "HAAAAAA!!!! PIPI AKUUUUUUUUUUUU!!!!"
    hide pia_side_silent with dissolve
    "[mcname!c]" "HUAHAHAHAHA!!!!"
    show pia_talk at pia_near
    show pia_side_talk at left
    hide pia_silent
    with dissolve
    pia "Ehehehuehue~\n*Pia mulai mencolekan kuasnya pada pallete catnya*"
    pia "RASAKAN PEMBALASANKU!!!"
    pia "HIAAAAAAAAAAAAT!!!!!\n*Mencoret balik muka [mcname!c]*"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "NOOOOOOOOOOOOOOO~"
    "[mcname!c]" "KAU PIKIR AKU AKAN MENYERAH?"
    "[mcname!c]" "TIDAK SEMUDAH ITU! RASAKAN INI HIAAAAAAAAAAAAAT!!"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "KAU PIKIR AKAN MUDAH MENYERANGKU?"
    pia "JURUS SERIBU BAYANGAN!!"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "JURUS LARI ZIG ZAG!!! HIAAAAAAT!!"
    hide pia with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Dosen.ogg" fadein 1.0
    scene kelas sore with Dissolve(1.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "Akhirnya [mcname!c] dan Pia kembali ke ruang kelas untuk mengumpulkan tugas dengan muka yang penuh coret."
    show dosen at dosen_center 
    show dosen_side at left
    with dissolve
    dosen "......"
    show dosen_talk at dosen_center
    show dosen_side_talk at left
    with dissolve
    dosen "Kalian kenapa?"
    dosen "Berantem?"
    hide dosen_talk
    hide dosen_side_talk
    hide dosen_side
    hide dosen
    show pia3
    show pia3:
        ypos 0.77 zoom 0.25 
    with dissolve
    "[mcname!c] & Pia" "E-engga Bu.\n*Sambil menahan tawa*"
    hide pia3
    show dosen_talk at dosen_center
    show dosen_side_talk at left
    with dissolve
    dosen "Oke makasih tugasnya, sana cuci muka terus pulang."
    dosen "Gak malu diliatin orang tadi pas jalan ke sini?"
    hide dosen_talk
    hide dosen_side_talk
    show pia3
    show pia3:
        ypos 0.77 zoom 0.25 
    with dissolve
    with dissolve 
    "[mcname!c]" "Pia mah udah gak punya malu, Bu."
    hide pia3
    hide dosen
    show pia at pia_near 
    show pia_silent at pia_near
    show pia_side_silent at left
    with dissolve
    pia "HEH! [mcname!u] YANG GAK PUNYA MALU, BU!!"
    hide pia_side_silent with dissolve
    hide pia_silent
    hide pia
    with dissolve
    show dosen at dosen_center with dissolve
    show dosen_talk at dosen_center
    show dosen_side_talk at left
    with dissolve
    dosen "Heeeeh… iya iya."
    dosen "Sana pergi."
    dosen "Kasian kulit muka kalian rusak nanti."
    hide dosen_talk
    hide dosen_side_talk
    with dissolve
    "[mcname!c] & Pia" "Iya Buuuuu. Makasih Buuuuuu."
    hide dosen with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Sore.ogg" fadein 1.0
    scene lorong sore with Dissolve(1.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname!c] dan Pia saling senggol."
    show pia at pia_near with dissolve
    show pia_smile at pia_near
    show pia_side_smile at left
    with dissolve
    pia "HAHAHAHAHAHA!!"
    hide pia_side_smile with dissolve
    "[mcname!c]" "HUAHAHAHAHAHAHA!!!"
    hide pia_smile
    hide pia
    with dissolve
    jump truendpia

label truendpia:
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    $ yangmulia_piaraan.grant()
    scene chapter 3 pia with Dissolve (1.0)
    pause(3.0)
    scene black with Dissolve (1.0)
    play music "audio/BGM_Kantin.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Hari demi hari berlalu, minggu demi minggu pun dilewati."
    "[mcname!c] dan Pia perlahan menunjukan kekompakan dan perkembangan project jualan mereka untuk event jejepangan ini semakin cepat."
    $ quick_menu = False
    scene kantin with Dissolve(2.0)
    show pia at pia_near with dissolve
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    $ quick_menu = True
    pia "[mcname!c]! Yuk anterin aku nyetak produknya."
    pia "Udah tinggal 2 minggu lagi nih."
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Sekarang banget?"
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Iya ayooooo~\n*Menarik tangan [mcname!c]*"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "I-iyaaa."
    hide pia with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Mall.ogg" fadein 1.0
    scene mall with Dissolve(1.0)
    show pia at pia_near with dissolve
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    $ quick_menu = True
    pia "Itu, di situ. Nyetak di situ."
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Oke oke, untung sepi tuh."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Yuk ngantri buat cetaknya."
    hide pia_talk 
    hide pia_side_talk
    with dissolve
    hide pia with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    pause(1.0)
    scene mall with Dissolve(1.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "Beberapa jam kemudian, [mcname!c] dan Pia pun selesai mencetak merch yang dibutuhkan."
    stop music fadeout 1.0
    $ quick_menu = False
    play music "BGM_Happy + HP.ogg" fadein 1.0 volume (2.0)
    nvl clear
    fio_nvl "Pi, udah selese nyetaknya?"
    pia_pov_nvl "Udah Cepio."
    pia_pov_nvl "Punya Cece udah?"
    fio_nvl "Aman, udah semua."
    fio_nvl "Tinggal ke eventnya aja deh ini ahaha."
    pia_pov_nvl "Mantaaaap"
    fio_nvl "Lagi di mana kamu?"
    fio_nvl "Eh ga jadi"
    fio_nvl "Aku tau"
    fio_nvl "Pasti lagi berduaan sama [mcname!c]"
    fio_nvl "Maaf ganggu"
    fio_nvl "Thx bye"
    $ renpy.block_rollback()
    stop music fadeout 1.0
    play music "audio/BGM_Mall.ogg" fadein 1.0
    scene mall with dissolve
    show pia at pia_near with dissolve
    show pia_silent at pia_near
    $ renpy.block_rollback()
    show pia_side_silent at left
    with dissolve
    $ quick_menu = True
    pia "CEPIOOOOOOOOOOOO~"
    hide pia_side_silent with dissolve
    "[mcname!c]" "Cepio?"
    show pia_shock at pia_near
    hide pia_silent
    show pia_side_shock at left
    with dissolve
    pia "I-iya."
    hide pia_side_shock with dissolve
    "[mcname!c]" "Oh oke oke."
    "[mcname!c]" "Dah kelar semua ini."
    "[mcname!c]" "Mau ngapain lagi?"
    "[mcname!c]" "Eh wait, itu kayaknya ada menu cake baru deh di cafe itu."
    show pia_talk at pia_near
    hide pia_shock
    show pia_side_talk at left
    with dissolve
    pia "Lah iya ada 2 rasa baru."
    pia "Gas ga sih?"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "Lah buset, lesgooo~"
    hide pia with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play sound "audio/cafe-entrance.mp3" fadein 1.0
    play music "audio/BGM_Cafe Sore.ogg" fadein 1.0 volume (2.0)
    scene cafe malam with Dissolve(1.0)
    show pia at pia_near with dissolve
    $ quick_menu = True
    "Staff" "Haloo. Mau pesan apa?"
    "[mcname!c]" "Hmmm… kamu mesen rasa yang mana, Pi?"
    "[mcname!c]" "Aku yang mangga deh kayaknya."
    show pia_talk at pia_near 
    show pia_side_talk at left
    with dissolve
    pia "Yaudah aku yang melon ya."
    hide pia_talk 
    hide pia_side_talk 
    with dissolve
    "Staff" "Baik, berarti 1 mango cake dan 1 melon cake."
    "Staff" "Mohon ditunggu, ya."
    hide pia with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene cafe malam with Dissolve(1.0)
    show pia at pia_near with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    "Staff" "Ini pesanannya ya, Kak."
    show pia_talk at pia_near 
    show pia_side_talk at left
    with dissolve
    "[mcname!c] & Pia" "Terima kasih kakk."
    hide pia_side_talk
    hide pia
    hide pia_talk
    with dissolve
    "Pia dan [mcname!c] mulai menyantap pesanan mereka."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene cafe malam with Dissolve(1.0)
    $ quick_menu = True
    show pia at pia_near with dissolve
    "[mcname!c]" "Wueeee enaaaak yang mangga."
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Iya kah?"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "[mcname!c]" "*Menyodorkan garpu yang sudah ada potongan kue*"
    "[mcname!c]" "Aaaaaaaa~"
    show pia_shock at pia_near
    show pia_side_shock at left
    with dissolve
    pia "Eeeh… aaaaaa~"
    hide pia_side_shock with dissolve
    "[mcname!c]" "Enak kan ya?"
    show pia_side_shock at left with dissolve
    pia "{i}Aaaaaaa indirect kiss{/i}\n*Blush*"
    hide pia_side_shock with dissolve
    "[mcname!c]" "Kenapa? Kurang enak kah?"
    show pia_smile at pia_near
    show pia_side_smile at left
    with dissolve
    pia "E-engga kok. Enak, aha ha ha."
    hide pia_shock
    hide pia_smile 
    show pia at pia_near
    hide pia_side_smile
    with dissolve
    "[mcname!c]" "Ya kan!!! Eh coba minta dong yang punya kamu."
    hide pia
    show pia_shock at pia_near
    show pia_side_shock at left
    with dissolve
    pia "Eeeeeeeeee~"
    show pia at pia_near
    hide pia_shock
    hide pia_side_shock
    show pia_side at left
    with dissolve
    pia "Ummm…."
    hide pia 
    hide pia_side 
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Aaaaaaa~\n*Nyodorin garpu dengan potongan kue*"
    hide pia_side_talk at left
    with dissolve
    "[mcname!c]" "Aaam…"
    hide pia_talk
    show pia at pia_near
    with dissolve
    "*[mcname!c] melahap kue dari garpu Pia*"
    "[mcname!c]" "Hmmm…. Enak juga."
    hide pia
    show pia_side_shock at left
    show pia_shock at pia_near
    with dissolve
    pia "Umm…"
    pia "I-iya."
    hide pia_side_shock with dissolve
    "[mcname!c]" "Ngapa lu?"
    show pia_side_shock at left with dissolve
    pia "Gapapa."
    hide pia_side_shock with dissolve
    "[mcname!c]" "?????"
    hide pia_shock 
    show pia_smile at pia_near
    hide pia_side_shock
    with dissolve
    pia "Hehehe~"
    hide pia_smile
    hide pia_shock
    hide pia
    with dissolve
    "Malam itu berakhir dengan [mcname!c] yang tidak peka."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Pagi Siang.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Hari Matsuri pun tiba."
    $ quick_menu = False
    $ renpy.block_rollback()
    scene depan kampus with Dissolve(2.0)
    $ quick_menu = True
    "Pia dan [mcname!c] sedang merias booth dan merapikan dagangan merch mereka."
    show fio at fio_near_left
    show pia_date at pia_near_right
    with dissolve
    show fio_talk at fio_near_left
    show fio_side_talk at left
    with dissolve
    $ quick_menu = True
    fio "Pagiiii~"
    fio "Rajin banget udah sampe nih kalian berdua."
    hide fio_talk 
    hide fio_side_talk
    with dissolve
    show pia_date_silent at pia_near_right
    show pia_date_side_silent at left
    with dissolve
    pia "Cepioooooooooooo~"
    hide pia_date_side_silent with dissolve
    show fio_talk at fio_near_left
    show fio_side_talk at left
    with dissolve
    fio "Sini aku bantu rapih-rapih."
    fio "Oh ini, kenalin temen aku yang bantu bantu jaga booth kita nanti."
    hide fio_side_talk
    hide fio_talk
    hide fio 
    hide pia_date_silent
    hide pia_date
    with dissolve
    show takamina at takamina_center with dissolve
    show takamina_talk at takamina_center
    show takamina_side_talk at left
    with dissolve
    $ takamina_name = "Takamina"
    takamina "Halo salam kenal. Aku Takamina."
    hide takamina_talk
    hide takamina_side_talk
    with dissolve
    "Pia & [mcname!c]" "Halo, salam kenaaaaal."
    show takamina_talk at takamina_center
    show takamina_side_talk at left
    with dissolve
    "Takamina" "Kalian temannya Fiony, ya?"
    hide takamina_talk
    hide takamina_side_talk
    hide takamina
    show pia_date at pia_near
    show pia_date_talk at pia_near
    show pia_date_side_talk at left
    with dissolve
    pia "I-iya Kak."
    hide pia_date_talk 
    hide pia_date_side_talk 
    show pia_date_smile at pia_near
    show pia_date_side_smile at left
    with dissolve
    pia "Uuummm… Kakak cantik banget!"
    hide pia_date_smile
    hide pia_date_side_smile
    hide pia_date with dissolve
    show takamina at takamina_center with dissolve
    show takamina_talk at takamina_center
    show takamina_side_talk at left
    with dissolve
    "Takamina" "Aduhhh bisa aja. Kamu juga imut banget deh."
    "Takamina" "Yauda aku bantu beresin merch nya juga yaa."
    hide takamina_talk
    hide takamina_side_talk 
    with dissolve
    hide takamina with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    pause(1.0)
    scene depan kampus with Dissolve(1.0)
    # Urutan Sprite Takamina, Pia, Pio
    show takamina at tana_right
    show takamina:
        subpixel True pos (0.17, 0.08) zoom 0.75
    show fio at fio_near_left
    show fio:
        subpixel True xpos 1.15
    show pia_date at pia_near
    with dissolve
    $ quick_menu = True
    "[mcname!c]" "Huaaaa udah rapih nih, tinggal nunggu acaranya buka."
    show pia_date_talk at pia_near 
    show pia_date_side_talk at left
    with dissolve
    pia "MELINGKAR ALL!!!"
    pia "KITA YEL-YEL DULU!"
    hide pia_date_talk
    hide pia_date_side_talk
    with dissolve
    "[mcname!c]" "…………"
    show takamina_talk at tana_right
    show takamina_talk:
        subpixel True pos (0.17, 0.08) zoom 0.75
    show takamina_side_talk at left
    with dissolve
    "Takamina" "Gemes juga ya, haha."
    hide takamina_talk
    hide takamina_side_talk
    with dissolve
    show fio_smile at fio_near_left
    show fio_smile:
        subpixel True xpos 1.15
    show fio_side_grin at left
    with dissolve
    fio "Maapin ya, kadang suka aneh emang anak ini."
    hide fio_smile
    hide fio_side_grin
    with dissolve
    show pia_date_talk at pia_near
    show pia_date_side_talk at left
    with dissolve
    pia "Aaaaaaaa~"
    hide pia_date_date_talk
    hide pia_date_side_talk
    with dissolve
    show takamina_talk at tana_right
    show takamina_talk:
        subpixel True pos (0.17, 0.08) zoom 0.75
    show fio_smile at fio_near_left
    show fio_smile:
        subpixel True xpos 1.15
    with dissolve
    "Semua Orang" "Hahahaha~"
    hide fio
    hide pia
    hide takamina
    with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Monas.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Akhirnya acara matsuri pun dibuka tepat pukul 10 pagi."
    $ quick_menu = False
    scene matsuri siang with Dissolve(2.0)
#HARUSNYA MATSURI SIANG
    $ quick_menu = True
    play sound "crowd_noise.mp3" loop fadein 1.0 volume (4.0)
    "Pengunjung mulai berdatangan."
    show takamina at tana_right
    show takamina:
        subpixel True pos (0.17, 0.08) zoom 0.75
    with dissolve
    show fio at fio_near_left
    show fio:
        subpixel True xpos 1.20
    with dissolve
    show pia_date at pia_near with dissolve
    show pia_date_talk at pia_near
    show pia_date_side_talk at left
    with dissolve
    pia "Weeeeeh rameeeeeeee."
    hide pia_date_talk
    hide pia_date_side_talk
    with dissolve
    show fio_talk at fio_near_left
    show fio_talk:
        subpixel True xpos 1.20
    show fio_side_talk at left
    with dissolve
    fio "Semangat guys!"
    hide fio_talk 
    hide fio_side_talk
    with dissolve
    show takamina_talk at tana_right
    show takamina_talk:
        subpixel True pos (0.17, 0.08) zoom 0.75
    show takamina_side_talk at left
    with dissolve
    "Takamina" "Yoooshaaaaaaaaa!!!"
    hide takamina_talk
    hide takamina_side_talk
    hide fio 
    hide pia_date
    hide takamina
    with dissolve
    stop sound
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Matsuri Malam.ogg" fadein 1.0
    play sound "audio/crowd_noise.mp3" loop fadein 1.0 volume (4.0)
    scene awan sore with Dissolve(1.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "Pukul 3 sore, semua jualan booth Pia, [mcname!c], Fiony dan Takamina pun ludes habis semua."
    $ quick_menu = False
    scene matsuri sore with Dissolve(2.0)
    show takamina at tana_right
    show takamina:
        subpixel True pos (0.17, 0.08) zoom 0.75
    with dissolve
    show fio at fio_near_left
    show fio:
        subpixel True xpos 1.20
    with dissolve
    show pia_date at pia_near
    show pia_date_talk at pia_near
    show pia_date_side_talk at left
    with dissolve
    $ quick_menu = True
    pia "OTSU ALLL, ABIS SEMUA WEEEEH!!!"
    hide pia_date_talk
    hide pia_date_side_talk
    with dissolve
    show fio_talk at fio_near_left
    show fio_talk:
        subpixel True xpos 1.20
    show fio_side_talk at left
    with dissolve
    fio "Hahahaha gak nyangka bakal selaku ini. Memang ke push karena nama \"Yang Mulia Piaraan\" sih ini mah."
    fio "Keren banget sih ga ada lawan."
    hide fio_talk
    hide fio_side_talk
    show takamina_talk at tana_right
    show takamina_talk:
        subpixel True pos (0.17, 0.08) zoom 0.75
    with dissolve
    "{size=-10}[mcname!c] & Takamina{/size}" "Kelaaaaaaas!!!!"
    hide takamina_talk
    hide takamina_side_talk
    with dissolve
    show pia_date_talk at pia_near
    show pia_date_side_talk at left
    with dissolve 
    pia "HEH!! APA SIH AHAHAHA!!"
    hide pia_date_talk 
    hide pia_date_side_talk
    with dissolve
    show fio_talk at fio_near_left
    show fio_talk:
        subpixel True xpos 1.20
    show fio_side_talk at left
    with dissolve
    fio "Dari tadi kamu sibuk mulu, istirahat dulu"
    fio "[mcname!c]! Gak peka, ajak Pia jalan-jalan keliling matsuri sana!"
    hide fio_talk
    hide fio_side_talk
    with dissolve
    "[mcname!c]" "Eeh. Terus gimana rapih-rapihnya…"
    show takamina_talk at tana_right
    show takamina_talk:
        subpixel True pos (0.17, 0.08) zoom 0.75
    show takamina_side_talk at left
    with dissolve
    "Takamina" "Aman, aku sama Fiony yang gantian beres-beres."
    "Takamina" "Kalian quality time aja, hehehehe."
    hide takamina_talk
    hide takamina_side_talk
    show pia_date_shock at pia_near
    show pia_date_side_shock at left
    with dissolve
    pia "Kakaaaaak~\n*Blush*"
    hide pia_date_side_shock with dissolve
    "[mcname!c]" "Huhuhu oke. Makasih ya Kak Takamina, Cepio."
    "{size=-5}Fiony & Takamina{/size}" "*Mengacungkan jempol*"
    hide fio 
    hide pia_date_shock
    hide pia_date
    hide takamina
    with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene matsuri sore with Dissolve(1.0)
    $ renpy.block_rollback()
    show pia_date at pia_near with dissolve
    $ quick_menu = True
    pia "*Menarik tangan [mcname!c]*"
    show pia_date_talk at pia_near
    show pia_date_side_talk at left
    with dissolve 
    pia "Mau ke situuuuuu~"
    hide pia_date_talk
    hide pia_date_side_talk
    with dissolve
    "[mcname!c]" "Eee… a-ayooo."
    hide pia_date with dissolve
    "[mcname!c] dan Pia pun berkeliling sembari membeli banyak jajanan seperti takoyaki, okonomiyaki, dan lain-lain."
    show takoyaki
    show takoyaki:
        pos (0.30, 0.8) zoom 0.22 
    show pia_date at pia_near with dissolve
    "[mcname!c]" "Itu mau kamu makan semua?"
    show pia_date_smile at pia_near
    show pia_date_side_smile at left
    with dissolve 
    pia "Amaaan. Perut aku ada ruangan tersendiri buat cemilan, huahahaha."
    hide takoyaki
    hide pia_date_smile
    hide pia_date_side_smile
    hide pia_date
    with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Beberapa menit kemudian..."
    $ quick_menu = False
    scene matsuri sore with Dissolve(2.0)
#Harusnya MATSURI SORE
    $ renpy.block_rollback()
    show pia_date at pia_near
    show pia_date_side at left
    with dissolve 
    $ quick_menu = True
    pia "......"
    show pia_date_talk at pia_near
    hide pia_date_side
    show pia_date_side_talk at left
    with dissolve
    pia "[mcname!c]....."
    pia "[mcname!c]......"
    hide pia_date_talk
    hide pia_date_side_talk
    with dissolve
    "[mcname!c]" "Apaan?"
    show pia_date_talk at pia_near
    show pia_date_side_talk at left
    with dissolve
    pia "Kenyang…\n*Sambil memegang tusuk takoyaki yang tinggal 1 buah*"
    hide pia_date_talk
    hide pia_date_side_talk
    with dissolve
    "[mcname!c]" "Aaaaaaammm~"
    "*[mcname!c] langsung memakan takoyaki yang sedang dipegang Pia*"
    show pia_date_shock at pia_near
    show pia_date_side_shock at left
    with dissolve 
    pia "!!!!\n*Blush*"
    hide pia_date_side_shock with dissolve
    "[mcname!c]" "Kaaan, pasti ga abis.\n*Sambil ngunyah*"
    show pia_date_smile at pia_near
    show pia_date_side_smile at left
    with dissolve
    pia "Hehehe~"
    hide pia_date_shock
    hide pia_date_smile 
    show pia_date at pia_near
    hide pia_date_side_smile
    with dissolve
    "[mcname!c]" "Mau ke mana lagi?"
    show pia_date_talk at pia_near
    hide pia_date_shock
    show pia_date_side_talk at left
    with dissolve
    pia "Jalan-jalan bentar, terus balik ke booth aja bantuin Cepio sama Takamina yuk."
    hide pia_date_talk
    hide pia_date_side_talk
    with dissolve
    "[mcname!c]" "Oke"
    hide pia_date with dissolve
    stop sound fadeout 1.0
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Sore.ogg" fadein 1.0
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Pukul 6 sore, [mcname!c] dan Pia kembali ke booth mereka."
    $ quick_menu = False
    scene matsuri malam with Dissolve(2.0)
#HARUSNYA MATSURI MALAM
    $ renpy.block_rollback()
    show takamina at tana_right
    show takamina:
        subpixel True pos (0.17, 0.08) zoom 0.75
    with dissolve
    show fio at fio_near_left
    show fio:
        subpixel True xpos 1.20
    with dissolve
    show pia_date at pia_near
    show pia_date_talk at pia_near
    show pia_date_side_talk at left
    with dissolve
    $ quick_menu = True
    pia "Weeeh udah rapih nih, siap pulang~"
    show fio_talk at fio_near_left
    show fio_talk:
        subpixel True xpos 1.20
    show fio_side_talk at left
    hide pia_date_side_talk
    hide pia_date_talk
    with dissolve
    fio "Pulang, enak aja! Mau jalan-jalan dulu."
    hide fio_talk 
    hide fio_side_talk
    with dissolve
    show takamina_talk at tana_right
    show takamina_talk:
        subpixel True pos (0.17, 0.08) zoom 0.75
    show takamina_side_talk at left
    with dissolve
    "Takamina" "Gimana kelilingnya?"
    show pia_date_smile at pia_near
    show pia_date_side_smile at left
    hide takamina_side_talk
    hide takamina_talk
    with dissolve
    pia "Ehehehe..."
    hide pia_date_smile
    hide pia_date_side_smile
    with dissolve
    show fio_talk at fio_near_left
    show fio_talk:
        subpixel True xpos 1.20
    show fio_side_talk at left
    with dissolve
    fio "Dari sini mau ke mana lagi deh?"
    hide fio_talk 
    hide fio_side_talk 
    with dissolve
    "[mcname!c]" "Gatau, tinggal nunggu acara kembang api aja sih ini."
    show fio_talk at fio_near_left
    show fio_talk:
        subpixel True xpos 1.20
    show fio_side_talk at left
    with dissolve
    fio "Pia, sini deh."
    fio "[mcname!c] kamu jauh-jauh dulu, aku mau ngobrol sama Pia sebentar"
    hide fio_talk 
    hide fio_side_talk 
    with dissolve
    "[mcname!c]" "Eeh… okee."
    $ quick_menu = False
    scene black with Dissolve(1.0) 
    scene matsuri malam with Dissolve(1.0)
    show takamina at tana_right
    show takamina:
        subpixel True pos (0.17, 0.08) zoom 0.75
    with dissolve
    show fio at fio_near_left
    show fio:
        subpixel True xpos 1.20
    with dissolve
    show pia_date at pia_near
    with dissolve
    show fio_talk at fio_near_left
    show fio_talk:
        subpixel True xpos 1.20
    show fio_side_talk at left
    with dissolve
    $ quick_menu = True
    show pia_date:
        xpos 0.57 
    with dissolve
    show key
    show key:
        pos (0.41, 0.68) zoom 0.12 
    with dissolve
    play sound "SFX - Key.mp3" volume (5.0)
    fio "Nih\n*Kasih kunci ke Pia*"
    hide fio_talk
    hide fio_side_talk
    show pia_date_talk at pia_near
    show pia_date_talk:
        xpos 0.57 
    show pia_date_side_talk at left
    with dissolve
    pia "Hah? Ini kunci apa?"
    hide key
    hide pia_date
    hide pia_date_talk
    hide pia_date_side_talk
    show pia_date at pia_near
    with dissolve
    show fio_smile at fio_near_left
    show fio_smile:
        subpixel True xpos 1.20
    show fio_side_smile at left
    with dissolve
    fio "Kunci pintu gedung DKV sama pintu rooftop, hehe."
    hide fio_smile 
    hide fio_side_smile
    with dissolve
    show pia_date_shock at pia_near
    show pia_date_side_shock at left
    with dissolve
    pia "HEEEEEEEEE~"
    pia "Kok Cepio bisa punya ini????"
    hide pia_date_shock
    hide pia_date_side_shock
    with dissolve
    show fio_talk at fio_near_left
    show fio_talk:
        subpixel True xpos 1.20
    show fio_side_talk at left
    with dissolve
    fio "Takamina anak BEM, dia ada kunci cadangan."
    fio "Ini aku pinjem dari Takamina, katanya gapapa."
    hide fio_talk
    hide fio_side_talk
    with dissolve
    show pia_date_talk at pia_near
    show pia_date_side_talk at left 
    with dissolve
    pia "Teruus?"
    hide pia_date_talk 
    hide pia_date_side_talk
    with dissolve
    show fio_smile at fio_near_left
    show fio_smile:
        subpixel True xpos 1.20
    show fio_side_grin at left
    with dissolve
    fio "Nonton kembang api kayaknya bagus deh dari rooftop, uhuk uhuk!"
    hide fio_smile 
    hide fio_side_grin
    with dissolve
    show pia_date_shock at pia_near
    show pia_date_side_shock at left
    with dissolve
    pia "Hahhhh??"
    hide pia_date_shock 
    hide pia_date_side_shock
    with dissolve
    show fio_talk at fio_near_left
    show fio_talk:
        subpixel True xpos 1.20
    show fio_side_talk at left
    with dissolve
    fio "Sana ajak [mcname!c], pemandangannya dari atas lebih bagus loh."
    hide fio_talk 
    hide fio_side_talk
    with dissolve
    show pia_date_talk at pia_near
    show pia_date_side_talk at left
    with dissolve
    pia "Terus kalian gimana?"
    hide pia_date_talk 
    hide pia_date_side_talk
    with dissolve
    show fio_talk at fio_near_left
    show fio_talk:
        subpixel True xpos 1.20
    show fio_side_talk at left
    with dissolve
    fio "Udaaaah, bawel Pia. Sana pergi."
    fio "[mcname!c]!!"
    fio "[mcname!c]!!"
    fio "Temenin Pia dong."
    hide fio_talk
    hide fio_side_talk
    with dissolve
    "[mcname!c]" "Ke mana?"
    show fio_talk at fio_near_left
    show fio_talk:
        subpixel True xpos 1.20
    show fio_side_talk at left
    with dissolve
    fio "Gatau tuh, ikutin Pia aja.\n*Mendorong Pia*"
    hide fio_talk
    hide fio_side_talk
    with dissolve
    show pia_date_shock at pia_near
    show pia_date_side_shock at left 
    with dissolve
    pia "Heeeeeeeeeee~"
    hide pia_date_side_shock with dissolve
    "[mcname!c]" "Mau ke mana?"
    show pia_date_talk at pia_near
    hide pia_date_shock
    hide pia_side_date_shock
    show pia_date_side_talk at left
    with dissolve
    pia "Umm… Ikut aku aja…" 
    hide pia_date_talk
    hide pia_date_side_talk
    with dissolve
    hide fio with dissolve
    hide pia_date with dissolve
    hide takamina with dissolve 
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene kampus malam with Dissolve(1.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "Pia dan [mcname!c] pun berjalan masuk ke gedung DKV."
    show pia_date at pia_near with dissolve
    "[mcname!c]" "Mau ngapain Pi? Kan udah dikunci kalo malem."
    show pia_date_talk at pia_near
    show pia_date_side_talk at left
    with dissolve
    pia "Aku ada kuncinya."
    hide pia_date_talk
    hide pia_date_side_talk
    with dissolve
    "[mcname!c]" "Heeeeeee dapet dari mana?"
    show pia_date_talk at pia_near
    show pia_date_side_talk at left
    with dissolve
    pia "Dipinjemin Takamina sama Cepio, hehe."
    hide pia_date_talk
    hide pia_date_side_talk 
    with dissolve
    "[mcname!c]" "Terus mau ke mana?"
    show pia_date_talk at pia_near
    show pia_date_side_talk at left
    with dissolve
    pia "Markas~"
    hide pia_date_talk 
    hide pia_date_side_talk
    with dissolve
    hide pia_date with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene lorong malam with Dissolve(1.0)
    $ renpy.block_rollback()
    show pia_date_sad at pia_near with dissolve
    show pia_date_shock at pia_near 
    show pia_date_side_shock at left
    with dissolve
    $ quick_menu = True
    pia "Eeeh gelap ya, kalo malem."
    hide pia_date_shock 
    hide pia_date_side_shock
    with dissolve
    "[mcname!c]" "Ya kalo terang siang sih Pi."
    show pia_date_shock at pia_near 
    show pia_date_side_shock at left
    with dissolve
    pia "Bukan gituuuuu. Ini sereeeeem kalo malem weeeeh!\n*Memegang erat tangan [mcname!c]*"
    hide pia_date_shock 
    hide pia_date_side_shock
    with dissolve
    "[mcname!c]" "Lah k-kamu yang ngajak ke sini, kok kamu yg takut?\n*blush*"
    "[mcname!c]" "Ahahaha~"
    show pia_date_silent at pia_near
    show pia_date_side_silent at left
    with dissolve
    pia "Bawel, buruan ke rooftop ih!"
    hide pia_date_silent 
    hide pia_date_side_silent
    with dissolve
    "[mcname!c]" "Kalo aku lari gimana?"
    show pia_date_sad at pia_near
    show pia_date_side_sad at left
    with dissolve
    pia "Kalo aku nangis gimana?"
    hide pia_date_side_sad
    with dissolve
    "[mcname!c]" "Iya, engga…. Ehehe."
    hide pia_date
    hide pia_date_sad
    with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    scene black with Dissolve(1.0)
    play music "audio/BGM_Rooftop Pia Malam.ogg" fadein 1.0 volume (2.0)
    scene rooftop malam with Dissolve(1.0)
    show pia_date at pia_near with dissolve
    $ renpy.block_rollback()
    show pia_date_talk at pia_near
    show pia_date_side_talk at left
    with dissolve
    $ quick_menu = True
    pia "HEEEEEEEEEE~"
    pia "KALO MALEM BAGUS JUGA YA PEMANDANGANNYA DARI ROOFTOP!"
    hide pia_date_talk
    hide pia_date_side_talk
    with dissolve
    "[mcname!c]" "Iya, ditambah lagi ada event begini jadi banyak cahaya gitu dari kejauhan."
    show pia_date_talk at pia_near
    show pia_date_side_talk at left
    with dissolve
    pia "Awwww… Iya cantik bangeeeeet."
    hide pia_date_talk 
    hide pia_date_side_talk
    with dissolve
    hide pia_date with dissolve
    "Pia dan [mcname!c] pun mulai duduk bersila di pinggir pagar sambil melihat acara dari jauh."
    show pia_date at pia_near with dissolve
    show pia_date_talk at pia_near
    show pia_date_side_talk at left
    with dissolve
    pia "Iiih lagi bon odori tuh di bawah."
    hide pia_date_talk 
    hide pia_date_side_talk
    with dissolve
    "[mcname!c]" "Iya…"
    "[mcname!c]" "Nyesel gak tuh ga ikut bon odori?"
    show pia_date_shock at pia_near
    show pia_date_side_shock at left
    with dissolve
    pia "Gak lah, enak di sini.\n*Blush*"
    hide pia_date_shock
    hide pia_date_side_shock
    with dissolve
    hide pia_date with dissolve
# Insert Chibi Pia nyender ke MC
    "Pia bersender ke [mcname!c]."
    "[mcname!c]" "*Blush*"
    show pia_date_side_talk at left with dissolve
    pia "[mcname!c], makasih ya. Berkat kamu, aku jadi banyak ngerasain hal menyenangkan selama kuliah di sini."
    hide pia_date_side_talk at left with dissolve
    "[mcname!c]" "Ahaha gak gitu, aku yang makasih."
    show pia_date_side_talk at left with dissolve
    pia "Tapi kamu selalu nurut, ngikutin kemauan anehku, support aku terus…"
    hide pia_date_side_talk with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene pia end no firework with Dissolve(1.0)
    scene pia end talk no firework with dissolve
    $ quick_menu = True
    pia "[mcname!c]! Makasih ya udah mau nemenin aku terus."
    $ quick_menu = False
    scene pia end no firework
    hide pia_side
    with dissolve
    $ quick_menu = True
    "[mcname!c]" "Sama-sama Pia, makasih udah mau selalu ada buat aku juga."
    $ quick_menu = False
    scene pia end talk no firework with dissolve
    $ quick_menu = True
    pia "Iiih harusnya itu kata-kata aku!!!"
    $ quick_menu = False
    scene pia end no firework with dissolve
    $ quick_menu = True
    "[mcname!c]" "Akulah si support system kamu itu~"
    "[mcname!c]" "Hahaha~"
    $ quick_menu = False
    scene pia end talk no firework with dissolve
    $ quick_menu = True
    pia "[mcname!c]..."
    $ quick_menu = False
    scene pia end no firework    
    with dissolve
    $ quick_menu = True
    "[mcname!c]" "Apaan??"
    $ quick_menu = False
    scene pia end talk no firework with dissolve
    $ quick_menu = True
    pia "Umm…"
    pia "[mcname!c], aku suka–"
    play sound "SFX - Hanabi.wav" loop
    $ quick_menu = False
    scene pia end talk with Dissolve(1.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "Suara kembang api pun mulai terdengar dan langit pun dipenuhi dengan cahaya indah."
    "Suara mereka pun kalah dengan bisingnya suara kembang api malam itu."
    $ quick_menu = False
    scene pia end smile with dissolve  
    $ quick_menu = True
    "[mcname!c] dan Pia bertatapan saling tersenyum sambil memandangi langit malam saat itu."
    "Malam itu…"
    "Menjadi malam yang tidak akan terlupakan untuk Pia dan [mcname!c]."
    stop sound fadeout 1.0
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    $ sukiyo.grant()
    show text "{color=#FFF}THE END{/color}" with Pause(4.0)
    play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
    jump credits