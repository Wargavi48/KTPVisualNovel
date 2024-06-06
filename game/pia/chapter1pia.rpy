define char_test = Transform(zoom=0.5,xalign=-2.0,yalign=-2.0)



label chapter1pia:
    $ renpy.block_rollback()
    $ quick_menu = False
    scene awan with dissolve
    scene depan kampus with Dissolve(2.0)
    "Pagi ini kubuka lembaran baru untuk melanjutkan pendidikanku ke jenjang selanjutnya. Aku mengambil jurusan DKV, hari ini merupakan hari dimana aku datang ke kampus."
    mcname "{i}Wah besar juga ya kampusnya{/i}"
    mcname "{i}Aku bakal kuliah disini nih{/i}"
    mcname "{i}Bakal ketemu orang-orang kayak gimana ya…{/i}"
    mcname "{i}Huehuehue, udah gak sabar aku–{/i}"
    scene black with dissolve
    play sound "audio/tabrakan.mp3"
    show text "{color=#FFF}BRUKKKKK{/color}" with Pause(2.0)
    scene depan kampus with dissolve
    show pia_shy at pia_near with dissolve
    show pia_side_shy at left with dissolve
    play music "audio/BGM_Kampus.mp3" fadein 1.0
    $ quick_menu = True
    pia "Eh maap, Kak. Ketabrak."
    pia "Gak apa-apa kan? Lagi buru-buru."
    pia "Maaf, ya."
    hide pia_side_shy with dissolve
    $ quick_menu = False
    menu:
        "Sikap Kamu"
        "Marahin":
            mcname "EH LAIN KALI LIAT-LIAT DONG"
            mcname "PAKE MATA!!!!!!"
            mcname "LAGI JALAN SANTAI SANTAI MALAH DITABRAK."
            hide pia_shy
            show pia_angry at pia_near with dissolve
            show pia_side_angry at left with dissolve
            pia "EH, AKU JUGA DAH MINTA MAAF LOH"
            pia "KOK MALAH NGEGAS?"
            stop music fadeout 1.0
            scene black with dissolve
            show text "{color=#FFF}KALIAN BERDUA MALAH BERANTEM TERUS DI LIATIN \nDAN BAHKAN DI REKAM ORANG ORANG{/color}" with Pause(2.0)
            show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
            scene black with dissolve
            play music "audio/Dreamcatcher.mp3" fadein 1.0
            jump credits    
        "Nasehatin":
            mcname "Iya gapapa, kok"
            mcname "Tapi lain kali ga usah lari-lari, ya."
            mcname "Kalau kata Mamahku tuh-"
            show pia_side_shy at left with dissolve
            pia "Eeh aku lagi buru-buru duh"
            pia "Nanti aja ya nasehatinnya."
            hide pia_side_shy with dissolve
            "[mcname] pun menahan tangan perempuan itu agar tidak lari dari tempat tersebut"
            mcname "Ehh kalau ada orang yang lagi nasehatin tuh dengerin dulu."
            mcname "Dilihat lihat nih anak muda jaman sekarang ga mau dengerin nasehat dari orang tua."
            mcname "Ibuku tuh banyak banget nasehat-nasehat yang baik."
            mcname "Dengerin dulu"
            mcname "Jadi-"
            stop music fadeout 1.0
            scene black with dissolve
            show text "{color=#FFF}[mcname] MALAH NGOMONG NASEHAT DAN MALAH BIKIN PEREMPUAN ITU TERLAMBAT \nDAN LU PUN DI LIAT ANEH SAMA ORANG - ORANG {/color}" with Pause(2.0)
            show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
            scene black with dissolve
            play music "audio/Dreamcatcher.mp3" fadein 1.0
            jump credits
        "Maafin":
            mcname "Ah gak papa kok"
            mcname "Hehe"
            mcname "Maaf juga, aku ngelamun di tengah jalan."
            show pia_side_shy at left with dissolve
            pia "Hehe, oke. Maaf, byeeee"
            hide pia_side_shy with dissolve
            hide pia_shy with dissolve
            jump chapter1piacarajalan
            stop music fadeout 1.0
            scene black with dissolve
            jump credits

label chapter1piacarajalan:
    $ quick_menu = False
    mcname "Ah! Aku juga harus buru-buru daftar ulang!!"
    menu:
        "Cara jalanmu kesana"
        "Lari terburu buru":
            $ renpy.block_rollback()
            $ quick_menu = True
            mcname "{i}EH, udah jam segini!!?? Oke gw lariii.{/i}"
            "[mcname] pun memilih untuk lari karena terburu-buru…akan tetapi dia tidak melihat adanya lampu lalu lintas dan akhirnya ke tabrak truk"
            stop music fadeout 1.0
            $ quick_menu = False
            scene black with dissolve
            show text "{color=#FFF}ADUHHHH BROOO BURU BURU SI BURU BURU TAPI GA USAH LARI BANGET JUGA KALI{/color}" with Pause(2.0)
            show text "{color=#FFF}AKHIRNYA GA LIAT LAMPU MERAH TERUS KENA TABRAK KAN{/color}" with Pause(2.0)
            show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
            scene black with dissolve
            play music "audio/Dreamcatcher.mp3" fadein 1.0
            jump credits
        "Jalan Cepat":
            "[mcname] memilih untuk berjalan cepat dan mengabaikan semua orang yang ada. Katanya sih, jalan cepat juga ada di olimpiade. Jadi harusnya efektif."
            $ quick_menu = False
            jump chapter1piajalancepat
        "Jalan Biasa":
            mcname "Eh jalan biasa aja deh, yang penting sampai."
            mcname "Kita harus santai"
            mcname "Kalau kata Mamah"
            mcname "{i}Alon alon sing penting kelakon.{/i}"
            "[mcname] pun memilih untuk jalan biasa dan dia melihat orang sedang kesusahan."
            menu:
                "Sikap Kamu"
                "Bantu":
                    mcname "Eh sini aku bantuiin."
                    "Orang" "Makasih ya ka, udah mau bantuin"
                    "Orang" "Eh kakak kan, kakak kandung ku yang udah lama ilang ya?"
                    mcname "HA!!?? Bukan aku bukan kakakmu"
                    mcname "Aku cuma orang lewat"
                    "Orang" "Mana adaaaa."
                    "Orang" "Nih liat ini foto kita waktu dulu"
                    "[mcname] pun melihat ke arah pergelangan orang itu dan ia melihat ada gelang yang menunjukan bahwa orang itu merupakan pasien RSJ."
                    stop music fadeout 1.0
                    scene black with dissolve
                    show text "{color=#FFF}WADUH NIAT BAIK TAPI MALAH ZONK{/color}" with Pause(2.0)
                    show text "{color=#FFF}SEKARANG LU MALAH KEJEBAK SAMA ORANG ODGJ{/color}" with Pause(2.0)
                    play music "audio/BGM_Kampus.mp3" fadein 1.0
                    scene depan kampus with dissolve
                    jump chapter1piacarajalan
                "Diemin":
                    "Setelah [mcname] melihat orang tersebut, [mcname] memilih untuk mengabaikan orang tersebut dan berjalan kembali."
                    "Akan tetapi, entah kenapa dia diikuti oleh orang tersebut."
                    "Ternyata mereka saling bertatap pandang dan orang itu mengira bahwa [mcname] adalah keluarganya"
                    scene black with dissolve
                    show text "{color=#FFF}WADUH DI KEJAR GA TUH IIII TAKUTNYEEE{/color}" with Pause(2.0)
                    play music "audio/BGM_Kampus.mp3" fadein 1.0
                    scene depan kampus with dissolve
                    jump chapter1piacarajalan

label chapter1piajalancepat:
    $ renpy.block_rollback()
    scene black with dissolve
    scene depan kampus with dissolve
    "[mcname] pun selesai registrasi daftar ulang ke jurusan DKV."
    scene black with dissolve
    show text "{color=#FFF}1 MINGGU KEMUDIAN{/color}" with Pause(2.0)
    scene awan with dissolve
    "Walaupun ini sudah pertengahan tahun, namun Matahari secara terik menerangi Jakarta Dan saat melihat ke atas langit, hanya langit biru lah yang terlihat"
    scene depan kampus with Dissolve(2.0)
    $ quick_menu = True
    mcname "{i}Untung saja masih sempat untuk ikut orientasi, gak nyangka di Jakarta ternyata beneran macet parah.{/i}"
    mcname "{i}Yah walaupun begitu, ini memang pengalaman baru yang aku rasakan, berbeda jauh dari tempatku dulu{/i}"
    mcname "{i} Huuuu, ini hari pertamaku orientasi di Jeketi University. Di sini tempat dimana aku bakalan kenal sama orang baru, temen baru, atau bahkan jodoh heheh{/i}"
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
    pia "HEEEEEEEEEEEE!! KAMUUUUUUU"
    hide pia_side with dissolve
    mcname "Buset, siapa itu teriak-teriak."
    hide pia with dissolve
    mcname "{i}Loh kok, kayaknya nyamperin aku?{/i}"
    show pia at pia_near with dissolve
    show pia_side at left with dissolve
    pia "HEYYYYYYY!!! INGET AKU GAKKK???"
    hide pia_side with dissolve
    mcname "Iya aku inget. Tapi bisa gak tereak, gak?"
    mcname "Malu diliatin banyak orang gini."
    show pia_side at left with dissolve
    pia "Oh iya, maap. Hehe..."
    pia "OH! INGET AKU?"
    pia "KITA TABRAKAN DEPAN GERBANG MINGGU LALU! KIRAIN KAMU SENIOR!"
    pia "TERNYATA MABA JUGA KAYAK AKU, HAHAHAHA."
    hide pia_side with dissolve
    mcname "{i}Buset teriak lagi ini orang{/i}"
    show pia_side at left with dissolve
    pia "Kamu DKV juga, ya! Gilak ternyata kita sejurusan"
    pia "Apakah jodoh?"
    pia "Candaaaaa, ahahaha"
    hide pia_side with dissolve
    mcname "Ahaha ahaha iya. Sejurusan ternyata ya, kita."
    mcname "Oh iya, kita belom kenalan. Namaku [mcname]"
    show pia_side at left with dissolve
    pia "LAH IYA BELOM KENALAN"
    $ pia_name = "Pia Meraleo"
    pia "Halo, aku Pia Meraleo salam kenal."
    $ pia_name = "Pia"
    pia "Kamu panggil aja aku Pia"
    hide pia_side with dissolve
    mcname "{i}Wah kalo diliat dari dekat gini, imut juga Pia yah{/i}"
    pia "[mcname], kok bengong? Makan bareng, yuk. Pengen liat kantin kampusnya kayak gimana. Laper juga sih."
    mcname "Lah, lesgooo. Pas banget ini lagi laper."
    "[mcname] dan Pia berjalan ke kantin kampus untuk makan"
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with dissolve
    scene kantin with dissolve
    play music "audio/BGM_kantin.mp3" fadein 1.0
    show pia at pia_near with dissolve
    show pia_side at left with dissolve
    $ quick_menu = True
    pia "WEEEH GEDE JUGA KANTINNYA YA!"
    hide pia_side with dissolve
    mcname "Selain kantin, suara kamu juga gede btw."
    show pia_side at left with dissolve
    pia "EH maap, kebiasaan ahahaha"
    hide pia_side with dissolve
    mcname "Gapapa kok. Seru juga kamu, gak abis-abis energinya."
    show pia_shy at pia_near with dissolve
    show pia_side_shy at left with dissolve
    pia "I-iya kah? Ahahaha"
    hide pia_shy with dissolve
    hide pia_side_shy with dissolve
    show pia_side at left with dissolve
    pia "Oh, mau makan dimana ini? Mejanya full semua."
    hide pia_side with dissolve
    hide pia with dissolve
    show pia at char_center with dissolve
    mcname "Iya, lagi. Eh tapi di pojokan itu ada meja isinya cuma sendiri. Numpang bareng aja ap--"
    show pia_side at left with dissolve
    pia "Halooo, sendiri? Boleh numpang duduk 1 meja disini, gak?"
    hide pia_side with dissolve
    mcname "Ah....... Pia...... Langsung banget."
    hide pia with dissolve
    show pia at pia_near_right with dissolve
    show fio at char_near_left with dissolve
    show fio_side at left with dissolve
    fio "Eh oh mmm. Iya k-kosong kok. Duduk aja."
    "[mcname], Pia, dan Perempuan itu duduk di 1 meja yang sama."
    hide fio_side with dissolve
    "Sambil makan"
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
    fio "Oh kamu MaBa, ya? Aku udah semester 4. Ga mungkin ikut kesana tadi."
    hide fio_side with dissolve
    show pia_side at left with dissolve
    pia "Eh kakak senior, maaf Kak. Kirain MaBa juga"
    show pia_sad at pia_near_right with dissolve 
    hide pia_side with dissolve
    show pia_side_sad at left with dissolve
    pia "Maaf Kaaak"
    hide pia_side_sad with dissolve
    mcname "Eh maap, Kak. Pia emang kelakuannya nyablak\n{i}Yup. pantes gak liat tadi{/i}"
    $ fio_name = "Fiony"
    show fio_side at left with dissolve
    fio "Hahaha santai aja, lanjut makan. Kok jadi kaku kalian. Kenalin aku, Fiony."
    hide fio_side with dissolve
    show pia_side_sad at left with dissolve
    pia "A-AKU PIA MEAMEO"
    hide pia_side_sad with dissolve
    mcname "Ppppfffftt Meameo, ahaha. Kenalin kak aku [mcname]"
    show pia_angry at pia_near_right with dissolve
    show pia_side_angry at left with dissolve
    pia "Aaaaa kan jadi typo, ngomongnya. Meraleo maksudnyaaaaa."
    hide pia_side_angry with dissolve
    "Mereka bertiga pun melanjutkan makan sembari ngobrol."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with dissolve
    show text "{color=#FFF}Keesokan Harinya{/color}" with Pause(2.0)
    scene kelas with Dissolve(2.0)
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    show pia at pia_near with dissolve
    show pia_side at left with dissolve
    pia "Hueeeeeee MC, baru hari pertama. Kayaknya udah berat gak sih, pelajarannya?"
    hide pia_side with dissolve
    mcname "Engga sih, seru kok kayaknya. Cuma ya… ternyata banyak yang harus kita beli nih buat pertemuan selanjutnya"
    show pia_side at left with dissolve
    pia "Eh! Iya weeeh! Bingung ini beli kemana… Mana kita berdua bukan asli Jakarta, gatau tempat aku. Kamu tau tempat belinya?"
    hide pia_side with dissolve
    $ quick_menu = False
    menu:
        "Jawaban Kamu"
        "Aku tau, kebetulan sempet jalan jalan daerah sini pas lowong kemaren":
            $ renpy.block_rollback()
            $ quick_menu = True
            mcname "Aku tau! Kebetulan sempet jalan-jalan daerah sini pas lowong kemaren."
            show pia_side at left with dissolve
            pia "Ah mantap! Beli di mana? Deket?"
            hide pia_side with dissolve
            mcname "Agak jauh sih tapi di sana lengkap. Mau beli bareng?"
            show pia_shy at pia_near with dissolve
            show pia_side_shy at left with dissolve
            pia "M-MAUUUUU!! AYOO"
            hide pia_side_shy with dissolve
            "[mcname] mengatur waktu dan pergi berduaan dengan Pia"
            $ quick_menu = False
            stop music fadeout 1.0
            jump chapter1piajalantanpapio
        "Gak tau, belom sempet muter muter jakarta. Tanya kak Fiony":
            $ renpy.block_rollback()
            $ quick_menu = True
            mcname "Gak tau, belom sempet muter-muter Jakarta."
            show pia_side at left with dissolve
            pia "Waduh, gimana ini ya belinya? Hmmmm."
            hide pia_side with dissolve
            mcname "Eh bukannya kamu kemaren minta nomer Kak Fiony?"
            mcname "Kenapa gak hubungin dia buat nanya?"
            show pia_side at left with dissolve
            pia "LAH IYA JUGAAAA! OTW HUBUNGIN CEPIO"
            hide pia_side with dissolve
            mcname "Cepio?"
            show pia_side at left with dissolve
            pia "Loh aku udah bestie!! Aku manggil dia Cepio sekarang. Muahahahaha."
            stop music fadeout 1.0
            $ quick_menu = False
            jump chapter1piajalansamapiapio
        "Gak tau, tapi aku sama anak anak cowok lain mau nyari bareng":
            $ renpy.block_rollback()
            $ quick_menu = True
            mcname "Gak tau, tapi aku sama anak-anak cowok lain mau nyari bareng."
            show pia_side at left with dissolve
            pia "Yah, yaudah deh. Aku nyari sendiri aja kalo gitu"
            hide pia_side with dissolve
            mcname "Okeee. Nanti aku kabarin tempatnya dimana, biar kamu tau juga."
            show pia_side at left with dissolve
            pia "Oh oke, makasih"
            stop music fadeout 1.0
            $ quick_menu = False
            scene black with dissolve
            show text "{color=#FFF}[mcname] lupa ngabarin Pia tempatnya{/color}" with Pause(2.0)
            show text "{color=#FFF}[mcname] jadi lebih seneng nongkrong sama anak-anak cowok dan mulai menjauh dari Pia.{/color}" with Pause(2.0)
            show text "{color=#FF0000}BAD END{/color}" with Pause(2.0)
            play music "audio/Dreamcatcher.mp3" fadein 1.0
            jump credits
    scene black with dissolve
    play music "audio/Dreamcatcher.mp3" fadein 1.0
    jump credits


label chapter1piajalantanpapio:
    scene black with dissolve
    "Scene Jalan Tanpa Pio"
    play music "audio/Dreamcatcher.mp3" fadein 1.0
    jump credits

label chapter1piajalansamapiapio:
    scene black with dissolve
    scene mall temp with dissolve
    play music "audio/BGM_Mall Slow.mp3" fadein 1.0
    $ renpy.block_rollback()
    $ quick_menu = True
    mcname "{i}Janjiannya di depan toko #sponsor 1, tapi mana nih Pia sama Kak Fiony belum sampe{/i}"
    mcname "{i}Udah setengah jam nunggu huhuhu{/i}"
    show pia at pia_near_right with dissolve
    show fio at char_near_left with dissolve
    show pia_side at left with dissolve
    pia "[mcname]!!!!!!! HOIIII!!! MAAAP TELAAAAAT"
    show fio_side at left with dissolve
    hide pia_side with dissolve
    fio "Maap ya [mcname], tadi nungguin Pia. Dandan dulu lama banget, mana macet pula di jalan"
    hide fio_side with dissolve
    show pia_side at left with dissolve
    pia "Dih! Kok Cepio nyalahin aku!!!!"
    hide pia_side with dissolve
    show fio_side at left with dissolve
    fio "Tapi kan emang dandannya lama tadi. Padahal cuma mau belanja cat, buku, dan sebagainya kan? Ngapain harus dandan banget yang banget banget? Apa jangan-jangan kamu s--"
    hide fio_side with dissolve
    show pia_side at left with dissolve
    pia "Ssssssaaaaah. Dah dah, jadi kemana mana ini. Lesgow! Lead the waaaay, Cepio!!!!"
    hide pia_side with dissolve
    mcname "Sejak kapan kalian jadi akrab banget?"
    show pia_side at left with dissolve
    pia "Tau gak sih [mcname], ternyata rumah Cepio deket sama aku!!"
    pia "Jadi kita banyak ngobrol gituuuu, ehehehe"
    hide pia_side with dissolve
    "Mereka pun berjalan sambil mengobrol panjang lebar"
    $ quick_menu = False
    scene black with dissolve
    scene mall temp with dissolve
    show pia at pia_near_right with dissolve
    show fio at char_near_left with dissolve
    show fio_side at left with dissolve
    $ quick_menu = True
    fio "Di sini tempatnya. Tadaaaaaa."
    hide fio_side with dissolve
    show pia_side at left with dissolve
    pia "WOAAAAA LENGKAP BANGET!!!"
    hide pia_side with dissolve
    mcname "Wah mantap, makasih kak Fiony!"
    $ fio_name = "Cepio"
    show fio_side at left with dissolve
    fio "Cepio ajaaa. Panggil aku Cepio, hehe."
    hide fio_side with dissolve
    show pia_angry at pia_near_right with dissolve
    mcname "Ah oke, Cepio hehe"
    show pia_side_angry at left with dissolve
    pia "Hmmmmmm!!!"
    hide pia_side_angry with dissolve
    show fio_side at left with dissolve
    fio "{size=-5}Cieee cemburu, hehehe{/size}"
    hide fio_side with dissolve
    show pia_side_angry at left with dissolve
    pia "CEPIOOOOOOOO!!!!!!"
    hide pia_side_angry with dissolve
    mcname "????"
    "Fiony pun membantu merekomendasikan peralatan yang dibutuhkan [mcname] dan Pia"
    $ quick_menu = False
    scene black with dissolve
    scene mall temp with dissolve
    show pia at pia_near_right with dissolve
    show fio at char_near_left with dissolve
    show pia_side at left with dissolve
    pia "Weeeeeeh mahal juga ya jadinya, tadi sih murah pas liat satuan. Pensil 2, cat air 1, kuas, dan sebagainya. Tapi pas dijumlah gak kerasa, tau-tau mahal juga"
    hide pia_side with dissolve
    show fio_side at left with dissolve
    fio "Welcome to DKV"
    "{size=-5}[mcname] & Pia{/size}" "Huhuuuu"
    show pia_side at left with dissolve
    pia "btw… MAU MAKAAAAAN. LAPEEEEEER"
    hide pia_side with dissolve
    mcname "Setuju, laper."
    jump credits