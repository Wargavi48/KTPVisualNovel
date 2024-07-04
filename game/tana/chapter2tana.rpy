label chapter2tana:
    $ quick_menu=True
    play music "audio/bgm_harvestmoon_spring.mp3" fadein 1.0
    scene awan with dissolve
    "Keesokan paginya, Tana berangkat menuju kampus seperti biasanya."
    $ quick_menu=False
    scene kelas with dissolve
    $ quick_menu=True
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    "Sesampainya di depan pintu ruang kelas, Tana mendengar keramaian dari dalam kelas."
    show tana at tana_near with dissolve
    show tana_side at left with dissolve
    tana "Anak-anak rame banget deh di dalam. Ada apa, ya?"
    hide tana_side
    "Penasaran dengan keramaian tersebut, Tana pun membuka pintu kelas."
    "Setelah pintu kelas terbuka dan para Mahasiswa/i melihat Tana di depan pintu, ada beberapa mahasiswa yang berteriak."
    #Sprite RG Hasan
    "RG Hasan" "Guys, ini dia dancer andalan kita!"
    "RG Hasan" "Hahahaha!"
    #Sprite Bang Rama
    "Bang Rama" "onoT, kamu centil banget sih!"
    "Bang Rama" "Hahahaha!"
    "Tana pun kebingungan dan mencoba memahami kejadian yang sedang terjadi di depan matanya ini."
    show tana_side at left with dissolve
    tana "Hah?! Centil?! Centil apaan kocak! G ausah ngadi-ngadi lu pada!"
    hide tana_side at left with dissolve
    "RG Hasan" "Alah alahh... Sa ae lu, Tana. Kita udah liat videonya."
    "RG Hasan" "Hahahaha!"
    "Tana pun semakin bingung dengan video apa yang dimaksud oleh teman-temannya. Dengan wajah bingung dan panik, Tana pun bertanya pada temannya."

    $ quick_menu=False
    scene awan with dissolve
    play music "audio/bgm_harvestmoon_spring.mp3" fadein 0.5
    show text "{size=+10} KEESOKAN HARINYA {/size}" with Pause(2.0)
    scene kelas with Dissolve(2.0)
    $ quick_menu=True
    play music "audio/BGM_Kelas.mp3" fadein 1.0
    "Jadwal kuliah hari ini hanya ada satu kelas praktikum jam 8 pagi, tapi seluruh mahasiswa disuruh untuk berkumpul di kelas karena akan ada arahan dari Bu Dosen."
    "[mcname] pun datang lebih pagi dan memilih untuk belajar di dalam kelas sembari menunggu kelas dimulai."
    mcname "Hadeh, susah banget deh mata kuliah ini. Kok bisa ada kating yang dapet nilai A. Ini gua yang bodoh atau gimana dah."

    menu:
        "Responmu:"
        "Duduk Tana":
            mcname "Duduk Ta-"
        ".................":
            mcnamne "................."
    "Setelah melihat ke sekitar kelas, Tana menemukan bangku kosong lainnya yang tidak jauh dari tempatnya sekarang."
    "Tanpa berkata apapun, Tana pergi meninggalkan MC dan langsung duduk di bangku tersebut."




    menu:
        "TRUE ENDING":
            jump chapter2tanaTRUE
        "GOOD ENDING":
            jump chapter2tanaGOOD

label chapter2tanaTRUE:
    stop music fadeout 1.0
    scene black with dissolve
    show text "{color=#FFF}CHAPTER III{/color}" with Pause(2.0)
    play music "audio/Dreamcatcher.mp3" fadein 1.0
    jump credits
label chapter2tanaGOOD:
    stop music fadeout 1.0
    scene black with dissolve
    show text "{color=#FFF}CHAPTER III{/color}" with Pause(2.0)
    play music "audio/Dreamcatcher.mp3" fadein 1.0
    jump credits