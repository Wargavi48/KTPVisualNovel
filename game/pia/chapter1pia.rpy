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
            play music "audio/Dreamcatcher.mp3" fadein 1.0
            scene dream with dissolve
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
        "Maafin":
            mcname "Ah gak papa kok"
            mcname "Hehe"
            stop music fadeout 1.0
            scene black with dissolve
            scene dream with dissolve
            jump credits

