from utils.ParseFile import ParseFile

try:
    parsed_data = ParseFile.parse_file('./input.txt')
except Exception as ex:
    print(ex)
