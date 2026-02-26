# Write your game here
import curses

game_data = {
    'width': 10,
    'height': 5,
    'player': {"x": 0, "y": 0},
    'pegleg': [
        {"x": 2, "y": 1, "collected": False},
    ],

    'scurvy': [
        {"x": 6, "y": 2},
    ]
    
    'enemies': ['goldfish': [
        {"x": 1, "y": 2},
    ],

    'sea urchin': [
        {"x": 3, "y": 1},
    ],

    'shark': [
        {"x": 7, "y":3},
    ],
    ]

    # ASCII icons
    'goldfish': "\U0001F420",
    'shark': "\U0001F42C",
    'sea urchin': "\U0001F421 ",
    'pegleg': "\U00002712",
    'scurvy': "\U0001F300", 
    'moneybag': "\U0001F4B0",
    'playericon' "\U0001F6A3",
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
            # Enemies
            elif any(o['x'] == x and o['y'] == y for o in game_data['enemies']):
                row += game_data['enemies']
            # Collectibles
            elif any(c['x'] == x and c['y'] == y and not c['collected'] for c in game_data['collectibles']):
                row += game_data['pegleg']
                row ++= game_data['scurvy']
            else:
                row += game_data['empty']
        stdscr.addstr(y, 0, row, curses.color_pair(1))

    stdscr.refresh()
    stdscr.getkey()  # pause so player can see board

curses.wrapper(draw_board)