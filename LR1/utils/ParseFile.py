import re


class ParseFile:
    __ALPHABET = "=\n{}(),.ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    __CASH = {
        "tuples_in_set": 0,
        "tuples": [str]
    }

    @staticmethod
    def parse_file(url: str):
        txt = ParseFile.__open_file(url).replace(' ', '')
        if ParseFile.__check_number_sets(txt) and ParseFile.__check_correct_symbols(txt) and \
                ParseFile.__check_number_tuples(txt):
            return ParseFile.__get_tuples()
        else:
            raise Exception("Write the correct set, example: A = {(x1, 0.0), (x2, 0.1), (x3, 0.3), (x4, 1.0)}")

    @staticmethod
    def __open_file(url: str) -> str:
        with open(url) as file:
            txt = file.read()
        return txt

    @staticmethod
    def __check_correct_symbols(txt: str):
        for char in txt:
            if not re.match(f"[{re.escape(ParseFile.__ALPHABET)}]", char):
                return False
        return True

    @staticmethod
    def __check_number_sets(txt: str) -> bool:
        pattern = r'[A-Z]+\d*='
        number_set_names = len(re.findall(pattern, txt))

        if number_set_names == txt.count('{') == txt.count('}') == 3:
            return True
        else:
            return False

    @staticmethod
    def __check_number_tuples(txt: str) -> bool:
        pattern = r'\(\w+[0-9]*,\d+\.\d+\)'
        tuples = re.findall(pattern, txt)

        pattern_opened_brackets = r'\('
        pattern_closed_brackets = r'\)'

        matches_opened = re.findall(pattern_opened_brackets, txt)
        matches_closed = re.findall(pattern_closed_brackets, txt)
        if len(matches_opened) == len(matches_closed) == len(tuples):
            if len(tuples) % len(matches_opened) == 0:
                ParseFile.__CASH["tuples_in_set"] = len(tuples) // 3
                ParseFile.__CASH["tuples"] = tuples
                return True
        else:
            return False

    @staticmethod
    def __get_tuples():
        parsed_data = {
            "first_set": [str],
            "second_set": [str],
            "third_set": [str]
        }
        tuple_list = []
        for value in ParseFile.__CASH["tuples"]:
            value = value.replace('(', '').replace(')', '')
            tuple_list.append((value.split(',')[0], value.split(',')[1]))

        offset = ParseFile.__CASH["tuples_in_set"]
        parsed_data["first_set"] = tuple_list[0:offset]
        parsed_data["second_set"] = tuple_list[offset:offset+offset]
        parsed_data["third_set"] = tuple_list[offset+offset:]

        return parsed_data
