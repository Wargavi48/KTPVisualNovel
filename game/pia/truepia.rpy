label truepia:
    mcname "aku tau, kebetulan sempet jalan jalan daerah sini pas lowong kemaren"
    show pia at char_placement with dissolve
    show pia_side at left
    pia "ah mantap! beli kemana? deket?"
    hide pia_side
    mcname "agak jauh sih tapi disana lengkap. mau beli bareng?"
    show pia_side at left
    pia "*blush* M-MAUUUUU!! AYOO"
    hide pia_side
    scene black with dissolve
    show text "KEESOKAN HARINYA" with Pause(1.5)
    scene black with dissolve
    # scene kampus with dissolve
    $ renpy.block_rollback()

    return
