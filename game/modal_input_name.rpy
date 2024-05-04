transform confirmation_button:
    xpos 230
    ypos 125

transform confirmation_button_2:
    xpos 237
    ypos 205

transform input_position:
    xpos 180
    ypos 64

style input_name:
    color "#000"
    size 50

screen name_input(message, ok_action, output_var="player", characters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890  ", len = 10):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    # style_prefix "confirm"

    # add "gui/input_box.png"
    key "K_RETURN" action ok_action

    frame:
        background "gui/input_box.png"
        xalign 0.4
        yalign 0.5
        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                # style "confirm_prompt"
                xpos 200
                ypos 15
            
            # This is the line we change to use our new variables.
            input default "" value VariableInputValue(output_var) length len allow characters at input_position style "input_name"

            #hbox:
            #    xalign 0.5
            #    style_prefix "radio_pref"
            #    textbutton "Male" action NullAction()
            #    textbutton "Female" action NullAction()
            hbox:
                xalign 0.5
                spacing 100

                textbutton _("OK") action ok_action at confirmation_button

screen popup_message(message, ok_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    # style_prefix "confirm"

    key "K_RETURN" action ok_action

    frame:
        xalign 0.4
        yalign 0.45
        background "gui/input_box.png" 
        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                # style "confirm_prompt"
                xpos 200
                ypos 15
            
            # This is the line we change to use our new variables.
            # input default "" value VariableInputValue(output_var) length len allow characters

            #hbox:
            #    xalign 0.5
            #    style_prefix "radio_pref"
            #    textbutton "Male" action NullAction()
            #    textbutton "Female" action NullAction()
            hbox:
                xalign 0.5
                spacing 100

                textbutton _("OK") action ok_action at confirmation_button_2