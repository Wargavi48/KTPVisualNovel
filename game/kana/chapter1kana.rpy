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
    scene black with Dissolve(2.0)
    play sound "audio/open_door.mp3" fadeout 1.0
    show text "{color=#FFF}MEMASUKI AULA{/color}" with Pause(2.0)
    scene kelas with Dissolve(2.0)
    $ quick_menu = True
    play sound "audio/crowd_noise.mp3" fadein 1.0
    "Saat memasuki ruangan [mcname] mendengar suara di aula yang sangat ramai"
    mcname "Seperti yang diharapkan dari kampus Ibu Kota"
    mcname "Orangnya rame banget"
    "Terlihat di dalam aula sudah diisi dengan mahasiswa baru."
    mcname "{i}Hmmm... kayaknya aku harus mencari tempat duduk yang kosong sebelum penuh.{/i}"
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
    stop sound fadeout 1.0
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
    play sound "audio/handbell.mp3" fadein 1.0
    show text "{color=#FFF}*DING DING DING DING*\n(screenshake){/color}" with Pause(2.0)
    play music "audio/BGM_Kampus.mp3" loop fadein 1.0
    scene kelas with dissolve
    $ quick_menu = True
    stop sound fadeout 1.0
    mcname "Ehhh… udah bel, serius??? Lama banget berarti aku liatin dia"
    mcname "Moga aja dia gak sadar deh kalo aku ngeliatin dia terus"
    mcname "Kalo misalnya ketahuan maaf banget dah."
    "Terdengar suara pintu terbuka dan seluruh perhatian tertuju kepada sumber suara tersebut"
    play sound "audio/open_door.mp3" fadeout 1.0
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
    scene kana awal senyum with Dissolve(2.0)
    mcname "{i}Aduh! Kok aku ga bisa hilangkan senyuman itu dari kepalaku ya?{/i}"
    scene black with dissolve
    scene kelas with Dissolve(2.0)
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
            # jump chapter1kana2Campus
            jump chapter1kana2kos
        "B. Ke Warteg":
            "Kamu milih makan ke warteg dan di situ ternyata wartegnya pake boraks dan akhirnya kamu masuk rumah sakit"
            scene black with dissolve
            show text "{color=#FFF}MAKANYA JANGAN MAKAN SEMBARANG BROO KAN MASUK RUMAH SAKIT{/color}" with Pause(2.0)
            show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
            play music "audio/Dreamcatcher.mp3"
            jump credits
        "C. Ke Cafe":
            $ quick_menu = False
            stop music fadeout 1.0
            scene black with dissolve
            jump chapter1kana2Cafe
            
label chapter1kana2kos:
    $ renpy.block_rollback()
    scene black with dissolve
    scene mc bedroom with dissolve
    play music "audio/BGM_Kosan 2.mp3" fadein 1.0
    $ quick_menu = True
    "Kamu habisin waktu di kosan dan memilih untuk beristirahat dibanding pergi kesana kemari"
    "Pulang dari kampus, [mcname] masih memikirkan kejadian yang dialaminya hari ini"
    mcname "{i}Lumayan capek ya orientasinya{/i}"
    mcname "{i}Ternyata panas banget di Jakarta{/i}"
    show kana at kana_near with dissolve
    mcname "{i}Aku gak nyangka bisa bertemu sama perempuan sebersinar itu{/i}"
    mcname "{i}Tapi dilihat - lihat, kayanya dia ramah ya{/i}"
    mcname "{i}Aku kira, dia bakalan kaya cool dan cuek gitu{/i}"
    mcname "{i}Udah ah mending aku tidur{/i}"
    "[mcname] pun tertidur dengan lelap"
    $ quick_menu = False
    stop music fadeout 1.0
    jump chapter1kana2Campus

label chapter1kana2Cafe:
    $ renpy.block_rollback()
    scene cafe with dissolve
    play music "audio/BGM_Cafe Cerah.mp3" fadein 1.0
    $ quick_menu = True
    "[mcname] memilih untuk menghabiskan waktu di sebuah cafe. Awalnya cafe itu terasa sepi, tetapi lama - lama cafe tersebut mulai penuh"
    mcname "Wah makin lama, makin rame ya cafe ini. Memang salah satu cafe terkenal sih, kalau kata internet..."
    "Banyak sekali orang yang berlalu lalang. Akan tetapi, ada satu orang yang menarik perhatian [mcname]"
    show kana at char_center with dissolve
    "Saat orang itu mendekati pintu cafe, [mcname] pun menyadari bahwa orang itu adalah cewek yang ada di kampus tadi."
    mcname "{i}Loh, itu kan perempuan yang tadi di kampus?{/i}"
    mcname "{i}Kita datang di cafe yang sama{/i}"
    mcname "{i}Kebetulan macam apa ini?{/i}"
    "Secara tidak sadar [mcname] pun melihat ke arah perempuan tersebut. Mungkin karena dia berdiam diri cukup lama, yang membuat beberapa pelanggan pun melihat ke arah nya"
    "Tetapi, perempuan itu terlihat sedang kebingungan"
    "Pandangannya yang melihat ke sana kemari dan gerak tubuhnya yang menunjukan dirinya gelisah, membuat [mcname] pun berpikir."
    mcname "{i}Hmmm kenapa ya, kok dari tadi dia kaya gelisah gitu??{/i}"
    "Mereka pun secara tidak sengaja bertukar pandangan"
    "Reflek, [mcname] pun memalingkan pandangannya"
    mcname "{i}Duh mata kita gak sengaja ketemu pula{/i}"
    mcname "{i}Perempuan itu pun mendekati meja tempat MC berada{/i}"
    show kana at kana_near with dissolve
    show kana_side at left with dissolve
    kana "H-halooo, maaf tapi apa kursinya kosong?"
    hide kana_side with dissolve
    mcname "Eh iya ini kosong kok kebetulan dari tadi ga ada yang nempatin takut kali ya sama aku haha"
    mcname "{i}Aduh sial ngomong apaan sih aku, garing banget lagi jokes nya{/i}"
    show kana_smile at kana_near with dissolve
    show kana_side_smile at left with dissolve
    kana "Haha…"
    kana "Kalau gitu aku boleh ya duduk di sini "
    "Cewek itu pun tersenyum manis"
    hide kana_side_smile with dissolve
    hide kana_smile with dissolve
    "Tanpa menunggu jawaban dari [mcname], perempuan itu pun duduk di sebelah [mcname]"
    "Mengangkat tangan untuk memanggil pelayan. Perempuan itu kemudian memesan pesanannya"
    show kana_side at left with dissolve
    kana "Mas aku mau pesen dong"
    hide kana_side with dissolve
    "(...)"
    "Pikiran [mcname] dibuat bingung dengan siapa dia kenapa dia langsung duduk di sebelahnya lalu kenapa dia mau duduk di situ, kenapa harus dia, banyak sekali pertanyaan yang muncul di pikiran [mcname]"
    show kana_side at left with dissolve
    kana "Mas aku pesan strawberry shortcake nya 1 ya, sama lemon tea nya satu, es nya jangan terlalu banyak ya, makasih banyak mas…"
    hide kana_side with dissolve
    "Pelayan cafe itu pun pergi untuk memproses pesanan Kana"
    show kana_clumsy at kana_near with dissolve
    show kana_side_clumsy at left with dissolve
    kana "Eh maaf ya langsung duduk aja"
    kana "Soalnya aku lagi kepengen banget cake yang ada disini karena cuma ada di hari tertentu aja"
    kana "Hahahaha"
    hide kana_clumsy with dissolve
    hide kana_side_clumsy with dissolve
    show kana_side at left with dissolve
    kana "Aku awalnya sempat khawatir gitu kalau nanti ga dapet tempat duduk gimana"
    kana "Untung aja ada tempat duduk disebelahmu ini"
    show kana_smile at kana_near with dissolve
    hide kana_side
    show kana_side_smile at left with dissolve
    kana "Makasih ya udah diizinin duduk di sini"
    hide kana_smile with dissolve
    hide kana_side_smile 
    show kana_side at left with dissolve
    $ kana_name = "Kanaia Asa"
    kana "Oh iya kenalin dulu nih namaku [kana_name] biasanya dipanggil Kana"
    $ kana_name = "Kana"
    hide kana_side with dissolve
    mcname "Aku [mcname] salam kenal ya"
    show kana_side at left with dissolve
    kana "Ohhh [mcname] salam kenal juga ya"
    kana "Udah lama duduk di cafe ini?"
    hide kana_side with dissolve
    mcname "Lumayan sih, pas awal dateng soalnya masih agak sepi"
    show kana_side at left with dissolve
    kana "Oh tadi sepi ya, agak telat berarti aku dateng haha"
    hide kana_side with dissolve
    mcname "Hahahaha"
    "Tidak lama kemudian datang pelayan cafe yang membawa pesanan yang dipesan [kana_name]"
    "Pelayan" "Maaf menunggu"
    "Pelayan" "Ini ya kak pesanan strawberry shortcake sama lemon tea nya"
    "Pelayan meletakan pesanan ke atas meja"
    show kana_side at left with dissolve
    kana "Eh cakenya sudah datang aku makan dulu ya"
    hide kana_side with dissolve
    "(...)"
    mcname "{i}Aduh gimana nih, bisa-bisa nya pas aku lagi pengen santai gini malah duduk barengan sama cewek{/i}"
    "Tidak ingin dikira aneh akhirnya [mcname] pun melanjutkan menikmati pesanannya"
    "[mcname] dan [kana_name] fokus terhadap apa yang ada di depannya, sesekali [mcname] melirik ke arah [kana_name]"
    show kana_side at left with dissolve
    kana "Ummm, kamu mau juga?"
    hide kana_side with dissolve
    "Mungkin sadar kalau [mcname] memperhatikannya, Kana menawarkan cake yang sedang ia makan"
    mcname "Eh engga kok haha"
    "Mendengar hal tesebut Kana lanjut memakan cake nya"
    "Karena moment nya cangung, [mcname] melihat sekeliling untuk mencari topik yang dibahas namun hasilnya nihil, tidak ada sesuatu yang menarik untuk dibahas di dalam cafe"
    "(...)"
    mcname "Ternyata kamu suka banget strawberry shortcakenya, ya?"
    "Melihat Kana fokus memakan cake [mcname] mencoba membawa topik strawberry shortcake"
    show kana_side at left with dissolve
    kana "I - iyah"
    hide kana_side with dissolve
    "(....)"
    "Kehabisan topik lagi"
    mcname "Pelayann! Pesan strawberry shortcake 1"
    "Mencoba untuk menghilangkan canggung, akhirnya [mcname] memesan makanan lagi"
    "Bingung karena [mcname] memesan lagi, Kana melihat bolak balik antara [mcname] dan pelayan"
    "Menyadari kana yang kebingungan, [mcname] pun memberikan alasannya"
    mcname "Ngeliat kamu makan enak banget. Jadinya penasaran mau coba, hehe."
    show kana_side at left with dissolve
    kana "Eh…. padahal udah ditawarin, tadi."
    hide kana_side with dissolve
    mcname "Hahaha"
    "Pelayan" "Maaf menunggu"
    "Pelayan" "Ini ya kak pesanannya strawberry shortcake"
    "Melihat cake yang diletakkan di atas meja tampak menggiurkan"
    "[mcname] pun memasukkan potongan strawberry shortcake ke mulutnya"
    "Tiba tiba [mcname] pun merasakan sensasi yang belum pernah dia rasakan sebelumnya, Rasa manis dan asam stroberi seakan menari di lidahnya, memberikan kenikmatan yang tak tertandingi."
    "Setiap gigitan membawa [mcname] ke dalam dunia yang penuh dengan kebahagiaan sederhana. [mcname] pun menutup matanya, membiarkan rasa itu menyelimutinya sepenuhnya"
    mcname "Hmmmmm enak juga ya"
    show kana_side at left with dissolve
    kana "Ya kannn? Makanya aku pengen banget makan di sini."
    hide kana_side with dissolve
    mcname "Makanya tadi kamu langsung duduk di bangku yang kosong, ya?"
    show kana_embarased at kana_near with dissolve
    show kana_side_embarased at left with dissolve
    kana "Hehehe"
    hide kana_side_embarased with dissolve
    mcname "Tapi makasih, loh. Berkat kamu, aku jadi tau enaknya strawberry shortcake ini."
    hide kana_embarased with dissolve
    show kana_side at left with dissolve
    kana "Aku juga mau bilang makasih lagi, ya. Aku jadi bisa makan di sini hari ini"
    hide kana_side with dissolve
    "[mcname] dan Kana pun saling melemparkan senyuman sambil menikmati strawberry shortcake di cafe tersebut"
    mcname "(...)"
    kana "(...)"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    scene cafe with dissolve
    play music "audio/BGM_Cafe Sore.mp3" fadein 1.0
    $ quick_menu = True 
    "Waktu Pun tidak terasa sudah malam, dan obrolan [mcname] & Kana pun saling nyambung satu sama lain"
    "Akhirnya, tibalah waktu mereka pulang ke rumah masing masing"
    show kana at kana_near with dissolve
    show kana_side at left with dissolve
    kana "Ummm. Makasih lagi ya udah dibolehin duduk di sini, untung saja aku bisa makan strawberry shortcake nya, kalau enggak kayaknya aku bakalan marah deh hahaha"
    hide kana_side with dissolve
    mcname "Haha, gpp ko santai aja"
    mcname "Kebetulan kursinya kosong di situ"
    show kana_side at left with dissolve
    kana "Eh udah jam segini aku harus pulang aku duluan ya, kamu hati hati di jalan"
    hide kana_side with dissolve
    mcname "Okee. Kamu juga hati hati di jalan ya"
    show kana_side at left with dissolve
    kana "See you~"
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with dissolve
    scene mc bedroom with dissolve
    play music "audio/BGM_Kosan 2.mp3" fadein 1.0
    $ quick_menu = True
    "Pulang dari cafe, [mcname] masih memikirkan kejadian yang dialaminya hari ini"
    mcname "{i}Banyak juga ya, hal yang terjadi pada hari pertamaku di Jakarta.{/i}"
    show kana at kana_near with dissolve
    mcname "{i}Aku gak nyangka kalau hari ini bakalan bisa ngobrol sama dia.{/i}"
    mcname "{i}Tapi dipikir - pikir, dia ramah juga ya{/i}"
    mcname "{i}Aku kira, dia bakalan kaya cool dan cuek gitu{/i}"
    mcname "{i}Ternyata nyambung juga kalau diajak ngobrol.{/i}"
    mcname "{i}Udah ah mending aku tidur{/i}"
    hide kana with dissolve
    "[mcname] pun tertidur dengan lelap"
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
    play sound "audio/run.mp3"
    "Terdengar suara langkah kaki yang terburu-buru"
    mcname "{i}Sial ternyata aku benar-benar meremehkan Jakarta{/i}"
    mcname "{i}Siapa sangka macet di sini parah banget{/i}"
    "Takut terlambat di hari pertama, [mcname] terburu-buru memasuki kelas kuliahnya"
    # background lift
    mcname "Ehhhh tungguuuu-"
    "[mcname] berlari menuju Lift yang mau tertutup"
    "Di dalam lift terlihat seorang cewek yang sepertinya juga mau menuju ke kelas"
    $ quick_menu = False
    play sound "audio/ding.mp3"
    scene black with dissolve
    scene depan kampus with Dissolve(2.0)
    $ quick_menu = True
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
    play sound "audio/ding.mp3"
    $ quick_menu = False
    scene black with dissolve
    show text "{color=#FFF}Pintu lift terbuka{/color}" with Pause(2.0)
    scene depan kampus with dissolve
    $ quick_menu = True
    mcname "Ah! Terima kasih lagi yak, sudah menahan lift tadi"
    "[mcname] kemudian lanjut berlari menuju kelas"
    hide freya with dissolve
    $ quick_menu = False
    scene black with Dissolve(2.0)
    scene kelas with dissolve
    play music "audio/BGM_Kelas.mp3" fadein 1.0
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
    show freya_side_smile at left with dissolve
    freya "Haha ada-ada deh kamu. Lain kali pastiin aja dulu deh."
    hide freya_side_smile with dissolve
    mcname "Eh dari tadi kita ngobrol belum kenalan ternyata"
    mcname "Boleh kali ya, kita kenalan dulu haha."
    mcname "Kenalin namaku [mcname]"
    mcname "Aku dari Ngawi"
    mcname "Salam kenal, ya"
    $ freya_name = "Freya"
    show freya_side_smile at left with dissolve
    freya "Eh, salam kenal juga namaku Freya asalku dari Yogyakarta"
    hide freya_side_smile with dissolve
    mcname "{i}Dia ternyata imut juga ya{/i}"
    mcname "{i}Apa sih, kalau kata orang-orang di internet sekarang.{/i}"
    mcname "{i}Owh iya!{/i}"
    mcname "{i}Senyumannya manis kaya karamel{/i}"
    hide freya_smug
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
        $ quick_menu = False
        "Tiba-tiba, suara pintu pun berbunyi"
        play sound "audio/open_door.mp3"
        stop music fadeout 1.0
        scene black with dissolve
        scene kelas with Dissolve(2.0)
    else:
        mcname "{i}Mereka ngobrolin [kana_name], ya?{/i}"
        mcname "{i}Tapi kalau dilihat lihat, memang modis sih pakaiannya{/i}"
        mcname "{i}Dia juga kenal deket sama Freya, ya?{/i}"
        "[kana_name] pun menyadari bahwa di sebelahnya Freya itu adalah [mcname] dan akhirnya senyum tipis muncul dari wajahnya."
        "Saat dia akan menyapa [mcname], suara pintu pun berbunyi."
        $ quick_menu = False
        play sound "audio/open_door.mp3"
        stop music fadeout 1.0
        scene black with dissolve
        scene kelas with Dissolve(2.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "Dosen pun memasuki ruangan kelas"
    "Kelas pun menjadi tenang dan lebih tertib dari sebelumnya"
    play music "audio/BGM_Dosen + Rektor.mp3" fadein 1.0
    "Dosen" "Selamat siang mahasiswa dan mahasiswi sekalian"
    "Dosen" "Selamat datang di mata kuliah pertama kalian di jenjang perkuliah ini"
    "Bu Fatimah" "Sebelumnya perkenalkan nama saya Fatimah"
    "Bu Fatimah" "Disini saya mengajar mata kuliah Teori Politik Internasional, Studi Perang Dan Damai, Strategi Dan Tatakelola Strategis"
    "Bu Fatimah" "Untuk semester pertama kalian akan mempelajari mata kuliah dasar yaitu Teori Politik Internasional"
    "Bu Fatimah" "Dengan begitu saya akan langsung ke dalam materi"
    "Suasana kelas pun terasa hening, fokus untuk memperhatikan apa yang dijelaskan oleh Bu Fatimah"
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(2.0)
    scene kelas with dissolve
    $ quick_menu = True
    play music "audio/BGM_Dosen + Rektor.mp3" fadein 1.0
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
    show freya at char_left with dissolve
    show freya_side at left with dissolve
    freya "Eeh, iyaa. Kita satu kelompok, nih. Kebetulan banget, ya. Haha"
    hide freya_side with dissolve
    show kana at char_right with dissolve
    show kana_side at left with dissolve
    $ kana_name = "???"
    kana "Halo Kita satu kelompok ya?"
    $ kana_name = "Kana"
    kana " Mohon bantuannya, ya. Sebelumnya, kenalkan namaku [kana_name]"
    kana "Eh, kamu sini dong. Kan kita juga satu kelompok"
    hide kana_side with dissolve
    show mahasiswa_c at char_center with dissolve
    show mahasiswa_c_side at left
    mahasiswa_c "Owh iya. Siang semuanya"
    $ mahasiswa_c_name = "Galaxy"
    mahasiswa_c " Sebelumnya, kenalin nama gw [mahasiswa_c_name]"
    mahasiswa_c "Gw dari Pekalongan. Salam kenal"
    hide mahasiswa_c_side with dissolve
    hide freya with dissolve
    hide kana with dissolve
    hide mahasiswa_c with dissolve
    "Freya, [kana_name], [mcname], dan [mahasiswa_c_name] pun saling bertukar sapa dan mengobrol lebih lanjut. Akhirnya, mereka pun membuat grup chat untuk membahas pekerjaan kelompok mereka."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(2.0)
    scene bedroom with dissolve
    play music "audio/BGM_Kosan 2.mp3"
    $ renpy.block_rollback()
    $ quick_menu = True 
    "Setelah [mcname] sampai Kos nya"
    "[mcname] pun membuang tasnya ke lantai lalu melepaskan sepatu dan menghempaskan tubuhnya ke kasur"
    "Setelah capek dengan kegiatan hari ini"
    "datang ke kos membuat [mcname] merasakan ketenangan di balik hiruk pikuk Kota Jakarta"
    "Memejamkan mata, menghela nafas, dan merenungkan kembali kegiatan yang telah terjadi hari ini"
    play sound "audio/ReceiveText.ogg"
    "(Notif WA)"
    mcname "(...)"
    play sound "audio/ReceiveText.ogg"
    "(Notif WA)"
    mcname "Duh. Notif WA nih"
    mcname "Apa nih? Dari Mamah, kah?"
    "[mcname] mencoba mengecek HP nya"
    mcname "{i}Oh, ternyata bukan.{/i}"
    mcname "{i}Ini notif dari grup chat itu, ternyata{/i}"
    $ quick_menu = False
    stop music fadeout 1.0
    jump phoneChat
    # play music "audio/Dreamcatcher.mp3"
    # jump credits

label chapter1kana3:
    $ renpy.block_rollback()
    scene black with Dissolve(2.0)
    show text "{color=#FFF}KEESOKAN HARINYA{/color}" with Pause(2.0)
    play music "audio/bgm_kantin.mp3" loop fadein 1.0
    scene kantin with Dissolve(2.0)
    $ quick_menu = True
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
    show freya at char_center with dissolve
    show freya_side at left with dissolve
    "Freya" "[mcname] SINI!!!"
    "Freya" "Duduk bareng kita!!"
    "Mendengar hal tersebut akhirnya MC menghampiri ke meja Freya Di sana ternyata ada [kana_name] yang juga duduk di sampingnya."
    hide freya 
    show freya at char_left with dissolve
    show kana at char_right with dissolve
    freya "Eh sini."
    freya "Duduk di sini"
    freya "Soalnya udah rame juga kan?"
    freya "Gapapa kan nay?"
    hide freya_side with dissolve
    show kana_side at left with dissolve
    kana "Iya. Gapapa kok. Lagian di sini kosong."
    hide kana_side with dissolve
    "Mendengar persetujuan mereka, dengan lega [mcname] duduk berhadapan dengan mereka"
    mcname "Akhirnya dapat juga"
    mcname "Makasih banget loh. Aku kira aku gak bakalan dapet tempat"
    show freya_side at left with dissolve
    freya "Santai aja"
    freya "Iya kan, Nay?"
    hide freya_side with dissolve
    show kana_smile at char_right with dissolve
    show kana_side_smile at left with dissolve
    kana "Iya, hehe"
    hide kana_side_smile with dissolve
    mcname "Nay? itu nama panggilanmu, [kana_name]?"
    hide kana_smile with dissolve
    kana "Iya, aku biasanya dipanggil \"Nay\" kalau sama [freya_name]"
    show freya_side at left with dissolve
    freya "Haha. Udah kebiasaan manggilnya \"Nay\""
    freya "Jadinya, kaya gini. Hehe."
    hide freya_side with dissolve
    show kana_side at left with dissolve
    kana "Ingyah, aku udah kenal sama [freya_name] dari lama"
    hide kana_side with dissolve
    show freya_side at left with dissolve
    freya "Oh iya."
    freya "Besok jadi kerja kelompoknya, kan?"
    hide freya_side with dissolve
    mcname "Jadi dong."
    mcname "Nanti jangan lupa kabarin si [mahasiswa_c_name]"
    play sound "audio/hungry.mp3"
    "Saat asik mengobrol tentang kerja kelompok, terdengar suara perut keroncongan"
    mcname "Suara apaan tuh?"
    "[mcname] mencoba mencari sumber suara tersebut dan menyadari Kana sedang tertunduk malu sambil menutup mukanya."
    show kana_shy at char_right with dissolve
    "[mcname] dan Freya melihat ke arah Kana sambil tertawa kecil."
    show freya_smile at char_left with dissolve
    show freya_side_smile at left with dissolve
    freya "Pfft"
    hide freya_side_smile with dissolve
    mcname "Aku juga pesen deh"
    mcname "Perutku juga sudah mulai lapar nih"
    show freya_smile at char_left with dissolve
    show freya_side_smile at left with dissolve
    freya "Hahahahaha"
    freya "Ya udah sana."
    freya "Kalian pesen aja dulu."
    freya "Nanti, kita ngobrol lagi"
    hide freya_smile with dissolve
    "[mcname] mengangkat tangan sambil berteriak memanggil Mbak kantin"
    "Dengan muka sedikit tersipu malu, Kana mencuri pandang melihat ke arah [mcname]."
    mcname "Mbaaak. Mau pesen"
    "[mcname] ngeliat menu yang tersedia di kantin"
    menu:
        "Menu Kantin"
        "Pesen Ayam Smack Down":
            scene black with Dissolve(2.0)
            show text "{color=#FFF}LO KEPEDESAN DAN AKHIRNYA MALAH KE WC TERUS TERUSAN DARIPADA NGOBROL SAMA MEREKA{/color}" with Pause(2.0)
            show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
            play music "audio/Dreamcatcher.mp3"
            jump credits
        "Pesen Mie Ayam":
            $ quick_menu = False
            jump chapter1kana3mie
        "Pesen Lotek":
            scene black with Dissolve(2.0)
            show text "{color=#FFF}SAYURAN YANG LO MAKAN TERNYATA BASI{/color}" with Pause(2.0)
            show text "{color=#FFF}AKHIRNYA LO KERACUNAN MAKANAN.{/color}" with Pause(2.0)
            show text "{color=#FFF}AKHIRNYA LO KERACUNAN MAKANAN.{/color}" with Pause(2.0)
            show text "{color=#FFF}MBAK YANG JUALAN PUN AKHIRNYA DIMARAHIN KARENA UDAH BIKIN MAHASISWANYA KERACUNAN MAKANAN{/color}" with Pause(2.0)
            show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
            play music "audio/Dreamcatcher.mp3"
            jump credits


label chapter1kana3mie:
        $ renpy.block_rollback()
        scene black with dissolve
        scene kantin with dissolve
        $ quick_menu = True
        "[mcname] pun memilih mie ayam sebagai makanan yang ia pesan. Kana yang masih menahan malu, memesan makanan yang sama dengan [mcname]."
        show freya at char_left with dissolve
        show kana at char_right with dissolve
        show freya_side at left with dissolve
        freya "Hahaha emang belum makan dari kapan, Nay?"
        hide freya_side with dissolve
        show kana_clumsy at char_right with dissolve
        show kana_side_clumsy at left with dissolve
        kana "Iiih apaan sih. Udahan dong."
        hide kana_side_clumsy with dissolve
        mcname "Kalian dekat banget ya."
        mcname "Dulu satu sekolah, kah?"
        show freya_side at left with dissolve
        freya "Iya"
        freya "Aku dan Kana dari TK sampai sekarang satu kelas mulu."
        hide freya_side with dissolve
        show kana at char_right with dissolve
        show kana_side at left with dissolve
        kana "Hmpph"
        hide kana_side with dissolve
        mcname "Waaah. Enak, ya sudah kenal dari lama."
        show freya_side at left with dissolve
        freya "Hehe. Kamu gatau kan?"
        freya "Kalau Kana dulu tuh-"
        hide freya_side with dissolve
        "Sebelum Freya menyelesaikan omongannya"
        "Kana mencoba menutup mulut freya"
        show kana at char_right with dissolve
        show kana_side at left with dissolve
        kana "Ehem."
        kana "Kamu tau gak kalau dulu yang pertama kali mengakui kemerdekaan Indonesia adalah Mesir"
        "Kana mencoba mengalihkan pembicaraan Kana memberikan fun fact random"
        "{size=-5}[freya_name] & [mcname]{/size}" "(...)"
        "Melihat fun fact yang dikatakannya tidak berhasil"
        "Akhirnya Kana mencoba untuk memberikan funfact yang lainnya"
        "Merasa kelakuan temannya yang mulai aneh"
        "Freya kemudian meletakkan telapak tangannya ke dahi Kana sambil tertawa jahil."
        show freya_side at left with dissolve
        freya "Waduh kambuh"
        freya "GWS"
        hide freya_side with dissolve
        show kana_side with dissolve
        kana "Hmpph"
        kana "{size=-10}Kan gara-gara kamu juga{/size}"
        hide kana_side with dissolve
        "Seakan menjadi penyelamat"
        "Mbak kantin pun datang membawakan pesanan mereka"
        "Mbak Kantin" "Ini ya pesanannya."
        "Mata Kana bersinar, melihat datangnya Mbak kantin yang membawa makanan."
        show kana_side at left with dissolve
        kana "Makanannya sudah datang, nih"
        kana "Yuk makan dulu"
        hide kana_side with dissolve
        "Kana mencoba untuk mengalihkan pembicaraan"
        mcname "Yaudah. Mari makan."
        show freya_side at left with dissolve
        freya "Eh… Eeee. Tadi mesen Mie ayam?"
        freya "Tumben kamu makan yang begituan, Nay?"
        hide freya_side with dissolve
        "Seolah masih ingin membahas masalah tadi, freya menanyakan hal tersebut"
        mcname "Hmm? Memangnya ada apa?"
        show kana_side at left with dissolve
        kana "Freee. Yuk makan"
        hide kana_side with dissolve
        "Kana berbicara dengan nada agak kesal"
        show freya_side at left with dissolve
        freya "Hehehehe. Iya deh."
        hide freya_side with dissolve
        "Tertawa, freya akhirnya berhenti membahas topik tersebut"
        "Karena sudah lapar, [mcname] mulai memakan makanan yang sudah dihidangkan"
        "Sesekali, [mcname] melihat Kana dan Freya yang saling berbincang kecil"
        "lalu [mcname] kembali berfokus ke sepasang sumpit yang digunakan untuk menarik helaian mie ke mulutnya."
        "Ada kalanya Freya dan Kana menyertakan [mcname] dalam pembicaraan mereka"
        "Satu percakapan berlanjut ke percakapan lainnya, membuat mereka merasa menjadi lebih dekat."
        $ quick_menu = False
        scene black with Dissolve(2.0)
        scene kantin with dissolve
        $ renpy.block_rollback()
        $ quick_menu = True
        "Setelah selesai makan, mereka pergi dan berpisah ke urusannya masing-masing."
        "[mcname] pun memikirkan apa yang akan dilakukan selanjutnya."
        $ quick_menu = False
        menu:
            "Yang kamu lakukan"
            "Keliling Kampus dan melihat lihat isi kampus":
                $ renpy.block_rollback()
                play music "audio/BGM_Kampus Sore.mp3" fadein 1.0
                scene black with dissolve
                scene depan kampus with Dissolve(2.0)
                $ quick_menu = True
                mcname "{i}Aku memilih menghabiskan waktu untuk berkeliling di sekitar kampus.{/i}"
                mcname "{i}Di perjalanan pertama{/i}"
                mcname "{i}Ada parkiran yang biasa dipakai anak-anak jurusan HI untuk memarkirkan kendaraan mereka{/i}"
                mcname "{i}Terlihat disana banyak kendaraan yang bisa dibilang lumayan mahal{/i}"
                mcname "{i}Hmmmm luas juga parkiran buat kampus ini{/i}"
                mcname "{i}Seperti yang diharapkan dengan kampus ibu kota{/i}"
                mcname "{i}Terasa sangat berbeda dibandingkan dengan bangunan yang ada di desa{/i}"
                mcname "{i} Entah kenapa tiba-tiba di pikiranku terbayang sosok Kana di aula waktu itu{/i}"
                $ quick_menu = False
                scene black with dissolve
                scene kana awal with Dissolve(2.0)
                $ quick_menu = True
                mcname "{i}Aduhhh sadar woi sadar.{/i}"
                $ quick_menu = False
                scene black with dissolve
                scene depan kampus with Dissolve(2.0)
                $ quick_menu = True
                "MC pun menggeleng gelengkan kepala untuk kembali fokus pada perjalanannya mengelilingi kampus."
                $ quick_menu = False
                scene black with dissolve
                # Harusnya BG Sawah
                scene depan kampus with Dissolve(2.0)
                $ quick_menu = True
                mcname "{i}Setelah itu aku melihat sawah yang digunakan oleh mahasiswa/i jurusan lain Jeketi University.{/i}"
                mcname "{i}sawah ya…{/i}"
                mcname "{i}Gak nyangka bakal ngeliat sesuatu yang familiar di kampus ini{/i}"
                mcname "{i}Tapi mungkin buat jurusan yang ku ambil gk bakal banyak kesini{/i}"
                mcname "{i}(...){/i}"
                $ quick_menu = False
                scene black with dissolve
                # Harusnya BG Rooftop
                scene depan kampus with Dissolve(2.0)
                $ quick_menu = True
                mcname "{i}Lalu yang terakhir aku pun mencoba menaiki rooftop untuk melihat keseluruhan kampus dari atas.{/i}"
                mcname "{i}Wah dilihat dari atas ternyata memang keren sih ini kampus{/i}"
                "Dari sana bisa terlihat seluruh pemandangan di kampus"
                "Terlihat beberapa orang melaksanakan beberapa aktifitas kampus, bahkan ada juga yang sepertinya sudah siap-siap untuk pulang"
                # SFX Peregangan
                mcname "mgghhhh"
                mcname "{i}Mungkin udah dulu kali ya buat hari ini{/i}"
                mcname "{i}Abis ini pulang ke kos aja deh{/i}"
                $ quick_menu = False
                stop music fadeout 1.0
                jump chapter1kana3kos
            "Menyelidiki tempat-tempat yang membuatmu penasaran":
                $ renpy.block_rollback()
                mcname "{i}Duhh masih lama lah{/i}"
                mcname "{i}Tidur lagi enak kali ya{/i}"
                mcname "{i}Lagian mereka juga pasti datangnya telat kan{/i}"
                mcname "{i}Di Indonesia gitu si ga ada yang tepat waktu{/i}"
                "[mcname] pun memilih untuk tidur lebih lama dikarenakan waktu perjanjian masih ada beberapa jam lagi akan tetapi dia lupa melihat batre hp nya"
                "Akhirnya tertidur lelap hingga melebihi waktu yang dijanjikan dan saat ia menyalakan hp nya ia pun dimarahi oleh Kana dan Freya"
                scene black with dissolve
                show text "{color=#FFF}EH KALAU UDAH JANJIAN TUH DITEPATI{/color}" with Pause(2.0)
                show text "{color=#FFF}SEKARANG LO MALAH DI MARAHIN SAMA ANGGOTA KELOMPOK LO KAN{/color}" with Pause(2.0)
                show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
                stop music fadeout 1.0
                play music "audio/Dreamcatcher.mp3" fadein 1.0
                scene mc bedroom with Dissolve(2.0)
                jump credits
            "Langsung berangkat lebih awal supaya ga ketinggalan":
                $ renpy.block_rollback()
                "[mcname] memilih untuk berangkat lebih awal dan beberapa jam dari yang telah dijanjikan tapi dia lupa kalau dirinya belum mandi dan makan"
                "setelah sampai di tempat dijanjikan dia jatuh pingsan karena hawa panas yang terpancarkan "
                scene black with dissolve
                show text "{color=#FFF}EH KALAU MAU KEGIATAN TUH MINIMAL MANDI DAN MAKAN{/color}" with Pause(2.0)
                show text "{color=#FFF}JANGAN LANGSUNG BERANGKAT{/color}" with Pause(2.0)
                show text "{color=#FFF}SEKARANG LO MALAH DI MARAHIN SAMA ANGGOTA KELOMPOK LO KAN{/color}" with Pause(2.0)
                show text "{color=#FFF}AKHIRNYA MALAH PINGSAN KAN{/color}" with Pause(2.0)
                show text "{color=#FFF}HADEEEUHHH DASAR{/color}" with Pause(2.0)
                show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
                stop music fadeout 1.0
                

label chapter1kana3kos:
    $ renpy.block_rollback()
    scene black with dissolve
    scene mc bedroom with dissolve
    play music "audio/BGM_Kosan 1.mp3" fadein 1.0
    $ quick_menu = True
    mcname "Hmmm, keknya mending aku bangun terus siap-siap deh biar ga telat."
    mcname "Ga enak juga kalau pertama kali malah telat terus bikin mereka ga enak kan"
    "[mcname] pun bersiap siap untuk berangkat kerja kelompok"
    "Ia menghabiskan kebanyakan waktunya di mandi agar merasa lebih segar dan tidak mengantuk"
    "Setelah itu dia pun berangkat menuju tempat yang pada awalnya sudah ditentukan"
    "Setelah [mcname] sampai di tempat perjanjian"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    scene depan kampus with Dissolve(2.0)
    $ quick_menu = True
    play music "audio/BGM_Kampus.mp3" fadein 1.0
    mcname "Tenang - tenang"
    mcname "Gak usah gugup"
    mcname "Santai aja"
    mcname "Kamu gak usah gugup"
    mcname "Meski ini kerja kelompok pertama kali di kuliah tapi kamu bisa kok"
    mcname "Yuk semangat"
    "Tidak menunggu lama Kana dan Freya pun datang dan menghampiri."
    show freya at char_left with dissolve
    show kana at char_right with dissolve
    show kana_side at left with dissolve
    kana "Eh haloo"
    kana "Udah lama ya nunggunya?"
    kana "Maaf ya Jakarta macet sii hehe"
    hide kana_side with dissolve
    show freya_side at left with dissolve
    freya "Eh iya nih tadi aku ke rumah Kana dulu juga"
    freya "Biasa si princess satu ini terlalu lama dandan nya"
    freya "Tapi ya macet juga si"
    hide freya_side with dissolve
    mcname "{i}Dandan!?{/i}"
    mcname "{i}Setelah diperhatikan lebih detail memang Kana saat ini terlihat lebih natural dan lebih cantik dari biasanya{/i}"
    mcname "{i}Makeupnya yang terlihat sedikit berbeda dari saat ia ke kampus membuat ku terdiam sebentar{/i}"
    "Menyadari [mcname] memperhatikan nya"
    "Kana jadi terdiam seakan panik mendatang, dan tidak dapat menjawab dari pertanyaan Freya"
    "Kana hanya bisa melihat ke arah Freya"
    show kana_side at left with dissolve
    kana "Apaan sih Free"
    kana "Aku kan gak dandan lama"
    kana "Itu kan karena macet ihhh"
    kana "Lagian aku juga kaya biasanya di kampus ko dandan nya iya kan?"
    hide kana_side with dissolve
    "Tak lama kana pun melihat [mcname] seakan meminta bantuan darinya"
    "[mcname] hanya bisa tertawa canggung"
    mcname "Eh..uuuu, hmmm"
    mcname "Hehe"
    mcname "I-iya mungkin iya tapi kamu yang sekarang kayaknya lebih cantik deh dari biasanya natural aja gitu heh"
    show kana_shy at char_right with dissolve
    "Wajah kana pun memerah dengan cepat menandakan bahwa ia malu mendengar kata itu dari [mcname]"
    "Saat itu juga freya pun tertawa dan membuat suasana lebih hidup"
    show freya_smile at char_left with dissolve
    show freya_side_smile at left with dissolve
    freya "hahaha"
    freya "Cieee di sebut cantik tuh nay"
    freya "Cieeee"
    freya "Kiw kiw cukurukuk"
    hide freya_side_smile with dissolve
    show kana_side_shy at left with dissolve
    kana "Apaan sih"
    kana "Udah ah Fre"
    kana "Itu kan cuma basic compliment doang"
    kana "Biar ga canggung doang"
    hide kana_shy with dissolve
    hide kana_side_shy with dissolve
    show kana_side at left with dissolve
    kana "By the way ini si [mahasiswa_c_name] kemana ya ?"
    kana "Kok belum datang si udah jam segini nih"
    hide kana_side with dissolve
    mcname "Tunggu bentar lagi aja dulu ya mungkin kejebak macet"
    mcname "Mending kita tanya di grup aja kali ya ?"
    hide freya_smile with dissolve
    show freya_side at left with dissolve
    freya "Ide bagus"
    freya "Yaudah, kita tunggu beberapa menit aja dulu lah ya"
    hide freya_side with dissolve
    "Mereka pun menunggu [mahasiswa_c_name]"
    "(...)"
    "Sudah 10 menit namun tidak ada kabar"
    "Akhirnya mereka menyerah menunggu"
    show kana_side at left with dissolve
    kana "Eh udah lama ini, mana panas banget lagi"
    kana "Kita duluan aja kali ya"
    kana "[mahasiswa_c_name] gak bales ini"
    kana "Ditelpon juga ga di angkat kan"
    hide kana_side with dissolve
    show freya_side at left with dissolve
    freya "Iya juga sih"
    freya "Ya udah lah ya mungkin ketiduran atau gimana"
    freya "Nanti kita suruh aja buat ngerjain bagian yang lain"
    hide freya_side with dissolve
    mcname "Eh bentar ada chat nih dari [mahasiswa_c_name]"
    "[mcname] kemudian membuka HP nya"
    mcname "Yahh ternyata dia tiba-tiba ada panggilan kerjaan tuh"
    mcname "Dia minta maaf ga bisa datang dan ngerjain bagian lain aja tuh katanya gimana?"
    show kana_side at left with dissolve
    kana "Ya udah deh gpp"
    kana "Yang penting sekarang kita kerjain aja dulu lah biar makin cepet istirahat"
    kana "Panas banget soalnya"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    # harusnya bg monas
    scene depan kampus with Dissolve(2.0)
    $ quick_menu = True
    play music "audio/BGM_Monas.mp3" loop fadein 1.0
    "Mereka pun memutuskan untuk meninggalkan [mahasiswa_c_name] dan mulai mengerjakan tugas kelompok yang diberikan"
    "Mereka pun mulai berjalan jalan dan mewawancarai sekitar"
    $ quick_menu = False
    stop music fadeout 2.0
    jump puzzle_start

label chapter1kana3monas:
    scene black with dissolve
    # Harusnya BG Monas
    scene depan kampus with Dissolve(2.0)
    $ quick_menu = True
    play music "audio/BGM_Monas.mp3" loop fadein 1.0
    "Setelah itu, mereka memutuskan untuk berhenti sejenak di sekitar monas dikarenakan panas yang tidak tertahankan"
    show freya at char_left with dissolve
    show kana at char_right with dissolve
    show freya_side at left with dissolve
    freya "Aduhh panas banget ya Nay, [mcname]"
    freya "Jujur ini mungkin hari terpanas dalam minggu ini"
    hide freya_side with dissolve
    show kana_side at left with dissolve
    kana "Iya panas banget mana haus lagi"
    hide kana_side with dissolve
    mcname "{i}Hmmm iya nih panas{/i}"
    mcname "{i}Bisa kali ya gw beliin mereka minum sesekali gtu{/i}"
    mcname "Eh bentar ya gw mau beli minum dulu"
    menu:
        "Kamu beliin mereka"
        "Minuman berenergi":
            "[mcname] membelikan Minuman berenergi untuk kana dan freya"
            "Dikarenakan minuman ini lah yang ia minum saat di desa saat merasa kecapean agar berenergi lagi"
            "akan tetapi kana dan freya melihat [mcname] dengan tatapan aneh saat tau itu ternyata minuman berenergi"
            stop music fadeout 1.0
            scene black with dissolve
            show text "{color=#FFF}BRO YANG BENER AJA{/color}" with Pause(2.0)
            show text "{color=#FFF}DI KIRA MEREKA ABIS OLAHRAGA ATAU NUKANG KALI YA DI KASIH GINIAN{/color}" with Pause(2.0)
            show text "{color=#FFF}AKHIRNYA MEREKA GA MAU NGOBROL KAN SAMA LO LAGI{/color}" with Pause(2.0)
            show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
            play music "audio/Dreamcatcher.mp3" fadein 1.0
            scene dream with dissolve
            jump credits
        "Es Teh":
            jump chapter1kana3monasesteh
        "Jamu":
            stop music fadeout 1.0
            scene black with dissolve
            "[mcname] membelikan jamu untuk Kana dan Freya, karena teringat dengan mama di desa dimana saat mama merasa capek selalu minta untuk di belikan jamu agar lebih segar"
            "Tetapi Kana dan Freya sangat lah asing dengan jamu dan saat itu juga mereka malah pucat dan muntah"
            show text "{color=#FFF}EH DIKIRA UDAH TUA KALI YA DI KASIH JAMU{/color}" with Pause(2.0)
            show text "{color=#FFF}LAGIAN GA SEMUA BISA MINUM JAMU BROO{/color}" with Pause(2.0)
            show text "{color=#FFF}MIKIR{/color}" with Pause(2.0)
            show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
            scene dream with dissolve
            play music "audio/Dreamcatcher.mp3" fadein 1.0
            jump credits



label chapter1kana3monasesteh:
    $ renpy.block_rollback()
    $ quick_menu = False
    scene black with dissolve
    # harusnya bg monas
    scene depan kampus with Dissolve(2.0)
    $ quick_menu = True
    "[mcname] melihat ada sebuah stand minuman es teh yang cukup ramai"
    "Ia pun memilih untuk membelikan mereka minuman itu"
    "Saat ia datang kembali dengan membawa 3 gelas es teh raut muka Kana dan Freya tersenyum dan merasa senang"        
    show kana at char_right with dissolve
    show freya at char_left with dissolve
    show kana_side at left with dissolve
    kana "Wahhhh cocok banget nih"
    kana "Makasih banyak ya [mcname]"
    kana "Ini berapa? nanti aku ganti ya"
    hide kana_side with dissolve
    show freya_side at left with dissolve
    freya "Duhh cocok banget nih siang siang minum es teh seger banget"
    freya "Makasih yaa"
    freya "Nanti teh punyaku di bayarin sama Kana ya"
    hide freya_side with dissolve
    # Yang bener aja rugi dong
    kana "..."
    mcname "Hahah udah udah gpp kok"
    mcname "Ini dari aku sekalian ucapan terimakasihku udah mau nunjukin sekitar Jakarta"
    mcname "Soalnya kemarin aku ga sempet muter muter jadi makasih ya"
    show freya_side at left with dissolve
    freya "Yang bener?"
    freya "Aku si gak nolak"
    freya "hehe"
    hide freya_side with dissolve
    show kana_side at left with dissolve
    kana "Hadeeeh Freya Freya"
    "Mereka tertawa bersama dan kembali mengobrol satu sama lain hingga waktu pun menunjukkan sudah sore."
    $ quick_menu = False
    scene black with dissolve
    # BG Monas
    scene depan kampus with dissolve
    show freya at char_left with dissolve
    show kana at char_right with dissolve
    $ quick_menu = True
    mcname "Eh ini udah kah?"
    mcname "Atau kira - kira gimana lagi nih?"
    mcname "Kalau dari aku sih udah cukup ga perlu ada yang di tambah nantinya malah makin ribet"
    show freya_side at left with dissolve
    freya "Sebenernya ada yang menurutku harus di tambah sih"
    freya "Tapi itu nanti sama aku aja"
    freya "Agak susah jelasinnya juga hehe"
    hide freya_side with dissolve
    show kana_side at left with dissolve
    kana "Aku sih udah oke aja"
    kana "Maklumin Freya ya [mcname]"
    hide kana_side with dissolve
    "Senyuman kecil keluar dari wajah Kana, seakan sudah terbiasa dengan Freya"
    show kana_smile at char_right with dissolve
    show kana_side_smile at left with dissolve
    kana "Freya emang gitu orangnya"
    kana "Dia susah jelasin beberapa hal yang ada di kepalanya"
    kana "Tapi dia punya banyak ide yang bagus kok"
    kana "Santai aja"
    kana "Nanti kita tinggal kasih tau ke [mahasiswa_c_name] aja berarti ya? bagian yang harus dia kerjain"
    hide kana_side_smile with dissolve
    hide kana_smile with dissolve
    mcname "Ooooo oke deh"
    mcname "Nanti aku aja yang hubungi [mahasiswa_c_name] sama jelasin bagian mana yang harus dia kerjain"
    show kana_smile at char_right with dissolve
    show kana_side_smile at left with dissolve
    kana "Okee makasih ya"
    hide kana_smile with dissolve
    hide kana_side_smile with dissolve
    show freya_side at left with dissolve
    freya "Mantappp"
    freya "Nay ayoo itu supirmu sudah nungguin"
    freya "Eh kita duluan ya"
    freya "Dadah"
    hide freya_side with dissolve
    "Terlihat orang dengan dengan jas hitam menunggu di depan mobil tidak jauh dari mereka"
    mcname "Okee makasih ya"
    hide kana with dissolve
    hide freya with dissolve
    "Setelah itu [mcname], Kana dan Freya pun pulang masing masing ke rumahnya"
    "Di perjalanan [mcname] mengenang kembali harinya yang telah ia habiskan bersama Kana dan Freya"
    "(...)"
    mcname "{i}Wahh, hari ini cape juga{/i}"
    mcname "{i}Tapi beruntung aku ga telat dan ikut kerja kelompok{/i}"
    mcname "{i}Kana sama Freya friendly juga ternyata{/i}"
    mcname "{i}Awalnya aku kira bakalan kaya judes gitu hahaha{/i}"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    scene mc bedroom with Dissolve(2.0)
    $ quick_menu = True
    play music "audio/BGM_Kosan 2.mp3" fadein 1.0
    "Meskipun merasa kecapean"
    "[mcname] tetap bisa mengingat kembali apa yang terjadi pada hari ini"
    "Sesaat sampai di kosannya, [mcname] hanya bisa rebahan di kasur dan melihat foto yang Freya kirimkan saat kerja kelompoknya"
    "Ada satu foto yang membuatnya tersenyum kembali, yaitu foto Kana yang tidak sengaja diambil oleh [mcname] saat kerja kelompok"
    mcname "Apakah ini yang dinamakan..."
    "[mcname] pun tertidur dan ia memimpikan foto Kana yang tersenyum itu"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with dissolve
    scene kelas with Dissolve(2.0)
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    $ quick_menu = True
    "Setelah sampai di kelas [mcname] menghampiri [mahasiswa_c_name] untuk menjelaskan bagian mana yang harus ia kerjakan"
    show mahasiswa_c at mahasiswa_c_center with dissolve
    mcname "Eh, [mahasiswa_c_name] kemarin ga datang ya?"
    show mahasiswa_c_side at left with dissolve
    mahasiswa_c "Eh iya [mcname], maaf ya soalnya tiba - tiba kakakku sakit terus ke RS, aku disuruh nemenin"
    hide mahasiswa_c_side with dissolve
    "Saat mereka berdua mengobrol satu sama lain, datang Freya dan Kana dari arah pintu dan menyapa mereka"
    show freya at char_left with dissolve
    show kana at char_right with dissolve
    mcname "Eh..."
    mcname "Bukannya kemarin kamu bilang kalau kamu ada panggilan kerja ya?"
    show kana_side at left with dissolve
    kana "Halo [mcname], halo [mahasiswa_c_name]"
    hide kana_side with dissolve
    show freya_side at left with dissolve
    freya "Haloo semuanya, ada apa nih"
    hide freya_side with dissolve
    show mahasiswa_c_side at left with dissolve
    mahasiswa_c "Yooo Kalian, ini cuma lagi ada yang mau dibahas sama [mcname]"
    hide mahasiswa_c_side with dissolve
    mcname "Nggak, ini tadi baru mau jelasin pekerjaan bagian dia tapi kok, alasannya beda ya?"
    show mahasiswa_c_side at left with dissolve
    mahasiswa_c "Huh beda???"
    mahasiswa_c "Gak kok ,jadi kemarin tuh emang ada panggilan kerja"
    mahasiswa_c "tapi tiba tiba kakak ku sakit terus ke RS gitu"
    mahasiswa_c "Hahahaha"
    hide mahasiswa_c_side with dissolve
    "Kata [mahasiswa_c_name] sambil tertawa canggung"
    "Melihat gelagat Mahasiswa C yang agak aneh, Freya memicingkan mata dengan tatapan curiga"
    show freya_angrysmile at char_left with dissolve
    show freya_side_angrysmile at left with dissolve
    freya "Hmmmm, gak tau deh"
    freya "Gak peduli juga mana yang bener"
    freya "Yang penting kamu kerjain ya"
    freya "Awas aja kalau engga"
    hide freya_side_angrysmile with dissolve
    hide freya_angrysmile with dissolve
    "Freya memberikan senyuman yang entah kenapa terasa berbeda dari senyum karamel biasanya"
    show kana_side at left with dissolve
    kana "hahaha, makan tuh kena ancam Freya"
    hide kana_side with dissolve
    show mahasiswa_c_side at left with dissolve
    mahasiswa_c "Iya iya"
    mahasiswa_c "Santai aja kali"
    mahasiswa_c "Nanti gue kerjain"
    mahasiswa_c "Ga usah khawatir dah"
    hide mahasiswa_c_side with dissolve
    "[mcname] pun menjelaskan apa yang harus dilakukan [mahasiswa_c_name] kedepannya untuk mengerjakan tugas kelompok nya"
    "[mahasiswa_c_name] pun setuju dan mengerti apa yang harus ia lakukan"
    show mahasiswa_c_side at left with dissolve
    mahasiswa_c "Oke dah paham-paham ternyata segini, ku kira bakalan banyak"
    hide mahasiswa_c_side with dissolve
    mcname "Sebenernya ada yang lain si tapi coba tanya Freya sana"
    show mahasiswa_c_side at left with dissolve
    mahasiswa_c "Ada lagi ga Freya?, aku kira bakalan banyak"
    hide mahasiswa_c_side with dissolve
    show freya_angrysmile at char_left with dissolve
    show freya_side_angrysmile at left with dissolve
    freya "Gini doang??"
    "Freya menatap Mahasiswa C dengan kesal"
    freya "Awas aja kalau ga bener ya!!"
    freya "Aku coret namamu dari kelompok"
    hide freya_side_angrysmile with dissolve
    show mahasiswa_c_side at left with dissolve
    mahasiswa_c "Lah santai aja napa"
    mahasiswa_c "Ya udah gw tinggal lagi yak"
    mahasiswa_c "Soalnya masih ada yang harus gue kerjain nih"
    hide mahasiswa_c_side with dissolve
    "[mahasiswa_c_name] kemudian mengambil tas nya kemudian lari pergi meninggalkan mereka"
    hide mahasiswa_c with dissolve
    show freya_side_angrysmile at left with dissolve
    freya "Ya ela, tuh anak malah kabur"
    freya "Ya udah lah ga tau lagi"
    hide freya_side_angrysmile with dissolve
    show kana_side at left with dissolve
    kana "Udah lah"
    kana "Oh iya [mcname] bagaimana liburanmu kemarin"
    hide kana_side with dissolve
    mcname "Yah, gak ada yang menarik sih"
    mcname "Palingan cuma rebahan di kamar aja soalnya kemarin ngabisin tenaga banget"
    show kana_side at left with dissolve
    kana "Sama dong"
    kana "Aku juga kemarin cuma di rumah aja buat bersih-bersih kamar"
    hide kana_side with dissolve
    mcname "Hahaha, Sama aku juga"
    hide freya_angrysmile with dissolve
    show freya_side at left with dissolve
    freya "Enak banget ya"
    freya "Aku pulang pulang harus nyari bahan buat project kita sih"
    hide freya_side with dissolve
    mcname "Lah, kalau perlu bantuan bilang Freya"
    mcname "Kita siap membantu tenang aja"
    show kana_side at left with dissolve
    kana "Iya nih jangan ngerjaiin sendirian yaa"
    kana "Awas aja"
    hide kana_side with dissolve
    show freya_side at left with dissolve
    freya "Santai aja, bisa ko"
    hide freya_side with dissolve
    mcname "Yang bener?"
    show freya_angrysmile at char_left with dissolve
    show freya_side_angrysmile at left with dissolve
    freya "Bener, kalau mau bahas project mah nanti aja deh bahas yang lain aja napa"
    hide freya_side_angrysmile with dissolve
    hide freya_angrysmile with dissolve
    show kana_side at left with dissolve
    kana "Haha, oke deh Frey aku percaya kok sama kamu"
    kana "By the way [mcname] kemarin nyasar ga nih pas pulang sendirian soalnya dulu aku pas pulang sendirian pernah nyasar"
    kana "Itulah kenapa sekarang pake supir"
    "[mcname] menjawab dengan semangat"
    mcname "IYA"
    mcname "Aku kemarin hampir aja dibuat nyasar sama maps"
    show freya_side at left with dissolve
    freya "Hahah bener tuh"
    freya "Dia sampe mau nangis loh pas telepon aku"
    hide freya_side with dissolve
    show kana_side at left with dissolve
    kana "“Ihh freya gak usah kasih tau juga kalau bagian itu"
    hide kana_side with dissolve
    mcname "Iya kah?"
    mcname "Jadi pengen liat kamu mau nangis itu hahah"
    "Dosen pun memasuki ruangan dan kelas pun di mulai"
    "Hari dipenuhi dengan kelas dan [mcname] pun memilih untuk pergi ke kos untuk istirahat."
    $ quick_menu = False
    scene black with dissolve
    scene kelas with Dissolve(2.0)
    $ renpy.block_rollback()
    $ quick_menu = True
    "Waktu yang diberikan untuk mengerjakan tugas pun telah berakhir, dan hari dimana presentasi dilakukan pun tiba"
    "[mcname], Kana, Freya dan [mahasiswa_c_name] pun melakukan presentasinya di depan"
    "Presentasi dilakukan secara lancar dan saat kelas akan selesai, dosen pun memberitahukan beberapa kelompok yang memiliki nilai tinggi"
    "Diantara kelompok itu [mcname], Kana, Freya dan [mahasiswa_c_name] mendapatkan salah satu dengan nilai tertinggi"
    show kana at char_right with dissolve
    show freya at char_left with dissolve
    show mahasiswa_c at mahasiswa_c_center with dissolve
    show kana_side at left with dissolve
    kana "Wahhhh, kita dapat nilai tertinggi loh!???"
    hide kana_side with dissolve
    show freya_side at left with dissolve
    freya "Hehehe, siapa dulu kan ada aku"
    hide freya_side with dissolve
    mcname "Enak aja, gara gara aku tuh"
    show mahasiswa_c_side at left with dissolve
    mahasiswa_c "Ya elah gara gara ku ini"
    mahasiswa_c "Coba aja aku ga ngerjaiin bagian ku kelar kelar dah"
    hide mahasiswa_c_side with dissolve
    show freya_angrysmile at char_left with dissolve
    show freya_side_angrysmile at left with dissolve
    freya "Eh yang ga datang ke kerja kelompok diem aja"
    hide freya_side_angrysmile with dissolve
    show kana_side at left with dissolve
    kana "Aduhh, fre fre santai free jangan marah"
    hide kana_side with dissolve
    show freya_side_angrysmile at left with dissolve
    freya "Lagian mancing mancing…"
    hide freya_side_angrysmile with dissolve
    mcname "Mancing apa tuh?"
    mcname "Mancing perkoro kah"
    mcname "Hahahaha"
    hide freya_angrysmile with dissolve
    "[mcname], Kana, Freya dan [mahasiswa_c_name] pun senang saling tertawa satu sama lain dan mengucapkan terimakasih kepada satu sama lain"
    "Di situ [mcname] melihat senyum Kana yang lebar terlihat begitu bahagia dan membuat hatinya pun berdetak kencang"
    $ quick_menu = False
    jump chapter2kanastart





    





