from sty import fg, ef

from Classes.lab_7.RequestsAPI import RequestsAPI
from sty import rs
import requests



# site = 'https://api.openweathermap.org/data/2.5/weather'
# q = 'Варшава'
# appid = "94214c464205a73bcf054c4c2d071905"
# params={'q': q, 'appid': appid}
#
# qa = (requests.get(site, params=params).json())
#
# # response1 = RequestsAPI(site=site, params=params)
# # response1.data = qa
# response2 = RequestsAPI(site='https://jsonplaceholder.typicode.com/users')
#
#
dct = [
{'header': 'name', 'color': fg.red, 'font': ef.bold},
{'header': 'email', 'color': fg.blue, 'font': ef.underl},
{'header': 'phone', 'color': fg.green, 'font': ef.dim},
]

# response2.get_table(dct)
# print(response2.visualize_table(dct))


class ConsoleRequestsApi:

    def __init__(self):
        self.site = ''
        self.params = {}
        self.headers = []
        self.history = []

    def configuration(self):
        self.site = input("Input site: ")
        if input("Do you want to input params(1/0): ") == '1':
            self.set_params()

        response = RequestsAPI(site=self.site, params=self.params)

        if input("Do you want to custom style for headers(1/0): ") == '1':
            self.set_headers_style(response)
            # result = response.visualize_table()

        result = response.get_table()
        self.history.append(result)

        if input("Do you want to custom headers output(1/0): ") == '1':
            self.set_custom_headers(response)
            result = response.visualize_table(self.headers)

        if input("Do you want to save your data: ") == '1':
            self.save(response)

        if input("Do you want to view your history: ") == '1':
            for history in self.history:
                print(history)

        return result

    def set_headers_style(self, response):
        response.color = self.select_color(response.COLORS)
        response.font = self.select_font(response.FONTS)
        return response

    def save(self, response):
        save = input("Input format (txt, csv, json): ")
        filename = input("Input name: ")
        if save == 'txt':
            response.save_to_txt(filename)
        elif save == 'csv':
            response.save_to_csv(filename)
        elif save == 'json':
            response.save_to_json(filename)
        else:
            ext = input("Incorrect format: Try again?(1/0)")
            if ext == '1':
                self.save(response)

    def set_custom_headers(self, response: RequestsAPI):
        stop = '1'
        while stop == '1':
            self.set_header_dict(response)
            stop = input("Do you have any parameters?(1/0)")

    def set_header_dict(self, response):
        header = self.select_header(response.get_headers())
        color = self.select_color(response.COLORS)
        font = self.select_font(response.FONTS)
        self.headers.append({'header': header, 'color': color, 'font': font})

    @staticmethod
    def select_color(colors):
        for key, value in colors.items():
            print(f"{key}: {value + rs.all}")
        value = input(f"Select color: ")
        current_value = colors.get(value, None)
        if current_value:
            return current_value
        else:
            return ''

    @staticmethod
    def select_font(fonts):
        for key, value in fonts.items():
            print(f"{key}: {value + rs.all}")
        value = input(f"Select font: ")
        current_value = fonts.get(value, None)
        if current_value:
            return current_value
        else:
            return ''

    @staticmethod
    def select_header(headers):
        header = input(f"Select header with {headers}: ")
        if header in headers:
            return header
        else:
            return ''

    def set_params(self):
        stop = '1'
        while stop == '1':
            self.set_dict()
            stop = input("Do you have any parameters?(1/0)")

    def set_dict(self):
        key = input("key: ")
        value = input("value: ")
        self.params[key] = value

    def run(self):
        stop = ''
        while stop != 'f':
            try:
                result = self.configuration()
                print(result)
            except Exception as e:
                print(e)
            finally:
                stop = input("Press 'f' if you want to exit: ")


# site = input("Input site: ")



# params = {}
#
#
# for i in range(2):
#     key = input("key: ")
#     value = input("value: ")
#     params[key] = value
#
# response = RequestsAPI(site=site, params=params)
#
# print(response1.visualize_table())
# print(response2.visualize_table())
# # print(response.visualize_table())
