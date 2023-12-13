from ArtGenerator import ArtGenerator
from fonts import *


class CustomArt(ArtGenerator):
    _font = standard
    _user_height = 5
    _user_width = 5
    _direction_message = ''
    _FONTS = {
        '1': standard,
        '2': banner3,
    }

    def _custom_justify(self):
        message = self.message
        if self.justify == 'center':
            message = message.rjust(20, ' ')
            # message = message.rjust(40, '')
        elif self.justify == 'right':
            message = message.rjust(40)
            # message = message.rjust(80, '')
        elif self.justify == 'left':
            message = message.ljust(0, ' ')
            # message = message.ljust(80, '')
        return message

    def _create(self, **kwargs):
        if 'font' in kwargs:
            font = kwargs['font']
        else:
            font = self._font

        self._direction_message = self._custom_justify()
        art = []
        max_lines = max(len(font.get(letter, '').split('\n')) for letter in self._direction_message)
        for line_num in range(max_lines):
            line = ""
            for letter in self._direction_message:
                letter_lines = self._font.get(letter, '').split('\n')
                if line_num < len(letter_lines):
                    if self.justify == 'left':
                        line += letter_lines[line_num].ljust(len(letter_lines[0]) + 1)
                    elif self.justify == 'center':
                        line += letter_lines[line_num].center(len(letter_lines[0]) + 1)
                    elif self.justify == 'right':
                        line += letter_lines[line_num].rjust(len(letter_lines[0]) + 1)
                else:
                    line += ' ' * (len(letter_lines[0]) + 1)
            art.append(line)
        output = '\n'.join(art)
        return output

    def _art_zoom(self):
        art = self._create(font=banner3)
        return art

    def prev_view(self):
        art = self._create()
        art = (self._color + art)
        return art

    def create(self):
        try:
            self._ascii_art = self._create()

        except NameError as e:
            raise NameError(f"Error: {e}")
