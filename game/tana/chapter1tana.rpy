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
    play music "audio/Dreamcatcher.mp3" fadein 1.0
    jump credits