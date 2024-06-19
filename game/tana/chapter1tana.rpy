label chapter1tana:
    scene awan with dissolve
    "Walaupun ini sudah pertengahan tahun, namun Matahari secara terik menerangi Jakarta.Dan saat melihat ke atas langit, hanya langit biru lah yang terlihat. [mcname] mendatangi gedung kampus untuk melakukan daftar ulang."
    scene depan kampus with dissolve
    play music "audio/BGM_Kampus.mp3" fadein 1.0
    $ renpy.block_rollback()
    $ quick_menu = True
    mcname "Akhirnya sampe juga di kampus, gede banget ya, gedungnya juga tinggi - tinggi"
    "Pada saat ke kampus, [mcname] melihat seorang gadis sedang dikerumunin 2 cowok. Terlihat agak gelisah."
    scene awal tana with dissolve
    mcname "Eh ada apaan tuh ribut-ribut?"
    scene awal tana mc with dissolve
    "[mcname] pun mendatangi perempuan tersebut"
    mcname "Woy ngapain kalian?! Beraninya sama cewek, keroyokan pula, tch"
    tono "Lah lu ngapa kocaaak, orang kita lagi bercanda"
    "Cowok 1" "Yeuuu party pooper lu!"
    "Cowok 2" "Dah bubar bubar"
    $ quick_menu = False
    scene black with dissolve
    scene depan kampus with dissolve
    "2 cowok itu pun pergi"
    mcname "{i}Noooo baru ketemu orang di sini malah malu-maluin aaaaa{/i}"
    show tono at char_center with dissolve
    show tono_side at left with dissolve
    tono "Ah kocak, mereka temen-temen gua, gak berani macem-macem juga kok mereka"
    hide tono_side with dissolve
    mcname "Aduh, maaf ya kukira kerumunan jahat tadi"
    show tono_side at left with dissolve
    tono "Halah halah…"
    tono "Tapi makasih loh udah khawatir, gua duluan yak. Dadaaah"
    hide tono_side with dissolve
    mcname "Iya.. Maaf ya"
    mcname "{i}Malu banget huhu pengen pulang{/i}"
    $ quick_menu = False
    menu:
        "Respon kamu..."
        "Aaaa malu banget pulang ke kosan aja deh":
            mcname "Aaaa malu banget pulang ke kosan aja deh"
            stop music fadeout 1.0
            scene black with dissolve
            show text "{color=#FFF}Kamu ga jadi kuliah karena telat daftar ulang{/color}" with Pause(2.0)
            show text "{color=#FF0000}BAD END{/color}"
            play music "audio/Dreamcatcher.mp3" fadein 1.0
            jump credits
        "Cuek lah gak bakal ketemu lagi sama orang-orang tadi, lanjut daftar ulang":
            $ renpy.block_rollback()
            $ quick_menu = True
            mcname "Cuek lah gak bakal ketemu lagi sama orang-orang tadi, lanjut daftar ulang"
            mcname "Ok lanjut daftar ulang abis itu ke kelas perkenalan, semoga gak ada kejadian memalukan lagi. Wish me luck..."
            $ quick_menu = False
            jump tanamcdaftarulang
        "Ke kantin dulu deh cari es teh":
            mcname "Ke kantin dulu deh cari es teh"
            stop music fadeout 1.0
            scene black with dissolve
            show text "{color=#FFF}Kamu ga jadi kuliah karena telat daftar ulang{/color}" with Pause(2.0)
            show text "{color=#FF0000}BAD END{/color}"
            play music "audio/Dreamcatcher.mp3" fadein 1.0
            jump credits

label tanamcdaftarulang:
    scene black with dissolve
    show text "{color=#FFF}[mcname] PULANG KE KOSAN{/color}" with Pause(2.0)
    scene mc bedroom with dissolve
    play music "audio/BGM_Kosan 1.mp3" fadein 1.0
    $ renpy.block_rollback()
    $ quick_menu = True
    "Setelah melakukan daftar ulang, [mcname] pun pulang ke kosannya untuk beristirahat."
    mcname "Hadeeeh. Baru juga dateng… Malu banget."
    "[mcname] pun mengingat kembali kejadian di depan kampus pada siang hari itu."
    show tono at char_center with dissolve
    mcname "Aduh kok aku jadi kepikiran terus sama cewek itu, ya? Apakah karena malu?"
    mcname "Dah ah. Tidur dulu, besok hari pertama orientasi"
    hide tono with dissolve
    "[mcname] pun tertidur"
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with dissolve
    show text "{color=#FFF}KEESOKAN HARINYA{/color}" with Pause(2.0)
    show depan kampus with dissolve
    play music "audio/BGM_Kampus.mp3" fadein 1.0
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname] datang ke kampus untuk memulai orientasinya"
    "[mcname] pun berjalan ke kelas"
    mcname "Aduh deg deg an."
    mcname "Hari ini awalan perkuliahan di Jakarta."
    mcname "Semoga yang kayak kemarin gak terulang lagi."
    $ quick_menu = False
    scene black with dissolve
    play music "audio/open_door.mp3"
    show text "{color=#FFF}MEMASUKI RUANG KELAS{/color}" with Pause(2.0)
    scene kelas with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    "Ternyata pas duduk di kelas, Cewek yang [mcname] temui kemarin pun duduk juga di sebelah [mcname]."
    show tono at char_center with dissolve
    show tono_side at left with dissolve
    tono "Lah sekelas?"
    hide tono_side with dissolve
    mcname "Ah eh umm. Iya, hehe"
    mcname "{i}LAH sekelas sama cewek yang kemarin aduh tambah malu dah ini mah{/i}"
    show tono_side at left with dissolve
    tono "Eh lu lagi... Kita kemarin belum kenalan kan?"
    $ tono_name = "Tana"
    tono "Gua Tana. Nama lu siapa?"
    hide tono_side with dissolve
    mcname "Gua [mcname]"
    show tono_side at left with dissolve
    tono "Salam kenal nama gw [mcname]"
    tono "Kaku amat ngomong \"gua\"-nya, bukan dari Jakarta ya?"
    hide tono_side with dissolve
    mcname "Hehe iya anak rantau nih"
    show tono_side at left with dissolve
    tono "Eh sama dong, gua juga dari desa. Terus kenapa pilih jurusan Teknik Pertanian?"
    hide tono_side with dissolve
    mcname "Kata mamah biar bisa memakmurkan para petani di kampung"
    show tono_side at left with dissolve
    tono "Heee. Alasan gua pilih jurusan ini juga mirip-mirip sama lu"
    tono "Selain itu, ya karena gua dari kecil doyan main di sawah hehe"
    hide tono_side with dissolve
    stop music fadeout 1.0

    