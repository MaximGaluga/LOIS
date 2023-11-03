import re


class ParseFile:
    __SETS_PATTERN = r'^[A-Z]+=\{\([a-z]\d,\d+\.\d+\)(?:,\([a-z]\d,\d+\.\d+\))*\}$'
    __IMPLICATIONS_PATTERN = r'^[A-Z]->[A-Z]$'
    __CASH = {
        "sets": {},
        "implications": []
    }

    @staticmethod
    def parse_file(url: str):
        txt = ParseFile.__open_file(url).replace(' ', '')
        sets = re.findall(ParseFile.__SETS_PATTERN, txt, re.MULTILINE)

        for current_set in sets:
            find_set_name = r'[A-Z]+'
            set_name = re.findall(find_set_name, current_set)
            ParseFile.__CASH["sets"][set_name[0]] = list()

            find_dataset = r'\([a-z]\d,\d+\.\d+\)'
            dataset = re.findall(find_dataset, current_set)

            for data in dataset:
                values = data.replace('(', '').replace(')', '')
                values = values.split(',')
                ParseFile.__CASH["sets"][set_name[0]].append((values[0], float(values[1])))

        implications = re.findall(ParseFile.__IMPLICATIONS_PATTERN, txt, re.MULTILINE)
        for implication in implications:
            values = implication.split('->')
            ParseFile.__CASH["implications"].append((values[0], values[1]))

        return ParseFile.__CASH

    @staticmethod
    def __open_file(url: str) -> str:
        with open(url) as file:
            txt = file.read()
        return txt
