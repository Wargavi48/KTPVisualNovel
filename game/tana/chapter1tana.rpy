define tana_route = ""


label chapter1tana:
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene chapter 1 tana with Dissolve (1.0)
    pause(3.0)
    scene black with Dissolve (1.0)
    play music "audio/BGM_Pagi Siang.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Walaupun ini sudah pertengahan tahun, namun matahari secara terik menerangi Jakarta. Saat melihat ke atas langit, hanya langit biru lah yang terlihat."
    $ quick_menu = False
    scene depan kampus with Dissolve(2.0)
    # #$ renpy.block_rollback()
    $ quick_menu = True
    "[mcname!c] mendatangi gedung kampus untuk melakukan daftar ulang."
    "[mcname!c]" "Akhirnya sampe juga di kampus. Gede banget ya, gedungnya juga tinggi-tinggi."
    "Pada saat ke kampus, [mcname!c] melihat seorang gadis sedang dikerumunin 2 cowok. Terlihat agak gelisah."
    stop music fadeout 1.0
    $ quick_menu = False
    play music "BGM_Bad End.ogg" fadein 1.0
    scene awal tana with Dissolve(1.0)
    $ quick_menu = True
    "[mcname!c]" "Eh ada apaan tuh ribut-ribut?"
    $ quick_menu = False
    scene awal tana mc with Dissolve(1.0)
    $ quick_menu = True
    "[mcname!c] pun mendatangi perempuan tersebut."
    "[mcname!c]" "Woy ngapain kalian?! Beraninya sama cewek, keroyokan pula, tch."
    stop music fadeout 1.0
    show tana_date_side_talk at left with dissolve
    play music "BGM_Funny 3.ogg" fadein 1.0
    tana "Lah lu ngapa kocaaak, orang kita lagi bercanda."
    hide tana_date_side_talk at left with dissolve
    "Cowok 1" "Yeuuu party pooper lu!"
    "Cowok 2" "Dah bubar bubar."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene depan kampus with Dissolve(1.0)
    $ quick_menu = True
    "2 cowok itu pun pergi."
    "[mcname!c]" "{i}Noooo baru ketemu orang di sini malah malu-maluin aaaaa~{/i}"
    show tana_date_talk at tana_near
    show tana_date_side_talk at left
    with dissolve
    tana "Ah kocak, mereka temen-temen gua, gak berani macem-macem juga kok mereka."
    hide tana_side_talk at left
    hide tana_date_side_talk at tana_near
    show tana_date at tana_near
    with dissolve
    "[mcname!c]" "Aduh, maaf ya kukira kerumunan jahat tadi."
    hide tana_date at tana_near
    show tana_date_talk at tana_near
    show tana_date_side_talk at left
    with dissolve
    tana "Halah halah…"
    tana "Tapi makasih loh udah khawatir, gua duluan yak. Dadaaah~"
    hide tana_date_side_talk at left
    hide tana_date_talk at tana_near
    show tana_date at tana_near
    with dissolve
    "[mcname!c]" "Iya.. Maaf ya."
    hide tana_date at tana_near with dissolve
    "[mcname!c]" "{i}Malu banget huhu pengen pulang.{/i}"
    menu:
        "Yang kamu lakukan sekarang..."
        "Aaaa malu banget pulang ke kosan aja deh":
            stop music fadeout 1.0
            $ quick_menu = False
            play music "BGM_Bad End.ogg" fadein 1.0
            "[mcname!c]" "Aaaa malu banget pulang ke kosan aja deh."
            scene black with dissolve
            show text "{color=#FFF}Kamu ga jadi kuliah karena telat daftar ulang{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FF0000}BAD END{/color}" with Pause(2.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits
        "Cuek lah gak bakal ketemu lagi sama orang-orang tadi, lanjut daftar ulang":
            # #$ renpy.block_rollback()
            $ quick_menu = False
            stop music fadeout 1.0
            scene black with Dissolve(1.0)
            play music "BGM_Kampus.ogg" fadein 1.0
            scene depan kampus with Dissolve(1.0)
            $ quick_menu = True
            "[mcname!c]" "Cuek lah gak bakal ketemu lagi sama orang-orang tadi, lanjut daftar ulang."
            "[mcname!c]" "Semoga gak ada kejadian memalukan lagi, wish me luck..."
            "Setelah melakukan daftar ulang, [mcname!c] pun pulang ke kosannya untuk beristirahat."
            $ quick_menu = False
            jump tanamcdaftarulang
        "Ke kantin dulu deh cari es teh":
            stop music fadeout 1.0
            $ quick_menu = False
            play music "BGM_Bad End.ogg" fadein 1.0
            "[mcname!c]" "Ke kantin dulu deh cari es teh."
            scene black with dissolve
            show text "{color=#FFF}Kamu ga jadi kuliah karena telat daftar ulang{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FF0000}BAD END{/color}" with Pause(2.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits

label tanamcdaftarulang:
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" fadein 1.0
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Malamnya di kost..."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(2.0)
    $ quick_menu = True
    # #$ renpy.block_rollback()
    "[mcname!c]" "Hadeeeh. Baru juga dateng… Malu banget."
    "[mcname!c] pun mengingat kembali kejadian di depan kampus pada siang hari itu."
    show white:
        default
        subpixel True 
        parallel:
            Null(0.0, 0.0)
            'white' with dissolve
        parallel:
            ypos 0 alpha 1.0 
            linear 1.30 ypos 252 alpha 0.7 
    show white as white2:
        default
        subpixel True 
        parallel:
            Null(0.0, 0.0)
            'white' with dissolve
        parallel:
            ypos 2080 alpha 1.0 
            linear 1.30 ypos 1908 alpha 0.7 
    with Pause(1.40)
    show tana_date at tana_near with dissolve
    "[mcname!c]" "Aduh kok aku jadi kepikiran terus sama cewek itu, ya? Apakah karena malu?"
    hide white
    hide white2
    hide tana_date
    with Dissolve(1.0)
    "[mcname!c]" "Dah ah. Tidur dulu, besok hari pertama orientasi."
    hide tana at tana_near with dissolve
    "[mcname!c] pun tertidur."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kampus.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True    
    "Keesokan harinya..."
    $ quick_menu = False
    show depan kampus with Dissolve(2.0)
    # $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname!c] datang ke kampus untuk memulai orientasinya."
    "[mcname!c] pun berjalan ke kelas."
    "[mcname!c]" "{i}Aduh deg deg an.{/i}"
    "[mcname!c]" "{i}Hari ini awalan perkuliahan di Jakarta.{/i}"
    "[mcname!c]" "{i}Semoga yang kayak kemarin gak terulang lagi.{/i}"
    stop music fadeout 1.0
    $ quick_menu = False
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    scene black with Dissolve(1.0)
    play music "BGM_Kelas.ogg" fadein 1.0 volume (1.5)
    scene kelas with Dissolve(1.0)
    # $ renpy.block_rollback()
    $ quick_menu = True
    "Ternyata pas duduk di kelas, cewek yang [mcname!c] temui kemarin pun duduk juga di sebelah [mcname!c]."
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Lah sekelas?"
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Ah eh umm. Iya, hehe."
    "[mcname!c]" "{i}LAH sekelas sama cewek yang kemarin aduh tambah malu dah ini mah!{/i}"
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Eh... Kita kemarin belum kenalan kan?"
    $ tono_name = "Tana"
    tana "Gua Tana. Nama lu siapa?"
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Gua [mcname!c]."
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Kaku amat ngomong \"gua\"-nya, bukan dari Jakarta ya?"
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Hehe iya anak rantau nih."
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Eh sama dong, gua juga dari desa. Terus kenapa pilih jurusan Teknik Pertanian?"
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Kata mamah biar bisa memakmurkan para petani di kampung."
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Heee. Alasan gua pilih jurusan ini juga mirip-mirip sama lu."
    tana "Selain itu, ya karena gua dari kecil doyan main di sawah hehe~"
    hide tana_side_talk at left
    hide tana_talk at tana_near
    with dissolve
    "Tiba-tiba..."
    stop music fadeout 1.0
    $ quick_menu = False
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    scene black with Dissolve(1.0)
    play music "BGM_Dosen.ogg" fadein 1.0
    scene kelas with Dissolve(1.0)
    show dosen_talk at dosen_center
    show dosen_side_talk at left
    with dissolve
    # $ renpy.block_rollback()
    $ quick_menu = True
    dosen "Selamat datang Mahasiswa baru Jurusan pertanian."
    dosen "Oke, kegiatan hari ini adalah perkenalan lingkungan kampus. Silahkan berkumpul dengan kelompoknya masing-masing."
    dosen "Instruksi selanjutnya ada di pembimbing kelompok\nmasing-masing, terima kasih."
    dosen "HIDUP PERTANIAN INDONESIA!"
    hide dosen_side_talk at left
    hide dosen_talk at dosen_center
    with dissolve
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "BGM_Kelas.ogg" fadein 1.0 volume (1.5)
    scene kelas with Dissolve(1.0)
    show flora_talk at flora_center
    show flora_side_talk at left
    with dissolve
    # #$ renpy.block_rollback()
    $ quick_menu = True
    $ flora_name = "Flora"
    flora "Halo semuanya! Kenalin aku Flora, pembimbing kelompok ini."
    flora "Sekarang langsung baris aja terus kita keliling kampus ya!"
    hide flora_side_talk at left
    hide flora_talk at flora_center
    show flora at flora_center
    with dissolve
    "Mahasiswa" "Iya Kak!"
    hide flora at flora_center with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Lorong.ogg" fadein 1.0
    scene lorong with Dissolve(1.0)
    # $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname!c] dan kelompoknya pun berkeliling kampus untuk melihat fasilitas jurusan pertanian dibimbing oleh Kakak kelasnya yang bernama Flora. Tapi tiba tiba…"
    "[mcname!c]" "{i}Duh kebelet!{/i}"
    "[mcname!c]" "{i}Ke toilet dulu aman kali ya? Gak bakal ketinggalan kelompok.{/i}"
    "Dengan sedikit terburu buru, [mcname!c] bergegas ke toilet."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    pause(1.0)
    scene lorong with Dissolve(1.0)
    # #$ renpy.block_rollback()
    $ quick_menu = True
    "Setelah selesai, [mcname!c] pun keluar toilet dan melihat sekeliling."
    "[mcname!c]" "{i}Aduh pada ke mana ya? Kok udah sepi aja, mana gak tau jalan lagi.{/i}"
    "[mcname!c]" "{i}Eh itu ada Tana lagi sendirian.{/i}"
    "[mcname!c] melihat Tana yang tampaknya sedang kebingungan."
    "[mcname!c] pun menghampiri Tana."
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Hmmm? Eh, kok lu ada di sini?"
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Gua ketinggalan rombongan, tadi ke toilet dulu soalnya."
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Yeuuu kocak!"
    tana "Yaudah ayo ikutin gua, kita nyusul yang lain."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Emang lu udah hafal denah kampus ini ya?"
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Alah gampang itu mah~"
    tana "Kampus paling gitu-gitu aja tata letaknya."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Yaudah ngikut deh."
    hide tana at tana_near with dissolve
    "Karena tidak tau arah, [mcname!c] pun mengikuti Tana menyusuri kampus."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "1 jam kemudian..."
    $ quick_menu = False
    play music "audio/BGM_Funny 2.ogg" fadein 1.0
    scene lorong with Dissolve(2.0)
    show tana at tana_near with dissolve
    $ quick_menu = True
    "[mcname!c]" "Tan, perasaan dari tadi kita cuma muter-muter doang deh."
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Santai~ Bentar lagi juga ketemu sama kelompok kita."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Udah lama gini mereka harusnya udah beres gak sih?"
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Sabar, kocak! Masih siang kok ini."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Sebenernya lu tau kita di mana gak sih?"
    hide tana at tana_near
    show tana_confused at tana_near
    show tana_side_confused at left
    with dissolve
    tana "T-tau, kok. Udah, ayo lanjut jalan."
    hide tana_side_confused at left
    hide tana_confused at tana_near
    with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Beberapa saat kemudian..."
    $ quick_menu = False
    scene kantin with Dissolve(2.0)
    show tana_confused at tana_near with dissolve
    # #$ renpy.block_rollback()
    $ quick_menu = True
    "[mcname!c]" "Tan, ini bukannya kantin ya?"
    show tana_side_confused at left with dissolve
    tana "E-Emang iya?"
    hide tana_side_confused at left with dissolve
    "[mcname!c]" "Iya, kocak."
    show tana_side_confused at left with dissolve
    tana "Kok lu jadi ikut-ikutan ngomong kocak?"
    hide tana_side_confused at left with dissolve
    "[mcname!c]" "Ga usah ngalihin pembicaraan."
    "[mcname!c]" "Sebenernya lu tadi juga nyasar kan?"
    show tana_side_confused at left with dissolve
    tana "M-mana ada gua nyasar."
    hide tana_side_confused at left
    hide tana_confused at tana_near
    show tana_angry at tana_near
    with dissolve
    "[mcname!c]" "Kocak."
    hide tana_angry at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Lu kocak."
    hide tana_side_angry_2 at left 
    hide tana_angry_2 at tana_near
    show tana_angry at tana_near
    with dissolve
    "[mcname!c]" "Hahahaha."
    "[mcname!c]" "Ternyata kita sama-sama malu-maluin, ya."
    hide tana_angry at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Lu doang kali. Gua kagak."
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana_angry at tana_near
    with dissolve
    "[mcname!c]" "Yeuuu, kocak."
    hide tana_angry at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Gak cocok lu ngomong kocak-kocak begitu."
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana_angry at tana_near
    with dissolve
    "[mcname!c]" "Biarin, daripada gak mau ngaku nyasar."
    hide tana_angry at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Alaaaah. Iya iya gua juga nyasar."
    tana "Puas lu?"
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana_angry at tana_near
    with dissolve
    "[mcname!c]" "AHAHAHAHAHAHAHAHAH!"
    hide tana_angry at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Diem lu."
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana_angry at tana_near
    with dissolve
    "[mcname!c]" "Dih, ngamuk."
    hide tana_angry at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Berisik."
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana_angry at tana_near
    with dissolve
    "[mcname!c]" "Sekarang mau gimana?"
    hide tana_angry at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Ya lanjut jalan lah. Masa diem di sini."
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana_angry at tana_near
    with dissolve
    "[mcname!c]" "Yaudah. Balik ke tempat tadi aja."
    hide tana_angry at tana_near with dissolve
    "[mcname!c] dan Tana pun kembali menyusuri kampus."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "BGM_Sore.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Tak terasa langit menjadi sore..."
    $ quick_menu = False
    scene lorong sore with Dissolve(2.0)
    show flora_angry_talk at flora_center
    show flora_side_angry_talk at left
    with dissolve
    # #$ renpy.block_rollback()
    $ quick_menu = True
    flora "Duh. Ini dari tadi 2 orang ilang pada ke mana ya?"
    flora "Kelompoknya udah beres keliling kampus, mereka masih gak ketemu."
    flora "Udah sore lagi..."
    flora "Harusnya jam segini aku beresin ruangan klub, ini malah harus nyari 2 bocah."
    flora "Aaarrggghh."
    flora "Pasti Kak Feni udah nungguin aku."
    flora "Hmm?"
    flora "Eh itu dia mereka."
    flora "Hey, kalian dari mana aja sih?! Dari tadi dicariin, tapi malah berduaan di sini."
    hide flora_side_angry_talk at left
    hide flora_angry_talk at flora_center
    show flora_angry at flora_left
    show tana_confused at tana_right
    show tana_confused:
        xpos -0.41 zoom 1.25
    show tana_side_confused at left
    with dissolve
    tana "M-Maaf kak, hehe."
    tana "Kita berdua tadi ketinggalan rombongan."
    hide tana_side_confused at left
    hide tana_confused at tana_right
    show tana_angry_2 at tana_right
    show tana_angry_2:
        xpos -0.41 zoom 1.25
    show tana_side_angry_2 at left
    with dissolve
    tana "Lu sih malah ke toilet dulu tanpa izin ke Kak Flora."
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_right
    show tana_angry at tana_right
    show tana_angry:
        xpos -0.41 zoom 1.25
    with dissolve
    "[mcname!c]" "Lah? Lu kan malah udah kepisah duluan dari kelompok sebelum kita ketemu."
    hide tana_angry at tana_right
    hide flora_angry at tana_right
    show tana_confused at tana_right
    show tana_confused:
        xpos -0.41 zoom 1.25
    show flora_angry_talk at flora_left
    show flora_side_angry_talk at left
    with dissolve
    flora "Dieeeem!"
    flora "Kalian tuh udah ngerusak jadwal aku sore ini tau gak?"
    flora "Malah ribut sendiri."
    hide flora_side_angry_talk at left
    hide flora_angry_talk at flora_left
    show flora_angry at flora_left
    with dissolve
    "[mcname!c]" "Maaf, kak, tadi kita niatnya mau nyusul kelompok, tapi malah nyasar. Gara-gara Tana, nih."
    hide tana_confused at tana_right
    show tana_angry_2 at tana_right
    show tana_angry_2:
        xpos -0.41 zoom 1.25
    show tana_side_angry_2 at left
    with dissolve
    tana "Lah? Kok salah gua."
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_right
    show tana_angry at tana_right
    show tana_angry:
        xpos -0.41 zoom 1.25
    with dissolve
    "[mcname!c]" "Lu sih sotoy. Jadinya salah jalan kan."
    hide tana_angry at tana_right
    show tana at tana_right
    show tana:
        xpos -0.41 zoom 1.25
    hide flora_angry at flora_left
    show flora_angry_talk at flora_left
    show flora_side_angry_talk at left
    with dissolve
    flora "Malah saling nyalahin."
    flora "Aduh, harusnya sore ini itu aku beres-beres ruangan klub, tapi gak jadi gara-gara harus nyariin kalian."
    flora "Kasian banget Kak Feni tadi aku tinggal sendirian."
    hide flora_side_angry_talk at left
    hide tana at tana_right
    hide flora_angry_talk at flora_left
    show flora_angry at flora_left
    show tana_confused at tana_right
    show tana_confused:
        xpos -0.41 zoom 1.25
    show tana_side_confused at left
    with dissolve
    tana "Maaf ya, kak…"
    hide tana_side_confused at left
    hide tana_confused at tana_right
    show tana at tana_right
    show tana:
        xpos -0.41 zoom 1.25
    hide flora_angry at flora_left
    show flora_angry_talk at flora_left
    show flora_side_angry_talk at left
    with dissolve
    flora "Maaf doang nih?"
    hide flora_side_angry_talk at left
    hide flora_angry_talk at flora_left
    show flora_angry at flora_left
    with dissolve
    "[mcname!c]" "Gimana kalo kita bantuin Kak Flora beres-beres sebagai gantinya?"
    hide tana at tana_right
    show tana_talk at tana_right
    show tana_talk:
        xpos -0.41 zoom 1.25
    show tana_side_talk at left
    with dissolve
    tana "Iyaa kak, kita bantuin deh…"
    hide tana_side_talk at left
    hide tana_talk at tana_right
    hide flora at flora_left
    show tana at tana_right
    show tana:
        xpos -0.41 zoom 1.25
    show flora_talk at flora_left
    show flora_side_talk at left
    with dissolve
    flora "Nah, gitu dong. Yaudah ayo ikut sini."
    hide flora_angry
    hide flora_side_talk at left
    hide flora_talk at flora_left
    hide tana at tana_right
    with dissolve
    "[mcname!c], Tana, dan Flora pun pergi menuju ruang klub yang dimaksud oleh Flora."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene ruang ukm sore with Dissolve(1.0)
    show tana at tana_near
    show feni_talk at feni_right
    show flora at flora_left 
    show feni_side_talk at left
    with dissolve
    # # #$ renpy.block_rollback()
    $ quick_menu = True
    feni "Flo-chaaaaan dari mana aja kamu?"
    feni "Aku dari tadi beberes sendirian tauuu."
    hide feni_side_talk at left
    hide feni_talk at feni_right
    hide flora at flora_left
    show feni at feni_right
    show flora_talk at flora_left
    show flora_side_talk at left
    with dissolve
    $ feni_name = "Feni"
    flora "Kak Feni, maaaaaf, tadi aku jadi pembimbing kelompok, terus 2 orang ini malah nyasar gak balik-balik."
    flora "Jadinya aku nyari mereka dulu."
    hide flora_side_talk at left
    hide tana at tana_near
    hide flora_talk at flora_left
    hide feni at feni_right
    show feni at feni_right
    show flora at flora_left
    show tana_confused at tana_near
    show tana_side_confused at left
    with dissolve
    "{size=-5}[mcname!c] & Tana{/size}" "Maaf, kak..."
    hide tana_side_confused at left
    hide tana_confused at tana_near
    hide feni at feni_right
    show tana at tana_near
    show feni_talk at feni_right
    show feni_side_talk at left
    with dissolve
    feni "Terus kenapa kalian ikut Flora ke sini?"
    hide feni_side_talk at left
    hide feni_talk at feni_right
    hide flora at flora_left
    show feni at feni_right
    show flora_talk at flora_left
    show flora_side_talk at left
    with dissolve
    flora "Katanya sih mereka mau bantuin aku beres-beres, Kak."
    flora "Iya, kan? Hehe~"
    hide flora_side_talk at left
    hide tana at tana_near
    hide flora_talk at flora_left
    hide feni at feni_right
    show flora at flora_left
    show feni at feni_right
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    "{size=-5}[mcname!c] & Tana{/size}" "Iya kak."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    hide flora at flora_left
    hide feni at feni_right
    show flora at flora_left
    show tana at tana_near
    show feni_talk at feni_right
    show feni_side_talk at left
    with dissolve
    feni "Yaudah, sok atuh."
    feni "Aku istirahat duluan, ya!"
    feni "Capek euy~"
    feni "Dari tadi beberes sendirian."
    hide feni_side_talk at left
    hide tana at tana_near
    hide flora at flora_left
    hide feni_talk at feni_right
    show flora at flora_left
    show feni at feni_right
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    "[mcname!c] & Tana" "Iya kak, izin bantu beresin ruangan klubnya, ya"
    hide tana_side_talk at left
    hide tana_talk at tana_near
    hide flora at flora_left
    hide feni at feni_right
    with dissolve
    "[mcname!c] dan Tana pun mulai membereskan ruang klub sesuai dengan arahan Feni dan Flora."
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Kak, ini tuh ruang klub jejepangan ya?"
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show flora_talk at flora_center
    show flora_side_talk at left
    with dissolve
    flora "Iya. Namanya \"Koiken\"."
    hide flora_side_talk at left
    hide flora_talk at flora_center
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Kegiatannya ngapain aja?"
    hide tana_side_talk at left
    hide tana_talk at tana_near
    with dissolve
    "Flora pun menjelaskan apa saja kegiatan klub jejepangan itu."
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Ih, seru banget!"
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show flora_talk at flora_center
    show flora_side_talk at left
    with dissolve
    flora "Seru, kan?"
    flora "Ada yang mau ikut aku?"
    hide flora_side_talk at left
    hide flora_talk at flora_center
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Aku aku aku!"
    tana "[mcname!c], lu mau ikut klub jejepangan ini juga kan??"
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Ngapain gua ikut beginian?"
    hide tana at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Yaudah ikut aja kenapa sih? Temenin gua napa."
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Iya iya..."
    show feni_talk at feni_right
    show feni_side_talk at left
    with dissolve
    feni "[mcname!c], kamu jangan iya iya aja. Kamu beneran mau ikut atau nggak?"
    feni "Emang kamu tau soal jejepangan?"
    hide feni_side_talk at left
    hide feni_talk at feni_right
    show feni at feni_right
    show flora_talk at flora_left
    show flora_side_talk at left
    with dissolve
    flora "Nah. Coba kamu sebutin deh 5 anime yang kamu tau."
    flora "Gak boleh nyebut Narto, Two Piece, sama Pembasmi Iblis."
    hide flora_side_talk at left
    hide tana at tana_near
    hide flora_talk at flora_left
    hide feni at feni_right
    with dissolve
    menu:
        "Anime pilihan kamu:"
        "-Samurai Y\n-Pemburu x Pemburu\n-Mengubah sampah menjadi pohon\n-Pelaut bulan\n-Inisial F":
            show tana at tana_near
            show flora at flora_left
            show feni at feni_right
            with dissolve
            # $ renpy.block_rollback()
            $ quick_menu = True
            "[mcname!c]" "-Samurai Y\n-Pemburu x Pemburu\n-Mengubah sampah menjadi pohon\n-Pelaut bulan\n-Inisial F"
            show feni_side_talk at left with dissolve
            feni "Kamu gak naik kelas berapa kali kok tau anime-anime itu, tapi sekarang masih maba."
            hide feni_side_talk at left with dissolve
            "[mcname!c]" "Hehehe..."
        "-Cinta Palsu\n-Ekor Peri\n-Yo-Gi-Ah 3Ds\n-Adu Gasing\n-April Skem":
            show tana at tana_near
            show flora at flora_left
            show feni at feni_right
            with dissolve
            # $ renpy.block_rollback()
            $ quick_menu = True
            "[mcname!c]" "-Cinta Palsu\n-Ekor Peri\n-Yo-Gi-Ah 3Ds\n-Adu Gasing\n-April Skem"
            hide flora at flora_left
            show flora_talk at flora_left
            show flora_side_talk at left
            with dissolve
            flora "Boleh juga tontonanmu. Mirip-mirip lah ya."
            hide flora_side_talk at left
            hide flora_talk at flora_left
            show flora at flora_left
            with dissolve
            "[mcname!c]" "Iya dong. Bagus, kan?"
            hide flora at flora_left
        "-Bola Naga X\n-Seni Pedang Offline\n-Siapa namamu?\n-Akademi Pahlawan\n-Keluarga Mata-Mata":
            show tana at tana_near
            show flora at flora_left
            show feni at feni_right
            with dissolve
            # $ renpy.block_rollback()
            $ quick_menu = True
            "[mcname!c]" "-Bola Naga X\n-Seni Pedang Offline\n-Siapa namamu?\n-Akademi Pahlawan\n-Keluarga Mata-Mata"
            show flora_side_talk at left with dissolve
            flora "Kamu pasti wibu fomo, ya."
            hide flora_side_talk at left with dissolve
            "[mcname!c]" "Waduh."
    show flora_talk at flora_left
    show flora_side_talk at left
    with dissolve
    flora "Yaa, sudah terbukti tingkat kewibuannya."
    flora "Ikut klub sini aja udah."
    hide flora_side_talk at left
    hide flora_talk at flora_left
    show flora at flora_left
    with dissolve
    "[mcname!c]" "Iya iya..."
    hide feni at feni_right
    show feni_talk at feni_right
    show feni_side_talk at left
    with dissolve
    feni "Malah iya-iya lagi."
    hide feni_side_talk at left
    hide feni_talk at feni_right
    show feni at feni_right
    with dissolve
    "[mcname!c]" "Hai, sumimasen."
    hide tana at tana_near
    hide flora at flora_left
    hide feni at feni_right
    show tana_talk at tana_near
    show flora at flora_left
    show feni at feni_right
    show tana_side_talk at left
    with dissolve
    tana "Dasar wibu."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    hide flora at flora_left
    hide feni at feni_right
    show tana at tana_near
    show flora at flora_left
    show feni at feni_right
    with dissolve
    "[mcname!c]" "Ngaca sana."
    hide tana at tana_near
    hide flora at flora_left
    hide feni at feni_right
    show tana_talk at tana_near
    show flora at flora_left
    show feni at feni_right
    show tana_side_talk at left
    with dissolve
    tana "Hai, gomen gomen."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    hide flora at flora_left
    hide feni at feni_right
    show tana at tana_near
    show flora_talk at flora_left
    show feni at feni_right
    show flora_side_talk at left
    with dissolve
    flora "Gomen gomen, summernya mana?"
    hide flora_side_talk at left
    hide flora_talk at flora_left
    hide feni at feni_right
    show feni_talk at feni_right
    show flora at flora_left
    show feni_side_talk at left
    with dissolve
    feni "Gomenne summer~"
    hide feni_side_talk at left
    hide tana at tana_near
    hide feni_talk at feni_right
    hide flora at flora_left
    hide feni at feni_right
    with dissolve
    "Sore itu, ruang club pun dipenuhi gelak tawa dan canda ria. [mcname!c] dan Tana pun akhirnya bergabung dalam klub jejepangan bersama Feni dan Flora."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Beberapa jam kemudian..."
    $ quick_menu = False
    scene ruang ukm sore with Dissolve(2.0)
    show tana_talk at tana_near
    show flora at flora_left
    show feni at feni_right
    show tana_side_talk at left
    with dissolve
    $ quick_menu = True
    tana "Akkh, akhirnya kelar juga."
    tana "Asli capek banget!"
    hide tana_side_talk at left
    hide tana_talk at tana_near
    hide flora at flora_left
    hide feni at feni_right
    show tana_angry at tana_near
    show flora at flora_left
    show feni at feni_right
    with dissolve
    "[mcname!c]" "Ah kayak lu kerja aja."
    hide tana_angry at tana_near
    hide flora at flora_left
    hide feni at feni_right
    show tana_angry_2 at tana_near 
    show flora at flora_left
    show feni at feni_right
    show tana_side_angry_2 at left
    with dissolve
    tana "Ehh gua mah kerja. Gak kek lu."
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    hide flora at flora_left
    hide feni at feni_right
    show tana_angry at tana_near
    show flora at flora_left
    show feni at feni_right
    with dissolve
    "[mcname!c]" "Mang eak?"
    hide tana_angry at tana_near
    hide flora at flora_left
    hide feni at feni_right
    show tana_angry_2 at tana_near
    show flora at flora_left
    show feni at feni_right
    show tana_side_angry_2 at left
    with dissolve
    tana "Halah halah."
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    hide flora at flora_left
    hide feni at feni_right
    show tana at tana_near
    show flora_talk at flora_left
    show feni at feni_right
    show flora_side_talk at left
    with dissolve
    flora "Kalian capek? Bayangin kalo itu cuma aku sama Kak Feni yang beresin."
    hide flora_side_talk at left
    hide flora_talk at flora_left
    show flora at flora_left
    show feni_talk at feni_right
    show feni_side_talk at left
    with dissolve
    feni "Kejauhan bayanginnya. Bayangin dulu coba kalo aku sendirian yang beresin!"
    hide feni_side_talk at left
    hide tana at tana_near
    hide feni_talk at feni_right
    show feni at feni_right
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Semangat, kak."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    hide feni at feni_right
    show tana at tana_near
    show feni_talk at feni_right
    show feni_side_talk at left
    with dissolve
    feni "Dih. Malah ngeledekin nih anak."
    hide feni_side_talk at left
    hide tana at tana_near
    hide feni_talk at feni_right
    show feni at feni_right
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Ampun ampun~"
    hide tana_side_talk at left
    hide tana_talk at tana_near
    hide flora at flora_left
    hide feni at feni_right
    show tana at tana_near
    show flora at flora_left
    show feni at feni_right
    with dissolve
    "[mcname!c]" "Hadeh."
    "[mcname!c]" "{i}Aduh. Kok gua jadi laper, ya?{/i}"
    hide tana at tana_near
    hide flora at flora_left
    hide feni at feni_right
    show tana_talk at tana_near
    show flora at flora_left
    show feni at feni_right
    show tana_side_talk at left
    with dissolve
    tana "[mcname!c], lu mau makan dulu ga?"
    hide tana_side_talk at left
    hide tana_talk at tana_near
    hide flora at flora_left
    hide feni at feni_right
    with dissolve
    menu: 
        "Respon kamu..."
        "Boleh. Gua juga laper nih":
            show tana at tana_near
            show flora at flora_left
            show feni at feni_right
            with dissolve
            # $ renpy.block_rollback()
            $ quick_menu = True
            "[mcname!c]" "Boleh. Gua juga laper nih."
            jump chapter1tanamakan

        "Skip, MUALAS.":
            stop music fadeout 1.0
            $ quick_menu = False
            play music "BGM_Bad End.ogg" fadein 1.0
            "[mcname!c]" "Skip, MUALAS."
            scene black with dissolve
            show text "{color=#FFF}INSTRUKSI CERITANYA GINI DOANG?{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FFF}WOY PENULIS CERITA YANG JELAS DONG MASA GITU DOANG{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FFF}DEVELOPER PUNDUNG KARENA YANG NULIS CERITA GAK JELAS{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FF0000}BAD END{/color}" with Pause(2.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits

label chapter1tanamakan:
    hide tana at tana_near
    hide flora at flora_left
    hide feni at feni_right
    show tana_talk at tana_near
    show flora at flora_left
    show feni at feni_right
    show tana_side_talk at left
    with dissolve
    tana "Gasssss. Kak Feni sama Kak Flora mau ikut makan juga?"
    hide tana_side_talk at left
    hide tana_talk at tana_near
    hide flora at flora_left
    hide feni at feni_right
    show tana at tana_near
    show flora at flora_left
    show feni_talk at feni_right
    show feni_side_talk at left
    with dissolve
    feni "Aduh, sorry. Aku udah mesen makan buat di kosan."
    hide feni_side_talk at left
    hide tana at tana_near
    hide flora at flora_left
    hide feni_talk at feni_right
    show tana at tana_near
    show flora_talk at flora_left
    show feni at feni_right
    show flora_side_talk at left
    with dissolve
    flora "Yahhh. Mamahku juga udah masak di rumah. Jadinya gak bisa ikut."
    hide flora_side_talk at left
    hide tana at tana_near
    hide flora_talk at flora_left
    hide feni at feni_right
    show tana_talk at tana_near
    show flora at flora_left
    show feni at feni_right
    show tana_side_talk at left 
    with dissolve
    tana "Aman ajaa."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    hide flora at flora_left
    hide feni at feni_right
    show tana at tana_near
    show flora at flora_left
    show feni at feni_right
    with dissolve
    "[mcname!c] melihat HPnya."
    "[mcname!c]" "Eh, Tana. Gue liat di HP, di mall itu ada Red Ant Cafe yang lagi promo."
    hide tana at tana_near
    hide flora at flora_left
    hide feni at feni_right
    show tana_talk at tana_near
    show flora at flora_left
    show feni at feni_right
    show tana_side_talk at left
    with dissolve
    tana "Wah iya kah? Ayok buruan, keburu sold out."
    tana "Yaudah. Kak, kita duluan yaa."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    hide flora at flora_left
    hide feni at feni_right
    show tana at tana_near
    show flora_talk at flora_left
    show feni_talk at feni_right
    "{size=-5}Feni & Flora{/size}" "Okeee~"
    hide tana at tana_near
    hide flora_talk at flora_left
    hide feni_talk at feni_right
    with dissolve
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Mall.ogg" fadein 1.0
    scene mall temp with Dissolve(1.0)
    $ quick_menu = True
    "Sesampainya di mall.."
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "[mcname!c], Red Ant Cafenya di mana?"
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c] pun membuka HPnya."
    "[mcname!c]" "Hmmm keknya di sini. Udah ikut aja."
    hide tana at tana_near with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Funny 2.ogg" fadein 1.0
    scene mall temp with Dissolve(1.0)
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    # #$ renpy.block_rollback()
    $ quick_menu = True
    tana "Mana nih, [mcname!c]. Lu yang bener, kocak."
    tana "Tau jalan, gak?"
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana_angry at tana_near
    with dissolve
    "[mcname!c]" "Bener kok lewat sini. Percaya aja."
    hide tana_angry at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Halah halah buta map."
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana_angry at tana_near
    with dissolve
    "[mcname!c]" "Ngaca kocakk."
    hide tana_angry at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Berisik lu."
    tana "Mending tanya orang aja. Udah laper."
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana_angry at tana_near
    with dissolve
    "[mcname!c]" "Yauda. Itu ada staff di sana."
    hide tana_angry at tana_near with dissolve
    "Tana dan [mcname!c] pun menghampiri staff mall."
    show tana_talk at tana_near
    show tana_side_talk at left 
    with dissolve
    tana "Permisi, Mba. Mau nanya, kalo Red Ant Cafe ini ada di mana ya?"
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "Staff" "Ohh. Tempatnya ada di sana."
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Wahh, thank you."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    with dissolve
    "Tana dan [mcname!c] pun berjalan sesuai arahan dari staff."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Mall.ogg" fadein 1.0
    scene mall with Dissolve(1.0)
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    $ quick_menu = True
    tana "Ohhh jadi ini cafenya."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Itu udah pada ngantri buat menu promo. Ayok buruan."
    hide tana at tana_near with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play sound "audio/cafe-entrance.mp3" fadein 1.0
    play music "audio/BGM_Cafe Sore.ogg" fadein 1.0
    scene cafe sore with Dissolve(1.0)
    # #$ renpy.block_rollback()
    $ quick_menu = True
    "Setelah mengantri beberapa saat, akhirnya giliran Tana dan [mcname!c] pun tiba."
    show tana at tana_near with dissolve
    "Staff" "Halo Kak. Mau pesan apa?"
    "[mcname!c]" "Mau menu promonya 2, Kak."
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Masih ada kan?"
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "Staff" "Aduh mohon maaf, Kak."
    "Staff" "Menu promonya baru aja sold out."
    hide tana at tana_near
    show tana_shock at tana_near
    show tana_side_shock at left
    with dissolve
    tana "Hahhhh. Udah sold out?"
    hide tana_side_shock at left
    hide tana_shock at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Lu sihh kelamaan muter muter tadi."
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana_angry at tana_near
    with dissolve
    "[mcname!c]" "Ya maap kocak."
    "Staff" "......"
    hide tana_angry at tana_near
    show tana at tana_near
    with dissolve
    "Staff" "Apa mau coba menu yang lain, Kak?"
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Yauda deh. Udah laper banget soalnya."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Yaudah deh nasi bakar tuna 1 sama milkshake strawberry 1."
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Aku samain aja dah."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Sama kentang goreng yang besar 1."
    "Staff" "Oke jadi grilled rice with tuna 2, milkshake strawberry 2, dan large french fries 1."
    "Staff" "Pesanannya nanti akan diantar, ya. Mohon ditunggu."
    hide tana at tana_near with dissolve
    "Tana dan [mcname!c] pun duduk di tempat yang kosong."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene cafe sore with Dissolve(1.0)
    # #$ renpy.block_rollback()
    show tana_confused at tana_near
    show tana_side_confused at left
    with dissolve
    $ quick_menu = True
    tana "Kok nama menunya jadi pake Bahasa Inggris, ya?"
    hide tana_side_confused at left
    hide tana_confused at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Lah kan di menunya emang ada 2 bahasa, kocak."
    hide tana at tana_near
    show tana_confused at tana_near
    show tana_side_confused at left
    with dissolve
    tana "Hmmm. Perasaan gue ga enak."
    hide tana_side_confused at left
    hide tana_confused at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Mau makan aja pake mikir."
    hide tana at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Kagaklah, kocak. Emang elu?"
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana_angry at tana_near
    with dissolve
    "[mcname!c]" "Lu pikir gue mikir, kocak?"
    hide tana_angry at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Halah halah."
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near 
    with dissolve
    "Pelayan pun datang mengantarkan pesanan Tana dan [mcname!c] ke meja mereka."
    show tana at tana_near with dissolve
    "Staff" "Pesanannya sudah semua, ya Kak."
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Iya, Kak. Terima kasih."
    tana "Waaaah. Keliatannya enak banget."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Gak usah sampe ngiler juga, kocak."
    hide tana at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Yeuuu. Siapa juga yang ngiler kocak?"
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana_angry at tana_near
    with dissolve
    "[mcname!c]" "Yauda buruan makan."
    hide tana_angry at tana_near 
    with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene cafe sore with Dissolve(1.0)
    show tana_talk at tana_near
    show tana_side_talk at left
    $ quick_menu = True
    tana "Hmmm enak ya!"
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Pelan-pelan, Tan."
    hide tana
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Santai ajaa~"
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Hadehh..."
    hide tana with dissolve
    stop music fadeout 1.0
    "Beberapa saat kemudian..."
    play music "BGM_Funny 3.ogg" fadein 1.0
# tana batuk
    with dissolve
    tana "UHUK UHUK!"
    "[mcname!c]" "Makanya makan pelan-pelan, kocak. Lu gak makan dari tahun kemarin ato gimana?"
    tana "UHUK UHUK!"
    "[mcname!c]" "Ini minum dulu."
# tana batuk hide
# tana minum
    tana "*Glug Glug*"
    tana "AHHHHH~!"
    show tana_angry at tana_near
    with dissolve
    "[mcname!c]" "Kalo kata gua sih kurang kenceng."
    hide tana_angry at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Yauda kenapa sih?"
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana_angry at tana_near
    with dissolve
    "[mcname!c]" "Hahahahahaha~"
    hide tana_angry at tana_near with dissolve
    "[mcname!c] dan Tana ngobrol di cafe sambil menikmati hidangan yang dipesan."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Kosan 1.ogg" fadein 1.0
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Tak terasa cafe semakin sepi dan para staff terlihat mulai\nberes-beres."
    $ quick_menu = False
    scene cafe malam with Dissolve(2.0)
    # #$ renpy.block_rollback()
    show tana at tana_near with dissolve
    $ quick_menu = True
    "[mcname!c]" "Eh. Kayaknya udah mau tutup nih."
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Yaudah. Ayok kita pulang."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Bayar dulu kocak."
    hide tana at tana_near with dissolve
    "[mcname!c] dan Tana menghampiri kasir untuk membayar pesanan mereka."
    show tana at tana_near with dissolve
    "Staff" "Semuanya jadi 159.420."
    hide tana at tana_near
    show tana_shock at tana_near
    show tana_side_shock at left
    with dissolve
    tana "Lhuk, larange!\n(Wih, mahalnya!)"
    hide tana_side_shock at left
    hide tana_shock at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Lah tadi pesen gak liat menu?"
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Gue kan ngikut pesenan elu. Hadeh, yauda jadi 80 80?"
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Udahh sama gue aja."
    hide tana at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Jangan lah. Lu pikir gue ga punya duit?"
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near 
    with dissolve
    "Tana pun merogoh tasnya untuk mengambil dompet."
#MUNCUL CHIBI TONO DOMPET
    show tana_side_confused at left 
    with dissolve
    tana "Hmmmm?"
    hide tana_side_confused at left with dissolve
    "[mcname!c]" "Kenapa?"
    show tana_side_confused at left with dissolve
    tana "......."
    tana "Ummmmm. Anu"
    tana "......"
    hide tana_side_confused at left with dissolve
    "[mcname!c]" "?????"
    show tana_side_confused at left  with dissolve
    tana "Anuu…"
    hide tana_side_confused at left with dissolve
    "[mcname!c]" "?????"
#HIDE CHIBI TONO DOMPET
    hide tana_confused at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Dompet gue ketinggalan nih, hehe."
    tana "Boleh pinjem duit lu dulu gak?"
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Li pikir giwi gi pinyi diit?"
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Hehehe. Nanti 80 ribu nya pasti gue ganti, serius."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Hadeh yauda. Awas gak lu ganti."
    hide tana at tana_near with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Mall.ogg" fadein 1.0
    scene mall with Dissolve(1.0)
    $ quick_menu = True
    "Setelah membayar, [mcname!c] dan Tana keluar dari cafe lalu bersiap siap untuk pulang."
    show tana_talk at tana_near
    show tana_side_talk at left 
    with dissolve
    tana "Makasih ya."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Aman aja. Btw lu langsung balik ato gimana?"
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Iya deh. Udah capek banget."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Okee. Kalo gitu sampai ketemu besok pagi."
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Jangan lupa besok katanya harus bawa baju ganti."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Buat apa emangnya?"
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Lah, lu nanya gue, gue nanya siapa?"
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Hadeh..."
    hide tana at tana_near with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Kampus.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya..."
    $ quick_menu = False
    scene depan kampus with Dissolve(2.0)
    # #$ renpy.block_rollback()
    $ quick_menu = True
    "Pagi itu [mcname!c] terbangun dan bersiap siap untuk pergi ke kampus."
    stop music fadeout 1.0
    $ quick_menu = False
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    scene black with Dissolve(1.0)
    play music "BGM_Kelas.ogg" fadein 1.0 volume (1.5)
    scene kelas with Dissolve(1.0)
    # #$ renpy.block_rollback()
    $ quick_menu = True
    "Sesampainya di kelas, tiba tiba ada yang menepuk pundak [mcname!c]."
    show tana_talk at tana_near
    show tana_side_talk at left 
    with dissolve
    tana "Oi. Sombong amat dipanggil kaga noleh."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Emang lu manggil?"
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Enggak."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "......."
    "[mcname!c]" "Yeuuu ga jelas. Btw lu bawa baju ganti, kan?"
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Hah? Ngapain?"
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Lah kan elu yang ingetin gua kemarin."
    hide tana at tana_near
    show tana_shock at tana_near
    show tana_side_shock at left
    with dissolve
    tana "Oh iyaa. Gimana nih?"
    tana "Gue gak bawaaa."
    hide tana_side_shock at left
    with dissolve
    "[mcname!c]" "Hadeh..."
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    hide tana_shock at tana_near with dissolve
    "???" "Selamat pagi, semuanya!"
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene kelas with Dissolve(1.0)
    # #$ renpy.block_rollback()
    show tana at tana_right
    show flora_talk at flora_left
    show flora_side_talk at left
    with dissolve
    $ quick_menu = True
    flora "Kalian bawa baju ganti, kan?"
    hide flora_talk
    show flora at flora_left
    hide flora_side_talk at left
    with dissolve
    "[mcname!c]" "Tana gak bawa, Kak!"
    hide tana at tana_right
    hide flora_talk at flora_left
    show tana_angry_2 at tana_right 
    show flora_angry at flora_left
    show tana_side_angry_2 at left
    with dissolve
    tana "Alahhh cepu."
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_right
    hide flora at flora_left
    show tana at tana_right 
    show flora_angry_talk at flora_left
    show flora_side_angry_talk at left 
    with dissolve
    flora "Kan udah dibilangin bawa baju ganti."
    flora "Soalnya hari ini agenda kita ke sawah."
    hide flora_angry_talk
    hide flora_side_angry_talk
    show flora_talk at flora_left
    show flora_side_talk at left
    with dissolve
    flora "Hmmm. Yaudah, tapi hati-hati kotor."
    hide flora_side_talk at left
    hide tana at tana_right
    hide flora_talk at flora_left
    show tana_talk at tana_right 
    show flora at flora_left
    show tana_side_talk at left 
    with dissolve
    tana "Siap, kak."
    hide tana_side_talk at left
    hide tana_talk at tana_right
    hide flora at flora_left 
    hide flora_angry
    with dissolve
    "Tana, [mcname!c], dan teman-teman sekelas pergi mengikuti arahan dari Kak Flora."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Sawah Siang.ogg" fadein 1.0
    scene sawah with Dissolve(1.0)
    # #$ renpy.block_rollback()
    $ quick_menu = True
    "Flora, Tana, [mcname!c], dan mahasiswa lainnya sampai di gerbang sawah."
    show tana at tana_right
    show flora_talk at flora_left
    show flora_side_talk at left 
    with dissolve
    flora "Ini sawah milik kampus, ya. Gerbang ke sawah dibuka dari jam 7 pagi sampai jam 5 sore."
    flora "Yuk masuk."
    hide flora_side_talk at left
    hide flora_talk at flora_left
    show flora at flora_left 
    with dissolve
    "[mcname!c]" "Nah, Tan. Harus hati hati soalnya Lu ga bawa baju ganti soalnya."
    hide tana at tana_right
    show tana_talk at tana_right
    show tana_side_talk at left
    with dissolve
    tana "Aman ajaa. Gue udah biasa di sawah."
    hide tana_side_talk at left
    hide tana_talk at tana_right
    show tana_angry at tana_right
    with dissolve
    "[mcname!c]" "Siap si yang paling tani."
    hide tana_angry at tana_right
    show tana_talk at tana_right
    show tana_side_talk at left
    with dissolve
    tana "Akulah si yang paling tani itu."
    hide tana_side_talk at left
    hide tana_talk at tana_right
    show tana_angry at tana_right
    with dissolve
    "[mcname!c]" "Siap Mbak Tani."
    hide tana_angry at tana_right
    show tana_angry_2 at tana_right
    show tana_side_angry_2 at left
    with dissolve
    tana "Nama gue Tana, kocak. Bukan Tani."
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_right
    hide flora at flora_left
    show flora_talk at flora_left
    show tana at tana_right
    show flora_side_talk at left
    with dissolve
    flora "Di sini ada banyak petak sawah. Kalian bebas mau ke mana, tapi hati-hati ya. Soalnya licin, sawahnya basah."
    flora "1 jam lagi kumpul di sini, ya."
    hide flora_side_talk at left
    hide tana at tana_right
    hide flora_talk at flora_left
    show flora at flora_left
    show tana_talk at tana_right
    show tana_side_talk at left
    with dissolve
    tana "Ke sana yuk, [mcname!c]."
    hide tana_side_talk at left
    hide tana_talk at tana_right
    show tana at tana_right
    with dissolve
    "[mcname!c]" "Ayoook."
    hide flora at flora_left
    hide tana at tana_right
    with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene sawah with Dissolve(1.0)
    # #$ renpy.block_rollback()
    $ quick_menu = True
    "Tana dan [mcname!c] menyusuri sawah bersama."
    show tana at tana_near with dissolve
    "[mcname!c]" "Tana! Jangan cepet-cepet woi. Licin tauu."
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Santai ajaa. Gua udah biasa jalan di sawah."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana_confused at tana_near
    show tana_side_confused at left
    with dissolve
    stop music fadeout 1.0
    tana "Eh!?"
    hide tana_side_confused at left
    hide tana_confused at tana_near 
    with dissolve
# Insert TONO kepeleset 1.png
    show tana_side_shock at left 
    with dissolve
    tana "EHHHHHHHH?"
    hide tana_side_shock at left 
    with dissolve
    "[mcname!c]" "Tannn!!"
    $ quick_menu = False
# Hide TONO Kepeleset 1.png
    play sound "SFX - Fall Water.WAV" volume (4.0)
    scene black with Dissolve(1.0)
# Harusnya BG Sawah
    play music "BGM_Funny 3.ogg" fadein 1.0
    scene sawah with Dissolve(1.0)
    $ quick_menu = True
    "[mcname!c] berniat menolong Tana, tapi malah ikut tercebur."
    "[mcname!c]" "Adududuh."
    # Insert Tono jatoh.png
    "Sambil mencoba berdiri, [mcname!c] melihat Tana yang tercebur dalam lumpur."
    "[mcname!c]" "Udah gede ga usah nangis kocak."
    show tana_side_shock at left
    with dissolve
    tana "S-siapa yang mau nangis?"
    hide tana_side_shock at left
    with dissolve
    # Hide Tono jatoh.png
    "[mcname!c] pun membantu Tana berdiri."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "BGM_Sawah Siang.ogg" fadein 1.0
    scene sawah with Dissolve(1.0)
    show tana_confused at tana_near
    show tana_side_confused at left 
    with dissolve
    $ quick_menu=True
    tana "M-Makasih ya."
    hide tana_side_confused at left
    hide tana_confused at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Lah tumben. Kepala lu gapapa?"
    "Tana pun mengusap kepalanya."
    show tana_talk at tana_near
    show tana_side_talk at left 
    with dissolve
    tana "Nggak apa apa kok. Ga ada benjol."
    tana "Emang kenapa?"
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "......"
    hide tana at tana_near 
    show tana_confused at tana_near
    show tana_side_confused at left
    with dissolve
    tana "????"
    hide tana_side_confused at left
    hide tana_confused at tana_near
    show tana_sad at tana_near
    show tana_side_sad at left
    with dissolve
    tana "Sorry ya. Elu jadi ikutan kotor buat nolongin gua."
    hide tana_side_sad at left with dissolve
    "[mcname!c]" "Makanya hati hati."
    hide tana_sad at tana_near
    show tana at tana_right
    show flora_angry_talk at flora_left
    show flora_side_angry_talk at left
    with dissolve
    flora "Aduhhh kalian kenapa ini."
    hide flora_side_angry_talk at left
    hide flora_angry_talk at flora_left
    show flora_talk at flora_left
    show flora_side_talk at left
    with dissolve
    flora "Yauda kalian nunggu di pinggir dulu aja sambil keringin dulu pake handuk ini."
    hide flora_side_talk at left
    hide tana at tana_right
    hide flora_talk at flora_left
    show tana_talk at tana_right
    show flora at flora_left
    show tana_side_talk at left
    with dissolve
    "{size=-5}Tana & [mcname!c]{/size}" "Terima kasih Kak."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    hide flora at flora_left 
    with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene sawah with Dissolve(1.0)
    show tana at tana_near with dissolve
    $ quick_menu = True
    "[mcname!c]" "Lu gimana pulangnya nanti?"
    "[mcname!c]" "Kan gak bawa baju ganti."
    hide tana at tana_near
    show tana_confused at tana_near
    show tana_side_confused at left
    with dissolve
    tana "Gimana, ya?"
    hide tana_side_confused at left
    hide tana_confused at tana_near 
    with dissolve
    "Tiba-tiba Flora datang menghampiri untuk memeriksa keadaan Tana dan [mcname!c]."
    show tana at tana_right
    show flora_talk at flora_left
    show flora_side_talk at left 
    with dissolve
    flora "Oi. Gimana kalian? Gapapa?"
    hide flora_side_talk at left
    hide tana at tana_right
    hide flora_talk at flora_left
    show tana_talk at tana_right
    show flora at flora_left
    show tana_side_talk at left 
    with dissolve
    tana "Untungnya gak ada luka. Cuman nahan malu aja."
    hide tana_side_talk at left
    hide tana_talk at tana_right
    hide flora at flora_left
    show tana at tana_right
    show flora at flora_left
    with dissolve
    "[mcname!c]" "Aku juga aman, tapi Tana gak bawa baju ganti."
    hide flora at flora_left
    show flora_talk at flora_left
    show flora_side_talk at left
    with dissolve
    flora "Tana. Nanti sesudah kegiatannya selesai, kamu ke ruang club aja."
    flora "Di sana harusnya ada baju ganti."
    hide flora_side_talk at left
    hide tana at tana_right
    hide flora_talk at flora_left
    show tana_talk at tana_right
    show flora at flora_left
    show tana_side_talk at left 
    with dissolve
    tana "Niceee. Arigatou, Senpai!"
    hide tana_side_talk at left
    hide tana_talk at tana_right
    hide flora at flora_left
    show tana at tana_right
    show flora at flora_left
    with dissolve
    "[mcname!c]" "Hadeh wibu… wibu."
    hide tana at tana_right
    hide flora at flora_left 
    with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Sore.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Tak terasa waktu menjadi sore..."
    $ quick_menu = False
    scene sawah sore with Dissolve(2.0)
    show tana at tana_right
    show flora_talk at flora_left
    show flora_side_talk at left
    with dissolve
    $ quick_menu = True
    flora "Ya. Kegiatannya sudah selesai, ya."
    flora "Semuanya boleh bersiap-siap lalu pulang."
    hide flora_side_talk at left
    hide tana at tana_right
    hide flora_talk at flora_left
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Akhirnyaa."
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left 
    with dissolve
    tana "Kamu mau ke kelas sekarang?"
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Iya, nih. Udah kotornya udah kelamaan soalnya."
    hide tana at tana_near with dissolve
    "Flora menghampiri Tana."
    show tana at tana_right
    show flora_talk at flora_left
    show flora_side_talk at left 
    with dissolve
    flora "Tana, ayo ikut ke ruangan club."
    hide flora_side_talk at left
    hide tana at tana_right
    hide flora_talk at tana_right
    show tana_talk at tana_right
    show flora at flora_left
    show tana_side_talk at left 
    with dissolve
    tana "Oke, Kak."
    hide tana_side_talk at tana_right
    hide flora at tana_right
    hide tana_talk at tana_right
    show tana at tana_right
    show flora at flora_left
    with dissolve
    "[mcname!c]" "Yaudah gue duluan ya, Tan."
    "[mcname!c]" "Kak Flora, aku pulang dulu ya."
    hide tana at tana_right
    hide flora at flora_left
    show tana_talk at tana_right
    show flora_talk at flora_left
    with dissolve
    "{size=-5}Flora & Tana{/size}" "Okeee~"
    hide tana_talk at tana_right
    hide flora_talk at flora_left 
    with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Kelas.ogg" fadein 1.0 volume (1.5)
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya.."
    $ quick_menu = False
    scene kelas with Dissolve(2.0)
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    # #$ renpy.block_rollback()
    $ quick_menu = True
    tana "Ohayou, [mcname!c]."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Hadeh wibu."
    "[mcname!c]" "Oha~"
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Yeu. Sama aja."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Hahahahaha~"
    "[mcname!c]" "Btw, kemarin jadinya gimana sama Kak Flora? Ada baju ganti?"
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Untungnya ada, hehe."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Makanya jangan aneh-aneh."
    "[mcname!c]" "Pake kepeleset segala."
    hide tana at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Ya kan ga sengaja, kocak."
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Hadeeh~"
    hide tana at tana_near with dissolve
    "Terdengar suara pintu terbuka."
    stop music fadeout 1.0
    $ quick_menu = False
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    scene black with Dissolve(1.0)
    play music "BGM_Dosen.ogg" fadein 1.0
    scene kelas with Dissolve(1.0)
    # #$ renpy.block_rollback()
    show dosen_talk at dosen_center
    show dosen_side_talk at left
    with dissolve
    $ quick_menu = True
    dosen "Ya teman-teman, saatnya memulai pembelajaran."
    hide dosen_side_talk at left
    hide dosen_talk at dosen_center 
    with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Sore.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Berjam jam kemudian..."
    $ quick_menu = False
    scene kelas sore with Dissolve(2.0)
    show dosen_talk at dosen_center
    show dosen_side_talk at left
    with dissolve
    $ quick_menu = True
    dosen "Pelajaran hari ini sampai sini saja."
    dosen "Kalian dipersilahkan untuk pulang."
    hide dosen_side_talk at left
    hide dosen_talk at dosen_center
    show dosen at dosen_center
    with dissolve
    "Mahasiswa/i" "Baik, Buu."
    hide dosen with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene kelas sore with Dissolve(1.0)
    show tana at tana_near with dissolve
    $ quick_menu = True
    "[mcname!c]" "Fiuuuh. Akhirnya pelajaran selesai juga."
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Iyaaa. Susah juga pelajarannya."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Itu mah elu yang skill issue."
    hide tana at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Lu aja tadi ngelamun, kocak."
    show tana_angry at tana_near
    hide tana_angry_2
    hide tana_side_angry_2 at left
    with dissolve
    "[mcname!c]" "Nggak kocak, itu tadi gue mode fokus banget."
    hide tana_angry
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Halah halah."
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "BTW kamu free?"
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Free, kok. Emangnya kenapa?"
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Kalo free, ayok ke cafe yang kemarin lagi."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Hah ngapain."
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Udahh ikut aja."
    tana "Sebagai tanda terima kasih udah nolongin gue kemarin, gue beliin menu promo yang waktu itu kehabisan."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Minimal 80k nya balikin kocaak."
    hide tana at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Ya nanti sekalian aja kocak."
    hide tana_angry_2
    show tana_angry at tana_near
    hide tana_side_angry_2 at left
    with dissolve
    "[mcname!c]" "Hahaha yauda, ayok."
    hide tana_angry at tana_near with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Mall.ogg" fadein 1.0
    scene mall temp with Dissolve(1.0)
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    $ quick_menu = True
    tana "Mumpung baru dateng, mau jalan-jalan dulu ga?"
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Ngikut aja gue mahh. Yang penting gak tersesat."
    hide tana at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Halah halah."
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near 
    with dissolve
    "[mcname!c] dan Tana berjalan bersama berkeliling di mall. Tiba tiba…"
    play sound "SFX - Telephone.mp3" fadein 1.0 loop
    show tana at tana_near with dissolve
    "Ada yang nelepon HP [mcname!c]."
    stop sound
    "[mcname!c] membuka HP nya dan melihat bahwa mamahnya menelpon."
    #Insert UI Handphone Nelpon"
    "[mcname!c]" "Eh Tana, bentar ya. Mamah gue nelepon."
    "[mcname!c]" "Gue ke sana dulu, ya."
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Okee~"
    stop music fadeout 1.0
    hide tana_side_talk at left
    hide tana_talk at tana_near 
    with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene mall temp with Dissolve(1.0)
    #Insert UI Handphone Nelpon"
    play music "BGM_Happy + HP.ogg" fadein 1.0 volume (2.0)
    show telpon_mamah at ui_handphone with dissolve
    show side mama at left with dissolve
    $ quick_menu = True
    mama "Enak ya, anakku udah tinggal sendiri. Sekarang ga pernah ngabarin Mamah lagi. Huhu."
    hide side mama at left with dissolve
    "[mcname!c]" "Maaf, Maah. Lupa, lagi banyak yang dikerjain."
    show side mama at left with dissolve
    mama "Sering-sering dong kabarin."
    mama "Mamah kan jadi gelisah."
    hide side mama at left with dissolve
    "[mcname!c]" "Iya, Mahh."
    show side mama at left with dissolve
    mama "Gimana kuliahnya?"
    hide side mama at left with dissolve
    "[mcname!c]" "Baik kok. Aku juga gabung club jejepangan, hehe."
    show side mama at left with dissolve
    mama "Waduh, kayak papahmu dong."
    hide side mama at left with dissolve
    "[mcname!c]" "Hehehe~"
    show side mama at left with dissolve
    mama "Yaudaa. Kamu baik-baik di sana. Kalo ada apa-apa, telepon mamah aja."
    hide side mama at left with dissolve
    "[mcname!c]" "Siap Mah. Aku duluan ya, bye-bye~"
    show side mama at left with dissolve
    mama "Byee~"
    hide side mama at left with dissolve
    "Hide UI Telepon"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Mall.ogg" fadein 1.0
    scene mall temp with Dissolve(1.0)
    $ quick_menu = True
    "[mcname!c]" "Hmmmmm."
    "[mcname!c]" "Eh, Tana mana?"
    "Bingung karena Tana menghilang, [mcname!c] melihat ke arah sekitar."
    "[mcname!c]" "Oh, di situ ternyata."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Game Center.ogg" fadein 1.0
    scene game center with Dissolve(1.0)
    # #$ renpy.block_rollback()
    $ quick_menu = True
    "[mcname!c]" "Tana ngapain ke sini ya?"
    "[mcname!c] menghampiri Tana yang pergi ke game center."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Rooftop Pia Malam.ogg" fadein 1.0
    scene game center with Dissolve(1.0)
#MUNCUL ASSET DANCE ARCADE GAME
    # #$ renpy.block_rollback()
    $ quick_menu = True
    "Terlihat seorang gadis cantik menari gemulai di depan mesin dance arcade."
    "Setiap gerakannya dari lompatan hingga ayunan lembut lengannya mengikuti irama lagu ceria yang dimainkan, membuat [mcname!c] terpukau."
    "[mcname!c]" "......"
    "Di tengah rasa kagum tersebut, [mcname!c] mengeluarkan HPnya."
    "[mcname!c]" "Tana, gue masukin story ya?"
    show tana_side at left
    with dissolve
    tana ".........."
    hide tana_side at left
    with dissolve
    "Tana yang fokus mengayunkan tangan dan kakinya, tampak tidak menyadari keberadaan [mcname!c]."
    "[mcname!c]" "Hmmm dia ga jawab, keknya lagi fokus. Harusnya dibolehin lah ya."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene game center with Dissolve(1.0)
    # #$ renpy.block_rollback()
    $ quick_menu = True
    "Ketika tarian itu mencapai puncaknya kemudian diakhiri dengan gerakan yang elegan, memutar tubuhnya sekali lagi sebelum berhenti dengan satu gerakan terakhir yang sempurna."
    show tana_side_talk at left
    with dissolve
    play sound "SFX - Large Cheering.mp3" fadein 1.0
    tana "Yeyyy perfect score!"
#HIDE SPRITE ASSET DANCE ARCADE
    hide tana_side_talk at left
    show tana at tana_near
    with dissolve
    stop music fadeout 1.0
    "[mcname!c]" "*Tepuk tangan*"
    hide tana at tana_near
    show tana_confused at tana_near
    show tana_side_confused at left
    with dissolve
    stop sound fadeout 1.0
    play music "BGM_Game Center.ogg" fadein 1.0
    tana "E-Eh? [mcname!c]? Lu dari kapan di sini?"
    hide tana_side_confused at left
    hide tana_confused at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Baru aja kok."
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Oooooh. Fiuh, gue kira udah dari tadi."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Keren juga lu perfect score!"
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Gue gitu lohh. Yauda, yuk ke cafenya sekarang."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Gass!"
    hide tana at tana_near with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    play sound "audio/cafe-entrance.mp3" fadein 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Cafe sore.ogg" fadein 1.0
    scene cafe sore with Dissolve(1.0)
    # #$ renpy.block_rollback()
    $ quick_menu = True
    "Sesampainya di cafe, Tana dan [mcname!c] langsung mendatangi kasir."
    show tana at tana_near with dissolve
    "Staff" "Haloo, mau pesan apa?"
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Mbak! Plis banget, yang ini promonya masih ada kan?"
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "Staff" "Ada kok, kak. Paket promonya 2 spicy noodle, 2 fried wonton, 2 ice tea, dan dimsum."
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Asikk masih ada!"
    tana "Kalo gitu, pesen 1 promo, ya."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Lu bawa duit, kan?"
    hide tana at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Sekarang mah bawa kocak."
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Iye iye, percaya dah."
    "Staff" "Kalo gitu paket promonya 1, ya."
    "Staff" "Pesanannya nanti akan kami antar."
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Terima kasih, kak."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Tan, di sana kosong."
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Oke."
    hide tana_side_talk at left
    hide tana_talk at tana_near 
    with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    pause(1.0)
    scene cafe sore with Dissolve(1.0)
    $ quick_menu = True
    "Tak lama setelah [mcname!c] dan Tana duduk, pesanan diantarkan oleh staff."
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Cepet juga datengnya."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Iya nih."
    "Staff" "Pesanan sudah sesuai, ya."
    "[mcname!c]" "Sudah, Mbak. Terima kasih."
    hide tana at tana_near with dissolve
    "Tana dan [mcname!c] berbincang sambil menikmati pesanan yang dipesan."
    show tana at tana_near with dissolve
    "[mcname!c]" "Pelan pelan, kocak. Kalo keselek Mi Pedes, mati lu."
    hide tana at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Iye iye."
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Btw, gue baru tau lu bisa ngedance."
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Iya, gue dulu perform di event-event jejepangan."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Oooooh, emang wibu."
    hide tana at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Lu juga, kocak."
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Tapi gua sekarang udah gak pernah ngedance lagi, sih."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Lah kenapa?"
    hide tana at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Kepo lu. Mending makan."
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Idihh, sok misterius banget lu."
    hide tana at tana_near
    show tana_laugh at tana_near
    show tana_side_laugh at left
    with dissolve
    tana "AHAHAHAHA-"
    hide tana_side_laugh at left
    hide tana_laugh at tana_near
    with dissolve
    stop music fadeout 1.0
    "Tiba-tiba..."
# SHOW tono keselek 2.png (Soalnya di ceritanya habis dari kampus, jdi harus pake keselek yg baju kampus)
    play music "BGM_Funny 3.ogg" fadein 1.0
    show tana_side_shock at left with dissolve
    tana "UHUK UHUK UHUK!"
    hide tana_side_shock with dissolve
    "[mcname!c]" "Nah, kan. Hadehh..."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
# HIDE tono keselek 2.png
    play music "BGM_Cafe Sore.ogg" fadein 1.0
    scene cafe sore with Dissolve(1.0)
    $ quick_menu = True
    "Setelah selesai makan, Tana dan [mcname!c] menghampiri kasir untuk membayar pesanan."
    show tana_talk at tana_near
    show tana_side_talk at left 
    with dissolve
    tana "Kak ini harga menu promonya 48 ribu, ya?"
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "Staff" "Iya, kak."
    "[mcname!c]" "Lu seriusan bawa duit, kan?"
    hide tana at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Liat nih gue bayar."
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near 
    with dissolve
    "Tana memberikan uang kepada kasir."
    show tana at tana_near with dissolve
    "Staff" "Terima kasih banyak, Kak."
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Yauda, ayok pulang."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "UHUK! UHUK!"
    hide tana at tana_near
    show tana_confused at tana_near
    show tana_side_confused at left
    with dissolve
    tana "Lu kenapa kocak?"
    tana "Keselek angin?"
    hide tana_side_confused at left
    hide tana_confused at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Uhuk 80 ribu, uhuk."
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Oia, lupa. Hehe~"
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana_angry_2 at tana_near
    show tana_side_angry_2 at left
    with dissolve
    tana "Ini yahh. Perhitungan banget sih lu ah."
    hide tana_side_angry_2 at left
    hide tana_angry_2 at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Nah, gitu dongg."
    hide tana at tana_near
    show tana_talk at tana_near
    show tana_side_talk at left
    with dissolve
    tana "Yauda gue duluan, ya. Habis ini ada urusan lagi."
    hide tana_side_talk at left
    hide tana_talk at tana_near
    show tana at tana_near
    with dissolve
    "[mcname!c]" "Yauda gue juga cabut dulu. Thanks ya traktirannya."
    hide tana at tana_near with dissolve
    "Tana dan [mcname!c] pulang ke rumahnya masing-masing."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Kosan 1.ogg" fadein 1.0
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Sesampainya di kost..."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(2.0)
    # #$ renpy.block_rollback()
    $ quick_menu = True
    "[mcname!c] berbaring di kasur sambil menatap langit-langit."
    "[mcname!c]" "......"
    show white:
        default
        subpixel True 
        parallel:
            Null(0.0, 0.0)
            'white' with dissolve
        parallel:
            ypos 0 alpha 1.0 
            linear 1.30 ypos 252 alpha 0.7 
    show white as white2:
        default
        subpixel True 
        parallel:
            Null(0.0, 0.0)
            'white' with dissolve
        parallel:
            ypos 2080 alpha 1.0 
            linear 1.30 ypos 1908 alpha 0.7 
    with Pause(1.40)
    show tana_laugh at tana_near with dissolve
    "[mcname!c]" "{i}Dipikir pikir, Tana cantik banget ya dancenya.{/i}"
    "[mcname!c]" "......"
    hide white
    hide white2
    hide tana_laugh
    with Dissolve(1.0)
    "[mcname!c]" "{i}Ah, kok malah jadi mikirin Tana.{/i}"
    "[mcname!c]" "{i}Mending turu.{/i}"
    jump chapter2tana