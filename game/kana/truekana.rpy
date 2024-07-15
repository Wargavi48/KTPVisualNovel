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
