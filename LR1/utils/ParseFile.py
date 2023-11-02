import re


class ParseFile:
    __PATTERN = r'([A-Z]+=\{\([a-z]\d,\d+\.\d+\)(?:,\([a-z]\d,\d+\.\d+\))*)\}'
    __CASH = {}

    @staticmethod
    def parse_file(url: str):
        txt = ParseFile.__open_file(url).replace(' ', '')
        text = re.findall(ParseFile.__PATTERN, txt)

        for current_set in text:
            find_set_name = r'[A-Z]+'
            set_name = re.findall(find_set_name, current_set)
            ParseFile.__CASH[set_name[0]] = set()

            find_dataset = r'\([a-z]\d,\d+\.\d+\)'
            dataset = re.findall(find_dataset, current_set)

            for data in dataset:
                value = data.replace('(', '').replace(')', '')
                value = value.split(',')
                ParseFile.__CASH[set_name[0]].add((value[0], float(value[1])))

        print(ParseFile.__CASH)

    @staticmethod
    def __open_file(url: str) -> str:
        with open(url) as file:
            txt = file.read()
        return txt
