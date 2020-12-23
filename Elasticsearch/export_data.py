from utils import *
import json

if __name__ == '__main__':
    final_data = []
    court = "_all"
    reason = '公然侮辱'
    fuzzy = False
    temp_data = True
    size = 5000
    start = 0
    while temp_data:
        temp_data = get_judgemet(court, reason, start, size, fuzzy)
        start += size
        final_data.extend(temp_data)
    with open('{}_{}.json'.format(court, reason), 'w', encoding='utf-8') as out:
        out.write(json.dumps(final_data, ensure_ascii=False))