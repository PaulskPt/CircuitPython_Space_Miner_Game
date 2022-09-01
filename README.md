# CircuitPython_Space_Miner_Game
No microtransactions or NFTs involved.

This fork contains various additions and modifictions by @PaulskPt

The modifications have to do with:
```
a) human readable REPL output for pressed buttons. Example "Pressed button X" instead of "Pressed button 5" and
   "Released button X" instead of "Released button 5".
   For this, in file code.py, the defitions for keypad.Keys() "board.SW_X", "board.SW_UP" and "board.SW_DN" have been added to the keypad.Keys() tuples.
   Initially this list had only defined the buttons that were actually used: LEFT, RIGHT, A, B and Y.
   Note that the 'new' buttons are added to the end of the list to leave the values for the buttons LEFT, RIGHT, A, B and Y unchanged.

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
        event = keys.events.get()
        # event will be None if nothing has happened.
        if event:
            k = event.key_number # create key to btns_dict.
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
                    print("released button", btns_dict[k])
                # [...]  etcetera.
    
b) increase the speed of the laser vertical (y) movement (30%). 
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
        
```