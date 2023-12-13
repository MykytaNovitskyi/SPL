import pyfiglet

from colorama import Fore


class ArtGenerator:
    _message = ''
    _ascii_art = None
    _font = 'standard'
    _color = Fore.RESET
    _width = 80

    _direction = 'auto'
    _justify = 'auto'

    _user_height = None
    _user_width = None

    _FONTS = {
        '1': "standard",
        '2': "slant",
        '3': "big",
        '4': "block",
        '5': "bubble",
        '6': "digital",
        '7': "isometric1",
        '8': "isometric2",
        '9': "letters",
        '10': "script",
        '11': "shadow",
        '12': "starwars",
    }
    _COLORS = {
        'BLACK': Fore.BLACK,
        'RED': Fore.RED,
        'GREEN': Fore.GREEN,
        'YELLOW': Fore.YELLOW,
        'BLUE': Fore.BLUE,
        'MAGENTA': Fore.MAGENTA,
        'CYAN': Fore.CYAN,
        'WHITE': Fore.WHITE,
        'RESET': Fore.RESET,
    }
    _DIRECTIONS = {
        'LTR': 'left-to-right',
        'RTl': 'right-to-left',
    }
    _JUSTIFIES = {
        'CENTER': 'center',
        'RIGHT': 'right',
        'LEFT': 'left',
    }

    # GET/SET MESSAGE
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    # GET/SET FONT
    @property
    def font(self):
        return self._font

    @font.setter
    def font(self, value):
        self._font = value

    # GET/SET COLOR
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    # GET/SET WIDTH
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    # GET/SET DIRECTION
    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value

    # GET/SET JUSTIFY
    @property
    def justify(self):
        return self._justify

    @justify.setter
    def justify(self, value):
        self._justify = value

    # GET/SET User height
    @property
    def user_height(self):
        return self._user_height

    @user_height.setter
    def user_height(self, value):
        self._user_height = value

        # GET/SET User height

    @property
    def user_width(self):
        return self._user_width

    @user_width.setter
    def user_width(self, value):
        self._user_width = value

    def __init__(self, message=''):
        self._message = message
        self._ascii_art = pyfiglet.figlet_format(self._message)

    def set_custom_font(self, symbol):
        self._font = 'banner3'
        self.create()
        # self._ascii_art = self._ascii_art(font='')
        for original_char, user_char in zip("#/", symbol):
            self._ascii_art = self._ascii_art.replace(original_char, user_char)

    def save(self, filename):
        with open(filename, 'w') as file:
            self.create()
            file.write(self._ascii_art)

    def _create(self, **kwargs):
        if 'font' in kwargs:
            font = kwargs['font']
        else:
            font = self._font
        return pyfiglet.Figlet(font=font, direction=self._direction, justify=self._justify, width=self._width)

    def create(self):
        try:
            art = self._create()
            self._ascii_art = art.renderText(self._message)

        except NameError as e:
            raise NameError(f"Error: {e}")

    def prev_view(self):
        art = self._create()
        art = (self._color + art.renderText(self._message))
        return art

    def _art_zoom(self):
        art = self._create(font='banner3')
        art = art.renderText(self._message)
        return art

    def zoom(self):
        line = ''
        lines = []
        len_line = 0
        len_lines = 0
        mx = 0
        art = self._art_zoom()

        for i in art:

            if i != '\n':
                line += i
                mx += 1
            else:
                if len_line < mx:
                    len_line = mx
                mx = 0
                lines += [line]

                line = ''
        len_lines = lines.__len__()
        square_base = len_lines * len_line
        square_update = self._user_height * self._user_width
        if square_update >= square_base:
            pw = round(square_update / square_base)
        else:
            pw = round(square_base / square_update)
        new_lines = []
        for line in lines:
            new_line = ''
            for l in line:
                new_line += l
                new_line += l
            new_lines += [new_line] * pw
        laq = ''
        for line in new_lines:
            laq += line + '\n'
        self._ascii_art = laq

    def __str__(self):
        return self._color + self._ascii_art
