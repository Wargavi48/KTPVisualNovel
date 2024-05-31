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
            scene black with dissolve
            scene depan kampus with dissolve
            $ renpy.block_rollback()
            "[mcname] pun selesai registrasi daftar ulang ke jurusan DKV."
            scene black with dissolve
            play music "audio/Dreamcatcher.mp3" fadein 1.0
            jump credits
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
