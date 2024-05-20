label phoneChat:
    $ renpy.block_rollback()
    scene bedroom with dissolve

    freya_nvl "{size=-5}Eh, guys{/size}"
    freya_nvl "{size=-5}Buat tema, udah fix kan jadinya?{/size}"
    freya_nvl "{size=-5}Mau yang udah kita tentuin sebelumnya?{/size}"
    kana_nvl "{size=-5}Kalau dari aku sih, setuju ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧{/size}"
    mcname "{i}Hm…? Lucu juga emote yang dipake Kana ini{/i}"
    freya_nvl "{size=-5}Kita mau kerja kelompok kapan, nih?{/size}"
    freya_nvl "{size=-5}Ini kan buat minggu depan.{/size}"
    freya_nvl "{size=-5}Jadi, kita punya waktu kurang lebih 5 harian.{/size}"
    kana_nvl "{size=-5}Kita harus nentuin kapan jadwal kita kosong.{/size}"
    kana_nvl "{size=-5}Kayaknya, lusa kita kosong nih.{/size}"
    kana_nvl "{size=-5}Gimana yang lain?(ㅅ´ ˘ `){/size}"


    menu:
        "Hari Lusa":
            mc_nvl "{size=-5}Kalau lusa, aku sih kosong juga{/size}"
            mc_nvl "{size=-5}Siapa tau bisa sekalian jalan-jalan keliling Kota Jakarta, hehe.{/size}"
            mc_nvl "{size=-5}Maklum wong ndeso{/size}"
            kana_nvl "{size=-5}Eh boleh tuh (˶ᵔ ᵕ ᵔ˶){/size}"
            freya_nvl "{size=-5}Boleh sihh. Tapi pada bisa, kan?{/size}"
            freya_nvl "{size=-5}Ga ada yang tiba-tiba ga bisa atau ada kegiatan, kan !?{/size}"
            donatur_nvl "{size=-5}Santai aja Mba? Galak banget sih, pasti bisa kok gw haha{/size}"
            mc_nvl "{size=-5}Iya. Aku kemungkinan bisa, kok{/size}"
            kana_nvl "{size=-5}Iya nih, santai aja dong Freya.{/size}"
            kana_nvl "{size=-5}Aku takuttt (｡•́︿•̀｡){/size}"
            donatur_nvl "{size=-5}Nah liat, si [kana_name] aja jadi takut{/size}"
            freya_nvl "{size=-5}Apa sih, Kana. Biasa aja kali. Jangan playing victim gitu. #KanaAkunJahat{/size}"
            kana_nvl "{size=-5}Apa sih Freya. Kan kamu yang akun jahat (¬_¬\") #FreyaAkunJahat{/size}"
            mc_nvl "{size=-5}Ehh, udah ah. Jadi makin berlarut gini. Intinya pada bisa, kan?{/size}"
            freya_nvl "{size=-5}Iya aku bisa…{/size}"
            kana_nvl "{size=-5}Aku juga{/size}"
            donatur_nvl "{size=-5}Boleh, gw sih ngikut aja.{/size}"
            scene bedroom with Dissolve(2.0)
            "Obrolan mereka tidak terasa sudah lama."
            " Malam pun menjadi semakin larut."
            "[mcname] pun terlelap."
            jump chapter1kana3
        "Ga bisa kerja kelompok":
            mc_nvl "{size=-5}Eh sorry. Aku ga bisa ikut kerja kelompok, kayaknya{/size}"
            mc_nvl "{size=-5}Soalnya jadwal penuh sama part-timeku yang bakal dimulai besok{/size}"
            mc_nvl "{size=-5}Nanti aku kerjain yang lain, gmn?{/size}"
            scene black with Dissolve(2.0)
            show text "{color=#FFF}BROOO YNG BENER AJA, BARU PERTAMA KALI KERJA KELOMPOK UDAH GINI !??{/color}" with Pause(2.0)
            show text "{color=#FFF}AKHIRNYA LO PUN DI JAUHIN SAMA TEMEN-TEMEN KELOMPOK{/color}" with Pause (2.0)
            show text "{color=#FF0000}BAD END{/color}" with Pause (2.0)
            play music "audio/Dreamcatcher.mp3"
            jump credits
        "Ga bisa kerja kelompok":
            scene black with Dissolve(2.0)
            show text "{color=#FFF}EH LO MASIH MABA, BUKANYA SOSIALISASI, MALAH MENYENDIRI{/color}" with Pause(2.0)
            show text "{color=#FFF}SADAR DIRI, NGACA SANA{/color}" with Pause (2.0)
            show text "{color=#FFF}ATAU LO MAU JADI MAHASISWA KUPU-KUPU{/color}" with Pause (2.0)
            show text "{color=#FFF} ATAU HIKIKOMORI !??{/color}" with Pause (2.0)
            show text "{color=#FF0000}BAD END{/color}" with Pause (2.0)
            play music "audio/Dreamcatcher.mp3"
            jump credits

    play music "audio/Dreamcatcher.mp3"
    jump credits