label chapter2kanastart:
    $ renpy.block_rollback()
    scene black with dissolve
    show text "{color=#FFF}Chapter II{/color}" with Pause(2.0)
    scene awan with dissolve
    mcname "Karena hari ini hari libur, jadi [mcname] memutuskan untuk menghabiskan waktunya berkeliling di Mall yang dekat dengan kosan nya"
    scene mall temp with dissolve
    play music "audio/BGM_Mall Slow.mp3" fadein 1.0
    play sound "audio/crowd_noise.mp3" fadein 1.0
    mcname "Rame juga ya ternyata mall di Jakarta ini"
    "Di sekeliling memang banyak orang terlihat, dari keluarga kecil, pasangan muda yang sedang kencan, bahkan seseorang yang terlihat sendirian menikmati waktunya"
    "Namun dari banyaknya orang disekitar, ada beberapa kumpulan orang yang menarik perhatian [mcname]"
    mcname "Lumayan nyentrik pakaian orang-orang itu, mungkin itu normal di Jakarta?"
    mcname "Ahhhh.. Mungkin itu mereka sedang cosplay yang sering mamah lakuin"
    scene white with Dissolve(2.0)
    # Harusnya ada frame putih atas bawah
    scene mc bedroom with dissolve
    play music "audio/backsound_kamar.mp3" loop fadein 1.0
    
    play music "audio/Dreamcatcher_v2.mp3" fadein 1.0
    jump credits