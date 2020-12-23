import requests
import json
from elasticsearch import Elasticsearch
import re


def get_judgemet(court, reason, start, size, mode):
    """
    :param court:裁判法院. ex:臺灣士林地方法院、_all(全部)
    :param reason:犯罪理由，支援fuzzy. ex: 公然污辱、污辱
    :param mode:True - Fuzzy
    :return:
    """
    if not mode:
        reason = '"{}"'.format(reason)
    res = requests.get('http://140.112.153.64:3679/{court}/_search?q=reason:{reason}&from={start}&size={size}'.format(court=court, reason=reason, start=start, size=size),
                       headers={
                           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'})
    query_data = json.loads(res.content.decode('utf-8'))['hits']['hits']
    return query_data


def create_index(es, index_name):
    es = Elasticsearch()
    es.indices.create(index='index名稱')