import csv
import json

import requests
from prettytable import PrettyTable
from sty import fg, ef, rs


class RequestsAPI:
    site = ''
    params = {}

    color = fg.blue

    font = ef.italic
    reset = rs.all

    COLORS = {
        'BLACK': fg.black,
        'RED': fg.red,
        'GREEN': fg.green,
        'YELLOW': fg.yellow,
        'BLUE': fg.blue,
        'MAGENTA': fg.magenta,
        'CYAN': fg.cyan,
        'WHITE': fg.white,
        'RESET': reset,

    }

    FONTS = {
        'italic': ef.italic,
        'bold': ef.bold,
        'dim': ef.dim,
        'underl': ef.underl,
        'blink': ef.blink,
        'hidden': ef.hidden,
        'inverse': ef.inverse,
        'strike': ef.strike,
        'RESET': reset,
    }

    def __init__(self, **kwargs):
        self.result = PrettyTable()
        if 'site' in kwargs:
            self.site = kwargs['site']
        if 'params' in kwargs:
            self.params = kwargs['params']
        self.response = requests.get(self.site)

        self.data = self.response.json()

    def get_headers(self, data=None):
        if not data:
            data = self.data
        if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
            return data[0].keys()
        elif isinstance(data, dict):
            return data.keys()
        else:
            raise ValueError("Непідтримуваний формат даних")

    def get_table(self):
        table = PrettyTable()
        field_names = []
        if isinstance(self.data, list) and len(self.data) > 0 and isinstance(self.data[0], dict):
            headers = self.data[0].keys()

            for row in self.data:
                table.add_row(row.values(), divider=True)
        elif isinstance(self.data, dict):
            headers = self.data.keys()
            table.add_row(self.data.values(),  divider=True)
        else:
            raise ValueError("Непідтримуваний формат даних")
        table.field_names = headers
        for field_name in table.field_names:
            field_names.append(self.color + self.font + field_name + self.reset)
        table.field_names = field_names
        return table

    def get_custom_headers(self, custom_headers):
        headers = []
        for custom_header in custom_headers:
            headers.append(custom_header.get('header'))

        return headers

    def get_custom_table(self, custom_headers):
        table = PrettyTable()
        new_headers = self.get_custom_headers(custom_headers)
        new_data = []
        if isinstance(self.data, list) and len(self.data) > 0 and isinstance(self.data[0], dict):
            for data in self.data:
                dicts = {}
                for key, value in data.items():
                    if key in new_headers:
                        dicts[key] = value
                new_data.append(dicts)

            for row in new_data:
                table.add_row(row.values(),  divider=True)
            headers = new_data[0].keys()

        elif isinstance(self.data, dict):

            headers = self.data.keys()
            table.add_row(self.data.values(),  divider=True)
        else:
            raise ValueError("Непідтримуваний формат даних")
        table.field_names = headers
        return table, new_data

    def set_custom_headers(self, custom_headers: list[dict], data):
        new_headers = []

        user_headers = [item.get('header') for item in custom_headers]

        old_headers = self.get_headers(data)

        for old_header in old_headers:
            if old_header in user_headers:
                new_header = self.get_custom_header(old_header, custom_headers)
            else:
                new_header = old_header
            new_headers.append(new_header)
        return new_headers

    def get_custom_header(self, old_header, custom_headers):
        new_header = ''
        for header in custom_headers:
            if header.get('header') == old_header:
                new_header = self.set_style(header.get('header'), header.get('color'), header.get('font'))
                break
        return new_header

    def set_style(self, header, color, font):
        return color + font + header + self.reset

    def visualize_table(self, custom_headers=None):
        table, data = self.get_custom_table(custom_headers)
        field_names = []
        if custom_headers:
            field_names = self.set_custom_headers(custom_headers, data)
            # print(field_names)
        else:
            for field_name in table.field_names:
                field_names.append(self.color + self.font + field_name + self.reset)
        table.field_names = field_names
        return table

    def save_to_json(self, filename):
        filename = self._add_extension(filename, "json")
        with open(filename, "w") as json_file:
            json.dump(self.data, json_file, indent=2)

    def save_to_csv(self, filename):
        filename = self._add_extension(filename, "csv")
        csv_columns = self.data[0].keys()
        with open(filename, "w", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
            writer.writeheader()
            for row in self.data:
                writer.writerow(row)

    def save_to_txt(self, filename):
        filename = self._add_extension(filename, "txt")
        with open(filename, "w") as txt_file:
            for row in self.data:
                txt_file.write(f"{row}\n")

    @staticmethod
    def _add_extension(filename, default_extension):
        if not filename.endswith(f".{default_extension}"):
            filename += f".{default_extension}"
        return filename

# site = 'https://jsonplaceholder.typicode.com/users'
# params = {}
#
# response = RequestsAPI(site=site, params=params)
#
# print(response.get_table())
# print(response.visualize_table())
