label chapter2piabegin:
    scene black with dissolve
    show text "{color=#FFF}Chapter II{/color}" with Pause(2.0)
    scene black with dissolve
    "Peralatan menggambar sudah siap, Mahasiswa/i baru DKV pun memulai kelas ujian menggambar pertamanya"
    scene kelas with dissolve
    play music "audio/BGM_Dosen + Rektor.mp3" fadein 1.0
    show dosen at dosen_center with dissolve
    show dosen_side at left with dissolve
    $ dosen_name = "Dosen Seni"
    $ quick_menu = True
    dosen "Ya, ujiannya adalah menggambar teman kalian."
    hide dosen_side at left with dissolve
    "Mahasiswa/i" "Heeeeeee, waduh bu"
    dosen "Ibu udah buat undiannya, ya. Kita undi nama pasangan gambar kalian"
    dosen "Jadi nanti kalian hadap-hadapan dan gambar teman di depan kalian"
    dosen " Semua karya tugas ini akan dipajang di sepanjang lorong gedung DKV ini, ya! Tunjukan bakat kalian kepada yang lain!"
    hide dosen_side with dissolve
    hide dosen with dissolve
    show pia at pia_near with dissolve
    show pia_side at left with dissolve
    pia "Hueeeee…..PRESUREEEEE"
    hide pia_side with dissolve
    mcname "Hahaha dapet siapa ya pasangannya~"
    hide pia with dissolve
    show dosen at dosen_center with dissolve
    show dosen_side at left with dissolve
    dosen "[mcname]"
    hide dosen_side with dissolve
    mcname "Hmm…. Yak"
    show dosen_side at left with dissolve
    dosen "Berpasangan sama Pia, ya."
    hide dosen with dissolve
    hide dosen_side with dissolve
    show pia at pia_near with dissolve
    show pia_side at left with dissolve
    pia "YEEEEES! MUAHAHAHA."
    hide pia with dissolve
    hide pia_side with dissolve
    show dosen at dosen_center with dissolve
    show dosen_side at left with dissolve
    dosen "Pia! Jangan berisik."
    hide dosen with dissolve
    hide dosen_side with dissolve
    show pia_sad at pia_near with dissolve
    show pia_side_sad at left with dissolve
    pia "Maaf, bu"
    hide pia_side_sad with dissolve
    "Mahasiswa/i" "Hahahahahahahaha"
    "Semua maba berpindah posisi berhadapan dengan pasangan yang sudah dipilih oleh Bu Dosen."
    $ quick_menu = False
    scene black with dissolve
    scene kelas with dissolve
    show pia at pia_near with dissolve
    show pia_side at left with dissolve
    $ quick_menu = True
    pia "HAI [mcname]! HUEHEHEHEH"
    hide pia_side with dissolve
    mcname "Apalah Pia Pia ini"
    show pia_side at left with dissolve
    pia "Mau gambar aku kayak gimana? Cute? Seksi? Cool?"
    hide pia_side with dissolve
    mcname "Halah, kuping gajah gak sih?"
    show pia_angry at pia_near with dissolve
    show pia_side_angry at left with dissolve
    pia "HEEEEH!!!! Ahahahaha."
    hide pia_side_angry with dissolve
    hide pia_angry with dissolve
    "Mereka pun bergantian setiap 15 menit untuk saling menggambar pasangannya tersebut."
    $ quick_menu = False
    scene black with dissolve
    scene kelas with dissolve
    show pia at pia_near with dissolve
    $ quick_menu = True
    mcname "*Sedang menggoreskan kuas di atas canvasnya sambil memandang Pia.*"
    stop music fadeout 1.0
    play music "audio/BGM_Romance Pia Kamar.mp3" fadein 1.0
    mcname "*dalam hati*"
    mcname "{i}Waduh. Makin diliat, makin imut dan manis ya Pia Pia ini.{/i}"
    mcname "*Sambil melirik melihat wajah samping Pia*"
    show pia_shy at pia_near with dissolve
    pia "*Muka memerah*"
    mcname "Sakit, Pia? ahahaha"
    show pia_side_shy at left with dissolve
    pia "Dieeeeeem! Aku tuh ga biasa dipandangin gini, ih"
    pia "Buru selesaiin gambarnya!!"
    hide pia_side_shy with dissolve
    show pia_angry at pia_near with dissolve
    hide pia_shy with dissolve
    hide pia_side with dissolve
    mcname "Lah sabar, baru sketch weh."
    show pia_side_angry at left with dissolve
    pia "*Huft*"
    $ quick_menu = False
    stop music fadeout 1.0
    jump startPiaGame


label chapter2piaaftergame:
    stop music fadeout 1.0
    scene black with dissolve
    "Mini Game Selesai"
    play music "audio/Dreamcatcher.mp3" fadein 1.0
    jump credits