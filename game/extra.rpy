# Extras Screens

image pager_button = im.FactorScale("extra/pager_cr.jpg", 0.25)
image lorong_button = im.FactorScale("extra/lorong_cr.jpg", 0.25)
image kepsek_button = im.FactorScale("extra/kantor_kepsek_cr.jpg", 0.25)
image kelas_button = im.FactorScale("extra/kelas_cr.jpg", 0.25)
image ruangtamu_button = im.FactorScale("extra/ruang_tamu_cr.jpg", 0.25)
image mall_button = im.FactorScale("extra/mall_cr.jpg", 0.25)
image kantin_button = im.FactorScale("extra/kantin_cr.jpg", 0.25)


# image bglock_button = "gui/bg_locked.jpg"

init python:

    # Gallery
    # g = Gallery()

    # A button with an image that is always unlocked
    # g.button("pager_cr")
    # g.image("pager_cr")
    
    # g.button("lorong_cr")
    # g.image("lorong_cr")

    # g.button("kantor_kepsek_cr")
    # g.image("kantor_kepsek_cr")

    # g.button("kelas_cr")
    # g.image("kelas_cr")
    
    # g.button("ruang_tamu_cr")
    # g.image("ruang_tamu_cr")

    # g.button("mall_cr")
    # g.image("mall_cr")

    # g.button("kantin_cr")
    # g.image("kantin_cr")


    # Ending Unlocked Pict

    # g_ed = Gallery()

    # g_ed.button("pager")
    # g_ed.image("pager")
    # g_ed.unlock("pager")

    # g_ed.button("lorong")
    # g_ed.image("lorong")
    # g_ed.unlock("lorong")

    # Button used for locked image

    # g_ed.locked_button = "bglock_button"

    # Transition used when switching images

    # g.transition = dissolve
    # g_ed.transition = dissolve    



    # Music
    mr = MusicRoom(fadeout=1.0)

    # Add Music files

    mr.add("audio/list_music/Run_Run_Run_(off_vocal).mp3", always_unlocked=True)
    mr.add("audio/list_music/eien_pressure.mp3", always_unlocked=True)
    mr.add("audio/list_music/oshibe.mp3", always_unlocked=True)



## Extras Navigation Screen

screen extras_navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        textbutton _("Characters") action ShowMenu("characters") alt "Characters"

        # textbutton _("Music List") action ShowMenu("music") alt "Music List"

        textbutton _("Gallery") action ShowMenu("bg_gallery") alt "Gallery"
        
        # textbutton _("Ending Unlocked") action ShowMenu("ed_gallery") alt "Ending Unlocked"

        textbutton _("Note For Marsha") action ShowMenu("catatan") alt "Notes"

        textbutton _("Return") action Return() alt "Return"


## Extras Menu Screen

screen extras_menu(title, scroll = None, yinitial = 0.0):
    style_prefix "game_menu"
    
    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude
    
    label title

    use extras_navigation

## About characters ################################################################
##
## This screen describe about characters in this games
## example of how to make a custom screen.

screen characters():
    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use extras_menu(_("Characters"), scroll="viewport"):

        style_prefix "characters"

        vbox:

            add "GC/profil_0.jpg" fit "contain"
            text _("\n")
            add "GC/profil_1.jpg" fit "contain"
            text _("\n")
            add "GC/profil_2.jpg" fit "contain"
            text _("\n")
            add "GC/profil_3.jpg" fit "contain"
            text _("\n")
            add "GC/profil_4.jpg" fit "contain"
            text _("\n")
            add "GC/profil_5.jpg" fit "contain"
            text _("\n")
            add "GC/profil_6.jpg" fit "contain"
            text _("\n")
            add "GC/profil_7.jpg" fit "contain"
            text _("\n")
            add "GC/profil_8.jpg" fit "contain"



style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

## Music List

screen music():

    tag menu

    use extras_menu(_("Music List")):

        vbox:

            xalign 0.5
            yalign 0.5

            # The buttons that play each track.

            textbutton "Run Run Run (Off Vocal)" action mr.Play("audio/list_music/Run_Run_Run_(off_vocal).mp3")
            textbutton "Eien Pressure (Off Vocal)" action mr.Play("audio/list_music/eien_pressure.mp3")
            textbutton "Oshibe to Meshibe to Yoru no ChouChou (Off Vocal)" action mr.Play("audio/list_music/oshibe.mp3")
            
            null height 20

            hbox:
            # Buttons that let us advance through tracks.
                textbutton "Previous" action mr.Previous() alt "Previous Song"
                textbutton "Next" action mr.Next() alt "Next Song"

            null height 20 

        # Start the music playing on entry to the music room.
        on "replace" action mr.Play()

        ## Restore the main menu music upon leaving.
        ## You can actually comment this out if you want to let players enjoy the music
        ## while looking at the other screens.
        # on "replaced" action Play("music", "audio/list_music/Run_Run_Run_(off_vocal).mp3")

# End Credit Scroll

# Credit ending scene

# Content of your credits screen
define credits_string = _p("""
{size=+50}{b}WGV: DreamCatcher{/b}{/size}

{size=+28}Production{/size}

Wargavi48
\n
{size=+10}Project Director{/size}

Nueks
\n
{size=+10}Project Manager{/size}

Koko Jon
\n
{size=+10}Lead Programmer{/size}

Tomato🔨🗿🔮🐿️🎨🅿️
\n
{size=+10}Programmer{/size}

Exilade

Koko Jon

Lima

Shota

Sunny🔆
\n
{size=+10}Lead Writer{/size}

Aergia

Addo

Fatimah

Lenkuass

Nueks

Rizka MD
\n
{size=+10}Co-Writer{/size}

Kodoknya Cepio

Koko Jon

Tomato🔨🗿🔮🐿️🎨🅿️

Tebtebo
\n
{size=+10}Quiz Maker{/size}

Kodoknya Cepio
\n
{size=+10}Characters{/size}

Lenkuass

Nueks

Yukisaki
\n
{size=+10}CG{/size}

Lenkuass
\n
{size=+10}Lead Backgrounds{/size}

BlueSky

Vhyrie
\n
{size=+10}Backgrounds{/size}

Awil

Hann

Pipigooro

Tebtebo
\n
{size=+10}Assets{/size}

Denden.zip

Nueks

Tebtebo
\n
{size=+10}UI Design{/size}

Heyysatsu

Exilade
\n
{size=+10}Logo{/size}

Ahsae
\n
{size=+10}Pia Minigame{/size}

Tebtebo
\n
{size=+10}Kana Minigame{/size}

Pipigooro
\n
{size=+10}Tana Minigame{/size}

Addo
\n
{size=+10}Opening Sound Track{/size}

HasbiLH

💖Rizuka Miku✨

Shiiyato
\n
{size=+10}Music Video{/size}

ElaDesuu

Galaxy

Kaizengraphic

Oxy Studio
\n
{size=+10}Music & Sound{/size}

BlackJckt

Copolatos

Kodoknya Cepio

Koko Jon

Lenkuass

Pipigooro

Tebtebo

Tomato🔨🗿🔮🐿️🎨🅿️
\n
{size=+10}Sponsors{/size}

Bangun Rama

Galaxy

Koko Jon

RG Hasan

Takamina

SAKU

Risqi Vodoo

Sadao Maou

RedAnt

Kodoknya Cepio

Kautsar AS

Addo

Sunny🔆

Vin

💖Rizuka Miku✨

Hanzfamz

Ta Ma

Farrel

Nakohayou

RidDhh

Panapajadah

AhSae

FZetaaa

Hmmmm

Rin
\n
{size=+10}Asset Background{/size}

{size=28}FREEPIK, Lifeforstock on Freepik, MrSiraphol on Freepik, Neeka.{/size}
\n
{size=+10}Background Music{/size}

{size=28}Ad-lib by ZUKISUZUKI, A Day Spent at a Cafe by NekoKimagure, Answer by ZUKISUZUKI, Chocolate Mint by Edamame88, Conjurer by Peritune, Cut The Wind by Shuki Yomrua, Daybreak by Peritune, Gentle Theme 1 by PeriTune, Gentle Theme 2 by PeriTune, Happy End by Kyatto, Holiday 2 by peritune, I Loved You by Yuuri, Koiwazurai by Sari, Laid Back 3 by Peritune, Let's Party 3 by Peritune, Nostalgic by Peritune, No Way by Peritune, Old Home by Noru, On The Gentle Wind by Shimtone, Parade by Sharo, Positive 2 by Peritune, Positive 4 by Peritune, Radiant Sunshine by Peritune, Recall by Sharo, Resort 4 by Peritune, Resort 5 by Peritune, RetroRoman Koharu by Peritune, Robot by Peritune, Scéal Réalta by Peritune, School Life by Maniira, Sky Blue Canvas by Yoshinori Tanaka, Shopping Mall by Imataku, Silver Bells at Dawn by Imataku, Smoked Quail Egg by Tanaka Tamago, Soft Day 2 by Peritune, Sugomori no Ritchi by MAKOOTO, Suspense 3 by Peritune, Toys Factory by Peritune, Train by Matsu, Violet by Sari, White Clover by Yuuki Wataru, Wind Feelings by Shimtone, Wish 2 by Peritune.{/size}
\n
{size=+10}Sound Effect{/size}

{size=28}Clock Alarm by Microsammy, CRASH 1 by Olenchic, David Gallie from Pixabay, Ftus Sound Effects, Jingle Retro Jazz 2 by Peritune, Jurij from Pixabay, PIXABAY, Qat from FreeSound, Rotich Wilson from Pixabay, SoundBiter, Soundsnap, Sound Laboratory, Universfield from Pixabay, U_z31mph1yzr from Pixabay.{/size}
\n
{size=+10}Special Thanks{/size}

All The Dreamcatcher Player & Warga Virtual 48

Ess_renpy_tutorials

Feniksdev.com

MarshaOshi

Tetsuoga
\n
{size=+30}Happy 1st Anniversary JKT48V{/size} 
\n
{size=+10}Made with Ren'Py{/size}

{size=+10}Thanks for Playing!{/size}\n\n\n\n
\n
{size=+10}Warga Virtual 48{/size} 
\n
{size=+10}Twitter{/size}

{size=+10}x.com/wargavirtual48{/size}

{size=+10}Discord{/size}

{size=+10}WARGAVI48{/size}

{size=+10}wargavi48.github.io/discord{/size}

{size=+10}Tiktok{/size}

{size=+10}tiktok.com/@wargavi48{/size}
{size=+10}{/size}

{size=+10}Youtube{/size}

{size=+10}youtube.com/@wargavi48{/size}
{size=+10}{/size}


{size=50}Disclaimer: This project is not affiliated in any way with JKT48 Operational Team or AKA Virtual. Any references to these entities are for contextual purposes only, and this project is independent and unaffiliated with them. The Migikata song in this game is a JKT48 song covered by Ranggapranendra. The copyright holder of the Migikata song in this game is JKT48.{/size}

{size=50}Penafian: Proyek ini tidak berafiliasi dengan Tim Operasional JKT48 maupun AKA Virtual. Segala referensi terhadap entitas-entitas tersebut hanya untuk keperluan kontekstual, dan proyek ini bersifat independen serta tidak memiliki hubungan dengan mereka. Lagu Migikata dalam game ini merupakan lagu JKT48 yang dicover oleh ranggapranendra. Pemegang hak cipta dari lagu Migikata dalam game ini adalah JKT48.{/size}


""")

# This controls the position and speed of your end credits
transform credits_scroll(t):
    xcenter 0.5 yanchor 0.0 ypos 1.0
    linear t yanchor 1.0 ypos 0.0

# The actual end credits screen that we call

screen credits(t):

    style_prefix "credits"

    # Ensure that the game_menu screens don't appear and interrupt the credits

    key "K_ESCAPE" action NullAction()
    key "K_MENU" action NullAction()
    key "mouseup_3" action NullAction()

    # If a player has sene the credits before, this button appears.

    if persistent.credits_seen:
        
        textbutton _("Skip End Credits") action Jump("skip_credits"):
            xalign 1.0 yalign 1.0

    # When t is up, the game will go to the next line.
    timer t action Return()
    # The contents of your credits screen is here.
    text credits_string text_align 0.5 at credits_scroll(t)

style credits_text:
    size gui.title_text_size
    color "#000000"

# Pesan untuk Marsha

screen catatan():

    tag menu

    ## This use statement includes the extras_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the extras_menu
    ## screen.
    use extras_menu(_("Note For Marsha"), scroll="viewport"):

        style_prefix "about"

        vbox:

            ## Your text goes here.
            if gui.dev_notes:
                text "[gui.dev_notes!t]\n"

## Type your special message here.
define gui.dev_notes = _p("""Halo Marsha, pertama-tama selamat ulang tahun ke-17. Happy sweet 17 yak. Cie udah bisa nyanyi lagu seventeen sekarang wkwkwk. Btw hadiah dari aku game ini aja ya, soalnya aku seneng bisa masuk bagian tim developer buat bikin game visual novel pertama MO ini.\n
Kalo ditanya susah apa gak ya... Susah-susah gampang tapi aku bawa seneng aja soalnya ilmu aku kepake juga dan bisa belajar banyak tentang bahasa pemrograman python ini. FYI kalo kamu mau kepo aja ya hehehe...\n
Bisa nyelesein game ini juga reward bagi anak-anak MO yang bener-bener khusus buat kamu. Kamu kalo mau ajak member-member lain juga boleh soalnya beberapa ada mereka juga di game ini. Walau gak semua yaaa...\n
Oh iya, kalo boleh jujur aku juga ngikutin kamu baru-baru ini loh Sha wkwkwkwk, jadi belom lama sebenernya. Masuk MO pun juga baru-baru ini juga.\n
Aku pun ganyangka juga bisa ikut bantu buat project STS sweet 17 kamu ini.\n
Mungkin itu dulu aja, kalo semisal dikasih kesempatan VC kita ketemu di VC aja yak!\n
-Tetsuoga-""")

screen bg_gallery():
    
    tag menu
    
    use extras_menu(_("Gallery"), scroll="viewport"):

        vbox:

            add "extra/pager_cr.jpg" fit "contain"
            text _("\n")
            add "extra/lorong_cr.jpg" fit "contain"
            text _("\n")
            add "extra/kelas_cr.jpg" fit "contain"
            text _("\n")
            add "extra/mall_cr.jpg" fit "contain"
            text _("\n")
            add "extra/kantin_cr.jpg" fit "contain"
            text _("\n")
            add "extra/kantor_kepsek_cr.jpg" fit "contain"
            text _("\n")
            add "extra/ruang_tamu_cr.jpg" fit "contain"
            text _("\n")
            # xalign 0.5
            # yalign 0.5
            # spacing 30

            # grid 1 7:
               
            #     add g.image("pager_cr", "pager_button", xalign=0.5, yalign=0.5)
            #     add g.image("lorong_cr", "lorong_button", xalign=0.5, yalign=0.5)
            #     add g.image("kantor_kepsek_cr", "kepsek_button", xalign=0.5, yalign=0.5)
            #     add g.image("kelas_cr", "kelas_button", xalign=0.5, yalign=0.5)
            #     add g.image("ruang_tamu_cr", "ruangtamu_button", xalign=0.5, yalign=0.5)
            #     add g.image("mall_cr", "mall_button", xalign=0.5, yalign=0.5)
            #     add g.image("kantin_cr", "kantin_button", xalign=0.5, yalign=0.5)

            #     spacing 15

            
            # textbutton "Return" action Return()

# screen ed_gallery:

#     tag menu
    
#     use extras_menu(_("Ending Unlocked"), scroll="viewport"):

#         vbox:
#             xalign 0.5
#             yalign 0.5
#             spacing 30

#             grid 2 2:

#                 add g.make_button("pager", "pager_button", xalign=0.5, yalign=0.5)
#                 add g.make_button("lorong", "lorong_button", xalign=0.5, yalign=0.5)
#                 add g.make_button("pager", "pager_button", xalign=0.5, yalign=0.5)
#                 add g.make_button("lorong", "lorong_button", xalign=0.5, yalign=0.5)

#                 spacing 15

            
            # textbutton "Return" action Return()