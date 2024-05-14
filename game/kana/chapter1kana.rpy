label chapter1kana1:
    $ renpy.block_rollback()
    scene dream with dissolve
    $ quick_menu = True
    play music "audio/kampus.mp3" loop fadein 1.0
    mcname "huuuu, ini hari pertama gw orientasi di Jeketi University"
    mcname "di sini tempat dimana gw bakalan kenal sama orang baru, temen baru, atau bahkan jodoh heheh"
    $ quick_menu = False
    scene depan kampus with dissolve
    $ quick_menu = True 
    "[mcname] memasuki aula"
    "Saat memasuki ruangan MC mendengar suara aula yang sangat ramai"
    mcname "Seperti yang diharapkan dari kampus ibu kota, orang nya rame banget"
    "Saat memperhartikan sekitar [mcname] mendengar suatu topik yang menarik perhatiannya"
    "{size=-5}Mahasiswa A{/size}" "Eh eh liat deh itu kan mahasiswi itu"
    "{size=-5}Mahasiswa B{/size}" "Yang mana sih?"
    "{size=-5}Mahasiswa A{/size}" "ituuu, yang ituu tuhh"
    "Pembicaraan mereka yang cukup keras membuat MC pun melirik ke arah orang yang menjadi bahan pembicaraan"
    "{size=-5}Mahasiswa B{/size}" "Owhhh dia!!, eh bukanya dia mahasiswa yang….bla bla bla"
    "Disaat itupun juga [mcname] terpana  dan mencoba untuk memfokuskan matanya fokus terhadap bahan pembicaraan para mahasiswa itu"
    $ quick_menu = False
    scene kana awal with dissolve
    $ quick_menu = True
    "seorang wanita muda yang memiliki rambut berwarna biru muda yang mengingatkan nya kepada lautan"
    "dan juga matanya yang seindah batu sapphire, serta tas dan sepatunya yang ber brand membuat [mcname] terdiam"
    $ quick_menu = False
    scene depan kampus with dissolve
    $ quick_menu = True
    mcname "Dia siapa"
    mcname "Ko banyak di gosipin sama mahasiswa baru ya"
    mcname "tapi diliat-liat cantik anggun, kalem banget dah sumpah kalau di liat liat mah"
    mcname "ko ada ya orang se cantik dia, atau emng semua orang dari kota itu kaya gitu"
    mcname "pasti dia orangnya kalem, sopan, pinter dan hobinya juga baca buku"
    "[mcname] pun melihat ke arah sekelilingnya"
    mcname "Hmmm emng si hampir semua keliatan cantik"
    mcname "tapiii ko cuma dia ya yang jadi perhatian orang-orang..ya termasuk aku juga si"
    $ quick_menu = False
    scene black with dissolve
    scene depan kampus with dissolve
    $ quick_menu = True
    "Rektor" " selamat datang mahasiswa baru yang memasuki Jekiti university bla bla bla…"
    "Perkataan sambutan dari rektor dan jajaran dosen membuat MC dan beberapa mahasiswa/i lain merasa bosan"
    "Seakan mendukung perkatan MC, beberapa mahasiswa pun ada yang bermain hp, mengobrol bahkan bercanda"
    "{size=-5}Mahasiswa A{/size}" "eh bosenin bet dah, template banget ini ucapan selamat datangnya tuh, bikin ngatuk ya ga ?"
    "{size=-5}Mahasiswa B{/size}" "Iyaa njirr, bener banget dah mending kita login yuk P MOLE MOLE"
    "{size=-5}Mahasiswa C{/size}" "Gas kali ya login"
    "Obrolan dari mahasiswa tersebut sesekali mengalihkan perhatian [mcname]"
    "Akan tetapi, pandangannya sekali lagi teralihkan saat kana  tersenyum tipis dan tanganya yang berusaha menutupi senyumannya"
    mcname "Akhirnya selesai juga sambutan dan kegiatan hari ini"
    "[mcname] merengangkan badannya yang terasa kaku akibat duduk terlalu lama"
    mcname "Eh masih jam segini mayan cape juga ya hari ini tapi masih ada energi si"
    # insert cg kana
    $ quick_menu = False
    scene kana awal with dissolve
    $ quick_menu = True
    mcname "Aduhhh ko gw ga bisa ilangin senyuman itu dari kepala gw ya ?"
    mcname "Apa jangan jangan gw kena santet lagi nih?"
    mcname "Ah masa sih, lagian kan dia emang cantik jadi pantes dong kalau gw suka hehe"
    mcname "Eh masih jam segini nih enaknya buat habisin waktu mending gw"
    $ quick_menu = False
    menu:
        "Mau Kemana?"
        "A. Ke Kosan":
            "Kamu habisin waktu di kosan dan memilih buat istirahatin diri daripada pergi kesana kemari"
            jump chapter1kana2Campus
        "B. Ke Warteg":
            "Kamu milih makan ke warteg dan di situ ternyata wartegnya pake boraks dan akhirnya kamu masuk rumah sakit"
            scene black with dissolve
            show text "{color=#FFF}MAKANYA JANGAN MAKAN SEMBARANG BROO KAN MASUK RUMAH SAKIT{/color}" with Pause(2.0)
        "C. Ke Cafe":
            $ quick_menu = False
            scene black with dissolve
            jump chapter1kana2Cafe
            
    
label chapter1kana2Cafe:
    $ renpy.block_rollback()
    scene cafe with dissolve
    play music "audio/bgm_cafe_2.mp3" fadein 1.0
    $ quick_menu = True
    "Ramainya orang orang yang lalu lalang di luar cafe dan memasuki cafe pun terkadang menarik perhatian si MC akan tetapi ada satu orang yang membuat dia semakin fokus"
    "Saat orang itu mendekati pintu cafe [mcname] pun menyadari bahwa orang itu adalah mahasiswi yang dibicarakan tadi"
    mcname "Anjir ko ada CEWEK ITU di sini, bukannya cewek itu yang katanya anak orang kaya, yang sepupunya rektor itu kan"
    mcname "ko dia masuk ke cafe ini anjir anjir dia"
    mcname "CANTIK BANGET CUYYYY"
    mcname "Stay cool…stay cool…eh tapi ko dia liat sana sini dah ?"
    mcname "Kenapa ya?"
    mcname "Samperin kali ya?"
    mcname "Ehhh tapi jangan deh stay cool aja"
    "Secara tidak sadar [mcname] pun melihat ke arah perempuan tersebut saking fokusnya ia melupakan semua pelanggan yang ada di dalam cafe tersebut"
    "Akan tetapi semakin diperhatikan semakin aneh gerak geriknya"
    "Pandangannya yang melihat ke sana kemari dan gerak tubuhnya yang menunjukan dirinya gelisah membuat [mcname] pun berpikir"
    mcname "Hmmm kenapa ya ko dari tadi dia kaya gelisah gtu sih"
    mcname "Lah iya ya, kan sekarang lagi rame makanya dia kaya gtu nyari yang kosong kali ya"
    "Perempuan itu dan [mcname] pun secara tidak sengaja bertukar pandangan"
    "Saat itu juga [mcname] sadar bahwa di sebelahnya itu terdapat kursi kosong untuk satu orang"
    "Saat itu juga [mcname] pun memalingkan pandangannya"
    "Perempuan itu pun mendekati Meja yang dimana [mcname] berada dengan cepat"
    "Seakan tidak sabar dan tidak ingin kehilangan kursi tersebut"
    "panik dan cemas tetapi rasa senang bercampur satu di dalam pikiran [mcname]"
    show kana_shy at char_center with dissolve
    show kana_side_shy at left with dissolve
    kana "H-halooo, maaf tapi apa kursinya kosong ?"
    hide kana_side_shy with dissolve
    mcname "Eh iya ini kosong ko kebetulan dari tadi ga ada yang nempatin"
    mcname "Takut kali ya sama aku haha"
    show kana_side_smile at left with dissolve
    show kana_smile at char_center with dissolve
    kana "Haha, kalau gtu aku boleh ya duduk di sini"
    hide kana_side_smile with dissolve
    "Tanpa menunggu jawaban dari [mcname] pun perempuan itu duduk di sebelah [mcname]"
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    kana "Mas aku mau pesen dong"
    hide Kana_side_shy with dissolve
    hide kana_side_smile with dissolve
    hide kana_side with dissolve
    "Pikiran [mcname] dibuat bingung siapa dia"
    "Kenapa dia langsung duduk di sebelahnya"
    "Lalu kenapa dia mau duduk di situ"
    "Kenapa harus dia"
    "Banyak sekali pertanyaan yang muncul di pikiran [mcname]"
    mcname "Lah ko dia duduk di sini!!???"
    mcname "Hoooo tenang tenang tarik nafas"
    mcname "Tapi kalau di pikir pikir ini masuk akal sih karena lagi penuh juga, Jadinya dia duduk di sini"
    mcname "Tapi ko dia langsung duduk gitu aja ya?"
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    kana "Mas aku pesen stobery shortcake nya 1 ya sama lemon tea nya satu"
    kana "Es nya jangan terlalu banyak ya, makasih banyak mas"
    hide kana_side with dissolve
    show kana_embarased at char_center with dissolve
    show kana_side_embarased at left with dissolve
    kana "Eh maaf ya langsung duduk aja aku lagi kepengen cake yang ada disini cuma ada di hari tertentu aja"
    hide kana_embarased with dissolve
    hide kana_side_embarased with dissolve
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    kana "Awalnya sempet khawatir gtu kalau ga dapet tempat duduk untung aja ada"
    hide kana with dissolve
    hide kana_side with dissolve
    hide kana_embarased with dissolve
    show kana_smile at char_center with dissolve
    show kana_side_smile at left with dissolve
    kana "Makasih yaa!!"
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    kana "eh kamu anak kuliah di jekti univesity juga kan?"
    hide kana_side_smile with dissolve
    mcname "Eh ko kamu tau"
    hide kana_smile with dissolve
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    kana "Iya soalnya cuma univ kita doang yang udah selesai di jam segini"
    kana "Kalau yang lain si baru mau selesai jam 5 sore"
    kana "Jadinya aku nebak aja sih"
    kana "Jurusan kamu apa ya kalau boleh tau ?"
    hide kana_side with dissolve
    mcname "Ooo gtu ya"
    mcname "Aku masuk ke jurusan HI si"
    mcname "Kebetulan lagi pengen jalan jalan aja haha"
    hide kana with dissolve
    show kana_shy at char_center with dissolve
    show kana_side_shy at left with dissolve
    kana "Loh kita samaan dong"
    kana "Satu angkatan juga"
    hide kana_shy with dissolve
    hide kana_side_shy with dissolve
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    kana "Eh oh iya aku sampe lupa"
    $ kana_name = "Kanaia Asa"
    kana "Sebelumnya kenalin namaku Kania Asa"
    kana "Biasanya di panggil kana"
    $ kana_name = "Kana"
    hide kana_side with dissolve
    mcname "Ahh iya salam kenal juga namaku [mcname]"
    mcname "Aku dari Ngawi"
    mcname "Mungkin blum pernah denger itu agak desa soalnya haha"
    mcname "Kalau kamu dari mana [kana_name]?"
    show kana_side at left with dissolve
    kana "Ohhh, tau ko"
    kana "kalau aku sih asli orang Jakarta meski belum pernah ke daerah Ngawi tapi tau ko"
    kana "Eh cakenya udah datang bentar yaa aku makan dulu"
    hide kana_side with dissolve
    mcname "{i}Duhhh ko dia imut banget sih ya{/i}"
    mcname "{i}CANTIK BANGET LAGI{/i}"
    mcname "{i}YA TUHAN APAKAH INI YANG DIMAKSUD DENGAN NGEDATE DI CAFE?{/i}"
    mcname "{i}Emang boleh se ngedate itu?{/i}"
    hide kana with dissolve
    hide kana_side with dissolve
    "[mcname] dan [kana_name] pun fokus terhadap apa yang ada di depannya"
    "sesekali [mcname] mencuri pandangan ke arah kana dan ia pun melihat cara makan [kana_name] yang annggun yang membuat [mcname] semakin terpesona"
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    kana "Eh kamu mau juga?"
    kana "Maaf ya, daritadi aku fokus sendiri"
    kana "Soalnya aku pengennn banget makan cake ini"
    hide kana_side with dissolve
    mcname "Ehh engga ko, gak usah"
    mcname "Aku tadi udah makan, santai aja"
    mcname "Aku juga lagi bingung mau kemana"
    mcname "Kebetulan katanya di sini cafe yang di rekomendasiin sama internet"
    mcname "Jadinya pengen cobain deh"
    show kana_side at left with dissolve
    kana "Ohhh, jadi kamu ke sini karena rekomendasi internet"
    kana "Jadi kamu udah kemana aja selama ini?"
    hide kana_side with dissolve
    mcname "Ummm, belum kemana mana sih"
    mcname "Lagian aku baru datang beberapa hari yang lalu ko"
    mcname "Jadinya bingung harus kemana kamu ada rekomendasi kah?"
    hide kana_side with dissolve
    "Waktupun tidak terasa sudah malam"
    "Obrolan [mcname] & [kana_name] pun saling nyambung satu sama lain"
    "Disitu mereka pun akan saling pulang ke rumah masing masing"
    show kana_smile at char_center with dissolve
    show kana_side_smile at left with dissolve
    kana "Eh makasih ya udah dibolehin duduk di sini"
    kana "Untung aja aku bisa makan stobery shortcake nya, kalau engga keknya aku bakalan marah deh hahaha"
    hide kana_side_smile with dissolve
    show kana_scared at char_center with dissolve
    show kana_side_scared at left with dissolve
    kana "Eh udah jam segini aku harus pulang aku duluan yaa"
    hide kana_scared with dissolve
    hide kana_smile with dissolve
    hide kana_side_scared with dissolve
    show kana at char_center with dissolve
    show kana_side at left with dissolve
    kana "Kamu hati hati di jalan"
    hide kana_side with dissolve
    mcname "Haha, gpp ko santai aja kebetulan kosong"
    mcname "Owh iya sama sama"
    mcname "Kamu juga hati hati di jalan ya"
    $ quick_menu = False
    hide kana with dissolve
    scene black with dissolve
    play music "audio/bgm_harvestmoon_spring.mp3"
    scene mc bedroom with dissolve
    $ quick_menu = True
    mcname "Anjir gw ga nyangka kalau hari ini bakalan bisa ngobrol sama dia"
    mcname "Tapi di pikir pikir ternyata dia ramah juga ya"
    mcname "Kukira bakalan jadi kaya cool dan cuek gitu"
    mcname "Mana nyambung juga kalau di ajak ngobrol"
    mcname "Dah ah mending aku tidur"
    $ quick_menu = False
    jump chapter1kana2Campus

    # jump credits


label chapter1kana2Campus:
    scene black 
    show text "KEESOKAN HARINYA" with Pause(2.0)
    scene depan kampus with dissolve
    # background lift
    mcname "Ehhhh tungguuuu-"
    "[mcname] pun terburu buru karena jam sudah menunjukan untuk memasuki kuliah"
    mcname "Untung keburu buat masuk lift, makasih ya udah mau nahan liftnya"
    "{size=-5}Mahasiswi A{/size}" "Iya sama sama" 
    scene black with dissolve
    scene kelas with dissolve
    play music "audio/bgm_ngobrol_normal.mp3" fadein 1.0
    "[mcname] pun memasuki ruangan kelas yang dimana lumayan asing baginya krana ini pertama kalinya ia memasuki ruangan yang luas dan besar seperti itu selain di aula"
    "di situ dia bertemu dengan muka yang ga asing di ingatannya ada [kana_name] dan mahasiswi yang dia temui waktu di lift"
    mcname "Eh kamu kan yang tadi di lift ya?"
    mcname "Ternyata jurusan HI juga, kenalin namaku [mcname], salam kenal ya!!"
    "???" "Owh iya kita ketemuan tadi"
    "???" "Ga nyangka ternyata satu jurusan dan satu kelas juga"
    "Freya" "Namaku Freya salam kenal juga"
    mcname "Dia diliat liat imut juga ya"
    mcname "Apa si kalau kata orang orang di internet sekarang?"
    mcname "Owh iya"
    mcname "Senyumannya manis kaya karamel"
    "Dari kejauhan terdengar beberapa kalimat samar yang terdengar oleh telinga [mcname]"
    "{size=-5}Mahasiswa A{/size}" "Ehh liat dia modis banget pakeannya"
    "{size=-5}Mahasiswa B{/size}" "Iyaaa cantik banget yaa"
    "{size=-5}Mahasiswa B{/size}" "Eh bukanya dia anak orang kaya yang katanya sepupunya rektor itu ya ?"
    "{size=-5}Mahasiswa B{/size}" "Eh lo ajak ngobrol sana siapa tau bisa lo deketin"
    mcname "{i}Apaan sih mereka{/i}"
    mcname "{i}Mereka ngomongin siapa si{/i}"
    mcname "{i}Eh…ternyata mereka ngomongin yang di sebelah gw?{/i}"
    mcname "{i}Iya si pakeannya modis banget{/i}"
    mcname "{i}Ehh tunggu dia di sebelah gw ?{/i}"
    mcname "{i}Apakah ini TAKDIR hehehe{/i}"
    "[kana_name] pun menyadari bahwa di sebelahnya itu adalah [mcname] dia pun mulai tersenyum tipis, saat dia akan menyapa [mcname] suara pintu pun berbunyi"
    "Dosen memasuki ruangan kelas dan kelas pun menjadi hening dan lebih tertrib dari sebelumnya"
    "Dosen" "Selamat siang mahasiswa dan mahasiswi sekalian"
    "Dosen" "Selamat datang di mata kuliah pertama kalian di jenjang perkuliah ini"
    "Dosen" "Sebelumnya perkenalkan nama saya Fatimah"
    "Dosen" "Disini saya mengajar mata kuliah Teori Politik Indonesia, Studi Perang Dan Damai, Strategi Dan Tatakelola Strategis"
    "Dosen" "Untuk semester pertama kalian akan mempelajri mata kuliah dasar yaitu Teori Politik Indonesia"
    "Dosen" "Dengan begitu saya akan langsung ke dalam materi"
    scene black with dissolve
    "Tidak terasa bahwa waktu telah berlalu selama 40 menit, hal ini menunjukan bahwa matkul sudah akan berakhir dan mata kuliah untuk hari ini sudah tidak ada lagi"
    scene kelas with dissolve
    "Dosen" "Baiklah semuanya karena waktu saya sudah habis"
    "Dosen" "Maka mata kuliah hari ini sudah selesai"
    "Dosen" "Tapi sebelum itu saya akan memberikan tugas kelompok yang ber isikan 4 orang saja"
    "Dosen" "Minggu depan di kumpulkan ya!!"
    "Dosen" "Untuk kelompoknya akan dibagi berdasarkan jajaran tempat duduk kalian saja agar tidak ribut dan tidak ada circle diantara kalian semua"
    "Dosen" "Lalu gunakan kesempatan ini untuk berkenalan dengan teman teman sekelas kalian"
    "Dosen" "Sekian untuk hari ini terimakasih banyak"
    mcname "{i}Aduh, satu jajaran!!??{/i}"
    mcname "{i}Tunggu bentar, kalau satu jajar??{/i}"
    mcname "{i}Eh gw sama cewek itu cuyyyy!!!{/i}"
    mcname "{i}Eh halo [kana_name] satu kelompok juga mohon bantuannya{/i}"
    play music "audio/Dreamcatcher.mp3"
    jump credits

