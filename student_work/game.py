# Write your game here
import curses

game_data = {
    'width': 10,
    'height': 5,
    'player': {"x": 0, "y": 0, 'score': 0},
    'goldfish_pos': {"x": 8, "y":4},
   
    'moneybag_col': [
        {"x": 9, "y": 4, "collected": False},
    ],

    'pegleg_collect': [
        {"x": 6, "y": 2, "collected": False},
    ], 

    'scurvy_obs': [
        {"x": 6, "y": 3},
        {"x": 4, "y": 4}
    ],
    
    'goldfish': [
        {"x": 1, "y": 2},
        ],


    # ASCII icons
    'goldfish': "\U0001F420",
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
            elif x == game_data['goldfish_pos']['x'] and y == game_data['goldfish_pos']['y']:
                row += game_data['goldfish']
        #     # Obstacles
            elif any(o['x'] == x and o['y'] == y for o in game_data['scurvy_obs']):
                row += game_data['scurvy']
        #     # Collectibles
            elif any(c['x'] == x and c['y'] == y and not c['collected'] for c in game_data['pegleg_collect']):
                row += game_data['pegleg']
            elif any(c['x'] == x and c['y'] == y and not c['collected'] for c in game_data['moneybag_col']):
                row += game_data['moneybag']
            else:
                row += game_data['empty']
        stdscr.addstr(y, 0, row, curses.color_pair(1))

    
    stdscr.addstr(game_data['height'] + 1, 0,
                  f"Moves Survived: {game_data['player']['score']}",
                  curses.color_pair(1))
    stdscr.addstr(game_data['height'] + 2, 0,
                  "Move with W/A/S/D, Q to quit",
                  curses.color_pair(1))
    stdscr.refresh()


def move_player(key):
    x = game_data['player']['x']
    y = game_data['player']['y']

    new_x, new_y = x, y
    key = key.lower()

    if key == "w" and y > 0:
        new_y -= 1
    elif key == "s" and y < game_data['height'] - 1:
        new_y += 1
    elif key == "a" and x > 0:
        new_x -= 1
    elif key == "d" and x < game_data['width'] - 1:
        new_x += 1
    else:
        return  # Invalid key or move off board

    # Check for obstacles
    if any(o['x'] == new_x and o['y'] == new_y for o in game_data['scurvy_obs']):
        return

    # Update position and increment score
    game_data['player']['x'] = new_x
    game_data['player']['y'] = new_y
    game_data['player']['score'] += 1

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)

    draw_board(stdscr)

    while True:
        try:
            key = stdscr.getkey()
        except:
            key = None

        if key:
            if key.lower() == "q":
                break

            move_player(key)
            draw_board(stdscr)

curses.wrapper(main)
