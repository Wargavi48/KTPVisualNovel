label chapter1kana1:
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene chapter 1 kana with Dissolve (1.0)
    pause(3.0)
    scene black with Dissolve (1.0)
    play music "audio/BGM_Kampus.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    #$ renpy.block_rollback()
    "Walaupun ini sudah pertengahan tahun."
    "Matahari secara terik menerangi kota Jakarta."
    "Saat melihat ke atas langit, hanya langit birulah yang terlihat."
    $ quick_menu = False
    scene depan kampus with Dissolve(2.0)
    $ quick_menu = True
    "[mcname!c]" "Untung saja masih sempat untuk ikut orientasi."
    "[mcname!c]" "Gak nyangka di Jakarta ternyata beneran macet parah."
    "[mcname!c]" "Yah walaupun begitu ini memang pengalaman baru yang aku rasakan."
    "[mcname!c]" "Berbeda jauh dari tempatku dulu."
    "[mcname!c]" "Huuuu, ini hari pertamaku orientasi di Jeketi University."
    "[mcname!c]" "Di sini tempat di mana aku bakalan kenal sama orang baru, temen baru, atau bahkan jodoh. Heheh."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Kelas.ogg" fadein 1.0
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    scene kelas with Dissolve(1.0)
    play sound "audio/crowd_noise.mp3" loop fadein 1.0 volume (4.0)
    $ quick_menu = True
    "[mcname!c]" "Seperti yang diharapkan dari kampus Ibu Kota."
    "[mcname!c]" "Orangnya rame banget."
    "Terlihat di dalam ruangan sudah diisi dengan mahasiswa baru."
    "[mcname!c]" "{i}Hmmm... kayaknya aku harus mencari tempat duduk yang kosong sebelum penuh.{/i}"
    "[mcname!c] melihat tempat duduk yang berada di pojok atas ruangan."
    "[mcname!c]" "{i}Ah sepertinya itu tidak ada orang.{/i}"
    "Saat sampai di sana, tidak terlihat orang di barisan tersebut."
    "[mcname!c]" "{i}Hmmm... tumben di bagian belakang kosong, padahal biasanya orang pada seneng di belakang.{/i}"
    "[mcname!c] kemudian duduk di kursi tersebut."
    "[mcname!c]" "{i}Tapi lumayan juga dapet duduk di sini, jadinya bisa ngeliat yang lain dengan jelas.{/i}"
    "Saat memperhatikan sekitar, [mcname!c] mendengar suatu topik yang menarik perhatiannya."
    stop sound fadeout 1.0
    "{size=-5}Mahasiswa A{/size}" "Eh eh liat deh itu kan mahasiswi itu..."
    "{size=-5}Mahasiswa B{/size}" "Yang mana sih?"
    "[mcname!c]" "{i}Hmmm? Apa yang sedang mereka bicarakan?{/i}"
    "{size=-5}Mahasiswa A{/size}" "Ituuu, yang ituu tuhh."
    "Mahasiswa tersebut memberikan kode kepada temannya ke arah seorang cewek."
    "Pembicaraan mereka yang cukup keras membuat [mcname!c] pun melirik ke arah orang yang menjadi bahan pembicaraan."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Romance Kana.ogg" fadein 1.0
    scene kana awal with Dissolve(2.0)
    $ quick_menu = True
    "{size=-5}Mahasiswa B{/size}" "Ohhh dia!!"
    "{size=-5}Mahasiswa B{/size}" "Eh bukannya dia mahasiswa yang…. bla bla bla-"
    "Terpesona terhadap cewek tersebut, [mcname!c] tidak mendengarkan pembicaraan para Mahasiswa tadi."
    "Di sana terlihat seorang cewek cantik yang terlihat seumuran dengan [mcname!c]."
    "Rambutnya biru yang mana mengingatkannya dengan lautan yang berada di kampung halamannya."
    "Matanya pun tidak kalah indah dengan batu sapphire."
    "……"
    "[mcname!c]" "{i}Aku tidak bisa melepaskan mataku dari dia...{/i}"
    "[mcname!c]" "{i}Oh...{/i}"
    "[mcname!c]" "{i}Dia siapa?{/i}"
    "[mcname!c] bertanya kepada dirinya sendiri."
    "[mcname!c]" "{i}Tapi memang benar jika dilihat, dia memberikan aura seorang gadis cantik yang anggun dan kalem.{/i}"
    "[mcname!c]" "{i}Kok ada ya orang secantik dia?{/i}"
    "[mcname!c]" "{i}Atau… memang semua orang dari kota itu kaya gitu?{/i}"
    "[mcname!c] pun melihat ke sekelilingnya, berusaha membandingkan dengan cewek yang ada di ruangan."
    "[mcname!c]" "{i}Hmmm emang sih, hampir semua kelihatan cantik…{/i}"
    "[mcname!c]" "{i}Tapi kok cuma dia ya, yang jadi perhatian orang-orang.{/i}"
    "[mcname!c]" "{i}Ya termasuk aku juga sih...{/i}"
    "……"
    "1… 2… 3… 8… 9… 10… menit telah berlalu dan [mcname!c] masih menatap cewek tersebut."
    "Mungkin itu adalah rekor terlama [mcname!c] dalam memperhatikan seseorang."
    $ quick_menu = False
    stop music fadeout 1.0
    scene kelas with Dissolve(2.0)
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    $ quick_menu = True
    "Tiba-tiba terdengar suara pintu terbuka dan seluruh perhatian tertuju ke sumber suara tersebut."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Dosen.ogg" fadein 1.0
    scene kelas with Dissolve(1.0)
    $ quick_menu = True
    "Rektor" "Selamat datang Mahasiswa baru yang memasuki *NAMA UNIVERSTASNYA* University…"
    $ quick_menu = False 
    scene black with Dissolve(1.0)
    scene kelas with Dissolve(1.0)
    $ quick_menu = True
    "Perkataan sambutan dari Rektor dan jajaran Dosen membuat [mcname!c] dan beberapa Mahasiswa/i lain merasa bosan."
    "Seakan mendukung perkataan [mcname!c], beberapa mahasiswa/i pun ada yang bermain HP, mengobrol, atau bahkan bercanda."
    "{size=-5}Mahasiswa A{/size}" "Eh bosenin bet dah, template banget ini ucapan selamat datangnya tuh, bikin ngatuk ya ga?"
    "{size=-5}Mahasiswa B{/size}" "Iyaa, bener banget dah mending kita login yuk, P MABAR MABAR..."
    "{size=-5}Mahasiswa C{/size}" "Gas kali ya login."
    show kana_smile at kana_near with dissolve
    "[mcname!c] pun tidak sengaja mengalihkan pandangannya kepada perempuan tadi yang juga tertawa kecil karena mendengar obrolan mahasiswa tersebut."
    stop music fadeout 1.0    
    show kana at kana_near with dissolve
    $ quick_menu = False
    play music "BGM_Romance Kana.ogg" fadein 1.0
    scene kana awal with Dissolve(2.0)
    $ quick_menu = True
    "[mcname!c]" "{i}Whoa.... Cantik banget ya...{/i}"
    "[mcname!c]" "{i}Aku tidak menyangka ternyata ada perempuan semanis dia.{i}"
    show kana awal senyum with Dissolve(2.0)
    "Mata [mcname!c] dan perempuan itu tidak sengaja bertemu."
    "[mcname!c]" "{i}Ah!{/i}"
    "[mcname!c]" "{i}Waduh mata kita gak sengaja bertemu pula.{/i}"
    $ quick_menu = False
    scene black with Dissolve (1.0)
    scene kelas with Dissolve(1.0)
    show kana at kana_near with dissolve
    $ quick_menu = True
    "[mcname!c] pun langsung mengalihkan pandangannya karena tersipu malu."
    "[mcname!c]" "{i}Semoga aja aku gak dikira orang aneh sama dia.{/i}"
    hide kana with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Kelas.ogg" fadein 1.0
    scene kelas with Dissolve(1.0)
    $ quick_menu = True 
    "[mcname!c] meregangkan badannya yang terasa kaku akibat duduk terlalu lama."
    "[mcname!c]" "{i}Akhirnya selesai juga sambutan dan kegiatan hari ini.{/i}"
    "[mcname!c]" "{i}Hari ini lumayan cape juga ya, tapi masih ada energi sih…{/i}"
    $ quick_menu = False
    window auto hide
    show kana awal senyum with Dissolve(1.0)
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
    window auto show
    $ quick_menu = True 
    "[mcname!c]" "{i}Aduh! Kok aku ga bisa hilangkan senyuman itu dari kepalaku ya?{/i}"
    $ quick_menu = False
    scene kelas with Dissolve(2.0)
    $ quick_menu = True
    "[mcname!c]" "{i}Ah udah lah.{/i}"
    "[mcname!c]" "{i}Hmmm...{/i}"
    "[mcname!c]" "{i}Eh masih jam segini nih...{/i}"
    "[mcname!c]" "{i}Enaknya buat habisin waktu, mending aku ke…{/i}"
    define mc_from = ""
    menu:
        #"Mau Kemana?"
        "[mcname!c]" "{i}Enaknya buat habisin waktu, mending aku ke…{/i}"
        "A. Ke Kosan":
            #$ kana_name = "Perempuan itu"
            $ mc_from = "Kos"
            stop music fadeout 1.0
            # jump chapter1kana2Campus
            jump chapter1kana2kos
        "B. Ke Warteg":
            stop music fadeout 1.0
            $ quick_menu = False
            play music "BGM_Bad End.ogg" fadein 1.0
            "Kamu milih makan ke warteg dan di situ ternyata wartegnya pake boraks dan akhirnya kamu masuk rumah sakit..."
            scene black with dissolve
            show text "{color=#FFF}MAKANYA JANGAN MAKAN SEMBARANG BROO KAN MASUK RUMAH SAKIT{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3"
            jump credits
        "C. Ke Cafe":
            $ mc_from = "Cafe"
            stop music fadeout 1.0
            $ quick_menu = False
            scene black with Dissolve(1.0)
            jump chapter1kana2Cafe
            
label chapter1kana2kos:
    ##$ renpy.block_rollback()
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" fadein 1.0 volume (0.8)
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Tak terasa langit menjadi gelap."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(2.0)
    $ quick_menu = True
    "[mcname!c] menghabiskan waktu di kosan dan memilih untuk beristirahat dibanding pergi kesana-kemari."
    "[mcname!c] masih memikirkan kejadian yang dialaminya hari ini."
    "[mcname!c]" "{i}Lumayan capek ya orientasinya...{/i}"
    "[mcname!c]" "{i}Ternyata panas banget di Jakarta.{/i}"
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
    show kana_smile at kana_near with dissolve
    "[mcname!c]" "{i}Aku gak nyangka bisa bertemu sama perempuan sebersinar itu...{/i}"
    "[mcname!c]" "{i}Tapi dilihat-lihat, kayaknya dia ramah ya...{/i}"
    "[mcname!c]" "{i}Aku kira, dia bakalan kaya cool dan cuek gitu..{/i}"
    "[mcname!c]" "{i}Udah ah mending aku tidur.{/i}"
    $ quick_menu = False
    hide kana_smile with dissolve
    scene awan malam with Dissolve(2.0)
    $ quick_menu = True
    "[mcname!c] pun tertidur dengan lelap."
    jump chapter1kana2Campus

label chapter1kana2Cafe:
    ##$ renpy.block_rollback()
    play sound "audio/cafe-entrance.mp3" fadein 1.0
    play music "audio/BGM_Cafe Cerah.ogg" fadein 1.0 volume (2.0)
    scene cafe with Dissolve(1.0)
    $ quick_menu = True
    "[mcname!c] memilih untuk menghabiskan waktu di sebuah cafe."
    play sound "audio/crowd_noise.mp3" loop fadein 1.0 volume (4.0)
    "Awalnya cafe itu terasa sepi, tetapi lama-lama cafe tersebut mulai penuh."
    "[mcname!c]" "Wah makin lama, makin rame ya cafe ini. Memang salah satu cafe terkenal sih, kalau kata internet..."
    "Banyak sekali orang yang berlalu lalang. Akan tetapi, ada satu orang yang menarik perhatian [mcname!c]."
    show kana at small_center with dissolve
    "Saat orang itu mendekati pintu cafe, [mcname!c] pun menyadari bahwa orang itu adalah cewek yang ada di kampus tadi."
    "[mcname!c]" "{i}Loh, itu kan perempuan yang tadi di kampus?{/i}"
    "[mcname!c]" "{i}Kita datang ke cafe yang sama...{/i}"
    "[mcname!c]" "{i}Kebetulan macam apa ini?{/i}"
    "Secara tidak sadar, [mcname!c] pun melihat ke arah perempuan tersebut. Mungkin karena dia berdiam diri cukup lama, yang membuat beberapa pelanggan pun melihat ke arahnya..."
    hide kana with dissolve
    show kana_confused at char_center with dissolve
    "Perempuan itu terlihat sedang kebingungan."
    "Pandangannya yang melihat ke sana kemari dan gerak tubuhnya yang menunjukan dirinya gelisah, membuat [mcname!c] pun berpikir."
    "[mcname!c]" "{i}Hmmm kenapa ya, kok dari tadi dia kaya gelisah gitu??{/i}"
    "Mereka pun secara tidak sengaja bertukar pandangan."
    "Reflek, [mcname!c] pun mengalihkan pandangannya."
    "[mcname!c]" "{i}Duh mata kita gak sengaja ketemu pula.{/i}"
    "Perempuan itu pun mendekati meja tempat [mcname!c] berada..."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    stop sound fadeout 1.0
    scene cafe with Dissolve(1.0)
    hide kana_confused
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    $ quick_menu = True
    kana "H-halooo, maaf tapi apa kursinya kosong?"
    hide kana_side_talk
    show kana at kana_near
    with dissolve
    "[mcname!c]" "Eh iya ini kosong kok kebetulan dari tadi ga ada yang nempatin takut kali ya sama aku, haha."
    "[mcname!c]" "{i}Aduh sial ngomong apaan sih aku, garing banget lagi jokesnya.{/i}"
    hide kana_talk
    show kana_drylaugh at kana_near
    show kana_side_drylaugh at left
    with dissolve
    kana "Haha…"
    hide kana_side_drylaugh
    hide kana_drylaugh
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Kalau gitu aku boleh ya duduk di sini?"
    hide kana_side_talk
    hide kana_talk
    show kana_smile at kana_near
    with dissolve
    "Cewek itu pun tersenyum manis."
    "Tanpa menunggu jawaban dari [mcname!c], perempuan itu pun duduk di sebelah [mcname!c]."
    "Mengangkat tangan untuk memanggil pelayan. Perempuan itu kemudian memesan pesanannya."
    hide kana_smile
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Mas! Aku mau pesen dong."
    hide kana_side_talk 
    hide kana_talk
    show kana at kana_near
    with dissolve
    "[mcname!c]" "..."
    "Pikiran [mcname!c] dibuat bingung dengan siapa dia kenapa dia langsung duduk di sebelahnya lalu kenapa dia mau duduk di situ, kenapa harus dia, banyak sekali pertanyaan yang muncul di pikiran [mcname!c]."
    hide kana
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Mas aku pesan strawberry shortcake nya 1 ya, sama lemon tea nya satu, es nya jangan terlalu banyak ya, makasih banyak mas…"
    hide kana_side_talk 
    hide kana_talk
    with dissolve
    "Pelayan cafe itu pun pergi untuk memproses pesanan cewek itu."
    show kana_confused at kana_near
    show kana_side_confused at left
    with dissolve
    kana "Eh maaf ya langsung duduk aja..."
    kana "Soalnya aku lagi kepengen banget cake yang ada di sini karena cuma ada di hari tertentu aja."
    hide kana_side_confused
    hide kana_confused
    show kana_drylaugh at kana_near
    show kana_side_drylaugh at left
    with dissolve
    kana "Hahahaha..."
    hide kana_side_drylaugh
    hide kana_drylaugh
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Aku awalnya sempat khawatir gitu kalau nanti ga dapet tempat duduk gimana."
    kana "Untung aja ada tempat duduk di sebelahmu ini."
    hide kana_side_talk
    hide kana_talk
    show kana_smile at kana_near
    with dissolve
    pause(1.0)
    hide kana_smile
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Makasih ya udah diizinin duduk di sini."
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near
    with dissolve
    pause(1.0)
    hide kana
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    $ kana_name = "Kana"
    kana "Oh iya kenalan dulu, namaku \"Kanaia Asa\", biasanya dipanggil Kana."
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near
    with dissolve
    "[mcname!c]" "Aku [mcname!c] salam kenal ya."
    hide kana
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Ohhh [mcname!c], salam kenal juga ya."
    kana "Udah lama duduk di cafe ini?"
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near
    with dissolve
    "[mcname!c]" "Lumayan sih, pas awal dateng soalnya masih agak sepi..."
    hide kana
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Oh tadi sepi ya, agak telat berarti aku dateng haha..."
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near
    with dissolve
    "[mcname!c]" "Hahahaha..."
    hide kana_drylaugh
    show kana at kana_near
    with dissolve
    "Tidak lama kemudian datang pelayan cafe yang membawa pesanan yang dipesan Kana."
    "Pelayan" "Maaf menunggu..."
    "Pelayan" "Ini ya kak pesanan strawberry shortcake sama lemon teanya."
    "Pelayan meletakan pesanan ke atas meja."
    hide kana_smile
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Eh cakenya sudah datang aku makan dulu ya."
    hide kana_side_talk
    hide kana_talk
    show kana_smile at kana_near
    with dissolve
    "[mcname!c]" "I-iya."
    "[mcname!c]" "..."
    "[mcname!c]" "{i}Aduh gimana nih, bisa-bisa nya pas aku lagi pengen santai gini malah duduk barengan sama cewek.{/i}"
    "Tidak ingin dikira aneh, akhirnya [mcname!c] pun melanjutkan menikmati pesanannya."
    "[mcname!c] dan Kana fokus terhadap apa yang ada di depannya, sesekali [mcname!c] melirik ke arah Kana."
    hide kana_smile
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Ummm, kamu mau juga?"
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near
    with dissolve
    "Mungkin sadar kalau [mcname!c] memperhatikannya, Kana menawarkan cake yang sedang ia makan."
    "[mcname!c]" "Eh engga kok haha..."
    hide kana_talk
    show kana_smile at kana_near
    with dissolve
    "Mendengar hal tesebut Kana lanjut memakan cake-nya."
    "Karena moment nya canggung, [mcname!c] melihat sekeliling untuk mencari topik yang dibahas namun hasilnya nihil, tidak ada sesuatu yang menarik untuk dibahas di dalam cafe."
    "[mcname!c]" "..."
    "[mcname!c]" "Ternyata kamu suka banget strawberry shortcakenya, ya?"
    hide kana_smile
    show kana at kana_near
    with dissolve
    "Melihat Kana fokus memakan cake [mcname!c] mencoba membawa topik strawberry shortcake."
    hide kana
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "I - iyah."
    hide kana_side_talk
    hide kana_talk
    show kana_smile at kana_near
    with dissolve
    "[mcname!c]" "...."
    "[mcname!c]" "{i}Kehabisan topik lagi...{/i}"
    "[mcname!c]" "Pelayann! Pesan strawberry shortcake 1."
    "Mencoba untuk menghilangkan canggung, akhirnya [mcname!c] memesan makanan lagi."
    hide kana_smile
    show kana_confused at kana_near
    with dissolve
    "Bingung karena [mcname!c] memesan lagi, Kana melihat bolak-balik antara [mcname!c] dan pelayan."
    "Menyadari Kana yang kebingungan, [mcname!c] pun memberikan alasannya."
    "[mcname!c]" "Ngeliat kamu makan enak banget. Jadinya penasaran mau coba, hehe."
    hide kana_confused
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Eh…. padahal udah ditawarin tadi."
    hide kana_side_talk
    hide Kana_talk
    show kana at kana_near
    with dissolve
    "[mcname!c]" "Hahaha."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene cafe with Dissolve(1.0)
    $ quick_menu = True
    "Pelayan" "Maaf menunggu."
    "Pelayan" "Ini ya kak pesanannya strawberry shortcake."
    "Melihat cake yang diletakkan di atas meja tampak menggiurkan."
    "[mcname!c] pun memasukkan potongan strawberry shortcake ke mulutnya."
    hide kana_confused
    show kana_smile at kana_near
    with dissolve
    "Tiba-tiba [mcname!c] pun merasakan sensasi yang belum pernah dia rasakan sebelumnya, Rasa manis dan asam stroberi seakan menari di lidahnya, memberikan kenikmatan yang tak tertandingi."
    "Setiap gigitan membawa [mcname!c] ke dalam dunia yang penuh dengan kebahagiaan sederhana. [mcname!c] pun menutup matanya, membiarkan rasa itu menyelimutinya sepenuhnya."
    "[mcname!c]" "Hmmmmm, enak juga ya."
    hide kana_smile
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Ya kannn? Makanya aku pengen banget makan di sini."
    hide kana_side_talk
    hide Kana_talk
    show kana_smile at kana_near
    with dissolve
    "[mcname!c]" "Makanya tadi kamu langsung duduk di bangku yang kosong, ya?"
    hide kana_smile
    show kana_shy at kana_near
    with dissolve
    hide kana_shy
    show kana_shy_smile at kana_near
    show kana_side_shy_smile at left
    with dissolve
    kana "Hehehe."
    hide kana_side_shy_smile
    hide kana_shy_smile
    show kana_shy at kana_near
    with dissolve
    "[mcname!c]" "Tapi makasih, loh. Berkat kamu, aku jadi tau enaknya strawberry shortcake ini."
    hide kana_shy
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Aku juga makasih. Aku jadi bisa makan di sini hari ini."
    hide kana_side_talk
    hide kana_talk
    show kana_smile at kana_near
    with dissolve
    "[mcname!c] dan Kana pun saling melemparkan senyuman sambil menikmati strawberry shortcake di cafe tersebut."
    "[mcname!c]" "..."
    kana "..."
    hide kana_smile with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Cafe Sore.ogg" fadein 1.0
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Tak terasa langit menjadi gelap..."
    $ quick_menu = False
    scene cafe malam with Dissolve(2.0)
    show kana_talk at kana_near with dissolve
    $ quick_menu = True
    "Waktu berlalu dengan cepat karena [mcname!c] dan Kana asik mengobrol."
    "Tapi, tibalah waktu untuk mereka pulang ke rumah\nmasing-masing."
    show kana_side_talk at left with dissolve
    kana "Ummm. Makasih ya udah dibolehin duduk di sini, untung saja aku bisa makan strawberry shortcakenya, kalau enggak kayaknya aku bakalan marah deh hahaha."
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near
    with dissolve
    "[mcname!c]" "Haha, gapapa kok santai aja. Kebetulan kursinya kosong di situ."
    hide kana
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "Eh udah jam segini aku harus pulang aku duluan ya, kamu hati-hati di jalan."
    hide kana_side_talk
    hide kana_talk
    show kana_smile at kana_near
    with dissolve
    "[mcname!c]" "Okee, kamu juga hati-hati di jalan ya."
    hide kana_smile
    show kana_talk at kana_near
    show kana_side_talk at left
    with dissolve
    kana "See you~"
    hide kana_side_talk
    hide kana_talk
    with dissolve
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" fadein 1.0 volume (0.8)
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Pulang dari cafe..."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(2.0)
    $ quick_menu = True
    "Di kost, [mcname!c] masih memikirkan kejadian yang dialaminya hari ini."
    "[mcname!c]" "{i}Banyak juga ya, hal yang terjadi pada hari pertamaku di Jakarta.{/i}"
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
    show kana_smile at kana_near with dissolve
    "[mcname!c]" "{i}Aku gak nyangka kalau hari ini bakalan bisa ngobrol sama dia.{/i}"
    "[mcname!c]" "{i}Tapi dipikir-pikir, dia ramah juga ya...{/i}"
    "[mcname!c]" "{i}Aku kira, dia bakalan kaya cool dan cuek gitu.{/i}"
    "[mcname!c]" "{i}Ternyata nyambung juga kalau diajak ngobrol.{/i}"
    hide white
    hide white2
    hide kana_smile
    with Dissolve(1.0)
    "[mcname!c]" "{i}Udah ah mending aku tidur.{/i}"
    "[mcname!c] pun tertidur dengan lelap..."
    jump chapter1kana2Campus

label chapter1kana2Campus:
    ##$ renpy.block_rollback()
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kampus.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya.."
    $ quick_menu = False
    scene depan kampus with Dissolve(2.0)
    play sound "audio/run.mp3" fadein 1.0 volume (10.0)
    $ quick_menu = True
    "Terdengar suara langkah kaki yang terburu-buru..."
    "[mcname!c]" "{i}Sial ternyata aku benar-benar meremehkan Jakarta.{/i}"
    "[mcname!c]" "{i}Siapa sangka macet di sini parah banget...{/i}"
    "Takut terlambat di hari pertama, [mcname!c] terburu-buru memasuki kelas kuliahnya."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene lorong with Dissolve(1.0)
    $ quick_menu = True
    "[mcname!c]" "Ehhhh tungguuuu!!"
    "[mcname!c] berlari menuju lift yang akan tertutup."
    "Di dalam lift terlihat seorang cewek yang sepertinya juga mau menuju ke kelas..."
    $ quick_menu = False
    play sound "audio/ding.mp3"
    show lift at lift_center with dissolve
    $ quick_menu = True
    "[mcname!c]" "Huft… huft… huft."
    "[mcname!c]" "Untung keburu buat masuk lift..."
    "[mcname!c]" "Makasih ya udah mau nahan liftnya."

    show freya_side_talk at left
    with dissolve
    "???" "Haha iya, sama-sama."
    hide freya_side_talk
    with dissolve
    "Sibuk menarik nafas dari olahraga pagi yang tidak direncanakan tadi, [mcname!c] tidak terlalu memperhatikan perempuan yang ada di lift."
    "[mcname!c]" "Huft... huft...."
    "[mcname!c]" "{i}Kayaknya aku harus ningkatin staminaku lagi nih.{/i}"
    play sound "audio/ding.mp3"
    $ quick_menu = False
    hide lift
    show freya at char_center 
    with dissolve
    $ quick_menu = True
    "Setelah lift berhenti, [mcname!c] mencoba melirik perempuan yang ada di dalam lift."
    "[mcname!c]" "{i}Memang ya, cewek di Jakarta ini cantik-cantik semua...{/i}"
    "[mcname!c]" "Ah! Terima kasih lagi yak, sudah nahan lift tadi."
    "[mcname!c] kemudian lanjut berlari menuju kelas."
    hide freya with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kelas.ogg" fadein 1.0 volume(1.5)
    scene kelas with Dissolve(1.0)
    ##$ renpy.block_rollback()
    $ quick_menu = True
    "[mcname!c] pun memasuki ruangan kelas."
    "Ini pertama kalinya ia memasuki ruangan yang luas dan besar seperti itu, selain di aula."
    "[mcname!c]" "{i}Fiuhh, untung aja kelasnya belum dimulai.{/i}"
    "[mcname!c] pun melihat ke sekeliling kelas."
    "[mcname!c]" "......."
    "[mcname!c]" "{i}Kok masih sepi kelasnya yah?{/i}"
    "Dikarenakan masih banyak kursi yang kosong, [mcname!c] memilih untuk duduk di bagian belakang terlebih dahulu agar dekat dengan pintu keluar-masuk dan tidak ingin mencolok untuk hari-hari pertama ini."
    "Saat [mcname!c] akan duduk, terdengar suara perempuan yang membuatnya langsung melihat ke belakang..."
    show freya_talk at char_center
    show freya_side_talk at left
    with dissolve
    freya "Kok buru-buru amat?"
    freya "Santai aja napa?"
    freya "Lagian masih jam segini."
    freya "Atau…"
    freya "Kamu ngincer posisi paling depan, nih? Haha."    
    hide freya_side_talk
    hide freya_talk
    show freya_smug at char_center
    with dissolve
    "[mcname!c] pun sadar bahwa perempuan itu adalah perempuan yang sama yang telah menahan pintu lift untuknya."
    "[mcname!c]" "Hahh, astagaa. Aku kira udah mulai loh kelasnya. Aku sampe\nlari-lari kan tadi?"
    "[mcname!c]" "Aduhh, ya udah deh yang penting datang aja dulu."
    "[mcname!c]" "Eh kamu kan yang tadi di lift ya?"
    hide freya_smug
    show freya_smile at char_center
    with dissolve
    "Perempuan itu tersenyum kecil dan manis."
    hide freya_smile
    show freya_talk at char_center
    show freya_side_talk at left
    with dissolve
    freya "Hahaha, makanya tadi aku liat kamu lari-lari lucu banget deh."
    freya "Kok bisa sih, ada orang yang langsung lari-lari gitu padahal masih hari pertama."
    hide freya_side_talk
    hide freya_talk
    show freya at char_center
    with dissolve
    "[mcname!c] melihat ke arah jam tangannya dan ia pun sadar." 
    hide freya
    show freya_smile at char_center
    with dissolve
    "[mcname!c]" "Aduhhh pantes aja aku lari-lari, jam tanganku mati. Ku kira udah telat."
    hide freya_smile
    show freya_talk at char_center
    show freya_side_talk at left
    with dissolve
    freya "Haha ada-ada deh kamu. Lain kali pastiin aja dulu deh."
    hide freya_side_talk
    hide freya_talk
    show freya at char_center
    with dissolve
    "[mcname!c]" "Eh dari tadi kita ngobrol belum kenalan ternyata."
    "[mcname!c]" "Boleh kali ya, kita kenalan dulu haha."
    "[mcname!c]" "Kenalin namaku [mcname!c]."
    "[mcname!c]" "Aku dari Ngawi."
    "[mcname!c]" "Salam kenal, ya~"
    $ freya_name = "Freya"
    hide freya
    show freya_talk at char_center
    show freya_side_talk at left
    with dissolve
    freya "Eh, salam kenal juga namaku Freya, asalku dari Yogyakarta."
    show freya at char_center
    hide freya_talk
    hide freya_side_talk
    with dissolve
    "[mcname!c]" "{i}Dia ternyata imut juga ya...{/i}"
    "[mcname!c]" "{i}Apa sih, kalau kata orang-orang di internet sekarang.{/i}"
    "[mcname!c]" "{i}Owh iya!{/i}"
    "[mcname!c]" "{i}Senyumannya manis kaya karamel.{/i}"
    hide freya with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play sound "audio/crowd_noise.mp3" loop fadein 1.0 volume (4.0)
    scene kelas with Dissolve(1.0)
    $ quick_menu = True

    #if kana_name == "Perempuan itu":
    if mc_from == "Kos":
        "Saat mengobrol, para Mahasiswa/i pun terdengar mulai memasuki ruangan kelas."
        hide freya_smile
        show freya at freya_near_right
        show kana at kana_near_left_2
        with dissolve
        "Seorang perempuan pun duduk di sebelah Freya dan dilihat oleh [mcname!c]."
        "Ternyata perempuan itu adalah perempuan yang menjadi bahan pembicaraan saat pembukaan Mahasiswa/i baru."
        hide freya
        hide kana
        show freya_shock at freya_near_right
        show kana_drylaugh at kana_near_left_2
        with dissolve
        "Saat itu pun, Freya terlihat akrab dengan perempuan tersebut dan [mcname!c] memilih untuk tidak mencampuri urusan mereka."
        "Akan tetapi, dari kejauhan terdengar beberapa kalimat samar yang terdengar oleh telinga [mcname!c]."
        stop sound fadeout 1.0
    elif mc_from == "Cafe":
        "Saat mengobrol, para Mahasiswa/i pun terdengar mulai memasuki ruangan kelas"
        hide freya_smile
        show freya at freya_near_right
        show kana at kana_near_left_2
        with dissolve
        "Seorang perempuan pun duduk di sebelah Freya dan dilihat oleh [mcname!c]."
        #"Ternyata perempuan itu adalah [kana_name] perempuan yang menjadi bahan pembicaraan saat pembukaan Mahasiswa/i baru"
        "Ternyata perempuan itu adalah Kana."
        hide freya
        hide kana
        show freya_shock at freya_near_right
        show kana_drylaugh at kana_near_left_2
        with dissolve
        "Saat itu pun, Freya terlihat akrab dengan Kana. Sehingga [mcname!c] memilih untuk tidak mencampuri urusan mereka."
        "Akan tetapi, dari kejauhan terdengar beberapa kalimat samar yang terdengar oleh telinga [mcname!c]."
        stop sound fadeout 1.0
    "{size=-5}Mahasiswa A{/size}" "Ehh liat dia modis banget pakaiannya..."
    "{size=-5}Mahasiswa B{/size}" "Iyaaa cantik banget yaa."
    "{size=-5}Mahasiswa B{/size}" "Eh bukanya dia anak orang kaya yang katanya sepupunya rektor itu ya?"
    "{size=-5}Mahasiswa B{/size}" "Eh lo ajak ngobrol sana siapa tau bisa lo deketin..."
    #if kana_name == "Perempuan itu":
    if mc_from == "Kos":
        "[mcname!c]" "{i}Mereka ngobrolin perempuan di sebelah Freya, ya?{/i}"
        "[mcname!c]" "{i}Tapi kalau dilihat-lihat, memang modis sih pakaiannya.{/i}"
        "[mcname!c]" "{i}Dia juga kenal deket sama Freya, ya?{/i}"
        hide freya_shock
        hide kana_drylaugh
        show kana_smile at kana_near
        with dissolve
        "Perempuan itu pun menyadari bahwa di sebelahnya Freya itu adalah [mcname!c] dan akhirnya senyum tipis muncul dari wajahnya."
        hide kana_smile
        show kana at kana_near
        with dissolve
        "Tiba-tiba, suara pintu pun berbunyi..."
    elif mc_from == "Cafe":
        "[mcname!c]" "{i}Mereka ngobrolin Kana, ya?{/i}"
        "[mcname!c]" "{i}Tapi kalau dilihat-lihat, memang modis sih pakaiannya...{/i}"
        "[mcname!c]" "{i}Dia juga kenal deket sama Freya, ya?{/i}"
        hide freya_shock
        hide kana_drylaugh
        show kana_smile at kana_near
        with dissolve
        "Kana pun menyadari bahwa di sebelahnya Freya itu adalah [mcname!c] dan akhirnya senyum tipis muncul dari wajahnya." 
        hide kana_smile
        show kana at kana_near
        with dissolve
        "Saat dia akan menyapa [mcname!c], suara pintu pun berbunyi..."
    hide kana with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    play sound "audio/open_door.mp3" fadein 1.0 volume (15.0)
    scene black with Dissolve(1.0)
    play music "audio/BGM_Dosen.ogg" fadein 1.0
    scene kelas with Dissolve(1.0)
    ##$ renpy.block_rollback()
    show dosen at dosen_center with dissolve
    $ quick_menu = True
    "Dosen pun memasuki ruangan kelas..."
    "Kelas pun menjadi tenang dan lebih tertib dari sebelumnya..."
    show dosen_side_talk at left
    show dosen_talk at dosen_center
    hide dosen
    with dissolve
    dosen "Selamat siang mahasiswa dan mahasiswi sekalian..."
    dosen "Selamat datang di mata kuliah pertama kalian di jenjang perkuliah ini."
    $ dosen_name = "Bu Fatimah"
    dosen "Sebelumnya perkenalkan nama saya Fatimah."
    dosen "Disini saya mengajar mata kuliah Teori Politik Internasional, Studi Perang Dan Damai, Strategi Dan Tatakelola Strategis."
    dosen "Untuk semester pertama kalian akan mempelajari mata kuliah dasar yaitu Teori Politik Internasional."
    dosen "Dengan begitu saya akan langsung ke dalam materi."
    hide dosen_side_talk
    hide dosen_talk
    show dosen at dosen_center
    with dissolve
    "Suasana kelas pun terasa hening, fokus untuk memperhatikan apa yang dijelaskan oleh Bu Fatimah."
    hide dosen with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Sore.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True 
    "Beberapa jam kemudian..."
    $ quick_menu = False
    scene kelas sore with Dissolve(2.0)
    show dosen_talk at dosen_center
    show dosen_side_talk at left with dissolve
    $ quick_menu = True
    dosen "Baiklah semuanya karena waktu saya sudah habis..."
    dosen "Maka mata kuliah hari ini sudah selesai."
    hide dosen_side_talk
    hide dosen_talk
    show dosen at dosen_center
    with dissolve
    "Terdengar suara lega dari para mahasiswa."
    hide dosen
    show dosen_talk at dosen_center
    show dosen_side_talk at left
    with dissolve
    dosen "Tapi sebelum itu..."
    dosen "Saya akan memberikan tugas kelompok yang berisikan 4 orang."
    dosen "Minggu depan dikumpulkan ya!!"
    hide dosen_side_talk
    hide dosen_talk
    show dosen at dosen_center
    with dissolve
    "Mendengar hal tersebut, para mahasiswa mengeluarkan suara kekecewaan."
    hide dosen
    show dosen_talk at dosen_center
    show dosen_side_talk at left
    with dissolve
    dosen "Jadi kelompoknya akan dibagi berdasarkan jajaran tempat duduk kalian saja agar simple dan tidak ada circle di antara kalian semua."
    dosen "Lalu gunakan kesempatan ini untuk berkenalan dengan teman-teman sekelas kalian."
    dosen "Sekian untuk hari ini."
    dosen "Terima kasih banyak."
    hide dosen_side_talk
    hide dosen_talk
    with dissolve
    "[mcname!c]" "{i}Aduh, satu jajaran!!??{/i}"
    "[mcname!c]" "{i}Tunggu bentar, kalau satu jajar…??{/i}"
    #"*SFX LIRIK KANAN KIRI*"
    if mc_from == "Kos":
        "[mcname!c]" "{i}Eh, aku sama cewek itu!!!{/i}"
        show kana_talk at kana_near_left_2
        show kana_side_talk at left
        with dissolve
        "???" "Eh, halo. Kita satu kelompok, ya..."
        hide kana_side_talk
        hide kana_talk
        show kana_smile at kana_near_left_2
    else:
        $ kana_name = "Kana"
        "[mcname!c]" "{i}Eh, aku sama Kana!!!{/i}"
        show kana_talk at kana_near_left_2
        show kana_side_talk at left
        with dissolve
        kana "Kita satu kelompok, ya. Mohon bantuannya~"
        hide kana_side_talk
        hide kana_talk
        show kana_smile at kana_near_left_2
    show freya_talk at freya_near_right
    show freya_side_talk at left
    with dissolve
    freya "Eeh, iyaa. Kita satu kelompok, nih. Kebetulan banget ya, haha."
    hide freya_side_talk
    hide freya_talk
    show freya at freya_near_right
    hide kana_smile
    show kana_talk at kana_near_left_2
    show kana_side_talk at left with dissolve
    if mc_from == "Kos":
        kana " Mohon bantuannya, ya. Sebelumnya, kenalkan namaku Kanaia Asa. Panggil aku Kana ya..."
    kana "Eh, kamu sini dong. Kan kita juga satu kelompok..."
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near_left_2
    show galaxy_talk at galaxy_center
    show galaxy_side_talk at left
    with dissolve
    galaxy "Owh iya. Siang semuanya."
    $ mahasiswa_name = "Galaxy"
    galaxy "Sebelumnya, kenalin nama gue Galaxy."
    galaxy "Gue dari Pekalongan. Salam kenal~"
    hide galaxy_side_talk
    hide galaxy_talk
    show galaxy at galaxy_center
    with dissolve
    "Freya, Kana, [mcname!c], dan Galaxy pun saling bertukar sapa dan mengobrol lebih lanjut."
    hide galaxy
    hide freya
    hide kana
    with dissolve
    "Akhirnya, mereka pun membuat grup chat untuk membahas pekerjaan kelompok mereka."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" fadein 1.0 volume (0.8)
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Di kost..."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(2.0)
    ##$ renpy.block_rollback()
    $ quick_menu = True 
    "Sesampainya di kost, [mcname!c] pun membuang tasnya ke lantai lalu melepaskan sepatu dan menghempaskan tubuhnya ke kasur."
    "Setelah capek dengan kegiatan hari ini, datang ke kos membuat [mcname!c] merasakan ketenangan di balik hiruk pikuk Kota Jakarta."
    "Memejamkan mata, menghela nafas, dan merenungkan kembali kegiatan yang telah terjadi hari ini."
    play sound "ReceiveText.ogg" loop volume (2.0)
    "[mcname!c]" "Duh. Notif WA nih."
    stop sound
    "[mcname!c]" "Apa nih? Dari Mamah, kah?"
    "[mcname!c] mencoba mengecek HPnya."
    "[mcname!c]" "{i}Oh, ternyata bukan...{/i}"
    "[mcname!c]" "{i}Ternyata notif dari grup chat.{/i}"
    $ quick_menu = False
    stop music fadeout 1.0
    jump phoneChat

label chapter1kana3:
    ##$ renpy.block_rollback()
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kantin.ogg" loop fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya..."
    $ quick_menu = False
    play sound "audio/crowd_noise.mp3" loop fadein 1.0 volume (4.0)
    scene kantin with Dissolve(2.0)
    $ quick_menu = True
    "Kantin Nama_Kampus, tempat para mahasiswa untuk melepaskan lapar dan haus sehabis belajar seharian."
    "Karena sudah jam makan siang, suasana kantin terasa sangat ramai dan tempat duduk pun terlihat hampir penuh diisi oleh para mahasiswa."
    "[mcname!c]" "{i}Wahhhh, rame juga ya...{/i}"
    "[mcname!c]" "{i}Mungkin karena sudah jam makan siang??{/i}"
    "[mcname!c]" "{i}Bentar. Kalau gini caranya, gimana dapet tempat duduk?{/i}"
    "[mcname!c]" "{i}Masa aku harus bungkus makanannya, sih?{/i}"
    "[mcname!c]" "{i}Perdana makan di kantin, ga enak rasanya kalo dibungkus.{/i}"
    "Merasa kecewa, [mcname!c] pun berniat untuk pergi mencari makanan di tempat lain..."
    "Saat [mcname!c] ingin melangkah pergi, ia melihat seseorang yang melambaikan tangannya dari kejauhan seakan memanggilnya."
    show freya_shock at small_center
    show freya_side_shock at left
    with dissolve
    "Freya" "[mcname!u]!! SINI!!!"
    "Freya" "Duduk bareng kita!!"
    hide freya_side_shock
    hide freya_shock
    show freya at small_center
    with dissolve
    "Setelah diperhatikan lagi, ternyata itu adalah Freya."
    "Mendengar hal tersebut akhirnya [mcname!c] menghampiri ke meja Freya. Di sana ternyata ada [kana_name] yang juga duduk di sampingnya."
    hide freya
    show kana at kana_near_left_2
    show freya_talk at freya_near_right
    show freya_side_talk at left
    with dissolve
    freya "Eh sini."
    freya "Duduk di sini."
    freya "Soalnya udah rame juga kan?"
    freya "Gapapa kan, Nay?"
    hide freya_side_talk
    hide freya_talk
    show freya at freya_near_right
    hide kana
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Iya. Gapapa kok. Lagian di sini kosong."
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near_left_2
    with dissolve
    "Mendengar persetujuan mereka, dengan lega [mcname!c] duduk berhadapan dengan mereka."
    hide freya
    hide kana
    with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    stop sound fadeout 1.0
    scene kantin with Dissolve(1.0)
    show kana at kana_near_left_2
    show freya at freya_near_right
    with dissolve
    $ quick_menu = True
    "[mcname!c]" "Akhirnya dapat duduk juga..."
    "[mcname!c]" "Makasih banget loh. Aku kira aku gak bakalan dapet tempat."
    hide freya
    show freya_talk at freya_near_right
    show freya_side_talk at left
    with dissolve
    freya "Santai aja..."
    freya "Iya kan, Nay?"
    hide freya_side_talk
    hide freya_talk
    show freya at freya_near_right
    hide kana
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Iya, hehe."
    hide kana_talk
    show kana at kana_near_left_2
    hide kana_side_talk
    with dissolve
    "[mcname!c]" "Nay? itu nama panggilanmu, [kana_name]?"
    hide kana_smile
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Iya, aku biasanya dipanggil \"Nay\" kalau sama [freya_name]."
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near_left_2
    with dissolve
    hide freya
    show freya_talk at freya_near_right
    show freya_side_talk at left
    with dissolve
    freya "Haha. Udah kebiasaan manggilnya \"Nay\"."
    freya "Jadinya, kaya gini. Hehe."
    hide freya_side_talk
    hide freya_talk
    show freya_smile at freya_near_right
    with dissolve
    hide kana
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Ingyah, aku udah kenal sama [freya_name] dari lama."
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near_left_2
    with dissolve
    hide freya_smile
    show freya_talk at freya_near_right
    show freya_side_talk at left
    with dissolve
    freya "Oh iya."
    freya "Besok jadi kerja kelompoknya, kan?"
    hide freya_side_talk
    hide freya_talk
    show freya at freya_near_right
    with dissolve
    "[mcname!c]" "Jadi dong."
    "[mcname!c]" "Nanti jangan lupa kabarin si [mahasiswa_name]."
    play sound "audio/hungry.mp3" fadein 1.0 volume (10.0)
    hide kana
    show kana_shy_talk at kana_near_left_2
    with dissolve
    "Saat asik mengobrol tentang kerja kelompok, terdengar suara perut keroncongan."
    stop sound fadeout 1.0
    "[mcname!c]" "Suara apaan tuh?"
    hide kana
    hide kana_shy_talk
    show kana_shy_closeeye_talk at kana_near_left_2
    with dissolve
    "[mcname!c] mencoba mencari sumber suara tersebut dan menyadari Kana sedang tertunduk malu sambil menutup mukanya."
    "[mcname!c] dan Freya melihat ke arah Kana sambil tertawa kecil."
    hide freya
    show freya_smile at freya_near_right
    show freya_side_smile at left
    with dissolve
    freya "Pffttt!"
    hide freya_side_smile with dissolve
    "[mcname!c]" "Hahaha, yaudah aku juga pesen deh..."
    "[mcname!c]" "Perutku juga sudah mulai lapar nih."
    hide freya_smile
    show freya_talk at freya_near_right
    show freya_side_talk at left
    with dissolve
    freya "Hahahahaha!"
    freya "Ya udah sana."
    freya "Kalian pesen aja dulu."
    freya "Nanti, kita ngobrol lagi..."
    hide freya_side_talk
    hide freya_talk
    show freya at freya_near_right
    with dissolve
    "[mcname!c] mengangkat tangan sambil berteriak memanggil Mbak kantin."
    hide kana_shy_talk
    show kana_shy at kana_near_left_2
    with dissolve
    "Dengan muka sedikit tersipu malu, Kana mencuri pandang melihat ke arah [mcname!c]."
    "[mcname!c]" "Mbaaak. Mau pesen..."
    hide kana_shy
    show kana at kana_near_left_2
    with dissolve
    "[mcname!c] ngeliat menu yang tersedia di kantin..."
    menu:
        "[mcname!c] ngeliat menu yang tersedia di kantin..."
        "Pesen Ayam Addo Smack Down":
            stop music fadeout 1.0
            $ quick_menu = False
            play music "BGM_Bad End.ogg" fadein 1.0
            scene black with Dissolve(2.0)
            show text "{color=#FFF}LO KEPEDESAN DAN AKHIRNYA MALAH KE WC TERUS TERUSAN DARIPADA NGOBROL SAMA MEREKA{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3"
            jump credits
        "Pesen Mie Kodoknya Cepio":
            jump chapter1kana3mie
        "Pesen Lotek Sadao Maou":
            stop music fadeout 1.0
            $ quick_menu = False
            play music "BGM_Bad End.ogg" fadein 1.0
            scene black with Dissolve(2.0)
            show text "{color=#FFF}SAYURAN YANG LO MAKAN TERNYATA BASI{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FFF}AKHIRNYA LO KERACUNAN MAKANAN.{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FFF}MBAK YANG JUALAN PUN AKHIRNYA DIMARAHIN KARENA UDAH BIKIN MAHASISWANYA KERACUNAN MAKANAN{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3"
            jump credits

label chapter1kana3mie:
    ##$ renpy.block_rollback()
    "[mcname!c] pun memilih mie sebagai makanan yang ia pesan. Kana yang masih menahan malu, memesan makanan yang sama dengan [mcname!c]."
    hide freya
    show freya_shock at freya_near_right
    show freya_side_shock at left
    with dissolve
    freya "Hahaha emang belum makan dari kapan, Nay?"
    hide freya_side_shock
    hide freya_shock
    show freya_smug at freya_near_right
    with dissolve
    hide kana_shy
    show kana_shy_talk at kana_near_left_2
    show side kana_side_shy_talk at left
    with dissolve
    kana "Iiih apaan sih. Udahan dong."
    hide side kana_side_shy_talk
    hide kana_shy_talk
    show kana_shy at kana_near_left_2
    with dissolve
    "[mcname!c]" "Kalian dekat banget ya~"
    "[mcname!c]" "Dulu satu sekolah, kah?"
    hide freya_smug
    show freya_talk at freya_near_right
    show freya_side_talk at left
    with dissolve
    freya "Iya."
    freya "Aku dan Kana dari TK sampai sekarang satu kelas mulu."
    hide freya_side_talk
    hide freya_talk
    show freya at freya_near_right
    with dissolve
    show kana_side_cry at left with dissolve
    kana "Hmpph."
    hide kana_side_cry with dissolve
    "[mcname!c]" "Waaah. Enak ya, sudah kenal dari lama."
    hide freya
    show freya_talk at freya_near_right
    show freya_side_talk at left
    with dissolve
    freya "Hehe. Kamu gatau kan?"
    freya "Kalau Kana dulu tuh-"
    hide freya_side_talk
    hide freya_talk
    show freya at freya_near_right
    with dissolve
    stop music fadeout 1.0
    "Sebelum Freya menyelesaikan omongannya, Kana mencoba menutup mulut freya."
    play music "BGM_Kana Pon.ogg" fadein 1.0
    hide kana_shy
    show kana_shy_talk at kana_near_left_2
    show side kana_side_shy_talk at left
    with dissolve
    kana "Ehem."
    kana "Kamu tau gak kalau dulu yang pertama kali mengakui kemerdekaan Indonesia adalah Mesir."
    hide side kana_side_shy_talk
    hide kana
    show freya_smug at freya_near_right
    with dissolve
    "Kana mencoba mengalihkan pembicaraan Kana memberikan fun fact random."
    "{size=-5}[freya_name] & [mcname!c]{/size}" "..."
    "Melihat fun fact yang dikatakannya tidak berhasil, akhirnya Kana mencoba untuk memberikan funfact yang lainnya..."
    "Merasa kelakuan temannya yang mulai aneh, Freya kemudian meletakkan telapak tangannya ke dahi Kana sambil tertawa jahil."
    hide freya_smug
    hide kana_shy_talk
    show kana_shy at kana_near_left_2
    show freya_shock at freya_near_right
    show freya_side_shock at left
    with dissolve
    freya "Waduh kambuh..."
    freya "GWS."
    hide freya_side_shock with dissolve
    hide kana_talk
    show freya_smug at freya_near_right
    show kana_shy_talk at kana_near_left_2
    show kana_side_cry at left
    with dissolve
    kana "Hmpph!"
    kana "{size=-10}Kan gara-gara kamu juga...{/size}"
    hide kana_side_cry with dissolve
    stop music fadeout 1.0
    "Seakan menjadi penyelamat, Mbak kantin pun datang membawakan pesanan mereka..."
    play music "BGM_Kantin.ogg" fadein 1.0
    show kana at kana_near_left_2
    hide kana_shy_talk
    with dissolve
    "Mbak Kantin" "Ini ya pesanannya."
    hide freya_shock
    hide kana_angry
    show freya at freya_near_right
    show kana at kana_near_left_2
    with dissolve
    "Mata Kana bersinar, melihat datangnya Mbak kantin yang membawa makanan."
    hide kana
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Makanannya sudah datang, nih~"
    kana "Yuk makan dulu~"
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near_left_2
    with dissolve
    "Kana mencoba untuk mengalihkan pembicaraan..."
    "[mcname!c]" "Yaudah. Mari makan."
    hide freya
    show freya_shock at freya_near_right
    show freya_side_shock at left
    with dissolve
    freya "Eh… Eeee. Tadi mesen Mie ayam?"
    freya "Tumben kamu makan yang begituan, Nay?"
    hide freya_side_shock
    hide freya_shock
    hide kana
    show kana_angry at kana_near_left_2
    with dissolve
    "Seolah masih ingin membahas masalah tadi, Freya menanyakan hal tersebut."
    "[mcname!c]" "Hmm? Memangnya ada apa?"
    hide kana_angry
    show kana_confused at kana_near_left_2
    show kana_side_confused at left
    with dissolve
    kana "Freee. Yuk makan..."
    hide kana_side_confused with dissolve
    "Kana berbicara dengan nada agak kesal."
    hide freya_shock
    show freya_talk at freya_near_right
    show freya_side_talk at left
    with dissolve
    freya "Hehehehe. Iya deh."
    hide freya_side_talk
    hide freya_talk
    show freya at freya_near_right
    with dissolve
    "Tertawa, Freya akhirnya berhenti membahas topik tersebut."
    "Karena sudah lapar, [mcname!c] mulai memakan makanan yang sudah dihidangkan."
    hide kana_confused
    hide freya
    show kana_talk at kana_near_left_2
    show freya_shock at freya_near_right
    with dissolve
    "Sesekali, [mcname!c] melihat Kana dan Freya yang saling berbincang kecil."
    "Lalu [mcname!c] kembali berfokus ke sepasang sumpit yang digunakan untuk menarik helaian mie ke mulutnya."
    hide freya_shock
    hide kana_talk
    show kana_smile at kana_near_left_2
    show freya_smile at freya_near_right
    with dissolve
    "Ada kalanya Freya dan Kana menyertakan [mcname!c] dalam pembicaraan mereka."
    "Satu percakapan berlanjut ke percakapan lainnya, membuat mereka merasa menjadi lebih dekat."
    hide kana_smile 
    hide freya_smile
    hide freya_smug 
    hide kana_shy
    hide kana_shy_closeeye_talk 
    with dissolve
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play music "BGM_Sore.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    ##$ renpy.block_rollback()
    $ quick_menu = True
    "Setelah selesai makan, mereka pergi dan berpisah ke urusannya masing-masing."
    "[mcname!c] pun memikirkan apa yang akan dilakukan selanjutnya."
    # Menunya agak aneh, tiba2 langsung besok
    menu:
        "Yang kamu lakukan...."
        "Keliling Kampus dan melihat lihat isi kampus":
            ##$ renpy.block_rollback()
            $ quick_menu = False
            scene black with Dissolve(1.0)
            scene kampus sore with Dissolve(1.0)
            $ quick_menu = True
            "[mcname!c]" "{i}Aku memilih menghabiskan waktu untuk berkeliling di sekitar kampus.{/i}"
            "Di perjalanan pertama, [mcname!c] melihat ada parkiran yang biasa dipakai anak-anak jurusan HI untuk memarkirkan kendaraan mereka..."
            "Terlihat disana banyak kendaraan yang bisa dibilang lumayan mahal."
            "[mcname!c]" "{i}Hmmmm luas juga parkiran buat kampus ini.{/i}"
            "[mcname!c]" "{i}Seperti yang diharapkan dengan kampus Ibu Kota.{/i}"
            "[mcname!c]" "{i}Terasa sangat berbeda dibandingkan dengan bangunan yang ada di desa.{/i}"
            "Entah kenapa [mcname!c] tiba-tiba terbayang sosok Kana di aula waktu itu."
            $ quick_menu = False
            window auto hide
            show kana awal senyum with Dissolve(1.0)
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
            window auto show
            $ quick_menu = True 
            "[mcname!c]" "{i}Aduhhh sadar woi sadar.{/i}"
            $ quick_menu = False
            scene black with Dissolve(1.0)
            scene kampus sore with Dissolve(1.0)
            $ quick_menu = True
            "[mcname!c] pun menggeleng gelengkan kepala untuk kembali fokus pada perjalanannya mengelilingi kampus."
            $ quick_menu = False
            scene black with Dissolve(1.0)
            # Harusnya BG Sawah
            scene sawah sore with Dissolve(1.0)
            $ quick_menu = True
            "[mcname!c]" "{i}Sawah ya…{/i}"
            "[mcname!c]" "{i}Gak nyangka bakal ngeliat sesuatu yang familiar di kampus ini...{/i}"
            "[mcname!c]" "{i}Tapi mungkin buat jurusan yang ku ambil gak bakal banyak ke sini.{/i}"
            "[mcname!c]" "{i}...{/i}"
            $ quick_menu = False
            scene black with Dissolve(1.0)
            scene rooftop sore with Dissolve(1.0)
            $ quick_menu = True
            "[mcname!c]" "{i}Hooooo, jadi ini rooftopnya.{/i}"
            "[mcname!c]" "{i}Wah dilihat dari atas ternyata memang keren sih ini kampus.{/i}"
            "Dari rooftop terlihat seluruh pemandangan di kampus."
            "Terlihat beberapa orang melaksanakan beberapa aktifitas kampus, bahkan ada juga yang sepertinya sudah siap-siap untuk pulang."
            "[mcname!c]" "Mgghhhh~\n*Peregangan*"
            "[mcname!c]" "{i}Mungkin udah dulu kali ya buat hari ini...{/i}"
            "[mcname!c]" "{i}Abis ini pulang ke kost aja deh.{/i}"
            jump chapter1kana3kos
        # Opsi ini beda sama di skrip + toba2 langsung besok
        "Ke kost lalu tidur.":
            ##$ renpy.block_rollback()
            jump chapter1kana3kos
        # Opsi ini beda sama di skrip, seharusnya ke kos
        "Langsung berangkat lebih awal supaya ga ketinggalan":
            ##$ renpy.block_rollback()
            stop music fadeout 1.0
            $ quick_menu = False
            play music "BGM_Bad End.ogg" fadein 1.0
            "[mcname!c] memilih untuk berangkat lebih awal dari waktu kerja kelompok yang telah ditetapkan, tapi dia lupa kalau dirinya belum mandi dan makan."
            "[mcname!c] juga lupa bahwa kerja kelompoknya besok, bukan hari ini."
            scene black with dissolve
            show text "{color=#FFF}EH KALAU MAU KEGIATAN TUH MINIMAL MANDI DAN MAKAN{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FFF}JANGAN LANGSUNG BERANGKAT{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FFF}SEKARANG LO MALAH DI MARAHIN SAMA ANGGOTA KELOMPOK LO KAN{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FFF}AKHIRNYA MALAH PINGSAN KAN{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FFF}BERANGKAT LEBIH AWAL JUGA BAGUS, TAPI GAK SAMPE SEHARI SEBELUM JUGA KALI{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FFF}HADEEEUHHH DASAR{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" #fadein 1.0
            jump credits
                
label chapter1kana3kos:
    ##$ renpy.block_rollback()
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" fadein 1.0
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Di kost..."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(2.0)
    $ quick_menu = True
    "[mcname!c]" "{i}Okeh, saatnya tidur. Besok ada kerja kelompok soalnya.{/i}"
    "[mcname!c]" "{i}Ga mau telat buat kerja kelompok pertama.{/i}"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Pagi Siang.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya..."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(1.0)
    $ quick_menu = True
    "[mcname!c]" "Hmmm, keknya mending aku bangun terus siap-siap deh biar ga telat."
    "[mcname!c]" "Ga enak juga kalau pertama kali malah telat."
    "[mcname!c] pun bersiap siap untuk berangkat kerja kelompok."
    "Ia menghabiskan kebanyakan waktunya saat mandi agar merasa lebih segar dan tidak mengantuk."
    "Setelah itu dia pun berangkat menuju tempat yang pada awalnya sudah ditentukan."
    $ quick_menu = False
    scene depan kampus with Dissolve(2.0)
    $ quick_menu = True
    "Setelah [mcname!c] sampai di tempat janjian..."
    "[mcname!c]" "{i}Tenang-tenang...{/i}"
    "[mcname!c]" "{i}Gak usah gugup.{/i}"
    "[mcname!c]" "{i}Santai aja.{/i}"
    "[mcname!c]" "{i}Kamu gak usah gugup.{/i}"
    "[mcname!c]" "{i}Meski ini kerja kelompok pertama kali di kuliah tapi kamu bisa kok.{/i}"
    "[mcname!c]" "Yuk semangat..."
    "Tak lama kemudian, Kana dan Freya pun datang dan menghampiri."
    show kana_date at kana_near_left_2
    show freya at freya_near_right
    with dissolve
    hide kana_date
    show kana_date_talk at kana_near_left_2
    show kana_date_side_talk at left
    with dissolve
    kana "Eh haloo~"
    kana "Udah lama ya nunggunya?"
    kana "Maaf ya Jakarta macet sii hehe..."
    hide kana_date_side_talk
    hide kana_date_talk
    show kana_date at kana_near_left_2
    with dissolve
    hide freya
    show freya_talk at freya_near_right
    show freya_side_talk at left
    with dissolve
    freya "Eh iya nih tadi aku ke rumah Kana dulu juga."
    freya "Biasa si princess satu ini terlalu lama dandannya~"
    freya "Tapi ya macet juga si..."
    hide freya_side_talk
    hide freya_talk
    show freya at freya_near_right
    with dissolve
    "[mcname!c]" "{i}Dandan!?{/i}"
    hide freya
    hide kana_date
    with dissolve
    show kana_date_smile at kana_near
    with dissolve
    "[mcname!c]" "{i}Setelah diperhatikan lebih detail memang Kana saat ini terlihat lebih natural dan lebih cantik dari biasanya...{/i}"
    "Makeup Kana yang terlihat sedikit berbeda dari saat ia ke kampus membuat [mcname!c] terdiam sebentar."
    hide kana_date_smile
    show freya_smug at freya_near_right
    show kana_date_confused_blush_sideeye at kana_near_left_2
    with dissolve
    "Menyadari [mcname!c] memperhatikannya, Kana jadi terdiam seakan panik mendatang, dan tidak dapat menjawab pertanyaan Freya."
    "Kana hanya bisa melihat ke arah Freya."
    hide kana_date_confused_blush_sideeye
    show kana_date_shy_smile at kana_near_left_2
    show kana_date_side_shy at left
    with dissolve
    kana "Apaan sih Free..."
    kana "Aku kan gak dandan lama."
    kana "Itu kan karena macet ihhh."
    kana "Lagian aku juga kaya biasanya di kampus ko dandannya, iya kan?"
    hide kana_date_side_shy
    hide kana_date_shy_smile 
    show kana_date_shy at kana_near_left_2
    with dissolve
    "Tak lama Kana pun melihat [mcname!c] seakan meminta bantuan darinya."
    "[mcname!c] hanya bisa tertawa canggung..."
    "[mcname!c]" "Eh.. ummmmm.."
    "[mcname!c]" "Hehe~"
    "[mcname!c]" "I-iya mungkin iya tapi kamu yang sekarang kayaknya lebih cantik deh dari biasanya natural aja gitu heh."
    hide kana_date_shy
    show kana_date_shy_closeeye at kana_near_left_2
    with dissolve
    "Wajah Kana pun memerah dengan cepat menandakan bahwa ia malu mendengar kata itu dari [mcname!c]."
    "Saat itu juga Freya pun tertawa dan membuat suasana lebih hidup."
    hide freya_smug
    show freya_shock at freya_near_right
    show freya_side_shock at left
    with dissolve
    freya "Hahaha~"
    freya "Cieee disebut cantik tuh Nay~"
    freya "Cieeee~"
    freya "Kiw kiw cukurukuk!"
    hide freya_side_shock
    hide kana_date_shy_closeeye
    hide freya_shock
    show freya_smug at freya_near_right 
    show kana_date_shy_smile at kana_near_left_2
    show kana_date_side_shy at left
    with dissolve
    kana "Apaan sih!"
    kana "Udah ah Fre~"
    kana "Itu kan cuma basic compliment doang."
    kana "Biar ga canggung doang..."
    hide kana_date_side_cry
    hide kana_date_shy_closeeye_talk
    show kana_date_talk at kana_near_left_2
    show kana_date_side_talk at left
    with dissolve
    kana "By the way ini si [mahasiswa_name] kemana ya?"
    kana "Kok belum datang si udah jam segini nih."
    hide kana_date_side_talk
    hide kana_date_talk
    hide kana_date_side_cry
    hide kana_date_shy_smile
    hide kana_date_side_shy
    show kana_date at kana_near_left_2
    hide freya_shock
    show freya at freya_near_right
    with dissolve
    "[mcname!c]" "Tunggu bentar lagi aja dulu ya mungkin kejebak macet."
    "[mcname!c]" "Mending kita tanya di grup aja kali ya?"
    hide freya
    show freya_talk at freya_near_right
    show freya_side_talk at left
    with dissolve
    freya "Ide bagus!"
    freya "Yaudah, kita tunggu beberapa menit aja dulu lah ya~"
    hide freya_side_talk
    hide freya_talk
    hide kana_date
    hide freya_smug
    with dissolve
    "Mereka pun menunggu [mahasiswa_name]."
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene depan kampus with Dissolve(1.0)
    $ quick_menu = True
    "..."
    "Sudah 10 menit namun tidak ada kabar."
    "Akhirnya mereka menyerah menunggu."
    hide kana_date
    show kana_date_confused at kana_near_left_2
    show kana_date_side_confused at left
    with dissolve
    kana "Eh udah lama ini, mana panas banget lagi."
    kana "Kita duluan aja kali ya."
    kana "[mahasiswa_name] gak bales ini."
    kana "Ditelpon juga ga di angkat kan?"
    hide kana_date_side_confused
    hide kana_date_confused
    show kana_date at kana_near_left_2
    hide freya
    show freya_shock at freya_near_right
    show freya_side_shock at left
    with dissolve
    freya "Iya juga sih."
    freya "Ya udah lah ya mungkin ketiduran atau gimana."
    freya "Nanti kita suruh aja buat ngerjain bagian yang lain."
    hide freya_shock 
    show freya at freya_near_right
    hide freya_side_shock
    with dissolve
    "[mcname!c]" "Eh bentar ada chat nih dari [mahasiswa_name]."
    hide freya
    hide kana_date
    with dissolve
    "[mcname!c] kemudian membuka HPnya."
    nvl clear
    $ quick_menu = False
    donatur_nvl "{size=-5}Sorry guys, gue mendadak ada panggilan kerja.{/size}"
    nvl clear
    scene depan kampus with dissolve
    $ quick_menu = True
    "[mcname!c]" "Yahh ternyata dia tiba-tiba ada panggilan kerjaan tuh."
    "[mcname!c]" "Dia minta maaf ga bisa datang dan ngerjain bagian lain aja tuh katanya gimana?"
    hide kana_date_confused
    show freya at freya_near_right
    show kana_date_talk at kana_near_left_2
    show kana_date_side_talk at left
    with dissolve
    kana "Ya udah deh gak papa."
    kana "Yang penting sekarang kita kerjain aja dulu lah biar makin cepet istirahat."
    kana "Panas banget soalnya."
    hide freya
    hide kana_date_talk
    hide kana_date_side_talk
    with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Monas.ogg" loop fadein 1.0
    scene monas temporary with Dissolve(1.0)
    $ quick_menu = True
    "Mereka pun memutuskan untuk meninggalkan [mahasiswa_name] dan mulai mengerjakan tugas kelompok yang diberikan."
    "Mereka pun mulai berjalan-jalan dan mewawancarai sekitar."
    $ quick_menu = False
    stop music fadeout 2.0
    jump puzzle_start

label chapter1kana3monas:
    #$ renpy.block_rollback()
    scene black with Dissolve(1.0)
    play music "audio/BGM_Monas.ogg" loop fadein 1.0
    scene monas temporary with Dissolve(1.0)
    show freya at freya_near_right
    show kana_date at kana_near_left_2
    with dissolve
    $ quick_menu = True
    "Setelah itu, mereka memutuskan untuk berhenti sejenak di sekitar monas dikarenakan panas yang tidak tertahankan."
    show freya_shock at freya_near_right
    hide freya
    show freya_side_shock at left
    with dissolve
    freya "Aduhh panas banget ya Nay, [mcname!c]."
    freya "Jujur ini mungkin hari terpanas dalam minggu ini."
    hide freya_side_shock
    show freya at freya_near_right 
    show kana_date_side_confused at left
    show kana_date_confused at kana_near_left_2
    with dissolve
    kana "Iya panas banget, mana haus lagi."
    hide kana_date_confused
    hide kana_date_side_confused
    with dissolve
    "[mcname!c]" "{i}Hmmm iya nih panas.{/i}"
    "[mcname!c]" "{i}Bisa kali ya aku beliin mereka minum sesekali gitu.{/i}"
    "[mcname!c]" "Eh bentar ya, mau beli minum dulu."
    menu:
        "Kamu beliin mereka..."
        "Minuman berenergi":
            stop music fadeout 1.0
            $ quick_menu = False
            play music "BGM_Bad End.ogg" fadein 1.0
            "[mcname!c] membelikan Minuman berenergi untuk Kana dan Freya."
            "Karena minuman ini lah yang ia minum saat di desa saat merasa kecapean agar berenergi lagi."
            hide freya
            hide kana_date
            show freya_shock at freya_near_right
            show kana_date_confused at kana_near_left_2
            with dissolve
            "Akan tetapi Kana dan Freya melihat [mcname!c] dengan tatapan aneh saat tau itu ternyata minuman berenergi."
            scene black with dissolve
            show text "{color=#FFF}BRO YANG BENER AJA{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FFF}DI KIRA MEREKA ABIS OLAHRAGA ATAU NUKANG KALI YA DI KASIH GINIAN{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FFF}AKHIRNYA MEREKA GA MAU NGOBROL KAN SAMA LO LAGI{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            scene dream with dissolve
            jump credits
        "Es Teh":
            hide freya_shock
            hide freya 
            hide kana_date 
            with dissolve
            jump chapter1kana3monasesteh
        "Jamu":
            stop music fadeout 1.0
            $ quick_menu = False
            play music "BGM_Bad End.ogg" fadein 1.0
            "[mcname!c] membelikan jamu untuk Kana dan Freya, karena teringat dengan mama di desa dimana saat mama merasa capek selalu minta untuk di belikan jamu agar lebih segar."
            hide freya
            hide kana
            show freya_shock at freya_near_right
            show kana_date_confused at kana_near_left_2
            with dissolve
            "Tetapi Kana dan Freya sangat lah asing dengan jamu dan saat itu juga mereka malah pucat dan muntah."
            scene black with dissolve
            show text "{color=#FFF}EH DIKIRA UDAH TUA KALI YA DI KASIH JAMU{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FFF}LAGIAN GA SEMUA BISA MINUM JAMU BROO{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FFF}MIKIR{/color}" with Pause(2.0)
            scene black with dissolve
            show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
            stop music fadeout 1.0
            scene black with dissolve
            play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
            jump credits

label chapter1kana3monasesteh:
    ##$ renpy.block_rollback()
    $ quick_menu = False
    scene black with Dissolve(1.0)
    scene monas temporary with Dissolve(1.0)
    $ quick_menu = True
    "[mcname!c] melihat ada sebuah stand minuman es teh yang cukup ramai."
    "Ia pun memilih untuk membelikan mereka minuman itu."
    hide freya
    hide kana
    show freya_smile at freya_near_right
    show kana_date_smile at kana_near_left_2
    with dissolve
    "Saat ia datang kembali dengan membawa 3 gelas es teh raut muka Kana dan Freya tersenyum dan merasa senang."        
    show kana_date_talk at kana_near_left_2
    show kana_date_side_talk at left
    with dissolve
    kana "Wahhhh cocok banget nih."
    kana "Makasih banyak ya [mcname!c]!"
    kana "Ini berapa? Nanti aku ganti ya."
    hide kana_date_side_talk with dissolve
    hide freya_smile
    hide kana_date_talk
    show freya_talk at freya_near_right
    show freya_side_talk at left
    with dissolve
    freya "Duhh cocok banget nih siang-siang minum es teh seger banget."
    freya "Makasih yaa~"
    freya "Nanti teh punyaku di bayarin sama Kana ya."
    hide freya_side_talk
    hide freya_talk
    show freya_smile at freya_near_right
    hide kana_date_talk
    show kana_date_confused at kana_near_left_2
    #SFX Yang bener aja rugi dong
    show kana_date_side_confused at left
    with dissolve
    kana "..."
    hide kana_date_side_confused
    show kana_date at kana_near_left_2
    with dissolve
    "[mcname!c]" "Hahah udah udah, gapapa kok~"
    "[mcname!c]" "Ini dari aku sekalian ucapan terima kasihku karena udah mau nunjukin sekitar Jakarta."
    "[mcname!c]" "Soalnya kemarin aku ga sempet muter-muter jadi makasih ya."
    hide freya_smile
    show freya_talk at freya_near_right
    show freya_side_talk at left
    with dissolve
    freya "Yang bener?"
    freya "Aku sih gak nolak."
    freya "Hehe~"
    hide freya_side_talk
    hide freya_talk
    show freya at freya_near_right
    with dissolve
    hide kana_date_angry
    show kana_date_talk at kana_near_left_2
    show kana_date_side_talk at left
    with dissolve
    kana "Hadeeeh Freya Freya~"
    hide kana_date_side_talk
    hide kana_date_talk
    hide freya 
    show kana_date_talk at kana_near_left_2
    show freya_shock at freya_near_right
    with dissolve
    "Mereka tertawa bersama dan kembali mengobrol satu sama lain."
    hide freya_shock 
    hide kana_date_talk
    hide kana_date
    hide kana_date_confused 
    hide kana_date_smile 
    with dissolve
    $ quick_menu = False
    scene black with Dissolve(1.0)
    pause(1.0)
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Beberapa jam kemudian..."
    $ quick_menu = False
    scene monas temporary with Dissolve(2.0)
    show freya at freya_near_right
    show kana_date at kana_near_left_2
    with dissolve
    $ quick_menu = True
    "[mcname!c]" "Eh ini udah kah?"
    "[mcname!c]" "Atau kira-kira gimana lagi nih?"
    "[mcname!c]" "Kalau dari aku sih udah cukup ga perlu ada yang ditambah nantinya malah makin ribet."
    hide freya
    show freya_talk at freya_near_right
    show freya_side_talk at left
    with dissolve
    freya "Sebenernya ada yang menurutku harus ditambah sih."
    freya "Tapi itu nanti sama aku aja."
    freya "Agak susah jelasinnya juga hehe."
    hide freya_side_talk
    hide freya_talk
    show freya at freya_near_right
    with dissolve
    hide kana_date
    show kana_date_talk at kana_near_left_2
    show kana_date_side_talk at left
    with dissolve
    kana "Aku sih udah oke aja."
    kana "Maklumin Freya ya, [mcname!c]."
    hide kana_date_side_talk
    hide kana_date_talk
    show kana_date at kana_near_left_2
    with dissolve
    "Senyuman kecil keluar dari wajah Kana, seakan sudah terbiasa dengan Freya."
    hide freya
    show freya_angrysmile at freya_near_right
    with dissolve
    hide kana_date
    show kana_date_talk at kana_near_left_2
    show kana_date_side_talk at left
    with dissolve
    kana "Freya emang gitu orangnya..."
    kana "Dia susah jelasin beberapa hal yang ada di kepalanya."
    kana "Tapi dia punya banyak ide yang bagus kok."
    kana "Santai aja."
    kana "Nanti kita tinggal kasih tau ke [mahasiswa_name] aja berarti ya? Bagian yang harus dia kerjain."
    hide kana_date_side_talk
    hide kana_date_talk
    show kana_date at kana_near_left_2
    hide freya_angrysmile
    show freya at freya_near_right
    with dissolve
    "[mcname!c]" "Ooooo oke deh."
    "[mcname!c]" "Nanti aku aja yang hubungi [mahasiswa_name], sama jelasin bagian mana yang harus dia kerjain."
    hide kana_date
    show kana_date_smile at kana_near_left_2
    show kana_date_side_talk at left
    with dissolve
    kana "Okee makasih ya~"
    hide kana_date_side_talk
    hide kana_date_smile
    show kana_date at kana_near_left_2
    with dissolve
    show freya_talk at freya_near_right
    show freya_side_talk at left
    with dissolve
    freya "Mantappp~"
    freya "Nay ayoo itu supirmu sudah nungguin."
    freya "Eh kita duluan ya..."
    freya "Dadah~"
    hide freya_talk
    show freya at freya_near_right
    hide freya_side_talk
    with dissolve
    "Terlihat orang dengan dengan jas hitam menunggu di depan mobil tidak jauh dari mereka."
    "[mcname!c]" "Okee makasih ya."
    hide kana_date
    hide freya_talk
    hide freya
    with dissolve
    "Setelah itu [mcname!c], Kana, dan Freya pun pulang ke rumahnya\nmasing-masing."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Sore.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Di perjalanan [mcname!c] mengenang kembali harinya yang telah ia habiskan bersama Kana dan Freya."
    "[mcname!c]" "..."
    "[mcname!c]" "{i}Hari ini capek juga ya...{/i}"
    "[mcname!c]" "{i}Tapi beruntung aku ga telat dan ikut kerja kelompok.{/i}"
    "[mcname!c]" "{i}Kana sama Freya friendly juga ternyata...{/i}"
    "[mcname!c]" "{i}Awalnya aku kira bakalan kaya judes gitu, hahaha.{/i}"
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kosan 1.ogg" fadein 1.0
    scene awan malam with Dissolve(1.0)
    $ quick_menu = True
    "Di kost..."
    $ quick_menu = False
    scene kamar mc kota with Dissolve(2.0)
    $ quick_menu = True
    "Meskipun merasa kecapekan..."
    "[mcname!c] tetap bisa mengingat kembali apa yang terjadi pada hari ini."
    "Sesaat sampai di kosannya, [mcname!c] hanya bisa rebahan di kasur dan melihat foto yang Freya kirimkan saat kerja kelompoknya."
    "Ada satu foto yang membuatnya tersenyum kembali, yaitu foto Kana yang tidak sengaja diambil oleh [mcname!c] saat kerja kelompok."
    "[mcname!c]" "{i}Apakah ini yang dinamakan...{/i}"
    "[mcname!c]" "Ah, apaan sih. Tidur aja dah."
    "[mcname!c] pun tertidur dan ia memimpikan foto Kana yang tersenyum itu..."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "audio/BGM_Kelas.ogg" fadein 1.0 volume(1.5)
    scene awan with Dissolve(1.0)
    $ quick_menu = True  
    "Keesokan harinya..."
    $ quick_menu = False
    scene kelas with Dissolve(2.0)
    $ quick_menu = True
    "Setelah sampai di kelas, [mcname!c] menghampiri [mahasiswa_name] untuk menjelaskan bagian mana yang harus ia kerjakan."
    show galaxy at galaxy_center with dissolve
    "[mcname!c]" "Eh, [mahasiswa_name] kemarin ga datang ya?"
    show galaxy_talk at galaxy_center
    show galaxy_side_talk at left
    with dissolve
    galaxy "Eh iya [mcname!c], maaf ya soalnya tiba-tiba kakakku sakit terus ke RS, aku disuruh nemenin."
    hide galaxy_side_talk
    hide galaxy_talk
    with dissolve
    "[mcname!c]" "Eh..."
    "[mcname!c]" "Bukannya kemarin kamu bilang kalau kamu ada panggilan kerja ya?"
    "Saat mereka berdua mengobrol satu sama lain, datang Freya dan Kana dari arah pintu dan menyapa mereka."
    show freya at freya_near_right
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Halo [mcname!c], halo [mahasiswa_name]."
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near_left_2
    with dissolve
    hide freya
    show freya_shock at freya_near_right
    show freya_side_shock at left
    with dissolve
    freya "Haloo semuanya~, ada apa nih~"
    hide freya_side_shock
    hide freya_shock
    show freya at freya_near_right
    with dissolve
    hide galaxy
    show galaxy_talk at galaxy_center
    show galaxy_side_talk at left
    with dissolve
    galaxy "Yooo Kalian, ini cuma lagi ada yang mau dibahas sama [mcname!c]..."
    hide galaxy_side_talk
    hide galax_talk
    show galaxy at galaxy_center
    with dissolve
    "[mcname!c]" "Nggak, ini tadi baru mau jelasin pekerjaan bagian dia tapi kok, alasannya beda ya?"
    hide galaxy
    show galaxy_talk at galaxy_center
    show galaxy_side_talk at left
    with dissolve
    galaxy "Huh beda???"
    galaxy "Gak kok, jadi kemarin tuh emang ada panggilan kerja."
    galaxy "Tapi tiba tiba kakak ku sakit terus ke RS gitu."
    galaxy "Hahahaha.."
    hide galaxy_side_talk
    with dissolve
    "Kata [mahasiswa_name] sambil tertawa canggung."
    hide galaxy_talk
    show galaxy at galaxy_center
    show freya_annoy at freya_near_right
    with dissolve
    "Melihat gelagat [mahasiswa_name] yang agak aneh, Freya memicingkan mata dengan tatapan curiga."
    hide freya_annoy
    show freya_angrysmile at freya_near_right
    show freya_side_angrysmile at left
    with dissolve
    freya "Hmmmm, gak tau deh~"
    freya "Gak peduli juga mana yang bener."
    freya "Yang penting kamu kerjain ya."
    freya "Awas aja kalau engga."
    hide freya_side_angrysmile
    hide freya_angrysmile
    show freya_annoy at freya_near_right
    with dissolve
    "Freya memberikan senyuman yang entah kenapa terasa berbeda dari senyum karamel biasanya."
    hide kana
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Hahaha, makan tuh kena ancam Freya."
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near_left_2
    with dissolve
    hide galaxy
    show galaxy_talk at galaxy_center
    show galaxy_side_talk at left
    with dissolve
    galaxy "Iya iya."
    galaxy "Santai aja kali~"
    galaxy "Nanti gue kerjain."
    galaxy "Ga usah khawatir dah..."
    hide galaxy_side_talk
    hide galaxy_talk
    show galaxy at galaxy_center
    "[mcname!c] pun menjelaskan apa yang harus dilakukan [mahasiswa_name] ke depannya untuk mengerjakan tugas kelompoknya."
    "Setelah dijelaskan, [mahasiswa_name] pun setuju dan memahami tentang apa yang harus dilakukan."
    hide galaxy
    show galaxy_talk at galaxy_center
    show galaxy_side_talk at left
    with dissolve
    galaxy "Oke dah paham-paham ternyata segini, ku kira bakalan banyak."
    hide galaxy_side_talk
    hide galaxy_talk
    show galaxy at galaxy_center
    with dissolve
    "[mcname!c]" "Sebenernya ada yang lain sih, tapi coba tanya Freya sana."
    hide galaxy
    show galaxy_talk at galaxy_center
    show galaxy_side_talk at left
    with dissolve
    galaxy "Ada lagi ga Freya? Aku kira bakalan banyak."
    hide galaxy_side_talk
    hide galaxy_talk
    show galaxy at galaxy_center
    with dissolve
    hide freya_annoy
    show freya_angrysmile at freya_near_right
    show freya_side_angrysmile at left
    with dissolve
    freya "Gini doang??"
    "Freya menatap [mahasiswa_name] dengan kesal..."
    freya "Awas aja kalo ga bener ya!!"
    freya "Aku coret namamu dari kelompok."
    hide freya_side_angrysmile
    hide freya_angrysmile
    show freya_annoy at freya_near_right
    with dissolve
    hide galaxy
    show galaxy_talk at galaxy_center
    show galaxy_side_talk at left
    with dissolve
    galaxy "Lah santai aja napa."
    galaxy "Ya udah gue tinggal lagi yak."
    galaxy "Soalnya masih ada yang harus gue kerjain nih..."
    hide galaxy_side_talk
    hide galaxy_talk
    with dissolve
    "[mahasiswa_name] kemudian mengambil tas nya kemudian lari pergi meninggalkan mereka..."
    hide galaxy_talk with dissolve
    hide freya_annoy
    show freya_angrysmile at freya_near_right
    show freya_side_angrysmile at left
    with dissolve
    freya "Ya ela, tuh anak malah kabur."
    freya "Ya udah lah, ga tau lagi."
    hide freya_side_angrysmile 
    hide freya_angrysmile
    show freya_annoy at freya_near_right
    with dissolve
    hide kana
    show kana_smile at kana_near_left_2
    show kana_side_smile at left
    with dissolve
    kana "Udah lah..."
    hide kana_side_smile 
    hide freya_annoy
    show freya at freya_near_right
    with dissolve
    hide kana_smile
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Oh iya [mcname!c], bagaimana liburanmu kemarin?"
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near_left_2
    with dissolve
    "[mcname!c]" "Yah, gak ada yang menarik sih."
    "[mcname!c]" "Palingan cuma rebahan di kamar aja soalnya kemarin ngabisin tenaga banget."
    hide kana
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Sama dong~"
    kana "Aku juga kemarin cuma di rumah aja buat bersih-bersih kamar."
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near_left_2
    with dissolve
    "[mcname!c]" "Hahaha, sama aku juga."
    hide freya
    show freya_talk at freya_near_right
    show freya_side_talk at left
    with dissolve
    freya "Enak banget ya."
    freya "Aku pas pulang harus nyari bahan buat project kita sih."
    hide freya_side_talk
    hide freya_talk
    show freya at freya_near_right
    with dissolve
    "[mcname!c]" "Lah, kalau perlu bantuan bilang Freya."
    "[mcname!c]" "Kita siap membantu, tenang aja."
    hide kana
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Iya nih jangan ngerjaiin sendirian yaa~"
    kana "Awas aja."
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near_left_2
    with dissolve
    hide freya
    show freya_talk at freya_near_right
    show freya_side_talk at left
    with dissolve
    freya "Santai aja, bisa kok..."
    hide freya_side_talk
    hide freya_talk
    show freya at freya_near_right
    with dissolve
    "[mcname!c]" "Yang bener?"
    hide freya
    show freya_angrysmile at freya_near_right
    show freya_side_angrysmile at left
    with dissolve
    freya "Bener, kalau mau bahas project mah nanti aja deh bahas yang lain aja napa."
    hide freya_side_angrysmile
    hide freya_angrysmile
    show freya_annoy at freya_near_right
    with dissolve
    hide kana
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Haha, oke deh Frey aku percaya kok sama kamu."
    kana "By the way [mcname!c], kemarin nyasar ga nih pas pulang sendirian? Soalnya dulu aku pas pulang sendirian pernah nyasar."
    kana "Itulah kenapa sekarang pake supir."
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near_left_2
    with dissolve
    "[mcname!c] menjawab dengan semangat."
    "[mcname!c]" "IYA!"
    "[mcname!c]" "Aku kemarin hampir aja dibuat nyasar sama maps..."
    hide freya_annoy
    show freya_talk at freya_near_right
    show freya_side_talk at left
    with dissolve
    freya "Hahah bener tuh."
    freya "Naya pernah sampe mau nangis loh pas telepon aku..."
    hide freya_side_talk
    hide freya_talk
    show freya_smile at freya_near_right
    hide kana
    show kana_shy_talk at kana_near_left_2
    show side kana_side_shy_talk at left
    with dissolve
    kana "Ihh Freya gak usah kasih tau juga bagian itu..."
    hide side kana_side_shy_talk
    hide kana_shy_talk
    show kana_shy_closeeye at kana_near_left_2
    with dissolve
    "[mcname!c]" "Iya kah?"
    "[mcname!c]" "Jadi pengen liat kamu mau nangis gitu, hahah."
    hide kana_shy_closeeye
    hide freya_smile 
    with dissolve
    "Tak lama kemudian, Dosen memasuki ruangan dan kelas pun dimulai."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Dosen.ogg" fadein 1.0
    scene awan with Dissolve(1.0)
    $ quick_menu = True
    "Keesokan harinya..."
    $ quick_menu = False
    scene kelas with Dissolve(2.0)
    ##$ renpy.block_rollback()
    $ quick_menu = True
    "Waktu yang diberikan untuk mengerjakan tugas pun telah berakhir, dan hari di mana presentasi dilakukan pun tiba."
    "[mcname!c], Kana, Freya, dan [mahasiswa_name] pun melakukan presentasinya di depan kelas."
    "Presentasi dilakukan secara lancar."
    stop music fadeout 1.0
    $ quick_menu = False
    scene black with Dissolve(1.0)
    play music "BGM_Sore.ogg" fadein 1.0
    scene awan sore with Dissolve(1.0)
    $ quick_menu = True
    "Saat kelas akan selesai..."
    $ quick_menu = False
    scene kelas sore with Dissolve(2.0)
    $ quick_menu = True
    "Dosen pun memberitahukan beberapa kelompok yang memiliki nilai tinggi."
    "Diantara kelompok itu, kelompok [mcname!c], Kana, Freya, dan [mahasiswa_name] merupakan salah satu kelompok dengan nilai tertinggi."
    show kana at kana_near_left_2
    show freya at freya_near_right
    show galaxy at galaxy_center
    with dissolve
    hide kana
    show kana_talk at kana_near_left_2
    show kana_side_talk at left
    with dissolve
    kana "Wahhhh, kita dapat nilai tertinggi loh!???"
    hide kana_side_talk
    hide kana_talk
    show kana at kana_near_left_2
    with dissolve
    hide freya
    show freya_smug at freya_near_right
    show freya_side_smug at left
    with dissolve
    freya "Hehehe, siapa dulu, kan ada aku~"
    hide freya_side_smug with dissolve
    "[mcname!c]" "Enak aja, gara gara aku tuh~"
    hide galaxy
    show galaxy_talk at galaxy_center
    show galaxy_side_talk at left
    with dissolve
    galaxy "Ya elah, gara-gara aku ini~"
    galaxy "Coba aja aku ga ngerjaiin bagianku dengan sempurna, kelar kelar dah."
    hide galaxy_side_talk
    hide galaxy_talk
    show galaxy at galaxy_center
    hide freya_smug
    show freya_annoy at freya_near_right
    with dissolve
    hide freya_annoy
    show freya_angrysmile at freya_near_right
    show freya_side_angrysmile at left
    with dissolve
    freya "Eh yang ga datang ke kerja kelompok diem aja."
    hide freya_side_angrysmile
    hide freya_angrysmile
    show freya_annoy at freya_near_right
    with dissolve
    hide kana
    show kana_confused at kana_near_left_2
    show kana_side_confused at left
    with dissolve
    kana "Aduhh, Fre Fre santai Fre. Jangan marah~"
    hide kana_side_confused with dissolve
    hide freya_annoy
    show freya_angrysmile at freya_near_right
    show freya_side_angrysmile at left
    with dissolve
    freya "Lagian mancing-mancing…"
    hide freya_side_angrysmile with dissolve
    "[mcname!c]" "Mancing apa tuh?"
    "[mcname!c]" "Mancing perkoro kah?"
    "[mcname!c]" "Hahahaha."
    show galaxy_talk at galaxy_center
    show galaxy_side_talk at left
    with dissolve
    galaxy "Mana adaa, hahahaha."
    hide galaxy_side_talk
    hide kana_confused
    show kana_smile at kana_near_left_2
    hide freya_angrysmile
    show freya_smug at freya_near_right
    with dissolve
    "[mcname!c], Kana, Freya, dan [mahasiswa_name] pun tertawa bersama dan mengucapkan terima kasih kepada satu sama lain."
    show kana_side_talk at left
    show kana_talk at kana_near_left_2
    hide galaxy_talk
    with dissolve
    kana "Tapi thank you loh Freya... [mcname!c]... Galaxy..."
    hide kana_side_talk
    show kana_smile at kana_near_left_2
    with dissolve
    "[mcname!c]" "Aman aja, hahahaha."
    show freya_shock at freya_near_right
    show freya_side_shock at left
    with dissolve
    freya "Sama-sama, hahaha."
    hide freya_side_shock
    hide freya_shock
    show galaxy_talk at galaxy_center
    show galaxy_side_talk at left 
    with dissolve
    galaxy "Anytime, hehehehe~"
    hide kana_talk 
    hide galaxy 
    hide galaxy_side_talk
    hide galaxy_talk
    hide freya_smug
    hide kana_smile
    with dissolve
    "Ruangan kelas pun dipenuhi canda tawa Kana, [mcname!c], Freya, dan Galaxy."
    show kana_smile at kana_near
    with dissolve
    "Saat itu, [mcname!c] melihat senyum Kana yang lebar terlihat begitu bahagia dan membuat hatinya berdegup kencang."
    hide kana_smile with dissolve
    $ quick_menu = False
    jump chapter2kanastart