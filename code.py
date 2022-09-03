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

STATE_GAME_ROUND_END = game.STATE_GAME_ROUND_END
STATE_GAME_OVER = game.STATE_GAME_OVER

main_group.append(game)

# Add the Group to the Display
display.show(main_group)

left_btn_is_down = False
right_btn_is_down = False

def main():
    # Loop forever so you can enjoy your image
    while True:
        try:
            #gcs = game.get_current_state()
            #gls = game.LAST_STATE
            event = keys.events.get()
            # event will be None if nothing has happened.
            if event:
                """
                print("game.score_shown=", game.score_shown)
                print("gcs=", game.state_dict[gcs])
                if gls in game.state_dict.keys():
                    print("gls=", game.state_dict[gls])
                """
                k = event.key_number
                no_button = False
                if event.pressed:
                    #print("pressed button", btns_dict[k]) # modified print command
                    if k == 0:  # LT arrow button
                        game.left_btn_is_down = True
                    elif k == 1:  # RT arrow button
                        game.right_btn_is_down = True
                    elif k == 6:  # UP arrow button
                        game.up_btn_is_down = True
                    elif k == 7:
                        game.down_btn_is_down = True
                    else:
                        no_button = True
                else:
                    #print("released button", btns_dict[k]) # modified print command
                    if k == 0:  # LT arrow button
                        game.left_btn_is_down = False
                        game.left_arrow_btn_event()
                    elif k == 1:  # RT arrow button
                        game.right_btn_is_down = False
                        game.right_arrow_btn_event()
                    elif k == 2:  # A button - fire LASER
                        game.a_btn_event()
                    elif k == 3:  # B button - start GAME
                        game.b_btn_event()
                    elif k == 4:  # Y button - start SHOP
                        game.y_btn_event()
                    elif k == 6:  # UP arrow button - in SHOP increase laser speed
                        game.up_btn_is_down = False
                    elif k == 7: # DN arrow button -  - in SHOP decrease laser speed
                        game.down_btn_is_down = False
                    else:
                        no_button = True
            game.tick()
        except KeyboardInterrupt:
            break

    cnt = 0
    while True:
        cnt += 1
        if cnt > 10000:
            cnt = 0

if __name__ == '__main__':
    main()
