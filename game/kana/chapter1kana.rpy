label chapter1kana1:
    $ renpy.block_rollback()
    play music "audio/BGM_Kampus.mp3" loop fadein 1.0
    scene awan with Dissolve(2.0)
    "Walaupun ini sudah pertengahan tahun"
    "Matahari secara terik menerangi kota Jakarta"
    "Saat melihat ke atas langit, hanya langit biru lah yang terlihat"
    scene depan kampus with Dissolve(2.0)
    $ quick_menu = True
    mcname "Untung saja masih sempat untuk ikut orientasi"
    mcname "Gak nyangka di Jakarta ternyata beneran macet parah"
    mcname "Yah walaupun begitu ini memang pengalaman baru yang aku rasakan"
    mcname "Berbeda jauh dari tempatku dulu"
    mcname "Huuuu, ini hari pertamaku orientasi di Jeketi University"
    mcname "Di sini tempat dimana aku bakalan kenal sama orang baru, temen baru, atau bahkan jodoh heheh"
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(2.0)
    play audio "audio/open_door.mp3" fadeout 1.0
    # show text "{color=#FFF}SFX PINTU DIBUKA{/color}" with Pause(1.0)
    show text "{color=#FFF}MEMASUKI AULA{/color}" with Pause(2.0)
    play music "audio/BGM_Kampus.mp3" loop fadein 1.0
    scene kelas with Dissolve(2.0)
    $ quick_menu = True
    "Saat memasuki ruangan [mcname] mendengar suara di aula yang sangat ramai"
    mcname "Seperti yang diharapkan dari kampus Ibu Kota"
    mcname "Orangnya rame banget"
    "Terlihat di dalam aula sudah diisi dengan mahasiswa baru."
    mcname "{i}Well, kayaknya aku harus mencari tempat duduk yang kosong sebelum penuh.{/i}"
    "[mcname] melihat tempat duduk yang berada di pojok atas ruangan."
    mcname "{i}Ah sepertinya itu tidak ada orang.{/i}"
    "Saat sampai di sana, tidak terlihat orang di barisan tersebut"
    mcname "{i}Hmmm... tumben di bagian belakang kosong{/i}"
    mcname "{i}Padahal biasanya orang pada seneng di belakang{/i}"
    "[mcname] kemudian duduk di kursi tersebut."
    mcname "{i}Tapi lumayan juga dapet duduk di sini{/i}"
    mcname "{i}Jadinya aku bisa ngeliat yang lain dengan jelas.{/i}"
    "Saat memperhatikan di sekitar"
    "[mcname] mendengar suatu topik yang menarik perhatiannya."
    "{size=-5}Mahasiswa A{/size}" "Eh eh liat deh itu kan mahasiswi itu"
    "{size=-5}Mahasiswa B{/size}" "Yang mana sih?"
    mcname "{i}Hmmm? Apa yang sedang mereka bicarakan{/i}"
    "{size=-5}Mahasiswa A{/size}" "ituuu, yang ituu tuhh"
    "Mahasiswa tersebut memberikan kode kepada temannya ke arah seorang cewek"
    "Pembicaraan mereka yang cukup keras membuat [mcname] pun melirik ke arah orang yang menjadi bahan pembicaraan"
    $ quick_menu = False
    scene kana awal with Dissolve(2.0)
    # Ganti Backsound
    $ quick_menu = True
    "{size=-5}Mahasiswa B{/size}" "Ohhh dia!!"
    "{size=-5}Mahasiswa B{/size}" "Eh bukannya dia mahasiswa yang….bla bla bla"
    "Terpesona terhadap cewek tersebut"
    "[mcname] tidak mendengarkan pembicaraan Mahasiswa tadi"
    "Di sana terlihat seorang cewek cantik yang terlihat seumuran dengan [mcname]"
    "Rambutnya biru yang mana mengingatkannya dengan lautan yang berada di kampung halamannya"
    "Matanya pun tidak kalah indah dengan batu sapphire"
    "(……)"
    mcname "{i}Aku tidak bisa melepaskan mataku dari dia{/i}"
    mcname "{i}Oh...{/i}"
    mcname "{i}Dia siapa?{/i}"
    "[mcname] bertanya kepada dirinya sendiri"
    mcname "{i}Tapi memang benar jika dilihat, dia memberikan aura seorang gadis cantik yang anggun dan kalem.{/i}"
    mcname "{i}Ko ada ya orang secantik dia?{/i}"
    mcname "{i}Atau… memang semua orang dari kota itu kaya gitu{/i}"
    "[mcname] pun melihat ke sekelilingnya, berusaha membandingkan dengan cewek yang ada di ruangan"
    mcname "{i}Hmmm emang sih, hampir semua kelihatan cantik…{/i}"
    mcname "{i}Tapi kok cuma dia ya, yang jadi perhatian orang-orang.{/i}"
    mcname "{i}Ya termasuk aku juga sih{/i}"
    "(……)"
    "1….2….3…"
    "8…9…10…"
    "Menit telah berlalu dan [mcname] masih menatap cewek tersebut"
    "Mungkin itu adalah rekor terlama [mcname] dalam memperhatikan seseorang"
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play audio "audio/handbell.mp3"
    show text "{color=#FFF}*DING DING DING DING*\n(screenshake){/color}" with Pause(2.0)
    play music "audio/BGM_Kampus.mp3" loop fadein 1.0
    scene kelas with dissolve
    $ quick_menu = True
    mcname "Ehhh… udah bel, serius??? Lama banget berarti aku liatin dia"
    mcname "Moga aja dia gak sadar deh kalo aku ngeliatin dia terus"
    mcname "Kalo misalnya ketahuan maaf banget dah."
    "Terdengar suara pintu terbuka dan seluruh perhatian tertuju kepada sumber suara tersebut"
    play audio "audio/open_door.mp3" fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(2.0)
    scene kelas with dissolve
    $ quick_menu = True
    play music "audio/BGM_Dosen + Rektor.mp3" fadein 1.0
    "Rektor" "Selamat datang Mahasiswa baru yang memasuki Jekiti University…"
    "Perkataan sambutan dari Rektor dan jajaran Dosen membuat [mcname] dan beberapa Mahasiswa/i lain merasa bosan"
    "Seakan mendukung perkataan [mcname], beberapa mahasiswa/i pun ada yang bermain HP, mengobrol, atau bahkan bercanda"
    "{size=-5}Mahasiswa A{/size}" "Eh bosenin bet dah, template banget ini ucapan selamat datangnya tuh, bikin ngatuk ya ga ?"
    "{size=-5}Mahasiswa B{/size}" "Iyaa njirr, bener banget dah mending kita login yuk P MABAR MABAR"
    "{size=-5}Mahasiswa C{/size}" "Gas kali ya login"
    "[mcname] pun tidak sengaja mengalihkan pandangannya kepada perempuan tadi yang juga tertawa kecil karena mendengar obrolan mahasiswa tersebut."
    mcname "{i}Astaga, aku tidak menyangka ternyata ada perempuan semanis dia{i}"
    "(……)"
    "Mata [mcname] dan perempuan itu tidak sengaja bertemu."
    "[mcname] pun langsung mengalihkan pandangannya karena tersipu malu."
    mcname "{i}Waduh mata kita gak sengaja bertemu pula{/i}"
    mcname "{i}Semoga aja aku gak dikira orang aneh sama dia.{/i}"
    "(……)"
    $ quick_menu = False 
    scene black with Dissolve(2.0)
    scene kelas with dissolve
    $ quick_menu = True 
    "[mcname] meregangkan badannya yang terasa kaku akibat duduk terlalu lama"
    mcname "{i}Akhirnya selesai juga sambutan dan kegiatan hari ini{/i}"
    mcname "{i}Hari ini lumayan cape juga ya.{/i}"
    mcname "{i}Tapi masih ada energi sih…{/i}"
    # insert cg kana
    $ quick_menu = False
    scene kana awal with Dissolve(2.0)
    scene kelas with dissolve
    $ quick_menu = True
    mcname "{i}Eh masih jam segini nih{/i}"
    mcname "{i}Enaknya buat habisin waktu, mending aku ke…{/i}"
    $ quick_menu = False
    menu:
        "Mau Kemana?"
        "A. Ke Kosan":
            "Kamu habisin waktu di kosan dan memilih buat istirahatin diri daripada pergi kesana kemari"
            $ kana_name = "Perempuan itu"
            stop music fadeout 1.0
            jump chapter1kana2Campus
        "B. Ke Warteg":
            "Kamu milih makan ke warteg dan di situ ternyata wartegnya pake boraks dan akhirnya kamu masuk rumah sakit"
            scene black with dissolve
            show text "{color=#FFF}MAKANYA JANGAN MAKAN SEMBARANG BROO KAN MASUK RUMAH SAKIT{/color}" with Pause(2.0)
            show text "{color=#FFF}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
            play music "audio/Dreamcatcher.mp3"
            jump credits
        "C. Ke Cafe":
            $ quick_menu = False
            stop music fadeout 1.0
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
    # show screen cinematicTalk
    show kana_side_shy at left with dissolve
    show black at showBlackTop
    show black as black2 at showBlackBottom
    show kana_shy at kana_near with dissolve
    kana "H-halooo, maaf tapi apa kursinya kosong ?"
    # hide screen cinematicTalk with dissolve
    hide kana_side_shy with dissolve
    hide black with dissolve
    hide black2 with dissolve
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
    hide kana_scared
    hide kana_smile
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
    stop music fadeout 1.0
    $ quick_menu = False
    jump chapter1kana2Campus

    # jump credits


label chapter1kana2Campus:
    $ renpy.block_rollback()
    scene black with dissolve
    show text "KEESOKAN HARINYA" with Pause(2.0)
    play music "audio/BGM_Kampus.mp3" fadein 1.0
    scene depan kampus with Dissolve(2.0)
    $ quick_menu = True
    "*STEP STEP STEP STEP*"
    "Terdengar suara langkah kaki yang terburu-buru"
    mcname "{i}Sial ternyata aku benar-benar meremehkan Jakarta{/i}"
    mcname "{i}Siapa sangka macet di sini parah banget{/i}"
    "Takut terlambat di hari pertama, [mcname] terburu-buru memasuki kelas kuliahnya"
    # background lift
    mcname "Ehhhh tungguuuu-"
    "[mcname] berlari menuju Lift yang mau tertutup"
    "Di dalam lift terlihat seorang cewek yang sepertinya juga mau menuju ke kelas"
    "*DING*"
    mcname "Huft… huft… huft."
    mcname "Untung keburu buat masuk lift"
    mcname "Makasih ya udah mau nahan liftnya"
    show freya at char_center with dissolve
    show freya_side at left with dissolve
    freya "Haha iya, sama-sama"
    hide freya_side with dissolve
    "Sibuk menarik nafas dari olahraga pagi yang tidak direncanakan tadi"
    "[mcname] tidak terlalu memperhatikan perempuan yang ada di lift."
    mcname "Huft... huft...."
    mcname "Kayaknya aku harus ningkatin lagi nih, stamina ku ini"
    "Setelah mendapatkan cukup oksigen"
    "[mcname] mencoba melirik perempuan yang ada di dalam lift."
    mcname "{i}Memang ya, cewek di Jakarta ini cantik-cantik semua{/i}"
    "DING"
    "Pintu lift terbuka"
    mcname "Ah! Terima kasih lagi yak, sudah menahan lift tadi"
    "[mcname] kemudian lanjut berlari menuju kelas"
    hide freya with dissolve
    $ quick_menu = False
    scene black with Dissolve(2.0)
    scene kelas with dissolve
    play music "audio/bgm_ngobrol_normal.mp3" fadein 1.0
    $ renpy.block_rollback()
    $ quick_menu = True
    "[mcname] pun memasuki ruangan kelas."
    "Ini pertama kalinya ia memasuki ruangan yang luas dan besar seperti itu, selain di aula."
    mcname "{i}Fiuhh. Untung aja kelasnya belum dimulai{/i}"
    "[mcname] pun melihat ke sekeliling kelas"
    "akan tetapi"
    mcname "{i}Loh kok masih sepi kelasnya yah?{/i}"
    "Dikarenakan masih banyak kursi yang kosong"
    "[mcname] memilih untuk duduk di bagian belakang terlebih dahulu agar dekat dengan pintu keluar-masuk dan tidak ingin mencolok untuk hari-hari pertama ini."
    "Saat [mcname] akan duduk"
    "Terdengar suara perempuan yang membuatnya langsung melihat ke belakang"
    show freya at char_center with dissolve
    show freya_side at left with dissolve
    freya "Kok buru-buru amat?"
    freya "Santai aja napa?"
    freya "Lagian masih jam segini"
    freya "Atau…"
    show freya_smug at char_center with dissolve
    show freya_side_smug at left with dissolve
    freya "Kamu ngincer posisi paling depan, nih? Haha"
    hide freya
    hide freya_side
    hide freya_side_smug with dissolve
    "[mcname] pun sadar bahwa perempuan itu adalah perempuan yang sama yang telah menahan pintu lift untuknya"
    mcname "Hahh, astagaa"
    mcname "Aku kira udah mulai loh kelasnya"
    mcname "Aku sampe lari-lari kan tadi?"
    mcname "Eh kamu kan yang tadi di lift ya?"
    mcname "Aduhh, ya udah deh yang penting datang aja dulu"
    "Perempuan itu tersenyum kecil dan manis"
    show freya_smile at char_center with dissolve
    show freya_side_smile at left with dissolve
    freya "Hahaha, makanya tadi aku liat kamu lari-lari lucu banget deh"
    freya "Kok bisa sih, ada orang yang langsung lari-lari gitu padahal masih hari pertama"
    "[mcname] melihat ke arah jam tangannya dan ia pun sadar"
    hide freya_side_smile with dissolve 
    mcname "Aduhhh pantes aja aku lari-lari, jam tanganku mati. Ku kira udah telat"
    show freya_side_smile with dissolve
    freya "Haha ada-ada deh kamu. Lain kali pastiin aja dulu deh."
    hide freya_side_smile with dissolve
    mcname "Eh dari tadi kita ngobrol belum kenalan ternyata"
    mcname "Boleh kali ya, kita kenalan dulu haha."
    mcname "Kenalin namaku [mcname]"
    mcname "Aku dari Ngawi"
    mcname "Salam kenal, ya"
    $ freya_name = "Freya"
    freya "Eh, salam kenal juga namaku Freya asalku dari Yogyakarta"
    mcname "{i}Dia ternyata imut juga ya{/i}"
    mcname "{i}Apa sih, kalau kata orang-orang di internet sekarang.{/i}"
    mcname "{i}Owh iya!{/i}"
    mcname "{i}Senyumannya manis kaya karamel{/i}"
    hide freya_smile with dissolve
    if kana_name == "Perempuan itu":
        "Saat mengobrol, para Mahasiswa/i pun terdengar mulai memasuki ruangan kelas"
        "Seorang perempuan pun duduk di sebelah Freya dan dilihat oleh [mcname]"
        "Ternyata perempuan itu adalah perempuan yang menjadi bahan pembicaraan saat pembukaan Mahasiswa/i baru"
        "Saat itu pun, Freya terlihat akrab dengan perempuan tersebut dan [mcname] memilih untuk tidak mencampuri urusan mereka"
        "Akan tetapi, dari kejauhan terdengar beberapa kalimat samar yang terdengar oleh telinga [mcname]"
    else:
        "Saat mengobrol, para Mahasiswa/i pun terdengar mulai memasuki ruangan kelas"
        "Seorang perempuan pun duduk di sebelah Freya dan dilihat oleh [mcname]"
        "Ternyata perempuan itu adalah [kana_name] perempuan yang menjadi bahan pembicaraan saat pembukaan Mahasiswa/i baru"
        "Saat itu pun, Freya terlihat akrab dengan [kana_name]. Sehingga [mcname] memilih untuk tidak mencampuri urusan mereka"
        "Akan tetapi, dari kejauhan terdengar beberapa kalimat samar yang terdengar oleh telinga [mcname]"
    "{size=-5}Mahasiswa A{/size}" "Ehh liat dia modis banget pakaiannya"
    "{size=-5}Mahasiswa B{/size}" "Iyaaa cantik banget yaa"
    "{size=-5}Mahasiswa B{/size}" "Eh bukanya dia anak orang kaya yang katanya sepupunya rektor itu ya?"
    "{size=-5}Mahasiswa B{/size}" "Eh lo ajak ngobrol sana siapa tau bisa lo deketin"
    if kana_name == "Perempuan itu":
        mcname "{i}Mereka ngobrolin perempuan di sebelah Freya, ya?{/i}"
        mcname "{i}Tapi kalau dilihat-lihat, memang modis sih pakaiannya.{/i}"
        mcname "{i}Dia juga kenal deket sama Freya, ya?{/i}"
        "Perempuan itu pun menyadari bahwa di sebelahnya Freya itu adalah [mcname] dan akhirnya senyum tipis muncul dari wajahnya."
        play audio "audio/open_door.mp3"
        "Tiba-tiba, suara pintu pun berbunyi"
    else:
        mcname "{i}Mereka ngobrolin [kana_name], ya?{/i}"
        mcname "{i}Tapi kalau dilihat lihat, memang modis sih pakaiannya{/i}"
        mcname "{i}Dia juga kenal deket sama Freya, ya?{/i}"
        "[kana_name] pun menyadari bahwa di sebelahnya Freya itu adalah [mcname] dan akhirnya senyum tipis muncul dari wajahnya."
        play audio "audio/open_door.mp3"
        "Saat dia akan menyapa [mcname], suara pintu pun berbunyi."
    "Dosen pun memasuki ruangan kelas"
    "Kelas pun menjadi tenang dan lebih tertib dari sebelumnya"
    "Dosen memasuki ruangan kelas dan kelas pun menjadi hening dan lebih tertrib dari sebelumnya"
    "Dosen" "Selamat siang mahasiswa dan mahasiswi sekalian"
    "Dosen" "Selamat datang di mata kuliah pertama kalian di jenjang perkuliah ini"
    "Bu Fatimah" "Sebelumnya perkenalkan nama saya Fatimah"
    "Bu Fatimah" "Disini saya mengajar mata kuliah Teori Politik Internasional, Studi Perang Dan Damai, Strategi Dan Tatakelola Strategis"
    "Bu Fatimah" "Untuk semester pertama kalian akan mempelajari mata kuliah dasar yaitu Teori Politik Internasional"
    "Bu Fatimah" "Dengan begitu saya akan langsung ke dalam materi"
    "Suasana kelas pun terasa hening, fokus untuk memperhatikan apa yang dijelaskan oleh Bu Fatimah"
    $ quick_menu = False
    scene black with Dissolve(2.0)
    scene kelas with dissolve
    $ quick_menu = True
    "Bu Fatimah" "Baiklah semuanya karena waktu saya sudah habis"
    "Bu Fatimah" "Maka mata kuliah hari ini sudah selesai"
    "Terdengar suara lega dari para mahasiswa"

    "Bu Fatimah" "Tapi sebelum itu"
    "Bu Fatimah" "Saya akan memberikan tugas kelompok yang berisikan 4 orang"
    "Bu Fatimah" "Minggu depan di kumpulkan ya!!"
    "Mendengar hal tersebut, para mahasiswa mengeluarkan suara kekecewaan"

    "Bu Fatimah" "Jadi kelompoknya akan dibagi berdasarkan jajaran tempat duduk kalian saja agar simple dan tidak ada circle diantara kalian semua"
    "Bu Fatimah" "Lalu gunakan kesempatan ini untuk berkenalan dengan teman - teman sekelas kalian"
    "Bu Fatimah" "Sekian untuk hari ini"
    "Bu Fatimah" "Terimakasih banyak"
    mcname "{i}Aduh, satu jajaran!!??{/i}"
    mcname "{i}Tunggu bentar, kalau satu jajar…??,{/i}"
    "*SFX LIRIK KANAN KIRI*"
    if kana_name == "Perempuan itu":
        mcname "Eh, aku sama cewek itu!!!"
    else:
        mcname "Eh, aku sama [kana_name]!!!"
    "Eh, halo. Kita satu kelompok, ya. Mohon bantuannya"
    "Freya" "Eeh, iyaa. Kita satu kelompok, nih. Kebetulan banget, ya. Haha"
    show kana at char_placement with dissolve
    show kana_side at left with dissolve
    $ kana_name = "???"
    kana "Halo Kita satu kelompok ya?"
    $ kana_name = "Kana"
    kana " Mohon bantuannya, ya. Sebelumnya, kenalkan namaku [kana_name]"
    kana "Eh, kamu sini dong. Kan kita juga satu kelompok"
    hide kana_side with dissolve
    "Mahasiswa C" "Owh iya. Siang semuanya"
    "Mahasiswa C" " Sebelumnya, kenalin nama gw Donatur"
    "Mahasiswa C" "Gw dari Pekalongan. Salam kenal"
    hide kana with dissolve
    "Freya, [kana_name], [mcname], dan (Donatur) pun saling bertukar sapa dan mengobrol lebih lanjut. Akhirnya, mereka pun membuat grup chat untuk membahas pekerjaan kelompok mereka."
    $ quick_menu = False
    scene black with Dissolve(2.0)
    scene bedroom with dissolve
    $ renpy.block_rollback()
    $ quick_menu = True 
    "Setelah [mcname] sampai Kos nya"
    "[mcname] pun membuang tasnya ke lantai lalu melepaskan sepatu dan menghempaskan tubuhnya ke kasur"
    "Setelah capek dengan kegiatan hari ini"
    "datang ke kos membuat [mcname] merasakan ketenangan di balik hiruk pikuk Kota Jakarta"
    "Memejamkan mata, menghela nafas, dan merenungkan kembali kegiatan yang telah terjadi hari ini"
    play audio "audio/ReceiveText.ogg"
    "(Notif WA)"
    mcname "(...)"
    play audio "audio/ReceiveText.ogg"
    "(Notif WA)"
    mcname "Duh. Notif WA nih"
    mcname "Apa nih? Dari Mamah, kah?"
    "[mcname] mencoba mengecek HP nya"
    mcname "{i}Oh, ternyata bukan.{/i}"
    mcname "{i}Ini notif dari grup chat itu, ternyata{/i}"
    $ quick_menu = False
    jump phoneChat
    # play music "audio/Dreamcatcher.mp3"
    # jump credits

label chapter1kana3:
    scene black with Dissolve(2.0)
    show text "{color=#FFF}KEESOKAN HARINYA{/color}" with Pause(2.0)
    scene kantin with Dissolve(2.0)
    "Kantin Jeketi University, dimana tempat para mahasiswa melepaskan lapar dan haus sehabis belajar seharian"
    "Karena sudah jam makan siang"
    "Suasana kantin terasa sangat ramai dan tempat duduk pun terlihat hampir penuh diisi oleh para mahasiswa"
    mcname "{i}Wahhhh, rame juga ya{/i}"
    mcname "{i}Mungkin karena sudah jam makan siang??{/i}"
    mcname "{i}Bentar. Kalau gini caranya, gimana dapet tempat duduk?{/i}"
    mcname "{i}Masa aku harus bungkus makanannya, sih?{/i}"
    mcname "{i}Perdana makan di kantin, ga enak rasanya kalo dibungkus.{/i}"
    "Merasa kecewa, [mcname] pun berniat untuk pergi mencari makanan di tempat lain"
    "Saat [mcname] ingin melangkah pergi, ia melihat seseorang yang melambaikan tangannya dari kejauhan seakan memanggilnya."
    "Setelah diperhatikan lagi, ternyata itu adalah Freya"
    "Freya" "[mcname] SINI!!!"
    "Freya" "Duduk bareng kita!!"
    "Mendengar hal tersebut akhirnya MC menghampiri ke meja Freya Di sana ternyata ada [kana_name] yang juga duduk di sampingnya."
    "Freya" "Eh sini."
    "Freya" "Duduk di sini"
    "Freya" "Soalnya udah rame juga kan?"
    "Freya" "Gapapa kan nay?"
    kana "Iya. Gapapa kok. Lagian di sini kosong."
    "Mendengar persetujuan mereka, dengan lega [mcname] duduk berhadapan dengan mereka"
    mcname "Akhirnya dapat juga"
    mcname "Makasih banget loh. Aku kira aku gak bakalan dapet tempat"
    play music "audio/Dreamcatcher.mp3"
    jump credits
