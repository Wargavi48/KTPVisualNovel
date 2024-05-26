# **** SCRIPT INFO ****
# This script was made for a free online video tutorial on Youtube for teaching purposes by creator "__ess__ Ren'Py Tutorials".
#
# This finished script is only available to download and use in projects by being a Patreon in the tier "Supporter" or higher on the Patreon page as linked to below.
#
# URL to video tutorial: https://www.youtube.com/watch?v=IKLBSJMv50Q
#
# The script comes with no warranty that it will work as the Ren'Py engine updates/changes.
#
# If you don't understand how something is working in this script, it's recommended you have a look at the tutorial video for more information.
#
# Please, do not redistribute this script for download anywhere. If you wish to share it with others, please link to the Patreon page as specified below.
#
# You may use and adapt this script for your game for personal or commercial purposes.
#
# Patreon page where this script is available: https://www.patreon.com/ess_renpy_tutorials
#
# Images available for this tutorial can be used in your finished commercial or personal projects if you wish. Background image used of a classroom is made by "mugenjohncel" on the lemmasoft.com forums. Link: https://lemmasoft.renai.us/forums/viewtopic.php?t=17302


init python:
    class DevtoolMouseposDisplayable(renpy.Displayable):
        def render(self,width,height,st,at):
            tr=Text("{}x{}".format(*renpy.get_mouse_pos()),color="#F00",font="DejaVuSans.ttf").render(width,height,st,at)
            bgr=Solid("#0004").render(max(160,tr.width+32),max(64,tr.height+32),st,at)
            rv=renpy.Render(bgr.width,bgr.height)
            rv.blit(bgr,(0,0))
            rv.blit(tr,((bgr.width-tr.width)//2,(bgr.height-tr.height)//2))
            renpy.redraw(self,0)
            return rv
    def setup_puzzle():
        # Setup the puzzle by placing each piece of the puzzle in a random location to the right of the screen.
        # We do that by setting a start and end coordinate that we can pick random values from.
        for i in range(page_pieces):
            start_x = 1700
            start_y = 200
            end_x = 1800
            end_y = 800
            rand_loc = (renpy.random.randint(start_x, end_x), renpy.random.randint(start_y, end_y))
            initial_piece_coordinates.append(rand_loc) # Add the random locations to a list so we can use them to place each piece.

    def piece_drop(dropped_on, dragged_piece):
        # Function that runs when a piece has been dropped.
        # Below, we check if the dragged piece is dropped on a droppable piece of the same kind and snap it to its location.
        global finished_pieces

        if dragged_piece[0].drag_name == dropped_on.drag_name:
            dragged_piece[0].snap(dropped_on.x, dropped_on.y) # Snap the piece to the dropped location.
            dragged_piece[0].draggable = False # Dropped piece in the correct place should no longer be able to be dragged.
            finished_pieces += 1

            if finished_pieces == page_pieces:
                # All pieces have been placed. We continue with the normal flow of the visual novel.
                renpy.jump("reassemble_complete")

label reassemble_complete:
        show screen puzzle_complete with dissolve
        kana "Akhirnya selesai juga"
        hide screen puzzle_complete with dissolve
        scene dream with Dissolve(2.0)
        play music "audio/Dreamcatcher.mp3" fadein 1.0
        jump credits

screen puzzle_complete:
        image "background.png"
        frame:
            background "images/puzzle_mini_game/Full Freya Kana Puzzle.jpg"
            xysize full_page_size
            anchor(0.5, 0.5)
            pos(800, 735)
        


screen reassemble_puzzle:
    image "background.png"
    add DevtoolMouseposDisplayable()
    frame:
        background "puzzle-frame-landscape.png"
        xysize full_page_size
        anchor(0.5, 0.5)
        pos(800, 735)

    draggroup:
        # Group of draggable pieces, and the spots they can be dragged to.
        # Paper pieces
        for i in range(page_pieces):
            drag:
                drag_name i
                pos initial_piece_coordinates[i]
                anchor(0.5, 0.5)
                focus_mask True
                drag_raise True
                image "puzzle_mini_game/Image_part_%s.jpg" % (i + 1)

        # Snappable spots to drag to.
        for i in range(page_pieces):
            drag:
                drag_name i
                draggable False
                droppable True
                dropped piece_drop
                pos piece_coordinates[i]
                anchor(0.5, 0.5)
                focus_mask True
                image "puzzle_mini_game/image_part_%s.jpg" % (i + 1) alpha 0.0 # Have the alpha at a higher value when first placing the pieces to make sure it looks correct.


default page_pieces = 20 # Amount of pieces for this puzzle.
default full_page_size = (711, 996)
default piece_coordinates = [(552, 332), (753, 332), (954, 332), (1155, 332), (1356, 332), (552, 510), (753, 510), (954, 510), (1155, 510), (1356, 510), (552, 688), (753, 688), (954, 688), (1155, 688), (1356, 688),(552, 866),(753, 866),(954, 866),(1155, 866),(1356, 866)] # The correct coordinates for each piece.
default initial_piece_coordinates = [] # Will be filled with random initial locations of the pieces.
default finished_pieces = 0 # Keeps track of the amount of pieces that have been placed correctly.

label puzzle_start:
    play music "audio/minigame_kana.mp3"
    $ setup_puzzle()
    call screen reassemble_puzzle with dissolve
    return
