init python:
    import random
    def corkGunTransform(t, st, at):
        global cork_gun_pos
        global cork_gun_size

        mousepos = renpy.get_mouse_pos()

        if mousepos[0] - cork_gun_size[0] / 2 <= config.screen_width - cork_gun_size[0] and mousepos[0] >= cork_gun_size[0] / 2:
            cork_gun_pos = (int(mousepos[0] - cork_gun_size[0] / 2), cork_gun_opos[1])

        t.xpos = cork_gun_pos[0]
        cork_gun_pos = (cork_gun_pos[0], cork_gun_opos[1] + int((mousepos[1] - config.screen_height / 2) / 7))

        t.ypos = cork_gun_pos[1]

        return 0

    def setupTargets():
        target_start_x = 400
        target_row_1_y = 210
        target_row_2_y = 500
        target_row_3_y = 775
        target_spacing = 100
        target_down_time = (0.0, 2.0)
        target_up_time = 2.0

        current_column = 0
        for i in range(12):
            if i < 3:
                target_transform = Transform(child = "images/shooting_game/target-1-4.png", zoom = target_row_1_zoom)
                target_sprites.append(target_SM.create(target_transform))
                target_sprites[-1].row = 1
                target_sprites[-1].down_time = random.uniform(target_down_time[0], target_down_time[1])
                target_sprites[-1].x = target_start_x + (target_sizes["top"][0] * i) + (target_spacing * i)
                target_sprites[-1].y = target_row_1_y
            elif i < 7:
                target_transform = Transform(child = "images/shooting_game/target-1-4.png", zoom = target_row_2_zoom)
                target_sprites.append(target_SM.create(target_transform))
                target_sprites[-1].row = 2
                target_sprites[-1].down_time = random.uniform(target_down_time[0], target_down_time[1])
                target_sprites[-1].x = target_start_x + (target_sizes["middle"][0] * current_column) + (target_spacing * current_column)
                target_sprites[-1].y = target_row_2_y
                current_column += 1
            elif i < 12:
                target_transform = Transform(child = "images/shooting_game/target-1-4.png", zoom = target_row_3_zoom)
                target_sprites.append(target_SM.create(target_transform))
                target_sprites[-1].row = 3
                target_sprites[-1].down_time = random.uniform(target_down_time[0], target_down_time[1])
                if i == 7:
                    current_column = 0
                else:
                    current_column += 1
                target_sprites[-1].x = target_start_x + (target_sizes["bottom"][0] * current_column) + (target_spacing * current_column)
                target_sprites[-1].y = target_row_3_y

            target_sprites[-1].idle_animation_direction = "up"
            target_sprites[-1].current_frame = 5
            target_sprites[-1].animation_time = 0.0
            target_sprites[-1].hit = False
            target_sprites[-1].up_time = target_up_time

    def targetUpdate(st):
        for li, target in enumerate(target_sprites):
            if target.hit == True:
                if target.current_frame == 1:
                    i = Image("images/shooting_game/target-1-2.png")
                    if target.row == 1:
                        target.animation_time = 0
                        t = Transform(child = i, zoom = target_row_1_zoom)
                    elif target.row == 2:
                        t = Transform(child = i, zoom = target_row_2_zoom)
                    elif target.row == 3:
                        t = Transform(child = i, zoom = target_row_3_zoom)
                    target.current_frame = 2
                    target.set_child(t)
                elif target.current_frame == 2:
                    i = Image("images/shooting_game/target-1-3.png")
                    if target.row == 1:
                        t = Transform(child = i, zoom = target_row_1_zoom)
                    elif target.row == 2:
                        t = Transform(child = i, zoom = target_row_2_zoom)
                    elif target.row == 3:
                        t = Transform(child = i, zoom = target_row_3_zoom)
                    target.current_frame = 3
                    target.set_child(t)
                elif target.current_frame == 3 and target.animation_time >= 0.1:
                    i = Image("images/shooting_game/target-1-4.png")
                    if target.row == 1:
                        t = Transform(child = i, zoom = target_row_1_zoom)
                    elif target.row == 2:
                        t = Transform(child = i, zoom = target_row_2_zoom)
                    elif target.row == 3:
                        t = Transform(child = i, zoom = target_row_3_zoom)
                    target.current_frame = 4
                    target.set_child(t)
                elif target.current_frame == 4 and target.animation_time >= 0.12:
                    i = Image("images/shooting_game/target-1-3.png")
                    if target.row == 1:
                        t = Transform(child = i, zoom = target_row_1_zoom)
                    elif target.row == 2:
                        t = Transform(child = i, zoom = target_row_2_zoom)
                    elif target.row == 3:
                        t = Transform(child = i, zoom = target_row_3_zoom)
                    target.current_frame = 5
                    target.set_child(t)
                elif target.current_frame == 5 and target.animation_time >= 0.13:
                    i = Image("images/shooting_game/target-1-4.png")
                    if target.row == 1:
                        t = Transform(child = i, zoom = target_row_1_zoom)
                    elif target.row == 2:
                        t = Transform(child = i, zoom = target_row_2_zoom)
                    elif target.row == 3:
                        t = Transform(child = i, zoom = target_row_3_zoom)
                    target.current_frame = 5
                    target.animation_time = 0
                    target.hit = False
                    target.set_child(t)
            else:
                if target.idle_animation_direction == "up":
                    if target.animation_time >= target.down_time:
                        if target.current_frame == 5:
                            i = Image("images/shooting_game/target-1-3.png")
                            if target.row == 1:
                                t = Transform(child = i, zoom = target_row_1_zoom)
                            elif target.row == 2:
                                t = Transform(child = i, zoom = target_row_2_zoom)
                            elif target.row == 3:
                                t = Transform(child = i, zoom = target_row_3_zoom)
                            target.current_frame = 3
                            target.set_child(t)
                        elif target.current_frame == 3 and target.animation_time >= target.down_time + 0.1:
                            i = Image("images/shooting_game/target-1-2.png")
                            if target.row == 1:
                                t = Transform(child = i, zoom = target_row_1_zoom)
                            elif target.row == 2:
                                t = Transform(child = i, zoom = target_row_2_zoom)
                            elif target.row == 3:
                                t = Transform(child = i, zoom = target_row_3_zoom)
                            target.current_frame = 2
                            target.set_child(t)
                        elif target.current_frame == 2 and target.animation_time >= target.down_time + 0.12:
                            i = Image("images/shooting_game/target-1-1.png")
                            if target.row == 1:
                                t = Transform(child = i, zoom = target_row_1_zoom)
                            elif target.row == 2:
                                t = Transform(child = i, zoom = target_row_2_zoom)
                            elif target.row == 3:
                                t = Transform(child = i, zoom = target_row_3_zoom)
                            target.current_frame = 1
                            target.idle_animation_direction = "down"
                            target.animation_time = 0
                            target.set_child(t)
                elif target.idle_animation_direction == "down":
                    if target.animation_time >= target.up_time:
                        if target.current_frame == 1:
                            i = Image("images/shooting_game/target-1-2.png")
                            if target.row == 1:
                                t = Transform(child = i, zoom = target_row_1_zoom)
                            elif target.row == 2:
                                t = Transform(child = i, zoom = target_row_2_zoom)
                            elif target.row == 3:
                                t = Transform(child = i, zoom = target_row_3_zoom)
                            target.current_frame = 2
                            target.set_child(t)
                        elif target.current_frame == 2:
                            i = Image("images/shooting_game/target-1-3.png")
                            if target.row == 1:
                                t = Transform(child = i, zoom = target_row_1_zoom)
                            elif target.row == 2:
                                t = Transform(child = i, zoom = target_row_2_zoom)
                            elif target.row == 3:
                                t = Transform(child = i, zoom = target_row_3_zoom)
                            target.current_frame = 3
                            target.set_child(t)
                        elif target.current_frame == 3 and target.animation_time >= target.up_time + 0.1:
                            i = Image("images/shooting_game/target-1-4.png")
                            if target.row == 1:
                                t = Transform(child = i, zoom = target_row_1_zoom)
                            elif target.row == 2:
                                t = Transform(child = i, zoom = target_row_2_zoom)
                            elif target.row == 3:
                                t = Transform(child = i, zoom = target_row_3_zoom)
                            target.current_frame = 4
                            target.set_child(t)
                        elif target.current_frame == 4 and target.animation_time >= target.up_time + 0.12:
                            i = Image("images/shooting_game/target-1-3.png")
                            if target.row == 1:
                                t = Transform(child = i, zoom = target_row_1_zoom)
                            elif target.row == 2:
                                t = Transform(child = i, zoom = target_row_2_zoom)
                            elif target.row == 3:
                                t = Transform(child = i, zoom = target_row_3_zoom)
                            target.current_frame = 5
                            target.set_child(t)
                        elif target.current_frame == 5 and target.animation_time >= target.up_time + 0.13:
                            i = Image("images/shooting_game/target-1-4.png")
                            if target.row == 1:
                                t = Transform(child = i, zoom = target_row_1_zoom)
                            elif target.row == 2:
                                t = Transform(child = i, zoom = target_row_2_zoom)
                            elif target.row == 3:
                                t = Transform(child = i, zoom = target_row_3_zoom)
                            target.current_frame = 5
                            target.idle_animation_direction = "up"
                            target.animation_time = 0
                            target.hit = False
                            target.set_child(t)

            target.animation_time += 0.01

        return 0

    def corkEvents(event, x, y, st):
        if event.type == renpy.pygame_sdl2.MOUSEBUTTONUP:
            if event.button == 1 and y < config.screen_height - 140:
                renpy.sound.play("audio/fire.mp3")
                cork_sprites.append(cork_SM.create(cork_transform))
                cork_sprites[-1].original_size = (110 / 2, 138 / 2)
                cork_sprites[-1].x = cork_gun_pos[0] + cork_sprites[-1].original_size[0]
                cork_sprites[-1].y = cork_gun_pos[1]
                cork_sprites[-1].original_pos = (cork_sprites[-1].x, cork_sprites[-1].y)
                cork_sprites[-1].zoom = 0.5
                cork_sprites[-1].move_to_pos = (cork_gun_pos[0], y)
                cork_SM.redraw(0)

    def corkUpdate(st):
        global score
        for cork in cork_sprites:
            if cork.y > cork.move_to_pos[1]:
                cork.y -= abs(cork.move_to_pos[1] - cork.original_pos[1]) / 15
                t = Transform(child = cork_image)
                cork.zoom -= 0.023
                cork.x += 1.2
                cork.original_size = (cork.original_size[0] * cork.zoom, cork.original_size[1] * cork.zoom)
                t.zoom = cork.zoom
                t.update()
                cork.set_child(t)
            else:
                for i, target in enumerate(target_sprites):
                    if target.row == 1:
                        if target.current_frame == 1 and target.x <= (cork.x - cork.original_size[0] / 2) <= (target.x + target_sizes["top"][0]) and target.y <= (cork.y - cork.original_size[1] / 2) <= (target.y + target_sizes["top"][1]) - 30:
                            target.hit = True
                            score += 5
                            renpy.sound.play("audio/target_hit.mp3")
                            target_SM.redraw(0)
                            cork.destroy()
                            cork_sprites.remove(cork)
                            renpy.restart_interaction()
                            break
                        elif i == len(target_sprites) - 1:
                            cork.destroy()
                            cork_sprites.remove(cork)
                    elif target.row == 2:
                        if target.current_frame == 1 and target.x <= (cork.x - cork.original_size[0] / 2) <= (target.x + target_sizes["middle"][0]) and target.y <= (cork.y - cork.original_size[1] / 2) <= (target.y + target_sizes["middle"][1]):
                            target.hit = True
                            score += 10
                            renpy.sound.play("audio/target_hit.mp3")
                            target_SM.redraw(0)
                            cork.destroy()
                            cork_sprites.remove(cork)
                            renpy.restart_interaction()
                            break
                        elif i == len(target_sprites) - 1:
                            cork.destroy()
                            cork_sprites.remove(cork)
                    elif target.row == 3:
                        if target.current_frame == 1 and target.x <= (cork.x - cork.original_size[0] / 2) <= (target.x + target_sizes["bottom"][0]) and target.y <= (cork.y - cork.original_size[1] / 2) <= (target.y + target_sizes["bottom"][1]):
                            target.hit = True
                            score += 15
                            renpy.sound.play("audio/target_hit.mp3")
                            target_SM.redraw(0)
                            cork.destroy()
                            cork_sprites.remove(cork)
                            renpy.restart_interaction()
                            break
                        elif i == len(target_sprites) - 1:
                            cork.destroy()
                            cork_sprites.remove(cork)

        return 0

    def prepareShootingGallery():
        global countdown_time
        global score

        countdown_time = inital_countdown_time
        score = 0

        for target in target_sprites:
            target.hit = False
            target.idle_animation_direction = "up"
            target.animation_time = 0.0
            target.current_frame = 5
            i = Image("images/shooting_game/target-1-4.png")
            if target.row == 1:
                t = Transform(child = i, zoom = target_row_1_zoom)
            elif target.row == 2:
                t = Transform(child = i, zoom = target_row_2_zoom)
            elif target.row == 3:
                t = Transform(child = i, zoom = target_row_3_zoom)
            target.set_child(t)

transform half_size:
    zoom 0.8




screen shooting_gallery():
    on "show" action [Function(prepareShootingGallery), SetVariable("default_mouse", "targetgame"), SetVariable("shooting_gallery", True)]
    add "images/shooting_game/targets-background.png" at half_size
    add target_SM
    add "images/shooting_game/shooting-gallery-background.png" at half_size
    add cork_gun_transform
    add cork_SM
    add "images/shooting_game/score-background.png" pos (10, 0) at half_size
    text "Score: [score]" color "#FFFFFF" outlines [(absolute(1), "#00000050", absolute(1), absolute(1))] size 32 pos(100, 75) anchor(0.0, 0.0)
    text "Time: {:.0f}".format(countdown_time) color "#FFFFFF" outlines [(absolute(1), "#00000050", absolute(1), absolute(1))] size 32 pos(300, 75) anchor(0.0, 0.0)

    timer 1.0 action If(countdown_time > 0, true = SetVariable("countdown_time", countdown_time - 1.0), false = Show("time_is_up")) repeat If(countdown_time > 0, true = True, false = False)

screen time_is_up():
    modal True

    frame:
        xfill True
        yalign 0.5
        background "#FFFFFF80"
        padding (15, 15)
        text "Time is up!" color "#000000" align(0.5, 0.5) size 40

    timer 3.0 action [Hide("time_is_up"), Show("final_score")]

screen final_score():
    zorder 2
    modal True

    frame:
        background "#000000BF"
        xfill True
        yfill True
        padding(0, 0)

        frame:
            align(0.5, 0.5)
            xysize(int(1485 / 2), int(912 / 2))
            background None
            padding(0, 0)
            add "images/shooting_game/final-score-background.png" align(0.5, 0.5) at half_size
            text "Your score: [score]" outlines [(absolute(1), "#00000050", absolute(1), absolute(1))] color "#FFBF5F" size 80 align(0.5, 0.5)
            imagebutton auto "images/shooting_game/play-again-button-%s.png" pos(0, 0.7) anchor(0.0, 0.0) action [Hide("final_score"), Hide("shooting_gallery"), Function(prepareShootingGallery), Show("shooting_gallery")] at half_size
            imagebutton auto "images/shooting_game/quit-button-%s.png" pos(0.55, 0.7) anchor(0.0, 0.0) action [Hide("final_score"), Hide("shooting_gallery"), Jump("credits"), SetVariable("default_mouse", None), SetVariable("shooting_gallery", False)] at half_size

define config.mouse = {}
define config.mouse["targetgame"] = [("images/shooting_game/target-pointer.png", 17, 10)]
define shooting_gallery = False

# Corkgun variables
default cork_gun_image = Image("images/shooting_game/cork-gun.png")
default cork_gun_size = (int(330 / 2), int(384 / 2))
default cork_gun_pos = (0, 0)
default cork_gun_opos = (int((config.screen_width / 2) - (cork_gun_size[0] / 2)), config.screen_height - cork_gun_size[1] + 60)
default cork_gun_transform = Transform(child = cork_gun_image, zoom = 0.8, pos = (cork_gun_opos[0], cork_gun_opos[1]), function = corkGunTransform)
default cork_image = Image("images/shooting_game/cork.png")
default cork_transform = Transform(child = cork_image, zoom = 0.8)
default cork_sprites = []
default cork_SM = SpriteManager(update = corkUpdate, event = corkEvents)

# Target variables
default target_SM = SpriteManager(update = targetUpdate)
default target_row_1_zoom = 0.8
default target_row_2_zoom = 0.6
default target_row_3_zoom = 0.4
default target_sizes = {"top" : (404 * target_row_1_zoom, 312 * target_row_1_zoom), "middle" : (404 * target_row_2_zoom, 312 * target_row_2_zoom), "bottom" : (404 * target_row_3_zoom, 312 * target_row_3_zoom)}
default target_sprites = []

# Other variables
default score = 0
default inital_countdown_time = 20.0
default countdown_time = inital_countdown_time

label shooting_game_start:
    stop music fadeout 1.0
    play music "audio/BGM_Minigame Tana.mp3" fadein 1.0
    $ setupTargets()
    call screen shooting_gallery
    return
