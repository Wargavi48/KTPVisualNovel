label phoneChat:
    $ renpy.block_rollback()
    scene bedroom with dissolve

    freya_nvl "Eh, guys"
    freya_nvl "Buat tema, udah fix kan jadinya?"
    freya_nvl "Mau yang udah kita tentuin sebelumnya?"
    kana_nvl "Kalau dari aku sih, setuju ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧"
    mcname "{i}Hm…? Lucu juga emote yang dipake Kana ini{/i}"
    freya_nvl "Kita mau kerja kelompok kapan, nih?"
    freya_nvl "Ini kan buat minggu depan."
    freya_nvl "Jadi, kita punya waktu kurang lebih 5 harian."
    kana_nvl "Kita harus nentuin kapan jadwal kita kosong."
    kana_nvl "Kayaknya, lusa kita kosong nih."
    kana_nvl "Gimana yang lain?(ㅅ´ ˘ `)"


    menu:
        "Hari Lusa":
            mc_nvl "Kalau lusa, aku sih kosong juga"
            mc_nvl "Siapa tau bisa sekalian jalan-jalan keliling Kota Jakarta, hehe."
            mc_nvl "Maklum wong ndeso"
            kana_nvl "Eh boleh tuh (˶ᵔ ᵕ ᵔ˶)"
            freya_nvl "Boleh sihh. Tapi pada bisa, kan?"
            freya_nvl "Ga ada yang tiba-tiba ga bisa atau ada kegiatan, kan !?"
            donatur_nvl "Santai aja Mba? Galak banget sih, pasti bisa kok gw haha"
            mc_nvl "Iya. Aku kemungkinan bisa, kok"
            kana_nvl "Iya nih, santai aja dong Freya."
            kana_nvl "Aku takuttt (｡•́︿•̀｡)"
            donatur_nvl "Nah liat, si [kana_name] aja jadi takut"
            freya_nvl "Apa sih, Kana. Biasa aja kali. Jangan playing victim gitu. #KanaAkunJahat"
            kana_nvl "Apa sih Freya. Kan kamu yang akun jahat (¬_¬\") #FreyaAkunJahat"
            mc_nvl "Ehh, udah ah. Jadi makin berlarut gini. Intinya pada bisa, kan?"
            freya_nvl "Iya aku bisa…"
            kana_nvl "Aku juga"
            donatur_nvl "Boleh, gw sih ngikut aja."
            jump chapter1kana3
        "Test choice 2":
            mc_nvl "Eh sorry. Aku ga bisa ikut kerja kelompok, kayaknya"
            mc_nvl "Soalnya jadwal penuh sama part-timeku yang bakal dimulai besok"
            mc_nvl "Nanti aku kerjain yang lain, gmn?"
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