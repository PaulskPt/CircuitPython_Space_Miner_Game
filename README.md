# CircuitPython_Space_Miner_Game
No microtransactions or NFTs involved.

This fork contains various additions and modifictions by @PaulskPt

The modifications have to do with:
```
a) human readable REPL output for pressed buttons. Example "Pressed button X" 
   instead of "Pressed button 5" and "Released button X" instead of "Released button 5".
   For this, in file code.py, the defitions for keypad.Keys() "board.SW_X", 
   "board.SW_UP" and "board.SW_DN" have been added to the keypad.Keys().
   Initially this list had only defined the buttons that were actually used: LEFT, RIGHT, A, B and Y.
   Note that the 'new' buttons are added to the end of the list to leave the values for the buttons LEFT, 
   RIGHT, A, B and Y unchanged.

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

   To facilitate a better human readable button print() in REPL, the following btns_dict has been added:

    btns_dict = {
            0: "LT",
            1: "RT",
            2: "A",
            3: "B",
            4: "Y",
            5: "X",
            6: "UP",
            7: "DN",}


    In code.py, in the infinite while loop the following changes have been made to facilitate the print readability:
    # Loop forever so you can enjoy your image
    while True:
        try:
            event = keys.events.get()
            # event will be None if nothing has happened.
            if event:
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
                    # [...]  etcetera.
    
b) Set the default speed of the laser vertical (y) movement to 3 (an increase of 30% compared to the original value).
   Added the possibility to change the laser speed (see f).
   This increases the chance to hit an ore.
   It is realized in file space_miner_helpers.py, class SpaceMinerGame, function tick():

    def tick(self):
        # [...]

        # move all lasers
        for laser in self.lasers:
            if laser.hidden == False:
                if laser.y > 0:
                    laser.y -= 3 # was: -= 1   <<<=== This increases the vertical speed of the laser with 30%.
                else:
                    laser.hidden = True

c) In file space_miner_helpers.py, class SpaceMinerGame,
   Added:
       state_dict = {
        0: "STATE_WAITING_TO_PLAY",
        1: "STATE_PLAYING",
        2: "STATE_GAME_OVER",
        3: "STATE_SHOP",
        4: "STATE_GAME_ROUND_END"
    }
    
    state_dict2 = {
        0: "WAITING TO PLAY",
        1: "PLAYING",
        2: "GAME_OVER",
        3: "SHOP",
        4: "ROUND END"
    }
    
    At the start of Class SpaceMinerGame, changed the REPL print of FRAME_DELAY to indicate the value in microseconds:
    FRAME_DELAY = 0.001 / 2  # = 500 uSecs
    # print(FRAME_DELAY) # original print command
    print("\nFRAME_DELAY = ", end='') # modified print commands
    n = int(FRAME_DELAY*1000000)+1 # +1 is correction because (incorrect) result was 499
    print(n, end='')
    print(" microeconds")
    
d) I experienced that the game score was only shown at a 'game over' or 'round end' during the first round. In subsequent rounds
   the game score was only shown in REPL, not on the display. 
   During @☺Foamyguys stream on Twitch.tv on Saturday September 3, 2022, it revealed that, while the Pimoroni PICO SYSTEM device,
   that I was using, was flashed with CircuitPython firmware version: CircuitPython v.8.0.0-beta0, the .mpy files in
   /lib/Adafruit_display_text were a bit outdated (March 28, 2022). After I replaced these files by ones with a date of 
   August 26, 2022, the problem of not displaying the game score in rounds >= 2, was solved.

   I added the following mods to space_miner_helpers.py:
   To have the score shown at every STATE_GAME_OVER and STATE_GAME_ROUND_END, in class SpaceMinderGame, 
   I added the function show_score(). The part in function update_round_end_info(),
   to show the score onto the display was moved to the function show_score(). Also was added a boolean attribute 'self.score_shown',
   to have the score shown one time only. 
   This flag is reset in the function 'b_btn_event()' which starts a game. The flag is set at the end of the show_score() function.
   In code.py, at the end of the infinite while loop, if the current game state is STATE_GAME_OVER and the flag game.score_shown is False,
   the function 'game.show_score()' will be called. The score will be shown on the display and the score will be printed in REPL.
 
e) in file space_miner_helpers.py, class Ship,
   set the initial self.x value to 'self.x = self.display_size[0] // 2 - 18' to show the ship in the middle instead of the extreme left.
 
f) in the STATE_SHOP, class SpaceMinerGame, added defines: LASER_MIN_SPEED = 1 and  LASER_MAX_SPEED = 5
   Added item "Laser Speed" to self.stats. In function update_shop_label(), added "Laser Speed".
   Using the functions: up_arrow_btn_event() and down_arrow_btn_event() to increase and decrease the value for 'self.laser_speed'.

g) in file space_miner_helpers.py, class SpaceMinerGame, function reset_round(), I changed the code to only reset the ship health progressbar
   after a GAME_OVER and not after each ROUND_END state.

h) In file space_miner_helpers.py, class SpaceMinerGame, I added 'import supervisor' and I added a function x_btn_event().
   This function calls 'supervisor.reload()' which causes a software reset. The function x_btn_event() is called from within code.py.

i) Added a round time progress bar in the left-top of the display. This progress bar indicates the time that one has left to play
   in the current round.
    
```
