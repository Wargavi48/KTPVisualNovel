init python:
    def randomize_cards():
        # Function to create cards.
        global cards
        cards = []

        for i in range(int(card_amount / 2)):
            # Fill the cards list with 2 cards (a pair) in each iteration of the loop.
            # The loop iterates card_amount / card_rows times to create the resulting amount of cards.
            # This creates a a nested list that looks like this example: cards = [["card-5", "deselected", "visible"], ["card-2", "deselected", "visible"] ...]
            # 1: name of the card, 2: if the card is selected or deselected, 3: if the card is visible or invisible.
            rand_card_num = renpy.random.randint(1, 10)
            cards.append(["card-%s" % rand_card_num, "deselected", "visible"])
            cards.append(["card-%s" % rand_card_num, "deselected", "visible"])

        # Shuffle the filled list so that each card ends up in a random location instead of right next to each other.
        renpy.random.shuffle(cards)

    def select_card(card_index):
        # Function to select a card that was clicked on.
        global selected_cards
        global match_found

        # Select the card the user clicked on.
        cards[card_index][1] = "selected"
        selected_cards.append(card_index)

        if len(selected_cards) == 2 and cards[selected_cards[0]][0] == cards[selected_cards[1]][0]:
            # Two matching pairs of cards has been selected.
            match_found = True

    def deselect_cards():
        # Function to deselect cards after 2 have been selected that doesn't match.
        global selected_cards

        if len(selected_cards) == 2:
            for card in cards:
                if card[1] == "selected":
                    card[1] = "deselected"
        selected_cards = []

    def hide_matches():
        # Function to hide matching cards.
        global selected_cards
        global match_found
        global hidden_cards

        cards[selected_cards[0]][2] = "hidden" # First card
        cards[selected_cards[1]][2] = "hidden" # Second card
        hidden_cards += 2
        deselect_cards()
        match_found = False

    def reset_memory_game():
        # Function to reset mini-game.
        global match_found
        global hidden_cards

        match_found = False
        hidden_cards = 0
        randomize_cards() # create new cards

transform card_fadein:
    alpha 0.0
    easein 0.5 alpha 1.0

screen memory_mini_game:
    image "card-game/background.png"
    grid int(card_amount / card_rows) card_rows:
        align(0.9, 0.5)
        spacing 5
        for i, card in enumerate(cards):
            if card[1] == "deselected" and card[2] == "visible":
                # This card isn't selected, and it hasn't been matched to another card yet, so we show the back of the card.
                # We set it to be sensitive/clickable only if the player hasn't clicked on 2 cards yet. This is to prevent the player from clicking more cards while they wait for the result.
                imagebutton idle "card-game/card-back.png" sensitive If(len(selected_cards) != 2, True, False) action Function(select_card, card_index = i) at card_fadein
            elif card[1] == "selected" and card[2] == "visible":
                # This card has been selected and it's visible, so we flip it to show its image.
                image "card-game/%s.png" % card[0] at card_fadein
            else:
                # This card is hidden because it was matched with another card.
                # We use a "null" displayable here to emulate an emptpy space due to that we're using a grid. If not, the cards that comes after will shift to fill the empty gap.
                null

    # If there's a matching pair visible on the screen, we want to make them invisible. If there are two non-matching cards instead, we flip them over again.
    # We do this with timers to make sure the player has time to observe the cards to see what they are.
    if match_found:
        timer 1.0 action Function(hide_matches) repeat True # Hides the cards 1.0 second after a match has been found.
    elif len(selected_cards) == 2:
        timer 1.0 action Function(deselect_cards) repeat True # Flips the cards back over 1.0 second after no match was found.
    elif hidden_cards == card_amount:
        # All cards have been matched. We reset the game after 0.5 seconds so the player can play again after the game finished.
        timer 0.5 action Jump("chapter2piaaftergame") 

    # As an alternative to having a timer that resets the game everytime it has finished, you can use a button of some sort to allow the player to choose if they want to play again or not.
    # Example below.

    # button:
    #     background "#FFFFFF"
    #     padding(15, 20)
    #     align(0.1, 0.1)
    #     anchor(0.0, 0.0)
    #     action Function(reset_memory_game)
    #     text "Play again" text_align 0.5 color "#000000" size 25

    # You can also allow the user to quit the mini-game and go back to the normal flow of the visual novel with a button of some sort.
    # Example below.

    # button:
    #     background "#FFFFFF"
    #     padding(15, 20)
    #     align(0.1, 0.2)
    #     anchor(0.0, 0.0)
    #     action NullAction() # Replace with your own action to go back to the main flow of the visual novel. For example: Jump("you_label_name")
    #     text "Quit" text_align 0.5 color "#000000" size 25

default card_amount = 24 # The amount of cards you want to show.
default card_rows = 3 # How many rows these cards should be placed on.
default cards = [] # Holds the name of the cards and their properties.
default selected_cards = [] # Holds the index positions of the cards selected in the cards list.
default hidden_cards = 0 # Amount of cards that have been hidden from matches.
default match_found = False # If a match has been found.

label startPiaGame:
    scene black with dissolve
    play sound "audio/Alarm.mp3" fadein 1.0
    show text "{size=45}{color=#FFF}MINI GAME TIME{/color}{/size}" with Pause(2.0)
    $randomize_cards() # Create cards.
    "Selesaikan mini game untuk menyelesaikan gambar Pia"
    play music "audio/BGM_Mini Game Pia.ogg" fadein 1.0
    call screen memory_mini_game