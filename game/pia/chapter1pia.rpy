define char_test = Transform(zoom=0.5,xalign=-2.0,yalign=-2.0)
define pia_route = ""

label chapter1pia:
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene chapter 1 pia with Dissolve (1.0)
    pause(3.0)
    scene black with Dissolve (1.0)
    play music "audio/BGM_Pagi Siang.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya..."
    $ quick_menu = False
    scene depan kampus with Dissolve(2.0)
    $ quick_menu = True
    "Pagi itu [mcname!c] membuka lembaran baru untuk melanjutkan pendidikan ke jenjang selanjutnya."
    "[mcname!c] mengambil jurusan DKV, hari ini merupakan hari di mana aku datang ke kampus."
    "[mcname!c]" "{i}Wah besar juga ya kampusnya.{/i}"
    "[mcname!c]" "{i}Aku bakal kuliah di sini nih.{/i}"
    "[mcname!c]" "{i}Bakal ketemu orang-orang kayak gimana ya...{/i}"
    "[mcname!c]" "{i}Huehuehue, udah gak sabar aku–{/i}"
    $ quick_menu = False
    stop music fadeout 0.3
    scene black with Dissolve(0.3)
    play sound "audio/tabrakan.mp3" volume (4.0)
    show text "{color=#FFF}BRUKKKKK{/color}" with Pause(3.0)
    scene pia tabrakan normal
    play music "audio/BGM_Kampus.ogg" fadein 1.0
    window auto hide
    camera:
        subpixel True xpos -1089 zoom 1.96
        ypos -990
    $ quick_menu = True
    "..."
    $ quick_menu = False
    window auto hide
    camera: 
        linear 7.00 ypos -270 
    with Pause(9.10)
    camera:
        subpixel True pos (0, 0) zoom 1.0
    with Dissolve(1.0)
    with Pause(2.10)
    scene pia tabrakan ngomong with Dissolve(1.0)
    window auto show
    $ renpy.block_rollback()    
    $ quick_menu = True
    pia "Eh maap, Kak. Ketabrak."
    pia "Gak apa-apa kan? Lagi buru-buru."
    pia "Maaf, ya."
    $ quick_menu = False
    scene pia tabrakan normal with dissolve
    $ quick_menu = True
    menu:
        "Respon kamu..."
        "Marahin":
            $ quick_menu = False
            stop music fadeout 1.0
            scene depan kampus with Dissolve(1.0)
            play music "BGM_Bad End.ogg" fadein 1.0
            $ renpy.block_rollback()
            "[mcname!c]" "EH LAIN KALI LIAT-LIAT DONG!"
            "[mcname!c]" "PAKE MATA!!!!!!"
            "[mcname!c]" "LAGI JALAN SANTAI-SANTAI MALAH DITABRAK."
            hide pia_shock
            show pia_silent at pia_near with dissolve
            show pia_side_silent at left with dissolve
            pia "EH, AKU JUGA DAH MINTA MAAF LOH."
            pia "KOK MALAH NGEGAS?"
            $ renpy.block_rollback()
            $ quick_menu = False
            scene black with dissolve
            show text "{color=#FFF}KALIAN BERDUA MALAH BERANTEM TERUS DILIATIN \nDAN BAHKAN DIREKAM ORANG-ORANG.{/color}" with Pause(4.0)
            scene black with dissolve
            show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(2.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits    
        "Nasehatin":
            $ quick_menu = False
            stop music fadeout 1.0
            scene depan kampus with Dissolve(1.0)
            play music "BGM_Bad End.ogg" fadein 1.0
            show pia_shock at pia_near with dissolve
            $ renpy.block_rollback()
            "[mcname!c]" "Iya gapapa, kok."
            "[mcname!c]" "Tapi lain kali ga usah lari-lari, ya."
            "[mcname!c]" "Kalau kata Mamahku tuh-"
            show pia_side_shock at left with dissolve
            pia "Eeh aku lagi buru-buru duh."
            pia "Nanti aja ya nasehatinnya."
            hide pia_side_shock with dissolve
            "[mcname!c] pun menahan tangan perempuan itu agar tidak lari dari tempat tersebut."
            "[mcname!c]" "Ehh kalau ada orang yang lagi nasehatin tuh dengerin dulu."
            "[mcname!c]" "Dilihat lihat nih anak muda jaman sekarang ga mau dengerin nasehat dari orang tua."
            "[mcname!c]" "Mamahku tuh banyak banget nasehat-nasehat yang baik."
            "[mcname!c]" "Dengerin dulu."
            "[mcname!c]" "Jadi-"
            scene black with dissolve
            show text "{color=#FFF}LU MALAH NASEHATIN DAN MALAH BIKIN PEREMPUAN ITU TERLAMBAT \nDAN LU PUN DILIAT ANEH SAMA ORANG-ORANG.{/color}" with Pause(4.0)
            scene black with dissolve
            show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(2.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits
        "Maafin":
            $ renpy.block_rollback()
            "[mcname!c]" "Ah gak papa kok, hehe."
            "[mcname!c]" "Maaf juga, aku ngelamun di tengah jalan."
            $ quick_menu = False
            scene pia tabrakan ngomong with dissolve
            $ quick_menu = True
            pia "Hehe, oke. Maaf, byeeee~"
            $ quick_menu = False
            scene black with Dissolve(1.0)
            scene depan kampus with Dissolve(1.0)
            jump chapter1piacarajalan

label chapter1piacarajalan:
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname!c]" "Ah! Aku juga harus buru-buru daftar ulang!!"
    menu:
        "Cara jalanmu ke sana..."
        "Lari terburu-buru":
            $ quick_menu = False
            stop music fadeout 1.0
            play music "BGM_Bad End.ogg" fadein 1.0
            "[mcname!c]" "{i}EH, udah jam segini!!?? Oke gue lariii.{/i}"
            "[mcname!c] pun memilih untuk lari karena terburu-buru… akan tetapi dia tidak melihat adanya lampu lalu lintas dan akhirnya ketabrak truk"
            scene black with dissolve
            show text "{color=#FFF}ADUHHHH BROOO BURU-BURU SIH... BURU-BURU TAPI GA USAH LARI BANGET JUGA KALI{/color}" with Pause(3.0)
            scene black with dissolve
            show text "{color=#FFF}AKHIRNYA GA LIAT LAMPU MERAH TERUS KETABRAK KAN?!!{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(2.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits
        "Jalan cepat":
            $ renpy.block_rollback()
            $ quick_menu = True
            "[mcname!c] memilih untuk berjalan cepat dan mengabaikan semua orang yang ada. Katanya sih, jalan cepat juga ada di olimpiade. Jadi harusnya efektif."
            $ quick_menu = False
            jump chapter1piajalancepat
        "Jalan biasa":
            $ renpy.block_rollback()
            $ quick_menu = True
            "[mcname!c]" "Eh jalan biasa aja deh, yang penting sampai."
            "[mcname!c]" "Kita harus santai."
            "[mcname!c]" "Kalo kata Mamah, {i}\"Alon-alon sing penting kelakon\".{/i}"
            "[mcname!c] pun memilih untuk jalan biasa dan dia melihat orang sedang kesusahan."
            menu:
                "Respon kamu..."
                "Bantu":
                    $ renpy.block_rollback()
                    $ quick_menu = True
                    "[mcname!c]" "Eh sini aku bantuin."
                    "Orang" "Makasih ya ka, udah mau bantuin."
                    "Orang" "Eh kakak kan, kakak kandung ku yang udah lama ilang ya?"
                    "[mcname!c]" "HA!!?? Bukan aku bukan kakakmu!"
                    "[mcname!c]" "Aku cuma orang lewat."
                    "Orang" "Mana adaaaa."
                    "Orang" "Nih liat ini foto kita waktu dulu."
                    "[mcname!c] pun melihat ke arah pergelangan orang itu dan ia melihat ada gelang yang menunjukan bahwa orang itu merupakan pasien RSJ."
                    $ quick_menu = False
                    stop music fadeout 1.0
                    scene black with dissolve
                    show text "{color=#FFF}WADUH NIAT BAIK TAPI MALAH ZONK.{/color}" with Pause(2.0)
                    scene black with dissolve
                    show text "{color=#FFF}SEKARANG LU MALAH KEJEBAK SAMA ORANG ODGJ.{/color}" with Pause(2.0)
                    play music "audio/BGM_Kampus.ogg" fadein 1.0
                    scene depan kampus with dissolve
                    jump chapter1piacarajalan
                "Diemin":
                    $ renpy.block_rollback()
                    $ quick_menu = True
                    "Setelah [mcname!c] melihat orang tersebut, [mcname!c] memilih untuk mengabaikan orang tersebut dan berjalan kembali."
                    "Akan tetapi, entah kenapa dia diikuti oleh orang tersebut."
                    "Ternyata mereka saling bertatap pandang dan orang itu mengira bahwa [mcname!c] adalah keluarganya."
                    $ quick_menu = False
                    stop music fadeout 1.0
                    scene black with dissolve
                    show text "{color=#FFF}WADUH DI KEJAR GA TUH IIII TAKUTNYEEE{/color}" with Pause(2.0)
                    scene black with dissolve
                    play music "audio/BGM_Kampus.ogg" fadein 1.0
                    scene depan kampus with dissolve
                    jump chapter1piacarajalan

label chapter1piajalancepat:
    $ quick_menu = False
    scene black with Dissolve(1.0)
    pause (1.0)
    scene depan kampus with Dissolve(1.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname!c] pun selesai registrasi daftar ulang ke jurusan DKV."
    $ quick_menu=False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "BGM_Pagi Siang.ogg" fadein 1.0 volume (1.5)
    scene awan with Dissolve(1.0)
    $ quick_menu=True
    "Beberapa hari kemudian..."
    $ quick_menu=False
    scene depan kampus with Dissolve(2.0)
    $ quick_menu=True
    "Walaupun ini sudah pertengahan tahun, namun matahari secara terik menerangi Jakarta dan saat melihat ke atas langit, hanya langit biru lah yang terlihat."
    $ renpy.block_rollback()
    "[mcname!c]" "{i}Untung aja masih sempat untuk ikut orientasi, gak nyangka di Jakarta ternyata beneran macet parah.{/i}"
    "[mcname!c]" "{i}Yah walaupun begitu, ini memang pengalaman baru yang aku rasakan, berbeda jauh dari tempatku dulu.{/i}"
    "[mcname!c]" "{i}Huuuu, ini hari pertamaku orientasi di Jeketi University. Di sini tempat di mana aku bakalan kenal sama orang baru, temen baru, atau bahkan jodoh heheh.{/i}"
    "[mcname!c]" "{i}Oke, saatnya masuk aula.{/i}"
    $ quick_menu = False
    stop music fadeout 1.0
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kelas.ogg" fadein 1.0 volume (1.5)
    scene kelas with Dissolve(1.0)
    play sound "audio/crowd_noise.mp3" loop fadein 1.0 volume (4.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "Saat memasuki ruangan, [mcname!c] mendengar suara di aula yang sangat ramai."
    "[mcname!c]" "{i}Seperti yang diharapkan dari kampus Ibu Kota, orangnya rame banget.{/i}"
    "Terlihat di dalam aula sudah diisi dengan mahasiswa baru."
    "[mcname!c]" "{i}Well, kayaknya aku harus mencari tempat duduk yang kosong sebelum penuh.{i}"
    "[mcname!c] melihat tempat duduk yang berada di pojok atas ruangan."
    "[mcname!c]" "{i}Ah sepertinya itu tidak ada orang.{/i}"
    "[mcname!c] pun berjalan menuju tempat tersebut."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene kelas with Dissolve(1.0)
    $ quick_menu = True
    "Sesampainya di sana, tidak terlihat orang di barisan tersebut."
    "[mcname!c]" "Hmmm... tumben di bagian belakang kosong, padahal biasanya orang pada seneng di belakang."
    "[mcname!c] kemudian duduk di kursi tersebut."
    "[mcname!c]" "Tapi lumayan juga dapat duduk di sini, jadinya bisa ngeliat yang lain dengan jelas."
    "Tiba-tiba terdengar suara pintu terbuka dan seluruh perhatian tertuju kepada sumber suara tersebut."
    stop sound fadeout 1.0
    stop music fadeout 1.0
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Dosen.ogg" fadein 1.0
    scene kelas with Dissolve(1.0)
    $ quick_menu = True
    "Dekan DKV" "Selamat datang Mahasiswa baru yang memasuki Jeketi University…"
    $ quick_menu=False
    scene black with Dissolve(1.0)
    scene awan with Dissolve(1.0)
    $ quick_menu=True
    "Beberapa jam kemudian..."
    $ quick_menu=False
    scene kelas with Dissolve(2.0)
    $ quick_menu=True
    "Dekan DKV" "Baik, sekian pengenalan singkat kita. Selamat datang di Jeketi University para Mahasiswa dan Mahasiswi baru! Raihlah mimpi kalian di sini!! Selamat berjuang! Setelah ini, kalian dipersilahkan untuk pulang."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kelas.ogg" fadein 1.0 volume (1.5)
    scene kelas with Dissolve(1.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname!c]" "Hueeeee.... capek juga duduk doang dengerin orang ngomong. Besok mulai masuk kuliah, gak sabar bakal ketemu orang-orang baru."
    pia "HEEEEEEEEEEEE!! KAMUUUUUUU?!!"
    "[mcname!c]" "Buset, siapa itu teriak-teriak."
    "[mcname!c]" "{i}Loh kok, kayaknya nyamperin aku?{/i}"
    show pia_talk at pia_near
    show pia_side_talk at left 
    with dissolve
    pia "HEYYYYYYY!!! INGET AKU GAKKK??!!!"
    hide pia_side_talk
    show pia at pia_near 
    with dissolve
    "[mcname!c]" "Iya aku inget. Tapi bisa gak tereak, gak?"
    "[mcname!c]" "Malu diliatin banyak orang gini."
    hide pia
    show pia_talk at pia_near 
    show pia_side_talk at left 
    with dissolve
    pia "Oh iya, maap. Hehe..."
    pia "OH! INGET AKU?!"
    pia "KITA TABRAKAN DEPAN GERBANG MINGGU LALU! KIRAIN KAMU SENIOR!"
    pia "TERNYATA MABA JUGA KAYAK AKU, HAHAHAHA!!"
    hide pia_side_talk
    show pia at pia_near 
    with dissolve
    "[mcname!c]" "{i}Buset teriak lagi ini orang.{/i}"
    hide pia
    show pia_side_talk at left 
    with dissolve
    pia "Kamu DKV juga, ya! Gilak ternyata kita sejurusan."
    pia "Apakah jodoh?"
    pia "Candaaaaa, ahahaha."
    hide pia_side_talk
    show pia at pia_near 
    with dissolve
    "[mcname!c]" "Ahaha ahaha iya. Sejurusan ternyata ya kita."
    "[mcname!c]" "Oh iya, kita belom kenalan. Namaku [mcname!c]."
    hide pia
    show pia_side_talk at left 
    with dissolve
    pia "LAH IYA BELOM KENALAN."
    $ pia_name = "Pia Meraleo"
    pia "Halo, aku Pia Meraleo salam kenal."
    $ pia_name = "Pia"
    pia "Kamu panggil aku Pia aja."
    hide pia_side_talk
    show pia at pia_near 
    with dissolve
    "[mcname!c]" "{i}Wah kalo diliat dari dekat gini, Pia imut juga yah.{/i}"
    hide pia
    show pia_side_talk at left 
    with dissolve
    pia "[mcname!c], kok bengong? Makan bareng yuk. Pengen liat kantin kampusnya kayak gimana. Laper juga sih."
    hide pia_side_talk
    show pia at pia_near 
    with dissolve
    "[mcname!c]" "Lah, lesgooo. Pas banget ini lagi laper."
    hide pia_talk 
    hide pia 
    with dissolve
    "[mcname!c] dan Pia pun berjalan ke kantin kampus untuk makan."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kantin.ogg" fadein 1.0
    scene kantin with Dissolve(1.0)
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    pia "WEEEH GEDE JUGA KANTINNYA YA!!"
    hide pia_side_talk
    show pia at pia_near 
    with dissolve
    "[mcname!c]" "Selain kantin, suara kamu juga gede btw."
    hide pia
    show pia_side_talk at left 
    with dissolve
    pia "EH maap, kebiasaan ahahaha."
    hide pia_side_talk
    show pia at pia_near 
    with dissolve
    "[mcname!c]" "Gapapa kok. Seru juga kamu, gak abis-abis energinya."
    show pia_shock at pia_near
    hide pia
    show pia_side_shock at left 
    with dissolve
    pia "I-iya kah? Ahahaha."
    hide pia_side_shock
    hide pia_shock
    hide pia_side_talk
    show pia_side_talk at left 
    with dissolve
    pia "Oh, mau makan di mana ini? Mejanya full semua."
    hide pia_side_talk
    hide pia_talk 
    with dissolve
    "[mcname!c]" "Iya, lagi. Eh tapi di pojokan itu ada meja isinya cuma sendiri. Numpang bareng aja ap--"
    pia "Halooo, sendiri? Boleh numpang duduk 1 meja di sini gak?"
    "[mcname!c]" "Ah....... Pia...... Langsung banget."
    show pia at pia_near_right
    show fio_talk at char_near_left
    show fio_side_talk at left 
    with dissolve
    fio "Eh oh mmm. I-iya k-kosong kok. Duduk aja."
    hide fio_side_talk
    show fio at char_near_left
    with dissolve
    "[mcname!c], Pia, dan perempuan itu duduk di 1 meja yang sama."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene kantin with Dissolve(1.0)
    show pia at pia_near_right 
    show fio at char_near_left
    with dissolve
    $ quick_menu = True
    "Sambil makan..."
    show pia_talk at pia_near_right
    show pia_side_talk at left 
    with dissolve
    pia "Jweerushan aphah kwamuh?\n(Jurusan apa kamu?)"
    hide pia_talk
    hide pia_side_talk
    show fio_talk at char_near_left
    show fio_side_talk at left 
    with dissolve
    fio "Aku? Aku DKV."
    hide fio_side_talk
    hide fio_talk at char_near_left
    show pia_talk at pia_near_right
    show pia_side_talk at left 
    with dissolve
    pia "EEEEEEH SWAAAMAAA!! KOK GWAK LIYAT KWAMU PAS PWENGENALAN?"
    hide pia_talk
    hide pia_side_talk 
    with dissolve
    "[mcname!c]" "Telen dulu, Pia..........."
    "[mcname!c]" "{i}Tapi iya deh, aku gak liat Mbak ini kayaknya pas pengenalan.{/i}"
    show fio_talk at char_near_left
    show fio_side_talk at left 
    with dissolve
    fio "Oh kamu Maba ya? Aku udah semester 4. Ga mungkin ikut ke sana tadi."
    hide fio_talk at char_near_left
    hide fio_side_talk
    show pia_shock at pia_near_right
    show pia_side_shock at left 
    with dissolve
    pia "Eh kakak senior, maaf Kak. Kirain Maba juga."
    show pia_sad at pia_near_right
    hide pia_shock
    hide pia_side_shock
    show pia_side_sad at left 
    with dissolve
    pia "Maaf Kaaak."
    hide pia_side_sad with dissolve
    "[mcname!c]" "Eh maap, Kak. Pia emang kelakuannya nyablak."
    "[mcname!c]" "{i}Yup. pantes gak liat tadi.{/i}"
    $ fio_name = "Fiony"
    hide fio
    show fio_talk at char_near_left
    show fio_side_talk at left 
    with dissolve
    fio "Hahaha santai aja, lanjut makan. Kok jadi kaku kalian?? Kenalin, aku Fiony."
    show fio at char_near_left
    hide fio_side_talk
    show pia_side_sad at left 
    with dissolve
    pia "A-AKU PIA MEAMEO."
    hide pia_side_sad with dissolve
    "[mcname!c]" "Ppppfffftt Meameo, ahaha. Kenalin kak, aku [mcname!c]."
    show pia_silent at pia_near_right
    show pia_side_silent at left 
    with dissolve
    pia "Aaaaa kan jadi typo ngomongnya. Meraleo maksudnyaaaaa."
    hide pia_side_silent with dissolve
    "Mereka bertiga pun melanjutkan makan sembari ngobrol."
    $ quick_menu=False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "BGM_Kelas.ogg" fadein 1.0 volume (1.5)
    scene awan with Dissolve(1.0)
    $ quick_menu=True
    "Keesokan harinya..."
    $ quick_menu=False
    scene kelas with Dissolve(2.0)
    $ renpy.block_rollback()
    show pia_talk at pia_near
    show pia_side_talk at left 
    with dissolve
    $ quick_menu = True
    pia "Hueeeeeee [mcname!c], baru hari pertama tapi kayaknya udah berat gak sih pelajarannya?"
    show pia at pia_near
    hide pia_side_talk 
    with dissolve
    "[mcname!c]" "Engga sih, seru kok kayaknya. Cuma ya… ternyata banyak yang harus kita beli buat pertemuan selanjutnya, nih."
    hide pia
    show pia_side_talk at left 
    with dissolve
    pia "Eh! Iya weeeh! Bingung ini beli ke mana… Mana kita berdua bukan asli Jakarta, gak tau tempat aku. Kamu tau tempat belinya?"
    show pia at pia_near
    hide pia_side_talk 
    with dissolve
    menu:
        "Jawaban kamu..."
        "Aku tau, kebetulan sempet jalan jalan daerah sini pas lowong kemaren.":
            $ renpy.block_rollback()
            $ quick_menu = True
            "[mcname!c]" "Aku tau! Kebetulan sempet jalan-jalan daerah sini pas lowong kemaren."
            hide pia
            show pia_side_talk at left 
            with dissolve
            pia "Ah mantap! Beli di mana? Deket?"
            show pia at pia_near
            hide pia_side_talk 
            with dissolve
            "[mcname!c]" "Agak jauh sih tapi di sana lengkap. Mau beli bareng?"
            show pia_shock at pia_near
            hide pia
            show pia_side_shock at left 
            with dissolve
            pia "M-MAUUUUU!! AYOO."
            hide pia_talk
            hide pia_shock
            hide pia_side_shock 
            with dissolve
            "[mcname!c]" "Okeee~"
            $ quick_menu = False
            stop music fadeout 1.0
            jump chapter1piajalantanpapio
        "Gak tau, belom sempet muter-muter Jakarta. Tanya kak Fiony.":
            $ renpy.block_rollback()
            $ quick_menu = True
            "[mcname!c]" "Gak tau, belom sempet muter-muter Jakarta."
            hide pia
            show pia_side_talk at left 
            with dissolve
            pia "Waduh, gimana ini ya belinya? Hmmmm."
            show pia at pia_near
            hide pia_side_talk 
            with dissolve
            "[mcname!c]" "Eh bukannya kamu kemaren minta nomer Kak Fiony?"
            "[mcname!c]" "Kenapa gak hubungin dia buat nanya?"
            hide pia
            show pia_side_talk at left 
            with dissolve
            pia "LAH IYA JUGAAAA! OTW HUBUNGIN CEPIO."
            show pia at pia_near
            hide pia_side_talk 
            with dissolve
            "[mcname!c]" "Cepio?"
            hide pia
            show pia_side_talk at left 
            with dissolve
            pia "Loh aku udah bestie!! Aku manggil dia Cepio sekarang. Muahahahaha."
            stop music fadeout 1.0
            $ quick_menu = False
            jump chapter1piajalansamapiapio
        "Gak tau, tapi aku sama anak-anak cowok lain mau nyari bareng.":
            $ renpy.block_rollback()
            stop music fadeout 1.0
            $ quick_menu = False
            play music "BGM_Bad End.ogg" fadein 1.0
            "[mcname!c]" "Gak tau, tapi aku sama anak-anak cowok lain mau nyari bareng."
            hide pia 
            show pia_side_talk at left 
            with dissolve
            pia "Yah, yaudah deh. Aku nyari sendiri aja kalo gitu."
            show pia at pia_near
            hide pia_side_talk 
            with dissolve
            "[mcname!c]" "Okeee. Nanti aku kabarin tempatnya di mana, biar kamu tau juga."
            hide pia
            show pia_side_talk at left 
            with dissolve
            pia "Oh oke, makasih"
            scene black with dissolve
            show text "{color=#FFF}TERNYATA [mcname!u] LUPA NGABARIN PIA TEMPATNYA.{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FFF}[mcname!u] JADI LEBIH SENENG NONGKRONG SAMA ANAK-ANAK COWOK DAN MULAI MENJAUH DARI PIA.{/color}" with Pause(3.0)
            scene black with dissolve
            show text "{color=#FF0000}BAD END{/color}" with Pause(2.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits


label chapter1piajalantanpapio:
    scene black with Dissolve (1.0)
    play music "BGM_Kosan 1.ogg" fadein 1.0 volume (0.8)
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True   
    "Malamnya, [mcname!c] mengatur waktu untuk pergi berdua dengan Pia."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(2.0)
    $ quick_menu = True  
    "[mcname!c] meraih HPnya."
    $ quick_menu = False
    nvl clear
    stop music fadeout 1.0
    play music "BGM_Happy + HP.ogg" fadein 1.0 volume (2.0)
    mc_nvl "Besok ketemuan di mana?"
    mc_nvl "Mau berangkat bareng atau janjian ketemuan di sana?"
    pia_nvl "Hmmm… bareng aja ih. Sekalian jalan bareng, hehe."
    mc_nvl "Mau jam berapa?"
    pia_nvl "Iih, terserah kamu aja. Mau jam berapa?"
    mc_nvl "Jam 10 pagi?"
    pia_nvl "OKE!!"
    mc_nvl "Sip, besok aku jemput ya."
    mc_nvl "Ketemuan di kampus?"
    pia_nvl "Alamat kosan aku di xxxxxx"
    pia_nvl "EH, MAU DI KAMPUS JUGA GAPAPA"
    mc_nvl "Oke aku jemput ke kosan, ya"
    $ renpy.block_rollback()
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    show text "{color=#FFF}KEESOKAN HARINYA{/color}" with Pause(2.0)
    play music "BGM_Happy + HP.ogg" fadein 1.0 volume (2.0)
    scene depan kosan with Dissolve(1.0)
    $ renpy.block_rollback()
    nvl clear
    mc_nvl "Udah di depan kosan, yak."
    pia_nvl "TUNGGU!!!"
    nvl clear
    $ renpy.block_rollback()
    scene depan kosan with Dissolve(0.3)
    $ quick_menu = True
    "Pia pun keluar dari kosan, siap untuk pergi dengan [mcname!c]."
    show pia_date_talk at pia_near
    show pia_date_side_talk at left 
    with dissolve
    pia "GAK TELAT, KAN? PAS KAN YA AKU SIAP SIAPNYA? JAM 10 UDAH READY."
    show pia_date at pia_near
    hide pia_date_side_talk 
    with dissolve
    "[mcname!c]" "Tetangga kosan kamu gak ada yang komplain ya, tiap hari ada yang teriak kayak kemalingan gini?"
    hide pia_date
    show pia_date_side_talk at left 
    with dissolve
    pia "HEH, SEMBARANGAN! HAHAHA."
    hide pia_date_side_talk
    hide pia_date_talk 
    with dissolve
    "[mcname!c] dan Pia pun berangkat bersama menuju lokasi tempat membeli peralatan DKV tersebut."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Mall.ogg" fadein 1.0
    scene mall temp with Dissolve(1.0)
    show pia_date_talk at pia_near 
    show pia_date_side_talk at left 
    with dissolve
    $ quick_menu = True
    pia "Wah gede juga ya mallnya."
    show pia_date at pia_near
    hide pia_date_side_talk 
    with dissolve
    "[mcname!c]" "Sebelah situ Pia tempatnya."
    hide pia_date 
    show pia_date_side_talk at left 
    with dissolve
    pia "Let's gooo!!!"
    show pia_date at pia_near
    hide pia_date_side_talk 
    with dissolve
    "[mcname!c]" "Gak usah lari, nanti ilang."
    show pia_date_silent at pia_near
    hide pia_date
    show pia_date_side_silent at left 
    with dissolve
    pia "Lu kata gue anak kecil, heh?!"
    hide pia_date_side_silent 
    with dissolve
    "[mcname!c]" "Ahahahahaha~"
    $ quick_menu = False
    scene black with Dissolve(0.3)
    play sound "audio/tabrakan.mp3" volume (4.0)
    show text "{color=#FFF}BRUKKKKK{/color}" with Pause(1.5)
    scene mall temp with Dissolve(1.0)
    show pia_date_sad at pia_near
    hide pia_angry
    show pia_date_side_sad at left 
    with dissolve
    $ quick_menu = True
    pia "Aaaah! Maaf, Pak."
    hide pia_side_sad with dissolve
    "*Orang tersebut dengan tatapan sinis langsung pergi*"
    "[mcname!c]" "Udah gapapa, orangnya lagi buru-buru kali."
    "[mcname!c]" "Sini..."
    "[mcname!c] pun menggenggam tangan Pia."
    show pia_date_shock at pia_near
    hide pia_date_sad
    show pia_date_side_shock at left 
    with dissolve
    pia "Ii-iya, maaci."
    hide pia_side_shy
    hide pia_date_side_sad
    hide pia_date_shock
    hide pia_date_side_shock
    with dissolve
    "Kemudian Pia dan [mcname!c] menuju toko yang menjual peralatan menggambar tersebut sambil bergandengan tangan."
    $ quick_menu=False
    scene black with Dissolve(1.0)
    scene awan with Dissolve(1.0)
    $ quick_menu=True
    "Beberapa jam kemudian..."
    $ quick_menu=False
    scene mall with Dissolve(2.0)
    show pia_date_talk at pia_near_right
    show pia_date_side_talk at left 
    show book
    show book:
        xpos 0.58 ypos 0.72 zoom 0.25 
    with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    pia "Weeeeeeh mahal juga ya jadinya, tadi sih murah pas liat satuan. Pensil 2, cat air 1, kuas, dan sebagainya.... Tapi pas dijumlah gak kerasa, tau-tau mahal juga."
    hide book
    hide pia_date_side_talk 
    hide pia_date_talk 
    show pia_date_talk at pia_near
    show pia_date at pia_near
    with dissolve
    "[mcname!c]" "Hahaha betuuuul."
    "*Tiba-tiba dari belakang ada yang berbisik*"
    "???" "{size=-5}Hayooo lagi ngapain berduaan?{/size}"
    "[mcname!c]" "HUAAAAA.."
    "[mcname!c]" "KAGET, KAK FIONY??!!!"
    hide pia_date_talk
    hide pia_date 
    show pia_date at pia_near_right 
    show fio_talk at char_near_left 
    show fio_side_talk at left 
    with dissolve
    fio "Haloooo~ Lagi ngapain nih kalian?"
    show fio at char_near_left 
    hide fio_side_talk 
    with dissolve
    "[mcname!c]" "Ini abis beli perlengkapan buat tugas nirmana, Kak."
    hide fio 
    show fio_side_talk at left 
    with dissolve
    fio "Kiw-kiw~ \n*Melirik Pia*"
    show fio at char_near_left
    hide fio_side_talk
    show pia_date_shock at pia_near_right 
    show pia_date_side_shock at left 
    with dissolve
    pia "CEPIOOOOOOOOOOO!!!!"
    hide pia_date_side_shock 
    show fio_smile at char_near_left 
    show fio_side_grin at left 
    with dissolve
    fio "Hahahahahaha.\n*sambil peluk Pia*"
    hide fio_side_grin 
    hide fio_smile 
    with dissolve
    "[mcname!c]" "Sejak kapan kalian jadi akrab banget?"
    hide pia_date_shock 
    show pia_date_talk at pia_near_right 
    show pia_date_side_talk at left 
    with dissolve
    pia "Tau gak sih [mcname!c], ternyata rumah Cepio deket sama kosan aku!! Jadi kita banyak ngobrol gituuuu, ehehehe."
    hide pia_date_talk 
    hide pia_date_side_talk 
    hide fio 
    show fio_side_talk at left 
    with dissolve
    fio "Sama, lagi beli peralatan juga, udah banyak yang abis. Di sini juga tempat langganan aku."
    fio "Btw, panggil Cepio aja."
    hide fio_side_talk 
    show fio at char_near_left 
    with dissolve
    "[mcname!c]" "Oke Cepioooo~"
    show pia_date_talk at pia_near_right
    show pia_date_side_talk at left 
    with dissolve
    pia "Nah mumpung ada Cepio, Si Sepuh penunggu mall ini, mending rekomendasiin tempat makan enak di sini."
    jump chapter1piamakanmall

label chapter1piajalansamapiapio:
    scene black with Dissolve(1.0)
    play music "audio/BGM_Mall.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya..."
    $ quick_menu = False
    scene mall temp with Dissolve(2.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname!c]" "{i}Hmmmm... Janjiannya di depan toko Kautsar As, tapi mana nih Pia sama Kak Fiony belum sampe.{/i}"
    "[mcname!c]" "{i}Udah setengah jam nunggu huhuhu.{/i}"
    show fio at char_near_left 
    show pia_date_talk at pia_near_right 
    show pia_date_side_talk at left 
    with dissolve
    pia "[mcname!u]!!!!!!! HOIIII!!! MAAAP TELAAAAAT!!"
    show pia_date at pia_near_right 
    hide pia_date_side_talk 
    show fio_talk at char_near_left
    show fio_side_talk at left 
    with dissolve
    fio "Maap ya [mcname!c], tadi nungguin Pia. Dandan dulu lama banget, mana macet pula di jalan."
    hide fio_talk
    hide fio_side_talk
    show pia_date_silent at pia_near_right
    show pia_date_side_silent at left
    with dissolve
    pia "Dih! Kok Cepio nyalahin aku??"
    hide pia_date_side_silent
    show fio_talk at char_near_left
    show fio_side_talk at left
    with dissolve
    fio "Tapi kan emang dandannya lama tadi. Padahal cuma mau belanja cat, buku, dan sebagainya kan?"
    fio "Ngapain harus dandan banget yang banget-banget? Apa jangan-jangan kamu s--"
    hide fio_talk 
    hide fio_side_talk 
    show pia_date_shock at pia_near_right 
    hide pia_date_silent
    show pia_date_side_shock at left 
    with dissolve
    pia "Ssssss aaaaah. Dah dah, jadi kemana mana ini. Lesgow! Lead the waaaay, Cepio!!!!"
    hide pia_date_silent
    hide pia_date
    hide pia_side_shock 
    with dissolve
    "[mcname!c]" "Sejak kapan kalian jadi akrab banget?"
    hide pia_date_shock 
    show pia_date_side_talk at left 
    with dissolve
    pia "Tau gak sih [mcname!c], ternyata rumah Cepio deket sama kosan aku!!"
    pia "Jadi kita banyak ngobrol gituuuu, ehehehe."
    hide pia_date_side_talk
    hide pia_date_talk
    hide fio
    with dissolve
    "Mereka pun berjalan sambil mengobrol panjang lebar."
    $ quick_menu = False
    scene mall with Dissolve(2.0)
    $ renpy.block_rollback()
    show pia_date at pia_near_right
    show fio_talk at char_near_left
    show fio_side_talk at left
    with dissolve
    $ quick_menu = True
    fio "Di sini tempatnya. Tadaaaaaa~"
    show fio at char_near_left
    hide fio_side_talk
    show pia_date_talk at pia_near_right 
    show pia_date_side_talk at left 
    with dissolve
    pia "WOAAAAA LENGKAP BANGET!!!"
    hide pia_date_talk 
    hide pia_date_side_talk
    with dissolve
    "[mcname!c]" "Wah mantap, makasih Kak Fiony!"
    hide fio
    show fio_side_talk at left 
    with dissolve
    fio "Cepio ajaaa. Panggil aku Cepio, hehe."
    show fio at char_near_left 
    hide fio_side_talk
    show pia_date_silent at pia_near_right 
    with dissolve
    "[mcname!c]" "Ah oke, Cepio hehe."
    show pia_date_side_silent at left with dissolve
    pia "Hmmmmmm!!!\n*Bombastic side eyes*"
    hide pia_date_side_silent 
    hide fio 
    show fio_side_talk at left 
    with dissolve
    fio "{size=-5}Cieee cemburu, hehehe.{/size}"
    show fio at char_near_left 
    hide fio_side_talk
    show pia_date_side_silent at left 
    with dissolve
    pia "CEPIOOOOOOOO!!!!!!"
    hide pia_date_side_silent with dissolve
    "[mcname!c]" "????"
    hide pia_date
    hide pia_date_talk
    hide pia_date_silent 
    hide fio_talk
    hide fio 
    with dissolve
    "Fiony pun membantu merekomendasikan peralatan yang dibutuhkan [mcname!c] dan Pia."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Beberapa saat kemudian..."
    $ quick_menu = False
    scene mall temp with Dissolve(2.0)
    show pia_date_talk at pia_near_right
    show fio at char_near_left
    show pia_date_side_talk at left
    with dissolve
    $ quick_menu = True
    pia "Weeeeeeh mahal juga ya jadinya, tadi sih murah pas liat satuan."
    pia "Pensil 2, cat air 1, kuas, dan sebagainya."
    pia "Tapi pas dijumlah gak kerasa, tau-tau mahal juga."
    show pia_date at pia_near_right 
    hide pia_date_side_talk
    show fio_talk at char_near_left 
    show fio_side_talk at left 
    with dissolve
    fio "Welcome to DKV."
    hide fio_talk 
    hide fio_side_talk 
    hide pia_date
    show pia_date_sad at pia_near_right
    with dissolve
    "{size=-5}[mcname!c] & Pia{/size}" "Huhuuuu."
    show pia_date_side_talk at left
    hide pia_date_sad at pia_near_right
    with dissolve
    pia "BTW… MAU MAKAAAAAN!! Lapeerrr."
    show pia_date at pia_near_right 
    hide pia_date_side_talk 
    with dissolve
    "[mcname!c]" "Setuju, laper."
    jump chapter1piamakanmall

label chapter1piamakanmall:
    hide pia_date_side_talk 
    hide pia_side_talk
    hide fio
    show fio_talk at char_near_left
    show fio_side_talk at left
    with dissolve
    fio "Ayo, aku ada tempat rekomendasi enak deket sini."
    hide fio_talk
    hide fio_side_talk
    show pia_date_talk at pia_near_right 
    hide pia_date
    show fio at char_near_left
    with dissolve
    "{size=-5}[mcname!c] & Pia{/size}" "Lesgoooooo~"
    hide pia_date_talk
    hide fio
    with dissolve
    "Mereka bertiga pun menuju cafe tempat nongkrong Fiony dan mulai memesan makanan yang direkomendasikan Fiony."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play sound "audio/cafe-entrance.mp3" fadein 1.0
    play music "audio/BGM_Cafe Cerah.ogg" fadein 1.0 volume (2.0)
    scene cafe with Dissolve(1.0)
    show pia_date_talk at pia_near_right
    show fio at char_near_left
    show pia_date_side_talk at left
    with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    pia "Ummmmmmmm!!!!! Enaaaaak!!! Mantap lah, Cepio!\n*Sambil makan*"
    show pia_date at pia_near_right 
    hide pia_date_side_talk 
    show fio_talk at char_near_left 
    show fio_side_talk at left 
    with dissolve
    fio "Hehehe enak, kan? Tempat langganan aku sama temen-temen aku nih. Enak, terus tempatnya cozy gitu buat foto-foto."
    hide fio_talk 
    hide fio_side_talk 
    hide pia_date 
    show pia_date_side_talk at left 
    with dissolve
    pia "Betuuuuul!!!"
    hide pia_date_talk 
    hide pia_date_side_talk 
    hide fio 
    with dissolve
    "Dari meja yang cukup jauh dari tempat [mcname!c], Pia, dan Fiony duduk…"
    $ freya_name = "???"
    show freya_talk at fio_near 
    show freya_side_talk at left 
    with dissolve
    freya "Lah, Fiony? Ngapain kamu di sini?"
    hide freya_talk
    hide freya_side_talk 
    show fio_talk at fio_near 
    show fio_side_talk at left 
    with dissolve
    fio "Lah Freya? Sama… mmmm..."
    $ freya_name = "Freya"
    hide fio_talk
    hide fio_side_talk
    with dissolve
    $ kana_name = "Kana"
    show freya at char_near_left 
    show kana_date_talk at kana_near_right 
    show kana_date_side_talk at left 
    with dissolve
    kana "Salam kenal, aku Kana."
    show freya_talk at char_near_left
    show kana_date at kana_near_right 
    hide kana_date_side_talk 
    show freya_side_talk at left
    with dissolve
    freya "Sini."
    hide freya_talk
    hide kana_date_talk
    hide freya_side_talk 
    hide freya 
    hide kana_date 
    show fio_talk at fio_near 
    show fio_side_talk at left 
    with dissolve
    fio "Okeh."
    hide fio_talk 
    hide fio_side_talk 
    show fio_smile at char_near_left 
    show pia_date at pia_near_right 
    show fio_side_grin at left 
    with dissolve
    fio "Ges, aku ke sana dulu sebentar ya. Kalian berduaan aja dulu. Jangan macem-macem ya [mcname!c]. Hehehe."
    hide fio_smile 
    hide fio_side_grin 
    hide pia_date 
    show pia_date_shock at pia_near 
    show pia_date_side_shock at left 
    with dissolve
    pia "CEPIOOOOOOOOOOOOO~"
    hide pia_date_side_shock with dissolve
    "[mcname!c]" "Ahahahahha."
    show pia_date_side_shock at left with dissolve
    pia "J-jadi… Abis berapa tadi belanja alat gambar?"
    hide pia_date_side_shock with dissolve
    "[mcname!c]" "400an lah, ahahaha. Kamu abis berapa?"
    show pia_date_sad at pia_near 
    show pia_date_side_sad at left 
    with dissolve
    pia "Kurang lebih sama lah, huhuhu~"
    hide pia_date_side_sad 
    with dissolve
    "*Hening*"
    hide pia_date_sad
    with dissolve
    "[mcname!c]" "Kalo berdua gini kayak ngedate gak sih kita?"
    $ quick_menu=False
    window auto hide
    hide pia_date_shock
    with dissolve
    show pia_nyembur with dissolve:
        zoom 0.3
        xalign 0.8
    $ quick_menu=True
    window auto show
    pia "UHUK-UHUK!!"
    hide pia_date_side_shock
    hide pia_nyembur
    show pia_date_side_shock at left
    show pia_date_shock at pia_near 
    with dissolve
    pia "GIMANA??!!!"
    hide pia_date_side_shock at left
    with dissolve
    "[mcname!c]" "Ahahaha, engga. Bercanda kok."
    show pia_date_side_sad at left 
    show pia_date_sad at pia_near 
    with dissolve
    pia "{size=-10}Ngedate beneran juga gapapa sih..{/size}"
    hide pia_date_sad 
    hide pia_date_side_sad 
    with dissolve
    "[mcname!c]" "Apa, Pia? Sorry, gak kedengeran?"
    show pia_date_side_shock at left with dissolve
    pia "GAK KOK, minumannya enak. Aku haus, mau nambah kayaknya."
    hide pia_date_side_shock with dissolve
    "[mcname!c]" "Oh okeh, mau aku panggil pelayannya?"
    show pia_date_silent at pia_near 
    show pia_date_side_silent at left 
    with dissolve
    pia "Gausah."
    hide pia_date_side_silent with dissolve
    "[mcname!c]" "Lah???"
    "*Suasana hening*"
    show pia_date_talk at pia_near 
    hide pia_date_silent
    hide pia_date_shock
    show pia_date_side_talk at left 
    with dissolve
    pia "Eh, btw tempatnya bagus gak sih buat foto-foto?"
    show pia_date at pia_near 
    hide pia_date_side_talk 
    with dissolve
    "[mcname!c]" "Tadi Cepio sih ngomong gitu juga."
    hide pia_date 
    show pia_date_side_talk at left 
    with dissolve
    pia "Selfie ah!!"
    window auto hide
    $ quick_menu=False
    play sound "audio/camera.mp3" volume (2.0)
    hide pia_date_side_talk with dissolve
    stop sound 
    with Pause(1.0)
    show pia_date_shock at pia_near 
    show pia_date_side_shock at left 
    with dissolve
    $ quick_menu=True
    window auto show
    pia "F-foto bareng sih kita. Udah jauh-jauh makan ke sini, masa ga difoto!"
    hide pia_date_side_shock with dissolve
    "[mcname!c]" "Hmm. Boleh deh.\n*Bergaya*"
    show pia_date_side_shock at left with dissolve
    pia "Oke, satuu..dua....tigaaaa~"
    hide pia_date_side_shock
    show pia_date_smile at pia_near
    with dissolve
    play sound "audio/camera.mp3" volume (2.0)
    "Fiony ngeliatin dari jauh sambil senyum-senyum ngeledek nyindir Pia."
    hide pia_date_smile 
    show pia_date_side_shock at left 
    with dissolve
    pia "CEPIOOOOOOOO!!"
    hide pia_date_talk
    hide pia_date_silent
    hide pia_date_side_shock 
    hide pia_date_shock 
    show pia_date_shock at pia_near_right 
    show fio_talk at char_near_left 
    show fio_side_talk at left 
    with dissolve
    fio "Ahahaha udah makannya? Seru tuh foto fotonya. \n*Sikut-sikut Pia*"
    show fio at char_near_left 
    hide fio_side_talk 
    show pia_date_side_shock at left 
    with dissolve
    pia "Ehehehehe~"
    show pia_date at pia_near_right 
    hide pia_date_shock 
    hide pia_date_side_shock 
    show fio_side_talk at left 
    hide fio 
    with dissolve
    fio "Kuy lah balik, takut kemaleman. Udah aku bayarin juga tadi makanannya ya."
    show fio at char_near_left 
    hide fio_side_talk 
    with dissolve
    "[mcname!c]" "Eh lah udah dibayar? Waduh aku transfer ke Cepio ya."
    hide fio 
    show fio_side_talk at left 
    with dissolve
    fio "Gausah. Ngeliat juniorku SENYUM-SENYUM sendiri udah cukup puas kok.\n*Senyum ke Pia*"
    show fio at char_near_left 
    hide fio_side_talk 
    show pia_date_silent at pia_near_right 
    show pia_date_side_silent at left 
    with dissolve
    pia "Ih Cepio maaaaaaaah. Ngeledekin muluuuuu~"
    #fio "Hehe~"
    hide pia_date_shock
    hide pia_date_silent
    hide pia_date_side_silent
    hide fio_talk
    hide fio
    hide pia_date
    with dissolve
    "Fiony berpisah dengan Pia dan [mcname!c]. Kemudian mereka pun pulang ke tempat tinggal masing-masing."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" fadein 1.0 volume (0.8)
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Di kost..."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(2.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname!c]" "Huaaaaa capeeeeek~\n*Langsung rebahan di kasur*"
    "[mcname!c]" "Seru juga hari ini, hehehe."
    "[mcname!c]" "Yosshaaaa! Saatnya bersih-bersih terus rapihin peralatan yang dibeli tadi, terus tiduuur."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kelas.ogg" fadein 1.0 volume(1.5)
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya..."
    $ quick_menu = False
    scene kelas with Dissolve(2.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "Mata kuliah nirmana dimulai, [mcname!c] dan Pia pun menggunakan peralatan yang dibelinya kemarin."
    $ quick_menu=False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "BGM_sore.ogg" fadein 1.0 volume (1.5)
    scene awan sore with Dissolve(1.0)
    $ quick_menu=True
    "Tak terasa berjam jam telah lewat..."
    $ quick_menu=False
    scene kelas sore with Dissolve(2.0)
    show pia_talk at pia_near 
    show pia_side_talk at left 
    with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    pia "[mcname!u]!!!!!! MUMET GUEH! AYO KELUAR. REFRESHING KE MANA KEK, MUTERIN KAMPUS."
    pia "NANTI MASIH ADA KELAS LAGI, JADI GA BISA JAUH-JAUH."
    show pia at pia_near 
    hide pia_side_talk 
    with dissolve
    "[mcname!c]" "Lesgo, sama. Pusing weh."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene lorong sore with Dissolve(1.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "Pia dan [mcname!c] pun berkeliling di kampus tanpa arah dan tujuan."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Sawah Sore.ogg" fadein 1.0
    scene sawah sore with Dissolve(1.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "Sampai akhirnya mereka masuk ke kawasan fakultas pertanian dan kehutanan."
    "Saat berjalan berdua..."
    # BGM STOP
    pia "Hmmm... Hmmmmm..\n*Bergumam*"
    "[mcname!c]" "*Berjalan di sebelah Pia sambil sesekali memejamkan mata menikmati suara Pia yang sedang humming*"
    # Harusnya ada humming migikata
    show pia at pia_near with dissolve
    "[mcname!c]" "Lagu apa Pia?"
    show pia_talk at pia_near 
    show pia_side_talk at left 
    with dissolve
    pia "Oh, ini judulnya Migikata."
    hide pia_talk 
    hide pia_side_talk 
    with dissolve
    "[mcname!c]" "Hmm, hummingmu bagus Pia. Merdu banget, hehe."
    show pia_shock at pia_near 
    show pia_side_shock at left 
    with dissolve
    pia "A-apaan sih!"
    pia "Huft~"
    hide pia_shock
    hide pia_side_shock
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    pia "Eh, ke situ yuk. Duduk bawah pohon."
    hide pia_talk 
    hide pia_side_talk 
    with dissolve
    "[mcname!c]" "Kuy!!"
    "[mcname!c] dan Pia pun duduk di bawah pohon rindang dekat pesawahan."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene sawah sore with Dissolve(1.0)
    $ quick_menu = True
    "Pia mengeluarkan HP dan earphone cablenya."
    show pia_talk at pia_near 
    show pia_side_talk at left 
    with dissolve
    pia "Mau denger lagu yang tadi aku nyanyiin nadanya? Nih."
    stop music fadeout 1.0
    hide pia_talk 
    hide pia_side_talk 
    with dissolve
    play music "audio/BGM_Migikata.ogg" fadein 1.0 volume (3.0)
    "Tiba-tiba Pia memasangkan earphonenya ke telinga [mcname!c]."
    pia "*Mulai bernyanyi lagu yang sedang didengarkan.*"
    "[mcname!c]" "{i}Woaaaa suara Pia bagus juga ternyata.{/i}"
    $ quick_menu = False
    scene black with Dissolve(1.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname!c] memejamkan mata menikmati alunan suara Pia yang sedang bernyanyi."
    $ quick_menu = False
    scene sawah sore with Dissolve(1.0)
    $ renpy.block_rollback()
    $ quick_menu=False
    window auto hide
    show black:
        default
        subpixel True 
        parallel:
            Null(0.0, 0.0)
            'black' with dissolve
        parallel:
            ypos 0 alpha 1.0 
            linear 1.30 ypos 252 alpha 0.7 
    show black as black2:
        default
        subpixel True 
        parallel:
            Null(0.0, 0.0)
            'black' with dissolve
        parallel:
            ypos 2080 alpha 1.0 
            linear 1.30 ypos 1908 alpha 0.7 
    with Pause(1.40)
    show pia at pia_near
    show pia:
        pos (0.45, -0.13) zoom 1.52 
    with dissolve
    window auto show
    $ quick_menu = True
    "*Pia pun tanpa sadar menyenderkan kepalanya di pundak kanan [mcname!c]*"
    "[mcname!c]" "Kamu suka lagunya ya?"
    show pia_smile at pia_near 
    show pia_smile:
        pos (0.45, -0.13) zoom 1.52 
    show pia_side_smile at left 
    with dissolve
    pia "Um.."
    pia "Suka banget."
    hide pia_smile
    hide pia_side_smile at left 
    hide pia_talk 
    with dissolve
    "[mcname!c]" "Artinya apa?"
    show pia_side_talk at left 
    show pia_talk at pia_near 
    show pia_talk:
        pos (0.45, -0.13) zoom 1.52 
    with dissolve
    pia "Tiap kali lagi sedih, bad mood, atau galau, jadi tenang pas denger lagu ini."
    hide pia_talk 
    hide pia_side_talk 
    with dissolve
    "[mcname!c]" "Eeeh? Kamu lagi bad mood kah sekarang?"
    show pia_talk at pia_near 
    show pia_talk:
        pos (0.45, -0.13) zoom 1.52 
    show pia_side_talk at left 
    with dissolve
    pia "Nggak kok."
    pia "Tiap kali aku denger lagu ini, aku bisa ngelupain masalah yang aku hadapi."
    pia "Well… masalah bakal tetep ada sih, tapi untuk sejenak rasanya masalah itu hilang."
    pia "Aku sebenernya baru sih suka lagu ini."
    pia "Entah kenapa…"
    pia "Lagu ini seolah ngingetin aku ke seseorang."
    hide pia_talk
    hide pia_side_talk
    show pia at pia_near 
    show pia:
        pos (0.45, -0.13) zoom 1.52
    with dissolve
    pia "*Melirik [mcname!c]*"
    show pia_talk at pia_near 
    show pia_talk:
        pos (0.45, -0.13) zoom 1.52 
    show pia_side_talk at left
    hide pia
    with dissolve
    pia "Seseorang yang selalu ada untuk aku…"
    pia "Seseorang yang bisa menerima aku apa adanya..."
    pia "Seseorang yang sayang aku…"
    pia "Aku mungkin susah untuk jujur, tapi aku harap orang itu tau bahwa the feeling is mutual."
    show pia_smile at pia_near 
    show pia_smile:
        pos (0.45, -0.13) zoom 1.52 
    show pia_side_smile at left
    hide pia_talk
    hide pia_side_talk
    with dissolve
    pia "Aku bakal nerima dia dan janji selalu ada untuk dia. Seperti dia yang selalu ada untuk aku…"
    show pia at pia_near 
    show pia:
        pos (0.45, -0.13) zoom 1.52 
    show pia_side at left
    hide pia_smile
    hide pia_side_smile
    with dissolve
    pia "......"
    show pia_talk at pia_near 
    show pia_talk:
        pos (0.45, -0.13) zoom 1.52 
    show pia_side_talk at left
    hide pia
    hide pia_side
    with dissolve
    pia "[mcname!c], 5 tahun lagi menurutmu kita bakal di mana?"
    hide pia_talk 
    hide pia_side_talk 
    show pia at pia_near 
    show pia:
        pos (0.45, -0.13) zoom 1.52 
    with dissolve
    "[mcname!c]" "Pia..."
    show pia_smile at pia_near 
    show pia_smile:
        pos (0.45, -0.13) zoom 1.52 
    show pia_side_smile at left
    hide pia
    with dissolve
    pia "Hehe~"
    hide pia_smile 
    hide pia_side_smile 
    with dissolve
    $ quick_menu=False
    window auto hide
    show black:
        subpixel True 
        ypos 252 
        linear 1.30 ypos -9 
    show black as black2:
        subpixel True 
        ypos 1908 
        linear 1.30 ypos 2169 
    with Pause(1.40)
    scene black with Dissolve(1.0)
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Tak terasa, waktu kelas sore akan dimulai."
    $ quick_menu = False
    scene sawah sore with Dissolve(2.0)
    show pia_talk at pia_near
    show pia_side_talk at left
    with dissolve
    $ quick_menu = True
    pia "A-AAAHH! UDAH KELAMAAN! AYOK BALIK KE KELAS LAGI!"
    hide pia_talk
    hide pia_side_talk
    with dissolve
    "Pia pun menegakkan kepalanya kembali dari pundak [mcname!c]. Mereka kembali ke fakultasnya untuk memasuki kelas yang dimulai sore itu."
    $ got_selfie.grant()
    jump chapter2piabegin