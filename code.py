import board
import displayio
import keypad

from space_miner_helpers import Ship, SpaceMinerGame

#keys = keypad.Keys((board.SW_LEFT, board.SW_RIGHT, board.SW_A, board.SW_B, board.SW_Y), value_when_pressed=False, pull=True)
keys = keypad.Keys((
    board.SW_LEFT,
    board.SW_RIGHT,
    board.SW_A,
    board.SW_B,
    board.SW_Y,
    board.SW_X,     # just for recording btn presses
    board.SW_UP,    # idem
    board.SW_DOWN), # idem
    value_when_pressed=False, pull=True)

btns_dict = {
        0: "LT",
        1: "RT",
        2: "A",
        3: "B",
        4: "Y",
        5: "X",
        6: "UP",
        7: "DN",}

display = board.DISPLAY
display.brightness = 0.1

main_group = displayio.Group()

game = SpaceMinerGame((display.width, display.height), display)
#print("dir(game)=", dir(game))
# Add the TileGrid to the Group
main_group.append(game)

# Add the Group to the Display
display.show(main_group)

left_btn_is_down = False
right_btn_is_down = False

# Loop forever so you can enjoy your image
while True:
    event = keys.events.get()
    # event will be None if nothing has happened.
    if event:
        #print("type(event)={}, event={}".format(type(event), event))
        k = event.key_number
        if event.pressed:
            if not game.get_current_state() == 2:  # STATE_GAME_OVER
                #print("pressed", event) # original print command
                print("pressed button", btns_dict[k]) # modified print command
            if k == 0:  # LT arrow button
                game.left_btn_is_down = True
            elif k == 1:  # RT arrow button
                game.right_btn_is_down = True
        else:
            if not game.get_current_state() == 2:  # STATE_GAME_OVER
                #print("released", event) # original print command
                print("released button", btns_dict[k]) # modified print command
            if k == 0:  # LT arrow button
                game.left_btn_is_down = False
                game.left_arrow_btn_event()
            elif k == 1:  # RT arrow button
                game.right_btn_is_down = False
                game.right_arrow_btn_event()
            elif k == 2:  # A button
                game.a_btn_event()
            elif k == 3:  # B button
                game.b_btn_event()
            elif k == 4:  # Y button
                game.y_btn_event()
            """
            elif k == 5:  # X button
                pass
                # game.x_btn_event()
            elif k == 6:  # UP arrow button
                pass
                # game.up_arrow_btn_event()
            elif k == 7:  # DN arrow button
                pass
                # game.down_arrow_btn_event()
            """

    game.tick()

