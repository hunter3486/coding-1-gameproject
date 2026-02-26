# Write your game here
import curses

game_data = {
    'width': 10,
    'height': 5,
    'player': {"x": 0, "y": 0},
    'moneybag_pos': {"x": 9, "y":4},
   
    'pegleg': [
        {"x": 2, "y": 1, "collected": False},
    ],

    'scurvy': [
        {"x": 6, "y": 2, "collected": False}
    ],
    
    'goldfish': [
        {"x": 1, "y": 2},
        ],

    'sea urchin': [
        {"x": 3, "y": 1},
    ],

    'shark': [
        {"x": 7, "y":3},
    ],

    # ASCII icons
    'goldfish': "\U0001F420",
    'shark': "\U0001F42C",
    'sea urchin': "\U0001F421 ",
    'pegleg': "\U00002712",
    'scurvy': "\U0001F300", 
    'moneybag': "\U0001F4B0",
    'playericon': "\U0001F6A3",
    'empty': "  "
}

def draw_board(stdscr):
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, -1)

    stdscr.clear()
    for y in range(game_data['height']):
        row = ""
        for x in range(game_data['width']):
            # Player
            if x == game_data['player']['x'] and y == game_data['player']['y']:
               row += game_data['playericon']
            #Eagle
            elif x == game_data['moneybag_pos']['x'] and y == game_data['moneybag_pos']['y']:
               row += game_data['moneybag']
            #Enemies
            # elif any(o['x'] == x and o['y'] == y for o in game_data['shark']):
            #     row += game_data['shark']
            print(o)
            # elif any(o['x'] == x and o['y'] == y for o in game_data['sea urchin']):
            #     row += game_data['sea urchin']
            # elif any(o['x'] == x and o['y'] == y for o in game_data['goldfish']):
            #     row += game_data['goldfish']
            # # Collectibles
            # elif any(c['x'] == x and c['y'] == y and not c['collected'] for c in game_data['pegleg']):
            #     row += game_data['pegleg']
            # elif any(c['x'] == x and c['y'] == y and not c['collected'] for c in game_data['scurvy']):
            #     row += game_data['scurvy']
            # else:
            #     row += game_data['empty']
        stdscr.addstr(y, 0, row, curses.color_pair(1))

    stdscr.refresh()
    stdscr.getkey()  # pause so player can see board

curses.wrapper(draw_board)
