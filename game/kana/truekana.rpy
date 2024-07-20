label truekana:
  stop music fadeout 1.0
  scene black with dissolve
  play music "audio/BGM_Kantin.mp3" fadein 1.0
  scene kantin with dissolve
  $ quick_menu = True
  mcname "Huft Huft. Ehh maaf, aku telat dikit gapapa kan?"
  show kana at kana_near with dissolve
  show kana_side at left with dissolve
  kana "Haha gapapa. Untung kamu cepet datangnya meskipun telat, ini tadi kursimu udah ada yang mau ambil loh."
  hide kana_side at left with dissolve
  mcname "Hehe sorry yaaa. Tadi beres kelas, perutnya mules dikit. Kemarin abis makan pedes soalnya."
  show kana_side at left with dissolve
  kana "Ya udah ini, tadi aku udah sekalian pesenin buat kamu juga."
  hide kana_side at left with dissolve
  mcname "Heeee, okee makasih yaa udah mesenin sekalian amanin tempat duduk juga."
  "[mcname] duduk di tempat duduk dan mulai melanjutkan obrolan."
  $ quick_menu = False
  scene black with dissolve
  scene kantin with dissolve
  $ quick_menu = True
  mcname "Ehh Kana, kamu tau ga siiih?"
  show kana_side at left with dissolve
  kana "Iya [mcname]? Kenapa?"
  hide kana_side at left with dissolve
  mcname "Aku denger-denger ada event jejepangan yang bakal diadain sama pihak kampus gitu loh."
  show kana_side at left with dissolve
  kana "YANG BENER!!??"
  hide kana_side at left with dissolve
  "Kana pun menjawab dengan penuh semangat, saking semangatnya ia sampai berdiri dari tempat duduknya dan membuatnya diliatin oleh orang-orang sekitar."
  mcname "Semangat banget kamu Kana, ahahah. Sampe diliatin orang-orang loh."
  show kana_side at left with dissolve
  kana "EH!??? I-iya maaf-maaf, terlalu excited soalnya. Denger-denger sih event jejepangan kampus ini tuh selalu rame gitu, makanya aku excited. Apalagi bareng temen, hehe."
  hide kana_side at left with dissolve
  mcname "Eh iya Kana, kalau gitu kamu mau ke eventnya bareng aku, gak? Sekalian ajarin aku, soalnya ini kan event pertamaku hehe."
  show kana_side at left with dissolve
  kana "Ah! Serius? Nanti kita kabar-kabaran ya."
  hide kana_side at left with dissolve
  mcname "Okeee~"
  "Setelah itu mereka pun menghabiskan makanannya, lalu Kana dan [mcname] berpisah karena sudah ada kegiatan masing-masing yang harus dilakukan. Tak terasa waktu pun telah berlalu dan malam hari telah tiba."
  jump truekanakos

label truekanakos:
  $ quick_menu = False
  stop music fadeout 1.0
  scene black with dissolve
  play music "audio/BGM_Kosan 1.mp3" fadein 1.0
  scene kamar mc kota with dissolve
  $ quick_menu = True
  mcname "{i}Aduuuh, mulai chatnya gimana ya? Bingung...{i}"
  menu:
    "Yang kamu lakukan..."
    "P":
      "[mcname] memilih untuk menghubungi Kana dengan awalan “P”, dibandingkan hal lainnya. Kana pun tidak membalas chat tersebut dan meng-ghosting pesan dari [mcname] sampai event dimulai."
      $ quick_menu = False
      stop music fadeout 1.0
      scene black with dissolve
      show text "{color=#FFF}*HAHAHAHA DI GHOSTING TUH, MAKANYA JANGAN ASAL P, P, P GA SOPAN TAU*{/color}" with Pause(2.0)
      show text "{color=#FF0000}BAD END{/color}"
      play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
      jump credits
    "Malam Kana, sibuk ga?":
      "[mcname] menghubungi Kana lewat HPnya, di situ [mcname] bertanya tentang kabarnya terlebih dahulu dan basa-basi seperti orang yang kehabisan topik."
      # scene call hp
      jump truekanachat
    "Langsung telepon aja":
      "[mcname] memilih untuk langsung menelepon Kana dan ternyata Kana sedang bersama keluarga. Tanpa sengaja, Kana memblokir nomor [mcname] karena [mcname] menelepon terus menerus."
      $ quick_menu = False
      stop music fadeout 1.0
      scene black with dissolve
      show text "{color=#FFF}*YAHAHAHA, DIBLOCK KAN? MAKANYA JANGAN LANGSUNG TELPON ORANG AJA, KAN DIBLOCK*{/color}" with Pause(2.0)
      show text "{color=#FF0000}BAD END{/color}"
      play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
      jump credits

label truekanachat:
  #*SKIP TO SCENE*
  #*BG HP CHATTING*
  mcname "Malam Kana, sibuk nggak ya? Hehe"
  kana "Umm engga kok knp ya?(｡･∀･)ﾉﾞ "
  mcname "Aku mau nanya soal event jejepangan itu, jadi kan?"
  kana "Maksudnya jadi?"
  mcname "Yaa jadi kan? Ummm kita berangkat bareng."
  kana "Jadi kok. Mau ketemuan jam berapa?┏ (゜ω゜)=👉"
  mcname "Jam 7 lewat 12 gimana?"
  kana "Jam 7 lewat 12? Kaya pernah denger di mana deh (⊙_⊙)？"
  mcname "Ahh perasaan kamu aja kali. Gimana? Ga kemaleman kah?"
  kana "Hmmm, oke deh jam segitu aja."
  mcname "Btw nanti kita di sana mau ngapain aja ya? Jujur ini event pertamaku, jadi tadi gimana tips and tricknya buat di event, Yang Mulia Kanaia Asa?"
  kana "IHHHH apaan sih. Ya udah jadi kalau dulu tuh biasanya aku-"
  "Tanpa sengaja Kana menekan tombol voice call dan [mcname] pun tanpa pikir panjang menekan tombol jawab."
  #*SKIP TO SCENE*
  #*BG HP VOICE CALL*
  kana "Ehh maaf kepencet!!! Aduh malu banget, aku matiin aja ya."
  mcname "JANGAN!!!"
  "Kana terdiam kaget karena mendengar suara [mcname] yang tiba-tiba teriak."
  mcname "Maksudnya ga usah dimatiin kalau boleh, biar lebih seru ngobrolnya."
  kana "Uuummm.. o-oke deh."
  mcname "Jadi gimana tadi pengalaman kamu? Aku nungguin loh, kasih tau dong biasanya gimana aja di event jejepangan tuh."
  kana "Oh iya lupa, jadi kalau aku dulu ikut event jejepangan tuh biasanya-"
  "Tanpa sadar Kana dan [mcname] pun mengobrol lama, bahkan sampai melewati tengah malam."
  "Beberapa kali [mcname] mendengar Kana menguap dan menyarankan untuk mengakhiri voice call, tetapi ia tetap melanjutkan ceritanya seakan meluapkan semua cerita yang telah ia simpan sendirian selama ini"
  "Beberapa saat kemudian pun Kana tertidur dengan voice call masih menyala."
  mcname "Kana...? Kana...?"
  #*SFX Amimir*
  "Beberapa kali [mcname] menyebutkan nama Kana akan tetapi Kana tetap tidak menjawab."
  mcname "{i}Heeee... Kana ketiduran ya?{/i}"
  "Suara nafas Kana sempat beberapa kali terdengar."
  "Setelah beberapa saat, [mcname] pun memilih untuk mengakhiri voice call itu dan tidur agar tidak telat besok."
  $ quick_menu = False
  stop music fadeout 1.0
  scene black with dissolve
  play music "audio/BGM_MC Pertama Kali ke JKT + BG Pagi.mp3" fadein 1.0
  scene kamar mc kota with dissolve
  $ quick_menu = True
  "[mcname] bangun beberapa lebih awal daripada waktu yang telah dijanjikan, ia tidak sabar untuk pergi ke event tersebut dan menghabiskan waktu dengan Kana."
  "[mcname] pun tidak lupa untuk makan, mandi, serta memakai parfum yang menurutnya lebih mahal daripada makannya selama 1 minggu."
  mcname "Oke, sudah siap! Let's go~"
  $ quick_menu = False
  stop music fadeout 1.0
  scene black with dissolve
  play music "audio/BGM_Kosan 2.mp3" fadein 1.0
  #Harusnya BGM Jejepangan Malam
  scene depan kampus with dissolve
  #Harusnya BG Jejepangan malam
  $ quick_menu = True
  kana "[mcname]... ha.. ha.."
  kana "Haloo, maaf ya nunggu lama.."
  "Suara Kana terpotong-potong yang menandakan bahwa Kana baru saja berlari."
  mcname "Hahaha santai aja Kana, tarik nafas dulu bentar gitu. Keliatan banget kalau kamu baru lari tuh."
  kana "Maaf ya tadi lumayan macet di jalan, makanya aku lari. Kukira udah telat, terus aku juga liat kamu udah ada di depan gerbang. Jadi tadi aku lari deh..."
  mcname "Santai aja Kana. Ya udah, nih kamu minum dulu."
#HARUSNYA SFX GLUG GLUG MINUM
  kana "Makasih ya [mcname]. Sekarang udah aman kok, jadi kamu siap gak?"
  mcname "Siap dong, ya kali ga siap. Nggak kaya siapa gitu... Yang ketiduran di tengah-tengah call."
  kana "IHHHH kamu masih bangun???? Kukira udah dimatiin callnya."
  mcname "Hahaha. Soalnya kamu asik banget, cerita ini itu, eh tiba-tiba diem. Pas dipanggil-panggil, kamu malah tidur. Mana sempet ngigo dikit juga."
  kana "KAMU DENGER!??? AAAAAA!!!"
  kana "Lupaiin gak? Kalau enggak, aku marah besar nih!"
  mcname "Marah karir, maksudnya?"
  kana "LUPAINNN!!!"
  mcname "Iya iya. Mending sekarang kita masuk yuk, keburu malem banget nanti pada tutup."
  kana "Awas aja kalo nggak, aku bakal buat kamu lupa dengan paksa! Ya udah deh, ayo masuk. Aku dah ga sabar."
  "[mcname] dan Kana pun pergi ke event tersebut."
  $ quick_menu = False
  scene black with dissolve
  scene depan kampus with dissolve
  #Harusnya BG Jejepangan malam
  $ quick_menu = True
  "Di sana banyak kegiatan, mulai dari event utama sampai event sampingan."
  "Di antaranya ada cosplay event, song cover competition, dan mini game yang terinspirasi dari permainan tradisional Jepang lainnya."
  mcname "Ehhh Kana bentar...\n*Huft huft*"
  mcname "Sabar... Kana... Kamu semangat banget sih... B-bentar aku tarik nafas dulu."
  kana "Ahhh ayooo~ Kamu masa kalah sih sama aku?"
  mcname "Soalnya kamu cepet banget ke sana ke sininya."
  mcname "Belum ada 10 menit, kita udah pindah tempat mulu. Kamu ga mau liat-liat dulu booth merch yang ada di situ?"
  kana "Ihhh kamu semalem ga research dulu tentang booth yang bakalan ada? Aku udah liat-liat listnya."
  kana "Ada beberapa tempat yang pengen aku samperin, jadi aku cuma bentar doang di tempat lainnya gitu..."
  mcname "Oooo gitu ya ternyata. Maaf deh ini kan event pertama ku, jadi aku ga tau harus research list kaya gitu."
  kana "Ya udah ayo ikutin aku aja."
  "Kana pun langsung menarik tangan [mcname] yang hanya bisa mengikuti kemana pun Kana pergi, hingga Kana berhenti di suatu tempat."
  mcname "Ummm Kana? Ada apa?"
  "Kana terdiam, di situ ada sebuah event yang sedang berlangsung."
  "[mcname] pun melihat event tersebut, di sana ada seseorang yang sedang melakukan sing cover competition."
  $ quick_menu = False
  stop music fadeout 1.0
  scene black with dissolve
  play music "audio/BGM_MC Pertama Kali ke JKT + BG Pagi.mp3" fadein 1.0
#Harusnya BGM Mini Stage
  scene depan kampus with dissolve
#Harusnya BG Mini Stage
  $ quick_menu = True
  #*SPRITE TONO/PIA NYANYI FOR A SEC, AFTER THAT BACK TO BG EVENT*
  tana "Ku sandarkann~ Kepadamu~"
  pia "Kepalaku pada pundak kananmu itu~"
  "[mcname] pun melihat panggung dan mengerti kenapa Kana terdiam. Di situ, terlihat dua orang yang sedang menyanyi dengan suara yang indah."
  "Kurang lebih 3 menit [mcname] dan Kana terdiam mendengarkan mereka bernyanyi. Saat selesai, Kana dan [mcname] pun bertepuk tangan dengan keras."
  $ quick_menu = False
  stop music fadeout 1.0
  scene black with dissolve
  play music "audio/BGM_Kosan 2.mp3" fadein 1.0
  #Harusnya BGM Jejepangan Malam
  scene kamar mc kota with dissolve
  #Harusnya BG Jejepangan Malam
  $ quick_menu = True
  play sound "audio/crowd_noise.mp3" fadein 1.0
  #HARUSNYA SFX Applause
  mcname "Gilaaaa, kereen bangeett sumpah! Iya ga, Kana?"
  kana "Iyaaa aku sampe terdiem loh, kamu juga dengerin tadi?"
  mcname "Iya lah, kamu tiba-tiba diem aja. Gimana aku ga ikutan dengerin? Keren banget, kapan ya aku bisa nyanyi kaya gitu..."
  mcname "Btw, kamu suka nyanyi juga?"
  kana "Eee-enggak kok, a-aku..."
  kana "E-ehhh liat deh, di situ ada cosplay yang bagus mending kita ke sana."
  "Kana tiba-tiba menghindari dari jawaban [mcname] dan berlari ke arah seorang cosplayer."
  $ quick_menu = False
  scene black with dissolve
  scene kamar mc kota with dissolve
  $ quick_menu = True
  kana "Eh Kaa, permisi~"
  "Cosplayer" "Iya Ka kenapa?"
  mcname "Kenapa Kana tiba-tiba... Ehh kamu cosplay jadi Kamen Driver Den-A ya?"
  "Cosplayer" "Wahhh iya ka, kebetulan aku suka Kamen Driver."
  kana "[mcname], kamu juga suka?"
  mcname "SUKA!!??? Wahhhh aku ngikutin banget semua series Kamen Driver loh Kana."
  "Cosplayer" "Wahh, kukira ga terlalu banyak yang kenal cosplayku. Ternyata ada juga ya yang kenal, makasih ya Kak."
  "Cosplayer" "Eh Kak, mau ngobrol lagi ga? Keknya seru kita ngobrol bareng."
  #*CHOSE*
  menu:
    "Yang [mcname] lakukan..."
    "Menghabiskan waktu sama cosplayer.":
      #*CHOSE A*
      "[mcname] tetap mengobrol dengan cosplayer tersebut dan mengabaikan keberadaan Kana untuk beberapa saat."
      "Tak lama saat [mcname] tersadar, Kana sudah menghilang dan HPnya tidak dapat dihubungi lagi."
      scene black with Dissolve(2.0)
      show text "{color=#FFF}BRO BRO LAGI JALAN BARENG BERDUAAN KO MALAH DITINGGAL NGOBROL SAMA ORANG LAIN SI ADUHHH{/color}" with Pause(2.0)
      show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
      play music "audio/Dreamcatcher_v2.mp3"
      jump credits
    "Menolak ajakan cosplayer tersebut.":
      #*CHOSE B*
      jump truekanajapanfest
  
label truekanajapanfest:
  mcname "Eh maaf ya nanti lagi, aku lagi sama temen soalnya. Kalp boleh minta social medianya aja kak, biar bisa ngobrol."
  "Orang" "Ooh iya kak, ini bisa di add \"@namadonatur_angka random\". Makasih banyak yaa~"
  mcname "Sama-sama kak"
  mcname "Eh Kana maaf lama ya. Tadi hampir aja keasikan, untung aku inget ada kamu yang lagi nungguin aku haha."
  kana "Enggak kok, ga lama. Seru ya."
  mcname "Eh kamu kenapa Kana, marah ya? Tadi kelamaan ya? Sorry..."
  kana "G."
  mcname "Waduh. Ya udah sebagai permintaan maaf aku ajak main di stand sana deh gimana?"
  kana " BEENER!?? Eh maksudnya... beneran nih?"
  mcname "Iya, bener kok. Ya udah, ayo."
  kana "Yayyy~"
  $ quick_menu = False
  stop music fadeout 1.0
  scene black with dissolve
  play music "audio/BGM_Minigame Tana.mp3" fadein 1.0
  scene lorong sore with dissolve
#Harusnya BG MINIGAME TANA (Tanpa mainin)
  $ quick_menu = True
  kana "Kamu beneran bisa ga?"
  mcname " Bener Kana, tenang aja. Kok kamu ga percaya ke aku gitu sih."
  kana "Soalnya kamu keliatan ga yakin."
  mcname "Ini aku lagi fokus, Kana."
  "Tak lama kemudian..."
  $ quick_menu = False
  stop music fadeout 1.0
  scene black with dissolve
  scene lorong sore with dissolve
#Harusnya BG MINIGAME TANA (Tanpa mainin)
  $ quick_menu = True
  play sound "audio/SFX - Finish Game.mp3"
  "[mcname] pun mendapatkan skor tinggi."
  stop sound fadeout 1.0
  $ quick_menu = False
  scene black with dissolve
  play music "audio/BGM_Kosan 2.mp3" fadein 1.0
#Harusnya BGM Jejepangan Malam
  scene kamar mc kota with dissolve
#Harusnya BG Jejepangan Malam
  $ quick_menu = True
  mcname "Liat, kan? Aku bisaaa, siapa dulu?"
  "[mcname] mendekatkan tangannya ke telinganya dan seolah olah menunggu Kana menjawab."
  mcname "Siapa dulu, hmmmm?"
  kana "Iya iya, kamu jago deh."
  mcname "Nahh gitu dong, hahah."
  "Setelah mendapatkan hadiah dari mini game di dalam booth, [mcname] memberikan hadiahnya kepada Kana."
  kana "Eeeh?"
  mcname "Ini, buat kamu."
  kana "Gapapa nih?"
  mcname "Iyaa, sekarang kamu gak marah lagi kan?"
  kana "M-masih, hmph!"
  mcname "Jadi Yang Muliaaa, kita mau ke mana lagi? Hambamu siap untuk menemanimu ke mana pun dan sampai kapan pun, ahaha."
  kana "Apaan sihh Yang Mulia Yang Mulia, mending mulai sekarang kamu panggil aku “Nay” deh."
  mcname "Okee dehh, Nay."
  mcname "Kalo gitu, kamu mau makan apa? Aku traktir deh, soalnya kamu udah guide sana-sini."
  kana "Hmmmm, apa ya? Kayaknya takoyaki enak deh."
  mcname "Bolehhh, tunggu bentar yaa."
  kana "Okeeee hati-hati, ya."
  "[mcname] pun pergi meninggalkan Kana sejenak untuk membeli takoyaki."
  $ quick_menu = False
  scene black with dissolve
  scene lorong sore with dissolve
  #Harusnya BG MINIGAME TANA (Tanpa mainin)
  $ quick_menu = True
  "Setelah beberapa saat, [mcname] kembali sambil membawa takoyaki."
  mcname "Yahhh Nay, maaf ini cuma sisa satu porsi lagi. Ini buat kamu aja deh, aku gapapa."
  kana "Lah kok gitu sih, kamu juga pasti laper kan?"
  mcname "Enggak koook."
  play sound "audio/hungry.mp3"
  "Tiba-tiba, terdengar suara perut [mcname] yang berbunyi cukup keras sehingga Kana dapat mendengarnya."
  stop sound
  kana "Hahaha ga bisa bohong tuh perut kalau masalah makanan mah."
  "Muka [mcname] pun memerah, merasa malu dengan perutnya." 
  mcname "Aduuhhhhh…\n*Blush*"
  kana "Sini kita makan bareng aja. Ini kan ada 6, kita bagi aja. Masing-masing 3 gimana?"
  mcname "Tapi kan kamu pengen takoyaki."
  kana "Gak apa-apa kok, lagian aku juga makannya sedikit."
  mcname "O-oke deh kalau gitu. Eh tapi ini cuma ada satu doang garpu nya, bentar ya aku coba minta lagi ke penjualnya."
  "Sesaat [mcname] akan pergi, Kana tiba-tiba menangkap tangan [mcname]."
  kana "[mcname], udah ga usah."
  kana "Keburu takoyaki nya dingin, nanti ga enak. Kita makan bareng aja."
  kana "Sini, kita gantian aja."
  mcname "Nay? Bukannya itu malah…"
  kana "Udah cepetan."
  mcname "I-iya iya. Oke deh."
  "Kana pun memakan takoyakinya, lalu Kana pun menjulurkan tangannya yang memegang garpu serta takoyaki ke arah [mcname]."
  kana "Nih."
  "Seakan tidak ingin sadar akan peristiwa yang sedang terjadi, [mcname] tetap memakan takoyaki yang diberikan Kana. Takoyakinya terasa sedikit manis, padahal takoyaki yang dipesan harusnya pedas asin."
  $ quick_menu = False
  scene black with dissolve
  scene lorong sore with dissolve
  #Harusnya BG JEJEPANGAN MALAM
  $ quick_menu = True
  mcname "Ah udah abis lagi aja, ga kerasa ya."
  mcname "Eh Nay, kamu kenapa?"
  "Terlihat muka Kana memerah, mungkin karena baru sadar akan apa yang baru saja terjadi."
  kana "E-eh iya udah abis aja.\n*Blush*"
  mcname "Okeeee selesai, jadi kita ke mana, Nay?"
  "Sesaat [mcname] akan pergi, Kana tiba-tiba mengambil tisu, mengulurkan tangannya, dan mengelap saus yang ada di pipi [mcname]."
  "Terkejut dengan tindakan Kana, [mcname] hanya bisa diam sambil tersenyum." 
  kana "Eh i-ini, a-aku kebiasaan ngurus sepupuku yang masih kecil. Eh ah, ini kita udah kan makannya? Yuk kita ke sana aja."
  "Kana yang malu pun berlari kabur, meninggalkan [mcname] yang masih berdiri di situ."
  mcname "Ehhh?? Tungguin Nay."
  $ quick_menu = False
  scene black with dissolve
  scene lorong sore with dissolve
  #Harusnya BG JEJEPANGAN MALAM
  $ quick_menu = True
  "Kana dan [mcname] pun pergi kembali untuk melihat-lihat booth yang ada di event tersebut, sampai pada akhirnya event utama pada hari itu pun dimulai."
  mcname "Eh Nay, ayoo ini event utamanya udah mau dimulai."
  kana "Eeeeh, okaay."
  $ quick_menu = False
  scene black with dissolve
  scene lorong sore with dissolve
  #Harusnya BG JEJEPANGAN MALAM
  $ quick_menu = True
  play sound "audio/crowd_noise.mp3" fadein 1.0
  "Kana dan [mcname] pun pergi ke tempat di mana event utama diadakan. Event tersebut adalah pertunjukan kembang api kecil kecilan yang akan diadakan oleh panitia acara."
  "Terlihat banyak pengunjung yang menantikan pertunjukan kembang api di event tersebut."
  mcname "Bentar lagi nihhh."
  kana "Aaaaa, udah gak sabaar!"
  stop sound fadeout 1.0
  play sound "audio/SFX - Whack.mp3" loop
  #Harusnya SFX Kembang Api
  $ quick_menu = False
  window auto hide
  with Pause(2.0)
  window auto show
  $ quick_menu = True
  kana "TAMAAYAAAAAA~!"
  mcname "TAMAYAAAAAA~!"
  "Kana dan [mcname] pun menikmati pemandangan kembang api di event tersebut. Meski hanya beberapa menit saja, tapi kenangannya akan tersimpan selamanya."
  stop sound
  stop music fadeout 1.0
  $ quick_menu = False
  scene black with dissolve
  play music "audio/BGM_Rooftop Romance Pia.mp3" fadein 1.0
  scene lorong sore with dissolve
  #Harusnya BG MALAM
  $ quick_menu = True
  "Kana dan [mcname] merasa hangat, senang, dan bahagia. Tanpa sadar event untuk hari ini sudah selesai."
  mcname "Seru banget hari ini Nay! Makasih banyak yaa."
  kana "Hahah, seru banget emang. Makasih juga udah mau nemenin aku, akhirnya aku ada temen yang suka hal-hal gini."
  "[mcname] tersenyum mendengar perkataan Kana."
  mcname "Aku juga seneng banget, soalnya bareng kamu."
  kana "*Blush*"
  mcname "Eh ah, kamu pulang naik apa Nay?"
  kana "Aku biasanya dijemput sih, soalnya udah malem. Emangnya kenapa?"
  mcname "Ooo enggak. Tadinya mau ngajak bareng, tapi aku juga baru sadar ternyata ini udah malem banget. Jadi mending naik mobil aja biar ga masuk angin."
  kana "Hmmm, nanti deh next time gimana? Soalnya mamah ga ijinin aku naik motor kalau udah malem."
  mcname "Iya aku ngerti kok Nay. Ya udah ya, kamu hati-hati Nay."
  kana "Iya makasih ya buat hari ini, kamu juga hati-hati."
  "[mcname] dan Kana pun pergi. [mcname] masih merasa senang dan bahagia karena telah menghabiskan waktu bersama Kana."
  #*SKIP TO SCENE*
  #*BG KOS MALAM*
  stop music fadeout 1.0
  $ quick_menu = False
  scene black with dissolve
  show text "{color=#FFF}Apakah ini date? Mungkin iya, atau mungkin hanya [mcname] yang merasa demikian. Meskipun begitu, rasa bahagia dan senang tidak dapat dihilangkan dari hati [mcname].{/color}" with Pause (4.0)
  play music "audio/BGM_Kosan 1.mp3" fadein 1.0
  scene kamar mc kota with dissolve
  $ quick_menu = True
  "Setelah beberapa menit, [mcname] datang ke kostnya."
  play sound "audio/cafe-entrance.mp3"
  #*DING* (NOTIF HP)
  "HP [mcname] pun berbunyi dan ia melihat adanya notif chat dari Kana." 
  #*BG HP (CHATTING APP)
  kana "H-halooo…(｡･∀･)ﾉﾞ"
  mcname "Halo juga Nayyy… Kenapa nih?"
  kana "Ee-engga kok, cuma mastiin kamu udah pulang aja… Takut nyasar ○( ＾皿＾)っ Hehehe…"
  mcname "Hahaha, ini baru aja selesai beres-beres. Kamu nungguin ya?"
  kana "K-kata siapa? Aku ga nungguin kamu kok (￣ε(#￣)"
  mcname "Hahaha, Nay… Kamu emang suka pake emot kayak gitu ya? Sorry kalo tiba-tiba nanya, soalnya aku penasaran. Dari dulu kalo chat kadang pake, kadang engga."
  kana "Ehhh… Sorry ya kebiasaan... Hehe"
  kana "A-aneh ya?"
  mcname "Engga lah, ga aneh kok. Malah keliatannya lucu aja. Kalau emang kamu lebih suka pake emot kaya gitu, pake aja lucu juga liatnya."
  kana "Yeeee (≧∇≦)ﾉ"
  mcname "Hahaha, lucu emang"
  "[mcname] dan Kana pun menghabiskan waktu mereka berdua dengan membahas kembali apa yang terjadi hari ini, mulai dari bertemu cosplayer, bermain di booth minigame, bahkan membeli merch-merch yang di jual di booth lainnya."
  "Sampai pada akhirnya mereka tertidur dengan tetap memegang HP masing-masing."
  stop music fadeout 1.0
  $ quick_menu = False
  scene black with dissolve
  show text "{color=#FFF}KEESOKAN HARINYA{/color}" with Pause (2.0)
  play music "audio/BGM_Kelas.mp3" fadein 1.0
  scene kelas with dissolve
  $ quick_menu = True
  "Hari dimulai seperti biasanya, [mcname] memasuki kelas dengan keadaan hampir terlambat. Saat mencari tempat kosong, [mcname] mendengar seseorang memanggilnya."
  freya "[mcname]! [mcname]! Sini!"
  "Karena waktu menunjukan bahwa kelas akan segera dimulai, tanpa pikir panjang [mcname] pun duduk di sebelah Freya."
  mcname "Psstt, Fre. Naya ke mana dah?"
  freya "Lah baru aja mau nanyain ke kamu, emang dia ga ngabarin?"
  mcname "Nggak. Terakhir chat tuh waktu malem, abis itu aku ketiduran deh. Ini aja kan hampir telat, emang ke kamu ga ada kabar gitu?"
  freya "Ga ada sama sekali, kalian emang sampe jam berapa?"
  mcname "Ga tau aku lupa, seingetku pas jam 1-an masih sadar kayaknya."
  freya "Wahhh udah jelas ini mah dia kesiangan, haduhhh."
  stop music fadeout 1.0
  $ quick_menu=False
  scene black with dissolve
  scene kelas with dissolve
  $ quick_menu=True
  play music "audio/BGM_Dosen + Rektor.mp3" fadein 1.0
  dosen "Selamat pagi semuanya."
  dosen "Mohon untuk beberapa menit ke depan perhatikan pelajaran dulu ya. Jadi untuk memahami bahwa-"
  $ quick_menu=False
  scene black with dissolve
  scene kelas with dissolve
  $ quick_menu=True
  dosen "Baik. Pelajaran hari ini sudah selesai. Sampai bertemu di pertemuan selanjutnya."
  "Setelah dosen meninggalkan ruangan, kelas pun berakhir."
  stop music fadeout 1.0
  $ quick_menu=False
  scene black with dissolve
  play music "audio/BGM_Kelas.mp3" fadein 1.0
  scene kelas with dissolve
  $ quick_menu=True
  play sound "audio/ding.mp3"
  #HARUSNYA KRIIIIINNNGGGG
  "Tiba-tiba HP Freya berbunyi cukup keras sehingga membuat hampir seluruh kelas melihat ke arahnya."
  freya "Aduhh maaf ya semuanya. Lupa ga disilent tadi, hehe."
  stop music fadeout 1.0
  play sound "audio/ding.mp3"
  #HARUSNYA SUARA ANGKAT TELEPON
  $ quick_menu=False
  scene black with dissolve
  play music "audio/BGM_Happy dan Handphone.mp3" fadein 1.0
  scene kelas with dissolve
  $ quick_menu=True
  freya "Apaan?"
  freya "Oo ini udah selesai. Kamu telat sih, ya udah gimana lagi."
  freya "Ga ada yang mintain izin ke dosen, orang ga ada kabar..."
  freya "Ya udah, dadah."
  play sound "audio/ding.mp3"
  #HARUSNYA SUARA TUTUP TELEPON
  stop music fadeout 1.0
  $ quick_menu=False
  scene black with dissolve
  play music "audio/BGM_Kelas.mp3" fadein 1.0
  scene kelas with dissolve
  $ quick_menu=True
  mcname "Itu tadi Naya?"
  freya "Iya katanya dia ketiduran, hadeuhh. Ya udah lah gimana lagi."
  mcname "Hadeeeh..."
  freya "Btw kamu udah siapin kado belum buat Naya? Kan dia 4 hari lagi ultah."
  mcname "EEHHHH!???"
  "[mcname] menjawab dengan suara yang cukup keras, hingga terdengar hingga ke ujung kelas dan membuat Mahasiswa/i yang masih ada di dalam kelas terkejut."
  freya "Biasa aja napa sih? Ya udah deh kamu siapin hadiahnya yang bener ya. Awas aja kalau ga ngasih hadiah!"
  freya "Oke, aku duluan ya. Ada janji sama yang lain, dahhh."
  mcname "Heeeee..."
  stop music fadeout 1.0
  $ quick_menu = False
  scene black with dissolve
  play music "audio/BGM_Kosan 1.mp3" fadein 1.0
  scene kamar mc kota with dissolve
  $ quick_menu = True
  "Karena hari ini hanya ada satu kelas, [mcname] memilih untuk menghabiskan waktunya di kosan sambil memikirkan apa yang cocok sebagai kado ulang tahun untuk Kana."
  mcname "{i}Aduuhhh aku ngasih apa ya buat Kana? Kalau diinget-inget lagi, Kana tuh suka sama jejepangan.{/i}"
  mcname "{i}Tapi masa aku ngasih Naya merch anime? Aku ga pernah liat dia pake pakaian anime-anime gitu sihh.{/i}"
  mcname "{i}Kalau official CD anime atau band? Tapi aku ga tau dia suka band apaan, aaaa bingung banget mau ngasih apa.{/i}"
  "Seakan sedang terjadi perang di dalam pikiran [mcname], tanpa terasa waktu berubah menjadi malam."
  "[mcname] hanya bisa kebingungan memilih kado ulang tahun apa yang cocok."
  "Tiba-tiba terdengar bunyi dari HP yang menunjukkan bahwa HP perlu dicharge, akan tetapi ternyata ada notifikasi lain dari Kana dan Freya yang mencoba menghubungi [mcname] berkali-kali."
#*BG HP LAGI TELEPON*
  freya "Nahhh kan kalau gini enak, ga usah ngehubungin satu-satu."
  mcname "Ah Naya, Freya, maaf ya tadi aku ketiduran."
  kana "Iya gapapa. Tadi juga aku terlalu spam, maaf ya."
  mcname "Enggak apa-apa, aku ga sempet liat semua chatnyaa. Sorry."
  freya "Jadi tadi kenapa Nay?"
  kana "Harus aku yang ngejelasin?"
  mcname "Ya udah, sini deh aku yang jelasin."
  freya "Lah, emang tau ada apa?"
  mcname "Ya nggak lah, makanya cepet jelasin."
  kana "Hahahaha."
  freya "Hadeeeh/"
  kana "Oke, jadi TLDR aja nih ya. Lusa tuh bakalan ada event di cafe mall yang udah aku tungguin banget dari beberapa bulan yang lalu."
  kana "Nah di eventnya tuh, bakalan ada cake yang dijual. Sumpah itu enak banget cakenya."
  kana "Terus, yang bikin aku pengen banget tuh cakenya limited edition gitu, jadi aku bisa jamin kalau cakenya itu bakalan ENAKKKKK BANGETTT."
  kana "Aku jamin itu bakalan enak banget. Kalau ga enak, nanti aku traktir makan di all you can eat deh."
  kana "Nahhhh tapi yang jadi masalahnya tuh, di event itu satu orang cuma bisa beli satu buah cake aja."
  kana "Jadi nanti aku pengen ajak Freya sama kamu buat antri dan beli juga."
  kana "Nanti uangnya dari aku kok, santai aja. Tapi nanti ikut antri biar bisa beli juga."
  freya "Kayaknya itu kepanjangan deh buat TLDR, Nay."
  mcname "Keknya TLDR-mu itu \"To Long Di Read\", Nay."
  kana "Hehehe, maaf terlalu semangat."
  mcname "Tapi oke, intinya lusa kan?"
  kana "Iya lusa."
  mcname "Oke aku bisa kok."
  freya "Yaudah nanti kabarin lagi yaa. Aku mau tidur dulu."
  kana "Okeee, good night minna~"
  mcname "Oke, good night."
#*BG HP LAGI TELEPON SELESAI*
  mcname "Hmmmmmm."
  mcname "{i}Oke nanti aku harus liat-liat sekalian milih hadiah apa yang kayaknya cocok buat Naya di mall.{/i}"
  stop music fadeout 1.0
  $ quick_menu = False
  scene black with dissolve
  show text "{color=#FFF}BEBERAPA HARI KEMUDIAN{/color}" with Pause (2.0)
  play music "audio/BGM_Mall Slow.mp3" fadein 1.0
  scene mall temp with dissolve
  $ quick_menu = True
  "Hari itu [mcname] pergi ke mall untuk menemani Kana membeli limited cake."
  "Di sana [mcname] berencana untuk melihat gerak-gerik Kana sebagai petunjuk tentang hadiah apa yang cocok untuknya."
  kana "Ah, halo [mcname]. Sorry, lama nunggu ya?"
  mcname "Enggak, kok. Haha."
  kana "Freya belum dateng ya? Hmmmm..."
  mcname "Tunggu bentar lagi deh haha."
  kana "Yaudaah."
  $ quick_menu = False
  scene black with dissolve
  scene mall temp with dissolve
  $ quick_menu = True
  kana "Aduhh ini Freya ke mana sih? Jangan bilang dia lupa?"
  mcname "Waduh aku juga ga tau tuh Nay, coba kamu telepon."
  kana "Oke bentar yaa-"
#SFX KRINGGG Telepon*
#BG Telepon ON
  kana "Eh?"
  kana "FREYAAA!! Kamu ke mana??"
  kana "HA!?? Aduhhh… ya udah deh."
#BG Telepon OFF
  kana "Umm [mcname], ini Freya katanya ada urusan di kampus. Jadinya kita berdua aja nih hehe, kaya waktu itu."
  mcname "Ahahaha, iya nih. Masih inget aja kamu. Ya udah yuk jalan."
  kana "Hahaha, okee deh."
  $ quick_menu = False
  scene black with dissolve
  scene mall temp with dissolve
  $ quick_menu = True
  "Saat masuk ke dalam mall dan berjalan ke arah cafe, Kana sempat beberapa kali curi-curi pandang ke arah toko perhiasan yang ada di dalam mall."
  "Lalu [mcname] pun sempat menanyakan beberapa hal."
  mcname "Eh Nay, tumben kamu ganti sepatu."
  kana "Iya nih. Kemarin pas aku coba udah agak sempit gitu sih, jadi ini pake sepatu yang lain haha."
  mcname "Ohhh gitu ya, kamu lagi suka apa belakangan ini?"
  kana "Heee? Kamu kenapa [mcname], kok tiba-tiba tanya kayak ginian?"
  mcname "Gak apa-apa, daripada -1 topik hahaha."
  kana "Hahaha, iya juga sih. Aku akhir-akhir ini sama sepupuku biasanya main masak-masak gitu sih."
  mcname "Ohhh gitu ya, eh itu cafenya kan?"
  mcname "{i}Mantep aku dapet beberapa ide kado buat Kana, hehehe.{/i}"
  kana "Iya, udah ya kita pura-pura ga kenal dulu biar ga dicurigai haha."
  mcname "Oke dehh."
  "Setelah membeli cake tersebut, [mcname] dan Kana pun bertemu."
  mcname "Ini cakenya Nayy."
  kana "Ehhh? Gapapa nih?"
  mcname "Gapapa, soalnya keliatannya kamu suka banget cake ini."
  kana "Wihhh thank you [mcname]!"
  kana "Kalo gitu aku pulang dulu ya, mau menikmati cakenya ehehehe."
  mcname "Okeee, hati-hati di jalan."
  "Kana pun pulang ke rumahnya, tidak sabar untuk menikmati limited cake yang baru saja dibelinya."
  $ quick_menu = False
  scene black with dissolve
  scene mall temp with dissolve
  $ quick_menu = True
  "Tetapi, [mcname] tidak pulang. Dia menghabiskan harinya di Mall dan memikirkan hadiah apa yang cocok untuk Kana."
  mcname "{i}Hmmm dari obrolan dan kode-kode yang Kana kasih, mending aku beliin apa ya?{/i}"
  #*CHOSE*
  menu:
    "Yang kamu beli..."
    "Kalung":
      $ kana_present = "Kalung"
      jump truekanabuypresent
    "Sepatu":
      $ kana_present = "Sepatu"
      jump truekanabuypresent
    "Alat Masak":
      $ kana_present = "Alat Masak"
      jump truekanabuypresent
    "CD Film Horror":
      $ kana_present = "CD Film Horror"
      jump truekanabuypresent

label truekanabuypresent:
  mcname "Oke kayaknya ini cocok deh buat Kana, sekarang waktunya pulang dan siap-siap buat besok pas ulang tahun Kana."
  stop music fadeout 1.0
  $ quick_menu = False
  scene black with dissolve
  play music "audio/BGM_Kosan 1.mp3" fadein 1.0
  scene kamar mc kota with dissolve
  $ quick_menu = True
  "Setelah [mcname] sampai di kosan, dia menghubungi Freya untuk membahas rencana ulang tahun Kana."
#*CHANGE/ADD BG HP*
#*CHATTING APP*
  mcname "Freya."
  freya "Kenapa?"
  mcname "Ini, mau nanya buat ultah Kana nanti. Kita bakalan gimana nih ngasih suprisenya? Terus mau di mana?"
  freya "Kalau tempat mah udah aman aja. Biasanya aku di rumah Kana sih, nanti kamu dateng aja."
  mcname "Emangnya boleh ya?"
  freya "Ga ada yang ngelarang kok. Nanti ga perlu dekorasi apa-apa, soalnya Si Naya ga suka kalo dirayain gede-gede pake aksesoris gitu."
  freya "Dulu pernah gitu, dia malah bete seharian. Lagian dia juga ga pernah inget hari ultahnya."
  mcname "Oke deh kalau emang gitu, nanti aku tinggal dateng aja ke rumah Kana?"
  freya "Iya nanti dateng aja, biar aku yang urus hehe."
  mcname "Okee. Thanks, Freya."
  freya "Iya sama-sama."
#CHATTING APP OFF
  "Setelah semua itu, akhirnya [mcname] dan Freya setuju untuk melakukan perayaan ulang tahun sederhana di rumah Kana. Setelah itu [mcname] memutuskan untuk tidur."
  stop music fadeout 1.0
  $ quick_menu = False
  scene black with dissolve
  show text "{color=#FFF}HARI ULANG TAHUN KANA{/color}" with Pause (2.0)
  play music "audio/BGM_Kosan 2.mp3" fadein 1.0
  scene kamar mc kota with dissolve
  $ quick_menu = True
  mcname "{i}Oke. Hari ini hari yang penting, pokoknya semua harus siap!{/i}"
  mcname "{i}Bentar cek dulu semuanya, pakaian? Oke.{/i}"
  mcname "{i}Hadiah? Oke, ada udah di bungkus juga.{/i}"
  mcname "{i}Wangy? Oke, tadi udah mandi sama pake parfum juga.{/i}"
  mcname "{i}Tinggal berangkat aja nih harusnya. Duh deg degan banget hari ini, mudah-mudahan lancar deh.{/i}"
  stop music fadeout 1.0
  $ quick_menu = False
  scene black with dissolve
  play music "audio/BGM_MC Pertama Kali ke JKT + BG Pagi.mp3" fadein 1.0
  scene awan with dissolve
  $ quick_menu = True
  "[mcname] pun datang ke rumah Kana pada waktu yang telah ditentukan sebelumnya dengan Freya. Tetapi saat [mcname] menghubungi Freya, ia tidak dapat dihubungi."
  "Rasa cemas, gelisah, serta was-was tidak dapat dihapus dari pikiran [mcname]."
  "Mungkin ini pertama kalinya [mcname] berinisiatif merayakan ulang tahun temannya seperti ini, sehingga ingin memberikan momen bahagia yang selalu dapat diingat oleh Kana."
#ASSET PINTU RUMAH KANA
  mcname "{i}Aduhhh masuk ga ya, tapi belum ada Si Freya.{/i}"
  mcname "{i}Tapi kalau di luar terus, nanti takut dicurigain orang-orang. Mending gimana ya...{/i}"
  menu:
    "Yang [mcname] lakukan..."
    "PERGI KE DALAM RUMAH.":
      #BG Ruang Tamu.
      jump truekanabeforeneutralroute
    "TUNGGUIN FREYA.":
      #*CHOSE B*
      "[mcname] memilih untuk menunggu Freya. Tak lama kemudian, Freya pun datang."
      mcname "Haloo."
      freya "Halo [mcname]."
      mcname "Yuk?"
      freya "Gasss!"
      play sound "audio/ding.mp3"
      "Freya memencet bel rumah Kana."
      play sound "audio/open_door.mp3"
      jump truekanaNungguFreya

label truekanabeforeneutralroute:
  #*CHOSE A*
  "[mcname] pun memutuskan untuk mengetuk pintu tanpa menunggu Freya."
  play sound "audio/ding.mp3"
  with Pause (2.0)
  play sound "audio/open_door.mp3"
  "Mamah Kana" "Ah [mcname]. Ada apa?"
  mcname "Halo Tante, Kana ada di rumah?"
  "Mamah Kana" "Ada kok, kenapa?"
  mcname "Jadi sebenarnya saya sama Freya mau ngadain kejutan untuk ulang tahun Kana."
  "Mamah Kana" "Eeeeh, makasih banyak ya [mcname]. Kana pasti bakal seneng banget!"
  mcname "Hehe, btw tante masih inget waktu itu pernah bilang mau ngabulin satu permintaan?"
  "Mamah Kana" "Iya, kenapa nih tiba-tiba."
  mcname "Kalo bisa, mau minta tolong kejutannya dirahasiakan dari Kanaa."
  "Mamah Kana" "Eeehh, oke oke. Tante gak bakal ganggu, hehe."
  mcname "Terima kasih banyak, tante."
  "Mamah Kana" "Ya sudah, ayok sini masuk dulu."
  stop music fadeout 1.0
  $ quick_menu = False
  scene black with dissolve
  play music "audio/BGM_Lorong.mp3" fadein 1.0
  scene lorong with dissolve
  #RUANG TAMU RUMAH KANA
  $ quick_menu = True
  mcname "Siang Nay, maaf telat ya?"
  kana "Engga kok sini masuk aja. Freya belum datang, nanti biasanya dia suka telat dikit."
  mcname "Eh, i-iya Nay."
  kana "Mau minum apa [mcname]? Sekalian nunggu Freya nih. Btw kok gugup sih, emang ada apa?"
  mcname "E-engga kok, cuma ini kan pertama kali kita berduaan… J-jadi agak gugup dikit."
  kana "Lah? Bukannya kemarin pas aku sakit, kamu temenin aku ya? Terus kita kan pernah ke cafe bareng, game center bareng, event jejepangan bareng, ke mall kemarin juga kita berduaan. Kamu ga anggep itu kah? Sedih sih, huhuhu."
  mcname "E-eh maksudnya gak gitu. Cuma entah kenapa hari ini aku lebih gugup aja dari biasanya.."
  kana "Gugup kenapa?"
  mcname "E-ehh itu..."
  mcname "{i}Aduhh kok aku gugup ya? Apa gara-gara mau ngasih hadiah ke Naya, terus takut dia gak suka ya?{/i}"
  mcname "Ya gitu deh, haha. Ini Si Freya ke mana ya, tumben lama."
  kana "Hmmm... Sebenernya kalian mau ngapain deh? Soalnya Si Freya Freya itu gak ngasih tau mau kumpul buat apaan?"
  mcname " Eh-"
  mcname "{i}Mampus, harus alesan apa ya biar bisa bohongin Kana?{/i}"
  mcname "Eh itu... Sebenarnya kita mau-"
  play sound "audio/open_door.mp3"
#HARUSNYA SUARA BRAK!
  "Sebelum [mcname] sempat menyelesaikan kata katanya, suara Freya terdengar dari arah pintu masuk."
  freya "HALOOOO SEMUANYAAA!!!"
  kana "Ah Frey, kaget."
  mcname "Waduh, Freya bikin kaget aja."
  jump truekananeutralroute1

#[Neutral Route 1]
label truekanaNungguFreya:
  "Mamah Kana" "Ah [mcname], Freya. Ada apa?"
  freya "Halo Tante, Kana ada di rumah?"
  "Mamah Kana" "Ada kok, kenapa?"
  freya "Jadi sebenarnya kita mau ngadain kejutan untuk ulang tahun Kana."
  "Mamah Kana" "Eeeeh, makasih banyak ya kalian. Kana pasti bakal seneng banget!"
  mcname "Btw tante masih inget waktu itu pernah bilang mau ngabulin satu permintaan?"
  "Mamah Kana" "Iya, kenapa nih tiba-tiba."
  mcname "Kalo bisa, mau minta tolong kejutannya dirahasiakan dari Kanaa."
  "Mamah Kana" "Eeehh, oke oke. Tante gak bakal ganggu, hehe."
  freya "Terima kasih banyak, tante."
  "Mamah Kana" "Ya sudah, ayok sini masuk dulu."
  mcname "Baik."
  stop music fadeout 1.0
  $ quick_menu = False
  scene black with dissolve
  play music "audio/BGM_Lorong.mp3" fadein 1.0
  scene lorong with dissolve
  #RUANG TAMU RUMAH KANA
  $ quick_menu = True

label truekananeutralroute1:
  freya "Hehe halo Naya, udah siap kan?"
  kana "Hah, siap?"
  mcname "Waduh Freya."
  freya "Lahh ini nih, padahal aku dah semangat gini. Dah bawa banyak game-game buat temenin kita sampe malem nih."
  kana "Ha?? Main game?"
  "Freya melihat ke arahku, seakan memberi kode secara tidak langsung. [mcname] mengangguk ke arah Freya."
  mcname "Lah iya Nayy, kamu ga tau? Kita kan bakalan main game lohhh."
  kana "Hmmm... Ya udah deh, aku ngikut aja."
  freya "Let's gooo!"
  "Mereka pun memainkan semua permainan yang dibawa oleh Freya."
  stop music fadeout 1.0
  $ quick_menu = False
  scene black with dissolve
  play music "audio/BGM_Lorong.mp3" fadein 1.0
#HARUSNYA BGM RUANG TAMU RUMAH KANA
  scene lorong malam with dissolve
#HARUSNYA RUANG TAMU RUMAH KANA
  $ quick_menu = True
  "Tak terasa malam pun tiba."
  freya "Eh kita pindah ke kamarmu aja yuk Nay. Udah malem, takut ganggu Mamahmu sama tetangga."
  kana "Iya sih, ya udah deh ayo."
  stop music fadeout 1.0
  $ quick_menu = False
  scene black with dissolve
  play music "audio/BGM_Kosan 1.mp3" fadein 1.0
#HARUSNYA BGM KAMAR KANA
  scene kamar kana with dissolve
  $ quick_menu = True
  mcname "Eh Freya, emang ruangan Naya kedap suara kah? Kok kita pindah ke sini?"
  freya "Iya mamahnya Naya masangin peredam suara, biar kalau dia berisik main game gak ganggu tetangga."
  kana "Perasaan ini kamarku, tapi kok kamu yang lebih tahu daripada aku."
  mcname "Hahaha."
  "Ini mungkin ketiga kalinya [mcname] ke kamar Kana, akan tetapi kali ini ia bisa melihat ruangan kamar Kana dengan lebih seksama."
  "[mcname] melihat ternyata di pojok ruangan kamarnya Kana tersembunyi satu tempat khusus yang dipenuhi kumpulan-kumpulan figur dan merch anime."
  mcname "Wahhhh… Kana ini kan dari anime itu, keren banget kamu punya? Bukannya ini limited-edition ya?"
  kana "Iya, hahaha. Ini aku nabung dari lama, untung dapet."
  mcname "Eh kalau ini dari anime itu kan? Boleh diliat dari deket ga?"
  kana "Boleh kok, liat aja. Asal jangan sampai rusak, hahaha."
  freya "Seneng banget tuh diliat-liat."
  mcname "Hehe sorry, soalnya ini kesukaanku juga."
  freya "Ya udah kalian have fun dulu ya, aku mau ke toilet dulu bentar."
  "Setelah mengatakan itu, Freya memberikan kode kepada [mcname] yang langsung mengerti apa yang dimaksud Freya."
  mcname "Eh, Nay. Kalau ini kamu beli dari luar negeri? Setauku di Indo belum ada."
  kana "Ehhh kalo itu sih beli di..."
  "[mcname] pun terus mengobrol dengan Kana, berusaha untuk mengalihkan perhatian Kana."
  stop music fadeout 1.0
  $ quick_menu = False
  scene black with dissolve
  play music "audio/BGM_Kosan 2.mp3" fadein 1.0
#HARUSNYA BGM KAMAR KANA
  scene kamar kana with dissolve
#HARUSNYA BG KAMAR KANA MALAM
  $ quick_menu = True
  "Tak terasa, jam menunjukan 12 malam yang menandakan bahwa hari telah berganti dan hari ulang tahun Kana pun tiba."
  mcname "Nay..."
  kana "Iya [mcname]?"
  mcname "Kamu lagi apa?"
  kana "Lagi duduk di kasur doang…"
  kana "Kamu kenapa sih dari tadi kaya ada yang aneh gitu?"
  mcname "Eh iya maaf, hehe."
  mcname "Gugup aja sih."
  kana "Gugup kenapa?"
  mcname "Jadi sebenernya... Aku ada hadiah buat kamu."
  "[mcname] mendekati Kana yang sedang duduk di kasurnya."
  kana "Hadiah?"
  mcname "Iya, tapi kamu harus tutup mata dulu."
  kana "Hah? Tutup mata?"
  mcname "Iyaa, udah tutup mata dulu sana."
  kana "O-oke."
  "Kana pun menutup matanya."
  stop music fadeout 1.0
  $ quick_menu = False
  scene black with dissolve
  $ quick_menu = True
  #Kalau di mall pilih:
  if kana_present = "Kalung":
    jump truekanarightpresent

  elif kana_present = "Sepatu": #Sepatu
    $ quick_menu = False
    window auto hide
    with Pause(2.0)
    play sound "audio/run.mp3"
  #HARUSNYA *SFX Suara Kresek*
    window auto show
    $ quick_menu = True
    kana "Udah boleh buka mata belum?"
    mcname "Bentar lagi."
    $ quick_menu = False
    window auto hide
    with Pause(2.0)
    play sound "audio/run.mp3"
  #HARUSNYA *SFX Suara Kresek*
    window auto show
    $ quick_menu = True
    kana "[mcname]?"
    mcname "Udah boleh buka matanya Nay."
    kana "O-okee."
    "Perlahan Kana membuka matanya."
    $ quick_menu = False
    scene black with dissolve
    scene kamar kana with dissolve
  #HARUSNYA BG KAMAR KANA MALAM
    $ quick_menu = True
  #MUNCUL Asset Sepatu Hadiah ultah Kana
    "Kana terdiam sejenak."
    "Lagi-lagi Kana terdiam."
    "Kana masih terdiam..."
    mcname "Nay?"
    kana "Eh i-iya makasih banyak ya. Tapi kok kamu tau ukuran sepatu aku, padahal aku ga pernah bilang ke kamu maupun Freya. Kamu tau dari mana?"
    mcname "....."
    kana "[mcname]...?"
    "Kana pun merasa aneh dengan [mcname], semua kedekatan mereka langsung sirna di hati Kana."
    "Kana langsung kabur sambil memanggil Freya untuk meminta tolong."
    scene black with Dissolve(2.0)
    show text "{color=#FFF}ADUHHH BROOO, KOK LU TAU UKURAN SEPATU KANA SIH?? NGERI KALI BROO, LU STALKER YA?{/color}" with Pause(2.0)
    show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
    play music "audio/Dreamcatcher_v2.mp3"
    jump credits

  elif kana_present = "Alat Masak": #Alat Masak
    $ quick_menu = False
    window auto hide
    with Pause(2.0)
    play sound "audio/run.mp3"
  #HARUSNYA *SFX Suara Kresek*
    window auto show
    $ quick_menu = True
    kana "Udah boleh buka mata belum?"
    mcname "Bentar lagi."
    $ quick_menu = False
    window auto hide
    with Pause(2.0)
    play sound "audio/run.mp3"
  #HARUSNYA *SFX Suara Kresek*
    window auto show
    $ quick_menu = True
    kana "[mcname]?"
    mcname "Udah boleh buka matanya Nay."
    kana " O-okee."
    "Perlahan Kana membuka matanya."
    $ quick_menu = False
    scene black with dissolve
    scene kamar kana with dissolve
  #HARUSNYA BG KAMAR KANA MALAM
    $ quick_menu = True
  #MUNCUL Asset CD Blu-ray
    "Raut wajah Kana bingung dan terheran-heran, kenapa [mcname] memberikan dia alat masak set lengkap."
    kana "Ummm ini apa?"
    mcname "Ini alat masak, Nay. Soalnya kamu pernah bilang sepupumu sering datang masak-masakan. Nah aku kasih hadiah buat kamu, siapa tau aku juga bisa cobain masakan kamu hehe."
    kana "Ummm, tapi sepupuku masih TK, jadi dia pake mainan alat masak-masak..."
    mcname "...."
    kana "...."
    "Kana terdiam tanpa kata-kata, hingga Freya datang dan kaget dengan hadiah yang [mcname] berikan."
    "Pandangan Kana dan Freya terhadap [mcname] pun menjadi aneh."
    scene black with Dissolve(2.0)
    show text "{color=#FFF}IH BROO, YA KALI AJA NGASIH HADIAH ALAT MASAK KE CEWE YANG TINGGAL SAMA ORTUNYA TERUS MASIH KULIAH, DIKIRA HADIAH ORANG NIKAHAN KALI YA.{/color}" with Pause(2.0)
    show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
    play music "audio/Dreamcatcher_v2.mp3"
    jump credits

  elif kana_present = "CD Film Horror": #CD Film Horror
    $ quick_menu = False
    window auto hide
    with Pause(2.0)
    play sound "audio/run.mp3"
  #HARUSNYA *SFX Suara Kresek*
    window auto show
    $ quick_menu = True
    kana "Udah boleh buka mata belum?"
    mcname "Bentar lagi."
    $ quick_menu = False
    window auto hide
    with Pause(2.0)
    play sound "audio/run.mp3"
  #HARUSNYA *SFX Suara Kresek*
    window auto show
    $ quick_menu = True
    kana "[mcname]?"
    mcname "Udah boleh buka matanya Nay."
    kana "O-okee."
    "Perlahan Kana membuka matanya."
    $ quick_menu = False
    scene black with dissolve
    scene kamar kana with dissolve
  #HARUSNYA BG KAMAR KANA MALAM
    $ quick_menu = True
  #MUNCUL Asset CD Blu-ray
    "Kana membuka dan melihat bahwa ada CD Blu-ray yang berjudul “The Conjurang” dengan cover yang gelap, mengerikan, dan ada hantunya."
    mcname "Ini film baru loh, katanya viral dan terinspirasi dari kisah nyata. Bisa kali ya kita nonton bareng-bareng nanti, jadi kita nobar gitu konsepnya hahah."
    kana "Tapi… Aku ga suka horror. Ini cuma kesukaan kamu aja, kan?"
    mcname "I-iya sih tapi…"
    "Kana pun meminta maaf dan menolak hadiah dari [mcname]. Bahkan dia terlalu takut untuk menyimpan CD Blu-ray itu."
    scene black with Dissolve(2.0)
    show text "{color=#FFF}ADUH BROOO LAIN KALI KALO MAU NGASIH HADIAH TUH HARUS MIKIRIN JUGA APA YANG DIA SUKA, JANGAN LU DOANG YANG SUKA.{/color}" with Pause(2.0)
    show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
    play music "audio/Dreamcatcher_v2.mp3"
    jump credits

label truekanarightpresent:
  #*CHOSE A*
  #*SFX Suara Kresek*
  #play sound "audio/open_door.mp3" fadeout 1.0
  "[mcname] mengambil kalung dan mulai memakaikannya ke leher Kana. Kana pun merasakan ada sensasi dingin di lehernya, curiga akan sesuatu Kana pun bertanya."
  kana "E-eh ini apa?"
  mcname "Sabar-sabar. Aman kok, bukan yang aneh-aneh."
  kana "E-eeeeeh."
  mcname "Udah boleh buka matanya Nay."
  kana " O-okee."
  #Narrator
  "Perlahan Kana membuka matanya."
  $ quick_menu = False
  scene black with dissolve
  play music "audio//BGM_Rooftop Romance Pia.mp3" fadein 1.0
  scene kana awal with dissolve
#HARUSNYA CG KANA END
  $ quick_menu = True
  "Saat Kana membuka matanya, dia terlihat kaget dan terkejut karena di lehernya terdapat sebuah kalung cantik bersinar yang berwarna biru."
  "Ternyata sensasi dingin yang sebelumnya terasa, adalah kalung."
  kana "EH INI KANN!!??"
  mcname "Selamat ulang tahun~!"
  kana "EHH!!!?? K-kamu tau hari ulang tahun ku?"
  mcname "Tau doong. Sekali lagi, selamat ulang tahun Kanaia Asa~"
  mcname "Bagiku, kamu orang yang spesial. Jadi, aku pengen ngasih hadiah yang spesial juga."
  kana "*BLUSH*"
  kana "M-makasih banyak ya."
  mcname "Hehe, gimana Nay kamu suka?"
  kana "BANGETTTT, aku suka pake banget. Kok kamu tau aku lagi pengen kalung sih?"
  mcname "Kita kan kemarin abis ke mall, terus aku liat kamu merhatiin toko perhiasan gitu."
  mcname "Jadinya aku beli kalung ini sambil bayangin kamu dan aku rasa kalung ini cocok buat kamu."
  kana "Iiiiii makasih banyak yaa, [mcname]"
  mcname "Iya Kana..."
  kana "Aduhhh. A-aku ga bisa berhenti senyum, ini bagus bangett."
  mcname "Bagus deh kalo kamu suka. Aku malah takut kamu ga suka dan jadi benci sama aku."
  kana "Aku suka banget. Lagian ga usah ngasih pun gapapa kok. A-aku ga bakalan bisa benci kamu."
  mcname "Eeeehh."
  mcname "*Blush*"
  mcname "Ke-kenapa?"
  kana "Soalnya..."
  mcname "........."
  kana "*Blush*"
  kana "[mcname]... Sebenarnya aku suk-"
  stop music
  $ quick_menu = False
  window auto hide
  play sound "audio/open_door.mp3"
#HARUSNYA *SFX Pintu Didobrak*
  scene black
  with Pause(2.0)
  window auto show
  play music "audio/BGM_Lawak Tana.mp3" fadein 1.0
  scene kamar kana with dissolve
  $ quick_menu = True
  freya "HAPPY BIRTHDAYYY NAYAAAA~!!!!"
  "Tanpa angin tanpa hujan, tiba-tiba Freya datang membuka pintu kamar Kana."
  "Melihat ke arah Kana dan [mcname] yang sedang berduaan dan suasana yang terasa berbeda dari biasanya, membuat Freya pun tersadar."
  freya "Eh? Sorry kayaknya ganggu, hehe."
  freya "Kalian lanjutin aja dulu berdua, hehe."
  freya "Hehe, aku pergi dulu baaay~"
  kana "F-FREEEEYYAAAAAAA~!"
  kana "*Blush*"
  mcname "Hahahahaha!"
  kana "K-kamu jangan ketawa [mcname]!!!"
  kana "*Blush*"
  "[mcname] tertawa dan Kana tersipu malu sambil memandang ke arah [mcname]."
  "Malam itu..."
  "Menjadi malam yang tidak akan terlupakan bagi [mcname] dan Kana."
  scene black with dissolve
  show text "{color=#FFF}THE END{/color}" with Pause(2.0)
  play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
  jump credits