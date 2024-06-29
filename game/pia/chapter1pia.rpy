define char_test = Transform(zoom=0.5,xalign=-2.0,yalign=-2.0)


label chapter1pia:
    scene awan with dissolve
    scene depan kampus with Dissolve(2.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "Pagi ini kubuka lembaran baru untuk melanjutkan pendidikanku ke jenjang selanjutnya. Aku mengambil jurusan DKV, hari ini merupakan hari dimana aku datang ke kampus."
    mcname "{i}Wah besar juga ya kampusnya,{/i}"
    mcname "{i}Aku bakal kuliah disini nih.{/i}"
    mcname "{i}Bakal ketemu orang-orang kayak gimana ya…{/i}"
    mcname "{i}Huehuehue, udah gak sabar aku–{/i}"
    $ quick_menu = False
    scene black with dissolve
    play sound "audio/tabrakan.mp3"
    show text "{color=#FFF}BRUKKKKK{/color}" with Pause(2.0)
    scene pia tabrakan normal    
    play music "audio/BGM_Kampus.mp3" fadein 1.0
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
    window auto show
    camera:
        subpixel True pos (0, 0) zoom 1.0
    with Pause(2.10)
    scene pia tabrakan ngomong with dissolve
    $ renpy.block_rollback()    
    $ quick_menu = True
    pia "Eh maap, Kak. Ketabrak."
    pia "Gak apa-apa kan? Lagi buru-buru."
    pia "Maaf, ya."
    $ quick_menu = False
    scene pia tabrakan normal with dissolve
    menu:
        "Respon kamu..."
        "Marahin":
            scene depan kampus with dissolve
            $ renpy.block_rollback()
            $ quick_menu = True
            mcname "EH LAIN KALI LIAT-LIAT DONG!"
            mcname "PAKE MATA!!!!!!"
            mcname "LAGI JALAN SANTAI-SANTAI MALAH DITABRAK."
            hide pia_shy
            show pia_angry at pia_near with dissolve
            show pia_side_angry at left with dissolve
            pia "EH, AKU JUGA DAH MINTA MAAF LOH,"
            pia "KOK MALAH NGEGAS?"
            stop music fadeout 1.0
            $ renpy.block_rollback()
            $ quick_menu = False
            scene black with dissolve
            show text "{color=#FFF}KALIAN BERDUA MALAH BERANTEM TERUS DI LIATIN \nDAN BAHKAN DIREKAM ORANG-ORANG.{/color}" with Pause(2.0)
            show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
            scene black with dissolve
            play music "audio/Dreamcatcher.mp3" fadein 1.0
            jump credits    
        "Nasehatin":
            scene depan kampus with dissolve
            show pia_shy at pia_near with dissolve
            $ renpy.block_rollback()
            $ quick_menu = True
            mcname "Iya gapapa, kok."
            mcname "Tapi lain kali ga usah lari-lari, ya."
            mcname "Kalau kata Mamahku tuh-"
            show pia_side_shy at left with dissolve
            pia "Eeh aku lagi buru-buru duh,"
            pia "Nanti aja ya nasehatinnya."
            hide pia_side_shy with dissolve
            "[mcname] pun menahan tangan perempuan itu agar tidak lari dari tempat tersebut."
            mcname "Ehh kalau ada orang yang lagi nasehatin tuh dengerin dulu."
            mcname "Dilihat lihat nih anak muda jaman sekarang ga mau dengerin nasehat dari orang tua."
            mcname "Mamahku tuh banyak banget nasehat-nasehat yang baik."
            mcname "Dengerin dulu."
            mcname "Jadi-"
            $ quick_menu = False
            stop music fadeout 1.0
            scene black with dissolve
            show text "{color=#FFF}[mcname] MALAH NGOMONG NASEHAT DAN MALAH BIKIN PEREMPUAN ITU TERLAMBAT \nDAN LU PUN DILIAT ANEH SAMA ORANG-ORANG.{/color}" with Pause(2.0)
            show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
            scene black with dissolve
            play music "audio/Dreamcatcher.mp3" fadein 1.0
            jump credits
        "Maafin":
            $ renpy.block_rollback()
            $ quick_menu = True
            mcname "Ah gak papa kok,"
            mcname "Hehe"
            mcname "Maaf juga, aku ngelamun di tengah jalan."
            $ quick_menu = False
            scene pia tabrakan ngomong with dissolve
            $ quick_menu = True
            pia "Hehe, oke. Maaf, byeeee"
            $ quick_menu = False
            scene depan kampus with dissolve
            jump chapter1piacarajalan

label chapter1piacarajalan:
    $ renpy.block_rollback()
    $ quick_menu = True
    mcname "Ah! Aku juga harus buru-buru daftar ulang!!"
    $ quick_menu = False
    menu:
        "Cara jalanmu kesana"
        "Lari terburu buru":
            $ renpy.block_rollback()
            $ quick_menu = True
            mcname "{i}EH, udah jam segini!!?? Oke gw lariii.{/i}"
            "[mcname] pun memilih untuk lari karena terburu-buru… akan tetapi dia tidak melihat adanya lampu lalu lintas dan akhirnya ketabrak truk"
            stop music fadeout 1.0
            $ quick_menu = False
            scene black with dissolve
            show text "{color=#FFF}ADUHHHH BROOO BURU-BURU SIH... BURU-BURU TAPI GA USAH LARI BANGET JUGA KALI{/color}" with Pause(2.0)
            show text "{color=#FFF}AKHIRNYA GA LIAT LAMPU MERAH TERUS KETABRAK KAN?!!{/color}" with Pause(2.0)
            show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
            scene black with dissolve
            play music "audio/Dreamcatcher.mp3" fadein 1.0
            jump credits
        "Jalan Cepat":
            $ renpy.block_rollback()
            $ quick_menu = True
            "[mcname] memilih untuk berjalan cepat dan mengabaikan semua orang yang ada. Katanya sih, jalan cepat juga ada di olimpiade. Jadi harusnya efektif."
            $ quick_menu = False
            jump chapter1piajalancepat
        "Jalan Biasa":
            $ renpy.block_rollback()
            $ quick_menu = True
            mcname "Eh jalan biasa aja deh, yang penting sampai."
            mcname "Kita harus santai."
            mcname "Kalau kata Mamah,"
            mcname "{i}Alon-alon sing penting kelakon.{/i}"
            "[mcname] pun memilih untuk jalan biasa dan dia melihat orang sedang kesusahan."
            $ quick_menu = False
            menu:
                "Respon kamu..."
                "Bantu":
                    $ renpy.block_rollback()
                    $ quick_menu = True
                    mcname "Eh sini aku bantuin."
                    "Orang" "Makasih ya ka, udah mau bantuin."
                    "Orang" "Eh kakak kan, kakak kandung ku yang udah lama ilang ya?"
                    mcname "HA!!?? Bukan aku bukan kakakmu!"
                    mcname "Aku cuma orang lewat."
                    "Orang" "Mana adaaaa."
                    "Orang" "Nih liat ini foto kita waktu dulu"
                    "[mcname] pun melihat ke arah pergelangan orang itu dan ia melihat ada gelang yang menunjukan bahwa orang itu merupakan pasien RSJ."
                    $ quick_menu = False
                    stop music fadeout 1.0
                    scene black with dissolve
                    show text "{color=#FFF}WADUH NIAT BAIK TAPI MALAH ZONK,{/color}" with Pause(2.0)
                    show text "{color=#FFF}SEKARANG LU MALAH KEJEBAK SAMA ORANG ODGJ.{/color}" with Pause(2.0)
                    play music "audio/BGM_Kampus.mp3" fadein 1.0
                    scene depan kampus with dissolve
                    jump chapter1piacarajalan
                "Diemin":
                    $ renpy.block_rollback()
                    $ quick_menu = True
                    "Setelah [mcname] melihat orang tersebut, [mcname] memilih untuk mengabaikan orang tersebut dan berjalan kembali."
                    "Akan tetapi, entah kenapa dia diikuti oleh orang tersebut."
                    "Ternyata mereka saling bertatap pandang dan orang itu mengira bahwa [mcname] adalah keluarganya"
                    $ quick_menu = False
                    scene black with dissolve
                    show text "{color=#FFF}WADUH DI KEJAR GA TUH IIII TAKUTNYEEE.{/color}" with Pause(2.0)
                    play music "audio/BGM_Kampus.mp3" fadein 1.0
                    scene depan kampus with dissolve
                    jump chapter1piacarajalan

label chapter1piajalancepat:
    $ quick_menu = False
    scene black with dissolve
    scene depan kampus with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname] pun selesai registrasi daftar ulang ke jurusan DKV."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with dissolve
    show text "{color=#FFF}1 MINGGU KEMUDIAN{/color}" with Pause(2.0)
    scene awan with dissolve
    play music "audio/BGM_Kampus.mp3" fadein 1.0
    $ renpy.block_rollback()
    $ quick_menu = True
    "Walaupun ini sudah pertengahan tahun, namun Matahari secara terik menerangi Jakarta dan saat melihat ke atas langit, hanya langit biru lah yang terlihat."
    $ quick_menu = False
    scene depan kampus with Dissolve(2.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    mcname "{i}Untung aja masih sempat untuk ikut orientasi, gak nyangka di Jakarta ternyata beneran macet parah.{/i}"
    mcname "{i}Yah walaupun begitu, ini memang pengalaman baru yang aku rasakan, berbeda jauh dari tempatku dulu{/i}"
    mcname "{i}Huuuu, ini hari pertamaku orientasi di Jeketi University. Di sini tempat di mana aku bakalan kenal sama orang baru, temen baru, atau bahkan jodoh heheh{/i}"
    $ quick_menu = False
    scene black with dissolve
    play sound "audio/open_door.mp3" fadein 1.0
    show text "{color=#FFF}MEMASUKI AULA{/color}" with Pause(2.0)
    stop music fadeout 1.0
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    scene kelas with Dissolve(2.0)
    play sound "audio/crowd_noise.mp3" fadein 1.0
    $ renpy.block_rollback()
    $ quick_menu = True
    "Saat memasuki ruangan, [mcname] mendengar suara di aula yang sangat ramai."
    mcname "{i}Seperti yang diharapkan dari kampus Ibu Kota, orangnya rame banget.{/i}"
    "Terlihat di dalam aula sudah diisi dengan mahasiswa baru."
    mcname "{i}Well, kayaknya aku harus mencari tempat duduk yang kosong sebelum penuh.{i}"
    "[mcname] melihat tempat duduk yang berada di pojok atas ruangan."
    mcname "{i}Ah sepertinya itu tidak ada orang.{/i}"
    "[mcname] pun berjalan menuju tempat tersebut."
    "Saat sampai di sana, tidak terlihat orang di barisan tersebut."
    mcname "Hmmm... tumben di bagian belakang kosong, padahal biasanya orang pada seneng di belakang."
    "[mcname] kemudian duduk di kursi tersebut."
    mcname "Tapi lumayan juga dapat duduk di sini, jadinya bisa ngeliat yang lain dengan jelas."
    $ quick_menu = False
    stop sound fadeout 1.0
    stop music fadeout 1.0
    scene black with dissolve
    play sound "audio/open_door.mp3" fadein 1.0
    scene kelas with dissolve
    play music "audio/BGM_Dosen + Rektor.mp3" fadein 1.0
    $ renpy.block_rollback()
    $ quick_menu = True
    "Dekan DKV" "Baik, sekian pengenalan singkat kita. Selamat datang di Jeketi University para Mahasiswa dan Mahasiswi baru! Raihlah mimpi kalian disini!! Selamat berjuang! Setelah ini, kalian dipersilahkan untuk pulang."
    $ quick_menu = False
    scene black with dissolve
    stop music fadeout 1.0
    scene kelas with dissolve
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    $ renpy.block_rollback()
    $ quick_menu = True
    mcname "Hueeeee.... capek juga duduk doang dengerin orang ngomong. Besok mulai masuk kuliah, gak sabar bakal ketemu orang-orang baru."
    show pia at char_center with dissolve
    show pia_side at left with dissolve
    pia "HEEEEEEEEEEEE!! KAMUUUUUUU?!!"
    hide pia_side with dissolve
    mcname "Buset, siapa itu teriak-teriak."
    hide pia with dissolve
    mcname "{i}Loh kok, kayaknya nyamperin aku?{/i}"
    show pia at pia_near with dissolve
    show pia_side at left with dissolve
    pia "HEYYYYYYY!!! INGET AKU GAKKK??!!!"
    hide pia_side with dissolve
    mcname "Iya aku inget. Tapi bisa gak tereak, gak?"
    mcname "Malu diliatin banyak orang gini."
    show pia_side at left with dissolve
    pia "Oh iya, maap. Hehe..."
    pia "OH! INGET AKU?!"
    pia "KITA TABRAKAN DEPAN GERBANG MINGGU LALU! KIRAIN KAMU SENIOR!"
    pia "TERNYATA MABA JUGA KAYAK AKU, HAHAHAHA!!"
    hide pia_side with dissolve
    mcname "{i}Buset teriak lagi ini orang.{/i}"
    show pia_side at left with dissolve
    pia "Kamu DKV juga, ya! Gilak ternyata kita sejurusan"
    pia "Apakah jodoh?"
    pia "Candaaaaa, ahahaha."
    hide pia_side with dissolve
    mcname "Ahaha ahaha iya. Sejurusan ternyata ya kita."
    mcname "Oh iya, kita belom kenalan. Namaku [mcname]."
    show pia_side at left with dissolve
    pia "LAH IYA BELOM KENALAN."
    $ pia_name = "Pia Meraleo"
    pia "Halo, aku Pia Meraleo salam kenal."
    $ pia_name = "Pia"
    pia "Kamu panggil aku Pia aja."
    hide pia_side with dissolve
    mcname "{i}Wah kalo diliat dari dekat gini, Pia imut juga yah.{/i}"
    pia "[mcname], kok bengong? Makan bareng yuk. Pengen liat kantin kampusnya kayak gimana. Laper juga sih."
    mcname "Lah, lesgooo. Pas banget ini lagi laper."
    "[mcname] dan Pia berjalan ke kantin kampus untuk makan."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with dissolve
    scene kantin with dissolve
    play music "audio/BGM_kantin.mp3" fadein 1.0
    show pia at pia_near with dissolve
    show pia_side at left with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    pia "WEEEH GEDE JUGA KANTINNYA YA!!"
    hide pia_side with dissolve
    mcname "Selain kantin, suara kamu juga gede btw."
    show pia_side at left with dissolve
    pia "EH maap, kebiasaan ahahaha."
    hide pia_side with dissolve
    mcname "Gapapa kok. Seru juga kamu, gak abis-abis energinya."
    show pia_shy at pia_near with dissolve
    show pia_side_shy at left with dissolve
    pia "I-iya kah? Ahahaha."
    hide pia_shy with dissolve
    hide pia_side_shy with dissolve
    show pia_side at left with dissolve
    pia "Oh, mau makan di mana ini? Mejanya full semua."
    hide pia_side with dissolve
    hide pia with dissolve
    show pia at char_center with dissolve
    mcname "Iya, lagi. Eh tapi di pojokan itu ada meja isinya cuma sendiri. Numpang bareng aja ap--"
    show pia_side at left with dissolve
    pia "Halooo, sendiri? Boleh numpang duduk 1 meja di sini gak?"
    hide pia_side with dissolve
    mcname "Ah....... Pia...... Langsung banget."
    hide pia with dissolve
    show pia at pia_near_right with dissolve
    show fio at char_near_left with dissolve
    show fio_side at left with dissolve
    fio "Eh oh mmm. I-iya k-kosong kok. Duduk aja."
    "[mcname], Pia, dan perempuan itu duduk di 1 meja yang sama."
    hide fio_side with dissolve
    "Sambil makan..."
    show pia_side at left with dissolve
    pia "Jweerushan aphah kwamuh?\n(Jurusan apa kamu?)"
    hide pia_side with dissolve
    fio "Aku? Aku DKV."
    show pia_side at left with dissolve
    pia "EEEEEEH SWAAAMAAA!! KOK GWAK LIYAT KWAMU PAS PWENGENALAN?"
    hide pia_side with dissolve
    mcname "Telen dulu, Pia..........."
    mcname "{i}Tapi iya deh, aku gak liat Mbak ini kayaknya pas pengenalan.{/i}"
    show fio_side at left with dissolve
    fio "Oh kamu Maba ya? Aku udah semester 4. Ga mungkin ikut ke sana tadi."
    hide fio_side with dissolve
    show pia_side at left with dissolve
    pia "Eh kakak senior, maaf Kak. Kirain Maba juga."
    show pia_sad at pia_near_right with dissolve 
    hide pia_side with dissolve
    show pia_side_sad at left with dissolve
    pia "Maaf Kaaak."
    hide pia_side_sad with dissolve
    mcname "Eh maap, Kak. Pia emang kelakuannya nyablak."
    mcname "{i}Yup. pantes gak liat tadi.{/i}"
    $ fio_name = "Fiony"
    show fio_side at left with dissolve
    fio "Hahaha santai aja, lanjut makan. Kok jadi kaku kalian?? Kenalin, aku Fiony."
    hide fio_side with dissolve
    show pia_side_sad at left with dissolve
    pia "A-AKU PIA MEAMEO."
    hide pia_side_sad with dissolve
    mcname "Ppppfffftt Meameo, ahaha. Kenalin kak, aku [mcname]."
    show pia_angry at pia_near_right with dissolve
    show pia_side_angry at left with dissolve
    pia "Aaaaa kan jadi typo ngomongnya. Meraleo maksudnyaaaaa."
    hide pia_side_angry with dissolve
    "Mereka bertiga pun melanjutkan makan sembari ngobrol."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with dissolve
    show text "{color=#FFF}KEESOKAN HARINYA{/color}" with Pause(2.0)
    scene kelas with Dissolve(2.0)
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    show pia at pia_near with dissolve
    show pia_side at left with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    pia "Hueeeeeee [mcname], baru hari pertama tapi kayaknya udah berat gak sih pelajarannya?"
    hide pia_side with dissolve
    mcname "Engga sih, seru kok kayaknya. Cuma ya… ternyata banyak yang harus kita beli buat pertemuan selanjutnya, nih."
    show pia_side at left with dissolve
    pia "Eh! Iya weeeh! Bingung ini beli kemana… Mana kita berdua bukan asli Jakarta, gak tau tempat aku. Kamu tau tempat belinya?"
    hide pia_side with dissolve
    $ quick_menu = False
    menu:
        "Jawaban kamu..."
        "Aku tau, kebetulan sempet jalan jalan daerah sini pas lowong kemaren.":
            $ renpy.block_rollback()
            $ quick_menu = True
            mcname "Aku tau! Kebetulan sempet jalan-jalan daerah sini pas lowong kemaren."
            show pia_side at left with dissolve
            pia "Ah mantap! Beli di mana? Deket?"
            hide pia_side with dissolve
            mcname "Agak jauh sih tapi di sana lengkap. Mau beli bareng?"
            show pia_shy at pia_near with dissolve
            show pia_side_shy at left with dissolve
            pia "M-MAUUUUU!! AYOO."
            hide pia_side_shy with dissolve
            "[mcname] mengatur waktu dan pergi berduaan dengan Pia."
            $ quick_menu = False
            stop music fadeout 1.0
            jump chapter1piajalantanpapio
        "Gak tau, belom sempet muter-muter Jakarta. Tanya kak Fiony.":
            $ renpy.block_rollback()
            $ quick_menu = True
            mcname "Gak tau, belom sempet muter-muter Jakarta."
            show pia_side at left with dissolve
            pia "Waduh, gimana ini ya belinya? Hmmmm."
            hide pia_side with dissolve
            mcname "Eh bukannya kamu kemaren minta nomer Kak Fiony?"
            mcname "Kenapa gak hubungin dia buat nanya?"
            show pia_side at left with dissolve
            pia "LAH IYA JUGAAAA! OTW HUBUNGIN CEPIO."
            hide pia_side with dissolve
            mcname "Cepio?"
            show pia_side at left with dissolve
            pia "Loh aku udah bestie!! Aku manggil dia Cepio sekarang. Muahahahaha."
            stop music fadeout 1.0
            $ quick_menu = False
            jump chapter1piajalansamapiapio
        "Gak tau, tapi aku sama anak-anak cowok lain mau nyari bareng.":
            $ renpy.block_rollback()
            $ quick_menu = True
            mcname "Gak tau, tapi aku sama anak-anak cowok lain mau nyari bareng."
            show pia_side at left with dissolve
            pia "Yah, yaudah deh. Aku nyari sendiri aja kalo gitu."
            hide pia_side with dissolve
            mcname "Okeee. Nanti aku kabarin tempatnya di mana, biar kamu tau juga."
            show pia_side at left with dissolve
            pia "Oh oke, makasih"
            stop music fadeout 1.0
            $ quick_menu = False
            scene black with dissolve
            show text "{color=#FFF}[mcname] lupa ngabarin Pia tempatnya.{/color}" with Pause(2.0)
            show text "{color=#FFF}[mcname] jadi lebih seneng nongkrong sama anak-anak cowok dan mulai menjauh dari Pia.{/color}" with Pause(2.0)
            show text "{color=#FF0000}BAD END{/color}" with Pause(2.0)
            play music "audio/Dreamcatcher.mp3" fadein 1.0
            jump credits
    scene black with dissolve
    play music "audio/Dreamcatcher.mp3" fadein 1.0
    jump credits


label chapter1piajalantanpapio:
    scene black with dissolve
    scene mc bedroom with dissolve
    nvl clear
    play music "audio/BGM_Happy dan Handphone.mp3" fadein 1.0
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
    scene black with dissolve
    show text "{color=#FFF}KEESOKAN HARINYA{/color}" with Pause(2.0)
    nvl clear
    scene depan kosan with dissolve
    mc_nvl "Udah di depan kosan, yak."
    pia_nvl "TUNGGU!!!"
    $ renpy.block_rollback()
    $ quick_menu = True
    "Pia pun keluar dari kosan, siap untuk pergi dengan [mcname]."
    show pia at pia_near with dissolve
    show pia_side at left with dissolve
    pia "GAK TELAT, KAN? PAS KAN YA AKU SIAP SIAPNYA? JAM 10 UDAH READY."
    hide pia_side with dissolve
    mcname "Tetangga kosan kamu gak ada yang komplain ya, tiap hari ada yang teriak kayak kemalingan gini?"
    show pia_side at left with dissolve
    pia "HEH, SEMBARANGAN! HAHAHA."
    "[mcname] dan Pia pun berangkat bersama menuju lokasi tempat membeli peralatan DKV tersebut. Di Mall."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}SESAMPAINYA DI MALL{/color}" with Pause(2.0)
    scene mall temp with dissolve
    play music "audio/BGM_Mall Slow.mp3" fadein 1.0
    show pia at pia_near with dissolve
    show pia_side at left with dissolve
    $ quick_menu = True
    pia "Wah gede juga ya mallnya."
    hide pia_side with dissolve
    mcname "Sebelah situ Pia tempatnya."
    show pia_side at left with dissolve
    pia "Let's gooo!!!"
    hide pia_side with dissolve
    mcname "Gak usah lari, nanti ilang."
    show pia_angry at pia_near with dissolve
    show pia_side_angry at left with dissolve
    pia "Lu kata gue anak kecil, heh?!"
    hide pia_side_angry with dissolve
    mcname "Ahahahahaha"
    $ quick_menu = False
    scene black with dissolve
    play sound "audio/tabrakan.mp3"
    "*Orang random nabrak Pia*"
    scene mall temp with dissolve
    show pia_sad at pia_near with dissolve
    hide pia_angry
    show pia_side_sad at left with dissolve
    $ quick_menu = True
    pia "Maaf, Pak."
    hide pia_side_sad with dissolve
    "*Orang tersebut dengan tatapan sinis langsung pergi*"
    "[mcname] menggandeng tangan Pia."
    mcname "Udah gapapa, orangnya lagi buru-buru kali."
    show pia_shy at pia_near with dissolve
    hide pia_sad
    show pia_side_shy at left with dissolve
    pia "Ii-iya, maaci."
    hide pia_side_shy with dissolve
    "Kemudian Pia dan [mcname] menuju toko yang menjual peralatan menggambar tersebut sambil bergandengan tangan."
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}1 JAM KEMUDIAN{/color}" with Pause(2.0)
    scene mall temp with Dissolve(2.0)
    show pia at pia_near with dissolve
    show pia_side at left with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    pia "Weeeeeeh mahal juga ya jadinya, tadi sih murah pas liat satuan. Pensil 2, cat air 1, kuas, dan sebagainya.... Tapi pas dijumlah gak kerasa, tau-tau mahal juga."
    hide pia_side with dissolve
    mcname "Hahaha betuuuul."
    "*Tiba tiba dari belakang [mcname] ada yang berbisik*"
    "???" "{size=-5}Hayooo lagi ngapain berduaan?{/size}"
    mcname "HUAAAAA.."
    mcname "KAGET, KAK FIONY??!!!"
    hide pia with dissolve
    show pia at pia_near_right with dissolve
    show fio at char_near_left with dissolve
    show fio_side at left with dissolve
    fio "Haloooo~ Lagi ngapain nih kalian?"
    hide fio_side with dissolve
    mcname "Ini abis beli perlengkapan buat tugas nirmana, Kak."
    show fio_side at left with dissolve
    fio "*melirik Pia*\nKiw-kiw~"
    hide fio_side with dissolve
    show pia_shy at pia_near_right with dissolve
    show pia_side_shy at left with dissolve
    pia "CEPIOOOOOOOOOOO!!!!"
    hide pia_side_shy with dissolve
    show fio_side at left with dissolve
    fio "Hahahahahaha.\n*sambil peluk Pia*"
    hide fio_side with dissolve
    mcname "Sejak kapan kalian jadi akrab banget?"
    hide pia_shy with dissolve
    show pia_side at left with dissolve
    pia "Tau gak sih [mcname], ternyata rumah Cepio deket sama kosan aku!! Jadi kita banyak ngobrol gituuuu, ehehehe."
    hide pia_side with dissolve
    show fio_side at left with dissolve
    fio "Sama, lagi beli peralatan juga, udah banyak yang abis. Di sini juga tempat langganan aku."
    $ fio_name = "Cepio"
    fio "Btw, panggil Cepio aja."
    hide fio_side with dissolve
    mcname "Oke Cepioooo~"
    show pia_side at left with dissolve
    pia "Nah mumpung ada Cepio, Si Sepuh penunggu mall ini, mending rekomendasiin tempat makan enak di sini."
    hide pia_side with dissolve
    jump chapter1piamakanmall

label chapter1piajalansamapiapio:
    scene black with dissolve
    show text "{color=#FFF}KEESOKAN HARINYA{/color}" with Pause(2.0)
    scene mall temp with dissolve
    play music "audio/BGM_Mall Slow.mp3" fadein 1.0
    $ renpy.block_rollback()
    $ quick_menu = True
    mcname "{i}Janjiannya di depan toko #sponsor 1, tapi mana nih Pia sama Kak Fiony belum sampe.{/i}"
    mcname "{i}Udah setengah jam nunggu huhuhu.{/i}"
    show pia at pia_near_right with dissolve
    show fio at char_near_left with dissolve
    show pia_side at left with dissolve
    pia "[mcname]!!!!!!! HOIIII!!! MAAAP TELAAAAAT!!"
    show fio_side at left with dissolve
    hide pia_side with dissolve
    fio "Maap ya [mcname], tadi nungguin Pia. Dandan dulu lama banget, mana macet pula di jalan."
    hide fio_side with dissolve
    show pia_side at left with dissolve
    pia "Dih! Kok Cepio nyalahin aku??"
    hide pia_side with dissolve
    show fio_side at left with dissolve
    fio "Tapi kan emang dandannya lama tadi. Padahal cuma mau belanja cat, buku, dan sebagainya kan?"
    fio "Ngapain harus dandan banget yang banget-banget? Apa jangan-jangan kamu s--"
    hide fio_side with dissolve
    show pia_side at left with dissolve
    pia "Ssssssaaaaah. Dah dah, jadi kemana mana ini. Lesgow! Lead the waaaay, Cepio!!!!"
    hide pia_side with dissolve
    mcname "Sejak kapan kalian jadi akrab banget?"
    show pia_side at left with dissolve
    pia "Tau gak sih [mcname], ternyata rumah Cepio deket sama kosan aku!!"
    pia "Jadi kita banyak ngobrol gituuuu, ehehehe."
    hide pia_side with dissolve
    "Mereka pun berjalan sambil mengobrol panjang lebar."
    $ quick_menu = False
    scene black with dissolve
    scene mall temp with dissolve
    show pia at pia_near_right with dissolve
    show fio at char_near_left with dissolve
    show fio_side at left with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    fio "Di sini tempatnya. Tadaaaaaa~"
    hide fio_side with dissolve
    show pia_side at left with dissolve
    pia "WOAAAAA LENGKAP BANGET!!!"
    hide pia_side with dissolve
    mcname "Wah mantap, makasih Kak Fiony!"
    $ fio_name = "Cepio"
    show fio_side at left with dissolve
    fio "Cepio ajaaa. Panggil aku Cepio, hehe."
    hide fio_side with dissolve
    show pia_angry at pia_near_right with dissolve
    mcname "Ah oke, Cepio hehe."
    show pia_side_angry at left with dissolve
    pia "Hmmmmmm!!!\n*Bombastic side eyes*"
    hide pia_side_angry with dissolve
    show fio_side at left with dissolve
    fio "{size=-5}Cieee cemburu, hehehe.{/size}"
    hide fio_side with dissolve
    show pia_side_angry at left with dissolve
    pia "CEPIOOOOOOOO!!!!!!"
    hide pia_side_angry with dissolve
    mcname "????"
    "Fiony pun membantu merekomendasikan peralatan yang dibutuhkan [mcname] dan Pia."
    $ quick_menu = False
    scene black with dissolve
    scene mall temp with dissolve
    show pia at pia_near_right with dissolve
    show fio at char_near_left with dissolve
    show pia_side at left with dissolve
    $ quick_menu = True
    pia "Weeeeeeh mahal juga ya jadinya, tadi sih murah pas liat satuan."
    pia "Pensil 2, cat air 1, kuas, dan sebagainya."
    pia "Tapi pas dijumlah gak kerasa, tau-tau mahal juga."
    hide pia_side with dissolve
    show fio_side at left with dissolve
    fio "Welcome to DKV."
    "{size=-5}[mcname] & Pia{/size}" "Huhuuuu."
    hide fio_side with dissolve
    show pia_side at left with dissolve
    pia "BTW… MAU MAKAAAAAN!! Lapeerrr."
    hide pia_side with dissolve
    mcname "Setuju, laper."
    jump chapter1piamakanmall

label chapter1piamakanmall:
    show fio_side at left with dissolve
    fio "Ayo, aku ada tempat rekomendasi enak deket sini."
    hide fio_side with dissolve
    "{size=-5}[mcname] & Pia{/size}" "Lesgoooooo~"
    "Mereka bertiga pun menuju cafe tempat nongkrong Fiony dan mulai memesan makanan yang direkomendasikan Fiony."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play sound "audio/cafe-entrance.mp3" fadein 1.0
    show text "{color=#FFF}MEMASUKI CAFE{/color}" with Pause(2.0)
    scene cafe with dissolve
    play music "audio/BGM_Cafe Cerah.mp3" fadein 1.0
    show pia at pia_near_right with dissolve
    show fio at char_near_left with dissolve
    show pia_side at left with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    pia "Ummmmmmmm!!!!! Enaaaaak!!! Mantap lah, Cepio!\n*Sambil makan*"
    hide pia_side with dissolve
    show fio_side at left with dissolve
    fio "Hehehe enak, kan? Tempat langganan aku sama temen-temen aku nih. Enak, terus tempatnya cozy gitu buat foto-foto."
    hide fio_side with dissolve
    show pia_side at left with dissolve
    pia "Betuuuuul!!!"
    hide pia_side with dissolve
    "Dari meja yang cukup jauh dari tempat [mcname], Pia, dan Fiony duduk…"
    hide pia with dissolve
    hide fio with dissolve
    $ freya_name = "???"
    show freya at char_near_left with dissolve
    show kana at kana_near_right with dissolve
    show freya_side at left with dissolve
    freya "Lah, Fiony? Ngapain kamu di sini?"
    hide freya_side with dissolve
    show fio_side at left with dissolve
    fio "Lah Freya? Sama… mmmm..."
    $ freya_name = "Freya"
    hide fio_side with dissolve
    $ kana_name = "Kana"
    show kana_side at left with dissolve
    kana "Salam kenal, aku Kana."
    hide kana_side with dissolve
    show freya_side at left with dissolve
    freya "Sini."
    hide freya_side with dissolve
    show fio_side at left with dissolve
    fio "Okeh."
    hide freya with dissolve
    hide kana with dissolve
    show fio at char_near_left with dissolve
    show pia at pia_near_right with dissolve
    show fio_side at left with dissolve
    fio "Ges, aku ke sana dulu sebentar ya. Kalian berduaan aja dulu. Jangan macem-macem ya [mcname]. Hehehe."
    hide fio_side with dissolve
    show pia_shy at pia_near_right with dissolve
    show pia_side_shy at left with dissolve
    pia "CEPIOOOOOOOOOOOOO~"
    hide pia_side_shy with dissolve
    hide pia with dissolve
    hide fio with dissolve
    hide pia_shy with dissolve
    show pia_shy at pia_near with dissolve
    mcname "Ahahahahha."
    show pia_side_shy at left with dissolve
    pia "J-jadi… Abis berapa tadi belanja alat gambar?"
    hide pia_side_shy with dissolve
    mcname "400an lah, ahahaha. Kamu abis berapa?"
    show pia_side_shy at left with dissolve
    pia "Kurang lebih sama lah, huhuhu"
    hide pia_side_shy with dissolve
    "*hening*"
    mcname "Kalo berdua gini kayak ngedate gak sih kita?"
    hide pia_shy with dissolve
    show pia_nyembur with dissolve:
        zoom 0.3
        xalign 0.8
    show pia_side_shy at left with dissolve
    pia "UHUK-UHUK!!"
    pia "GIMANA??!!!"
    hide pia_side_shy with dissolve
    hide pia_nyembur with dissolve
    show pia_shy at pia_near with dissolve
    mcname "Ahahaha, engga. Bercanda kok."
    show pia_side_shy at left with dissolve
    pia "{size=-10}Ngedate beneran juga gapapa sih..{/size}"
    hide pia_side_shy with dissolve
    mcname "Apa, Pia? Sorry, gak kedengeran?"
    show pia_side_shy at left with dissolve
    pia "GAK KOK, minumannya enak. Aku haus, mau nambah kayaknya."
    hide pia_side_shy with dissolve
    mcname "Oh okeh, mau aku panggil pelayannya?"
    show pia_angry at pia_near with dissolve
    show pia_side_angry at left with dissolve
    pia "Gausah."
    hide pia_side_angry with dissolve
    mcname "Lah???"
    "*suasana hening*"
    show pia at pia_near with dissolve
    hide pia_angry 
    show pia_side at left with dissolve
    pia "Eh, tempatnya bagus gak sih buat foto-foto?"
    hide pia_side with dissolve
    mcname "Tadi Cepio sih ngomong gitu juga."
    show pia_side at left with dissolve
    pia "Selfie ah!!"
    # window auto hide
    play sound "audio/camera.mp3" loop
    hide pia_side with dissolve
    show pia_shy at pia_near with dissolve
    show pia_side_shy at left with dissolve
    stop sound 
    # window auto show
    pia "F-foto bareng sih kita. Udah jauh-jauh makan ke sini, masa ga difoto!"
    hide pia_side_shy with dissolve
    mcname "Hmm. Boleh deh.\n*bergaya*"
    show pia_side_shy at left with dissolve
    pia "Oke, satuu..dua....tigaaaa~"
    play sound "audio/camera.mp3"
    hide pia_side_shy with dissolve
    "Fiony ngeliatin dari jauh sambil senyum-senyum ngeledek nyindir Pia."
    show pia_angry at pia_near with dissolve
    show pia_side_angry at left with dissolve
    pia "CEPIOOOOOOOO!!"
    hide pia
    hide pia_shy
    hide pia_side_angry with dissolve
    hide pia_angry with dissolve
    show pia at pia_near_right with dissolve
    show fio at char_near_left with dissolve
    show fio_side at left with dissolve
    fio "Ahahaha udah makannya? Seru tuh foto fotonya. \n*sikut-sikut Pia*"
    hide fio_side with dissolve
    show pia_shy at pia_near_right with dissolve
    show pia_side_shy at left with dissolve
    pia "Ehehehehe~"
    hide pia_shy with dissolve
    hide pia_side_shy with dissolve
    show fio_side at left with dissolve
    fio "Kuy lah balik, takut kemaleman. Udah aku bayarin juga tadi makanannya ya."
    hide fio_side with dissolve
    mcname "Eh lah udah dibayar? Waduh aku transfer ke Cepio ya!"
    show fio_side at left with dissolve
    fio "Gausah. Ngeliat juniorku SENYUM-SENYUM sendiri udah cukup puas kok.\n*senyum ke Pia*"
    hide fio_side with dissolve
    show pia_shy at pia_near_right with dissolve
    show pia_side_shy at left with dissolve
    pia "Ih Cepio maaaaaaaah. Ngeledekin muluuuuu~"
    hide pia_side_shy with dissolve
    "Fiony berpisah dengan Pia dan [mcname]. Kemudian mereka pun pulang ke tempat tinggal masing-masing."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    scene mc bedroom with dissolve
    play music "audio/BGM_Kosan 2.mp3" fadein 1.0
    $ renpy.block_rollback()
    $ quick_menu = True
    mcname "Huaaaaa capeeeeek~\n*langsung rebahan di kasur*"
    mcname "Seru juga hari ini, hehehe."
    mcname "Yosshaaaa! Saatnya bersih-bersih terus rapihin peralatan yang dibeli tadi, terus tiduuur."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with dissolve
    show text "{color=#FFF}KEESOKAN HARINYA{/color}" with Pause(2.0)
    scene kelas with dissolve
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    $ renpy.block_rollback()
    $ quick_menu = True
    "Mata kuliah nirmana dimulai, [mcname] dan Pia pun menggunakan peralatan yang dibelinya kemarin."
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}3 JAM KEMUDIAN, SETELAH SELESAI SESI PERKULIAHAN{/color}" with Pause(2.0)
    scene kelas with dissolve
    show pia at pia_near with dissolve
    show pia_side at left with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    pia "[mcname]!!!!!! MUMET GUEH! AYO KELUAR. REFRESHING KE MANA KEK, MUTERIN KAMPUS."
    pia "SORE MASIH ADA KELAS LAGI, JADI GA BISA JAUH-JAUH."
    hide pia_side with dissolve
    mcname "Lesgo, sama. Pusing weh."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with dissolve
    scene lorong with dissolve
    play music "audio/BGM_Lorong.mp3" fadein 1.0
    $ renpy.block_rollback()
    $ quick_menu = True
    "Pia dan [mcname] pun berkeliling di kampus tanpa arah dan tujuan."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    scene sawah with dissolve
    # harusnya BGM Sawah
    play music "audio/BGM_Kampus.mp3" fadein 1.0
    $ renpy.block_rollback()
    $ quick_menu = True
    "Sampai akhirnya mereka masuk ke kawasan fakultas pertanian dan kehutanan."
    "Saat berjalan berdua..."
    # BGM STOP
    pia "Hmmm..hmmmmm\n*bergumam*"
    mcname "*berjalan di sebelah Pia sambil sesekali memejamkan mata menikmati suara Pia yang sedang humming*"
    # Harusnya ada humming migikata
    show pia at pia_near with dissolve
    mcname "Lagu apa Pia?"
    show pia_side at left with dissolve
    pia "Oh, ini judulnya Migikata."
    hide pia_side with dissolve
    mcname "Hmm, hummingmu bagus Pia. Merdu banget, hehe."
    show pia_shy at pia_near with dissolve
    show pia_side_shy at left with dissolve
    pia "A-apaan sih!"
    pia "Huft~"
    hide pia_shy with dissolve
    hide pia_side_shy with dissolve
    show pia_side at left with dissolve
    pia "Eh, ke situ yuk. Duduk bawah pohon."
    hide pia_side with dissolve
    mcname "Kuy!!"
    "[mcname] dan Pia pun duduk di bawah pohon rindang dekat pesawahan. Pia mengeluarkan HP dan earphone cablenya."
    show pia_side at left with dissolve
    pia "Mau denger lagu yang tadi aku nyanyiin nadanya? Nih."
    hide pia_side with dissolve
    play music "audio/migikata-off.mp3" fadein 1.0
    "Tiba-tiba..."
    # Harusnya ada acapella pia kalo gak ya bgm aja dah wkwkw
    pia "*Tiba tiba mulai bernyanyi lagu yang sedang didengarkan.*"
    mcname "{i}Woaaaa suara Pia bagus juga ternyata.{/i}"
    $ quick_menu = False
    scene black with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname] memejamkan mata menikmati alunan suara Pia yang sedang bernyanyi."
    $ quick_menu = False
    scene sawah with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    mcname "*Pia pun tanpa sadar menyenderkan kepalanya di pundak kanan [mcname]*"
    "Tak terasa, waktu pun sudah beranjak sore. [mcname] dan Pia kembali ke fakultasnya untuk memasuki kelas yang dimulai sore itu."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with dissolve
    show text "{color=#FFF}1 MINGGU KEMUDIAN{/color}" with Pause(2.0)
    jump chapter2piabegin


