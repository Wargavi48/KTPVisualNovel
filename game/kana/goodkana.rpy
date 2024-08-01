label goodkana:
    #<TRUE ENDING END>
    
    #*CHOOSE*
    #AMBIL FLAYER
    #ABAIKAN FLAYER
    #
    #—---------------------------------------------------IF CHOSE A—----------------------------------------------
    #—-------------------------------------------------GOOD ENDING—-------------------------------------------
    hide matsuri
    hide club
    with dissolve
    show club at poster
    show club:
        pos (0.14, 0.17) zoom 0.36 
    with dissolve
    "[mcname!c]" "Hmmm, kayaknya kalau ajak Kana dia mau deh. Ya udah deh, aku ambil aja dulu."
    #*SKIP TO SCENE*
    #*BG KANTIN*
    hide club with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kantin.ogg" loop fadein 1.0
    scene kantin with Dissolve(1.0)
    $ quick_menu = True
    "[mcname!c]" "Eh maaf lama ya, tadi abis dari toilet hehe."
    show kana at kana_near_left_2
    show freya_talk at freya_near_right
    show freya_side_talk at left
    with dissolve
    freya "Cuci tangan ga?"
    hide freya_side_talk
    hide freya_talk
    show freya at freya_near_right
    with dissolve
    "[mcname!c]" "Ya cuci lah, masa enggak? Jorok banget ih."
    hide kana
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Hahaha, gapapa kita juga baru datang tadi kok."
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near_left_2
    with dissolve
    "[mcname!c]" "Eh kalian udah pesen makan? Aku mau pesen bentar ya."
    hide kana
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Udah tadi, tapi lama nunggu soalnya ngantri."
    hide kana_side_talk
    hide kana_talk
    hide freya
    show kana at kana_near_left_2
    show freya_talk at freya_near_right
    show freya_side_talk at left
    with dissolve
    freya "Iya, aku sama Naya udah pesen."
    hide freya_side_talk
    hide freya_talk
    show freya at freya_near_right
    with dissolve
    "[mcname!c]" "Oke aku pesen dulu ya."
    hide kana
    hide freya
    with dissolve
    #*CHOSE*
    menu:
        "Kamu memesan..."
        "Nasi Cumi Pak Sunny":
            jump goodkanaafterorder
        "Karedok Pak Vin":
            stop music fadeout 1.0
            $ quick_menu = False
            play music "BGM_Bad End.ogg" fadein 1.0
            "[mcname!c]" "Karedok Pak Vin kali ya,? Udah lama ga makan sayuran aku."
            "Ternyata sayuran yang dipake sama tukang dagangnya kebanyakan busuk semua dan hampir setengah mahasiswa/i keracunan dan dilarikan ke rumah sakit."
            scene black with dissolve
            "ADUH KALO MAU BELI SAYURAN, TANYA TANYA DULU DEH! TAKUTNYA BUSUK, MALAH KAYA GINI SEKARANG."
            scene black with dissolve
            show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(2.0)
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3"
            jump credits

        "Ayam Geprek Pak Hmmmm":
            stop music fadeout 1.0
            $ quick_menu = False
            play music "BGM_Bad End.ogg" fadein 1.0
            "[mcname!c]" "{i}Hmmm kayaknya makan ayam geprek Pak Addo enak deh, pengen yang pedes sesekali.{/i}"
            "Ternyata ayam yang kamu pesen terlalu pedes dan bikin kamu sakit perut sampe dilarikan ke rumah sakit."
            scene black with dissolve
            "ADUHHH KASIAN BANGET MASIH MUDA UDAH KE RS GARA GARA SENENG MAKAN PEDES, LAIN KALI JANGAN TERLALU PEDES YA!"
            scene black with dissolve
            show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(2.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3"
            jump credits

label goodkanaafterorder:
    #*CHOSE A*
    "[mcname!c]" "{i}Eh nyoba nasi cumi Pak Sunny kali ya? Katanya terkenal sampe masuk di subtitle gitu di beberapa film, nyobain ah.{/i}"
    "[mcname!c] pun memesan makanan dan kembali ke meja di mana Kana dan Freya berada."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    pause(1.0)
    scene kantin with Dissolve(1.0)
    $ quick_menu = True
    "[mcname!c]" "Eh maaf lama, tadi aku jadinya pesan nasi cumi Pak Sunny itu."
    show freya at freya_near_right
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Ooo yang katanya pernah masuk ke film-film itu ya?"
    hide kana_side_talk
    hide kana_talk
    hide freya
    show kana at kana_near_left_2
    show freya_talk at freya_near_right
    show freya_side_talk at left
    with dissolve
    freya "Ooo aku tau itu, katanya sih enak."
    hide freya_side_talk
    hide freya_talk
    show freya at freya_near_right
    with dissolve
    "[mcname!c]" "Iya yang itu. Aku nyobain sih, penasaran juga haha."
    hide freya
    show freya_talk at freya_near_right
    show freya_side_talk at left
    with dissolve
    freya "Eh itu di tasmu ada apaan [mcname!c]? Kok ada yang nongol sih? Dari tadi mau ambil tapi ga berani soalnya ga sopan gitu kalo ga ijin ke orangnya."
    hide freya_side_talk
    hide freya_talk
    show freya at freya_near_right
    with dissolve
    "[mcname!c]" "OWH IYA, INI!!!"
    "Dengan nada semangat [mcname!c] mengambil selembaran yang berada di tasnya."
    "[mcname!c]" "Jadi ini tuh ada rekrutmen buat masuk ke klub jejepangan gitu."
    "[mcname!c]" "Tadi liat sekilas, tapi aku ambil soalnya kayaknya seru gitu sih."
    hide freya
    show freya_talk at freya_near_right
    show freya_side_talk at left
    with dissolve
    freya "Oalah, Nay ini mah kesukaanmu tuh."
    hide freya_side_talk
    hide freya_talk
    show freya at freya_near_right
    show kana_confused at kana_near_left_2
    show kana_side_confused at left
    with dissolve
    kana "Ehh… Ummm keliatannya seru sih… tapi a-aku malu."
    hide kana_side_confused
    hide kana_confused
    hide freya
    show kana at kana_near_left_2
    show freya_awe at freya_near_right
    show freya_side_awe at left
    with dissolve
    freya "Alahhh, pake malu segala. Ini kesempatan, Nayaaaa. Biar kamu banyak temen jejepangan gitu."
    hide freya_side_awe
    hide freya_awe
    show freya at freya_near_right
    with dissolve
    "[mcname!c]" "Iya Nay ikut yuk, aku juga ikut."
    hide kana
    show kana_confused_blush at kana_near_left_2
    show kana_side_cry at left
    with dissolve
    kana "T-tapiiiiii."
    hide kana_side_cry with dissolve
    "[mcname!c]" "Gini deh, kamu ikut aja dulu. Kalo emang ga suka, nanti keluar aja. Nanti aku yang ngomong deh ke ketuanya, trial and error gitu."
    show kana_side_cry at left
    with dissolve
    kana "Emang bisa ya kaya gitu?"
    hide kana_side_cry
    hide kana_confused_blush
    hide freya
    show kana_confused_blush_sideeye at kana_near_left_2
    show freya_talk at freya_near_right
    show freya_side_talk at left
    with dissolve
    freya "Udah Nay, ikutan aja duluu."
    hide freya_side_talk
    hide freya_talk
    hide kana_confused_blush_sideeye
    show freya at freya_near_right
    show kana_confused_blush at kana_near_left_2
    with dissolve
    "[mcname!c]" "Iya Nayy, ikutan yaaa."
    hide kana_confused_blush
    show kana_confused at kana_near_left_2
    show kana_side_confused at left
    with dissolve
    kana "Ummm i-iya deh aku ikut aja dulu ya. Tapi kalau aku ga suka, aku ga join ya?"
    hide kana_side_confused
    show kana at kana_near_left_2
    hide kana_confused
    with dissolve
    "[mcname!c]" "NAHHHH GITU DONG."
    "Tak lama kemudian, makanan pun datang. Mereka bertiga menghabiskan makanan mereka dan membayarnya."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Sore.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Di perjalanan pulang, [mcname!c] dan Kana..."
    $ quick_menu = False
    scene lorong sore with Dissolve(2.0)
    show kana at kana_near 
    with dissolve
    $ quick_menu = True
    "[mcname!c]" "Eh Nay, nanti besok ya kita ke klubnya."
    show kana_confused at kana_near
    show kana_side_confused at left
    with dissolve
    kana "Ehhh aku masih belum siap, minggu depan aja deh."
    hide kana_side_confused
    with dissolve
    "[mcname!c]" "Kelamaan Nay, lagian batas pendaftaran cuma sampai lusa aja. Besok yaa, nanti aku tunggu di depan kampus. Dadahhhh."
    show kana_side_confused at left
    with dissolve
    kana "Ehhh…"
    show kana_confused_blush_sideeye at kana_near
    hide kana
    hide kana_confused
    hide kana_side_confused
    with dissolve
    "[mcname!c] pun pergi pulang ke kosan meninggalkan Kana yang sedikit kebingungan.."
    hide kana_confused_blush_sideeye
    with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" loop fadein 1.0
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Di kost..."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(2.0)
    $ quick_menu = True
    play sound "audio/ReceiveText.ogg" loop
    "[mcname!c] melihat ke arah HPnya yang berbunyi."
    stop sound
    "Saat membuka HPnya, ternyata ia mendapatkan notifikasi chat dari Kana."
    stop music fadeout 1.0
    $ quick_menu = False
    nvl clear
    play music "BGM_Happy + HP.ogg" fadein 1.0
    kana_nvl "Eh. B-besok kita reschedule aja gimana >_<"
    mc_nvl "G"
    kana_nvl "Iiiii kok gitu siih ayolah pleaseeeeeee..(QAQ)"
    mc_nvl "Ya udah, boleh"
    kana_nvl "Yeeee akhirnya, jadinya kapan?"
    mc_nvl "Minggu depan tapi kamu sendirian ya Nay, soalnya aku mau besok."
    kana_nvl "Iiiiihh, tapi kan."
    mc_nvl "Klo gmw ikut, gpp. Ga maksa."
    mc_nvl "Klo mw ikut, w tunggu jam 3 sore ya…"
    mc_nvl "Jangan telat, good night."
    kana_nvl "Ehhh..."
    nvl clear
    play sound "audio/ReceiveText.ogg" loop fadein 1.0
    scene kamar mc kota with dissolve
    $ quick_menu = True
    "HP [mcname!c] terus-terusan bersuara, suara notif tidak berhenti terdengar."
    stop sound
    "Hingga akhirnya [mcname!c] pun memilih untuk memasuki mode getar."
    "[mcname!c]" "{i}Hahaha biarin aja lah sesekali biar Kana juga mau. Kata Freya harus digituin dulu biar dia mau.{/i}"
    "[mcname!c] pun memilih untuk mengabaikan HPnya dan pergi tidur."
    nvl clear
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kampus Sore.ogg" loop fadein 1.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan sorenya..."
    $ quick_menu = False
    scene lorong sore with Dissolve(1.0)
    $ quick_menu = True
    "[mcname!c]" "Hmmmm bentar lagi jam 3, aku tinggal aja kali ya?"
    "Saat [mcname!c] akan pergi, dari kejauhan terdengar suara Kana berteriak."
    show kana_confused at kana_near
    show kana_side_confused at left
    with dissolve
    kana "Ehhh tungguuuuuu!!!! [mcname!u] TUNGGUUUU!!!"
    hide kana_side_confused
    with dissolve
    "[mcname!c]" "Nahhh datang juga."
    show kana_side_confused at left with dissolve
    kana "Ihh kamu kenapa sih ga bales chat aku? Sengaja ya bikin aku marah?"
    hide kana_side_confused
    show kana_angry at kana_near
    with dissolve
    "[mcname!c]" "Hahah, soalnya kata Freya kamu harus digituin sih biar mau, makanya aku diemin kamu dulu."
    show kana_side_confused at left
    hide kana_angry
    with dissolve
    kana "Iiii, kamu mah…"
    hide kana_side_confused with dissolve
    "[mcname!c] dan Kana pun pergi ke arah di mana klub jejepangan berada.."
    "[mcname!c]" "Kamu siap kan, Nay?"
    hide kana_confused
    show kana_shy_closeeye at kana_near
    show kana_side_shy at left
    with dissolve
    kana "Bentar bentar, aku mau narik nafas dulu…"
    hide kana_side_shy with dissolve
    "[mcname!c] melihat ke arah Kana yang sedang mempersiapkan dirinya untuk melanjutkan masuk ke arah ruangan jejepangan, ia pun melihat tangannya yang sedang membuat kata kanji orang di telapak tangannya."
    "[mcname!c]" "{i}Haaaaa… Segugup apa deh dia…{/i}"
    hide kana_shy_closeeye
    show kana_confused at kana_near
    with dissolve
    "[mcname!c]" "Ahhh lama Nay ayooooo."
    hide kana_confused with dissolve
    "Tak sabar dengan Kana, [mcname!c] pun memaksa Kana untuk segera masuk ke ruangan klub jejepangan. Saat mendekati ruangan, terdengar suara yang cukup ramai."
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    #???( TONO )
    "???" "Woyyy lu mau ke mana kocakkkk!"
    hide tana_side_talk
    hide tana_talk
    with dissolve
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    #???( PIA )
    "???" "Ahahaha!"
    hide pia_side_talk
    hide pia_talk
    show kana_confused_blush at kana_near
    show kana_side_cry at left
    with dissolve
    kana "K-kelihatannya rame banget ya [mcname!c], kita pulang aja yuk? Lain kali aja."
    hide kana_side_cry
    with dissolve
    "[mcname!c]" "Udah lah namanya juga klub, yuk masuk. Permisiii~"
    hide kana_confused_blush with dissolve
    "[mcname!c] pun masuk ke arah ruangan klub. Kana panik dan mencoba untuk menghentikan [mcname!c], akan tetapi [mcname!c] telah memasuki ruangan terlebih dahulu."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    play music "BGM_UKM.ogg" fadein 1.0
    scene ruang ukm sore with Dissolve(1.0)
    $ quick_menu = True
    "Suasa ruangan tiba-tiba hening, akan tetapi terlihat wajah yang agak familiar di sana."
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    #??(TONO)
    "???" "Eeehhh elo!??"
    hide tana_side_talk
    hide tana_talk
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Eeeh?"
    "Tono langsung pergi ke arah belakang [mcname!c], di mana Kana bersembunyi."
    hide tana
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    #???(TONO)
    "???" "Elu kan yang waktu itu menghindar ya? Akhirnya dateng juga, udah gue tungguin loh."
    hide tana_side_talk
    hide tana_talk
    with dissolve
    show tana at tana_near
    show kana_shy_talk at kana_near_left_2
    show kana_side_cry at left
    with dissolve
    kana "Eeehh, I-iya hehe."
    hide kana_side_cry with dissolve
    "[mcname!c]" "Nay, santai aja napa."
    show kana_shy at kana_near_left_2
    show tana at tana_near
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    #???(PIA)
    "???" "Ton, dia siapa?"
    hide pia_side_talk
    hide pia_talk
    hide tana
    show pia at pia_near_right
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    #???(TONO)
    "???" "Ooohhh Pii. Ini loh yang waktu itu aku ceritain yang suka ngechant sama wotagei itu loh, ini orangnya."
    hide tana_side_talk
    hide tana_talk
    hide pia
    show tana at tana_near
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    #???(PIA)
    "???" "Oohhh ini toh."
    hide pia_side_talk
    hide pia_talk
    show pia at pia_near_right
    with dissolve
    "[mcname!c]" "Eeehh ummm sorry, ini klub jejepangan kan?"
    #???(TANA)
    hide tana
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    "???" "Iya kok kalian ga salah masuk, lo kan yang waktu itu di depan kampus ya?"
    hide tana_side_talk
    hide tana_talk
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Iya namaku [mcname!c], salam kenal ya. "
    "[mcname!c] melihat ke arah Pia. Sosoknya yang enerjik, kecil serta lucu membuatnya teringat dengan kucing di rumahnya…"
    hide pia
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    $ pia_name = "Pia"
    pia "Btw kenalin namaku Pia Meraleo. Panggil Pia aja."
    hide pia_side_talk
    hide pia_talk
    hide tana
    show pia at pia_near_right
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    $ tono_name = "Tana"
    tana "Owh iya sampe lupa haha, kenalin juga gue Tana Nona. Salam kenal ya guys."
    hide tana_side_talk
    hide tana_talk
    hide pia
    show tana at tana_near
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Panggil dia Tono aja ya, hahaha."
    hide pia_side_talk
    hide pia_talk
    hide tana
    show pia at pia_near_right
    show tana_angry at tana_near
    show tana_side_angry at left
    with dissolve
    tana "Apaan sih kocak, main ganti nama gitu. Lama-lama gue laporin lu pencemaran nama baik."
    hide tana_side_angry
    hide tana_angry
    hide pia
    hide kana_shy_talk
    show tana at tana_near
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Ahahahaha, emang berani? Eh btw kamu siapa namanya?"
    hide pia_side_talk
    hide pia_talk
    show pia at pia_near_right
    hide kana_shy
    show kana_shy_talk at kana_near_left_2
    show kana_side_cry at left
    with dissolve
    kana "Eeehh… Uumm aku Kana."
    hide kana_shy_talk
    hide kana_side_cry
    show kana_shy at kana_near_left_2
    with dissolve
    "[mcname!c]" "Maaf ya dia gugup, Nay ayoo lah."
    hide kana_shy at kana_near_left_2
    show kana_shy_talk at kana_near_left_2
    show kana_side_cry at left
    with dissolve
    kana "T-tapii.."
    hide kana_side_cry
    hide kana_shy_talk at kana_near_left_2
    hide pia
    show kana_shy at kana_near_left_2
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Eh kamu masuk jurusan apaan?"
    hide pia_side_talk
    hide pia_talk
    hide kana_shy
    show pia at pia_near_right
    show kana_shy_talk at kana_near_left_2
    show kana_side_cry at left
    with dissolve
    kana "A-aku masuk ke jurusan HI. "
    hide kana_side_cry
    hide kana_shy_talk
    hide tana
    show kana_shy at kana_near_left_2
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Wihhh anak HI. aku masuk pertanian, kalau yang pendek satu ini masuk ke DKV."
    hide tana_side_talk
    hide tana_talk
    hide pia
    show tana at tana_near
    show pia_silent at pia_near_right
    show pia_side_silent at left
    with dissolve
    pia "AKU GA PENDEK!!"
    hide pia_side_silent
    hide pia_silent
    hide kana_shy
    hide tana
    with dissolve
    "Pia menjawab dengan nada dan ekspresi marah, membuatnya terlihat semakin lucu. [mcname!c] hanya tertawa melihat mereka bertengkar satu sama lain."
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Jadi kalian ke sini abis liat flyer itu kan? Kalian mau masuk kan ke klub ini? Mau bantu juga di event nanti yang akan datang kan?"
    hide tana_side_talk
    hide tana_talk
    show tana at tana_near
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Santai napa? Kasian tuh langsung dikasih pertanyaan gitu."
    hide pia_side_talk
    hide pia_talk
    show pia at pia_near_right
    with dissolve
    "[mcname!c]" "Kalau aku iya haha, tapi kalau Kana.."
    show kana_shy at kana_near_left_2 
    with dissolve
    "[mcname!c] melihat ke arah Kana diikuti oleh Tana dan Pia."
    hide kana_shy
    show kana_shy_talk at kana_near_left_2
    show kana_side_cry at left
    with dissolve
    kana "A-aku mau liat-liat dulu kalo boleh."
    hide kana_side_cry
    hide kana_shy_talk
    hide pia
    show kana_shy at kana_near_left_2
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Boleh kok, boleh pake bangettt."
    pia "Kamu liat-liat aja juga gapapa kok, apalagi nanti kalau di akhir-akhir ikutan join."
    hide pia_side_talk 
    hide pia_talk 
    show pia_smile at pia_near_right 
    show pia_side_smile at left 
    with dissolve
    pia "Soalnya kita juga lagi perlu satu orang lagi nih dan kayaknya kamu cocok deh."
    hide pia_side_talk
    hide pia_talk
    hide kana_shy at kana_near_left_2
    show pia at pia_near_right
    show kana_confused at kana_near_left_2
    show kana_side_confused at left
    with dissolve
    kana "Kurang satu orang?"
    hide kana_side_confused
    hide pia
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Iya kurang satu lagi buat iku-"
    hide pia_side_talk
    with dissolve
    "Mungkin karena Tana tau betapa malunya Kana untuk menunjukkan sifat wibunya, tanpa membiarkan Pia menyelesaikan kalimatnya, Tana memotong omongan Pia."
    hide pia_talk
    hide tana
    show pia at pia_near_right
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Buat ikut panitia ya… hahaha buat ikut panitia event nanti, iya kan Pia? Hahaha."
    hide tana_side_talk
    hide tana_talk
    hide pia
    show tana at tana_near
    show pia_shock at pia_near_right
    show pia_side_shock at left
    with dissolve
    pia "Eh? I-iya."
    hide pia_side_shock
    hide pia_shock
    hide tana
    hide kana_confused
    show kana at kana_near_left_2
    show pia at pia_near_right
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Iya jadi ada event jejepangan yang bakalan diadain sama kampus dan kerja sama dengan pihak-pihak lain juga, makanya kita lagi lumayan sibuk nyari panitia sama tenaga tambahan. Kalian mau ikut kan?"
    hide tana_side_talk
    hide tana_talk
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Waahhhhh, iya iya aku mau ikut. Nay ayo ikut bantu-bantu dikit aja biar tau, seru loh ikut kaya gini tuh. "
    hide pia
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Iya kalo mau bantu gapapa kok, ga bakalan dimarahin atau diapain kok tenang aja."
    hide pia_side_talk
    hide pia_talk
    hide kana
    show pia at pia_near_right
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Ummm, aku mikir-mikir dulu deh ya…."
    hide kana_side_talk
    hide kana_talk
    hide tana
    show kana at kana_near_left_2
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Ayolah brooo, gue tau kalau lu tuh suka jejepangan. Dijamin deh ga bakalan nyesel, kalau nyesel nanti Pia traktir buat beli merch di event itu deh gimana?"
    hide tana_side_talk
    hide tana_talk
    hide pia
    show tana at tana_near
    show pia_silent at pia_near_right
    show pia_side_silent at left
    with dissolve
    pia "Kok jadi gue sihhh, Ton."
    hide pia_side_silent
    hide tana
    show tana_laugh at tana_near
    show tana_side_laugh at left
    with dissolve
    tana "Ahahaha!"
    hide tana_side_laugh
    hide tana_laugh
    show tana at tana_near
    with dissolve
    "[mcname!c]" "EH GAS KALI YA."
    hide kana
    show kana_drylaugh at kana_near_left_2
    show kana_side_drylaugh at left
    with dissolve
    kana "Hahaha"
    hide kana_side_drylaugh
    hide kana_drylaugh
    show kana at kana_near_left_2
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Nahhhh gitu dong ketawa santai aja dong. Kita kan ga gigit kecuali Si Pia Meraleo itu tuh ati-ati aja, ada LEOnya soalnya xixixi."
    hide tana_side_talk
    hide tana_talk
    hide pia_silent
    show tana at tana_near
    show pia_silent at pia_near_right
    show pia_side_silent at left
    with dissolve
    pia "Ton… Lawakan lu kayak bapak-bapak dah, ga lucu."
    hide pia_side_silent
    hide pia_silent
    hide tana
    show pia at pia_near_right
    show tana_angry at tana_near
    show tana_side_angry at left
    with dissolve
    tana "Hargain napa, udah susah-susah gue bikin jokes."
    hide tana_side_angry
    hide tana_angry
    hide kana
    show tana at tana_near
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Mau berapa? Harganya 2 ribu cukup ga ya, hehe."
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near_left_2
    with dissolve
    "[mcname!c]" "Tumben lu bales ngejokes, Nay?"
    hide kana
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Heheh keliatannya mereka asik sih, hehe."
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near_left_2
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Asik lahhhh, pake bangetttt."
    hide tana_side_talk
    hide tana_talk
    hide pia
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Iya dong siapa dulu, gueee gitu loh."
    hide pia_side_talk
    hide pia_talk
    show pia at pia_near_right
    with dissolve
    "[mcname!c]" "Kita ga diajak nih?"
    hide tana
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Iya biarin aja, dia agak freek emang."
    hide tana_side_talk
    hide tana_talk
    hide kana
    show tana at tana_near
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Okee noted dah… Pia orangnya agak freak. "
    hide kana_side_talk
    hide kana_talk
    hide pia
    show kana at kana_near_left_2
    show pia_sad at pia_near_right
    show pia_side_sad at left
    with dissolve
    pia "Ehhhh jangan dong, kok gitu sihhh."
    hide pia_side_sad
    hide kana
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Hahahaha, iya iya enggak. Santai aja, kalian kan nyuruh aku santai."
    hide kana_side_talk
    hide kana_talk
    hide pia_smile
    hide pia_sad
    show kana at kana_near_left_2
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "I-iya sih…"
    hide pia_side_smile
    hide pia_side_talk
    hide pia_talk
    hide kana
    hide tana
    show tana_laugh at tana_near
    show kana_smile at kana_near_left_2
    show pia_smile at pia_near_right
    with dissolve
    "Mereka menghabiskan waktu di sore hari itu dengan berbincang bersama dan mulai mengenal satu sama lain lebih dalam."
    "Ada juga beberapa pembicaraan mengenai event yang akan datang dan apa saja tugas yang akan dilakukan oleh [mcname!c] dan Kana."
    stop music fadeout 1.0
    #*SKIP SCENE*
    #*BG KAMAR KOS MALAM*
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" loop fadein 1.0
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Malam itu..."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(2.0)
    $ quick_menu = True
    play sound "audio/SFX - Telephone.mp3" loop
    "Saat sedang tiduran, HP [mcname!c] berdering dengan terus menerus."
    show kana_calling at ui_handphone with dissolve
    "Saat melihat HPnya tersebut, ternyata yang menelepon [mcname!c] adalah Kana."
    stop sound
    hide kana_calling
    show kana_connect at ui_handphone
    with dissolve
    "[mcname!c]" "Kenapa Nay?"
    show kana_side_talk at left with dissolve
    kana "Nahhh akhirnya diangkat juga, lagi sibuk kah?"
    hide kana_side_talk with dissolve
    "[mcname!c]" "Heheh maaf tadi aku lagi main game, kenapa?"
    show kana_side_confused at left with dissolve
    kana "A-aku mau jujur sama kamu boleh? Ini penting banget buat ke depannya."
    hide kana_side_confused with dissolve
    "[mcname!c]" "{i}Waduhhh, kenapa ini kok Si Kana tiba-tiba kaya gini? Aduhhh kok gue jadi gugup gini?{/i}"
    "[mcname!c]" "I-iya Nay, kenapa tumben kok jadi serius gini."
    show kana_side_shy at left with dissolve
    kana "Se-sebenernya…"
    kana "A-akuuu…"
    kana "Aku…tuhhh…pengen…"
    hide kana_side_shy with dissolve
    "[mcname!c]" "Nay…?"
    show kana_side_shy at left with dissolve
    kana "Jadi…aku tuh pengen ikut juga di kepanitiaan…"
    hide kana_side_shy
    show kana_side_smile at left
    with dissolve
    kana "Fiuuuuhhh, akhirnya bisa juga. Dari tadi aku gugup tau mau ngomong itu, hahaha. Jadi kamu juga ikut kan [mcname!c]?"
    hide kana_side_smile with dissolve
    "[mcname!c]" "{i}Oalahh ternyata Kana mau ngomongin itu… Kukira mau ngomong apaan. Aduhhhh aku ke-PDan, aaaaaaa~{/i}"
    show kana_side_confused at left with dissolve
    kana "[mcname!c]? Kok diem?"
    hide kana_side_confused with dissolve
    "[mcname!c]" "Eh… e-enggak kok. Wahhh tumben kamu mau, alasannya apaan dah Nay?"
    show kana_side_talk at left with dissolve
    kana "Soalnya mereka kelihatannya asik gitu, kayaknya aku bisa deket deh sama mereka. Jarang banget aku ngerasain kaya gini sih selain sama Freya..."
    hide kana_side_talk with dissolve
    "Kana memelankan suaranya seperti sengaja tidak ingin terdengar oleh [mcname!c]."
    show kana_side_shy at left with dissolve
    kana "Sama kamu juga…"
    hide kana_side_shy with dissolve
    "[mcname!c]" "Hmmm Nay?"
    show kana_side_shy_smile at left with dissolve
    kana "Gapapa kok, pokoknya aku ikut kepanitiaan juga ya. Gitu aja ya, dadah selamat malaamm."
    hide kana_side_shy_smile with dissolve
    hide kana_connect at ui_handphone
    with dissolve
    "[mcname!c] terdiam."
    "[mcname!c]" "Ahhhhh… Kenapa aku malah deg degan kayak gitu sih, udah lah mendingan tidur."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_UKM.ogg" loop fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya..."
    $ quick_menu = False
    scene ruang ukm with Dissolve(2.0)
    $ quick_menu = True
    "Beberapa hari kemudian Kana dan [mcname!c] pun lolos dalam seleksi kepanitian dan mereka datang ke ruangan klub untuk rapat."
    "Di sana ada Tana dan Pia yang sudah menunggu mereka bersama dengan anggota panitia lainnya."
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Okee udah datang semuanya nih, mulai aja kali ya?"
    hide tana_side_talk
    hide tana_talk
    with dissolve
    "Rapat pun dimulai, rapat kali ini berlangsung cukup lama karena ada beberapa panitia tambahan."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Sore.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Beberapa jam kemudian..."
    $ quick_menu = False
    scene ruang ukm sore with Dissolve(2.0)
    $ quick_menu = True
    "Di akhir rapat, Pia dan Tana memanggil Kana dan [mcname!c]."
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Jadi gimana rapat pertama kalian? Seru kan?"
    hide tana_side_talk
    hide tana_talk
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Seruu sihh… tapi ga tau nanti pas kerjanya, hahaha."
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Santai aja nanti kan bareng-bareng, btw Kana aku seneng banget kamu ikut. Soalnya kukira ga bakalan ikut, kenapa tuh tiba-tiba kalo boleh tau?"
    hide pia_side_talk
    hide pia_talk
    show pia at pia_near_right
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Gapapa hehe, pengen ikut aja soalnya seru pas kemarin sama kalian."
    hide kana_side_talk
    hide kana_talk
    hide tana
    show kana at kana_near_left_2
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Iya lah kita mah asik, kapan kita ga asik ya Pii?"
    hide tana_side_talk
    hide tana_talk
    hide pia
    show tana at tana_near
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Kali ini gue setuju sama lu, Ton."
    hide pia_side_talk
    hide pia_talk
    hide tana
    show pia at pia_near_right
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Nahh kan, Pia aja setuju…"
    hide tana_side_talk
    hide tana_talk
    show tana_silent at tana_near
    show tana_side_idle at left
    with dissolve
    tana "........."
    hide tana_side_idle
    hide tana_silent
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Kok kali ini doang sih, Pi? Biasanya nggak, gitu?"
    hide tana_side_angry_2
    hide tana_angry_2
    hide pia
    show tana_angry at tana_near
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Hehehe~"
    hide pia_side_talk
    hide pia_talk
    hide tana_angry
    show pia at pia_near_right
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Ahhhh elah kocak."
    hide tana_side_angry_2
    hide tana_angry_2
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Hahaha. Eh mau tanya dong, ini kan di eventnya pasti ada lomba ya? Panitia panitia boleh ikut lombanya kah?"
    hide tana
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Boleh lah, emang lu mau ikutan lomba apaan dah?"
    hide tana_side_talk
    hide tana_talk
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Kayaknya pengen ikut lomba cosplay deh, ahaha."
    hide pia
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Widihhhh semangat aja deh, asal jangan keteteran kerjaan panitianya."
    hide pia_side_talk
    hide pia_talk
    show pia at pia_near_right
    with dissolve
    "[mcname!c]" "Aman aja."
    hide pia
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Eh Kana, mending kamu ikut lomba juga yuk, bareng aku sama Tono."
    hide pia_side_talk
    hide pia_talk
    hide kana
    show pia at pia_near_right
    show kana_confused at kana_near_left_2
    show kana_side_confused at left
    with dissolve
    kana "HA!!!?? LOMBA!!!???"
    hide kana_side_confused with dissolve
    "Tiba-tiba Kana berteriak dan membuat Tana, Pia, serta [mcname!c] kaget."
    show kana_side_confused at left
    with dissolve
    kana "Engga gak gak. Ga mau dan ga mungkin aku ikut lomba sama kalian, pokoknya enggaaak…"
    hide kana_side_confused
    hide tana
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Aduhhh Piaaa. Kan udah gw bilang, jangan tanya ke Kana langsung. Dia ini maluan orangnya."
    hide tana_side_talk
    hide tana_talk
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Emang lomba apaan ya?"
    hide tana
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Lomba idol gituuu. Jadi kan event ini kerja sama dengan idol organization, terus mereka juga sekalian nyari talent buat direkrut gitu."
    hide tana_side_talk
    hide tana_talk
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Wahhhhh… Seru tuh Nay, kamu harus ikutan. Ayooo!"
    show kana_side_confused at left
    with dissolve
    kana "HA!?? IDOL!??? Hahaha ga ga ga, pokoknya ga mau… Malu tau di depan banyak orang tuh."
    hide kana_side_confused
    hide tana
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Alah malu-malu, waktu itu aja lu di event jejepangan teriak paling kenceng gitu."
    hide tana_side_talk
    hide tana_talk
    show tana at tana_near
    show kana_side_confused at left
    with dissolve
    kana "Waktu itu kan beda..."
    hide kana_side_confused
    hide tana
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Alaahhh sama aja, beda dari mana? Lu ga sadar ya, kita yang lagi perform sama orang-orang lainnya tuh kadang liat lu gara-gara lu paling semangat diantara para penonton."
    hide tana_side_talk
    hide tana_talk
    hide pia
    show tana at tana_near
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Iya aku juga lihat rekaman dari Si Tono, ada kamu lagi wotagei juga. Udah kamu tuh cocok tau, suara kamu juga kedengeran ademmm banget. Cocok pokoknya, coba dulu yaaaa.."
    hide pia_side_talk
    hide pia_talk
    show pia at pia_near_right
    show kana_side_confused at left
    with dissolve
    kana "Ga ga ga, pokoknya ga mau."
    hide kana_side_confused
    hide tana
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Ayolah Kana, ikut yaa cobain dulu deh. Nanti kalo emang ga suka atau ga mau, gapapa. Satu minggu dulu deh, gimana?"
    hide tana_side_talk
    hide tana_talk
    hide kana_confused
    show tana at tana_near
    show kana_shy_talk at kana_near_left_2
    show kana_side_cry at left
    with dissolve
    kana "T-tapiii"
    hide kana_side_cry
    hide kana_shy_talk
    show kana_shy at kana_near_left_2
    with dissolve
    "[mcname!c]" "Ayolah Nayyy, pleaseeeee~"
    "Baik [mcname!c], Pia, serta Tana, memohon dengan sangat… Membuat Kana semakin terdesak."
    "Kana pun mau tidak mau mengiyakan hal itu, akan tetapi dengan beberapa syarat."
    hide kana_shy
    show kana_shy_talk at kana_near_left_2
    show kana_side_cry at left
    with dissolve
    kana "Aaaaaaa… Iya deh iya, tapi [mcname!c] harus ikut kapan pun pas latihan. Dan kalo aku ga mau lanjut, aku udahan yaa."
    hide kana_side_cry
    hide kana_shy_talk
    hide pia
    hide tana
    show kana_shy at kana_near_left_2
    show pia_smile at pia_near_right
    show tana_laugh at tana_near
    with dissolve
    "{size=-5}Pia & Tono{/size}" "“Yessss!!"
    hide pia_smile
    hide tana_laugh
    hide kana_shy
    with dissolve
    "Tana dan Pia merayakan hari itu karena akhirnya mereka bisa mendaftarkan diri mereka ke dalam lomba yang mereka inginkan."
    "Setelah itu Kana, [mcname!c], Tana, dan Pia mengerjakan tugas yang telah diberikan oleh ketua panitia."
    stop music fadeout 1.0
    $ quick_menu = False
    #*SKIP TO SCENE*
    #*BG KOS MALAM*
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" loop fadein 1.0
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Di kost..."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(2.0)
    $ quick_menu = True
    play sound "audio/ReceiveText.ogg" loop
    "[mcname!c] melihat ke arah HPnya yang berbunyi."
    "Di saat [mcname!c] sedang beristirahat, terdengar suara HPnya yang tidak pernah berhenti bergetar sejak ia selesai mandi."
    stop sound fadeout 1.0
    "[mcname!c]" "Aduhhh ini siapa sih, dari tadi notif jebol gini."
    #*CHANGE SCENE*
    $ quick_menu = False
    stop music fadeout 1.0
    nvl clear
    play music "BGM_Happy + HP.ogg" fadein 1.0
    tana_nvl "Eh ini group buat kita yaa. Buat bahas latihan dan bahas yang lain-lain juga lah, biar ga usah ngechat satu-satu."
    pia_nvl "Hadeehhh. Lu belum ijin dulu kan ke yang lain, Ton?"
    tana_nvl "Alah ga usah lah, kan temen ini. Ngapain sampe segitunya sih Pii."
    pia_nvl "MANNER TON, MANNER, ah elah."
    tana_nvl "Aaaaaaa….udah lah biar ga ribet juga, {color=#0000ff}@Kana{/color} & {color=#0000ff}@[mcname!c]{/color} woiii keluar napa? Jangan diem-diem ae"
    kana_nvl "Hehehe, seru liat kalian berantem. Aku baru selesai beres-beres, ga usah dimarahin napa."
    mc_nvl "Iya nih, dikira kita ini nolep apa ya, yang sering main HP."
    pia_nvl "Iya emang gitu Si Tono Tono mah, maklumin yaa."
    mc_nvl "Ooooo pantess aja, ya udah lah ya gapapa."
    kana_nvl "Oke deh Pii."
    tana_nvl "Aalahhh gue lagi, gue lagi. Gue aja terussss."
    pia_nvl "Hahah"
    mc_nvl "Jadi mau ngapain nih?"
    tana_nvl "Jadiiii giniii…"
    scene kamar mc kota with Dissolve(0.3)
    $ quick_menu = True
    "Tana pun menceritakan rencana dia untuk latihan persiapan lomba yang akan datang. Rencananya akan latihan seminggu 3-4x, meliputi latihan dance dan latihan bernyanyi."
    "Tempat latihan akan diberi tahu nanti, untuk sementara akan menggunakan ruangan klub untuk latihan terlebih dahulu."
    $ quick_menu = False
    tana_nvl "Jadii gituu sih, gimana? Setuju kan? KAN!!???"
    pia_nvl "Iya gue sih setuju, kamu gimana Kana?"
    kana_nvl "Ummm… Boleh sih, tapi [mcname!c] juga ikut nemenin kan? Inget perjanjian awal ya, kalau dia ga ikut aku juga enggak."
    mc_nvl "Iya iya, aku ikut nemenin kok."
    mc_nvl "Kalo inget, hahahahha."
    kana_nvl "Iiiiiihhhh"
    tana_nvl "Ayolah jangan gitu, please lah bantuin."
    mc_nvl "Iya iya, nanti aku datang kok. Aman aja."
    pia_nvl "Nahhh gitu dong. Ya udah ya, nanti ketemuan di ruangan klub ya."
    nvl clear
    stop music fadeout 1.0
    $ quick_menu = False
    scene kamar mc kota with dissolve
    #*SKIP TO SCENE*
    #*BG RUANG KLUB*
    scene black with Dissolve(1.0)
    play music "audio/BGM_UKM.ogg" loop fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya..."
    $ quick_menu = False
    scene ruang ukm with Dissolve(2.0)
    $ quick_menu = True
    "Kana, Tana, serta Pia mulai melakukan latihannya ditemani oleh [mcname!c]."
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Oookeee siap yaa."
    hide tana_side_talk
    hide tana_talk
    show tana at tana_near
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "SIAPPP MA BROOOO!"
    hide pia_side_talk
    hide pia_talk
    show pia at pia_near_right
    show kana at kana_near_left_2
    show kana_side at left
    with dissolve
    kana "...."
    hide kana_side
    hide tana
    show tana_confused at tana_near
    show tana_side_confused at left
    with dissolve
    tana "Kana?"
    hide tana_side_confused
    hide tana_confused
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Nayyyy!"
    hide kana
    show kana_shy_talk at kana_near_left_2
    show kana_side_cry at left
    with dissolve
    kana "Huh? K-kenapa ya?"
    hide kana_side_cry
    hide kana_shy_talk
    show kana_shy at kana_near_left_2
    with dissolve
    "[mcname!c]" "Nay u ok? Tadi dipanggil sama Tono ga nyaut, kamu gapapa kan?"
    hide kana_shy
    show kana_shy_talk at kana_near_left_2
    show kana_side_cry at left
    with dissolve
    kana "Gapapa kok cuma gugup aja. Takut gimana kalo nanti aku salah, gimana kalo nanti aku ketinggalan, gimana kalo nanti aku…"
    hide kana_side_cry
    hide kana_shy_talk
    show kana_shy at kana_near_left_2
    with dissolve
    "[mcname!c]" "NAYA!!"
    "[mcname!c] berteriak cukup kencang hingga Pia dan Tana pun terkejut dengan suara [mcname!c]."
    "[mcname!c]" "KANAIA ASA, please don't be like that. It’s ok to make mistakes, mistakes happen. Santai aja Nay, mereka ga bakalan salahin kamu kok. Kalaupun mereka berani, bakal kugetok mereka kok. Jadi just be you, ok?"
    hide kana_shy
    show kana_shy_talk at kana_near_left_2
    show kana_side_cry at left
    with dissolve
    kana "T-tapi…"
    hide kana_side_cry
    hide kana_shy_talk
    show kana_shy at kana_near_left_2
    with dissolve
    "[mcname!c]" "Ga ada tapi-tapian, sekarang kamu coba dulu. Ga usah malu, ga ada siapa-siapa kok di sini."
    hide pia
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Iya Kana. Kita ga bakalan salahin kamu kok, ga bakalan pernah."
    pia "Asal kamu tau ya Kana, dulu Si Tono itu pertama kali nyoba nyanyi suaranya aneh bangettt. Sampe satpam dateng katanya dapat laporan ada suara aneh gitu, hahaha."
    hide pia_side_talk
    hide pia_talk
    hide tana
    show pia at pia_near_right
    show tana_angry at tana_near
    show tana_side_angry at left
    with dissolve
    tana "Iiiiihhhh Piaaaa, katanya janji ga bakalan bilang ke siapa-siapa."
    hide tana_side_angry
    hide tana_angry
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Oke kalau gitu dulu juga pas Si Pia Pia itu ngedance beuhhh, jatuh terus brooo. Mana nangis juga, aduhhh dede kecil nangisss."
    hide tana_side_talk
    hide tana_talk
    hide pia
    show tana at tana_near
    show pia_silent at pia_near_right
    show pia_side_silent at left
    with dissolve
    pia "Aaaahhh lu juga malah bales ah Ton."
    hide pia_side_silent
    hide pia_silent
    hide tana
    show pia at pia_near_right
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Hehehe 1-1."
    hide tana_side_talk
    hide tana_talk
    show tana at tana_near
    with dissolve
    "[mcname!c]" "See Nay? Ga ada yang langsung bisa, santai aja. Kamu lakuin apa yang kamu bisa, aku dan kita semua pasti dukung, oke? Semangat yuk."
    hide kana_shy
    show kana_shy_talk at kana_near_left_2
    show kana_side_cry at left
    with dissolve
    kana "O-okeee aku coba ya."
    hide kana_side_cry
    hide kana_shy_talk
    hide tana
    hide pia
    with dissolve
    "Kana akhirnya mau mencoba latihan bersama Tana dan Pia."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Sore.ogg" loop fadein 1.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Tak terasa langit telah menjadi sore..."
    $ quick_menu = False
    scene ruang ukm sore with Dissolve(2.0)
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    $ quick_menu = True
    tana "Gileeeee, lu keren banget Nayyy bisa ikutin tempo kita."
    tana "Sumpah stamina lu kuat banget, emang ga sia-sia ya kamu sering ke event."
    hide tana_side_talk
    hide tana_talk
    show tana at tana_near
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Iya loh, aku kagum. Kerja bagus Nay!"
    hide pia_side_talk
    hide pia_talk
    show pia at pia_near_right
    show kana at kana_near_left_2
    with dissolve
    "[mcname!c]" "Nay, kamu gapapa? Nih minyum dulu yaa, jangan lupa. You did great, kamu bagus bangett!"
    hide kana
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "M-makasih yaa…"
    kana "Hehee seru juga ya ternyata, tapi cape bangeeet."
    hide kana_side_talk
    hide kana_talk
    hide tana
    show kana at kana_near_left_2
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Hahaha iya lah bro. Gue juga awal-awal serasa mau pingsan, tapi ya sekarang terbiasa."
    tana "Oke deh, buat hari ini segini aja dulu yaaa. Nanti kita lanjut lagi lah ya, buat selanjutnya kita latihan nyanyi."
    hide tana_side_talk
    hide tana_talk
    hide pia
    show tana at tana_near
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Iya cape bangettt. Ya udah deh, nanti bahas di grup aja yaaa."
    hide pia_side_talk
    hide pia_talk
    hide kana
    show pia at pia_near_right
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Iya nih capee banget, tapi makasih yaa buat hari ini."
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near_left_2
    with dissolve
    "[mcname!c]" "Makasih juga yaa."
    hide kana
    hide tana
    hide pia
    with dissolve
    "Mereka pun pulang ke rumah masing-masing."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" loop fadein 1.0
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Di kost..."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(2.0)
    $ quick_menu = True
    "[mcname!c] mengingat kembali perjuangan Kana saat latihan."
    "[mcname!c]" "{i}Nay… Kamu berjuang banget yaa, mulai terbuka sama orang lain lalu sekarang kamu mau ngedance dan nyanyi… Aku bangga banget sama kamu...{/i}"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_UKM.ogg" loop fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya..."
    $ quick_menu = False
    scene ruang ukm with Dissolve(2.0)
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    $ quick_menu = True
    tana "Okeee buat hari ini, kita coba latihan vocal yaa. Piii kasih paham."
    hide tana_side_talk
    hide tana_talk
    show tana at tana_near
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Ah elah, gue kira elu yang bakalan mulai."
    hide pia_side_talk
    hide pia_talk
    hide tana
    show pia at pia_near_right
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Hehe, kan lu lebih jago brokk."
    hide tana_side_talk
    hide tana_talk
    hide pia
    show tana at tana_near
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Ya udah kita coba dulu ya."
    show kana at kana_near_left_2 with dissolve
    pia "Kana, Coba deh kamu nyanyi lagu yang paling kamu sukai dulu. Nanti aku coba kasih masukan, boleh kan?"
    hide pia_side_talk
    hide pia_talk
    hide kana
    show pia at pia_near_right
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Boleh aku siap kalau sekarang, tapi jangan terlalu kasar ya ngasih masukannya, hehe. "
    hide kana_side_talk
    hide kana_talk
    hide pia
    show kana at kana_near_left_2
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Aman aja."
    stop music fadeout 1.0
    hide pia_side_talk
    hide pia_talk
    show pia at pia_near_right
    show kana_shy_closeeye_talk at kana_near_left_2
    with dissolve
    "Kana pun menyanyikan lagu yang ia sukai. Lagunya cukup lama sekitar 4 menit, tetapi bisa dilihat bahwa Kana bernyanyi dengan penuh penghayatan."
    hide kana_shy_closeeye_talk
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Huuuuu, gimana? Huuuuu… Bentar ya aku narik nafas dulu."
    play music "BGM_Bad End.ogg" fadein 1.0
    hide kana_talk
    hide kana_side_talk
    hide pia
    show tana
    show kana at kana_near_left_2
    show pia_silent at pia_near_right
    show pia_side_silent at left
    with dissolve
    pia "Hmmm… Kana, aku boleh blak-blakan ga?"
    hide kana
    hide pia_side_silent
    show kana_confused at kana_near_left_2
    show kana_side_confused at left
    with dissolve
    kana "Eh k-kenapa ini kok jadi kaya gini?"
    show kana_confused_blus_sideeye at kana_near_left_2
    hide kana_side_confused
    with dissolve
    "Kana pun kebingungan. Ia melihat ke arah Tana dan [mcname!c], akan tetapi Tana hanya bisa diam."
    "[mcname!c]" "Piia?"
    hide kana_confused_blus_sideeye
    hide pia
    show pia_side_silent at left
    with dissolve
    pia "Bentar ya [mcname!c], ini aku sama Kana dulu. Oke Kana, jadi…"
    hide pia_side_silent with dissolve
    "Pia pun mengomentari nyanyian dari Kana. Pia tidak mengatakan bahwa Kana tidak bisa bernyanyi ataupun suaranya jelek."
    "Akan tetapi, Pia mengomentari tentang teknik vokal yang digunakan Kana dan memberikan petunjuk mengenai teknik vokal yang lebih cocok untuk suara Kana."
    hide pia_talk
    hide kana_confused
    show pia at pia_near_right
    show kana at kana_near_left_2
    show kana_side at left
    with dissolve
    kana "...."
    hide kana_side
    hide pia
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Okeee kita coba nyanyi lagu ini bareng ya, kamu tau kan Kana?"
    hide pia_side_talk
    hide pia_talk
    hide kana
    show pia at pia_near_right
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "I-iya aku tau kok, haha."
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near_left_2
    with dissolve
    "[mcname!c]" "Nay, you okay?"
    "[mcname!c] melihat ke arah Kana yang mukanya terlihat agak pucat, membuat [mcname!c] sedikit khawatir."
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Oke deh, ayoo!"
    hide kana
    hide pia
    hide tana
    hide pia_silent
    hide tana_side_talk
    hide tana_talk
    with dissolve
    "Saat bernyanyi bersama, sempat beberapa kali Kana terdiam sehingga mereka bertiga menyanyikan lagunya dari awal lagi…"
    show kana_confused_blush at kana_near_left_2
    show kana_side_cry at left
    with dissolve
    kana "E-eh maaf ya, aku salah terus."
    hide kana_side_cry
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Santai aja Kana, ga salah kok. Kamu udah bagus kok."
    hide tana_side_talk
    hide tana_talk
    show tana at tana_near
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Iya Kana, santai aja. Ini pertama juga, you did good."
    hide pia_side_talk
    hide pia_talk
    show pia at pia_near_right
    with dissolve
    "[mcname!c]" "Iya kok Nay. Meski aku ga terlalu tau soal vocal, tapi suara kamu enak didenger kok."
    hide kana_confused_blush
    show kana_shy_smile at kana_near_left_2
    show kana_side_shy_smile at left
    with dissolve
    kana "Makasih ya, haha."
    hide kana_side_shy_smile
    hide kana_shy_smile
    show kana_deadeye at kana_near_left_2
    with dissolve
    kana "...."
    hide kana_deadeye
    show kana_deadeye_smile at kana_near_left_2
    with dissolve
    kana "Eh maaf ini aku ditelpon sama orang rumah, aku izin angkat dulu ya."
    hide kana_side_talk
    hide kana_deadeye_smile
    hide pia
    hide tana
    with dissolve
    #*Black Screen
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Sore.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Tak terasa langit telah menjadi sore..."
    $ quick_menu = False
    scene ruang ukm sore with Dissolve(2.0)
    show pia at pia_near
    $ quick_menu = True
    "[mcname!c]" "Eh… Piii."
    hide pia
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Hmmm kenapa?"
    hide pia_side_talk
    hide pia_talk
    show pia at pia_near
    with dissolve
    "[mcname!c]" "Ummm… gapapa deh, lupakan aja. "
    hide pia
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Ya udah kalau gitu."
    hide pia_side_talk
    hide pia_talk
    with dissolve
    "Tiba-tiba Tana menarik lengan [mcname!c], seakan ingin berbicara dengannya secara personal."
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Eh [mcname!c], maaf ya kalau Si Pia agak gimana gitu komennya. Soalnya ke gue juga lebih parah, tapi habis itu vocal gue improve bangettt."
    hide tana_side_talk
    hide tana_talk
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Kok minta maafnya ke gue, kan Kana yang kena komen."
    hide tana
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Soalnya lu kan yang lebih deket, nanti sampaiin ya."
    hide tana_side_talk
    hide tana_talk
    show tana at tana_near
    show kana_smile at kana_near_left_2
    show kana_side_smile at left
    with dissolve
    kana "Eh temen-temen, maaf ya. Tadi ada telepon, kayaknya aku harus pulang duluan deh. Maaf banget yaa."
    hide kana_side_smile
    hide kana_smile
    show kana at kana_near_left_2
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Eeh gapapa kok Kana, ini juga kayaknya udahan aja dulu deh."
    hide pia_side_talk
    hide pia_talk
    hide tana
    show pia at pia_near_right
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Iya ini juga udah aja dulu."
    hide tana_side_talk
    hide tana_talk
    hide pia
    hide kana
    with dissolve
    "Di perjalanan pulang, [mcname!c] memikirkan Kana. Ia tampak agak berbeda dari biasanya, seakan ada yang membuat dia gelisah."
    "Tetapi yang ada di pikiran [mcname!c] hanya mimik muka Kana sesaat setelah diberi komentar oleh Pia…"
    "[mcname!c]" "Oke dehh, nanti aku tanya Si Kana aja."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" loop fadein 1.0
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Di kost..."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(2.0)
    $ quick_menu = True
    "[mcname!c]" "{i}Hmmm, enaknya gimana ya mulainya?{/i}"
    $ quick_menu = False
    #*INSERT HP*
    nvl clear
    mc_nvl "Malam Nayy.."
    scene kamar mc kota with Dissolve(0.3)
    $ quick_menu = True
    "Setelah kurang lebih 10 menit, akhirnya muncul notif pesan dari Kana."
    $ quick_menu = False
    kana_nvl "I-iya kenapa?"
    mc_nvl "Gimana kabarnya, hari ini ngapain aja haha."
    kana_nvl "Template amat pertanyaannya."
    mc_nvl "Hahaha"
    kana_nvl "Kenapa?"
    mc_nvl "Uummm sebenernya.. "
    mc_nvl "Tadi kok kamu agak gimana gitu pas latihan.."
    kana_nvl "Ga ada apa-apa kok…"
    mc_nvl "Nay meski kita baru deket, tapi aku tau kalau kamu bohong… Waktu bilang ada telepon juga kamu bohong kan? Kenapa Naya, ada apa?"
    kana_nvl "Uummmm nanti besok kita ketemuan aja, gimana"
    kana_nvl "Aku ga mau jelasin hal ini di chat."
    mc_nvl "Ookee, nanti kita besok ketemuan di..."
    scene kamar mc kota with Dissolve(0.2)
    $ quick_menu = True
    menu:
        "Ketemuan di..."
        "Cafe":
            #*IF CHOSE*
            #A
            mc_nvl "Gimana kalau di cafe Nay? Cafe yang sering kita kunjungi itu loh."
            kana_nvl "Uummm aku takut ada orang lain yang denger, aku malu..."
            $ quick_menu = False
            nvl clear
            stop music fadeout 1.0
            scene black with dissolve
            show text "{color=#FFF}“COBA LAGI YA BROK, KURANG BERUNTUNG LUH”{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3"
            jump credits
        "Warteg":
            #*IF CHOSE*
            #B
            mc_nvl "Warteg gimana Nay??? Sekalian makan siang gitu, hehe."
            kana_nvl "Yang bener aja…. Aku kan ngajaknya ngobrol, bukan makan. Bodo ah."
            $ quick_menu = False
            nvl clear
            stop music fadeout 1.0
            scene black with dissolve
            show text "{color=#FFF}“ADUHHH BROOOO BROOO, COBA LAGI DEH TINGGAL SATU PILIHAN TUH”{/color}" with Pause(3.0)
            scene black with dissolve
            show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3"
            jump credits
        "Rumah Kana":
            jump goodkanameetinhome

label goodkanameetinhome:
    #*IF CHOSE*
    #C
    mc_nvl "Kalo di rumah gimana Nay? Aku sebenernya bebas sih mau di mana aja, yang penting kamu nyaman."
    kana_nvl "Boleh deh, nanti di rumah aku aja ya. Jam 12 siang gimana?"
    mc_nvl "Okee Nay.."
    nvl clear
    scene kamar mc kota with Dissolve(0.3)
    $ quick_menu = True
    "Hmmm ini pasti ada hubungannya sama latihan tadi, fix siiih…"
    stop music fadeout 1.0
    $ quick_menu = False
    #*SKIP TO SCENE*
    #*BG RUMAH KANA*
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Ruang Tamu.ogg" loop fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya..."
    $ quick_menu = False
    scene ruang tamu with Dissolve(2.0)
    $ quick_menu = True
    "[mcname!c] pun mendatangi rumah Kana tepat jam 12. Merasa hal ini adalah sesuatu yang penting, [mcname!c] tidak ingin membuat Kana kecewa karena telat."
    show kana_home_talk at kana_near
    show kana_home_side_talk at left
    with dissolve
    kana "Eh, masuk aja."
    hide kana_home_side_talk
    hide kana_home_talk
    show kana_home at kana_near
    with dissolve
    "[mcname!c]" "Ohh iya…"
    hide kana_home with dissolve
    "Terdapat ketenangan sejenak di antara Kana dan [mcname!c]. Kana yang merasa takut untuk bercerita dan [mcname!c] yang ingin bertanya tapi merasa tidak enak, membuat keduanya tidak dapat memulai pembicaraan. Sampai pada akhirnya…"
    show kana_home at kana_near with dissolve
    "[mcname!c]" "Nay… Jadi sebenernya ada apa."
    hide kana_home
    show kana_home_confused at kana_near
    show kana_home_side_confused at left
    with dissolve
    kana "Sebenernya…."
    kana "Kamu inget ga, pas kita latihan kemarin itu?"
    hide kana_home_side_confused
    hide kana_home_confused
    show kana_home_sad at kana_near
    with dissolve
    "[mcname!c]" "Inget, latihan vokal kan?"
    hide kana_home_sad
    show kana_home_confused at kana_near
    show kana_home_side_confused at left
    with dissolve
    kana "Iya latihan vokal itu. Setelah denger masukan dari Pia dan latihan bareng, aku ngerasa ketinggalan banget masalah tekniknya."
    kana "Bahkan Pia aja sampe ngajarin aku teknik-teknik vokal gitu, aku malu-maluin ya…"
    hide kana_home_side_confused
    hide kana_home_confused
    with dissolve
    "Kana mengatakan hal tersebut dengan wajahnya yang sedih, melihat ke arah [mcname!c] seakan ada air mata yang akan keluar dari matanya Kana."
    show kana_home_confused at kana_near
    show kana_home_side_confused at left
    with dissolve
    kana "Pas liat rekaman dance juga aku merasa masih banyak ketinggalan temponya."
    kana "Emang sih kalo stamina aku bisa imbangin yang lain, tapi tempo, ketukan, dan lainnya, aku telat semua haha."
    kana "Apa Tono sama Pia muji aku cuma supaya aku tetep mau sama mereka ya, padahal aslinya aku tuh kaya beban..."
    hide kana_home_side_confused
    hide kana_home_confused
    show kana_home_normal at kana_near
    with dissolve
    "[mcname!c] hanya diam saja, ia tidak ingin menyela cerita dari Kana."
    show kana_home_confused at kana_near
    show kana_home_side_confused at left
    hide kana_home_normal at kana_near
    with dissolve
    kana "Kayaknya aku mending udahan aja deh, lagian aku kan ga berbakat nyanyi atau dance gitu. Tana punya dance, Pia punya vokal, kalau aku ga punya apa-apa."
    hide kana_home_side_confused
    hide kana_home_confused
    show kana_home_sad at kana_near
    with dissolve
    "[mcname!c]" "Udah Nay?"
    hide kana_home_sad
    show kana_home_confused at kana_near
    show kana_home_side_confused at left
    with dissolve
    kana "Maksudnya udah?"
    hide kana_home_side_confused
    hide kana_home_confused
    show kana_home_normal at kana_near
    with dissolve
    "[mcname!c]" "Udah ngerendahin diri kamu sendiri? Okee ini sekarang pandanganku ya, ga boleh nyela."
    "[mcname!c]" "INGET, GA BOLEH NYELA."
    "[mcname!c]" "Ok?"
    hide kana_home_normal
    show kana_home_confused at kana_near
    show kana_home_side_confused at left
    with dissolve
    kana "O-oke."
    hide kana_home_side_confused
    hide kana_home_confused
    show kana_home_normal at kana_near
    with dissolve
    "[mcname!c]" "Dancemu off tempo… off ketukan… emang kenapa Nay? Emang mereka komen soal itu? Enggak, kan?"
    "[mcname!c]" "Ini pertama kalinya dance buat kamu kan? Dan mereka aja muji kamu, Naya, ga usah berkecil hati."
    "[mcname!c]" "Soal vokal, kalo kamu mau tau, Si Tana sampe minta tolong buat sampein permintaan maaf ke kamu."
    "[mcname!c]" "Dia bilang kalo Si Pia emang ngajarinnya kaya gitu, tapi niat dia kan baik. Buktinya kamu sekarang tau teknik vokal lainnya."
    "Kana yang hanya bisa terdiam sambil menatap [mcname!c]."
    "[mcname!c]" "Yang lebih penting dari semua itu ada kamu, Kanaia Asa. Apa kamu seneng belajar bareng dan temenan sama mereka?"
    "Kana tetap terdiam beberapa menit."
    "[mcname!c]" "Sekali lagi Kanaia asa, kamu seneng ga sama mereka?"
    show kana_home_side_normal at left with dissolve
    kana "....."
    hide kana_home_side_normal
    hide kana_home_normal
    show kana_home_confused at kana_near
    show kana_home_side_confused at left
    with dissolve
    kana "A-a-aku seneng…. Aku seneng bisa ketemu sama mereka, latihan sama mereka, dan pengen terus sama mereka."
    kana "Tapi… aku takut jadi beban.."
    hide kana_home_side_confused
    hide kana_home_confused
    show kana_home_normal at kana_near
    with dissolve
    "[mcname!c]" "Yang bilang kamu beban siapa? Kan ga ada, apa mau aku tanya langsung ke mereka?"
    hide kana_home_normal
    show kana_home_confused at kana_near
    show kana_home_side_confused at left
    with dissolve
    kana "J-jangan! Jangan tanya ke mereka, nanti aku makin maluuu."
    hide kana_home_side_confused
    hide kana_home_confused
    show kana_home_normal at kana_near
    with dissolve
    "[mcname!c]" "Ya udah, ga usah mikir kaya gitu lagi ya. Kamu udah berjuang kok, jadi kamu harus bangga. Oke?"
    hide kana_home_normal
    show kana_home_confused at kana_near
    show kana_home_side_confused at left
    with dissolve
    kana "I-i’ll try… "
    hide kana_home_side_confused
    hide kana_home_confused
    show kana_home at kana_near
    with dissolve
    "[mcname!c]" "Good, jadi sekarang mau ngapain lagi?"
    hide kana_home
    show kana_home_talk at kana_near
    show kana_home_side_talk at left
    with dissolve
    kana "Hahaha. Iya juga ya, ngapain lagi ya?"
    hide kana_home_side_talk
    hide kana_home_talk
    show kana_home at kana_near
    with dissolve
    "[mcname!c]" "Gimana kalo kamu coba teknik vokal yang diajarin Pia waktu itu, sama dance dikit-dikit. Gimana?"
    hide kana_home
    show kana_home_talk at kana_near
    show kana_home_side_talk at left
    with dissolve
    kana "Umm boleh sih… tapi jangan ketawain aku kalo salah langkah atau bahkan sampe jatoh, ya."
    hide kana_home_side_talk
    hide kana_home_talk
    show kana_home at kana_near
    with dissolve
    "[mcname!c]" "Engga kok, aku janji. "
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Setelah itu Kana pun melatih dirinya untuk bisa lebih baik lagi sambil ditemani [mcname!c] yang selalu ada untuk mendukungnya."
    "Kana cukup semangat untuk latihan pribadi kali ini."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Kosan 1.ogg" fadein 1.0
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    " Tak terasa langit sudah menjadi gelap."
    $ quick_menu = False
    scene ruang tamu malam with Dissolve(2.0)
    $ quick_menu = True
    "[mcname!c]" "Nay, kayaknya aku pulang dulu ya. Udah malem ini, ga kerasa emang kalau lagi asik-asik tuh."
    hide kana_home
    show kana_home_talk at kana_near
    show kana_home_side_talk at left
    with dissolve
    kana "Eeh iya astaga, udah jam segini. Makasih ya, udah mau dengerin dan temenin aku."
    hide kana_home_side_talk
    hide kana_home_talk
    show kana_home at kana_near
    with dissolve
    "[mcname!c]" "Iya sama-sama, see you Nay."
    hide kana_home
    show kana_home_talk at kana_near
    show kana_home_side_talk at left
    with dissolve
    kana "See youu~"
    hide kana_home_side_talk
    hide kana_home_talk
    with dissolve
    "[mcname!c] pun pergi dari rumah Kana."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Di perjalanan ia memikirkan Kana yang terkadang masih memiliki negatif thinking, dan saat itu juga ia berjanji."
    "[mcname!c]" "{i}Okeee, pokoknya aku harus bisa dukung Kana sampe perlombaan! Jangan sampe kana punya pikiran negatif lagi!{/i}"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_UKM.ogg" loop fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya..."
    $ quick_menu = False
    scene ruang ukm with Dissolve(2.0)
    $ quick_menu = True
    "Hari baru dimulai, para anggota dan panitia pun cukup sibuk dengan persiapan yang dibutuhkan."
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Kana… maaf ya kemaren kalo masukan atau komen aku ada yang bikin kamu sakit hati."
    pia "Kemaren aku juga udah dimarahin sama Tono, maaf ya."
    hide pia_side_talk
    hide pia_talk
    show pia at pia_near_right
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Iya Kana, maafin Pia yaa. Dia ga ada maksud jelek-jelekin kamu, sumpah dah. Maafin ya…"
    hide tana_side_talk
    hide tana_talk
    show tana at tana_near
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Gapapa kok, aku tau kalo itu masukan yang bikin aku improve."
    kana "Makasih ya masukannya, aku ga marah kok aman aja."
    kana "Next time kalau emang ada masukan bilang aja langsung ya, ga usah ragu-ragu lagi. Btw panggil aku Nay aja."
    hide kana_side_talk
    hide kana_talk
    hide pia
    show kana at kana_near_left_2
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Yeeeeeee, ku kira kamu marah. Makasih ya Naaayyyy."
    hide pia_side_talk
    hide pia_talk
    hide tana
    show pia at pia_near_right
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Oke deh Nay. Btw kita latihan di mana ya? Di ruangan klub kayaknya ga bisa deh, soalnya pada penuh gitu."
    hide tana_side_talk
    hide tana_talk
    hide kana
    hide pia
    with dissolve
    "Padangan dari ketiganya mengarah ke [mcname!c], seakan meminta [mcname!c] untuk memberikan tempat yang cocok untuk latihan."
    "[mcname!c]" "Ummm gimana kalau di… "
    #*CHOOSE*
    menu:
        "Mana yang akan kamu pilih?"
        "ROOFTOP":
            jump goodkanadancepractice
        "TANAH KOSONG DI UJUNG KAMPUS":
            stop music fadeout 1.0
            $ quick_menu = False
            scene black with Dissolve(1.0)
            play music "BGM_Bad End.ogg" fadein 1.0
            scene black with Dissolve(1.0)
            $ quick_menu = True        
            show tana_angry_2 at tana_near
            show tana_side_angry_2 at left
            with dissolve
            tana "Lu serius brok, di sini?"
            hide tana_angry_2
            hide tana_side_angry_2
            show tana_angry at tana_near
            with dissolve
            "[mcname!c]" "Emang kenapa, Ton?"
            show pia_silent at pia_near_right
            show pia_side_silent at left
            with dissolve
            pia "Eh kok aku ngerasa gimana ya sama hawanya."
            hide pia_side_silent
            hide pia_silent
            show pia_silent at pia_near_right
            show kana_confused_blush at kana_near_left_2
            show kana_side_cry at left
            with dissolve
            kana "[mcname!c], serius kan di sini?"
            hide kana_side_cry
            with dissolve
            "[mcname!c]" "Iya soalnya kan Kana masih belum terbiasa tampil gitu, terus kalian pengen di tempat kosong kan? Aku denger tempat ini dari temen-temen gitu sih, gimana?"
            hide tana
            show tana_shock at tana_near
            show tana_side_shock at left
            with dissolve
            tana "Broo sebenarnya ini tempat apaan dah, jujur hawanya ga enak. Kita pindah aja yuk, sumpah dah mending ga latihan sekalian gw mah daripada di sini."
            hide tana_side_shock
            hide tana_shock
            hide pia
            show tana_sad at tana_near
            show pia_silent at pia_near_right
            show pia_side_silent at left
            with dissolve
            pia "Gue setuju sama Tono sih buat kali ini."
            hide pia_side_silent
            hide kana
            show kana_deadeye at kana_near_left_2
            with dissolve
            kana "!!!!!!!!!"
            "[mcname!c]" "Nay? Kamu kenapa Nay?"
            kana "!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            show kana_deadeye_smile at kana_near_left_2 with dissolve
            kana "AHAHAHAHAHAHAHAH!!!!!!!!!!!!!!!!!!!!!!!!"
            show tana_shock at tana_near
            show tana_side_shock at left
            with dissolve
            tana "TUH KAN! GW BILANG APA!"
            hide pia_silent 
            hide tana_sad
            hide kana_confused_blush 
            hide tana_angry
            hide kana_deadeye_smile
            hide tana_side_shock
            hide tana_shock
            hide kana_deadeye
            hide pia
            with dissolve
            $ quick_menu = False
            scene black with dissolve
            show text "{color=#FFF}“TERNYATA TEMPAT ITU SALAH SATU TEMPAT YANG KATANYA ANGKER DI KAMPUS LU, KANA MALAH KESURUPAN TUH BROK.”{/color}" with Pause(5.0)
            scene black with dissolve
            show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3"
            jump credits
        "DI BAWAH POHON":
            stop music fadeout 1.0
            $ quick_menu = False
            scene black with Dissolve(1.0)
            play music "BGM_Sawah Siang.ogg" fadein 1.0
            scene sawah with Dissolve(1.0)
            $ quick_menu = True
            "[mcname!c]" "Nahhh ini luas nih, adem juga kan?"
            show tana_talk at tana_near
            show tana_side_talk at left
            with dissolve
            tana "Wiiihh iya nih adem, bisa juga lu nyari tempat."
            hide tana_side_talk
            hide tana_talk
            show tana at tana_near
            show kana_talk at kana_near_left_2
            show kana_side_talk at left
            with dissolve
            kana "Oke juga pilihanmu, [mcname!c]."
            hide kana_side_talk
            hide kana_talk
            show kana at kana_near_left_2
            show pia_talk at pia_near_right
            show pia_side_talk at left
            with dissolve
            pia "Ya udah, yuk latihan."
            stop music fadeout 1.0
            hide pia_side_talk
            hide pia_talk
            hide tana
            hide kana
            with dissolve
            play music "BGM_Bad End.ogg" fadein 1.0
            "Tak lama saat latihan tiba-tiba terdengar suara yang keras, membuat mereka panik."
            "Ternyata salah satu dahan pohon di tempat itu patah dan jatuh menimpa Kana."
            "Kana pun terluka dan akhirnya harus dilarikan ke rumah sakit."
            $ quick_menu = False
            scene black with dissolve
            show text "{color=#FFF}“ADUH BROOOO ATI-ATI DAH! JANGAN SERING SERING DI BAWAH POHON TUA YANG GEDE!! TAKUT JATOH DAHANNYA TERUS MALAH LUKA!”{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3"
            jump credits

label goodkanadancepractice:
    #*IF CHOOSE A*
    "[mcname!c]" "Eh aku tau tempat yang bagus… Ikut yuk."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Rooftop Siang.ogg" loop fadein 1.0
    scene rooftop with Dissolve(1.0)
    $ quick_menu = True
    "[mcname!c]" "Gimana, bagus kan?"
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Wahhhh gokil juga pilihan lu, tapi ini ga ada orang yang ke sini kah?"
    hide tana_side_talk
    hide tana_talk
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Ada tapi jarang sih, paling 1 atau 2 orang doang. Aman aja lah harusnya."
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Ya udah deh, ayooo latihannn. Pokoknya hari ini target yaaa, inget target kita."
    hide pia_side_talk
    hide pia_talk
    show pia at pia_near_right
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Siap Bu Guru Piaaa."
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near_left_2
    with dissolve
    "[mcname!c]" "Semangat yaaa, aku mau beli minum dulu buat kalian semua."
    hide tana 
    hide pia 
    hide kana 
    with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    $ quick_menu = True
    "Kana, Tana, dan Pia pun melakukan latihannya di rooftop."
    "Entah mengapa mereka merasa lebih leluasa, mungkin karena tempatnya yang cukup luas dan udaranya yang sejuk membuat mereka cukup nyaman."
    "Akan tetapi saat [mcname!c] kembali ke rooftop dan membuka pintu, dia melihat sesuatu yang sedang terjadi."
    $ quick_menu = False
    play music "BGM_Bad End.ogg" fadein 1.0
    scene rooftop with Dissolve(1.0)
    $ quick_menu = True
    hide pia
    show pia_silent at pia_near_right
    show pia_side_silent at left
    with dissolve
    pia "Eh Nay ayoo dongg, jangan off tempoo. Udah berapa kali ini?"
    hide pia_side_silent
    hide kana
    show kana_confused at kana_near_left_2
    show kana_side_confused at left
    with dissolve
    kana "Maaf maaf..."
    hide kana_side_confused
    show pia_side_silent at left
    with dissolve
    pia "Lu juga Ton, bukannya lu yang harusnya guide kita ya? Kok malah ga tau kalo kita off tempo atau salah sih…"
    hide pia_side_silent
    hide tana
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Eh gue juga udah nyoba ya, dikira gampang apa liatin 3 orang langsung?"
    tana "Lu mah kan giliran di vokal, tunggu aja dulu napa? Tunggu giliran."
    hide tana_side_angry_2
    hide tana_angry_2
    show tana_angry at tana_near
    show pia_side_silent at left
    with dissolve
    pia "Maksud lu apaan Ton? Gue kan pengen kita semua bisa, biar semuanya bisa, biar nanti pas tampil setidaknya ga salah dan ga malu-maluin diliatin orang."
    hide pia_side_silent
    hide tana_angry
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Eh biasa aja dong, dikira gue ga mau bisa apa ya? Gue juga pengen bisa dong san-"
    stop music fadeout 1.0
    hide tana_side_angry_2
    show tana_silent at tana_near
    with dissolve
    play sound "audio/SFX - Door Slam.WAV" volume (5.0)
    "Saat keadaan memuncak, [mcname!c] datang dan menjatuhkan kantong kresek yang penuh dengan minuman dan cemilan."
    "[mcname!c]" "UDAH NAPA?! "
    "Mereka semua terdiam, melihat [mcname!c] yang telah datang."
    play music "BGM_Sawah Sore.ogg" fadein 1.0
    "[mcname!c]" "Bentar-bentar, coba pelan-pelan deh ini masalahnya apa dah."
    show pia_silent at pia_near_right
    show pia_side_silent at left
    with dissolve
    pia "Ini loh Tono. Dia kan harusnya yang guide dance kita, tapi Kana off tempo, gue off tempo, atau dia yang off tempo, dia ga ngeh."
    hide pia_side_silent
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Ya sabar, gue juga harus ngecek rekaman dulu. Di sini ga ada kaca gede kaya di studio."
    hide tana_side_angry_2
    hide tana_angry_2
    show tana_angry at tana_near
    show kana_confused at kana_near_left_2
    show kana_side_confused at left
    with dissolve
    kana "Eh… Maaf ya kayaknya aku kebayakan salahnya deh, jadi berantem gini…"
    hide kana_side_confused
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Enggak Nay, ini bukan salah mu kok."
    hide pia_side_talk
    hide pia_talk
    show pia_silent at pia_near_right
    with dissolve
    "[mcname!c]" "Udah udah..."
    "[mcname!c]" "Mending kalian semua minum sama nyemil dulu dah, ini lagi panas-panasnya emang. Meskipun ada angin sepoi-sepoi, tapi cahayanya tetap panas. Minum dulu sana."
    "Mereka pun mengambil beberapa minuman dan makanan dari kantong kresek yang telah dibawa [mcname!c] sebelumnya."
    "Setelah menenangkan diri masing-masing, [mcname!c] pun berbicara."
    "[mcname!c]" "Okeee, ini pandangan gue ya. Jadi kalo kata Pia, Si Tono harusnya bisa nge-guide kan? Tapi Tono ga bisa nge-guide terus-terusan karena harus lihat rekaman, ya? Dan Kana, kamu jangan mulai salahin diri sendiri lagi oke?"
    show kana_side_confused at left
    with dissolve
    kana "Ehh… Uummm...."
    hide kana_side_confused
    hide tana_angry
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Nahhh iya gituuu. Kalo di studio besar atau di ruang klub setidaknya ada kaca cermin, jadi gue bisa liat kalian semua."
    tana "Tapi kalo di sini ga ada, jadi gue harus liat bolak-balik rekaman gitu."
    hide tana_side_talk
    hide tana_talk
    hide pia_silent
    hide kana_confused
    show kana at kana_near_left_2
    show tana at tana_near
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "I-iya juga sih..."
    hide pia_side_talk
    hide pia_talk
    show pia at pia_near_right
    with dissolve
    "[mcname!c]" "Oke kalo gitu gue yang liat dan bantu rekam aja deh, nanti gue kasih rekamannya."
    "[mcname!c]" "Buat Pia, tetep kasih tau aja kalo ada yang off tempo."
    hide kana
    show kana_confused at kana_near_left_2
    show kana_side_confused at left
    with dissolve
    kana "Maaf ya, aku sadar kok kalo tadi aku banyak off tempo dan diingetin bahkan dibackup sama Pia dan kamu Ton, supaya gerakanku ga terlalu keliatan aneh... "
    hide kana_side_confused
    hide kana_confused
    hide tana
    show kana at kana_near_left_2
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Ah elah aman aja brookk, kamu juga baru belajar. Kamu udah bagus kok, tinggal sering sering latihan aja sih menurutku."
    hide tana_side_talk
    hide tana_talk
    hide pia
    show tana at tana_near
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Iya kamu udah bagus kok, Nay. Nanti aku kasih tau deh triknya biar dapet tempo/ketukan yang pas gitu."
    hide pia_side_talk
    hide pia_talk
    show pia at pia_near_right
    with dissolve
    "[mcname!c]" "Nah kan kalo gini enak akur semua."
    hide tana
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Iya Pii. Tadi sorry ya, gue kebawa emosi. Keknya karena emang panas sih, hehehe."
    hide tana_side_talk
    hide tana_talk
    hide pia
    show tana at tana_near
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Gue juga minta maaf ya Ton. Padahal lu kan dah bantu guide kita dance gini, eh gue malah marah-marah ga jelas."
    hide pia_side_talk
    hide pia_talk
    hide kana
    show pia at pia_near_right
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Aku juga minta maaf ya kalau banyak salah dan malah ngerepotin kalian."
    hide kana_side_talk
    hide kana_talk
    hide tana
    show kana at kana_near_left_2
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Ah elah napa malah jadi maaf-maafan gini dah, perasaan lebaran masih lama."
    hide tana_side_talk
    hide tana_talk
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Nahhh kan mantepppp."
    hide tana_silent
    hide pia
    hide tana
    hide kana
    with dissolve
    "Kana, Tana, dan Pia pun melanjutkan latihannya kembali."
    $ quick_menu = False
    scene awan berkabut with Dissolve(2.0)
    $ quick_menu = True
    "Meski beberapa kali Kana terjatuh dan tertinggal, tapi ia tidak pernah dimarahi oleh Tono ataupun Pia."
    "Malah Kana ditunjukan cara yang tepat dan dibimbing agar gerakannya menjadi lebih bagus lagi.."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Sore.ogg" loop fadein 1.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Beberapa jam kemudian..."
    $ quick_menu = False
    scene rooftop sore with Dissolve(2.0)
    hide kana
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    $ quick_menu = True
    kana "Aaaaa, capeeek banget~"
    hide kana_side_talk
    hide kana_talk
    hide pia
    show kana at kana_near_left_2
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Iya nih, panas gerah banget yaaa capeeek. Tapi apalagi kamu Nay, kita istirahat kamu malah terus nyoba benerin gerakan kamu."
    hide pia_side_talk
    hide pia_talk
    hide kana
    show pia at pia_near_right
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Iya dong, biar ga ketinggalan sama kalian."
    hide kana_side_talk
    hide kana_talk
    hide tana
    show kana at kana_near_left_2
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Lu keren banget Nay."
    hide tana_side_talk
    hide tana_talk
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Eeh udah kali ya buat hari ini, rooftop udah mau ditutup."
    "[mcname!c]" "Tadi ada satpam yang ngasih tau aku gitu, terus aku bilang 5 menit lagi. Yuk beres-beres, jangan nyampah ya."
    hide tana
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Oke deh, ga kerasa ya udah sore gini."
    hide tana_side_talk
    hide tana_talk
    hide kana
    show tana at tana_near
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Iya ya ga kerasa. Makasih ya dah mau bantuin aku. Maaf kalau aku agak nyebelin, hahah."
    hide kana_side_talk
    hide kana_talk
    hide pia
    show kana at kana_near_left_2
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Ga usah kebanyakan minta maaf Nay, geli tau."
    hide pia_side_talk
    hide pia_talk
    hide tana
    show pia at pia_near_right
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Bener. Ga usah minta maaf terus, santai aja."
    hide tana_side_talk
    hide tana_talk
    hide pia
    hide kana
    with dissolve
    "Setelah pulang dari rooftop, mereka pun pulang ke rumah masing-masing."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    $ quick_menu = True
    "Hari demi hari berlalu diiringi latihan"
    "Hingga tak terasa waktu event dan perlombaan tinggal 1 minggu lagi."
    "Latihan yang dilakukan menjadi semakin rumit dan semakin lama, ada kalanya mereka saling bertengkar satu sama lain akan tetapi langsung reda dan mencoba saling memahami."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Sore.ogg" loop fadein 1.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Suatu hari..."
    $ quick_menu = False
    scene lorong sore with Dissolve(2.0)
    $ quick_menu = True
    "[mcname!c] melihat Kana pergi ke arah rooftop sendirian. Awalnya [mcname!c] mengira akan ada latihan tambahan, akan tetapi di group chat tidak ada obrolan mengenai hal tersebut."
    "[mcname!c]" "{i}Hmmm itu kan Kana, kenapa dia sendirian ya ke rooftop? Perasaan hari ini ga ada latihan deh… Aku nyusul dah.{/i}"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Rooftop Sore.ogg" loop fadein 1.0
    scene rooftop sore with Dissolve(2.0)
    $ quick_menu = True
    "Saat membuka pintu, terlihat Kana yang sedang melihat ke arah langit dengan pandangan kosong, bahkan sampai tidak menyadari kehadiran [mcname!c] di situ."
    "[mcname!c]" "NAY!"
    show kana_confused at kana_near
    show kana_side_confused at left
    with dissolve
    kana "HAAAAA!!!"
    hide kana_side_confused
    hide kana_confused
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Eh [mcname!c]? Ku kira siapa, kaget tau."
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near
    with dissolve
    "[mcname!c]" "Hahaha dari tadi aku panggil loh, kamu ga sadar kah? Ada apa Nay?"
    hide kana
    show kana_confused at kana_near
    show kana_side_confused at left
    with dissolve
    kana "Engg-"
    hide kana_side_confused
    hide kana_confused
    show kana at kana_near
    with dissolve
    "[mcname!c]" "Sebelum itu, nih minum dulu. "
    "Kana melihat ke arah [mcname!c]. Pandangan Kana terlihat sedih, senang, dan cemas di saat yang bersamaan."
    "Mungkin Kana memiliki banyak pikiran atau mungkin hanya ingin sendirian, tetapi Kana saat itu tahu kalau dia hanya bisa bercerita tentang hal ini kepada [mcname!c]."
    hide kana
    show kana_drylaugh at kana_near
    show kana_side_drylaugh at left
    with dissolve
    kana "Hahaha, ketahuan ya kalo aku lagi ada pikiran."
    hide kana_side_drylaugh
    hide kana_drylaugh
    show kana at kana_near
    with dissolve
    "[mcname!c]" "...."
    hide kana
    show kana_confused at kana_near
    show kana_side_confused at left
    with dissolve
    kana "Entah kenapa selama latihan aku liat rekaman kita, aku ngerasa kalau aku paling telat dan paling ga menonjol gitu."
    kana "Meski udah coba berusaha buat positif, pikiran negatif ini terus-terusan muncul dan buat aku kadang ga bisa tidur."
    kana "Aku takut malah menghambat mereka pas perform nanti, haha."
    hide kana_side_confused
    with dissolve
    "[mcname!c]" "..."
    show kana_side_confused at left
    with dissolve
    kana "Maaf ya. Padahal aku udah janji ke kamu bakal berusaha ga berpikiran negatif lagi, eh tapi sekarang malah gini lagi."
    hide kana_side_confused
    with dissolve
    "[mcname!c]" "Ga usah minta maaf Nay, harusnya aku yang bisa dukung kamu lebih baik lagi."
    "[mcname!c]" "Aku ga bisa bilang apa-apa lagi, semua yang aku katakan waktu itu bener-bener apa yang ada di pikiranku."
    "[mcname!c]" "Kalau kamu mau tau seberapa berkembangnya kamu, nih kamu bisa lihat rekaman ini."
    "[mcname!c] memberikan HPnya kepada Kana. Di dalam HP tersebut ada sebuah video yang menunjukan Kana pada saat latihan pertama kali dan latihannya yang terakhir kali."
    "Kana dan [mcname!c] hanya terdiam melihat rekamanan tersebut. Setelah selesai, [mcname!c] pun mulai memberikan pendapatnya."
    "[mcname!c]" "Kamu udah improve banyak banget, Nay. Kamu liat deh gerakan kamu, nyanyian kamu, teknik kamu, kamu udah berkembang sejauh ini."
    show kana_side_confused at left
    with dissolve
    kana "T-tapi kan.."
    hide kana_side_confused
    hide kana_confused
    show kana at kana_near
    with dissolve
    "[mcname!c]" "Nay, even if u fall on stage, kamu pikir Tono sama Pia bakalan marahin kamu? Atau kamu pikir aku bakalan malu sama kamu?"
    "[mcname!c]" "Tono, Pia, dan aku tau perjuangan kamu. Jadi aku yakin mereka ga bakalan marah, malahan bangga sama usaha dan kerja kerasmu."
    hide kana
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Kalau dipikir-pikir Tono sama Pia meski aku udah sering jatoh dan salah, mereka ga pernah marahin aku."
    kana "Malah bantuin aku gitu, ya meski diketawain sama Si Tono dulu sih."
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near
    with dissolve
    "[mcname!c]" "Itu dia, mereka ga pernah marah ke kamu karena mereka udah liat seberapa besar perkembangan kamu."
    "[mcname!c]" "Jadi, tetep semangat oke? Besok kita latihan lagi loh."
    hide kana
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Makasih yaaa [mcname!c], udah mau dengerin cerita aku yang gini lagi. "
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near
    with dissolve
    "[mcname!c]" "Aku ga bakalan pernah bosen dengerin kamu cerita kok Nay."
    hide kana with dissolve
    "Sambil ditemani oleh [mcname!c] di rooftop, Kana mulai latihan lagi karena tidak ingin menjadi beban dan tidak ingin berbuat kesalahan pada saat perform nanti."
    stop music fadeout 1.0
    $ quick_menu = False
    #*SKIP TO SCENE*
    #*BG ROOFTOP*
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_UKM.ogg" loop fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Beberapa hari kemudian..."
    "Tak terasa, waktu telah sampai ke H-1 acara."
    $ quick_menu = False
    scene rooftop with Dissolve(2.0)
    $ quick_menu = True
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Okeee! Waktu kita sudah semakin dekat, jadi kita ga terlalu banyak latihannya. Takut nanti malah ada yang cedera atau gimana, jadi kita latihan ringan aja."
    hide tana_side_talk
    hide tana_talk
    show tana at tana_near
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Siappp."
    hide pia_side_talk
    hide pia_talk
    show pia at pia_near_right
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Oke Ton. "
    hide kana_side_talk
    hide kana_talk
    hide pia
    hide tana
    with dissolve
    $ quick_menu = False
    scene awan with Dissolve(2.0)
    $ quick_menu = True
    "Mereka bertiga pun memulai latihannya kembali."
    "Di saat latihan, ada beberapa momen Kana yang membuat dia putus asa karena tidak dapat mengikuti beberapa gerakan yang menjadi titik lemahnya saat latihan selama ini."
    "Tono dan Pia memberikan beberapa saran untuk membantu Kana melakukan gerakan tersebut. Saat mencoba, Kana tiba-tiba melihat ke arah [mcname!c]."
    "[mcname!c]" "SEMANGAT NAYYYY!!!!"
    "Saat mendengar suara tersebut, Kana menjadi bersemangat dan akhirnya setelah beberapa kali mencoba, dia dapat melakukan gerakan tersebut."
    "Terkejut senang, Tono dan Pia pun memeluk Kana karena bangga dengan apa yang Kana berhasil lakukan."
    $ quick_menu = False
    scene rooftop with Dissolve(2.0)
    $ quick_menu = True
    show tana_laugh at tana_near
    show tana_side_laugh at left
    with dissolve
    tana "Akhirnya lu bisa juga Nayyyy!!"
    hide tana_side_laugh
    hide tana_laugh
    show tana at tana_near
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Iyaaa Nayyyy, setelah sekian purnama akhirnya kamu bisa!!"
    hide pia_side_talk
    hide pia_talk
    show pia at pia_near_right
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Hehehe, makasih ya udah mau ngajarin dengan sabar. Makasih juga tadi buat semangatnya, [mcname!c]."
    hide kana_side_talk
    hide kana_talk
    show kana_smile at kana_near_left_2
    with dissolve
    "Kana tersenyum ke arah [mcname!c]. Meskipun ia terlihat kelelahan, senyumannya tetap manis dan membuat [mcname!c] merasa tenang."
    hide kana_smile
    hide tana
    show kana at kana_near_left_2
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Break dulu bentar ya, kita harus obrolin juga buat nanti tampil."
    hide tana_side_talk
    hide tana_talk
    hide pia
    show tana at tana_near
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Okeee. Btw Nay gimana, kamu siap ga? Kan tampil di depan banyak orang."
    hide pia_side_talk
    hide pia_talk
    hide kana
    show pia at pia_near_right
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Eehhhhh iyaa! Aku lupa soal itu aaaaa… Kalo aku pake topeng boleh ga ya?"
    hide kana_side_talk
    hide kana_talk
    hide tana
    show kana at kana_near_left_2
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Haaaa topeng? Ini kan idol Nay, bukan pertunjukan tari tradisional. Ah elah santai aja napa? Lu kan cantik, pasti banyak yang liatin kok. Ga usah malu gitu."
    hide tana_side_talk
    hide tana_talk
    hide pia
    show tana at tana_near
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Setuju sama Tono, santai aja ga usah malu. Nanti liat ke kita atau ke [mcname!c] aja, hahaha."
    hide pia_side_talk
    hide pia_talk
    show pia at pia_near_right
    with dissolve
    "[mcname!c]" "Eh umm, i-iya kali ya? Hahaha."
    hide kana
    show kana_confused at kana_near_left_2
    show kana_side_confused at left
    with dissolve
    kana "Eeh..uuuu..."
    hide kana_side_confused
    with dissolve
    "Kana dan [mcname!c] saling bertatapan dan suasana canggung itu dipecahkan oleh Tana."
    hide kana_confused
    hide tana
    show kana at kana_near_left_2
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Udah lah, nanti juga bisa kok. Yuk lanjut latihan gerakan tadi, pengen liat kalau kita bareng-bareng gimana."
    hide tana_side_talk
    hide tana_talk
    hide pia
    hide kana
    with dissolve
    $ quick_menu = False
    scene awan with Dissolve(2.0)
    $ quick_menu = True
    "Mereka melanjutkan latihan mereka. Kali ini mereka melakukan semuanya dari awal, ditambah dengan bernyanyi juga."
    stop music fadeout 1.0
    $ quick_menu = False
    play music "audio/BGM_Rooftop Sore.ogg" loop fadein 1.0
    scene awan sore with Dissolve(2.0)
    $ quick_menu = True
    "Tak terasa langit telah menjadi sore..."
    $ quick_menu = False
    scene rooftop sore with Dissolve(2.0)
    $ quick_menu = True
    "Saat selesai latihan, Tana dan Pia terkejut."
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Nay… ini serius? Piii serius kan ini? Ini bukan mimpi kan?"
    hide tana_side_talk
    hide tana_talk
    with dissolve
    play sound "SFX - Slap.wav" volume (5.0)
    "Pia pun menampar pipi Tana."
    show tana_angry at tana_near
    show tana_side_angry at left
    with dissolve
    tana "AAAAAAWWWW!! Apaan sih kocak, sakit tau!"
    hide tana_side_angry
    hide tana_angry
    show tana at tana_near
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Oke. Berarti ini bukan mimpi, Ton."
    hide pia_side_talk
    hide pia_talk
    hide tana
    show pia at pia_near_right
    show tana_angry at tana_near
    show tana_side_angry at left
    with dissolve
    tana "Ya ga usah ke gue juga kocak! Kan bisa ke lu sendiri, ahhhh!"
    hide tana_side_angry
    hide tana_angry
    show tana at tana_near
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Hehehe, akhirnya bisa juga. Keren kan?"
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near_left_2
    with dissolve
    "[mcname!c]" "KEREN BANGET! PAKE BANGET, NAY!!"
    hide tana
    show tana_laugh at tana_near
    show tana_side_laugh at left
    with dissolve
    tana "Iyaaa akhirnya lu bisa juga! Aduhhh jadi ini apa yang dirasakan ibu-ibu pas liat anaknya berhasil."
    hide tana_side_laugh
    hide tana_laugh
    hide pia
    show tana at tana_near
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Emang lu punya anak, Ton?"
    hide pia_side_talk
    hide pia_talk
    hide tana
    show pia at pia_near_right
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Ya ga gitu konsepnya, ah elah. Maksudnya gue bangga gitu, kan ga harus jadi ibu supaya bangga."
    hide tana_side_angry_2
    hide tana_angry_2
    hide kana
    show tana at tana_near
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Ibu enggak, tapi jompo iya. Hahahah"
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near_left_2
    with dissolve
    "[mcname!c]" "Kalo soal jompo mah aku setuju sih, ahahah."
    hide tana
    show tana_angry at tana_near
    show tana_side_angry at left
    with dissolve
    tana "Ah elah nyerang gue aja semuanya."
    hide tana_side_angry
    hide tana_angry
    hide pia
    hide kana
    with dissolve
    "Selagi tertawa dan membahas bagaimana perform nanti, waktu tak terasa sudah sore. Satpam kembali memperingatkan [mcname!c], Tana, Pia, dan Kana untuk segera pulang."
    "[mcname!c]" "Eh udah beres-beres belum? Ini udah diingetin lagi sama satpamnya."
    show pia at pia_near_right
    with dissolve
    show tana at tana_near
    with dissolve
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Udah kok, yuk."
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near_left_2
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Eh kalian berdua duluan aja, soalnya kita ada perlu di klub."
    tana "Ga tau ini aku sama Pia dipanggil sama ketua klub, kayaknya ada sesuatu yang urgent deh."
    hide tana_side_talk
    hide tana_talk
    with dissolve
    "[mcname!c]" "Hmmm kok aku sama Kana ga dipanggil ya? Padahal sama-sama panitia juga."
    show pia_talk at pia_near_right
    show pia_side_talk at left
    with dissolve
    pia "Kan kita beda divisi. Gapapa kok duluan aja, nanti kita ngobrol di chat aja."
    hide pia_side_talk
    hide pia_talk
    hide kana
    show pia at pia_near_right
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Oke dehh, duluan yaa~"
    hide kana_side_talk
    hide kana_talk
    hide pia
    hide tana
    with dissolve
    "Kana dan [mcname!c] pergi duluan, sedangkan Tana dan Pia harus pergi ke ruangan klub jejepangan."
    stop music fadeout 1.0
    $ quick_menu = False
    #*SKIP TO SCENE*
    #*BG DEPAN KAMPUS SORE*
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kampus Sore.ogg" loop fadein 1.0
    scene kampus sore with Dissolve(1.0)
    $ quick_menu = True
    "Di perjalanan pulang…"
    show kana at kana_near
    "[mcname!c]" "Jadi gimana perasaan idol kita yang satu ini?"
    hide kana
    show kana_confused at kana_near
    show kana_side_confused at left
    with dissolve
    kana "Iiiihh apaan sih, aku kan belum jadi idol."
    hide kana_side_confused
    hide kana_confused
    show kana at kana_near
    with dissolve
    "[mcname!c]" "Heeee BELUM ya… berarti mau dong."
    hide kana
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Yaaa awalnya sih aku coba-coba."
    kana "Meski sering ngedown, punya pikiran negatif…. Tapi latihan sama mereka, coba nyanyi, coba dance ternyata seruu banget!"
    kana "Aku juga enjoy pas sama mereka. Mungkin kalo kita menang, aku mau deh jadi idol hahah."
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near
    with dissolve
    "[mcname!c]" "Cieeee, kalau gitu besok debut pertama kamu dong."
    hide kana
    show kana_confused at kana_near
    show kana_side_confused at left
    with dissolve
    kana "Iiihhh apaan siihh. Ga usah kaya gitu ah, makin gugup nih aku."
    hide kana_side_confused
    hide kana_confused
    show kana at kana_near
    with dissolve
    "[mcname!c]" "Biar ga gugup nanti aku paling depan deh. Terus bakal jadi yang paling semangat teriaknya, gimana? Jadi kalo gugup, liatnya ke aku aja."
    hide kana
    show kana_confused_blush at kana_near
    show kana_side_confused at left
    with dissolve
    kana "Eh…"
    hide kana_side_confused
    hide kana_confused_blush
    show kana_shy at kana_near
    with dissolve
    "Wajah Kana tersipu mendengar apa yang diucapkan [mcname!c] saat itu"
    hide kana_shy
    show kana_shy_talk at kana_near
    show kana_side_shy at left
    with dissolve
    kana "J-janji ya.."
    hide kana_side_shy
    hide kana_shy_talk
    show kana_shy at kana_near
    with dissolve
    "[mcname!c]" "Iya, janji kok Nay."
    hide kana_shy
    show kana_shy_talk at kana_near
    show kana_side_shy at left
    with dissolve
    kana "A-awas aja kalau enggak."
    hide kana_side_shy
    hide kana_shy_talk
    with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Sambil tersipu malu, Kana dan [mcname!c] pulang ke rumahnya masing-masing."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" loop fadein 1.0
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Di kost..."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(2.0)
    $ quick_menu = True
    "[mcname!c]" "Kalo gugup liat ke aku aja…"
    "[mcname!c]" "Aaaa malu juga kalau diinget-inget."
    "[mcname!c]" "Tapi ya udah deh, yang penting Kana bisa semangat."
    play sound "audio/ReceiveText.ogg" loop
    ".........."
    "[mcname!c]" "Siapa nih?"
    stop music fadeout 1.0
    stop sound fadeout 1.0
    "[mcname!c] pun mengambil HPnya."
    play music "BGM_Happy + HP.ogg" fadein 1.0
    $ quick_menu = False
    nvl clear
    tana_nvl "Eh besok kita datang lebih awal yaa, dari pagi aja biar ada waktu latihan dikit-dikit dan supaya ga gugup juga, gimana?"
    pia_nvl "Gue ikut deh Ton, tapi awas aja lu jangan sampe telat ya."
    kana_nvl "Dih yang bener aja."
    kana_nvl "Aku mah ga pernah telat, coba tanya [mcname!c]."
    mc_nvl "Iya ga telat, cuma mepet aja."
    kana_nvl "Heheh~"
    mc_nvl "Ya udah kalian istirahat. Besok hari besar buat kalian semua, semangat yaa jangan sampe begadang loh."
    kana_nvl "Siappp!"
    pia_nvl "Okee"
    tana_nvl "Okee Brookkk."
    nvl clear
    stop music fadeout 1.0
    scene kamar mc kota with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Monas.ogg" loop fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Tak terasa hari festival pun tiba."
    $ quick_menu = False
    scene depan kampus with Dissolve(2.0)
#HARUSNYA BG Event Jejepangan
    play sound "audio/crowd_noise.mp3" loop fadein 1.0 volume (7.0)
    $ quick_menu = True
    "Hari yang dinanti-nantikan telah tiba, acara event jejepangan pun di buka."
    "Banyak Mahasiswa/i pun bersorak sampai terdengar ke luar kampus."
    "Akan tetapi di tempat lain..."
    stop sound fadeout 1.0
    stop music fadeout 1.0
    $ quick_menu = False
    play music "BGM_UKM.ogg" fadein 1.0
    scene ruang ukm with Dissolve(2.0)
    $ quick_menu = True
    "Kana, Tono, dan Pia seakan tidak mendengar suara tersebut, mereka terus-terusan mencoba beberapa gerakan dan terkadang duduk diam menghafalkan lirik."
    "Kana pun sama, ia duduk diam tangannya yang gemetaran bisa terlihat oleh [mcname!c]."
    "[mcname!c]" "Nay, ikut aku keluar dulu yuk."
    show kana_idol_confused at kana_near
    show kana_idol_side_confused at left
    with dissolve
    kana "Eh?"
    hide kana_idol_side_confused
    hide kana_idol_confused
    with dissolve
    "[mcname!c] menarik tangan Kana, membuat Kana kaget dan berdiri meninggalkan kursinya."
    "[mcname!c] membawa Kana ke area event jejepangan."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Matsuri Malam.ogg"
    play sound "audio/crowd_noise.mp3" loop fadein 1.0 volume (7.0)
    scene matsuri siang with Dissolve(1.0)
    show kana_idol_confused at kana_near
    show kana_idol_side_confused at left
    with dissolve
    $ quick_menu = True
    kana "Eeeh… [mcname!c] kenapa ya?"
    hide kana_idol_side_confused
    hide kana_idol_confused
    show kana_idol at kana_near
    with dissolve
    "[mcname!c]" "Kamu yang kenapa gugup banget, tanganmu gemetaran tuh hahaha."
    hide kana_idol
    show kana_idol_talk at kana_near
    show kana_idol_side_talk at left
    with dissolve
    kana "Gimana ga gugup? Ini kan pertama kalinya aku tampil…"
    hide kana_idol_side_talk
    hide kana_idol_talk
    show kana_idol at kana_near
    with dissolve
    "[mcname!c]" "Ya udah ikut aja yuk, muter-muter event sini. Kita liat-liat dulu ada apa aja."
    hide kana_idol
    show kana_idol_talk at kana_near
    show kana_idol_side_talk at left
    with dissolve
    kana "Boleh deh, dari pada aku pusing sendiri."
    hide kana_idol_side_talk
    hide kana_idol_talk
    with dissolve
    #*SKIP TO SCENE*
    #*BG JEJEPANGAN*
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Kana dan [mcname!c] menikmati booth dan stand yang ada di event jejepangan tersebut."
    "Sesekali Kana dan [mcname!c] juga melihat ke arah main stage di mana ada mini konser yang sedang berlangsung."
    stop sound fadeout 1.0
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_sore.ogg"
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Tak terasa langit telah menjadi sore..."
    $ quick_menu = False
    scene matsuri sore with Dissolve(2.0)
    $ quick_menu = True
    "Terlihat wajah Kana mulai kembali berseri dan mungkin sudah melupakan ke grogiannya meski hanya sedikit."
    show kana_idol_talk at kana_near
    show kana_idol_side_talk at left
    with dissolve
    kana "Hahahaha, asik bangettt~"
    hide kana_idol_side_talk
    hide kana_idol_talk
    show kana_idol at kana_near
    with dissolve
    "[mcname!c]" "Iya kannn? Jadi gimana, udah ga gugup lagi?"
    hide kana_idol
    show kana_idol_talk at kana_near
    show kana_idol_side_talk at left
    with dissolve
    kana "Masih sih, tapi udah lumayan aman. Kayaknya gara-gara udah muter-muter terus ngeliat orang lain perform."
    kana "Ternyata mereka perform karena mereka suka ya, seneng gitu liatnya."
    hide kana_idol_side_talk
    hide kana_idol_talk
    show kana_idol at kana_near
    with dissolve
    "[mcname!c]" "Iyaa kan, tujuan event jejepangan biar bisa have fun. Jadi ga usah gugup yaa."
    hide kana_idol
    show kana_idol_talk at kana_near
    show kana_idol_side_talk at left
    with dissolve
    kana "Siappp.."
    hide kana_idol_side_talk
    hide kana_idol_talk
    with dissolve
    "Di saat mereka sedang bercanda dan melihat performa yang lain, Pia dan Tana menghampiri dengan buru-buru."
    show kana_idol at kana_near_left_2
    show tana_idol at tana_near
    show pia_idol_talk at pia_near_right
    show pia_idol_side_talk at left
    with dissolve
    pia "NAHHH! ITU DIA TON!"
    hide pia_idol_side_talk
    hide pia_idol_talk
    hide tana_idol
    show pia_idol at pia_near_right
    show tana_idol_talk at tana_near
    show tana_idol_side_talk at left
    with dissolve
    tana "Alahhhhh, ke mana aja kalian sihh. Gue nyariin, ayoo cepet siap-siap 30 menit lagi kita tampilll."
    hide tana_idol_side_talk
    hide tana_idol_talk
    hide kana_idol 
    show tana_idol at tana_near
    show kana_idol_talk at kana_near_left_2
    show kana_idol_side_talk at left
    with dissolve
    kana "Eehhhh, [mcname!c]. Aku duluan yaaa, aku mau siap-siap dulu."
    hide kana_idol_side_talk
    hide kana_idol_talk
    show kana_idol at kana_near_left_2
    with dissolve
    "[mcname!c]" "Iyaa, semangat yaa."
    hide kana_idol
    show kana_idol_talk at kana_near_left_2
    show kana_idol_side_talk at left
    with dissolve
    kana "Btw jangan lupa janjimu ya, dadahhhh."
    hide kana_idol_side_talk
    hide kana_idol_talk
    hide pia_idol
    hide tana_idol
    with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    #*SKIP TO SCENE*
    #*BG STAGE*
    scene black with Dissolve(1.0)
    play music "audio/BGM_Matsuri Malam.ogg" loop fadein 1.0
    scene stage with Dissolve(1.0)
    $ quick_menu = True
    "Announcer" "Baiklah, untuk selanjutnya kita akan ada pertunjukan dari salah satu perwakilan klub Jepang!!"
    "Announcer" "Kalo sebelumnya kita udah nonton band, cosplay, dan lainnya. Sekarang kita waktunya untuk melihat idol!!!"
    play sound "SFX - Cheering.ogg" fadein 0.5
    "Announcer" "Apakah kalian semua siap!!??? Ini dia saksikan KTp!!!"
    show tana_idol_side_talk at left 
    with dissolve
    tana "Haloooo semuanya~ Sebelumnya kenalin yaa, kita dari Ktp, Kana, Tana, dan Piaaa~"
    tana "Di sini kita bakalan nyoba nyanyi sama dikit-dikit dance yaa, tapi sebelumnya mari kita kenalan dulu~"
    stop sound fadeout 0.5
    hide tana_idol_side_talk
    show pia_idol_side_talk at left 
    with dissolve
    pia "Halo semuanya~"
    pia "We Are On Fire! Semangat ku membara, siap menghangatkan hari-hari mu!"
    pia "Halo, aku Pia Meraleo dari JKT48V. Senang bertemu kalian!"
    play sound "SFX - Large Cheering.mp3" loop fadein 0.5
    hide pia_idol_side_talk 
    hide pia_idol_talk at pia_near
    with dissolve
    "Penonton" "WUOOOH!!!!"
    stop sound fadeout 0.5
    show tana_idol_side_talk at left 
    with dissolve
    tana "Okeee selanjutnya giliran gue."
    tana "Wassup ma bross!!! I'm fresh like a breeze!"
    tana "JKT48V Tana Nona! Cool enough to make you freeEeEzZEe~"
    play sound "SFX - Large Cheering.mp3" loop fadein 0.5
    hide tana_idol_side_talk 
    hide tana_idol_talk at tana_near
    with dissolve
    "Penonton" "WUOOOH!!!!"
    stop sound fadeout 0.5
    show kana_idol_side_shy_talk at left 
    with dissolve
    kana "Ehh… I-iyaaa… K-kenalin semuanya n-namaku Kanaaaa-"
    $ quick_menu = False
    window auto hide
    stop music fadeout 1.0
    play sound "SFX - Fall.WAV" fadein 1.0 volume(15.0)
    hide kana_idol_side_shy_talk 
    hide kana_idol_shy_talk
    with dissolve
    show kana jatuh at char_center
    show kana jatuh:
        pos (0.53, -0.01) zoom 0.27 
    with dissolve
    pause(4.0)
    window auto show
    $ quick_menu = True
    "Tiba-tiba Kana tersandung di panggung."
    hide kana jatuh with dissolve
    stop sound fadeout 1.0
    "Para penonton pun terdiam, bahkan ada beberapa yang tertawa."
    show kana_idol_side_confused_blush at left
    with dissolve
    "Wajah Kana terlihat pucat dan tangannya gemetaran."
    hide kana_idol_side_confused_blush
    show kana_idol_side_cry at left
    with dissolve
    "Air mata mulai muncul di ujung matanya. Kana sangat gugup dan hampir menangis."
    hide kana_idol_side_cry
    with dissolve
    play music "BGM_Rooftop Pia Malam.ogg" fadein 1.0
    "Tiba-tiba…"
    "[mcname!c]" "KANAIAAA!!!!! SEMANGAATTTTT!!!!"
    "Di antara keheningan para penonton, [mcname!c] berteriak hingga\norang-orang melihat ke arahnya dengan tatapan aneh."
    "Akan tetapi [mcname!c] tidak peduli dan hanya tersenyum ke arah Kana."
    show kana_idol_side_shy_talk at left
    with dissolve
    kana "{i}[mcname!c]??{/i}"
    hide kana_idol_side_shy_talk
    with dissolve
    "Kana terkejut lalu melihat ke arah [mcname!c] dan tersenyum."
    show kana_idol_side_shy at left
    with dissolve
    kana "......."
    hide kana_idol_side_shy
    show kana_idol_side_smile at left
    with dissolve
    kana "{i}[mcname!c].... Terima kasih ya...{/i}"
    hide kana_idol_side_smile
    with dissolve
    "Kana menarik nafas, lalu mengambil micnya dan tersenyum."
    show kana_idol_side_shy_closeeye_talk at left 
    with dissolve
    kana "Uhuk."
    hide kana_idol_side_shy_closeeye_talk
    show kana_idol_side_shy_smile at left
    with dissolve
    kana "Maaf yaaa soal sebelumnya, gugup dikit hehe."
    hide kana_idol_side_shy_smile
    show kana_idol_side_talk at left
    with dissolve
    kana "Oke semuanya. Mari bernyanyi, sambil bermain air. Aku dari laut tapi tidak salty! 🎶🐟"
    hide kana_idol_side_talk
    show kana_idol_side_smile at left 
    with dissolve
    kana "Halo! Aku Kanaia yang akan membuat harimu indah bagai pelangi~"
    play sound "SFX - Large Cheering.mp3" loop fadein 0.5
    hide kana_idol_side_smile
    hide kana_idol_talk at kana_near
    with dissolve
    "[mcname!c]" "KANAAAAAAA!!!!"
    "Penonton" "WUOOOH!!!!"
    show kana_idol_side_talk at left 
    with dissolve
    stop sound fadeout 1.0
    kana "Kalau begitu, dengarkanlah lagu dari kami."
    hide kana_idol_side_talk
    show kana_idol_side_smile at left
    with dissolve
    kana "Dreamcatcher!"
    stop music fadeout 1.0
    hide kana_idol_side_smile
    with dissolve
    "[mcname!c]" "SEMANGAT KANAAA!!!"
    $ quick_menu = False
    scene konser end with Dissolve(2.0)
    play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
    $ quick_menu = False
    show text "{color=#FFF}THE END{/color}" with Pause(2.0)
    with Pause(20.0)
    jump credits