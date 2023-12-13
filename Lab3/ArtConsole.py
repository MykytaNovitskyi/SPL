from ArtGenerator import ArtGenerator


class ArtConsole(ArtGenerator):

    @classmethod
    def set_parameters(cls, dct, input_message):
        for key, value in dct.items():
            print(f"{key}: {value}")
        value = input(f"Select {input_message}: ")
        current_value = dct.get(value, None)
        if current_value:
            return current_value
        else:
            return None

    def input_function(self, dct, input_message, default):
        check = input(f"do you want to set {input_message}? (1/0): ")
        font = None
        if check == '1':
            font = self.set_parameters(dct, 'font')
        if font:
            return font
        else:
            return default

    def configuration(self):
        message = input("Input message: ")
        self.message = message

        self.font = self.input_function(self._FONTS, 'font', self.font)

        self.color = self.input_function(self._COLORS, 'color', self.color)

        self.justify = self.input_function(self._JUSTIFIES, 'justify', self.justify)
        self.direction = self.input_function(self._DIRECTIONS, 'direction', self.direction)

        change_font = input('do you want to create own font? (1/0): ')
        if change_font == '1':
            custom_symbol = input("Input custom symbol: ")
            self.set_custom_font(custom_symbol)

        change_zoom = input('do you want to create zoom? (1/0): ')
        if change_zoom == '1':
            height = int(input("Input custom height: "))
            width = int(input("Input custom width: "))
            self.user_height = height
            self.user_width = width
            self.zoom()

        watch = input("do you want to watch art before to save? (1/0):")
        if watch == '1':
            if self._ascii_art:
                print(self._ascii_art)
            else:
                print(self.prev_view())
            check = input("do you want to save? (1/0): ")
            if check == '1':
                save = input("Input filename: ")
                self.save(save)

    def run(self):
        while input("input 'f' if you want to exit: ") != 'f':
            try:
                self.configuration()
                self.create()
                print(self)
            except Exception as e:
                print(e)
