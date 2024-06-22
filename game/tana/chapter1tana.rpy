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