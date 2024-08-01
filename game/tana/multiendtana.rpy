label multiendlearnUTS:
    menu:
        "[mcname!c] mengajak Tana belajar di..."
        "Cafe":
            #IF CHOOSE A ( GO TO TRUE ENDING ROUTE 2)
            jump chapter2tanaTRUE2
        "Ruang Klub":
            #IF CHOSE B (GO TO GOOD ENDING ROUTE 2)
            jump chapter2tanaGOOD2
        "Warteg":
            "[mcname!c]" "Gimana kalau di warteg aja Tan? lagi pengen menghemat gue hehehe, biasa akhir bulan anak kost."
            hide tana
            show tana_talk at tana_near
            show tana_side_talk at left
            with dissolve
            tana "Alah, ya udah deh gue mah ngikut ajah dah gimana lu."
            hide tana_side_talk
            hide tana_talk
            show tana at tana_near
            with dissolve
            "[mcname!c]" "Mantappp."
            #SKIP TO SCENE
            #BG WARTEG
            #Gak ada BG Warteg
            stop music fadeout 1.0
            $ quick_menu = False
            scene black with Dissolve(1.0)
            play sound "audio/cafe-entrance.mp3" fadein 1.0
            play music "audio/BGM_Cafe Sore.ogg" fadein 1.0
            scene cafe sore with Dissolve(1.0)
            $ renpy.block_rollback()
            show tana at tana_near with dissolve
            pause(1.0)
            hide tana
            show tana_shock at tana_near
            show tana_side_shock at left
            with dissolve
            $ quick_menu = True
            tana "[mcname!c], lu yakin kita mau belajar disini?"
            hide tana_side_shock
            hide tana_shock
            show tana at tana_near
            "[mcname!c]" "Iya gue juga kadang belajar di sini."
            hide tana
            show tana_talk at tana_near
            show tana_side_talk at left
            with dissolve
            tana "Oalah pantesan..."
            hide tana_side_talk
            hide tana_talk
            show tana_angry at tana_near
            with dissolve
            "[mcname!c]" "Kenapa Tan?"
            hide tana_angry
            show tana_angry_2 at tana_near
            show tana_side_angry_2 at left
            with dissolve
            tana "Gimana mau fokus, orang rame gini terus berisik juga. Dah ah gue mau balik aja."
            hide tana_side_angry_2
            hide tana_angry_2
            with dissolve
            $ quick_menu = False
            stop music fadeout 1.0
            scene black with dissolve
            play music "BGM_Bad End.ogg"
            show text "{color=#FFF}*Tana pun meninggalkan [mcname!c] sendirian di warteg dan tidak dapat dihubungi lagi.*{/color}" with Pause(3.0)
            scene black with dissolve
            show text "{color=#FF0000}BAD END{/color}" with Pause(2.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits
        "Kampus":
            "[mcname!c]" "Di kampus aja gimana? biar wifinya kenceng gitu, searching apa-apa jadi gampang."
            hide tana
            show tana_talk at tana_near
            show tana_side_talk at left
            with dissolve
            tana "Ide bagus okee, nanti kita ketemuan di kampus."
            hide tana_side_talk
            hide tana_talk
            show tana at tana_near
            with dissolve
            #SKIP TO SCENE
            #BG KAMPUS SORE
            stop music fadeout 1.0
            $ quick_menu = False
            scene black with Dissolve(1.0)
            play music "audio/BGM_Sore.ogg" fadein 1.0
            scene kampus sore with Dissolve(2.0)
            show tana_talk at tana_near
            show tana_side_talk at left
            with dissolve
            $ quick_menu = True
            tana "[mcname!c], jadi kita mau belajar dari mana?"
            hide tana_side_talk
            hide tana_talk
            show tana at tana_near
            with dissolve
            "[mcname!c]" "bentar Tan tanggung ini lagi download film-film dulu biasa, buat stock di kosan, wifi kosan gw jelek sih..."
            hide tana
            show tana_talk at tana_near
            show tana_side_talk at left
            with dissolve
            tana "Ya udah cepetan."
            hide tana_side_talk
            hide tana_talk
            show tana at tana_near
            with dissolve
            "[mcname!c]" "Okee ini udah lagi download. Jadi kita mau belajar dari soal tahun lalu aja gimana Tan? Kebetulan gue dapet soal-soal dari kating gitu..."
            hide tana
            show tana_talk at tana_near
            show tana_side_talk at left
            with dissolve
            tana "Nahhh ide bagus tuh! mana coba gue liat."
            hide tana_side_talk
            hide tana_talk
            show tana at tana_near
            with dissolve
            "[mcname!c]" "Ini bentar ada di laptop."
            "[mcname!c]" "Lah lah LAHHHHHH"
            hide tana
            show tana_shock at tana_near
            show tana_side_shock at left
            with dissolve
            tana "Lu napa kocak teriak-teriak gitu!"
            hide tana_side_shock
            hide tana_shock
            show tana at tana_near
            with dissolve
            "[mcname!c]" "Laptop gue nge heng Tan… padhal tadi ga apa-apa."
            hide tana
            show tana_angry_2 at tana_near
            show tana_side_angry_2 at left
            with dissolve
            tana "Lu sih kebanyakan download film dari situs bajakan, makanya jadi kena virus kan. Rasaiin! Dah ah gue mau belajar sama yang lain aja."
            hide tana_side_talk
            hide tana_talk
            with dissolve
            "Tana pun pergi dari kampus, karena laptop [mcname!c] lama dan ga nyala-nyala"
            $ quick_menu = False
            stop music fadeout 1.0
            scene black with dissolve
            play music "BGM_Bad End.ogg"
            show text "{color=#FFF}*YAHAHHA, MAKANYA BROK, JANGAN DOWNLOAD/NONTON FILM DARI SITUS BAJAKAN KAN SEKARANG MALAH GINI*{/color}" with Pause(4.0)
            scene black with dissolve
            show text "{color=#FF0000}BAD END{/color}" with Pause(2.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits

label multiendafterUTS:
    menu:
        "Tempat mana yang akan kamu pilih?"
        "Rooftop":
            #IF CHOOSE A TRUE ENDING
            jump chapter2tanaTRUE3
        "Ruang Klub":
            #IF CHOOSE B GOOD ENDING
            jump chapter2tanaGOOD3
        "Nunggu di Kantin":
            "[mcname!c]" "Gimana kalau kita nunggu aja? Kayaknya ini orang-orang dah mau selesai sih, biar ga jauh-jauh gitu. Males jalan gue..."
            hide tana
            show tana_talk at tana_near
            show tana_side_talk at left
            with dissolve
            tana "Ya udah gue ngikut."
            hide tana_side_talk
            hide tana_talk
            show tana at tana_near
            with dissolve
            "[mcname!c] dan Tana pun menunggu. Untuk mendapatkan bangku kosong, untuk bisa menyantap makanan mereka, mereka terus menunggu, menunggu, dan menunggu. Hingga beberapa menit bahkan hingga 1 jam lamanya..."
            hide tana
            show tana_shock at tana_near
            show tana_side_shock at left
            with dissolve
            tana "Kok lama banget sih ini! ga ada yang kosong napa, mie gue lama-lama dingin gini ga enak."
            hide tana_side_shock
            hide tana_shock
            show tana_angry at tana_near
            with dissolve
            "[mcname!c]" "Iya ya, ko lama ya?"
            hide tana_angry
            show tana_shock at tana_near
            show tana_side_shock at left
            with dissolve
            tana "Ah udah lah gw duluan aja mau beli mie pedes lagi, gw ga suka makan mie pedes dingin."
            "Tana pun meninggalkan [mcname!c] sendirian."
            hide tana_side_shock
            hide tana_shock
            with dissolve
            stop sound fadeout 1.0
            stop music fadeout 1.0
            $ quick_menu = False
            scene black with dissolve
            play music "BGM_Bad End.ogg"
            show text "{color=#FFF}*MAKANYA BROO KALAU MAU NYARI TEMPAT MAKAN TUH LIAT SITUASI DAN KONDISI*{/color}" with Pause(3.0)
            scene black with dissolve
            show text "{color=#FF0000}BAD END{/color}" with Pause(2.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits
        "Di Bawah Pohon":
            "[mcname!c]" "Gimana kalau di bawah pohon aja? Kan rindang tuh enak keknya kalau kita makan sambil neduh."
            hide tana
            show tana_laugh at tana_near
            show tana_side_laugh at left
            with dissolve
            tana "Boleh tuh ide bagus! Oke gass~"
            hide tana_side_laugh
            hide tana_laugh
            show tana at tana_near
            with dissolve
            "[mcname!c]" "Okee yuk."
            "[mcname!c] dan Tana pun pergi mencari pohon yang cukup besar dan rindang untuk memakan mie pedas mereka."
            "[mcname!c]" "Nahhh gimana kalau di sini Tan?"
            hide tana
            show tana_talk at tana_near
            show tana_side_talk at left
            with dissolve
            tana "Bagus juga pilihan lu. Ya udah yuk, gue ga suka kalau mie gue dingin..."
            hide tana_side_talk
            hide tana_talk
            show tana at tana_near
            with dissolve
            "Mereka pun memakan mie pedas mereka."
            "Akan tetapi, di saat mereka makan mie mereka, [mcname!c] dan Tana terdiam beberapa saat karena ada sesuatu yang berjatuhan dari pohon."
            hide tana
            show tana_confused at tana_near
            show tana_side_confused at left
            with dissolve
            tana "[mcname!c]…"
            hide tana_side_confused
            hide tana_confused
            show tana_silent at tana_near
            with dissolve
            "[mcname!c]" "Tan…"
            hide tana_silent
            show tana_shock at tana_near
            show tana_side_shock at left
            with dissolve
            tana "INI BANYAK ULET NYA KOCAKKK PADA JATUHAN!!!"
            hide tana_side_shock
            hide tana_shock
            show tana_angry at tana_near
            with dissolve
            "[mcname!c]" "DI GUE JUGA SAMA KOCAK!!!"
            hide tana_angry
            show tana_shock at tana_near
            show tana_side_shock at left
            with dissolve
            tana "Sumpah untung ga kemakan, ayo lah pergi!"
            tana "AAAA mana mie gue baru di makan sedikit, elu sih!"
            hide tana_side_shock
            hide tana_shock
            show tana_angry at tana_near
            with dissolve
            "[mcname!c]" "Ya maaf, gue juga ga tau bakalan kaya gini..."
            stop sound fadeout 1.0
            stop music fadeout 1.0
            $ quick_menu = False
            scene black with dissolve
            play music "BGM_Bad End.ogg"
            show text "{color=#FFF}*YAHAHAH KASIAN LAGI MAKAN MALAH ADA ULET, MAKAN AJA KALI KAN PROTEIN TAMBAHAN HAHAH*{/color}" with Pause(4.0)
            scene black with dissolve
            show text "{color=#FF0000}BAD END{/color}" with Pause(2.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits