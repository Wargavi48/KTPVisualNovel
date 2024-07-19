label goodkana:
  #<TRUE ENDING END>
  
  #*CHOOSE*
  #AMBIL FLAYER
  #ABAIKAN FLAYER
  #
  #—---------------------------------------------------IF CHOSE A—----------------------------------------------
  #—-------------------------------------------------GOOD ENDING—-------------------------------------------
  mcname "Hmmm, kayaknya kalau ajak Kana dia mau deh. Ya udah deh, aku ambil aja dulu." 
  #*SKIP TO SCENE*
  #*BG KANTIN*
  mcname "Eh maaf lama ya, tadi abis dari toilet hehe."
  show freya_side at left with dissolve
  freya "Cuci tangan ga?"
  hide freya_side with dissolve
  mcname "Ya cuci lah, masa enggak? Jorok banget ih."
  show kana_side at left with dissolve
  kana "Hahaha, gapapa kita juga baru datang tadi kok."
  hide kana_side with dissolve
  mcname "Eh kalian udah pesen makan? Aku mau pesen bentar ya."
  show kana_side at left with dissolve
  kana "Udah tadi, tapi lama nunggu soalnya ngantri."
  hide kana_side with dissolve
  show freya_side at left with dissolve
  freya "Iya, aku sama Naya udah pesen."
  hide freya_side with dissolve
  mcname "Oke aku pesen dulu ya."
  #*CHOSE*
  menu:
    "Kamu memesan..."
    "Nasi Cumi Pak (donatur)":
      jump goodkanaafterorder

    "Karedok pak/bu (donatur)":
      #*CHOSE B*
      mcname "Karedok kali ya, udah lama ga makan sayuran aku."
      "Ternyata sayuran yang dipake sama tukang dagangnya kebanyakan busuk semua dan hampir setengah mahasiswa/i keracunan dan dilarikan ke rumah sakit."
      scene black with Dissolve(2.0)
      show text "{color=#FFF}ADUH KALO MAU BELI SAYURAN, TANYA TANYA DULU DEH! TAKUTNYA BUSUK, MALAH KAYA GINI SEKARANG{/color}" with Pause(2.0)
      show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
      play music "audio/Dreamcatcher_v2.mp3"
      jump credits

    "Ayam geprek pak (donatur)":
      #*CHOSE C*
      mcname "{i}Hmmm kayaknya makan ayam geprek enak deh, pengen yang pedes sesekali.{/i}"
      "Ternyata ayam yang kamu pesen terlalu pedes dan bikin kamu sakit perut sampe dilarikan ke rumah sakit."
      scene black with Dissolve(2.0)
      show text "{color=#FFF}ADUHHH KASIAN BANGET MASIH MUDA UDAH KE RS GARA GARA SENENG MAKAN PEDES, LAIN KALI JANGAN TERLALU PEDES YA!{/color}" with Pause(2.0)
      show text "{color=#FF0000}{size=+10}BAD END{/size}{/color}" with Pause(1.0)
      play music "audio/Dreamcatcher_v2.mp3"
      jump credits

label goodkanaafterorder:
  #*CHOSE A*
  mcname "{i}Eh nyoba nasi cumi Pak (donatur) kali ya? Katanya terkenal sampe masuk di subtitle gitu di beberapa film, nyobain ah.{/i}"
  "MC pun memesan makanan dan kembali ke meja di mana Kana dan Freya berada."
  mcname "Eh maaf lama, tadi aku jadinya pesan nasi cumi Pak (donatur) itu."
  show kana_side at left with dissolve
  kana "Ooo yang katanya pernah masuk ke film-film itu ya?"
  hide kana_side with dissolve
  show freya_side at left with dissolve
  freya "Ooo aku tau itu, katanya sih enak."
  hide freya_side with dissolve
  mcname "Iya yang itu. Aku nyobain sih, penasaran juga haha."
  show freya_side at left with dissolve
  freya "Eh itu di tasmu ada apaan [mcname]? Kok ada yang nongol sih? Dari tadi mau ambil tapi ga berani soalnya ga sopan gitu kalo ga ijin ke orangnya."
  hide freya_side with dissolve
  mcname "OWH IYA, INI!!!"
  "Dengan nada semangat [mcname] mengambil selembaran yang berada di tasnya."
  mcname "Jadi ini tuh ada rekrutmen buat masuk ke klub jejepangan dan jadi panitia di event gitu."
  mcname "Tadi liat sekilas, tapi aku ambil soalnya kayaknya seru gitu sih."
  show freya_side at left with dissolve
  freya "Oalah, Nay ini mah kesukaanmu tuh."
  hide freya_side with dissolve
  show kana_side at left with dissolve
  kana "Ehh… Ummm keliatannya seru sih… tapi a-aku malu."
  hide kana_side with dissolve
  show freya_side at left with dissolve
  freya "Alahhh, pake malu segala. Ini kesempatan, Nayaaaa. Biar kamu banyak temen jejepangan gitu."
  hide freya_side with dissolve
  mcname "Iya Nay ikut yuk, aku juga ikut."
  show kana_side at left with dissolve
  kana "T-tapiiiiii."
  hide kana_side with dissolve
  mcname "Gini deh, kamu ikut aja dulu. Kalo emang ga suka, nanti keluar aja. Nanti aku yang ngomong deh ke ketuanya, trial and error gitu."  
  show kana_side at left with dissolve
  kana "Emang bisa ya kaya gitu?"
  hide kana_side with dissolve
  show freya_side at left with dissolve
  freya "Udah Nay, ikutan aja duluu."
  hide freya_side with dissolve
  mcname "Iya Nayy, ikutan yaaa."
  show kana_side at left with dissolve
  kana "Ummm i-iya deh aku ikut aja dulu ya. Tapi kalau aku ga suka, aku ga join ya?"
  hide kana_side with dissolve
  mcname "NAHHHH GITU DONG."
  "Tak lama kemudian, makanan pun datang. Mereka bertiga menghabiskan makanan mereka dan membayarnya."
  "Di perjalanan pulang, [mcname] dan Kana membuat janji untuk mengunjungi klub jejepangan tersebut. "
  mcname "Eh Nay, nanti besok ya kita ke klubnya."
  show kana_side at left with dissolve
  kana "Ehhh aku masih belum siap, minggu depan aja deh."
  hide kana_side with dissolve
  mcname "Kelamaan Nay, lagian batas pendaftaran cuma sampai lusa aja. Besok yaa, nanti aku tunggu di depan kampus. Dadahhhh."
  show kana_side at left with dissolve
  kana "Ehhh…"
  hide kana_side with dissolve
  "MC pun pergi pulang ke kosan meninggalkan Kana yang sedikit kebingungan.."
  
  #*SKIP TO SCENE*
  #*KOS (MALAM)*
  
  #*RING RING RING*
  "MC melihat ke arah HPnya yang berbunyi, saat membuka HPnya ia mendapatkan notifikasi chat dari Kana."
  
  show kana_side at left with dissolve
  kana "Eh… B-besok kita reschedule aja gimana ＞﹏＜ "
  hide kana_side with dissolve
  
  mcname "G"
  
  show kana_side at left with dissolve
  kana "Iiiii kok gitu siih ayolah pleaseeeeeee..(✿◕‿◕✿)"
  hide kana_side with dissolve
  
  mcname "Ya udah. Boleh "
  
  show kana_side at left with dissolve
  kana "Yeeee akhirnya jadinya kapan ?"
  hide kana_side with dissolve
  
  mcname "Minggu depan tapi kamu sendirian ya Nay, soalnya aku mau besok."
  
  show kana_side at left with dissolve
  kana "Iiiiihh, tapi kan."
  hide kana_side with dissolve
  
  mcname "Kalo ga mau ikut gapapa kok, ga mau maksa. Kalo mau ikut, aku tunggu sampai jam 3 sore ya… Jangan telat, good night."
  
  show kana_side at left with dissolve
  kana "Ehhh…"
  hide kana_side with dissolve
  "HP [mcname] terus-terusan bersuara, suara notif tidak berhenti terdengar, hingga akhirnya [mcname] pun memilih untuk memasuki mode getar. "
  
  mcname "Hahaha biarin aja lah sesekali biar Kana juga mau. Kata Freya harus digituin dulu biar dia mau."
  
  "Mc pun memilih untuk mengabaikan HPnya dan pergi tidur."
  
  #*SKIP TO SCENE*
  #*BG KAMPUS SIANG MENUJU SORE*
  
  mcname "Hmmmm bentar lagi jam 3, aku tinggal aja kali ya?"
  
  "Saat [mcname] akan pergi, dari kejauhan terdengar suara Kana berteriak."
  
  show kana_side at left with dissolve
  kana "Ehhh tungguuuuuu!!!! [mcname] TUNGGUUUU!!!"
  hide kana_side with dissolve
  
  mcname "Nahhh datang juga."
  
  show kana_side at left with dissolve
  kana "Ihh kamu kenapa sih ga bales chat aku? Sengaja ya bikin aku marah?"
  hide kana_side with dissolve
  
  mcname "Hahah, soalnya kata Freya kamu harus digituin sih biar mau, makanya aku diemin kamu dulu "
  
  show kana_side at left with dissolve
  kana "Iiii, kamu mah…"
  hide kana_side with dissolve
  
  
  #MC dan Kana pun pergi ke arah dimana klub jejepangan berada..
  mcname "Kamu siap kan, Nay?"
  
  show kana_side at left with dissolve
  kana "Bentar bentar, aku mau narik nafas dulu…"
  hide kana_side with dissolve
  #MC melihat ke arah Kana yang sedang mempersiapkan dirinya untuk melanjutkan masuk ke arah ruangan jejepangan, ia pun melihat tangannya yang sedang membuat kata kanji orang di telapak tangannya.
  
  mcname "Haaaaa… Segugup apa deh dia… "
  #“Ahhh lama Nay ayooooo.”
  
  #Tak sabar dengan Kana, [mcname] pun memaksa Kana untuk segera masuk ke ruangan klub jejepangan. Saat mendekati ruangan, terdengar suara yang cukup ramai.
  
  #???( TONO )
  #“ Woyyy lu mau kemana kocakkkk! “
  
  #???( PIA )
  #“ Ahahaha! ”
  
  show kana_side at left with dissolve
  kana "K-kelihatannya rame banget ya MC, kita pulang aja yuk? Lain kali aja "
  hide kana_side with dissolve
  
  mcname "Udah lah namanya juga klub, yuk masuk… Permisiii~"
  
  #MC pun masuk ke arah ruangan klub. Kana panik dan mencoba untuk menghentikan MC, akan tetapi [mcname] telah memasuki ruangan terlebih dahulu. Suasa ruangan tiba-tiba hening, akan tetapi terlihat wajah yang agak familiar di sana. 
  
  #??(TONO)
  #“ Eeehhh elo!??”
  
  mcname "Eeeh?"
  
  #Tono langsung pergi ke arah belakang MC, di mana Kana bersembunyi.
  #???(TONO)
  #“ Elu kan yang waktu itu menghindar ya? Akhirnya dateng juga, udah gue tunggiin loh.“
  
  show kana_side at left with dissolve
  kana "Eeehh… I-iya hehe. "
  hide kana_side with dissolve
  
  mcname "Nay, santai aja napa… "
  
  #???(PIA)
  #“ Ton, dia siapa ?”
  
  tono "Ooohhh Pii. Ini loh yang waktu itu aku ceritain yang suka nge chant sama wotagei itu loh, ini orangnya. “"
  
  show pia_side at left with dissolve
  pia "Oohhh ini toh. ”"
  hide pia_side with dissolve
  
  mcname "Eeehh ummm sorry, ini klub jejepangan kan?"
  #
  tono "Iya kok kalian ga salah masuk, lo kan yang waktu itu di depan kampus ya?”"
  
  mcname "Iya namaku MC, salam kenal ya. "
  
  #MC melihat ke arah Pia. Sosoknya yang enerjik, kecil serta lucu membuatnya teringat dengan kucing di rumahnya…
  show pia_side at left with dissolve
  pia "Btw kenalin namaku Pia Meraleo.”"
  hide pia_side with dissolve
  
  tono "Owh iya sampe lupa haha, kenalin juga gue Tana Nona. Salam kenal ya guys. “"
  
  show pia_side at left with dissolve
  pia "Panggil dia Tono aja ya, hahaha. “"
  hide pia_side with dissolve
  
  tono "Apaan sih kocak, main ganti nama gitu. Lama-lama gue laporin lu pencemaran nama baik. “"
  
  show pia_side at left with dissolve
  pia "Ahahahaha, emang berani? Eh btw kamu siapa namanya? “"
  hide pia_side with dissolve
  
  show kana_side at left with dissolve
  kana "Eeehh… Uumm aku Kana. "
  hide kana_side with dissolve
  
  mcname "Maaf ya dia gugup, Nay ayoo lah. "
  
  show kana_side at left with dissolve
  kana "T-tapii.."
  hide kana_side with dissolve
  
  show pia_side at left with dissolve
  pia "Eh kamu masuk jurusan apaan?”"
  hide pia_side with dissolve
  
  show kana_side at left with dissolve
  kana "A-aku masuk ke jurusan HI. "
  hide kana_side with dissolve
  
  tono "Wihhh anak HI. aku masuk pertanian, kalau yang pendek satu ini masuk ke DKV.”"
  
  show pia_side at left with dissolve
  pia "AKU GA PENDEK!! ” "
  hide pia_side with dissolve
  #Pia menjawab dengan nada dan ekspresi marah, membuatnya terlihat semakin lucu. [mcname] hanya tertawa melihat mereka bertengkar satu sama lain.
  
  #
  tono "Jadi kalian ke sini abis liat flyer itu kan? Kalian mau masuk kan ke klub ini? Mau bantu juga di event nanti yang akan datang kan?”"
  
  show pia_side at left with dissolve
  pia "Santai napa? Kasian tuh langsung dikasih pertanyaan gitu. “"
  hide pia_side with dissolve
  
  mcname "Kalau aku iya haha, tapi kalau Kana.."
  
  #MC melihat ke arah Kana diikuti oleh Tana dan Pia 
  
  show kana_side at left with dissolve
  kana "A-aku mau liat-liat dulu kalo boleh. "
  hide kana_side with dissolve
  
  show pia_side at left with dissolve
  pia "Boleh kok, boleh pake bangettt. Kamu liat-liat aja juga gapapa kok, apalagi nanti kalau di akhir-akhir ikutan join. Soalnya kita juga lagi perlu satu orang lagi nih dan kayaknya kamu cocok deh.”"
  hide pia_side with dissolve
  
  show kana_side at left with dissolve
  kana "Kurang satu orang ?"
  hide kana_side with dissolve
  
  show pia_side at left with dissolve
  pia "Iya kurang satu lagi buat iku-”"
  hide pia_side with dissolve
  
  #Mungkin karena Tana tau betapa malunya Kana untuk menunjukkan sifat wibunya, tanpa membiarkan Pia menyelesaikan kalimatnya, Tana memotong omongan Pia.
  tono "Buat ikut panitia ya… hahaha buat ikut panitia event nanti, iya kan Pia? Hahaha.  “"
  #
  #
  show pia_side at left with dissolve
  pia "Eh? I-iya."
  hide pia_side with dissolve
  
  tono "Iya jadi ada event jejepangan yang bakalan diadain sama kampus dan kerja sama dengan pihak-pihak lain juga, makanya kita lagi lumayan sibuk nyari panitia sama tenaga tambahan. Kalian mau ikut kan?”"
  
  mcname "Waahhhhh, iya iya aku mau ikut. Nay ayo ikut bantu-bantu dikit aja biar tau, seru loh ikut kaya gini tuh. "
  
  show pia_side at left with dissolve
  pia "Iya kalo mau bantu gapapa kok, ga bakalan dimarahin atau diapain kok tenang aja. “"
  hide pia_side with dissolve
  show kana_side at left with dissolve
  kana "Ummm, aku mikir-mikir dulu deh ya…."
  hide kana_side with dissolve
  
  tono "Ayolah brooo, gue tau kalau lu tuh suka jejepangan. Dijamin deh ga bakalan nyesel, kalau nyesel nanti Pia traktir buat beli merch di event itu deh gimana ?”"
  
  show pia_side at left with dissolve
  pia "Kok jadi gue sihhh, Ton. “"
  hide pia_side with dissolve
  
  tono "Ahahaha!”"
  
  mcname "EH GAS KALI YA "
  
  show kana_side at left with dissolve
  kana "Hahaha"
  hide kana_side with dissolve
  
  tono "Nahhhh gitu dong ketawa santai aja dong. Kita kan ga gigit kecuali Si Pia Meraleo itu tuh ati-ati aja, ada LEOnya soalnya xixixi.”"
  
  show pia_side at left with dissolve
  pia "Ton… Lawakan lu kayak bapak-bapak dah, ga lucu.”"
  hide pia_side with dissolve
  
  tono "Hargain napa, udah susah-susah gue bikin jokes.”"
  
  show kana_side at left with dissolve
  kana "Mau berapa? Harganya 2 ribu cukup ga ya, hehe."
  hide kana_side with dissolve
  
  mcname "Tumben lu bales ngejokes, Nay?"
  
  show kana_side at left with dissolve
  kana "Heheh keliatannya mereka asik sih, hehe."
  hide kana_side with dissolve
  
  tono "Asik lahhhh, pake bangetttt. “"
  
  show pia_side at left with dissolve
  pia "Iya dong siapa dulu, gueee gitu loh. “"
  hide pia_side with dissolve
  
  mcname "Kita ga diajak nih?"
  
  tono "Iya biarin aja, dia agak freek emang. “"
  
  show kana_side at left with dissolve
  kana "Okee noted dah… Pia orangnya agak freak. "
  hide kana_side with dissolve
  
  show pia_side at left with dissolve
  pia "Ehhhh jangan dong, kok gitu sihhh.”"
  hide pia_side with dissolve
  
  show kana_side at left with dissolve
  kana "hahahaha, iya iya enggak. Santai aja, kalian kan nyuruh aku santai. "
  hide kana_side with dissolve
  
  show pia_side at left with dissolve
  pia "I-iya sih…”"
  hide pia_side with dissolve
  
  #Mereka menghabiskan waktu di sore hari itu dengan berbincang bersama dan mulai mengenal satu sama lain lebih dalam. Ada juga beberapa pembicaraan mengenai event yang akan datang dan apa saja tugas yang akan dilakukan oleh [mcname] dan Kana.
  
  #*SKIP SCENE*
  #*BG KAMAR KOS MALAM*
  
  #HP [mcname] pun berdering dengan terus menerus membuatnya terganggu karena sedang bermain game online. Saat melihat HPnya tersebut, ternyata itu adalah notif dari Kana. [mcname] pun akhirnya membalas chatnya, akan tetapi Kana langsung menelpon MC.
  
  #*CUT TO SCENE*
  #*HP FACE KANA DI HP*
  
  mcname "Kenapa Nay?"
  
  show kana_side at left with dissolve
  kana "Nahhh akhirnya diangkat juga, lagi sibuk kah?"
  hide kana_side with dissolve
  
  mcname "Heheh maaf tadi aku lagi main game, kenapa?"
  
  show kana_side at left with dissolve
  kana "A-aku mau jujur sama kamu boleh? Ini penting banget buat ke depannya. "
  hide kana_side with dissolve
  
  mcname "Waduhhh, kenapa ini kok Si Kana tiba-tiba kaya gini? Aduhhh kok gue gugup gini?"
  #“I-iya Nay, kenapa tumben kok jadi serius gini.“
  
  show kana_side at left with dissolve
  kana "Se-sebenernya…"
  hide kana_side with dissolve
  #“ A-akuuu…”
  #“ Aku…tuhhh…pengen…”
  
  mcname "Nay…?"
  
  show kana_side at left with dissolve
  kana "Jadi…aku tuh pengen ikut juga di kepanitian…"
  hide kana_side with dissolve
  #“Fiuuuuhhh, akhirnya bisa juga. Dari tadi aku gugup tau mau ngomong itu, hahaha. Jadi kamu juga ikut kan [mcname]?”
  
  mcname "Oalahh ternyata Kana mau ngomongin itu… Kukira mau ngomong apaan. Aduhhhh aku ke PDan, aaaaaaa~"
  
  show kana_side at left with dissolve
  kana "[mcname] ? Kok diem?"
  hide kana_side with dissolve
  
  mcname "Eh… e-enggak kok. Wahhh tumben kamu mau, alasannya apaan dah Nay?"
  
  show kana_side at left with dissolve
  kana "Soalnya mereka kelihatannya asik gitu, kayaknya aku bisa deket deh sama mereka. Jarang banget aku ngerasain kaya gini sih selain sama Freya.."
  hide kana_side with dissolve
  
  #Kana memelankan suaranya seperti sengaja tidak ingin terdengar oleh MC. 
  #“Sama kamu juga…”
  
  mcname "Hmmm Nay ?"
  
  show kana_side at left with dissolve
  kana "Gapapa kok, pokoknya aku ikut kepanitiaan juga ya. Gitu aja ya, dadah selamat malaamm."
  hide kana_side with dissolve
  
  #Suara telepon pun ditutup, [mcname] terdiam.
  
  mcname "Ahhhhh… Kenapa aku malah deg degan kayak gitu sih, udah lah mendingan tidur. "
  
  #*SKIP TO SCENE*
  #*BG RUANG KLUB*
  
  #Beberapa hari kemudian Kana dan [mcname] pun lolos dalam seleksi kepanitian dan mereka datang ke ruangan klub untuk rapat. Di sana ada Tana dan Pia yang sudah menunggu mereka bersama dengan anggota panitia lainnya.
  
  tono "Okee udah datang semuanya nih, mulai aja kali ya?"
  
  #Rapat pun dimulai, rapat kali ini berlangsung cukup lama karena ada beberapa panitia tambahan. Di akhir rapat tersebut pun Pia dan Tana memanggil Kana dan MC. 
  
  tono "Jadi gimana rapat pertama kalian? Seru kan?”"
  
  mcname "Seruu sihh… tapi ga tau nanti pas kerjanya, hahaha."
  
  show pia_side at left with dissolve
  pia "Santai aja nanti kan bareng-bareng, btw Kana aku seneng banget kamu ikut. Soalnya kukira ga bakalan ikut, kenapa tuh tiba-tiba kalo boleh tau?”"
  hide pia_side with dissolve
  
  show kana_side at left with dissolve
  kana "Gapapa hehe, pengen ikut aja soalnya seru pas kemarin sama kalian. "
  hide kana_side with dissolve
  
  tono "Iya lah kita mah asik, kapan kita ga asik ya Pii?”"
  
  show pia_side at left with dissolve
  pia "Kali ini gue setuju sama lu, Ton.“"
  hide pia_side with dissolve
  
  tono "Nahh kan, Pia aja setuju…”"
  #“.........”
  #“Kok kali ini doang sih, Pi? Biasanya nggak, gitu?”
  
  show pia_side at left with dissolve
  pia "Hehehe “"
  hide pia_side with dissolve
  
  tono "Ahhhh elah kocak. “"
  
  mcname "Hahaha. Eh mau tanya dong, ini kan di eventnya pasti ada lomba ya? Panitia panitia boleh ikut lombanya kah?"
  
  tono "Boleh lah, emang lu mau ikutan lomba apaan dah?“"
  
  mcname "Kayaknya pengen ikut lomba cosplay deh, ahaha."
  
  show pia_side at left with dissolve
  pia "Widihhhh semangat aja deh, asal jangan keteteran kerjaan panitianya”"
  hide pia_side with dissolve
  
  mcname "Aman aja."
  
  show pia_side at left with dissolve
  pia "Eh Kana, mending kamu ikut lomba juga yuk, bareng aku sama Tono. “"
  hide pia_side with dissolve
  
  show kana_side at left with dissolve
  kana "HA!!!?? LOMBA!!!???"
  hide kana_side with dissolve
  #Tiba-tiba Kana berteriak dan membuat Tana, Pia, serta [mcname] kaget.
  #“ Engga gak gak. Ga mau dan ga mungkin aku ikut sama lomba, pokoknya enggaaak….”
  
  tono "Aduhhh Piaaa. Kan udah gw bilang, jangan tanya ke Kana langsung. Dia ini maluan orangnya. “"
  
  mcname "Emang lomba apaan ya?"
  
  tono "Lomba idol gituuu. Jadi kan event ini kerja sama dengan idol organisation, terus mereka juga sekalian nyari talent buat direkrut gitu. “"
  
  mcname "Wahhhhh… seru tuh Nay, kamu harus ikutan. Ayooo!"
  
  show kana_side at left with dissolve
  kana "HA!?? IDOL!??? Hahaha ga ga ga, pokoknya ga mau… Malu tau di depan banyak orang tuh. "
  hide kana_side with dissolve
  
  tono "Alah malu malu, waktu itu aja lu dulu di event jejepangan teriak paling kenceng gitu.“"
  
  show kana_side at left with dissolve
  kana "Waktu itu kan beda.. "
  hide kana_side with dissolve
  
  tono "Alaahhh sama aja, beda dari mana? Lu ga sadar ya, kita yang lagi perform sama orang-orang lainnya tuh kadang liat lu gara-gara lu paling semangat diantara para penonton.“"
  
  show pia_side at left with dissolve
  pia "Iya aku juga lihat rekaman dari Si Tono, ada kamu lagi wotagei juga. Udah kamu tuh cocok tau, suara kamu juga kedengeran ademmm banget. Cocok pokoknya, coba dulu yaaaa..’"
  hide pia_side with dissolve
  
  show kana_side at left with dissolve
  kana "Ga ga ga, pokoknya ga mau. "
  hide kana_side with dissolve
  
  tono "Ayolah Kana, ikut yaa cobain dulu deh. Nanti kalo emang ga suka atau ga mau, gapapa. Satu minggu dulu deh, gimana?”"
  
  show kana_side at left with dissolve
  kana "T-tapiii"
  hide kana_side with dissolve
  
  mcname "Ayolah Nayyy, pleaseeeee."
  
  #Baik MC, Pia, serta Tana, memohon dengan sangat… Membuat Kana semakin terdesak.
  #Kana pun mau tidak mau mengiyakan hal itu, akan tetapi dengan beberapa syarat.
  
  show kana_side at left with dissolve
  kana "Aaaaaaa… Iya deh iya, tapi [mcname] harus ikut kapan pun pas latihan. Dan kalo aku ga mau lanjut, aku udahan yaa. "
  hide kana_side with dissolve
  
  #Pia dan tono 
  #“Yessss!!”
  
  #Tana dan Pia merayakan hari itu karena akhirnya mereka bisa mendaftarkan diri mereka ke dalam lomba yang mereka inginkan. Setelah itu Kana, MC, Tana, dan Pia mengerjakan tugas yang telah diberikan oleh ketua panitia.
  
  #*SKIP TO SCENE*
  #*BG KOS MALAM*
  
  #Di saat [mcname] sedang beristirahat, terdengar suara HPnya yang tidak pernah berhenti bergetar sejak ia selesai mandi.
  
  mcname "Aduhhh ini siapa sih, dari tadi notif jebol gini. "
  
  #*CHANGE SCENE*
  #*HP*
  
  tono "Eh ini group buat kita yaa. Buat bahas latihan dan bahas yang lain lain juga lah, biar ga usah ngechat satu-satu.“"
  
  show pia_side at left with dissolve
  pia "Hadeehhh. Lu belum ijin dulu kan ke yang lain, Ton?”"
  hide pia_side with dissolve
  
  tono "Alah ga usah lah, kan temen ini. Ngapain sampe segitunya sih Pii.”"
  
  show pia_side at left with dissolve
  pia "MANNER TON, MANNER, ah elah. “"
  hide pia_side with dissolve
  
  tono "Aaaaaaa….udah lah biar ga ribet juga, @kana & @mc woiii keluar napa? Jangan diem-diem ae “"
  
  show kana_side at left with dissolve
  kana "Hehehe, seru liat kalian berantem. Aku baru selesai beres-beres, ga usah dimarahin napa. "
  hide kana_side with dissolve
  
  mcname "Iya nih, dikira kita ini nolep apa ya, yang sering main HP. "
  
  show pia_side at left with dissolve
  pia "Iya emang gitu Si Tono Tono mah, maklumin yaa. “"
  hide pia_side with dissolve
  
  mcname "Ooooo pantess aja, ya udah lah ya gapapa."
  
  show kana_side at left with dissolve
  kana "Oke deh Pii."
  hide kana_side with dissolve
  
  tono "Aalahhh gue lagi, gue lagi. Gue aja terussss. “"
  
  show pia_side at left with dissolve
  pia "Hahah”"
  hide pia_side with dissolve
  
  mcname "Jadi mau ngapain nih?"
  
  tono "Jadiiii giniii…”"
  #Tana pun menceritakan rencana dia untuk latihan persiapan lomba yang akan datang. Rencananya akan latihan seminggu 3-4x, meliputi latihan dance dan latihan bernyanyi. Tempat latihan akan dikabarin lagi, untuk sementara akan menggunakan ruangan klub untuk latihan terlebih dahulu. 
  
  tono "Jadii gituu sih, gimana? Setuju kan? KAN!!???”"
  
  show pia_side at left with dissolve
  pia "Iya gue sih setuju, kamu gimana Kana?”"
  hide pia_side with dissolve
  
  show kana_side at left with dissolve
  kana "Ummm… Boleh sih, tapi [mcname] juga ikut nemenin kan? Inget perjanjian awal ya, kalau dia ga ikut aku juga enggak. "
  hide kana_side with dissolve
  
  mcname "Iya iya, aku ikut nemenin kok."
  #“Kalo inget, hahahahha.”
  
  show kana_side at left with dissolve
  kana "Iiiiiihhhh"
  hide kana_side with dissolve
  
  tono "Ayolah jangan gitu, please lah bantuin. “"
  
  mcname "Iya iya, nanti aku datang kok. Aman aja. "
  
  show pia_side at left with dissolve
  pia "Nahhh gitu dong. Ya udah ya, nanti ketemuan di ruangan klub ya. “"
  hide pia_side with dissolve
  
  #*SKIP SCENE*
  #*BG RUANG KLUB*
  
  #Sore hari di ruangan klub, semua anggota sudah pulang dan sibuk dengan urusannya masing-masing. Kana, Tana, serta Pia mulai melakukan latihannya ditemani oleh MC. 
  
  #Tana 
  #“ Oookeee siap yaa. “
  
  show pia_side at left with dissolve
  pia "SIAPPP MA BROOOO!”"
  hide pia_side with dissolve
  
  show kana_side at left with dissolve
  kana "...."
  hide kana_side with dissolve
  
  tono "Kana ?”"
  
  mcname "Nayyyy!"
  
  show kana_side at left with dissolve
  kana "Huh ? K-kenapa ya ?"
  hide kana_side with dissolve
  
  mcname "Nay u ok ? Tadi dipanggil sama Tono ga nyaut, kamu gapapa kan?"
  
  show kana_side at left with dissolve
  kana "Gapapa kok cuma gugup aja. Takut gimana kalo nanti aku salah, gimana kalo nanti aku ketinggalan, gimana kalo nanti aku…"
  hide kana_side with dissolve
  
  mcname "NAYA!!..."
  #MC berteriak cukup kencang hingga Pia dan Tana pun terkejut dengan suara [mcname] 
  
  #“ KANAIA ASA, please don't be like that. It’s ok to make mistakes, mistakes happen. Santai aja Nay, mereka ga bakalan salahin kamu kok. Kalaupun mereka berani, bakal kugetok mereka kok. Jadi just be you, ok?”
  
  show kana_side at left with dissolve
  kana "T-tapi…"
  hide kana_side with dissolve
  
  mcname "Ga ada tapi tapian, sekarang kamu coba dulu. Ga usah malu, ga ada siapa-siapa kok di sini."
  
  show pia_side at left with dissolve
  pia "Iya Kana. Kita ga bakalan salahin kamu kok, ga bakalan pernah. Asal kamu tau ya Kana, dulu Si Tono itu pertama kali nyoba nyanyi suaranya aneh bangettt. Sampe satpam dateng katanya dapat laporan ada suara aneh gitu, hahaha.”"
  hide pia_side with dissolve
  
  tono "Iiiiihhhh Piaaaa, katanya janji ga bakalan bilang ke siapa-siapa. Oke kalau gitu dulu juga pas Si Pia Pia itu ngedance beuhhh, jatuh terus brooo. Mana nangis juga, aduhhh dede kecil nangisss.”"
  
  show pia_side at left with dissolve
  pia "Aaaahhh lu juga malah bales ah Ton.“"
  hide pia_side with dissolve
  
  tono "Hehehe 1-1. “"
  
  mcname "See Nay? Ga ada yang langsung bisa, santai aja. Kamu lakuin apa yang kamu bisa, aku dan kita semua pasti dukung, oke? Semangat yuk."
  
  show kana_side at left with dissolve
  kana "O-okeee aku coba ya."
  hide kana_side with dissolve
  
  #Kana akhirnya mau mencoba latihan bersama Tana dan Pia.
  
  tono "Gileeeee, lu keren banget Nayyy bisa ikutin tempo kita. Sumpah stamina lu kuat banget, emang ga sia-sia ya kamu sering ke event. “"
  
  show pia_side at left with dissolve
  pia "Iya loh, aku kagum. Kerja bagus Nay! “"
  hide pia_side with dissolve
  
  mcname "Nay, kamu gapapa? Nih minyum dulu yaa, jangan lupa. You did great, kamu bagus bangett! "
  
  show kana_side at left with dissolve
  kana "M-makasih yaa…"
  hide kana_side with dissolve
  #“ Hehee seru juga ya ternyata, tapi cape bangeeet. “
  
  tono "Hahaha iya lah bro. Gue juga awal-awal serasa mau pingsan, tapi ya sekarang terbiasa. Oke deh, buat hari ini segini aja dulu yaaa. Nanti kita lanjut lagi lah ya, buat selanjutnya kita latihan nyanyi.“"
  
  show pia_side at left with dissolve
  pia "Iya cape bangettt. Ya udah deh, nanti bahas di grup aja yaaa. “"
  hide pia_side with dissolve
  
  #
  show kana_side at left with dissolve
  kana "Iya nih capee banget, tapi makasih yaa buat hari ini. "
  hide kana_side with dissolve
  
  mcname "Makasih juga yaa. "
  
  #Mereka pun pulang ke rumah masing-masing.
  #
  #*SKIP TO SCENE*
  #*BG KOS MALAM*
  #
  #Narator
  #MC mengingat kembali perjuangan Kana saat latihan.
  mcname "Nay… Kamu berjuang banget yaa, mulai terbuka sama orang lain lalu sekarang kamu mau ngedance dan nyanyi… Entah kenapa aku bangga sama kamu."
  
  #*SKIP TO SCENE*
  #*BG RUANG KLUB*
  
  tono "Okeee buat hari ini, kita coba latihan vocal yaa. Piii kasih paham.“"
  
  show pia_side at left with dissolve
  pia "Ah elah, gue kira elu yang bakalan mulai.”"
  hide pia_side with dissolve
  
  tono "Hehe, kan lu lebih jago brokk.”"
  
  show pia_side at left with dissolve
  pia "Ya udah kita coba dulu ya, Kana. Coba deh kamu nyanyi lagu yang paling kamu sukai dulu. Nanti aku coba kasih masukan, boleh kan?"
  hide pia_side with dissolve
  
  show kana_side at left with dissolve
  kana "Boleh aku siap kalau sekarang, tapi jangan terlalu kasar ya ngasih masukannya, hehe. "
  hide kana_side with dissolve
  
  show pia_side at left with dissolve
  pia "Aman aja. “"
  hide pia_side with dissolve
  
  #Kana pun menyanyikan lagu yang ia sukai. Lagunya cukup lama sekitar 4 menit, tetapi bisa dilihat bahwa Kana bernyanyi dengan penuh penghayatan. 
  
  show kana_side at left with dissolve
  kana "Huuuuu, gimana? Huuuuu… Bentar ya aku narik nafas dulu. "
  hide kana_side with dissolve
  
  show pia_side at left with dissolve
  pia "Hmmm… Kana, aku boleh blak blakan ga? “"
  hide pia_side with dissolve
  
  show kana_side at left with dissolve
  kana "Eh k-kenapa ini kok jadi kaya gini?"
  hide kana_side with dissolve
  
  #Kana pun kebingungan. Ia melihat ke arah Tana dan MC, akan tetapi Tana hanya bisa diam 
  
  mcname "Piia?"
  
  show pia_side at left with dissolve
  pia "Bentar ya MC, ini aku sama Kana dulu. Oke Kana, jadi…”"
  hide pia_side with dissolve
  
  #Pia pun mengomentari nyanyian dari Kana. Pia tidak mengatakan bahwa Kana tidak bisa bernyanyi ataupun suaranya jelek, akan tetapi Pia mengomentari tentang teknik vokal yang digunakan Kana dan memberikan petunjuk mengenai teknik vokal yang lebih cocok untuk suara Kana. 
  
  show kana_side at left with dissolve
  kana "...."
  hide kana_side with dissolve
  
  show pia_side at left with dissolve
  pia "Okeee kita coba nyanyi lagu ini bareng ya, kamu tau kan Kana?“"
  hide pia_side with dissolve
  
  show kana_side at left with dissolve
  kana "I-iya aku tau kok, haha."
  hide kana_side with dissolve
  
  mcname "Nay, you okay?"
  
  #MC melihat ke arah Kana yang mukanya terlihat agak pucat, membuat [mcname] sedikit khawatir.
  
  tono "Oke deh, ayoo! “"
  
  #Saat bernyanyi bersama, sempat beberapa kali Kana terdiam sehingga mereka bertiga menyanyikan lagunya dari awal lagi…
  
  show kana_side at left with dissolve
  kana "E-eh maaf ya, aku salah terus. "
  hide kana_side with dissolve
  
  tono "Santai aja Kana, ga salah kok. Kamu udah bagus kok. “"
  
  show pia_side at left with dissolve
  pia "Iya Kana, santai aja. Ini pertama juga, you did good. “"
  hide pia_side with dissolve
  
  mcname "Iya kok Nay. Meski aku ga terlalu tau soal vocal, tapi suara kamu enak didenger kok. "
  
  show kana_side at left with dissolve
  kana "Makasih ya, haha."
  hide kana_side with dissolve
  #“……….”
  #“Eh maaf ini aku ditelpon sama orang rumah, aku izin angkat dulu ya. “
  
  #*Black Screen
  
  mcname "Eh… Piii"
  
  show pia_side at left with dissolve
  pia "Hmmm kenapa?”"
  hide pia_side with dissolve
  
  mcname "Ummm… gapapa deh, lupakan aja. "
  
  #Pia 
  #‘“ Ya udah kalau gitu. “
  
  #Tiba-tiba Tana menarik lengan mc, seakan ingin berbicara dengannya secara personal 
  
  tono "Eh MC, maaf ya kalau Si Pia agak gimana gitu komennya. Soalnya ke gue juga lebih parah, tapi habis itu vocal gue improve bangettt. “"
  
  mcname "Kok minta maafnya ke gue, kan Kana yang kena komen. "
  
  tono "Soalnya lu kan yang lebih deket, nanti sampai ya. “"
  
  show kana_side at left with dissolve
  kana "Eh temen-temen, maaf ya. Tadi ada telepon, kayaknya aku harus pulang duluan deh. Maaf banget yaa. "
  hide kana_side with dissolve
  
  show pia_side at left with dissolve
  pia "Eeh gapapa kok Kana, ini juga kayaknya udahan aja dulu deh. “"
  hide pia_side with dissolve
  
  tono "Iya ini juga udah aja dulu. “"
  
  #Di perjalanan pulang, [mcname] memikirkan Kana. Ia tampak agak berbeda dari biasanya, seakan ada yang membuat dia gelisah. Tetapi yang ada di pikiran mc hanya mimik muka Kana sesaat setelah diberi komentar oleh Pia…
  
  mcname "Oke dehh, nanti aku tanya Si Kana aja. "
  
  #*SKIP TO SCENE* 
  #*BG KOS MALAM*
  
  mcname "Hmmm, enaknya gimana ya mulainya?"
  
  #*INSERT HP*
  mcname "Malam Nayy.."
  
  #Setelah kurang lebih 10 menit, akhirnya muncul notif pesan dari Kana.
  
  show kana_side at left with dissolve
  kana "I-iya kenapa ?"
  hide kana_side with dissolve
  
  mcname "Gimana kabarnya, hari ini ngapain aja haha."
  
  show kana_side at left with dissolve
  kana "Template amat pertanyaannya. "
  hide kana_side with dissolve
  
  mcname "Hahaha"
  
  show kana_side at left with dissolve
  kana "Kenapa? "
  hide kana_side with dissolve
  
  mcname "Uummm sebenernya.. "
  #“ Tadi kok kamu agak gimana gitu pas latihan..”
  
  show kana_side at left with dissolve
  kana "Ga ada apa-apa kok…"
  hide kana_side with dissolve
  
  mcname "Nay meski kita baru deket, tapi aku tau kalau kamu bohong… Waktu bilang ada telepon juga kamu bohong kan? Kenapa Naya, ada apa?"
  
  show kana_side at left with dissolve
  kana "Uummmm nanti besok kita ketemuan aja, gimana? Aku ga mau jelasin hal ini di chat."
  hide kana_side with dissolve
  
  mcname "Ookee, nanti kita besok ketemuan di "
  
  #*CHOSE*
  #Cafe
  #Warteg
  #Rumah Kana
  #*IF CHOSE*
  #A
  mcname "Gimana kalau di cafe Nay ? Cafe yang sering kita kunjungi itu loh. "
  
  show kana_side at left with dissolve
  kana "Uummm aku takut ada orang lain yang denger, aku malu…"
  hide kana_side with dissolve
  
  #“COBA LAGI YA BROK, KURANG BERUNTUNG LUH”
  
  #*IF CHOSE*
  #B
  mcname "Warteg gimana Nay??? Sekalian makan siang gitu, hehe. "
  
  show kana_side at left with dissolve
  kana "Yang bener aja…. Aku kan ngajaknya ngobrol, bukan makan. Bodo ah "
  hide kana_side with dissolve
  
  #“ADUHHH BROOOO BROOO, COBA LAGI DEH TINGGAL SATU PILIHAN TUH”
  
  #*IF CHOSE*
  #C
  mcname "Kalo di rumah gimana Nay? Aku sebenernya bebas sih mau di mana aja, yang penting kamu nyaman."
  
  show kana_side at left with dissolve
  kana "Boleh deh, nanti di rumah aku aja ya. Jam 12 siang gimana?"
  hide kana_side with dissolve
  
  mcname "Okee Nay.."
  #“Hmmm ini pasti ada hubungannya sama latihan tadi, fix siiih…”
  
  #*SKIP TO SCENE*
  #*BG RUMAH KANA*
  
  #MC pun mendatangi rumah Kana tepat jam 12. Merasa hal ini adalah sesuatu yang penting, [mcname] tidak ingin membuat Kana kecewa karena telat.
  
  show kana_side at left with dissolve
  kana "Eh, masuk aja "
  hide kana_side with dissolve
  
  mcname "Ohh iya…"
  
  #Terdapat ketenangan sejenak di antara Kana dan MC. Kana yang merasa takut untuk bercerita dan [mcname] yang ingin bertanya tapi merasa tidak enak, membuat keduanya tidak dapat memulai pembicaraan. Sampai pada akhirnya…
  
  mcname "Nay… Jadi sebenernya ada apa. "
  
  show kana_side at left with dissolve
  kana "Sebenernya…."
  hide kana_side with dissolve
  #“ Kamu inget ga, pas kita latihan kemarin itu?”
  
  mcname "Inget, latihan vokal kan?"
  
  show kana_side at left with dissolve
  kana "Iya latihan vokal itu. Setelah denger masukan dari Pia dan latihan bareng, aku ngerasa ketinggalan banget masalah tekniknya. Bahkan Pia aja sampe ngajarin aku teknik-teknik vokal gitu, aku malu maluin ya…"
  hide kana_side with dissolve
  
  #Kana mengatakan hal tersebut dengan wajahnya yang sedih, melihat ke arah [mcname] seakan ada air mata yang akan keluar dari matanya Kana
  
  #“ Pas liat rekaman dance juga aku merasa masih banyak ketinggalan temponya. Emang sih kalo stamina aku bisa imbangin yang lain, tapi tempo, ketukan, dan lainnya, aku telat semua haha. Apa Tono sama Pia muji aku cuma supaya aku tetep mau sama mereka ya, padahal aslinya aku tuh kaya beban...”
  
  #MC hanya diam saja, ia tidak ingin menyela cerita dari Kana 
  
  #“ Kayaknya aku mending udahan aja deh, lagian aku kan ga berbakat nyanyi atau dance gitu. Tana punya dance, Pia punya vokal, kalau aku ga punya apa-apa.“
  
  mcname "Udah Nay ?"
  
  show kana_side at left with dissolve
  kana "Maksudnya udah?"
  hide kana_side with dissolve
  
  mcname "Udah ngerendahin diri kamu sendiri? Okee ini sekarang pandanganku ya, ga boleh nyela."
  #“INGET, GA BOLEH NYELA.
  #“ Ok?”
  
  #Kana
  #‘O-oke.”
  
  mcname "Dancemu off tempo… off ketukan… emang kenapa Nay? Emang mereka komen soal itu? Enggak, kan? Ini pertama kalinya dance buat kamu kan? Dan mereka aja muji kamu, Naya, ga usah berkecil hati. Soal vokal, kalo kamu mau tau, Si Tana sampe minta tolong buat sampein permintaan maaf ke kamu. Dia bilang kalo Si Pia emang ngajarinnya kaya gitu, tapi niat dia kan baik. Buktinya kamu sekarang tau teknik vokal lainnya."
  
  #Kana yang hanya bisa terdiam menundukan kepalanya.
  
  #“ Yang lebih penting dari semua itu ada kamu, Kanaia Asa. Apa kamu seneng belajar bareng dan temenan sama mereka?”
  
  #Kana tetap terdiam beberapa menit 
  
  mcname "Sekali lagi Kanaia asa, kamu seneng ga sama mereka?"
  
  show kana_side at left with dissolve
  kana "....."
  hide kana_side with dissolve
  #“A-a-aku seneng…. Aku seneng bisa ketemu sama mereka, latihan sama mereka, dan pengen terus sama mereka.
  #Tapi… aku takut jadi beban..”
  
  mcname "Yang bilang kamu beban siapa? Kan ga ada, apa mau aku tanya langsung ke mereka?"
  
  show kana_side at left with dissolve
  kana "J-jangan! Jangan tanya ke mereka, nanti aku makin maluuu."
  hide kana_side with dissolve
  
  mcname "Ya udah, ga usah mikir kaya gitu lagi ya. Kamu udah berjuang kok, jadi kamu harus bangga. Oke?"
  
  show kana_side at left with dissolve
  kana "I-i’ll try… "
  hide kana_side with dissolve
  
  mcname "Good, jadi sekarang mau ngapain lagi?"
  
  show kana_side at left with dissolve
  kana "Hahaha. Iya juga ya, ngapain lagi ya?"
  hide kana_side with dissolve
  
  mcname "Gimana kalo kamu coba teknik vokal yang diajarin Pia waktu itu, sama dance dikit-dikit. Gimana?"
  
  show kana_side at left with dissolve
  kana "Umm boleh sih… tapi jangan ketawain aku kalo salah langkah atau bahkan sampe jatoh, ya."
  hide kana_side with dissolve
  
  mcname "Engga kok, aku janji. "
  #Setelah itu Kana pun melatih dirinya untuk bisa lebih baik lagi sambil ditemani [mcname] yang selalu ada untuk mendukungnya. Kana cukup semangat untuk latihan pribadi kali ini. Tak terasa hari sudah mulai gelap.
  
  mcname "Nay, keknya aku pulang dulu ya. Udah malem ini, ga kerasa emang kalau lagi asik-asik tuh."
  
  show kana_side at left with dissolve
  kana "Eeh iya astaga, udah jam segini. Makasih ya, udah mau dengerin dan temenin aku. "
  hide kana_side with dissolve
  
  mcname "Iya sama-sama, see you Nay."
  
  show kana_side at left with dissolve
  kana "See youu~"
  hide kana_side with dissolve
  
  #MC pun pergi dari rumah Kana. Di perjalanan ia memikirkan Kana yang terkadang masih memiliki negatif thinking, dan saat itu juga ia berjanji 
  mcname "Okeee, pokoknya aku harus bisa dukung Kana sampe perlombaan! Jangan sampe kana punya pikiran negatif lagi!"
  
  #*SKIP TO SCENE*
  #*BG RUANG KLUB*
  
  #Hari baru dimulai, para anggota dan panitia pun cukup sibuk dengan persiapan yang dibutuhkan.
  
  show pia_side at left with dissolve
  pia "Kana… maaf ya kemaren kalo masukan atau komen aku ada yang bikin kamu sakit hati. Kemaren aku juga udah dimarahin sama Tono, maaf ya. “"
  hide pia_side with dissolve
  
  tono "Iya kana, maafin Pia yaa. Dia ga ada maksud jelek jelekin kamu, sumpah dah. Maafin ya…”"
  
  show kana_side at left with dissolve
  kana "Gapapa kok, aku tau kalo itu masukan yang bikin aku improve. Makasih ya masukannya, aku ga marah kok aman aja. Next time kalau emang ada masukan bilang aja langsung ya, ga usah ragu-ragu lagi. Btw panggil aku Nay aja."
  hide kana_side with dissolve
  
  show pia_side at left with dissolve
  pia "Yeeeeeee, ku kira kamu marah. Makasih ya Naaayyyy.”"
  hide pia_side with dissolve
  
  tono "Oke deh Nay. Btw kita latihan di mana ya? Di ruangan klub kayaknya ga bisa deh, soalnya pada penuh gitu.“"
  
  #Padangan dari ketiganya mengarah ke MC, seakan meminta [mcname] untuk memberikan tempat yang cocok untuk latihan.
  
  mcname "Ummm gimana kalau di… "
  
  #*CHOOSE*
  #ROOFTOP
  #TANAH KOSONG DI UJUG KAMPUS
  #DIBAWAH POHON 
  
  #*IF CHOOSE B*
  
  tono "Lu serius brok, di sini?”"
  
  mcname "Emang kenapa, Ton?"
  
  show pia_side at left with dissolve
  pia "Eh kok aku ngerasa gimana ya sama hawanya. “"
  hide pia_side with dissolve
  
  show kana_side at left with dissolve
  kana "MC, serius kan di sini ?"
  hide kana_side with dissolve
  
  mcname "Iya soalnya kan Kana masih belum terbiasa tampil gitu, terus kalian pengen di tempat kosong kan? Aku denger tempat ini dari temen-temen gitu sih, gimana? "
  
  tono "Broo sebenarnya ini tempat apaan dah, jujur hawanya ga enak. Kita pindah aja yuk, sumpah dah mending ga latihan sekalian gw mah daripada di sini. “"
  
  show pia_side at left with dissolve
  pia "Gue setuju sama Tono sih buat kali ini.”"
  hide pia_side with dissolve
  
  show kana_side at left with dissolve
  kana "He..he…hehehehe…ahahahahhaha"
  hide kana_side with dissolve
  
  mcname "Nay? Kamu kenapa Nay?"
  
  show kana_side at left with dissolve
  kana "Ahahahahhaha"
  hide kana_side with dissolve
  #“AHAHAHAHAHAHAHAH!”
  
  tono "TUH KAN! GW BILANG APA!”"
  
  #“TERNYATA TEMPAT ITU SALAH SATU TEMPAT YANG KATANYA ANGKER DI KAMPUS LU, KANA MALAH KESURUPAN TUH BROK. “
  
  #*IF CHOOSE C*
  
  mcname "Nahhh ini luas nih, adem juga kan?"
  
  tono "Wiiihh iya nih adem, bisa juga lu nyari tempat.”"
  
  show kana_side at left with dissolve
  kana "Oke juga pilihanmu, MC."
  hide kana_side with dissolve
  
  show pia_side at left with dissolve
  pia "Ya udah, yuk latihan. “"
  hide pia_side with dissolve
  
  #Tak lama saat latihan tiba-tiba terdengar suara yang keras, membuat mereka panik. Ternyata salah satu dahan pohon di tempat itu patah dan jatuh menimpa Kana. Kana pun terluka dan akhirnya harus dilarikan ke rumah sakit.
  
  #“ADUH BROOOO ATI ATI DAH JANGAN SERING SERING DI BAWAH POHON TUA YANG GEDE YAA TAKUT JATOH DAHANNYA TRS MALAH LUKA KAN “
  
  #*IF CHOOSE A*
  
  mcname "Eh aku tau tempat yang bagus… Ikut yuk. "
  
  #*SKIP TO SCENE*
  #*BG ROOFTOP*
  
  mcname "Gimana, bagus kan?"
  
  tono "Wahhhh gokil juga pilihan lu, tapi ini ga ada orang yang ke sini kah?”"
  
  mcname "Ada tapi jarang sih, paling 1 atau 2 orang doang. Aman aja lah harusnya. "
  
  show pia_side at left with dissolve
  pia "Ya udah deh, ayooo latihannn. Pokoknya hari ini target yaaa, inget target kita.”"
  hide pia_side with dissolve
  
  show kana_side at left with dissolve
  kana "Siap Bu Guru Piaaa."
  hide kana_side with dissolve
  
  mcname "Semangat yaaa, aku mau beli minum dulu buat kalian semua. "
  
  #Kana, Tana, dan Pia pun melakukan latihannya di rooftop. Entah mengapa mereka terlihat lebih leluasa, mungkin karena tempatnya yang cukup luas dan udaranya yang sejuk membuat mereka cukup nyaman. Akan tetapi saat [mcname] membuka pintu, dia melihat sesuatu yang sedang terjadi.
  
  show pia_side at left with dissolve
  pia "Eh Nay ayoo dongg, jangan off tempoo. Udah berapa kali ini?”"
  hide pia_side with dissolve
  
  show kana_side at left with dissolve
  kana "Maaf maaf"
  hide kana_side with dissolve
  
  show pia_side at left with dissolve
  pia "Lu juga ton bukannya lu yang harusnya guide kita ya? Kok malah ga tau kalo kita off tempo atau salah sih… “"
  hide pia_side with dissolve
  
  tono "Eh gue juga udah nyoba ya, dikira gampang apa liatin 3 orang langsung? “"
  #“ Lu mah kan giliran di vokal, tunggu aja dulu napa? Tunggu giliran. “
  
  show pia_side at left with dissolve
  pia "Maksud lu apaan Ton? Gue kan pengen kita semua bisa, biar semuanya bisa, biar nanti pas tampil setidaknya ga salah dan ga malu maluin diliatin orang. “"
  hide pia_side with dissolve
  
  tono "Eh biasa aja dong, dikira gue ga mau bisa apa ya? Gue juga pengen bisa dong san-”"
  
  #Saat keadaan memuncak, [mcname] datang dan menjatuhkan kantong kresek yang penuh dengan minuman dan cemilan.
  #*BRAK*
  
  mcname "UDAH NAPA?! "
  
  #Mereka semua terdiam, melihat [mcname] yang telah datang
  
  #“ Bentar bentar, coba pelan-pelan deh ini masalahnya apa dah. “
  
  show pia_side at left with dissolve
  pia "Ini loh Tono. Dia kan harusnya yang guide dance kita, tapi Kana off tempo, gue off tempo, atau dia yang off tempo, dia ga ngeh. “"
  hide pia_side with dissolve
  
  tono "Ya sabar, gue juga harus ngecek rekaman dulu. Di sini ga ada kaca gede kaya di studio. “"
  
  show kana_side at left with dissolve
  kana "Eh… Maaf ya kayaknya aku kebayakan salahnya deh, jadi berantem gini… "
  hide kana_side with dissolve
  
  show pia_side at left with dissolve
  pia "Enggak Nay, ini bukan salah mu kok. “"
  hide pia_side with dissolve
  
  mcname "Udah udah"
  #“ Mending kalian semua minum sama nyemil dulu dah, ini lagi panas panasnya emang. Meskipun ada angin sepoi-sepoi, tapi cahayanya tetap panas. Minum dulu sana. “
  
  #Mereka pun mengambil beberapa minuman dan makanan dari kantong kresek yang telah dibawa [mcname] sebelumnya. Setelah menenangkan diri masing-masing, [mcname] pun berbicara 
  
  mcname "Okeee, ini pandangan gue ya. Jadi kalo kata Pia, Si Tono harusnya bisa nge guide kan? Tapi Tono ga bisa ngeguide terus-terusan karena harus lihat rekaman, ya? Dan Kana, kamu jangan mulai salahin diri sendiri lagi oke? "
  
  show kana_side at left with dissolve
  kana "Ehh… Uummm"
  hide kana_side with dissolve
  
  tono "Nahhh iya gituuu. Kalo di studio besar atau di ruang klub setidaknya ada kaca cermin, jadi gue bisa liat kalian semua. Tapi kalo di sini ga ada, jadi gue harus liat bolak balik rekaman gitu. “"
  
  show pia_side at left with dissolve
  pia "I-iya juga sih”"
  hide pia_side with dissolve
  
  mcname "Oke kalo gitu gue yang liat dan bantu rekam aja deh, nanti gue kasih rekamannya. Buat Pia, tetep kasih tau aja kalo ada yang off tempo. "
  
  show kana_side at left with dissolve
  kana "Maaf ya, aku sadar kok kalo tadi aku banyak off tempo dan diingetin bahkan dibackup sama Pia dan kamu ton, supaya gerakanku ga terlalu keliatan aneh... "
  hide kana_side with dissolve
  
  tono "Ah elah aman aja brookk, kamu juga baru belajar. Kamu udah bagus kok, tinggal sering sering latihan aja sih menurutku. “"
  
  show pia_side at left with dissolve
  pia "Iya kamu udah bagus kok, Nay. Nanti aku kasih tau deh triknya biar dapet tempo/ketukan yang pas gitu. “"
  hide pia_side with dissolve
  
  mcname "Nah kan kalo gini enak akur semua."
  
  #Tono 
  #‘ Iya Pii. Tadi sorry ya, gue kebawa emosi. Keknya karena emang panas sih, hehehe.”
  
  #Pia 
  #Gue juga minta maaf ya Ton. Padahal lu kan dah bantu guide kita dance gini, eh gue malah marah-marah ga jela. 
  
  #Kana
  #Aku juga minta maaf ya kalau banyak salah dan malah ngerepotin kalian.
  
  #Tono 
  #Ah elah napa malah jadi maaf maafan gini dah, perasaan lebaran masih lama dah. 
  
  #Mc
  #Nahhh kan mantepppp.
  
  #Kana, Tana, dan Pia pun melanjutkan latihannya kembali. Meski beberapa kali Kana terjatuh dan tertinggal, tapi ia tidak pernah dimarahi oleh Tono ataupun Pia. Malah Kana ditunjukan cara yang tepat dan dibimbing agar gerakannya menjadi lebih bagus lagi..
  
  show kana_side at left with dissolve
  kana "Aaaaa, capeeek banget."
  hide kana_side with dissolve
  
  show pia_side at left with dissolve
  pia "Iya nih, panas gerah banget yaaa capeeek. Tapi apalagi kamu Nay, kita istirahat kamu malah terus nyoba benerin gerakan kamu.”"
  hide pia_side with dissolve
  #,
  show kana_side at left with dissolve
  kana "Iya dong, biar ga ketinggalan sama kalian."
  hide kana_side with dissolve
  
  tono "Lu keren banget Nay. “"
  
  mcname "Eeh udah kali ya buat hari ini, rooftop udah mau ditutup. Tadi ada satpam yang ngasih tau aku gitu, terus aku bilang 5 menit lagi. Yuk beres-beres, jangan nyampah ya."
  
  tono "Oke deh, ga kerasa ya udah sore gini. “"
  
  show kana_side at left with dissolve
  kana "Iya ya ga kerasa. Makasih ya dah mau bantuuin aku. Maaf kalau aku agak nyebelin, hahah."
  hide kana_side with dissolve
  
  show pia_side at left with dissolve
  pia "Ga usah kebanyakan minta maaf Nay, geli tau. “"
  hide pia_side with dissolve
  
  tono "Bener. Ga usah minta maaf terus, santai aja. “"
  
  #Setelah pulang dari rooftop, mereka pun pulang ke rumah masing-masing. Hari demi hari berlalu diiringi latihan, hingga tak terasa waktu event dan perlombaan tinggal 1 minggu lagi. Latihan yang dilakukan menjadi semakin rumit dan semakin lama, ada kalanya mereka saling bertengkar satu sama lain akan tetapi langsung reda dan mencoba saling memahami.
  
  #Di suatu hari 
  #MC melihat Kana pergi ke arah rooftop sendirian. Awalnya [mcname] mengira akan ada latihan tambahan, akan tetapi di group tidak ada obrolan mengenai hal tersebut.
  
  mcname "Hmmm itu kan Kana, kenapa dia sendirian ya ke rooftop? Perasaan hari ini ga ada latihan deh… Aku nyusul dah."
  
  #Saat membuka pintu, terlihat Kana yang sedang melihat ke arah langit dengan pandangan kosong, bahkan sampai tidak menyadari kehadiran [mcname] di situ.
  
  mcname "NAY!"
  
  show kana_side at left with dissolve
  kana "HAAAAA!!!"
  hide kana_side with dissolve
  #“ Eh [mcname]? Ku kira siapa, kaget tau. “
  
  #MC
  #‘Hahaha dari tadi aku panggil loh, kamu ga sadar kah? Ada apa Nay? “
  
  show kana_side at left with dissolve
  kana "Engg-"
  hide kana_side with dissolve
  
  mcname "Sebelum itu, nih minum dulu. "
  
  #Kana melihat ke arah MC. Pandangan Kana terlihat sedih, senang, dan cemas di saat yang bersamaan. Mungkin Kana memiliki banyak pikiran atau mungkin hanya ingin sendirian, tetapi Kana saat itu tahu kalau dia hanya bisa bercerita tentang hal ini kepada MC.
  
  show kana_side at left with dissolve
  kana "Hahaha, ketahuan ya kalo aku lagi ada pikiran. "
  hide kana_side with dissolve
  
  mcname "...."
  
  show kana_side at left with dissolve
  kana "Entah kenapa selama latihan aku liat rekaman kita, aku ngerasa kalau aku paling telat dan paling ga menonjol gitu."
  hide kana_side with dissolve
  #“Meski udah coba berusaha buat positif, pikiran negatif ini terus-terusan muncul dan buat aku kadang ga bisa tidur.”
  #“Aku takut malah menghambat mereka pas perform nanti, haha.”
  
  mcname "..."
  
  show kana_side at left with dissolve
  kana "Maaf ya. Padahal aku udah janji ke kamu bakal berusaha ga berpikiran negatif lagi, eh tapi sekarang malah gini lagi."
  hide kana_side with dissolve
  
  mcname "Ga usah minta maaf Nay, harusnya aku yang bisa dukung kamu lebih baik lagi."
  #“ Aku ga bisa bilang apa-apa lagi, semua yang aku katakan waktu itu bener-bener apa yang ada di pikiranku. Kalau kamu mau tau seberapa berkembangnya kamu, nih kamu bisa lihat rekaman ini.“
  
  #MC memberikan HPnya kepada Kana. Di dalam HP tersebut ada sebuah video yang menunjukan Kana pada saat latihan pertama kali dan latihannya yang terakhir kali. Kana dan [mcname] hanya terdiam melihat rekamanan tersebut. Setelah selesai, [mcname] pun mulai memberikan pendapatnya
  
  mcname "Kamu udah improve banyak banget, Nay. Kamu liat deh gerakan kamu, nyanyian kamu, teknik kamu, kamu udah berkembang sejauh ini. "
  
  show kana_side at left with dissolve
  kana "T-tapi kan.."
  hide kana_side with dissolve
  
  mcname "Nay, even if u fall on stage, kamu pikir Tono sama Pia bakalan marahin kamu? Atau kamu pikir aku bakalan malu sama kamu?"
  
  mcname "Tono, Pia, dan aku tau perjuangan kamu. Jadi aku yakin mereka ga bakalan marah, malahan bangga sama usaha dan kerja kerasmu."
  
  show kana_side at left with dissolve
  kana "Kalau dipikir-pikir Tono sama Pia meski aku udah sering jatoh dan salah, mereka ga pernah marahin aku. Malah bantuin aku gitu, ya meski diketawain sama Si Tono dulu sih."
  hide kana_side with dissolve
  
  mcname "Itu dia, mereka ga pernah marah ke kamu karena mereka udah liat seberapa besar perkembangan kamu. Jadi, tetep semangat oke? Besok kita latihan lagi loh."
  
  show kana_side at left with dissolve
  kana "Makasih yaaa MC, udah mau dengerin cerrita aku yang gini lagi. "
  hide kana_side with dissolve
  
  mcname "Aku ga bakalan pernah bosen dengerin kamu cerita kok Nay."
  
  #Sambil ditemani oleh [mcname] di rooftop, Kana mulai latihan lagi karena tidak ingin menjadi beban dan tidak ingin berbuat kesalahan pada saat perform nanti. 
  
  #*SKIP TO SCENE*
  #*BG ROOFTOP*
  
  #BEBERAPA HARI KEMUDIAN
  #Tono 
  #H-1 acara
  #“ Okeee! Waktu kita sudah semakin dekat, jadi kita ga terlalu banyak latihannya. Takut nanti malah ada yang cedera atau gimana, jadi kita latihan ringan aja.“
  
  show pia_side at left with dissolve
  pia "Siappp.”"
  hide pia_side with dissolve
  
  show kana_side at left with dissolve
  kana "Oke Ton. "
  hide kana_side with dissolve
  
  #Mereka bertiga pun memulai latihannya kembali. Di saat latihan, ada beberapa momen Kana yang membuat dia putus asa karena tidak dapat mengikuti beberapa gerakan yang menjadi titik lemahnya saat latihan selama ini. Tono dan Pia memberikan beberapa saran untuk membantu Kana melakukan gerakan tersebut. Saat mencoba, Kana tiba-tiba melihat ke arah [mcname] 
  
  mcname "SEMANGAT NAYYYY!!!!"
  
  #Saat mendengar suara tersebut, Kana menjadi bersemangat dan akhirnya setelah beberapa kali mencoba, dia dapat melakukan gerakan tersebut. Terkejut senang, Tono dan Pia pun memeluk Kana karena bangga dengan apa yang Kana berhasil lakukan.
  
  tono "Akhirnya lu bisa juga Nayyyy!!”"
  
  show pia_side at left with dissolve
  pia "Iyaaa Nayyyy, setelah sekian purnama akhirnya kamu bisa!! “"
  hide pia_side with dissolve
  
  show kana_side at left with dissolve
  kana "Hehehe, makasih ya udah mau ngajarin dengan sabar. Makasih juga tadi buat semangatnya, [mcname] "
  hide kana_side with dissolve
  
  #Kana tersenyum ke arah MC. Meskipun ia terlihat kelelahan, senyumannya tetap manis dan membuat [mcname] merasa tenang.
  
  tono "Break dulu bentar ya, kita harus obrolin juga buat nanti tampil. “"
  
  show pia_side at left with dissolve
  pia "Okeee. Btw Nay gimana, kamu siap ga? Kan tampil di depan banyak orang.”"
  hide pia_side with dissolve
  
  show kana_side at left with dissolve
  kana "Eehhhhh iyaa! Aku lupa soal itu aaaaa… Kalo aku pake topeng boleh ga ya? "
  hide kana_side with dissolve
  
  tono "Haaaa topeng? Ini kan idol Nay, bukan pertunjukan tari tradisional. Ah elah santai aja napa? Lu kan cantik, pasti banyak yang liatin kok. Ga usah malu gitu. “"
  
  show pia_side at left with dissolve
  pia "Setuju sama Tono, santai aja ga usah malu. Nanti liat ke kita atau ke [mcname] aja, hahaha.“"
  hide pia_side with dissolve
  
  mcname "Eh umm, i-iya kali ya? Hahaha"
  
  show kana_side at left with dissolve
  kana "Eeh..uuuu"
  hide kana_side with dissolve
  #Kana dan [mcname] saling bertatapan dan suasana canggung itu dipecahkan oleh Tana.
  
  tono "Udah lah, nanti juga bisa kok. Yuk lanjut latihan gerakan tadi, pengen liat kalau kita bareng-bareng gimana.“"
  #
  #Mereka melanjutkan latihan mereka. Kali ini mereka melakukan semuanya dari awal, ditambah dengan bernyanyi juga. Saat selesai, Tana dan Pia terkejut
  
  tono "Nay…ini serius? Piii serius kan ini? Ini bukan mimpi kan?”"
  
  #Pia pun menampar pipi Tana 
  #*plak*
  
  tono "AAAAAAWWWW!! Apaan sih kocak, sakit tau!“"
  
  #Pia 
  #‘ Oke. Berarti ini bukan mimpi, Ton. “
  
  tono "Ya ga usah ke gue juga kocak! Kan bisa ke lu sendiri, ahhhh!”"
  
  show kana_side at left with dissolve
  kana "Hehehe, akhirnya bisa juga. Keren kan?"
  hide kana_side with dissolve
  
  mcname "KEREN BANGET! PAKE BANGET, NAY!!"
  
  tono "Iyaaa akhirnya lu bisa juga! Aduhhh jadi ini apa yang dirasakan ibu-ibu pas liat anaknya berhasil. “"
  
  show pia_side at left with dissolve
  pia "emang lu punya anak, Ton?”"
  hide pia_side with dissolve
  
  tono "Ya ga gitu konsepnya, ah elah. Maksudnya gue bangga gitu, kan ga harus jadi ibu supaya bangga.“"
  
  show kana_side at left with dissolve
  kana "Ibu enggak, tapi jompo iya. Hahahah"
  hide kana_side with dissolve
  
  mcname "Kalo soal jompo mah aku setuju sih, ahahah."
  
  tono "Ah elah nyerang gue aja semuanya.“"
  
  #Selagi tertawa dan membahas bagaimana perform nanti, waktu tak terasa sudah sore. Satpam kembali memperingatkan MC, Tana, Pia, dan Kana untuk segera pulang.
  
  mcname "Eh udah beres-beres belum? Ini udah diingetin lagi sama satpamnya. "
  
  show kana_side at left with dissolve
  kana "Udah kok, yuk. "
  hide kana_side with dissolve
  
  tono "Eh kalian berdua duluan aja, soalnya kita ada perlu di klub. Ga tau ini aku sama Pia dipanggil sama ketua klub, kayaknya ada sesuatu yang urgent deh. “"
  
  mcname "Hmmm kok aku sama Kana ga dipanggil ya? Padahal sama-sama panitia juga. "
  
  show pia_side at left with dissolve
  pia "Kan kita beda divisi. Gapapa kok duluan aja, nanti kita ngobrol di chat aja. “"
  hide pia_side with dissolve
  
  show kana_side at left with dissolve
  kana "Oke dehh, duluan yaa~ "
  hide kana_side with dissolve
  
  "Kana dan [mcname] pergi duluan, sedangkan Tana dan Pia harus pergi ke ruangan klub jejepangan."
  #*SKIP TO SCENE*
  #*BG DEPAN KAMPUS SORE*
  
  #Di perjalanan pulang…
  
  #MC
  #‘ Jadi gimana perasaan idol kita yang satu ini?”
  
  show kana_side at left with dissolve
  kana "Iiiihh apaan sih, aku kan belum jadi idol."
  hide kana_side with dissolve
  
  mcname "Heeee BELUM ya…berarti mau dong."
  
  show kana_side at left with dissolve
  kana "Yaaa awalnya sih aku coba-coba."
  hide kana_side with dissolve
  #“ Meski sering ngedown, punya pikiran negatif…. Tapi latihan sama mereka, coba nyanyi, coba dance ternyata seruu banget! Aku juga enjoy pas sama mereka. Mungkin kalo kita menang, aku mau deh jadi idol hahah.”
  
  mcname "Cieeee, kalau gitu besok debut pertama kamu dong. "
  
  show kana_side at left with dissolve
  kana "Iiihhh apaan siihh. Ga usah kaya gitu ah, makin gugup nih aku. "
  hide kana_side with dissolve
  
  mcname "Biar ga gugup nanti aku paling depan deh. Terus bakal jadi yang paling semangat teriaknya, gimana? Jadi kalo gugup, liatnya ke aku aja."
  
  show kana_side at left with dissolve
  kana "Eh…"
  hide kana_side with dissolve
  #Wajah Kana tersipu mendengar apa yang diucapkan [mcname] saat itu
  #“J-janji ya.. “
  
  mcname "Iya, janji kok Nay."
  
  show kana_side at left with dissolve
  kana "A-awas aja kalau enggak."
  hide kana_side with dissolve
  
  #Sambil tersipu malu, Kana dan [mcname] pulang ke rumahnya masing-masing.
  #
          #*SKIP TO SCENE*
            #*BG KOS MALAM*
  #
  mcname "Kalo gugup liat ke aku aja… aaaa malu juga kalau diinget-inget."
  #“ Tapi ya udah deh, yang penting Kana bisa semangat. “
  
  
  #*SUARA NOTIF*
  
            #*HP*
  
  tono "Eh besok kita datang lebih awal yaa, dari pagi aja biar ada waktu latihan dikit-dikit dan supaya ga gugup juga, gimana?”"
  
  show pia_side at left with dissolve
  pia "Gue ikut deh Ton, tapi awas aja lu jangan sampe telat ya. “"
  hide pia_side with dissolve
  
  show kana_side at left with dissolve
  kana "Dih yang bener aja. "
  hide kana_side with dissolve
  #“ Aku mah ga pernah telat, coba tanya MC. “
  
  mcname "Iya ga telat, cuma mepet aja. "
  
  show kana_side at left with dissolve
  kana "Heheh~"
  hide kana_side with dissolve
  
  #MC
  #‘ Ya udah kalian istirahat. Besok hari besar buat kalian semua, semangat yaa jangan sampe begadang loh. “
  
  show kana_side at left with dissolve
  kana "Siappp!"
  hide kana_side with dissolve
  
  show pia_side at left with dissolve
  pia "Okee”"
  hide pia_side with dissolve
  
  tono "Okee Brookkk.”"
  
  #*SKIP TO SCENE*
  #*BG RUANGAN KLUB*
  #ACARA JEJEPANGAN
  #Hari yang dinanti-nantikan telah tiba, acara event jejepangan pun di buka. Banyak Mahasiswa/i pun bersorak sampai terdengar ke ruangan klub jejepangan. Akan tetapi Kana, Tono, dan Pia seakan tidak mendengar suara tersebut, mereka terus terusan mencoba beberapa gerakan dan terkadang duduk diam menghafalkan lirik.
  #Kana pun sama, ia duduk diam tangannya yang gemetaran bisa terlihat oleh MC.
  
  mcname "Nay, ikut aku keluar dulu yuk. "
  
  show kana_side at left with dissolve
  kana "Eh?"
  hide kana_side with dissolve
  
  #MC menarik tangan Kana, membuat Kana kaget dan berdiri meninggalkan kursinya.
  #MC membawa Kana ke area event jejepangan. 
  
  show kana_side at left with dissolve
  kana "Eeeh… [mcname] kenapa ya "
  hide kana_side with dissolve
  
  mcname "Kamu yang kenapa gugup banget, tanganmu gemetaran tuh hahaha."
  
  #Kana
  #‘ Gimana ga gugup? Ini kan pertama kalinya aku tampil… “
  
  #Mc
  #‘ Ya udah ikut aja yuk, muter-muter event sini. Kita liat-liat dulu ada apa aja. “
  
  show kana_side at left with dissolve
  kana "Boleh deh, dari pada aku pusing sendiri. "
  hide kana_side with dissolve
  
  #*SKIP TO SCENE*
  #*BG JEJEPANGAN*
  #Kana dan [mcname] menikmati booth dan stand yang ada di event jejepangan tersebut, sesekali mereka juga melihat ke arah main stage di mana ada mini konser yang sedang berlangsung. Kana pun merasa senang dan mungkin sudah melupakan ke grogiannya meski hanya sedikit 
  
  show kana_side at left with dissolve
  kana "Hahahaha, asik bangettt~ "
  hide kana_side with dissolve
  
  mcname "Iya kannn? Jadi gimana, udah ga gugup lagi?"
  
  show kana_side at left with dissolve
  kana "Masih sih, tapi udah lumayan aman. Kayaknya gara-gara udah muter-muter terus ngeliat orang lain perform. Ternyata mereka perform karena mereka suka ya, seneng gitu liatnya."
  hide kana_side with dissolve
  
  mcname "Iyaa kan, tujuan event jejepangan biar bisa have fun. Jadi ga usah gugup yaa. "
  
  show kana_side at left with dissolve
  kana "Siappp.."
  hide kana_side with dissolve
  
  #Di saat mereka sedang bercanda dan melihat performa yang lain, Pia dan Tana menghampiri dengan buru-buru. 
  
  show pia_side at left with dissolve
  pia "NAHHH! ITU DIA TON! “"
  hide pia_side with dissolve
  
  tono "Alahhhhh, ke mana aja kalian sihh. Gue nyariin, ayoo cepet siap-siap 30 menit lagi kita tampilll.“"
  
  #Kana
  #‘ Eehhhh, MC. Aku duluan yaaa, aku mau siap-siap dulu.”
  
  #Mc
  #‘ Iyaa, semangat yaa. “
  
  show kana_side at left with dissolve
  kana "Btw jangan lupa janjimu ya, dadahhhh."
  hide kana_side with dissolve
  
  #*SKIP TO SCENE*
  #*BG STAGE*
  
  #MC (PEMBAWA ACARA)
  #“ Baiklah, untuk selanjutnya kita akan ada pertunjukan dari salah satu perwakilan klub jepang!! Kalo sebelumnya kita udah nonton band, cosplay, dan lainnya, sekarang kita waktunya untuk melihat idol!!! Apakah kalian semua siap!!??? Ini dia saksikan KTp!!!”
  
  #*SFK SUARA TERIAKAN ORANG ORANG*
  
  tono "Haloooo semuanya~ Sebelumnya kenalin yaa, kita dari Ktp, Kana, Tana, dan Piaaa~"
  #Di sini kita bakalan nyoba nyanyi sama dikit-dikit dance yaa, tapi sebelumnya mari kita kenalan dulu~ “
  
  show pia_side at left with dissolve
  pia "Halo semuanya~"
  hide pia_side with dissolve
  #“We Are On Fire! 🔥 Semangat ku membara, siap menghangatkan hari-hari mu! Halo, aku Pia Meraleo dari JKT48V. Senang bertemu kalian 🔥🦁”
  #
  #Penonton
  #“WUOOOH!!!!”
  
  tono "Okeee selanjutnya giliran gue. Wassup ma bross!!👊🏻👊🏻 I'm fresh like a breeze🍃 JKT48V Tana Nona! Cool enough to make you freeEeEzZEeE😎🥶 “"
  
  #Penonton
  #“WUOOOH!!!!”
  
  show kana_side at left with dissolve
  kana "Ehh… I-iyaaa… K-kenalain semuanya n-namaku Kanaaaa-"
  hide kana_side with dissolve
  #*SFX BRAK*
  #Seketika para penonton terdiam ada beberapa yang tertawa karena mic Kana tiba-tiba terjatuh dari tangannya. Wajah Kana terlihat pucat dan tangannya gemetaran. Air mata mulai muncul di ujung matanya. Kana sangat gugup dan hampir menangis.
  #Tiba-tiba…
  
  mcname "KANAIAAA!!!!! SEMANGAATTTTT!!!!"
  
  #Di antara keheningan para penonton, [mcname] berteriak hingga orang-orang melihat ke arahnya dengan tatapan aneh. Akan tetapi [mcname] tidak peduli dan hanya tersenyum ke arah Kana. 
  #Kana terkejut lalu melihat ke arah [mcname] dan tersenyum. Kana menarik nafas, lalu mengambil micnya dan tersenyum.
  
  show kana_side at left with dissolve
  kana "Maaf yaaa soal sebelumnya, gugup dikit hehe. Oke semuanya. Mari bernyanyi, sambil bermain air. Aku dari laut tapi tidak salty! 🎶🐟 Halo! Aku Kanaia yang akan membuat harimu indah bagai pelangi~ 🌈✨ "
  hide kana_side with dissolve
  
  mcname "KANAAAAAAA!!!!"
  
  #Penonton
  #“WUOOOH!!!!”
  
  #Tana
  #“ Udah sesi perkenalannya, sekarang kita akan tampil. Jadi, jangan lepaskan pandangan kalian dan dengarkanlah lagu dari kami!”
  
  #Penonton
  #“WUOOOH!!!!”
  
  #*SKIP TO CG PERFORM*
  #*CREDIT*
