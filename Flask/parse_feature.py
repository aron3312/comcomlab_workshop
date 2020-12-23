import re
import json
import chinese2digits as c2d


def parse_money(text):
    check_parse = re.search('.*處罰金新臺幣(.+?)元.*', text)
    if check_parse:
        money_num = check_parse.group(1)
        return c2d.takeNumberFromString(money_num)['replacedText']


def get_feature_count(data, col):
    all_data = [single['_source'][col] for single in data]
    result = [(c, all_data.count(c)) for c in set(all_data)]
    return result