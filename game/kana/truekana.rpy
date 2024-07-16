label truekana:
  $ renpy.block_rollback()
  scene kantin with Dissolve(2.0)
  $ quick_menu = True
  mcname "Ehhh tapi udah kelamaan ini, ga enak sama Kana nunggu lama."
  "[mcname] pun memilih untuk mengabaikan flayer tersebut, lalu lari agar bisa datang tepat waktu."
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
  mcname "Ehh Kana, kamu tau ga siiih?"
  show kana_side at left with dissolve
  kana "Iya [mcname]? Kenapa?"
  hide kana_side at left with dissolve
  mcname "Aku denger-denger ada event jejepangan yang bakalan diadain sama pihak kampus gitu loh."
  show kana_side at left with dissolve
  kana "YANG BENER!!??"
  hide kana_side at left with dissolve
  mcname "Aku denger-denger ada event jejepangan yang bakalan diadain sama pihak kampus gitu loh."
  "Kana pun menjawab dengan penuh semangat, saking semangatnya ia sampai berdiri dari tempat duduknya dan membuatnya diliatin oleh orang-orang sekitar. "
  mcname "Semangat banget kamu Kana, ahahah. Sampe diliatin orang-orang loh."
  show kana_side at left with dissolve
  kana "EH!??? I-iyya maaf maaf, terlalu excited dengernya. Denger-denger sih event jejepangan kampus ini tuh selalu rame gitu, makanya aku excited. Apalagi bareng temen, hehe."
  hide kana_side at left with dissolve
  mcname "Eh…i-iya kana, kalau gitu kamu mau ke eventnya bareng aku, gak? Sekalian ajarin aku, soalnya ini kan event pertamaku hehe."
  show kana_side at left with dissolve
  kana "B-boleh….nanti kita kabar kabaran aja deh."
  hide kana_side at left with dissolve
  "Setelah itu mereka pun menghabiskan makanannya, lalu Kana dan [mcname] pun berpisah karena sudah ada kegiatan masing-masing yang harus dilakukan. Tak terasa waktu pun telah berlalu dan malam hari telah tiba."
  jump truekanakos

label truekanakos:
  scene mc bedroom
  mcname "{i}Aduuuh, mulai chat nya gimana ya? Bingung…{i}"
  $ quick_menu=False
  menu:
    "P":
      "[mcname] memilih untuk menghubungi Kana dengan awalan “P”, dibandingkan hal lainnya. Kana pun tidak membalas chat tersebut dan meng-ghosting pesan dari MC sampai event di mulai…"
      # BadEnding
    "Malam nay sibuk ga?":
      "[mcname] memilih untuk langsung menelepon Kana dan ternyata Kana sedang bersama keluarga dan tanpa sengaja Kana memblokir nomor MC karena MC menelepon terus menerus."
      # BadEnding
    "Langsung telepon aja":
      "[mcname] menghubungi Kana lewat HPnya, di situ MC bertanya tentang kabarnya terlebih dahulu dan basa basi seperti orang yang kehabisan topik."
      # scene call hp
  
  #*SKIP TO SCENE*
  #*BG HP*

  #MC
  #“Malam Kana, sibuk nggak ya? Hehe”

  #Kana
  #“Umm engga kok knp ya ?(｡･∀･)ﾉﾞ” 

  #MC
  #“Aku mau nanya soal, event jejepangan itu, jadi kan?”

  #Kana
  #“Maksudnya jadi?”
  #MC
  #“Yaa jadi kan? Ummm kita berangkat bareng.”

  #Kana
  #“Jadi kok. Mau ketemuan jam berapa?┏ (゜ω゜)=👉”
  #MC
  #“Jam 7 lewat 12 gimana?”

  #Kana
  #“Jam 7 lewat 12 ? Kaya pernah denger di mana deh (⊙_⊙)？“

  #MC
  #“Ahh perasaan kamu aja kali, gimana ga kemaleman kah?”

  #Kana
  #“Hmmm, oke deh jam segitu aja.“
  #MC
  #“Btw nanti kita disana mau ngapain aja ya? Jujur ini event pertamaku, jadi tadi gimana tips n triknya buat di event, Yang Mulia Kanaia Asa?“

  #Kana
  #“IHHHH apaan sih. Ya udah jadi kalau dulu tuh biasanya aku-”

  #Tanpa sengaja Kana menekan tombol voice call dan MC pun tanpa pikir panjang menekan tombol jawab 

  #*SKIP TO SCENE*
  #*BG HP*
  #“Ehh maaf kepencet… aduh malu banget, aku matiin aja ya.”

  #MC
  #“ JANGAN !!!””

  #Kana terdiam kaget karena dengar suara MC yang tiba-tiba teriak .
  #“Maksudku… ga usah dimatiin kalau boleh, biar lebih seru ngobrolnya.”

  #Kana
  #“Uuu mmm… o-oke deh.”

  #MC
  #“Jadi gimana tadi pengalaman kamu? Aku nungguin loh, kasih tau dong biasanya gimana aja di event jejepangan tuh.“

  #Kana
  #“Oh iya lupa, jadi kalau aku dulu ikut event jejepangan tuh biasanya-”

  #Tanpa sadar Kana dan MC pun mengobrol lama, bahkan sampai melewati tengah malam. Beberapa kali MC mendengar Kana menguap dan menyarankan untuk mengakhiri voice call, tetapi ia tetap melanjutkan ceritanya seakan meluapkan semua cerita yang telah ia simpan sendirian selama ini… Beberapa saat kemudian pun Kana tertidur dengan voice call masih menyala.

  #MC
  #“Kana? Kana…”
  #*SFX Amimir*
  #Beberapa kali MC menyebutkan nama Kana akan tetapi Kana tetap tidak menjawab. Beberapa saat kemudian, MC menyadari bahwa Kana telah tertidur. Suara nafas Kana sempat beberapa kali terdengar, setelah beberapa saat MC pun memilih untuk mengakhiri voice call itu dan tidur agar besok tidak telat.


  #*SKIP TO SCENE*
  #*BG KOS (PAGI)*

  #MC bangun beberapa lebih awal daripada waktu yang telah dijanjikan, ia tidak sabar untuk pergi ke event tersebut dan menghabiskan waktu dengan Kana. MC dan Kana berjanji untuk bertemu di depan kampus. MC pun tidak lupa untuk makan, mandi, serta memakai parfum yang menurutnya lebih mahal daripada makannya selama 1 minggu. MC datang 10 menit lebih awal dari pada jam yang telah ditentukan sebelumnya.

  #*SKIP TO SCENE*
  #*BG DEPAN KAMPUS (INTERIOR JEJEPANGAN)

  #Kana
  #“ MC…ha…ha..haloo…maaf yaa… nunggu lama..”
  #Suara Kana terpotong-potong yang menandakan bahwa Kana sudah lari…

  #MC
  #“Hahah santai aja Nay, tarik nafas dulu bentar gitu. Keliatan banget kalau kamu baru lari tuh.“

  #Kana
  #“Maaf ya, tadi lumayan macet di jalan, makanya aku lari. Kukira udah telat, terus aku juga liat kamu udah ada di depan gerbang. Jadi tadi aku lari deh…“

  #MC
  #“Santai aja Nay. Ya udah, nih kamu minum dulu.“

  #IF CAN 
  #*SKIP TO CG*
  #*KANA AMBIL MINUM/KANA MINUM DARI BOTOL*

  #Kana
  #“Makasih ya MC. Sekarang udah aman kok, jadi kamu siap gak?”

  #*BACK TO BG EVENT*
  #MC
  #“Siap dong, ya kali ga siap. Nggak kaya siapa gitu, yang ketiduran di tengah-tengah call.”

  #Kana
  #“IHHHH kamu masih bangun???? Kukira udah dimatiin callnya“

  #MC
  #“Hahaha. Soalnya kamu asik banget, cerita ini itu, eh tiba-tiba diem. Pas dipanggil-panggil, kamu malah tidur. Mana sempet ngigo dikit juga.“

  #Kana
  #“KAMU DENGER!??? AAAAAA!!!“
  #“Lupaiin gak? Kalau engga, aku marah besar nih!“

  #MC
  #“Marah karir, maksudnya ?”

  #Kana
  #“LUPAINNN!!!”

  #MC
  #“Iya iya. Mending sekarang kita masuk yuk, keburu malem banget nanti pada tutup.”

  #Kana
  #“Awas aja kalau nggak, aku bakal buat kamu lupa dengan paksa!  Ya udah deh, ayo masuk. Aku dah ga sabar.“

  #MC dan Kana pun pergi ke event tersebut. Di sana banyak kegiatan, mulai dari event utama sampai event sampingan, diantaranya ada cosplay event, song cover competition, dan mini game yang terinspirasi dari permainan tradisional jepang lainnya.

  #MC
  #“Ehhh Kana bentar….
  #*huft*-*huft*-*huft*-*huft*
  #Sabar… Kana… kamu semangat banget sih… B-bentar aku tarik nafas dulu ya”

  #Kana
  #“Ahhh ayooo~ Kamu masa kalah sih sama aku?”

  #MC
  #“Soalnya kamu cepet banget ke sana ke sini nya. Belum ada 10 menit, kita dah pindah tempat mulu. Kamu ga mau liat-liat dulu booth merch yang ada di situ?”

  #Kana
  #“Ihhh kamu semalam ga research dulu tentang booth yang bakalan ada? Aku udah liat-liat listnya dan ada beberapa tempat yang pengen aku samperin. Jadi aku cuma bentar doang di tempat yang nggak aku pengen banget.”

  #MC
  #“Oooo gitu ya ternyata… Maaf deh ini kan event pertama ku, jadi aku ga tau harus research list kaya gitu.“

  #Kana
  #“Ya udah ayo ikutinn aku aja.”

  #Kana pun langsung menarik tangan MC yang hanya bisa mengikuti kemanapun Kana pergi, hingga Kana berhenti di suatu tempat,

  #MC
  #“Ummm Kana? Ada apa?”

  #Kana terdiam, di situ ada sebuah event yang sedang berlangsung. MC pun melihat event tersebut ada yang sedang menunjukan seseorang yang sedang melakukan sing cover competition.

  #*IF CAN*
  #*SKIP TO SCENE*
  #*BG PANGGUNG MINI*
  #*SPRITE TONO/PIA NYANYI FOR A SEC, AFTER THAT BACK TO BG EVENT*

  #MC pun melihat panggung dan mengerti kenapa Kana terdiam. Di situ, terlihat seorang perempuan yang sedang menyanyi dengan suara yang indah. Kurang lebih 3 menit MC dan Kana terdiam mendengarkan perempuan itu bernyanyi. Saat selesai, Kana dan MC pun bertepuk tangan dengan keras.
  #SFX Applause

  #MC
  #“ Gilaaaa, kereen bangeett sumpah! Iya ga, Kana?

  #Kana
  #“Iyaaa aku sampe terdiem loh, kamu juga dengerin tadi?

  #MC
  #“Iya lah, kamu tiba-tiba diem aja. Gimana aku ga ikutan dengerin? Keren banget, kapan ya aku bisa nyanyi kaya gitu… Btw kamu bisa nyanyi?”

  #Kana
  #“Eee-enggak kok, aku gak bisa nyanyi… Ehhh liat deh, di situ ada cosplay yang bagus mending kita ke sana.“ 

  #Kana tiba-tiba menghindari dari jawaban MC dan berlari ke arah seorang cosplayer.

  #Kana
  #“Eh Kaa, permisi~”

  #Cosplayer
  #“Iya Ka kenapa?”

  #MC
  #“Kenapa Kana… Ehh kamu cosplay jadi Kamen Driver Den-A  ya?”

  #Orang
  #“Wahhh iya ka, kebetulan aku juga suka.“

  #Kana
  #“ MC, kamu suka?”

  #MC
  #“SUKA!!??? Wahhhh aku ngikutin banget semua series kamen driver loh Kana.”

  #Orang
  #“Wahh, kukira ga terlalu banyak yang kenal cosplay ku. Ternyata ada juga ya yang kenal, makasih ya Kak. Eh Kak, mau ngobrol lagi ga? Keknya seru kita ngobrol bareng.“

  #*CHOSE*
  #Menghabiskan waktu sama orang
  #Menolak dan melanjutkan kegiatan dengan kana

  #*CHOSE A*
  #MC tetap mengobrol dengan cosplayer tersebut, dan mengabaikan keberadaan kana untuk beberapa saat, hingga saat MC sadar… Kana sudah menghilang dan HP nya tidak dapat dihubungi lagi…
  #BRO BRO LAGI JALAN BARENG BERDUAAN KO MALAH DITINGGAL NGOBROL SAMA ORANG LAIN SI ADUHHH

  #*CHOSE B*
  #MC
  #“Eh maaf ya nanti lagi, aku lagi sama temen soalnya. Kalau boleh minta social media nya kak, biar kita bisa ngobrol.“

  #Orang
  #“Ooh iya kak, ini ka bisa di add @namadonatur_angka random, makasih banyak yaa”

  #MC
  #“Sama sama ka…”
  #“Eh Kana maaf lama ya. Tadi hampir aja keasikan, untung aku inget ada kamu yang lagi nungguin aku haha.”

  #Kana
  #“E-enggak kok, ga lama… Seru ya...”

  #MC
  #“Eh kamu kenapa Kana, marah ya ? Tadi kelamaan ya?”

  #Kana
  #“E-enggak..”

  #MC
  #“Ya udah sebagai permintaan maaf aku ajak main di stand di sana deh gmn ?”

  #Kana
  #“ BEENER!?? Eh maksud nya… beneran nih?”

  #MC
  #“Iya, bener Kok. Ya udah, ayo.”

  #*SKIP TO SCENE*
  #*BG MINI GAMES*

  #Kana
  #“Kamu beneran bisa ga?”

  #MC
  #“ Bener Kana, tenang aja. Kok kamu ga percaya ke aku gitu sih.”

  #Kana
  #“Soalnya kamu keliatan ga yakin.“

  #Mc
  #“Ini aku lagi fokus, Kana.“


  #MC pun mendapatkan skor tinggi dan mendapatkan hadiah. 

  #MC
  #“Liat, kan? Aku bisaaa, siapa dulu?”
  #MC mendekatkan tangannya ke telinganya dan seolah olah menunggu Kana menjawab.

  #“Siapa dulu….hmmmm?”

  #Kana
  #“Iya iya, kamu jago deh.”

  #MC
  #“Nahh gtu dong, hahah.”

  #Setelah mendapatkan hadiah dari menyelesaikan mini game di dalam booth, MC sedikit bercanda dengan Kana karena telah memainkan mini game tersebut

  #MC
  #“Jadi Yang Muliaaa, kita mau ke mana lagi? Hambamu siap untuk menemanimu kemana pun dan sampai kapan pun, ahaha.”

  #Kana
  #“ Apaan sihh yang mulia yang mulia, mending mulai sekarang kamu panggil aku “Nay” deh.”“

  #MC
  #“ Okee dehh, Nay.“
  #“Eh Nay, kamu mau pesen apa? Aku traktir deh, kan udah diguide sana sini.“

  #Kana
  #“Hmmmm, apa ya? Kayaknya takoyaki enak deh.“

  #MC
  #“Bolehhh, tunggu bentar yaa.“

  #Kana
  #“Okeeee hati hati, ya.“

  #MC pun pergi meninggalkan Kana sejenak untuk membeli takoyaki. Setelah beberapa saat, MC kembali dengan membawa takoyaki.

  #MC
  #“Eh Nay, maaf ini cuma sisa satu porsi lagi. Ini buat kamu aja deh, aku gapapa.“

  #Kana
  #“Lah kok gitu sih, kamu juga pasti laper kan.”

  #MC
  #“Enggak koook.“
  #Tanpa sadar terdengar suara perut MC yang berbunyi cukup keras sehingga Kana dapat mendengarnya.

  #Kana
  #“Hahaha ga bisa bohong tuh perut kalau masalah makanan mah.”

  #Muka MC pun memerah, merasa malu dengan perutnya. 

  #MC
  #“Aduuhhhhh…”

  #Kana
  #“Sini kita makan bareng aja. Ini kan ada 6, kita bagi aja. Masing-masing 3 gimana?”

  #MC
  #“Tapi kan kamu pengen takoyaki.“

  #Kana
  #“Gak apa-apa kok, lagian aku juga makannya sedikit.“

  #MC
  #“O-oke deh kalau emang gitu. Eh tapi ini cuma ada satu doang garpu nya, bentar ya aku coba minta lagi ke penjualnya.“

  #Sesaat MC akan pergi, Kana tiba-tiba menangkap tangan MC. Dengan malu-malu Kana berkata.
  #Kana
  #“MC, udah ga usah.”
  #“Keburu takoyaki nya dingin, nanti ga enak. Kita makan bareng aja.”
  #“Sini, kita gantian aja.“
  #MC
  #“Nay? Bukannya itu malah…”

  #Kana
  #“Udah cepetan.“

  #MC
  #“I-iya iya. Oke deh.“

  #Kana pun memakan takoyakinya, lalu Kana pun menjulurkan tangannya yang memegang garpu serta takoyaki ke arah MC.

  #Kana
  #“Nih.”

  #Seakan tidak ingin sadar akan peristiwa yang sedang terjadi, MC tetap memakan takoyaki yang diberikan Kana. Takoyakinya terasa sedikit manis,  padahal takoyaki yang ia pesan harusnya pedas asin.
  #MC
  #“Eh udah abis lagi aja, ga kerasa ya…”
  #“Eh Nay, kamu kenapa?”

  #Muka Kana tiba-tiba memerah, mungkin Kana baru sadar akan apa yang terjadi saat itu. Tapi nasi telah menjadi bubur, hal ini tidak dapat ubah dan telah terjadi.

  #Kana
  #“E-eh iya udah abis aja.“
  #MC
  #“Okeeee, selesai jadi kita ke mana, Nay?“
  #Sesaat MC akan pergi, Kana tiba-tiba mengambil tisu, mengulurkan tangannya, dan mengelap saus yang ada di pipi MC.
  #Terkejut dengan tindakan Kana, MC hanya bisa terdiam saja, dan beberapa saat kemudian Kana pun sadar akan tindakannya 

  #Kana
  #“Eh ini, a-aku kebiasaan ngurus sepupuku yang masih kecil. Eh ah, ini kita udah kan makannya? Yu kita ke sana aja.“
  #Kana pun langsung pergi dari bangku tersebut, meninggalkan MC yang masih merasa malu di situ.

  #MC
  #“Ehhh?? Tungguin Nay.”
  #Kana dan MC pun pergi kembali untuk melihat lihat booth yang ada di event tersebut, sampai pada akhirnya event utama pada hari itu pun dimulai.

  #MC
  #“Eh nay, ayoo ini event utama nya udah mau dimulai.“

  #Kana
  #“Iya bentarr ini lagi bayar dulu.“

  #Kana dan MC pun pergi ke tempat di mana event utama diadakan. Event tersebut adalah pertunjukan kembang api kecil kecilan yang akan diadakan oleh panitia acara.

  #Kana
  #“TAMAAYAAAAAA~!”

  #MC
  #“TAMAYAAAAAA~!”

  #Kana dan MC pun menikmati pemandangan kembang api di event tersebut. Meski hanya beberapa menit saja, tapi kenangannya akan tersimpan selamanya. Kana dan MC merasa hangat, senang, dan bahagia. Tanpa sadar event untuk hari ini sudah selesai. 

  #MC
  #“Seru banget hari ini Nay! Makasih banyak yaa.”

  #Kana
  #“Hahah, seru banget emang. Makasih juga udah mau nemenin aku, akhirnya aku ada temen yang suka hal-hal gini.“

  #Narrator
  #MC tersenyum mendengar perkataan Kana

  #MC
  #“Aku juga seneng banget, soalnya bareng kamu.”

  #Kana
  #*Blush*

  #MC
  #“Eh ah, kamu pulang naik apa Nay?”

  #Kana
  #“Aku biasanya dijemput sih, soalnya udah malem. Emangnya kenapa?”

  #MC
  #“Ooo enggak. Tadinya mau ngajak bareng, tapi aku juga baru sadar ternyata ini udah malem banget. Jadi mending naik mobil aja biar ga masuk angin.“

  #Kana
  #“Hmmm, nanti deh next time gimana? Soalnya mamah ga ijinin aku naik motor kalau udah malem.”

  #MC
  #“Iya aku ngerti kok Nay. Ya udah ya, kamu hati-hati Nay.“

  #Kana
  #“Iya makasih ya buat hari ini, kamu juga hati-hati.”

  #MC dan Kana pun pergi, MC masih merasa senang dan bahagia karena telah menghabiskan waktu bersama Kana. Apakah ini date? Mungkin iya, atau mungkin hanya MC yang merasa demikian. Meskipun begitu, rasa bahagia dan senang tidak dapat dihilangkan dari hati MC.

  #*SKIP TO SCENE*
  #*BG KOS MALAM*

  #*DING* (NOTIF HP)

  #Setelah beberapa menit, MC datang ke kosnya. HP MC pun berbunyi dan ia melihat adanya notif chat dari Kanaia. 

  #*BG HP (CHATTING APP)

  #Kana
  #“H-halooo…(｡･∀･)ﾉﾞ”

  #MC
  #“Halo juga Nayyy… Kenapa nih?”

  #Kana
  #“Ee-engga kok, cuma mastiin kamu udah pulang aja… Takut nyasar ○( ＾皿＾)っ Hehehe…”

  #MC
  #“Hahaha, ini baru aja selesai beres-beres. Kamu nungguin ya?“

  #Kana
  #“K-kata siapa? Aku ga nungguin kamu kok (￣ε(#￣)”

  #MC
  #“Hahaha, Nay… Kamu emang suka pake emot kayak gitu ya? Sorry kalo tiba-tiba nanya, soalnya aku penasaran. Dari dulu kalo chat kadang pake, kadang engga.“

  #Kana
  #“Ehhh… Sorry ya kebiasaan... Hehe”

  #“A-aneh ya?”

  #MC
  #“Engga lah, ga aneh kok. Malah keliatannya lucu aja. Kalau emang kamu lebih suka pake emot kaya gitu, pake aja lucu juga liatnya.“

  #Kana
  #“Yeeee (≧∇≦)ﾉ”

  #MC
  #“Hahaha, lucu emang“

  #MC dan Kana pun menghabiskan waktu mereka berdua dengan membahas kembali apa yang terjadi hari ini, mulai dari bertemu cosplayer, bermain di booth minigame, bahkan membeli merch-merch yang di jual di booth lainnya. Sampai pada akhirnya mereka tertidur dengan tetap memegang HP masing-masing..


  #*SKIP DAY*
  #*SKIP TO SCENE*
  #*BG KELAS*

  #Hari dimulai seperti biasanya, MC memasuki kelas dengan keadaan hampir terlambat. Saat mencari tempat kosong, Freya menyuruh MC untuk duduk di sampingnya. Karena waktu menunjukan bahwa kelas akan dimulai, tanpa pikir panjang MC pun duduk di sebelah Freya.

  #MC
  #“Psstt, Fre… Naya ke mana dah?”

  #Freya
  #“Lah baru aja mau nanyain ke kamu, emang dia ngabarin?”

  #MC
  #“Nggak. Terakhir chat tuh waktu malem, abis itu aku ketiduran deh. Ini aja kan hampir telat, emang ke kamu ga ada kabar gitu?”

  #Freya
  #“Ga ada sama sekali, kalian emang sampe jam berapa?”

  #MC
  #“Ga tau aku lupa, seingetku pas jam 1 an masih sadar kayaknya.“

  #Freya
  #“Wahhh udah jelas ini mah, dia kesiangan. Haduhhh.”

  #Dosen
  #“Teman-teman, mohon untuk beberapa menit kedepan perhatikan pelajaran dulu ya. Ini sangatlah penting, untuk kedepannya bapak tidak ingin kalian ketahuan mengobrol. Terima kasih banyak, jadi untuk memahami bahwa…”


  #Dosen
  #“Baik. Pelajaran hari ini sudah selesai. Sampai bertemu di pertemuan selanjutnya.”
  #Setelah dosen meninggalkan ruangan, kelas pun berakhir. Tiba-tiba HP Freya berbunyi cukup keras sehingga membuat hampir seluruh kelas melihat ke arahnya.
  #*KRINGG*
  #*BG KELAS*

  #Freya 
  #“Aduhh maaf ya semuanya. Lupa ga disilent tadi, hehe.“

  #Transisi BlackScreen bentar
  #SFX Angkat Telepon
  #“Apaan?”

  #“Oo ini udah selesai. Kamu telat shi, ya udah gimana lagi. Ga ada yang mintain izin ke dosen, orang ga ada kabar…”

  #“Ya udah, dadah.”

  #MC
  #“Itu tadi Naya?”

  #Freya 
  #“Iya katanya dia ketiduran, hadeuhh. Ya udah lah gimana lagi. Btw kamu udah siapin kado belum buat Naya? Kan dia 4 hari lagi ultah.“

  #MC
  #“HAAAA!???”

  #MC menjawab dengan suara yang cukup keras, hingga terdengar hingga ke ujung kelas dan membuat mahasiswa/i yang masih ada di dalam kelas terkejut.

  #Freya 
  #“Biasa aja napa sih, ya udah deh kamu siapin hadiahnya yang bener ya. Awas aja kalau ga ngasih hadiah! Oke, aku duluan ya. Ada janji sama yang lain, dahhh.“

  #Karena hari ini hanya ada satu kelas, MC memilih untuk menghabiskan waktunya di kosan dan memikirkan apa yang cocok sebagai kado ulang tahun untuk Kana.

  #*SKIP TO SCENE*
  #*BG KOS SIANG*

  #MC
  #“Aduuhhh aku ngasih apa ya buat Kana? Kalau diinget-inget lagi, Kana tuh suka sama jejepangan. Tapi masa aku ngasih Naya merch anime? Aku ga pernah liat dia pake pakaian anime-anime gitu sihh. Kalau official CD anime atau band? Tapi aku ga tau dia suka band apaan, aaaa bingung banget mau ngasih apa.“

  #Seakan sedang terjadi perang di dalam pikiran MC, tanpa terasa waktu berubah menjadi malam. MC hanya bisa kebingungan memilih kado ulang tahun apa yang cocok agar Kana bisa terus mengingat dirinya. Tiba-tiba HP MC berbunyi yang menunjukkan bahwa baterai HPnya sudah sedikit dan perlu di-charge, akan tetapi ternyata ada notif lain dari Kana dan Freya yang mencoba menghubunginya beberapa kali.

  #*SKIP TO SCENE*
  #*BG KOS MALAM*
  #*CHATTING APP*

  #MC
  #“Eh maaf, tadi aku ketiduran hehe.”

  #Beberapa saat kemudian Kana dan Freya  pun menelepon MC.
  #*BG HP LAGI TELEPON*

  #Freya
  #“Nahhh kan kalau gini enak, ga usah ngehubungin satu-satu.”

  #MC
  #“Ah Naya, maaf ya tadi aku ketiduran.“

  #Kana
  #“Iya gapapa. Tadi juga aku terlalu spam, maaf ya.“

  #MC
  #“Enggak apa-apa,  aku ga sempet liat semua chatnyaa. Sorry. “

  #Freya
  #“Jadi tadi kenapa Nay?“

  #Kana
  #“Harus aku yang ngejelasin?”

  #MC
  #“Ya udah, sini deh aku yang jelasin.“

  #Freya 
  #“Lah, emang tau ada apa?”

  #MC
  #“Ya nggak lah, makanya cepet jelasin.“

  #Kana & Freya
  #“Hahahaha.”
  #Kana
  #“Oke, jadi TLDR aja nih ya. Lusa tuh bakalan ada event di cafe mall yang udah aku tungguin banget dari beberapa bulan yang lalu.“
  #“Nah di eventnya tuh, bakalan ada cake yang dijual. Sumpah itu enak banget cakenya.”
  #“Terus, yang bikin aku pengen banget tuh cakenya limited edition gitu, jadi aku bisa jamin kalau cakenya itu bakalan ENAKKKKK BANGETTT.”
  #“Aku jamin itu bakalan enak banget. Kalau ga enak, nanti aku traktir makan di all you can eat deh.“
  #“Nahhhh tapi yang jadi masalahnya tuh, di event itu satu orang cuma bisa beli satu buah cake aja. Jadi nanti aku pengen ajak Freya sama kamu buat antri dan beli juga. Nanti uangnya dari aku kok, santai aja. Tapi nanti ikut antri biar bisa beli juga.“

  #Freya
  #“Kayaknya itu kepanjangan deh buat TLDR, Nay.”

  #MC
  #“Keknya TLDR mu itu “To Long Di Read”, makanya kamu telepon ya.”

  #Kana
  #“Hehehe, maaf terlalu semangat.”
  #MC
  #“Tapi oke, intinya lusa kan?”
  #Kana
  #“Iya lusa.“

  #MC
  #“Oke aku bisa kok.”
  #Freya
  #“Yaudah nanti kabarin lagi yaa. Aku mau tidur dulu.”
  #Kana
  #“Okeee, good night minna~”
  #MC
  #“Oke, good night.”
  #*BG HP LAGI TELEPON SELESAI*
  #MC
  #“Oke nanti aku harus liat-liat sekalian milih hadiah apa yang kayaknya cocok buat Naya di mall.“
  #Transisi Ganti Hari

  #*SKIP TO SCENE*
  #*BG MALL*
  #Lusa Kana, Freya, serta MC pergi ke mall untuk membeli limited cake. Tanpa kana dan freya sadari, mc memiliki niat terselubung dimulai dari masuk mall mc sesekali melihat gerak gerik kana mulai dari apa yang dia katakan dan toko apa yang ia lihat pun menurutnya petunjuk apa yang ia inginya untuk pada hari ulang tahunnya, sempat kana melihat ke toko perhiasan, berbicara tentang sepatunya yang mulai agak sempit, dan sampai bercerita tentang keponakannya yang sering main masak masakan, setelah mendapatkan apa yang kana mau, mc beralasan untuk pergi duluan padahal dia akan membelikan hadiah untuk kana

  #Kana
  #“Aduhh ini Freya ke mana sih? Jangan bilang dia lupa?”
  #,
  #MC
  #“Waduh aku ga tau tuh Nay, coba kamu telepon.“

  #Kana
  #“Oke bentar yaa-”
  #*sfx dering telepon*
  #“Eh?”
  #“FREYAAA!! Kamu ke mana??“
  #“HA!?? Aduhhh… ya udah deh.“
  #“Umm MC, ini Freya katanya ada urusan di kampus, jadinya kita berdua. Kita berduaan nih hehe, kaya waktu itu”

  #MC
  #“Ahahaha, iya nih inget aja kamu. Ya udah yuk jalan.“

  #Kana
  #“Hahaha, okee deh.“

  #Di saat datang ke dalam mall dan berjalan ke arah cafe, Kana sempat beberapa kali curi-curi pandang ke arah beberapa toko yang ada di dalam mall, seperti toko perhiasan, lalu Kana pun sempat bercerita tentang beberapa hal.

  #MC
  #“Eh Nay, tumben kamu ganti sepatu.“

  #Kana
  #“Iya nih. Kemarin pas aku coba udah agak sempit gitu sih, jadi ini pake sepatu yang lain haha.”

  #MC
  #“Ohhh gitu ya, kamu lagi suka apa belakangan ini?”

  #Kana
  #“Heee? Kamu kenapa MC, kok tiba-tiba tanya kayak giniian?”

  #MC
  #“Gak apa apa, daripada -1 topik hahaha.”

  #Kana
  #“Hahaha, iya juga sih. Aku akhir-akhir ini sama sepupuku biasanya main masak-masak gitu sih.”

  #MC
  #“Ohhh gitu ya, eh itu kan cafenya kah?”
  #“Mantep aku dapet beberapa ide kado buat Kana, hehehe.”

  #Kana
  #“Iya, udah ya kita pura-pura ga kenal dulu biar ga dicurigai haha.”

  #MC
  #“Oke dehh.”

  #Setelah membeli cake tersebut, MC dan Kana pun berpisah dan pulang ke tempat tinggal masing-masing. Akan tetapi MC tidak pulang, dia menghabiskan harinya di Mall dan memikirkan harus membeli kado apa untuk Kana.
  #MC.
  #“Hmmm dari obrolan dan kode-kode yang Kana kasih, mending aku beliin apa ya?”

  #*CHOSE*
  #Kalung
  #Sepatu
  #Alat Masak
  #CD FILM HORROR
  #*CHOSE ANYTHING*

  #MC
  #“Oke kayaknya ini cocok deh buat Kana, sekarang waktunya pulang dan siap-siap buat besok pas ulang tahun Kana.“

  #*SKIP TO SCENE*
  #*BG KOS MALAM*

  #Setelah MC sampai di kosan, dia menghubungi Freya untuk membahas rencana ulang tahun Kana.

  #*CHANGE/ADD BG HP*
  #*CHATTING APP*

  #MC
  #“Freya.”

  #Freya
  #“Kenapa?”

  #MC
  #“Ini, mau nanya buat ultah Kana nanti. Kita bakalan gimana nih ngasih suprisenya? Terus mau di mana?”

  #Freya 
  #“Kalau tempat mah udah aman aja. Biasanya aku di rumah Kana sih, nanti kamu dateng aja.“

  #MC
  #“Emangnya boleh ya?”

  #Freya 
  #“Ga ada yang ngelarang kok. Manti ga perlu dekorasi apa-apa, soalnya Si Naya ga suka kalo dirayain gede-gede pake aksesoris gitu. Dulu pernah gitu ,dia malah bete seharian. Lagian dia juga ga pernah inget hari ultahnya.”

  #MC
  #“Oke deh kalau emang gitu, nanti aku tinggal dateng aja ke rumah Kana?”

  #Freya
  #“Iya nanti dateng aja.”

  #MC
  #“Oke. Thanks, Freya.”

  #Freya
  #“Iya sama-sama.“

  #Setelah semua itu, akhirnya MC dan Freya setuju untuk hanya melakukan perayaan yang sederhana saja. Setelah itu MC memutuskan untuk tidur.

  #*SKIP TO SCENE*
  #*KOS SORE*

  #MC
  #“Oke. Hari ini hari yang penting, pokoknya semua harus siap. Bentar cek dulu semuanya, pakaian? Oke. Hadiah? Oke, ada udah di bungkus juga. Wangy? Oke, tadi udah mandi sama pake parfum juga. Tinggal berangkat aja nih harusnya. Duh deg degan banget hari ini, mudah mudahan lancar deh.”

  #*SKIP TO SCENE*
  #*BG RUMAH KANA*

  #MC pun datang ke rumah Kana pada waktu yang telah ditentukan sebelumnya dengan Freya. Tetapi saat MC menghubungi Freya, ia tidak dapat dihubungi. Rasa cemas,gelisah, serta was-was tidak dapat dihapus dari pikiran MC. Mungkin ini pertama kalinya MC berinisiatif merayakan ulang tahun temannya seperti ini, sehingga ingin memberikan momen bahagia yang selalu dapat diingat oleh Kana.

  #MC
  #“Aduhhh masuk ga ya, tapi belum ada Si Freya. Aduhhh tapi kalau di luar terus, nanti takut dicurigai orang-orang. Mending gimana ya…”

  #*CHOSE*
  #PERGI KE DALAM RUMAH
  #TUNGGUIIN FREYA
  #*CHOSE B*
  #MC memilih untuk menunggu Freya. Tak lama kemudian, Freya pun datang dan mereka masuk ke rumah Kana bersama sama.
  #LANJUT KE [NEUTRAL ROUTE 1]

  #BG Ruang Tamu.
  #*CHOSE A*
  #MC pun memutuskan untuk mengetuk pintunya tanpa menunggu Freya dan masuk ke dalam rumah Kana.

  #MC
  #“Siang Nay, maaf telat ya?”

  #Kana
  #“Engga kok sini masuk aja. Freya belum datang, nanti biasanya dia suka telat dikit.”

  #MC
  #“Eh, i-iya Nay, Makasih ya..”

  #Kana 
  #“Mau minum apa MC? Sekalian nunggu Freya nih. Btw kok gugup sih, emang ada apa?”

  #MC
  #“E-engga kok, cuma ini kan pertama kali kita berduaan… J-jadi agak gugup dikit.“

  #Kana
  #“Lah? Bukannya kemarin pas aku sakit, kamu temenin aku ya? Terus kita kan pernah ke cafe bareng, game center bareng, event jejepangan bareng, ke mall kemarin juga kita berduaan. Kamu ga anggep itu kah? Sedih sih, huhuhu.”

  #MC
  #“E-eh maksudnya gak gitu. Cuma entah kenapa hari ini aku lebih gugup aja dari biasanya..”

  #Kana
  #“ Gugup kenapa?”

  #MC
  #“E-ehh itu…”
  #“Aduhh kok aku gugup ya? Apa gara-gara mau ngasih hadiah ke Naya, terus takut dia gak suka ya?”

  #MC
  #“Ya gitu deh, haha. Ini Si Freya ke mana ya, tumben lama.“

  #Kana
  #“Hmmm… Sebenernya kalian mau ngapain deh? Soalnya Si Freya Freya itu gak ngasih tau mau kumpul buat apaan?”

  #MC
  #“ Eh-”
  #“Mampus , harus alesan apa ya biar bisa bohongin Kana?”
  #“Eh itu… Sebenarnya, kita mau…“
  #Sebelum MC sempat menyelesaikan kata katanya, suara Freya terdengar dari arah pintu masuk.

  #Freya
  #“HALOOOO SEMUANYAAA!!!”

  #Kana
  #“Eh Frey, kaget…”

  #MC
  #“Waduh… Freya bikin kaget aja.”
  #[Neutral Route 1]

  #Freya
  #“Halo Naya, udah siap kan?”

  #Kana & MC
  #“Hah, siap?”

  #Freya 
  #“Lahh ini nih, padahal aku dah semangat gini. Dah bawa banyak game-game buat temenin kita sampe malem nih.”

  #Kana
  #“Ha?? Main game?”

  #Freya melihat ke arahku, seakan memberi kode secara tidak langsung. MC mengangguk ke arah Freya.

  #MC
  #“Lah iya Nayy, kamu ga tau? Kita kan bakalan main game lohhh.“

  #Kana
  #“Hmmm… Ya udah, deh aku ngikut aja.“

  #Mereka pun memainkan semua permainan yang dibawa oleh Freya. Tak terasa malam pun tiba, Freya meminta untuk pindah ke kamar Kana, karena tidak mau Mamah Kana merasa terganggu dengan suara mereka.

  #Freya
  #“Eh kita pindah ke kamarmu aja yuk Nay. Ini udah malem, takut ganggu Mamahmu sama tetangga.“

  #Kana
  #“Iya sih, ya udah deh ayo.“

  #*SKIP TO SCENE*
  #*BG KAMAR KANA MALAM*

  #MC
  #“Eh Freya, emang ruangan Naya kedap suara kah? Kok kita pindah ke sini?”

  #Freya
  #“Iya mamahnya Naya masangin peredam suara, biar kalau dia berisik main game gak ganggu tetangga.”

  #Kana
  #“Perasaan ini kamarku, tapi kok kamu yang lebih tahu daripada aku.“

  #MC
  #“Hahaha.”
  #Ini mungkin kali ke tiga MC ke kamar Kana, akan tetapi kali ini ia bisa melihat ruangan kamar Kana dengan lebih seksama. MC melihat ternyata di pojok ruangan kamarnya Kana tersembunyi satu tempat khusus yang dipenuhi kumpulan-kumpulan figur dan merch anime.

  #MC
  #“Wahhhh… Kana ini kan dari anime itu, keren banget kamu punya? Bukannya ini limited-edition ya?”

  #Kana
  #“Iya, hahaha. Ini aku nabung dari lama, untung dapet.“

  #MC
  #“Eh kalau ini dari anime itu kan? Boleh diliat dari deket ga?”

  #Kana
  #“Boleh kok, liat aja. Asal jangan sampai rusak, hahaha.”


  #Freya 
  #“Seneng banget tuh diliat-liat.“

  #MC
  #“Hehe sorry, soalnya ini kesukaanku juga.“

  #Freya
  #“Ya udah kalian have fun dulu ya, aku mau ke toilet dulu bentar.“

  #Setelah mengatakan itu, Freya memberikan kode kepada MC yang langsung mengerti apa yang dimaksud Freya.

  #MC
  #“Eh, Nay. Kalau ini kamu beli dari luar negeri? Setauku di Indo belum ada.“
  #Kana
  #“Ehhh kalo itu sih beli di…”

  #MC pun terus mengobrol dengan Kana, berusaha untuk mengalihkan perhatian Kana. Tak lama kemudian, jam menunjukan 12 malam yang menandakan bahwa hari telah berganti dan hari ulang tahun Kana pun tiba.

  #MC
  #“Nay…”

  #Kana
  #“Iya MC?”

  #MC
  #“Kamu lagi apa?”

  #Kana
  #“Lagi duduk di kasur doang…”
  #“Kamu kenapa sih dari tadi kaya ada yang aneh gitu?“

  #MC
  #“Eh iya maaf, hehe.“
  #“Gugup aja sih.“

  #Kana
  #“Gugup kenapa?”

  #MC
  #“Jadi…sebenernya… Aku ada hadiah buat kamu.“
  #Narator
  #MC mendekati Kana yang sedang duduk di kasurnya.

  #Kana
  #“Hadiah?”

  #MC
  #“Iya, tapi kamu harus tutup mata dulu.“

  #Kana
  #“Hah? Tutup mata?”

  #MC
  #“Iyaa, udah tutup mata dulu sana.“

  #Kana
  #“O-oke.”
  #Kana pun menutup matanya.
  #Kalau di mall pilih:
  #Kalung
  #Sepatu
  #Alat Masak
  #CD FILM HORROR
  #*IF MC CHOOSE B DI MALL*
  #*SFX Suara Kresek*
  #Kana
  #“Udah boleh buka mata belum?”
  #MC
  #“Bentar lagi.”
  #*SFX Suara Kresek*
  #MC
  #“Udah boleh buka matanya Nay.“

  #Kana
  #“ O-okee.“
  #Narrator
  #Perlahan Kana membuka matanya.
  #Asset Sepatu Hadiah ultah Kana
  #Kana terdiam sejenak…
  #Lagi-lagi Kana terdiam…
  #Kana masih terdiam…

  #MC
  #“Nay?”

  #Kana
  #“Eh i-iya makasih banyak ya. Tapi kok kamu tau ukuran sepatu aku, padahal aku ga pernah bilang ke kamu maupun Freya. Kamu tau dari mana?”

  #MC
  #“.....”
  #Kana
  #“MC…?”

  #Kana pun merasa aneh dengan MC, semua kedekatan mereka langsung sirna di hati Kana. Kana langsung kabur sambil memanggil Freya untuk meminta tolong.

  #“ADUHHH BROOO, KOK LU TAU UKURAN SEPATU KANA SIH?? NGERI KALI BROO, LU STALKER YA?”

  #*CHOSE C*
  #*SFX Suara Kresek*
  #Kana
  #“Udah boleh buka mata belum?”
  #MC
  #“Bentar lagi.”
  #*SFX Suara Kresek*
  #MC
  #“Udah boleh buka matanya Nay.“

  #Kana
  #“ O-okee.“
  #Narrator
  #Perlahan Kana membuka matanya.
  #Asset Alat masak Set
  #Raut wajah Kana bingung dan terheran heran, kenapa MC memberikan dia alat masak set lengkap.

  #Kana
  #“Ummm ini apa?

  #MC
  #“Ini kan alat masak Kana, soalnya kamu pernah bilang sepupumu sering datang masak-masakan. Nah aku kasih hadiah buat kamu, siapa tau aku juga bisa cobain masakan kamu hehe.“

  #Kana
  #“Ummm, tapi sepupuku masih TK, jadi dia pake mainan alat masak-masak...”

  #MC
  #“....”
  #Kana
  #“....”
  #“Kana terdiam tanpa kata-kata, hingga Freya datang dan kaget dengan hadiah yang MC berikan. Pandangan Kana dan Freya terhadap MC pun menjadi aneh.

  #“IH BROO, YA KALI AJA NGASIH HADIAH ALAT MASAK KE CEWE YANG TINGGAL SAMA ORTUNYA TERUS MASIH KULIAH, DIKIRA HADIAH ORANG NIKAHAN KALI YA.“
  #*CHOSE D*
  #*SFX Suara Kresek*
  #Kana
  #“Udah boleh buka mata belum?”
  #MC
  #“Bentar lagi.”
  #*SFX Suara Kresek*
  #MC
  #“Udah boleh buka matanya Nay.“

  #Kana
  #“O-okee.“
  #Narrator
  #Perlahan Kana membuka matanya.
  #Asset CD Blu-ray
  #Kana membuka dan melihat bahwa ada CD Blu-ray yang berjudul “The Conjurang” dengan cover yang gelap, mengerikan, dan ada hantunya.

  #MC
  #“Ini film baru loh, katanya viral dan terinspirasi dari kisah nyata. Bisa kali ya kita nonton bareng-bareng nanti, jadi kita nobar gitu konsepnya hahah.”

  #Kana
  #“Tapi… Aku ga suka horror. Ini cuma kesukaan kamu aja, kan?”

  #MC
  #“I-iya sih tapi…”

  #Kana pun meminta maaf dan menolak hadiah dari MC. Dia terlalu takut bahkan untuk menyimpan CD Blu-ray itu.
  #“ADUH BROOO LAIN KALI KALO MAU NGASIH HADIAH TUH HARUS MIKIRIN JUGA APA YANG DIA SUKA, JANGAN LU DOANG YANG SUKA.“

  #*CHOSE A*
  #*SFX Suara Kresek*
  #MC mengambil kalung dan mulai memakaikannya ke leher Kana. Kana pun merasakan ada sensasi dingin di lehernya, curiga akan sesuatu Kana pun bertanya.
  #Kana
  #“E-eh ini apa?”
  #MC
  #“Sabar-sabar. Aman kok, bukan yang aneh-aneh.”
  #Kana
  #“E-eeeeeh.”
  #MC
  #“Udah boleh buka matanya Nay.“

  #Kana
  #“ O-okee.“
  #Narrator
  #Perlahan Kana membuka matanya.
  #Saat Kana membuka matanya, dia terlihat kaget dan terkejut karena di lehernya terdapat sebuah kalung cantik bersinar yang berwarna biru. Ternyata sensasi dingin tersebut merupakan kalung.
  #*SKIP TO SCENE*
  #*CG KANA KALUNG*

  #Kana
  #“EH INI KANN!!??”

  #MC
  #“Selamat ulang tahun~!“

  #Kana
  #“EHH!!!?? K-kamu tau hari ulang tahun ku?”

  #MC
  #“Tau doong. Sekali lagi, selamat ulang tahun Kanaia Asa~“
  #“Bagiku, kamu orang yang spesial. Jadi, aku pengen ngasih hadiah yang spesial juga.”

  #Kana
  #*BLUSH*
  #“M-makasih banyak ya.”

  #MC
  #“Hehe, gimana Nay kamu suka?”

  #Kana
  #“BANGETTTT, aku suka pake banget. Kok kamu tau aku lagi pengen kalung sih?“

  #MC
  #“Kita kan kemarin abis ke mall, terus aku liat kamu merhatiin toko perhiasan gitu. Jadinya aku beli kalung ini sambil bayangin kamu dan aku rasa kalung ini cocok buat kamu.“

  #Kana
  #“Iiiiii makasih banyak yaa, MC“

  #MC
  #“Iya Kana...”

  #Kana
  #“Aduhhh. A-aku ga bisa berhenti senyum, ini bagus bangett.“

  #MC
  #“Bagus deh kalo kamu suka. Aku malah takut kamu ga suka dan jadi benci sama aku.“

  #Kana
  #“Aku suka banget. Lagian ga usah ngasih pun gapapa kok. A-aku ga bakalan bisa benci kamu.
  #MC
  #“Eeeehh.”
  #*Blush*
  #“Ke-kenapa?”
  #Kana
  #“Soalnya…”
  #“.........”
  #MC
  #“.........”
  #Kana
  #“........”
  #*Blush*
  #“MC… Sebenarnya aku suk-”
  #*SFX Pintu Didobrak*

  #Narator
  #Tanpa ada angin dan hujan, tiba-tiba Freya datang membuka pintu kamar Kana.

  #Freya
  #“HAPPY BIRTHDAYYY NAYAAAA~!!!!”

  #Melihat ke arah Kana dan MC yang sedang berduaan dan suasana yang terasa berbeda dari biasanya, membuat Freya pun tersadar.
  #Freya
  #“Eh? Sorry kayaknya ganggu, hehe.”
  #“Kalian lanjutin aja dulu berdua, hehe.”
  #“Hehe, aku pergi dulu baaay~”
  #Kana
  #“F-FREEEEYYAAAAAAA~!”
  #*Blush*
  #MC
  #“Hahahahaha!”

  #Kana
  #“K-kamu jangan ketawa MC!!!”
  #*Blush*

  #MC tertawa dan Kana tersipu malu sambil memandang ke arah MC.
  #Malam itu…
  #Menjadi malam yang tidak akan terlupakan bagi MC dan Kana.
  #*Credits*
  