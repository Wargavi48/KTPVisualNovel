################################################################################
## Inisialisasi
################################################################################

init offset = -1


################################################################################
## Gaya
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/custom_scroll_bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/custom_scroll_thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/custom_scroll_bar_vertical.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/custom_scroll_thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/custom_scroll_bar_1.png", gui.slider_borders, tile=gui.slider_tile) xsize 486
    thumb "gui/slider/custom_scroll_thumb_1.png" thumb_offset 18

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/custom_scroll_bar_vertical.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/custom_scroll_thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)




# animation menu
transform initial_menu:
    alpha 0.0
    pause 1.0
    ease 1.0 alpha 1.0


transform ktp_appear:
    alpha 0.0
    pause 2.0
    ease 1.0 alpha 1.0

transform overlay_appear:
    xoffset -100 alpha 0.0
    pause 3.0
    ease 1.0 xoffset 0 alpha 1.0

transform overlay_left:
    xoffset -100 alpha 0.0
    pause 3.0
    ease 1.0 xoffset 0 alpha 1.0

transform overlay_right:
    xoffset 1180 alpha 0.0
    pause 3.0
    ease 1.0 xoffset 770 alpha 1.0

transform start_menu:
    xoffset -100 alpha 0.0
    pause 4.3
    ease 0.3 xoffset 0 alpha 1.0

# transform achievement_menu:
#     yoffset 100 alpha 0.0
#     pause 4.6
#     ease 0.3 yoffset 0 alpha 1.0


transform load_menu:
    xoffset -100 alpha 0.0
    pause 4.6
    ease 0.3 xoffset 0 alpha 1.0


transform setting_menu:
    xoffset -100 alpha 0.0
    pause 4.9
    ease 0.3 xoffset 0 alpha 1.0

# transform about_menu:
#     yoffset 100 alpha 0.0
#     pause 5.5
#     ease 0.3 yoffset 0 alpha 1.0

transform help_menu:
    xoffset -100 alpha 0.0
    pause 5.2
    ease 0.3 xoffset 0 alpha 1.0

# transform help_menu:
#     yoffset 100 alpha 0.0
#     pause 5.8
#     ease 0.3 yoffset 0 alpha 1.0

transform quit_menu:
    xoffset -100 alpha 0.0
    pause 5.5
    ease 0.3 xoffset 0 alpha 1.0

transform fade_in:
    alpha 0.0
    linear 0.3 alpha 1.0

transform logo_game:
    zoom 2.0 alpha 0.0
    pause 5.8
    ease 1.0 zoom 1.0 alpha 1.0


# transform quit_menu:
#     yoffset 100 alpha 0.0
#     pause 6.2
#     ease 0.3 yoffset 0 alpha 1.0


################################################################################
## Layar In-game
################################################################################


## Layar Say ###################################################################
##
## Layar say di gunakan untuk menampilkan dialog kepada pemain. Ini menggunakan
## dua parameter, who dan what, yang merupakan nama karakter yang berbicara dan
## text yang akan di tampilkan, masing-masing. (Kedua parameter dapat berisi
## None jika tidak ada nama yang di berikan.
##
## Layar ini harus membuat text yang dapat di tampilkan dengan id "what", yang
## di mana Ren'Py menggunakan ini untuk mengatur tampilan text. Ini juga dapat
## membuat sesuatu yang dapat di tampilkan dengan id "who" dan id "window" untuk
## mengaplikasikan properti gaya.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window" 

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## Jika ada gambar di sisi, tampilkan di atas text. Jangan tampilkan di
    ## versi HP[Handphone)(Android) - Karena tidak ada ruang.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Buat namebox tersedia untuk mengatur gaya melalui objek karakter.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/dialog/custom_dialog_default.png", xalign=0.65,yalign=1.55)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xpos 65
    ypos -90
    size 35
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos 0.23
    xsize gui.dialogue_width
    ypos -30
    adjust_spacing False

## Layar masukkan/input ########################################################
##
## Layar ini di gunakan untuk menampilkan renpy.input. Parameter prompt
## digunakan untuk meneruskan text yang di prompt/minta.
##
## Layar ini harus membuat input yang dapat di tampilkan dengan id "input" untuk
## menerima berbagai parameter masukan.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width





## Layar Pilihan ###############################################################
##
## Layar ini digunakan untuk menampilkan pilihan dalam game yang disajikan oleh
## menu statement. Satu parameter, item, adalah daftar objek, masing-masing
## dengan bidang keterangan dan tindakan.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Layar Menu Cepat/Quick Menu #################################################
##
## Menu cepat ditampilkan dalam game untuk memudahkan akses ke menu di luar
## game.

screen quick_menu():

    ## Memastikan ini muncul di atas layar yang lain.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Kembali") action Rollback():
                yoffset -55
                xoffset -20
            textbutton _("Riwayat") action ShowMenu('history'):
                yoffset -55
                xoffset 10
            textbutton _("Lompati") action Skip() alternate Skip(fast=True, confirm=True):
                yoffset -55
                xoffset 40
            textbutton _("Otomatis") action Preference("auto-forward", "toggle"):
                yoffset -55
                xoffset 65
            textbutton _("Simpan") action ShowMenu('save'):
                yoffset -55
                xoffset 100
            textbutton _("Simpan.C") action QuickSave():
                yoffset -55
                xoffset 130
            textbutton _("Muat.C") action QuickLoad():
                yoffset -55
                xoffset 170
            textbutton _("Setting") action ShowMenu('preferences'):
                yoffset -55
                xoffset 220


## Kode ini memastikan layar quick_menu di tampilkan di dalam permainan,
## kapanpun player tidak secaralangsung menyembunyikan antarmuka.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Layar Menu Utama dan Menu Permainan
################################################################################

## Layar navigasi ##############################################################
##
## Layar ini di ikutsertakan di menu utama dan permainan, dan menyediakan
## navigasi ke menu lainnya, dan untuk memulai permainan.

#screen navigation():

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## Layar Menu utama ############################################################
##
## Digunakan untuk menampilkan menu utama ketika Ren'Py dimulai.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## Ini Memastikan Layar Menu Yang Lain Telah Di Timpa
    tag menu
    add "white"
    add gui.main_menu_background at initial_menu
    add "screens/Tono.png" at ktp_appear
    add "screens/Pia.png" at ktp_appear
    add "screens/Kana.png" at ktp_appear
    add "screens/kabut_kiri.png" at overlay_left
    #add "screens/kabut_kanan.png" at overlay_right
    add "gui/Logo_VN_KTP_re.png":
        at logo_game
        #zoom 1.5
        ypos 78
        xpos 16

    # add "gui/overlay/side_bar_menu.png" at overlay_appear
    ## Frame kosong ini menggelap di menu utama.
    frame:
        style "main_menu_frame"

    ## Pernyataan 'use' mengikutsertakan layar lain ke layar ini. Isi sebenarnya
    ## dari menu utama adalah layar navigasi.
    #use navigation

    fixed:
        style_prefix "navigation"

        # xpos gui.navigation_xpos
        # xalign 0.5
        # yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            #textbutton _("Start") action Start():
    
            imagebutton auto "gui/menu/mm_start_%s.png" xpos 0 ypos 260 focus_mask True action Start() hovered [ Play("sound","audio/click.wav") ] at start_menu

            # if renpy.get_screen("main_menu"):
            # at start_menu
            # text_color "#000000"
            # text_hover_color "#FF7700"
            # ypos -100
            # ypos 0
            # background "gui/main_menu_button.png"
            # text_xpos 120

            # textbutton _("Achievements") action ShowMenu("achievement_gallery"):
            #     if renpy.get_screen("main_menu"):
            #         at achievement_menu
            #         text_color "#000000" 
            #         text_hover_color "#FF7700"
            #         ypos -100
            #         background "gui/main_menu_button.png"
            #         text_xpos 50

        else:

            textbutton _("History") action ShowMenu("history") background None

            textbutton _("Save") action ShowMenu("save") background None


        #textbutton _("Load") action ShowMenu("load"):

        imagebutton auto "gui/menu/mm_load_%s.png" xpos 0 ypos 375 focus_mask True action ShowMenu("load") hovered [ Play("sound","audio/click.wav") ] at load_menu

            #if renpy.get_screen("main_menu"):
                #at load_menu
                #text_color "#000000"
                #text_hover_color "#FF7700"
                #ypos -50
                # ypos 50
                #background "gui/main_menu_button.png"
                #text_xpos 130

        #textbutton _("Setting") action ShowMenu("preferences"):

        imagebutton auto "gui/menu/mm_config_%s.png" xpos 0 ypos 490 focus_mask True action ShowMenu("preferences") hovered [ Play("sound","audio/click.wav") ] at setting_menu

            #if renpy.get_screen("main_menu"):
                #at setting_menu
                #text_color "#000000"
                #text_hover_color "#FF7700"
                #ypos 0
                # ypos 100
                #background "gui/main_menu_button.png"
                #text_xpos 110


        #if _in_replay:

            #textbutton _("Akhiri Replay") action EndReplay(confirm=True)

        #elif not main_menu:

            #textbutton _("Main Menu") action MainMenu()

        # textbutton _("About") action ShowMenu("about"):
        #     if renpy.get_screen("main_menu"):
        #         at about_menu
        #         text_color "#000000"
        #         text_hover_color "#FF7700" 
        #         ypos 50
        #         background "gui/main_menu_button.png"
        #         text_xpos 120

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Bantuan tidak perlu atau relevan dengan perangkat mobile.
            # Harusnya dibawah ini help sementara ganti jadi extras dulu
            # textbutton _("Extras") action ShowMenu("extras"):
            # textbutton _("Extras") action ShowMenu("help"):
                imagebutton auto "gui/menu/mm_extra_%s.png" xpos 0 ypos 605 focus_mask True action ShowMenu("gallery_a") hovered [ Play("sound","audio/click.wav") ] at help_menu
                #if renpy.get_screen("main_menu"):
                    #at help_menu
                    #text_color "#000000"
                    #text_hover_color "#FF7700" 
                    #ypos 50
                    # ypos 150
                    #background "gui/main_menu_button.png"
                    #text_xpos 100

        if renpy.variant("pc"):

            ## Tombol keluar dilarang di iOS dan tidak diperlukan di Android dan
            ## Web.
            #textbutton _("Quit Game") action Quit(confirm=not main_menu):

            imagebutton auto "gui/menu/mm_exit_%s.png" xpos 0 ypos 720 focus_mask True action Show("confirm_quit") hovered [ Play("sound","audio/click.wav") ] at quit_menu

                #if renpy.get_screen("main_menu"):
                    #at quit_menu
                    #text_color "#000000"
                    #text_hover_color "#FF7700"
                    #ypos 100
                    # ypos 200
                    #background "gui/main_menu_button.png"
                    #text_xpos 80

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    # background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")

## layar Confirm Exit ########################################################
##

screen confirm_quit():
        modal True
        zorder 100

        # Background for the confirmation screen (optional)
        add "gui/menu/end_c.png" at fade_in
        # Centered buttons for confirm and cancel
        
        fixed:

            # Confirm button
            imagebutton auto "gui/menu/x_yes_%s.png" xpos 648 ypos 503 action Quit(confirm=False) focus_mask True hovered [ Play("sound","audio/click.wav") ] at fade_in

            # Cancel button
            imagebutton auto "gui/menu/x_no_%s.png" xpos 982 ypos 503 action Hide("confirm_quit") focus_mask True hovered [ Play("sound","audio/click.wav") ] at fade_in

## layar Menu Permainan ########################################################
##
## Ini menjalaskan struktur dasar yang paling sering di gunakan di layar menu
## permainan, ini ditampilkan beserta layar judul, dan menampilkan latar
## belakang,judul,dan navigasi.
##
## Parameter scroll dapat berisi 'None', atau "viewport" dan "vpgrid". Layar
## ini di maksudkan untuk di gunakan dengan cabang satu atau lebih, yang di
## tempatkan di dalamnya.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background 
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Memesan tempat untuk bagian navigasi.
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
                            spacing spacing

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

                        spacing spacing

                        transclude

                else:

                    transclude

    #use navigation

    textbutton _("Kembali"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "screens/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## Layar About #################################################################
##
## Layar ini menampilkan credit dan informasi copyright tentang game dan Ren.Py.
##
## Tidak ada yang spesial dengan layar ini, semenjak ini juga berperan sebagai
## contoh bagaimana membuat layar custom.

screen about():

    tag menu

    ## Pernyataan 'use' ini mengikutsertakan layar game_menu ke dalam layar ini.
    ## Percabangan vbox lalu di ikutsertakan kedalam viewport di dalam layar
    ## game_menu.
    use game_menu(_("Tentang"), scroll="viewport"):

        style_prefix "about"

        vbox:

            ## gui.about biasanya di set di options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("{color=#ff7700}WGV : Dreamcatcher{/color} {color=#fff}adalah sebuah permainan yang dibuat oleh Wargavi. Rasakan pengalaman yang luar biasa dalam perjalanan ini, yang penuh dengan tantangan, kenangan, dan cinta untuk JKT48V. Mari bergembira bersama kami{/color}")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Layar Load and Save #########################################################
##
## Layar ini bertanggungjawab untuk mengijinkan pemain menyimpan dan
## meload lagi. Semenjak mereke hampir memiliki hal yang sama, keduanya di
## implementasinan di percabangan layar ketiga, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Simpan"))


screen load():

    tag menu

    use file_slots(_("Muat"))


screen file_slots(title):
    add "images/save/bg_save.png"
    imagebutton auto "gui/button/back_ico_%s.png" xpos 40 ypos 1010 focus_mask True action Return()
    
    vbox:
        xalign 0.5
        yalign 0.5
        grid 4 3:
            xspacing 49
            yspacing 16
            for i in range(12):
                $slot = i+1
                frame:
                    xsize 373
                    ysize 265  
                    background Frame("images/save/save_frame.png")

                    fixed:
                            xpos 43
                            ypos 55
                            add FileScreenshot(slot) at Transform(xsize=280, ysize=150)
                    button:
                        xalign 0.5
                        yalign 0.5
                        action FileAction(slot)
                        has vbox

                        text FileTime(slot, format=_("{#file_time}%a, %b %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"
                            yoffset 110
                        text FileSaveName(slot):
                            style "slot_name_text"
    
    fixed:
        xalign 1.0
        yalign 1.0

        if config.has_autosave:
            imagebutton auto "images/save/auto_%s.png" xpos 792 ypos 990 action FilePage("auto")
        
        if config.has_quicksave:
            imagebutton auto "images/save/quick_%s.png" xpos 1042 ypos 990 action FilePage("quick")

        # Loop untuk 2 halaman dengan imagebutton
        for page in range(1, 3):
            imagebutton auto "images/save/page_1_%s.png" xpos 1302 ypos 990 action FilePage(1)
            imagebutton auto "images/save/page_2_%s.png" xpos 1391 ypos 990 action FilePage(2)
            imagebutton auto "images/save/page_3_%s.png" xpos 1480 ypos 990 action FilePage(3) 



    default page_name_value = FilePageNameInputValue(pattern=_("Halaman {}"), auto=_("Otomatis save"), quick=_("Save cepat"))

    #use game_menu(title):

        #fixed:

            ## Ini memastikan input akan mendapat event masuk sebelum tombol
            ## lainnya.
            #order_reverse True

            ## Nama halaman, yang dapat di edit dengan mengklik tombol.
            #button:
                #style "page_label"

                #key_events True
                #xalign 0.5
                #action page_name_value.Toggle()

                #input:
                    #style "page_label_text"
                    #value page_name_value

            ## Kolom slot file.
            #grid gui.file_slot_cols gui.file_slot_rows:
                #style_prefix "slot"

                #xalign 0.5
                #yalign 0.5

                #spacing gui.slot_spacing

                #for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    #$ slot = i + 1

                    #button:
                        #action FileAction(slot)

                        #has vbox

                        #add FileScreenshot(slot) xalign 0.5

                        #text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("Slot Kosong")):
                            #style "slot_time_text"

                        #text FileSaveName(slot):
                            #style "slot_name_text"

                        #key "save_delete" action FileDelete(slot)

            ## Tombol untuk mengakses halaman lain.
            #vbox:
                #style_prefix "page"

                #xalign 0.5
                #yalign 1.0

                #hbox:
                    #xalign 0.5

                    #spacing gui.page_spacing

                    #textbutton _("<") action FilePagePrevious()

                    #if config.has_autosave:
                        #textbutton _("{#auto_page}O") action FilePage("auto")

                    #if config.has_quicksave:
                        #textbutton _("{#quick_page}C") action FilePage("quick")

                    ## antara(1,10) beri nomor antara 1 sampai 9.
                    #for page in range(1, 10):
                        #textbutton "[page]" action FilePage(page)

                    #textbutton _(">") action FilePageNext()

                #if config.has_sync:
                    #if CurrentScreenName() == "save":
                        #textbutton _("Sinkronisasi Unggah"):
                            #action UploadSync()
                            #xalign 0.5
                    #else:
                        #textbutton _("Unduh Sinkronisasi"):
                            #action DownloadSync()
                            #xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Layar preferensi/opsi #######################################################
##
## Layar preferensi mengijinkan pemain untuk mengkonfigurasi permainan untuk
## menyesuaikan gaya bermain masing masing individu.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences


screen extras():
    tag menu
    #if main_menu:
        #add gui.main_menu_background 
    #else:
        #add gui.game_menu_background
        
    #frame:
        #style "game_menu_outer_frame"
        #vbox:
            #style_prefix "navigation"

            #xpos gui.navigation_xpos
            # xalign 0.5
            #ypos 140

            #spacing gui.navigation_spacing
            #label "{size=+20}Extras{/size}":
                #ypos -200
            #textbutton _("Achievement") action ShowMenu("achievement_gallery")
            #textbutton _("Gallery") action ShowMenu("gallery_a")
            #textbutton _("Kembali") action Return()

                

screen preferences():

    tag menu

    #use game_menu(_("Setting"), scroll="viewport"):

    viewport:
        draggable False
        mousewheel False

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    fixed:
                        # background Frame("gui/custom_setting_frame.png",0,0,0,0)
                        # xysize (750,150)
                        # has hbox
                        #style_prefix "radio"

                        add "gui/config/con_bg.png"
                        add "gui/config/con_display.png" xpos 550 ypos 219
                        imagebutton auto "gui/config/con_win_%s.png" xpos 303 ypos 301 focus_mask True action Preference("display", "window")
                        imagebutton auto "gui/config/con_full_%s.png"xpos 663 ypos 301 focus_mask True action Preference("display", "fullscreen")

                        add "gui/config/con_skip.png" xpos 592 ypos 397
                        imagebutton auto "gui/config/con_uns_%s.png" xpos 303 ypos 478 focus_mask True action Preference("skip", "toggle")
                        imagebutton auto "gui/config/con_aft_%s.png" xpos 663 ypos 478 focus_mask True action Preference("after choices", "toggle")

                        imagebutton auto "gui/button/back_ico_%s.png" xpos 40 ypos 1010 focus_mask True action Return()
                        imagebutton auto "gui/button/save_ico_%s.png" xpos 635 ypos 990 focus_mask True action ShowMenu('save')
                        imagebutton auto "gui/button/load_ico_%s.png" xpos 865 ypos 990 focus_mask True action ShowMenu('load')
                        imagebutton auto "gui/button/title_ico_%s.png" xpos 1095 ypos 990 focus_mask True action MainMenu()
                        imagebutton auto "gui/button/exit_ico_%s.png" xpos 1315 ypos 990 focus_mask True action Show("confirm_quit")

                        imagebutton auto "gui/button/ach_ico_%s.png" xpos 383 ypos 990 action ShowMenu("achievement_gallery")
                
                        hbox:
                            style_prefix "slider"
                            box_wrap True

                            vbox:

                                add "gui/config/kecepatan_text.png" xpos 417 ypos 627

                                bar value Preference("text speed") xpos 417 ypos 647

                                add "gui/config/waktu_otomatis_maju.png" xpos 417 ypos 667

                                bar value Preference("auto-forward time") xpos 417 ypos 687

                                if config.has_music:
                                    add "gui/config/volume_musik.png" xpos 1150 ypos 200
                                    

                                    hbox:
                                        bar value Preference("music volume") xpos 1134 ypos 230

                                if config.has_sound:

                                    add "gui/config/volume_suara.png" xpos 1150 ypos 260

                                    hbox:
                                        bar value Preference("sound volume") xpos 1134 ypos 290


                                if config.has_voice:
                                    add "gui/config/volume_vokal.png" xpos 1150 ypos 320

                                    hbox:
                                        bar value Preference("voice volume") xpos 1134 ypos 350

                                    add "gui/config/senyapkan.png" xpos 1150 ypos 380
                                    imagebutton auto "gui/config/con_mute_%s.png" xpos 1550 ypos 320 focus_mask True action Preference("all mute", "toggle") style "mute_all_button"
                    
        #vbox:
           
            #bar value Preference("text speed")
                        #add "gui/config/waktu_otomatis_maju.png" xpos 550 ypos 219
                        #bar value Preference("auto-forward time")
                        #null height (4 * gui.pref_spacing)

                    #if config.has_music:
                        #add "gui/config/con_display.png" xpos 1163 ypos 352
                        #bar value Preference("sound volume")



                #vbox:
                    #style_prefix "check"
                    #label _("Skip")
                    #textbutton _("Unseen Text") action Preference("skip", "toggle")
                    #textbutton _("After Choice") action Preference("after choices", "toggle")
                    # textbutton _("Transisi") action InvertSelected(Preference("transitions", "toggle"))

                ## Tipe tambahan vboxes "radio_pref" atau "check_pref" dapat di
                ## tambahkan disini, untuk menambahkan tambahan preferensi yang
                ## dibuat creator.

            #null height (4 * gui.pref_spacing)

            #hbox:
                #style_prefix "slider"
                #box_wrap True

                #vbox:

                    #label _("Kecepatan Text")

                    #bar value Preference("text speed")

                    #label _("Waktu Otomatis-Maju")

                    #bar value Preference("auto-forward time")

                #vbox:

                    #if config.has_music:
                        #label _("Volume Musik")

                        #hbox:
                            #bar value Preference("music volume")

                    #if config.has_sound:

                        #label _("Volume Suara")

                        #hbox:
                            #bar value Preference("sound volume")

                            #if config.sample_sound:
                                #textbutton _("Tes") action Play("sound", config.sample_sound)


                    #if config.has_voice:
                        #label _("Volume Vokal")

                        #hbox:
                            #bar value Preference("voice volume")

                            #if config.sample_voice:
                                #textbutton _("Tes") action Play("voice", config.sample_voice)

                    #if config.has_music or config.has_sound or config.has_voice:
                        #null height gui.pref_spacing

                        #textbutton _("Senyapkan Semua"):
                            #action Preference("all mute", "toggle")
                            #style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing


style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## Layar Riwayat ###############################################################
##
## Layar yang menampilkan History dialog kepada pemain. Semenjak tidak ada yang
## spesial tentang layar ini, ini memiliki akses ke history dialog yang di
## simpan di _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Hindari mempredisi layar ini, ini dapat berukuran sangat besar.
    predict False

    use game_menu(_("Riwayat"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## Ini menampilkan layar secara semestinya jika history_height
                ## memiliki value None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Mengambil warna dari text 'who' dari karakter, jika
                        ## di set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("Riwayat dialog kosong.")


## Ini menentukan tag apa yang diizinkan ditampilkan di layar sejarah/catatan.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Layar Bantuan ###############################################################
##
## Layar yang memberikan informasi tentang keyboard dan mouse binding. Ini
## menggunakan layar lain (keyboard_help, mouse_help, and gamepad_help) untuk
## menampilkan bantuan yang sebenarnya.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Bantuan"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Papanketik") action SetScreenVariable("device", "keyboard")
                textbutton _("Tetikus") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Masukkan")
        text _("Dialog tingkat lanjut dan mengaktifkan antarmuka.")

    hbox:
        label _("Spasi")
        text _("Dialog tingkat lanjut tanpa memilih pilihan.")

    hbox:
        label _("Tombol Panah")
        text _("Navigasi di antarmuka")

    hbox:
        label _("Melarikan diri")
        text _("Akses menu permainan.")

    hbox:
        label _("Ctrl")
        text _("Lompati dialog ketika di tahan.")

    hbox:
        label _("Tab")
        text _("Nyala/Matikan lompati dialog.")

    hbox:
        label _("Halaman Atas")
        text _("Putar mundur ke dialog sebelumnya.")

    hbox:
        label _("Page Down")
        text _("Putar maju ke dialog berikut.")

    hbox:
        label "H"
        text _("Sembunyikan antarmuka.")

    hbox:
        label "S"
        text _("Ambiil tangkapan layar.")

    hbox:
        label "V"
        text _("Nyalakan assisten {a=https://www.renpy.org/l/voicing}suara-sendiri{/a}")

    hbox:
        label "Shift+A"
        text _("Membuka menu aksesibilitas.")


screen mouse_help():

    hbox:
        label _("Klik Kiri")
        text _("Dialog tingkat lanjut dan mengaktifkan antarmuka.")

    hbox:
        label _("Klik Tengah")
        text _("Sembunyikan antarmuka.")

    hbox:
        label _("Klik Kanan")
        text _("Akses menu permainan.")

    hbox:
        label _("Roda Mouse Atas")
        text _("Putar mundur ke dialog sebelumnya.")

    hbox:
        label _("Roda Mouse Bawah")
        text _("Putar maju ke dialog berikut.")


screen gamepad_help():

    hbox:
        label _("Trigger Kanan\nA/Tombol Bawah")
        text _("Dialog tingkat lanjut dan mengaktifkan antarmuka.")

    hbox:
        label _("Trigger Kiri\nBahu Kiri")
        text _("Putar mundur ke dialog sebelumnya.")

    hbox:
        label _("Pundak Kanan")
        text _("Putar maju ke dialog berikut.")

    hbox:
        label _("D-Pad, Stick")
        text _("Navigasi di antarmuka")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Akses menu permainan.")

    hbox:
        label _("Y/Tombol Atas")
        text _("Sembunyikan antarmuka.")

    textbutton _("Kalibrasi") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Layar Tambahan
################################################################################


## Layar konfirmasi ############################################################
##
## Layar konfirmasi di panggil ketika Ren'Py mau menanyakan ke pemain pertanyaan
## ya atau tidak.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Memastikan layar lain tidak mendapatkan input ketika layar ini di
    ## panggil.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                imagebutton auto "gui/c_ya_%s.png" xpos -10 ypos 5 focus_mask True action yes_action 
                imagebutton auto "gui/c_tidak_%s.png" xpos -10 ypos 5 focus_mask True action no_action 

    ## Klik kanan dan jawaban escape "Tidak".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/Custom_Confirm.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style achievement_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5
    color "#FFF"

style confirm_prompt_text:
    ypos 20
    layout "subtitle"
    color "#000"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")
    xpos 70
    color "#FFFFFF"
    hover_color "#ff7700"

## Lompati indikator layar #####################################################
##
## layar skip_indicator di tampilkan untuk mengindikasian proses skipping sedang
## dalam proses.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Melompati")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## transform digunakan untuk mengkedipkan panah setelah yang lain.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## Kami harus menggunakan font yang mempunyai glyph BLACK RIGHT-POINTING
    ## SMALL TRIANGLE didalamnya.
    font "DejaVuSans.ttf"


## Layar pemberitahuan #########################################################
##
## layar notify digunakan untuk menampilkan pesan kepada pemain. (Seperti,
## ketika game di simpan cepat atau screenshot di ambil.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## Layar NVL ###################################################################
##
## Layar ini digunakan untuk dialog dan menu mode-NVL.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    #### ADD THIS TO MAKE THE PHONE WORK!! :) ###
    if nvl_mode == "phone":
        use PhoneDialogue(dialogue, items)
    else:
    ####
    ## Indent the rest of the screen
        window:
            style "nvl_window"

            has vbox:
                spacing gui.nvl_spacing

            ## Displays dialogue in either a vpgrid or the vbox.
            if gui.nvl_height:

                vpgrid:
                    cols 1
                    yinitial 1.0

                    use nvl_dialogue(dialogue)

            else:

                use nvl_dialogue(dialogue)

            ## Displays the menu, if given. The menu may be displayed incorrectly if
            ## config.narrator_menu is set to True, as it is above.
            for i in items:

                textbutton i.caption:
                    action i.action
                    style "nvl_button"

        add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## Ini mengendalikan angka maksimum entri mode-NVL yang dapat di tampilkan
## sekaligus.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Layar gelembung #############################################################
##
## Layar gelembung digunakan untuk menampilkan dialog kepada pemain saat
## menggunakan gelembung ucapan. Layar gelembung mengambil parameter yang sama
## dengan layar ucapkan, harus membuat tampilan dengan id "apa", dan dapat
## membuat tampilan dengan id "kotak nama", "siapa", dan "jendela".
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Versi Mobile(HP/Handphone/Android)
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Semenjak mouse tidak ada, kami mengganti menu cepat dengan yang menggunakan
## tombol yang lebih besar dan sedikit, yang memudahkan untuk di sentuh.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Kembali") action Rollback()
            textbutton _("Lompati") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Otomatis") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/side_bar_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
