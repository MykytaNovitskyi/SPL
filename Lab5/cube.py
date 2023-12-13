from __future__ import division
from colorama import init, Fore, Style

init(autoreset=True)

class CubeDrawer:
    def __init__(self, x_size=1, y_size=1, z_size=1, color=Fore.WHITE):
        self.x_size = x_size
        self.y_size = y_size
        self.z_size = z_size
        self.color = color
        self.width = x_size * 2
        self.height = y_size * 2
        self.cube = [[' ']*self.width for _ in range(self.height)]

    def draw_cube(self):
        vertices = {
            'tc': (self.width//2, 0),
            'tl': (0, int(.25*self.height)),
            'tr': (self.width-1, int(.25*self.height)),
            'cc': (self.width//2, self.height//2),
            'bl': (0, int(.75*self.height)),
            'br': (self.width-1, int(.75*self.height)),
            'bc': (self.width//2, self.height-1)
        }
        edges = (
            ('tc', 'tl'),
            ('tc', 'tr'),
            ('tl', 'cc'),
            ('tl', 'bl'),
            ('tr', 'cc'),
            ('tr', 'br'),
            ('bl', 'bc'),
            ('br', 'bc'),
            ('cc', 'bc')
        )

        for edge in edges:
            v1 = vertices[edge[0]]
            v2 = vertices[edge[1]]
            x1 = v1[0]
            y1 = v1[1]
            x2 = v2[0]
            y2 = v2[1]
            if x1 > x2:
                x1, x2 = x2, x1
                y1, y2 = y2, y1
            try:
                m = (y2-y1)/(x2-x1)
            except ZeroDivisionError:
                c = '|'
                for yy in range(min(y1, y2), max(y1, y2)+1):
                    self.cube[yy][x1] = self.color + c
            else:
                c = '.'
                yy = y1
                for xx in range(x1, x2+1):
                    self.cube[int(yy)][xx] = c
                    yy += m

                if edge[0] in ('tc', 'tr', 'tl') and edge[1] in ('tc', 'tr', 'tl'):
                    self.cube[y1][x1] = c

        cube_str = '\n'.join(''.join(row) for row in self.cube)
        return cube_str

    def draw_square(self, length):
        square_width = int(length * 2.5)
        square = [[' ']*square_width for _ in range(length)]

        for i in range(length):
            for j in range(square_width):
                if i == 0 or i == length-1:
                    square[i][j] = self.color + '-'
                elif j == 0 or j == square_width-1:
                    square[i][j] = self.color + '|'

        square_str = '\n'.join(''.join(row) for row in square)
        return square_str

    def remove_color_codes(self, text):
        while '\033[' in text:
            start = text.find('\033[')
            end = text.find('m', start)
            if end != -1:
                text = text[:start] + text[end+1:]
            else:
                break
        return text

    def save_to_file(self, content):
        filename = input("Enter the file name to save: ")
        with open(filename, 'w') as file:
            file.write(self.remove_color_codes(content))
