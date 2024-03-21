define char_test = Transform(zoom=0.5,xalign=-2.0,yalign=-2.0)


label chapter1pia:
    scene kampus with dissolve
    "Jeketi University\nKampus ternama di indonesia dibawah naungan Melody Corps. Merupakan universitas Negeri unggulan di Jakarta." 
    "Banyak orang bilang, kampus ini mencetak banyak sekali orang sukses. Artis, politisi, ilmuan, bahkan menjadi Idol terkenal pun bisa diraih disini." 
    "Orang yang lulus menyandang gelar lulusan dari JU banyak dicari orang, karena kualitas pelajarnya sangat baik. Namun, untuk masuk ke JU ini pun tidak mudah"
    mcname "Wah! besar juga ya kampusnya, dan aku bakal berkuliah disini huhuuu beruntungnya aku"
    scene black with dissolve
    show text "BRUKKKK!" with Pause(1)
    scene kampus with dissolve
    show pia at char_placement with dissolve
    # show piasprites at char_test with dissolve
    pia "Eh maaf kak ketabrak, gak apa - apa kan?"
    pia "Lagi buru-buru maaf ya"
    mcname "Ah gak papa kok."
    mcname "hehe"
    mcname "Maaf juga aku ngelamun ditengah jalan"
    pia "hehe oke maaf bye!"
    hide pia 
    mcname "Ah! Aku juga harus buru - buru daftar ulang!"
    "MC pun selesai registrasi daftar ulang ke jurusan DKV"
    scene black with dissolve
    show text "1 MINGGU KEMUDIAN" with Pause(1.5)
    scene black with dissolve
    scene kampus with dissolve
    "Dekan DKV" "Selamat datang di Jeketi University para Mahasiswa dan Mahasiswi baru! raihlah mimpi kalian disini!! selamat berjuang!"
    "Dekan DKV" "Hadirin, dipersilakan untuk pulang"
    mcname "Hueeeee....capek juga duduk doang dengerin orang ngomong. besok mulai masuk kuliah, gak sabar bakal ketemu orang orang baru"
    pia "HEEEEEEEEEEEE!! KAMUUUUUUU"
    mcname "buset, siapa itu tereak tereak"
    mcname "loh kok kayaknya nyamperin aku"
    show pia at char_placement with dissolve
    pia "HEIIIII!!! INGET AKU GAKKK???"
    mcname "iya aku inget, tapi bisa gak tereak gak? malu diliatin banyak orang ini"
    pia "oh iya, maap. hehe OH! INGET AKU? KITA TABRAKAN DEPAN GERBANG MINGGU LALU! KIRAIN KAMU SENIOR! TERNYATA MABA JUGA KAYAK AKU HAHAHAHA"
    mcname "((buset tereak lagi))"
    pia "kamu DKV juga ya! gilak ternyata kita sejurusan. apakah jodoh?"
    pia "candaaaaa ahahaha"
    mcname "ahaha ahaha iya sejurusan ternyata ya kita. oh iya kita belom kenalan. nama aku [mcname]"
    $ pia_name = "Pia"
    pia "LAH IYA BELOM KENALAN. halo, aku Pia Meraleo salam kenal"
    mcname "((wah kalo diliat dari dekat gini, manis juga Pia ini))"
    pia "[mcname], kok bengong? makan bareng yuk, pengen liat kantin kampusnya kayak gimana. laper juga sih"
    mcname "lah, lesgooo, pas banget ini laper"
    hide pia 
    "MC dan pia berjalan ke kantin kampus untuk makan"
    show pia at char_placement with dissolve
    pia "WEEEH GEDE JUGA KANTINNYA YA!"
    mcname "selain kantin, suara kamu juga gede btw"
    pia "EH maap, kebiasaan ahahaha"
    mcname "gapapa kok. seru juga kamu gak abis abis energinya"
    pia "i-iya kah? ahahaha *blushing*"
    pia "oh, mau makan dimana ini mejanya full semua"
    mcname "iya lagi, eh tapi dipojokan itu ada meja isinya cuma sendiri, numpang bareng aja ap--"
    pia "halooo, sendiri? boleh numpang duduk 1 meja disini gak?"
    mcname "ah.......Pia......langsung banget"
    "???" "eh oh mmm iya k-kosong kok. duduk aja"
    hide pia 
    "[mcname], Pia dan Orang itu duduk di 1 meja yang sama"
    "Sambil makan"
    show pia at char_placement with dissolve
    pia "jweerushan aphah kwamuh?\n(jurusan apa kamu)"
    "???" "aku? aku DKV"
    pia "EEEEEEH SWAAAMAAA!! KOK GWAK LIYAT KWAMU PAS PWENGENALAN?"
    mcname "Telen dulu Pia.........."
    mcname "(tapi iya deh, aku gak liat mba ini kayaknya pas pengenalan)"
    "???" "oh kamu MaBa ya? aku udah semester 4. gamungkin ikut kesana tadi"
    pia "eh kakak senior, maaf kak. kirain MaBa juga"
    mcname "eh maap kak Pia emang kelakuannya nyablak (yup. pantes gak liat tadi)"
    "Fiony" "hahaha santai aja, lanjut makan. kok jadi kaku kalian. kenalin aku Fiony"
    pia "A-AKU PIA MELALEO *panik"
    mcname "pppfffftt melaleo ahaha, kenalin kak aku [mcname]"
    pia "aaaaa kan jadi typo ngomongnya. meraleo maksudnyaaaaa"
    hide pia
    "Mereka ber 3 pun melanjutkan makan sembari ngobrol "
    # jump memory_game_start
    jump utamapia