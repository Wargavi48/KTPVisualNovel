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
    tana "Lah lu ngapa kocaaak, orang kita lagi bercanda"
    "Cowok 1" "Yeuuu party pooper lu!"
    "Cowok 2" "Dah bubar bubar"
    $ quick_menu = False
    scene black with dissolve
    scene depan kampus with dissolve
    "2 cowok itu pun pergi"
    mcname "{i}Noooo baru ketemu orang di sini malah malu-maluin aaaaa{/i}"
    show tana at char_center with dissolve
    show tana_side at left with dissolve
    tana "Ah kocak, mereka temen-temen gua, gak berani macem-macem juga kok mereka"
    hide tana_side with dissolve
    mcname "Aduh, maaf ya kukira kerumunan jahat tadi"
    show tana_side at left with dissolve
    tana "Halah halah…"
    tana "Tapi makasih loh udah khawatir, gua duluan yak. Dadaaah"
    hide tana_side with dissolve
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
    show tana at char_center with dissolve
    mcname "Aduh kok aku jadi kepikiran terus sama cewek itu, ya? Apakah karena malu?"
    mcname "Dah ah. Tidur dulu, besok hari pertama orientasi"
    hide tana with dissolve
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
    play sound "audio/open_door.mp3"
    show text "{color=#FFF}MEMASUKI RUANG KELAS{/color}" with Pause(2.0)
    scene kelas with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    "Ternyata pas duduk di kelas, Cewek yang [mcname] temui kemarin pun duduk juga di sebelah [mcname]."
    show tana at char_center with dissolve
    show tana_side at left with dissolve
    tana "Lah sekelas?"
    hide tana_side with dissolve
    mcname "Ah eh umm. Iya, hehe"
    mcname "{i}LAH sekelas sama cewek yang kemarin aduh tambah malu dah ini mah{/i}"
    show tana_side at left with dissolve
    tana "Eh lu lagi... Kita kemarin belum kenalan kan?"
    $ tono_name = "Tana"
    tana "Gua Tana. Nama lu siapa?"
    hide tana_side with dissolve
    mcname "Gua [mcname]"
    show tana_side at left with dissolve
    tana "Kaku amat ngomong \"gua\"-nya, bukan dari Jakarta ya?"
    hide tana_side with dissolve
    mcname "Hehe iya anak rantau nih"
    show tana_side at left with dissolve
    tana "Eh sama dong, gua juga dari desa. Terus kenapa pilih jurusan Teknik Pertanian?"
    hide tana_side with dissolve
    mcname "Kata mamah biar bisa memakmurkan para petani di kampung"
    show tana_side at left with dissolve
    tana "Heee. Alasan gua pilih jurusan ini juga mirip-mirip sama lu"
    tana "Selain itu, ya karena gua dari kecil doyan main di sawah hehe"
    hide tana_side with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play sound "audio/open_door.mp3"
    show text "{color=#FFF}DOSEN MEMASUKI KELAS{/color}"
    scene kelas with dissolve
    play music "audio/BGM_Dosen + Rektor.mp3" fadein 1.0
    show dosen at dosen_center with dissolve
    show dosen_side at left with dissolve
    dosen "Selamat datang Mahasiswa baru Jurusan pertanian"
    dosen "Oke, kegiatan hari ini adalah perkenalan lingkungan kampus. Silahkan berkumpul dengan kelompoknya masing-masing"
    dosen "Instruksi selanjutnya ada di pembimbing kelompok masing-masing, terima kasih"
    dosen "HIDUP PERTANIAN INDONESIA."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with dissolve
    scene kelas with dissolve
    play music "audio/BGM_kelas.mp3" fadein 1.0
    show flora at char_center with dissolve
    show flora_side at left with dissolve
    flora "Halo semuanya, kenalin aku Flora, pembimbing kelompok ini"
    flora "Sekarang langsung baris aja terus kita keliling kampus ya!"
    hide flora_side with dissolve
    "Mahasiswa" "Iya Kak"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    # Harusnya BG Lorong
    scene depan kampus with dissolve
    #  Harusnya BGM Lorong
    play music "audio/BGM_Kampus.mp3" fadein 1.0
    "[mcname] dan kelompoknya pun berkeliling kampus untuk melihat fasilitas jurusan pertanian dibimbing oleh Kakak kelasnya yang bernama Flora. Tapi tiba tiba…"
    mcname "{i}Duh kebelet{/i}"
    mcname "{i}Ke toilet dulu aman kali ya gak bakal ketinggalan kelompok{/i}"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    "Dengan sedikit terburu buru, [mcname] bergegas ke toilet."
    "Setelah selesai, [mcname] pun keluar toilet dan melihat sekeliling."
    $ quick_menu = False
    # Harusnya BG Lorong
    scene depan kampus with dissolve
    # Harusnya BGM Lorong
    play music "audio/BGM_Kampus.mp3" fadein 1.0
    $ renpy.block_rollback()
    $ quick_menu = True
    mcname "{i}Aduh pada kemana ya kok udah sepi aja, mana gak tau jalan lagi{/i}"
    mcname "Eh itu ada Tana lagi sendirian"
    "[mcname] melihat Tana yang tampaknya sedang kebingungan"
    "[mcname] pun menghampiri Tana"
    show tana at char_center with dissolve
    show tana_side at left with dissolve
    tana "Hmmm? Eh, kok lu ada di sini?"
    hide tana_side with dissolve
    mcname "Gua ketinggalan rombongan, tadi ke toilet dulu soalnya"
    show tana_side at left with dissolve
    tana "Yeuuu kocak"
    tana "Yaudah ayo ikutin gua, kita nyusul yang lain"
    hide tana_side with dissolve
    mcname "Emang lu udah hapal denah kampus ini ya?"
    show tana_side at left with dissolve
    tana "Alah gampang itu mah"
    tana "Kampus paling gitu-gitu aja tata letaknya"
    hide tana_side with dissolve
    mcname "Yaudah ngikut deh"
    "Karena tidak tau arah, [mcname] pun mengikuti Tana menyusuri kampus."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}1 JAM KEMUDIAN{/color}" with Pause(2.0)
    scene awan with dissolve
    scene black with dissolve
    # Harusnya BG lorong 
    scene depan kampus with dissolve
    #  Harusnya BGM Lorong
    play music "audio/BGM_Lawak Tana.mp3" fadein 1.0
    show tana at char_center with dissolve
    mcname "Tan, perasaan dari tadi kita cuma muter-muter doang deh"
    show tana_side at left with dissolve
    tana "Santai. Bentar lagi juga ketemu sama kelompok kita"
    hide tana_side with dissolve
    mcname "Udah sore gini mereka harusnya udah beres gak sih?"
    show tana_side at left with dissolve
    tana "Sabar, kocak, masih siang kok ini"
    hide tana_side with dissolve
    mcname "Sebenernya lu tau kita di mana gak sih?"
    show tana_side at left with dissolve
    tana "T-tau, kok. Udah, ayo lanjut jalan"
    hide tana_side with dissolve
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}1 JAM KEMUDIAN{/color}" with Pause(2.0)
    scene kantin with dissolve
    show tana at char_center with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    mcname "Tan, ini bukannya kantin, ya?"
    show tana_side at left with dissolve
    tana "E-Emang iya?"
    hide tana_side with dissolve
    mcname "Iya, kocak"
    show tana_side at left with dissolve
    tana "Kok lu jadi ikut-ikutan ngomong kocak?"
    hide tana_side with dissolve
    mcname "Ga usah ngalihin pembicaraan."
    mcname "Sebenernya lu tadi juga nyasar kan?"
    show tana_side at left with dissolve
    tana "M-mana ada gua nyasar"
    hide tana_side with dissolve
    mcname "Kocak"
    show tana_side at left with dissolve
    tana "Lu kocak"
    hide tana_side with dissolve
    mcname "Hahahaha."
    mcname "Ternyata kita sama-sama malu-maluin, ya"
    show tana_side at left with dissolve
    tana "Lu doang kali. Gua kagak"
    hide tana_side with dissolve
    mcname "Yeuuu, kocak"
    show tana_side at left with dissolve
    tana "Gak cocok lu ngomong kocak-kocak begitu"
    hide tana_side with dissolve
    mcname "Biarin. Daripada gak mau ngaku nyasar"
    show tana_side at left with dissolve
    tana "Alaaaah. Iya iya gua juga nyasar."
    tana "Puas lu?"
    hide tana_side with dissolve
    mcname "AHAHAHAHAHAHAHAHAH"
    show tana_side at left with dissolve
    tana "Diem lu"
    hide tana_side with dissolve
    mcname "Dih, ngamuk"
    show tana_side at left with dissolve
    tana "Berisik"
    hide tana_side with dissolve
    mcname "Sekarang mau gimana?"
    show tana_side at left with dissolve
    tana "Ya lanjut jalan lah. Masa diem di sini"
    hide tana_side with dissolve
    mcname "Yaudah. Balik ke tempat tadi aja"
    hide tana with dissolve
    "[mcname] dan Tana pun kembali menyusuri kampus"
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with dissolve
    show text "{color=#FFF}DISAAT BERSAMAAN{/color}" with Pause(2.0)
    # Harusnya BG Lorong
    scene depan kampus with dissolve
    play music "audio/BGM_Kampus.mp3" fadein 1.0
    show flora at char_center with dissolve
    show flora_side at left with dissolve
    flora "Duh. Ini dari tadi 2 orang ilang pada kemana ya?"
    flora "Kelompoknya udah beres keliling kampus, mereka masih gak ketemu."
    flora "Udah sore lagi..."
    flora "Harusnya jam segini aku beresin ruangan klub, ini malah harus nyari 2 bocah."
    flora "Aaarrggghh."
    flora "Pasti Kak Feni udah nungguin aku."
    flora "Hmm?"
    flora "Eh itu dia mereka"
    flora "Hey, kalian dari mana aja sih?! Dari tadi dicariin, tapi malah berduaan di sini"
    hide flora_side with dissolve
    hide flora with dissolve
    show flora at char_left with dissolve
    show tana at char_right with dissolve
    show tana_side at left with dissolve
    tana "M-Maaf, kak, hehe"
    tana "Kita berdua tadi ketinggalan rombongan"
    tana "Lu sih malah ke toilet dulu tanpa izin ke Kak Flora"
    hide tana_side with dissolve
    mcname "Lah? Lu kan malah udah kepisah duluan dari kelompok sebelum kita ketemu"
    show flora_side at left with dissolve
    flora "Dieeeem!"
    flora "Kalian tuh udah ngerusak jadwal aku sore ini tau gak?"
    flora "Malah ribut sendiri"
    hide flora_side with dissolve
    mcname "Maaf, kak, tadi kita niatnya mau nyusul kelompok, tapi malah nyasar. Gara-gara Tana, nih"
    show tana_side at left with dissolve
    tana "Lah? Kok salah gua"
    hide tana_side with dissolve
    mcname "Lu sih sotoy. Jadinya salah jalan kan"
    show flora_side at left with dissolve
    flora "Malah saling nyalahin"
    flora "Aduh, harusnya sore ini itu aku beres-beres ruangan klub, tapi gak jadi gara-gara harus nyariin kalian"
    flora "Kasian banget Kak Feni tadi aku tinggal sendirian"
    hide flora_side with dissolve
    show tana_side at left with dissolve
    tana "Maaf ya, kak…"
    hide tana_side with dissolve
    show flora_side at left with dissolve
    flora "Maaf doang nih?"
    hide flora_side with dissolve
    mcname "Gimana kalo kita bantuin Kak Flora beres-beres sebagai gantinya?"
    show tana_side at left with dissolve
    tana "Iyaa kak, kita bantuin deh…"
    hide tana_side with dissolve
    show flora_side at left with dissolve
    flora "Nah, gitu dong. Yaudah ayo ikut sini."
    hide flora_side with dissolve
    hide flora with dissolve
    hide tana with dissolve
    "[mcname], Tana, dan Flora pun pergi menuju ruang klub yang dimaksud oleh Flora"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    # Harusnya BG UKM Jepang
    scene kelas with dissolve
    # Harusnya BGM UKM Jepang
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    show feni at char_left with dissolve
    show flora at char_right with dissolve
    show tana at char_center with dissolve
    show feni_side at left with dissolve
    feni "Flo-chaaaaan dari mana aja kamu?"
    feni "Aku dari tadi beberes sendirian tauuu"
    hide feni_side with dissolve
    show flora_side at left with dissolve
    flora "Kak Feni, maaaaaf, tadi aku jadi pembimbing kelompok, terus 2 orang ini malah nyasar gak balik-balik."
    flora "Jadinya aku nyari mereka dulu"
    hide flora_side with dissolve
    "{size=-5}[mcname] & Tana{/size}" "Maaf, kak"
    show feni_side at left with dissolve
    feni "Terus kenapa kalian ikut Flora kesini?"
    hide feni_side with dissolve
    show flora_side at left with dissolve
    flora "Katanya sih mereka mau bantuin aku beres-beres, Kak."
    flora "Iya, kan?"
    flora "Hehe"
    hide flora_side with dissolve
    "{size=-5}[mcname] & Tana{/size}" "Iya kak"
    show feni_side at left with dissolve
    feni "Yaudah, sok atuh."
    feni "Aku istirahat duluan, ya!"
    feni "Capek euy"
    feni "Dari tadi beberes sendirian"
    hide feni_side with dissolve
    "[mcname] & Tana" "Iya, kak, izin bantu beresin ruangan klubnya, ya"
    "[mcname] dan Tana pun mulai membereskan ruang klub sesuai dengan arahan Feni dan Flora"
    show tana_side at left with dissolve
    tana "Kak, ini tuh ruang klub jejepangan ya?"
    hide tana_side with dissolve
    show flora_side at left with dissolve
    flora "Iya. Namanya \"Koiken\"(Nyoba masukin nama random yang artinya bagus)"
    hide flora_side with dissolve
    show tana_side at left with dissolve
    tana "Kegiatannya ngapain aja?"
    hide tana_side with dissolve
    "Flora pun menjelaskan apa saja kegiatan klub jejepangan itu"
    show tana_side at left with dissolve
    tana "Ih, seru banget!"
    hide tana_side with dissolve
    show flora_side at left with dissolve
    flora "Seru, kan?"
    flora "Ada yang mau ikut aku?"
    hide flora_side with dissolve
    show tana_side at left with dissolve
    tana "Aku aku aku!"
    tana "[mcname], lu mau ikut klub jejepangan ini juga kan??"
    hide tana_side with dissolve
    mcname "Ngapain gua ikut beginian?"
    show tana_side at left with dissolve
    tana "Yaudah ikut aja kenapa sih? Temenin gua napa"
    hide tana_side with dissolve
    mcname "Iya iya"
    show feni_side at left with dissolve
    feni "[mcname], kamu jangan iya iya aja. Kamu beneran mau ikut atau nggak?"
    feni "Emang kamu tau soal jejepangan?"
    hide feni_side with dissolve
    show flora_side at left with dissolve
    flora "Nah. Coba kamu sebutin deh 5 anime yang kamu tau"
    flora "Gak boleh nyebut Narto, Two Piece, sama Pembasmi Iblis"
    hide flora_side with dissolve
    $ quick_menu = False
    menu:
        "Anime Pilihan Kamu:"
        "-Samurai Y\n-Pemburu x Pemburu\n-Mengubah sampah menjadi pohon\n-Pelaut bulan\n-Inisial F":
            $ renpy.block_rollback()
            $ quick_menu = True
            mcname "-Samurai Y\n-Pemburu x Pemburu\n-Mengubah sampah menjadi pohon\n-Pelaut bulan\n-Inisial F"
            show feni_side at left with dissolve
            feni "Kamu gak naik kelas berapa kali kok tau anime-anime itu, tapi sekarang masih maba"
            hide feni_side with dissolve
            mcname "Hehehe..."
        "-Cinta Palsu\n-Ekor Peri\n-Yo-Gi-Ah 3Ds\n-Adu Gasing\n-April Skem":
            $ renpy.block_rollback()
            $ quick_menu = True
            mcname "-Cinta Palsu\n-Ekor Peri\n-Yo-Gi-Ah 3Ds\n-Adu Gasing\n-April Skem"
            show flora_side at left with dissolve
            flora "Boleh juga tontonanmu. Mirip-mirip lah ya"
            hide flora_side with dissolve
            mcname "Iya dong. Bagus, kan?"
        "-Bola Naga X\n-Seni Pedang Offline\n-Siapa namamu?\n-Akademi Pahlawan\n-Keluarga Mata-Mata":
            $ renpy.block_rollback()
            $ quick_menu = True
            mcname "-Bola Naga X\n-Seni Pedang Offline\n-Siapa namamu?\n-Akademi Pahlawan\n-Keluarga Mata-Mata"
            show flora_side at left with dissolve
            flora "Kamu pasti wibu fomo, ya"
            hide flora_side with dissolve
            mcname "Waduh"
    show flora_side at left with dissolve
    flora "Yaa, sudah terbukti tingkat kewibuannya."
    flora "Ikut klub sini aja udah"
    hide flora_side with dissolve
    mcname "Iya iya"
    show feni_side at left with dissolve
    feni "Malah iya-iya lagi"
    hide feni_side with dissolve
    mcname "Hai, sumimasen"
    show tana_side at left with dissolve
    tana "Dasar wibu"
    hide tana_side with dissolve
    mcname "Ngaca sana"
    show tana_side at left with dissolve
    tana "Hai, gomen gomen"
    hide tana_side with dissolve
    show flora_side at left with dissolve
    flora "Gomen gomen, summernya mana?"
    hide flora_side with dissolve
    show feni_side at left with dissolve
    feni "Gomenne summer~"
    hide feni_side with dissolve
    "Sore itu, ruang club pun dipenuhi gelak tawa dan canda ria.[mcname] dan Tana pun akhirnya bergabung dalam klub jejepangan bersama Feni dan Flora. Mereka berempat pun lanjut membersihkan ruang klub sampai malam."
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}BEBERAPA MENIT KEMUDIAN{/color}"
    # Harusnya BG UKM Jejepangan
    scene kelas with dissolve
    show flora at char_left with dissolve
    show feni at char_right with dissolve
    show tana at char_center with dissolve
    show tana_side at left with dissolve
    tana "Akkh. Akhirnya kelar juga"
    tana "Asli capek banget"
    hide tana_side with dissolve
    mcname "Ah kayak lu kerja aja"
    show tana_side at left with dissolve
    tana "Ehh gua mah kerja. Gak kek lu"
    hide tana_side with dissolve
    mcname "Mang eak?"
    show tana_side at left with dissolve
    tana "Halah halah"
    hide tana_side with dissolve
    show flora_side at left with dissolve
    flora "Kalian capek? Bayangin kalo itu cuma aku sama Kak Feni yang beresin"
    hide flora_side with dissolve
    show feni_side at left with dissolve
    feni "Kejauhan bayanginnya. Bayangin dulu coba kalo aku sendirian yang beresin!"
    hide feni_side with dissolve
    show tana_side at left with dissolve
    tana "Semangat, kak"
    hide tana_side with dissolve
    show feni_side at left with dissolve
    feni "Dih. Malah ngeledekin nih anak"
    hide feni_side with dissolve
    show tana_side at left with dissolve
    tana "Ampun ampun"
    hide tana_side with dissolve
    mcname "Hadeh"
    mcname "{i}Aduh. Kok gua jadi laper, ya?{/i}"
    show tana_side at left with dissolve
    tana "[mcname], lu mau makan dulu, ga?"
    $ quick_menu = False
    menu: 
        "Respon Kamu"
        "Boleh. Gua juga laper nih":
            $ renpy.block_rollback()
            $ quick_menu = True
            mcname "Boleh. Gua juga laper nih"
        "Skip, MUALAS.":
            mcname "Skip, MUALAS."
            stop music fadeout 1.0
            scene black with dissolve
            show text "{color=#FFF}INSTRUKSI CERITANYA GINI DOANG?{/color}" with Pause(2.0)
            show text "{color=#FFF}WOY PENULIS CERITA YANG JELAS DONG MASA GITU DOANG{/color}" with Pause(2.0)
            show text "{color=#FFF}DEVELOPER PUNDUNG KARENA YANG NULIS CERITA GAK JELAS{/color}" with Pause(2.0)
            show text "{color=#FF0000}BAD END{/color}"
            play music "audio/Dreamcatcher.mp3" fadein 1.0
            jump credits
    show tana_side at left with dissolve
    tana "Gasssss. Kak Feni sama Kak Flora mau ikut makan juga?"
    hide tana_side with dissolve
    show feni_side at left with dissolve
    feni "Aduh, sorry. Aku udah mesen makan buat di kosan."
    hide feni_side with dissolve
    show flora_side at left with dissolve
    flora "Yahhh. Mamahku juga udah masak di rumah. Jadinya gak bisa ikut."
    hide flora_side with dissolve
    show tana_side at left with dissolve
    tana "Aman ajaa."
    hide tana_side with dissolve
    "[mcname] melihat HP nya"
    mcname "Eh, Tana. Gue liat di HP, di mall itu ada cafe #Sponsor 2 yang lagi promo."
    show tana_side at left with dissolve
    tana "Wah iya kah? Ayok buruan, keburu sold out."
    tana "Yauda. kak, kita duluan yaa."
    hide tana_side with dissolve
    "{size=-5}Feni & Flora{/size}" "Okeee"
    "[mcname] & Tana pun pergi ke mall"
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with dissolve
    show text "{color=#FFF}SESAMPAINYA DI MALL{/color}" with Pause(2.0)
    play music "audio/BGM_Mall Slow.mp3" fadein 1.0
    scene mall temp with dissolve
    show tana at char_center with dissolve
    show tana_side at left with dissolve
    $ quick_menu = True
    tana "MC, Cafe #Sponsor 2 nya di mana?"
    hide tana_side with dissolve
    "[mcname] pun membuka HP nya"
    mcname "Hmmm keknya di sini. Udah ikut aja"
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}20 MENIT KEMUDIAN{/color}" with Pause(2.0)
    show tana at char_center with dissolve
    show tana_side at left with dissolve
    tana "Mana nih, [mcname]. Lu yang bener, kocak."
    tana "Tau jalan, gak?"
    hide tana_side with dissolve
    mcname "Bener kok lewat sini. Percaya aja."
    show tana_side at left with dissolve
    tana "Halah halah buta map."
    hide tana_side with dissolve
    mcname "Ngaca kocakk."
    show tana_side at left with dissolve
    tana "Berisik lu."
    tana "Mending tanya orang aja. Udah laper."
    hide tana_side with dissolve
    mcname "Yauda. Itu ada staff di sana."
    "Tana dan [mcname] pun menghampiri staff mall"
    show tana_side at left with dissolve
    tana "Permisi, Mba. Mau nanya, kalo cafe #Sponsor 2 ini ada di mana ya?"
    hide tana_side with dissolve
    "Staff" "Ohh. Tempatnya ada di sana."
    show tana_side at left with dissolve
    tana "Wahh, thank you."
    hide tana_side with dissolve
    "Tana dan MC berjalan sesuai arahan Staff"
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}BEBERAPA MENIT KEMUDIAN{/color}" with Pause(2.0)
    scene mall temp with dissolve
    show tana at char_center with dissolve
    show tana_side at left with dissolve
    $ quick_menu = True
    tana "Ohhh jadi ini cafenya."
    hide tana_side with dissolve
    mcname "Itu udah pada ngantri buat menu promo. Ayok buruan."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with dissolve
    play sound "audio/cafe-entrance.mp3" fadein 1.0
    show text "{color=#FFF}MEMASUKI CAFE{/color}"
    play music "audio/BGM_Cafe Sore" fadein 1.0
    scene cafe with dissolve
    show tana at char_center with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    "Setelah mengantri beberapa saat, akhirnya giliran Tana dan [mcname] pun tiba."
    "Staff" "Halo Kak. Mau pesan apa?"
    mcname "Menu promonya 2, Kak"
    show tana_side at left with dissolve
    tana "Masih ada kan?"
    hide tana_side with dissolve
    "Staff" "Aduh mohon maaf, Kak"
    "Staff" "Menu promonya baru aja sold out"
    show tana_side at left with dissolve
    tana "Hahhhh. Udah sold out?"
    tana "Lu sihh kelamaan muter muter tadi."
    hide tana_side with dissolve
    mcname "Ya maap kocak."
    "Staff" "......"
    "Staff" "Apa mau coba menu yang lain, Kak?"
    show tana_side at left with dissolve
    tana "Yauda deh. Udah laper banget soalnya."
    hide tana_side with dissolve
    mcname "Yaudah deh nasi bakar tuna 1 sama milkshake strawberry 1"
    show tana_side at left with dissolve
    tana "Aku samain aja dah."
    hide tana_side with dissolve
    mcname "Sama kentang goreng yang besar 1."
    "Staff" "Oke jadi grilled rice with tuna 2, milkshake strawberry 2, dan large french fries 1."
    "Staff" "Pesanannya nanti akan diantar, ya. Mohon ditunggu."
    "Tana dan [mcname] duduk di tempat yang kosong"
    show tana_side at left with dissolve
    tana "Kok nama menunya jadi pake Bahasa Inggris, ya?"
    hide tana_side with dissolve
    mcname "Lah kan di menunya emang ada 2 bahasa, kocak."
    show tana_side at left with dissolve
    tana "Hmmm. Perasaan gue ga enak."
    hide tana_side with dissolve
    mcname "Mau makan aja pake mikir."
    show tana_side at left with dissolve
    tana "Kagaklah, kocak. Emang elu?"
    hide tana_side with dissolve
    mcname "Lu pikir gue mikir, kocak?"
    show tana_side at left with dissolve
    tana "Halah halah."
    hide tana_side with dissolve
    "Pelayan pun datang mengantarkan pesanan Tana dan [mcname] ke meja mereka."
    "Staff" "Pesanannya sudah semua, ya Kak."
    show tana_side at left with dissolve
    tana "Iya, Kak. Terima kasih."
    tana "Waaaah. Keliatannya enak banget"
    hide tana_side with dissolve
    mcname "Gak usah sampe ngiler juga, kocak."
    show tana_side at left with dissolve
    tana "Yeuuu. Siapa juga yang ngiler kocak?"
    hide tana_side with dissolve
    mcname "Yauda buruan makan."
    "Tana dan [mcname] menyantap makanan yang dipesan."
    show tana_side at left with dissolve
    tana "UHUK UHUK."
    hide tana_side with dissolve
    mcname "Makanya makan pelan-pelan, kocak. Lu gak makan dari tahun kemarin ato gimana?"
    show tana_side at left with dissolve
    tana "UHUK UHUK."
    hide tana_side with dissolve
    mcname "Ini minum dulu"
    show tana_side at left with dissolve
    tana "*Glug Glug*"
    tana "AHHHHH"
    hide tana_side with dissolve
    mcname "Kalo kata gua sih kurang kenceng"
    show tana_side at left with dissolve
    tana "Yauda kenapa sih?"
    hide tana_side with dissolve
    mcname "Hahahahahaha"
    $ quick_menu = False
    scene black with dissolve
    scene cafe with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname] dan Tana ngobrol di cafe sambil menikmati hidangan yang dipesan. Tak terasa cafe semakin sepi dan para staff terlihat mulai beres-beres."
    show tana at char_center with dissolve
    mcname "Eh. Kayaknya udah mau tutup nih."
    show tana_side at left with dissolve
    tana "Yaudah. Ayok kita pulang."
    hide tana_side with dissolve
    mcname "Bayar dulu kocak."
    "[mcname] dan Tana menghampiri kasir untuk membayar pesanan mereka."
    "Staff" "Semuanya jadi 159.420."
    show tana_side at left with dissolve
    tana "Lhuk, larange!\n(Wih, mahalnya)"
    hide tana_side with dissolve
    mcname "Lah tadi pesen gk liat menu?"
    show tana_side at left with dissolve
    tana "Gue kan ngikut pesenan elu. Hadeh, yauda jadi 80 80?"
    hide tana_side with dissolve
    mcname "Udahh sama gue aja."
    show tana_side at left with dissolve
    tana "Jangan lah. Lu pikir gue ga punya duit?"
    hide tana_side with dissolve
    "Tana pun merogoh tasnya untuk mengambil dompet."
    show tana_side at left with dissolve
    tana "Hmmmm?"
    hide tana_side at left with dissolve
    mcname "Kenapa?"
    show tana_side at left with dissolve
    tana "......."
    tana "Ummmmm. Anu"
    tana "......"
    hide tana_side with dissolve
    mcname "?????"
    show tana_side at left with dissolve
    tana "Anuu…"
    tana "Dompet gue ketinggalan nih, hehe"
    tana "Boleh pinjem duit lu dulu gak?"
    hide tana_side with dissolve
    mcname "Li pikir giwi gi pinyi diit?"
    show tana_side at left with dissolve
    tana "Hehehe. Nanti 80 ribu nya pasti gue ganti, serius."
    hide tana_side with dissolve
    mcname "Hadeh yauda. Awas gak lu ganti"
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with dissolve
    scene mall temp with dissolve
    play music "audio/BGM_Mall Slow.mp3" fadein 1.0
    $ quick_menu = True
    "Setelah membayar, [mcname] dan Tana keluar dari cafe lalu bersiap siap untuk pulang."
    show tana at char_center with dissolve
    show tana_side at left with dissolve
    tana "Makasih ya."
    hide tana_side with dissolve
    mcname "Aman aja. Btw lu langsung balik ato gimana?"
    show tana_side at left with dissolve
    tana "Iya deh. Udah capek banget."
    hide tana_side with dissolve
    mcname "Okee. Kalo gitu sampai ketemu besok pagi."
    show tana_side at left with dissolve
    tana "Jangan lupa besok katanya harus bawa baju ganti"
    hide tana_side with dissolve
    mcname "Buat apa emangnya?"
    show tana_side at left with dissolve
    tana "Lah, lu nanya gue, gue nanya siapa?"
    hide tana_side with dissolve
    mcname "Hadeh..."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}KEESOKAN HARINYA{/color}" with Pause(2.0)
    scene depan kampus with dissolve
    "Pagi itu [mcname] terbangun dan bersiap siap untuk pergi ke kampus."
    $ quick_menu = False
    play sound "audio/open_door.mp3"
    scene black with dissolve
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    scene kelas with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    "Sesampainya di kelas, tiba tiba ada yang menepuk pundak [mcname]."
    show tana at char_center with dissolve
    show tana_side at left with dissolve
    tana "Oi. Sombong amat dipanggil kaga noleh."
    hide tana_side with dissolve
    mcname "Emang lu manggil?"
    show tana_side at left with dissolve
    tana "Enggak."
    hide tana_side with dissolve
    mcname "......."
    mcname "Yeuuu ga jelas. Btw lu bawa baju ganti, kan?"
    show tana_side at left with dissolve
    tana "Hah? Ngapain?"
    hide tana_side with dissolve
    mcname "Lah kan elu yang ingetin gua kemarin."
    show tana_side at left with dissolve
    tana "Oh iyaa. Gimana nih?"
    tana "Gue gak bawaaa."
    hide tana_side with dissolve
    mcname "Kata gue GUAS sih."
    "???" "Selamat pagi, semuanya!"
    $ quick_menu = False
    scene black with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    "Kakak pembimbing sampai di kelas"
    show flora at char_left with dissolve
    show tana at char_right with dissolve
    show flora_side at left with dissolve
    flora "Kalian bawa baju ganti, kan?"
    hide flora_side with dissolve
    show tana_side at left with dissolve
    tana "Alahhh cepu."
    hide tana_side with dissolve
    show flora_side at left with dissolve
    flora "Kan udah dibilangin bawa baju ganti"
    flora "Soalnya hari ini agenda kita ke sawah."
    flora "Hmmm. Yaudah, tapi hati-hati kotor."
    hide flora_side with dissolve
    show tana_side at left with dissolve
    tana "Siap, kak"
    hide tana_side with dissolve
    "Tana, [mcname], dan teman-teman sekelas pergi mengikuti arahan dari Kak Flora."
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with dissolve
    # Harusnya BG Sawah
    scene depan kampus with dissolve
    #  Harusnya BGM Sawah
    play msuic "audio/BGM_Kampus.mp3" fadein 1.0
    $ renpy.block_rollback()
    $ quick_menu = True
    "Flora, Tana, [mcname], dan mahasiswa lainnya sampai di gerbang sawah."
    show flora at char_left with dissolve
    show tana at char_right with dissolve
    show flora_side at left with dissolve
    flora "Ini sawah milik kampus, ya. Gerbang ke sawah dibuka dari jam 7 pagi sampai jam 5 sore."
    flora "Yuk masuk"
    hide flora_side with dissolve
    mcname "Nah, Tan. Harus hati hati soalnya Lu ga bawa baju ganti soalnya"
    show tana_side at left with dissolve
    tana "Aman ajaa. Gue udah biasa di sawah."
    hide tana_side with dissolve
    mcname "Siap si yang paling tani."
    show tana_side at left with dissolve
    tana "Akulah si yang paling tani itu."
    hide tana_side with dissolve
    tana "Siap Mbak Tani"
    show tana_side at left with dissolve
    tana "Nama gue Tana, kocak. Bukan Tani."
    hide tana_side with dissolve
    show flora_side at left with dissolve
    flora "Di sini ada banyak petak sawah. Kalian bebas mau ke mana, tapi hati-hati ya. Soalnya licin."
    flora "1 jam lagi kumpul di sini, ya."
    hide flora_side with dissolve
    show tana_side at left with dissolve
    tana "Ke sana yuk, [mcname]."
    hide flora_side with dissolve
    mcname "Ayoook"
    $ quick_menu = False
    scene black with dissolve
    # Harusnya BG Sawah
    scene depan kampus with dissolve
    show tana at char_center with dissolve
    "Tana dan [mcname] menyusuri sawah bersama."
    mcname "Tana! Jangan cepet-cepet woi. Licin tauu."
    show tana_side at left with dissolve
    tana "Santai ajaa. Gua udah biasa jalan di sawah."
    tana "Eh!?"
    hide tana with dissolve
    # Insert Chibi tana kecebur sawah
    show tana_side at left with dissolve
    tana "EHHHHHHHH?"
    hide tana_side with dissolve
    mcname "Tannn!!"
    # Hide Chibi tana kecebur sawah
    $ quick_menu = False
    scene black with dissolve
    # Insert SFX Byurrr
    # Harusnya BG Sawah
    scene depan kampus with dissolve
    "[mcname] berniat menolong Tana, tapi malah ikut tercebur."
    mcname "Adududuh"
    "Sambil mencoba berdiri, [mcname] melihat Tana yang tercebur dalam lumpur"
    # Insert Chibi Tono Jatuh Tutup Mulut
    mcname "Udah gede ga usah nangis kocak."
    # Chibi Tono Jatuh ilang
    show tana at char_center with dissolve
    show tana_side at left with dissolve
    tana "S-siapa yang mau nangis?"
    hide tana_side with dissolve
    "[mcname] membantu Tana berdiri."
    show tana_side at left with dissolve
    tana "M-Makasih ya."
    hide tana_side with dissolve
    mcname "Lah tumben. Kepala lu gapapa?"
    "Tana pun mengusap kepalanya"
    show tana_side at left with dissolve
    tana "Nggak apa apa kok. Ga ada benjol."
    tana "Emang kenapa?"
    hide tana_side with dissolve
    mcname "......"
    show tana_side at left with dissolve
    tana "????"
    tana "Sorry ya. Elu jadi ikutan kotor buat nolongin gua."
    hide tana_side with dissolve
    mcname "Makanya hati hati."
    hide tana with dissolve
    show tana at char_left with dissolve
    show flora at char_right with dissolve
    show flora_side at left with dissolve
    flora "Aduhhh kalian kenapa ini."
    flora "Yauda kalian nunggu di pinggir dulu aja sambil keringin dulu pake handuk ini."
    hide flora_side with dissolve
    "{size=-5}Tana & [mcname]{/size}" "Terima kasih Kak."
    scene black with Pause(2.0)
    # Harusnya BG Sawah
    scene depan kampus with dissolve
    show tana at char_center with dissolve
    mcname "Lu gimana pulangnya nanti?"
    mcname "Lu kan gak bawa baju ganti"
    show tana_side at left with dissolve
    tana "Gimana, ya?"
    hide tana_side with dissolve
    "Tiba tiba Flora datang menghampiri untuk memeriksa keadaan Tana dan [mcname]."
    hide tana with dissolve
    show tana at char_left with dissolve
    show flora at char_right with dissolve
    show flora_side at left with dissolve
    flora "Oi. gimana kalian? Gapapa?"
    hide flora_side with dissolve
    show tana_side at left with dissolve
    tana "Untungnya gak ada luka. Cuman nahan malu aja."
    hide tana_side with dissolve
    mcname "Aku juga aman, tapi Tana gak bawa baju ganti."
    show flora_side at left with dissolve
    flora "Tana. Nanti sesudah kegiatannya selesai, kamu ke ruang club aja"
    flora "Di sana harusnya ada baju ganti."
    hide flora_side with dissolve
    show tana_side at left with dissolve
    tana "Niceee. Arigatou, Senpai!"
    hide tana_side with dissolve
    mcname "Hadeh wibu… wibu."
    $ quick_menu = False
    scene black with dissolve
    scene awan with dissolve
    # Harusnya BG Sawah siang
    scene depan kampus with dissolve
    show flora at char_left with dissolve
    show tana at char_right with dissolve
    show flora_side at left with dissolve
    $ quick_menu = True
    flora "Ya. Kegiatannya sudah selesai, ya."
    flora "Semuanya boleh bersiap-siap lalu pulang."
    hide flora_side with dissolve
    mcname "Akhirnyaa."
    show tana_side at left with dissolve
    tana "Kamu mau ke kelas sekarang?"
    hide tana_side with dissolve
    mcname "Iya, nih. Udah kotornya udah kelamaan soalnya."
    "Flora menghampiri Tana"
    show flora_side at left with dissolve
    flora "Tana, ayo ikut ke ruangan club."
    hide flora_side with dissolve
    show tana_side at left with dissolve
    tana "Oke, Kak"
    hide tana_side with dissolve
    mcname "Yaudah gue duluan ya, Tan."
    mcname "Kak Flora, aku pulang dulu ya."
    "{size=-5}Flora & Tana{/size}" "Okeee"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}KEESOKAN HARINYA\nDI KELAS{/color}" with Pause(2.0)
    scene kelas with dissolve
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    show tana at char_center with dissolve
    show tana_side at left with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    tana "Ohayou, [mcname]"
    hide tana_side at left with dissolve
    mcname "Hadeh wibu."
    mcname "Oha~"
    show tana_side at left with dissolve
    tana "Yeu. Sama aja"
    hide tana_side with dissolve
    mcname "Hahahahaha~"
    mcname "Btw, kemarin jadinya gimana sama Kak Flora? Ada baju ganti?"
    show tana_side at left with dissolve
    tana "Untungnya ada, hehe."
    hide tana_side with dissolve
    mcname "Makanya jangan aneh-aneh."
    mcname "Pake kepeleset segala."
    show tana_side at left with dissolve
    tana "Ya kan ga sengaja, kocak."
    hide tana_side with dissolve
    mcname "Hadeeh~"
    "Terdengar suara pintu terbuka."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    play sound "audio/open_door.mp3"
    show text "{color=#FFF}DOSEN PUN MEMASUKI RUANG KELAS{/color}"
    scene kelas with dissolve
    play music "audio/BGM_Dosen + Rektor.mp3" fadein 1.0
    show dosen at dosen_center with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True
    show dosen_side at left with dissolve
    dosen "Ya teman-teman, saatnya memulai pembelajaran."
    $ quick_menu = False
    scene black with dissolve
    show dosen at dosen_center with dissolve
    show dosen_side at left with dissolve
    $ quick_menu = True
    dosen "Pelajaran hari ini sampai sini saja."
    dosen "Kalian dipersilahkan untuk pulang."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    scene kelas with dissolve
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    show tana at char_center with dissolve
    $ quick_menu = True
    mcname "Fiuuuh. Akhirnya pelajaran selesai juga."
    show tana_side at left with dissolve
    tana "Iyaaa. Susah juga pelajarannya"
    hide tana_side with dissolve
    mcname "Itu mah elu yang skill issue."
    show tana_side at left with dissolve
    tana "Lu aja tadi ngelamun, kocak."
    hide tana_side with dissolve
    mcname "Nggak kocak, itu tadi gue mode fokus banget."
    show tana_side at left with dissolve
    tana "Halah halah."
    tana "BTW kamu free?"
    hide tana_side with dissolve
    mcname "Free, kok. Emangnya kenapa?"
    show tana_side at left with dissolve
    tana "Kalo free, ayok ke cafe yang kemarin lagi."
    hide tana_side with dissolve
    mcname "Hah ngapain"
    show tana_side at left with dissolve
    tana "Udahh ikut aja."
    tana "Sebagai tanda terima kasih udah nolongin gue kemarin, gue beliin menu promo yang waktu itu kehabisan."
    hide tana_side with dissolve
    mcname "Minimal 80k nya balikin kocaak."
    show tana_side at left with dissolve
    tana "Ya nanti sekalian aja kocak."
    hide tana_side with dissolve
    mcname "Hahaha yauda, ayok."