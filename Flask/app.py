import json
import plotly as py
from flask import Flask, render_template
from parse_feature import *


app = Flask(__name__)

# 方法1 - server啟動前先load資料
with open('data.json', 'r', encoding='utf-8') as f:
    judgement_data = json.load(f)

money_no = [(judge['_source']['no'], parse_money(judge['_source']['mainText'].replace('仟', '千'))) for judge in judgement_data if parse_money(judge['_source']['mainText'])]

@app.route('/')
def index():
    # 設置圓餅圖資料
    court_count = get_feature_count(judgement_data, "court")
    values = [p[1] for p in court_count]
    labels = [p[0] for p in court_count]
    pie = {
        'values': values,
        'labels': labels,
        'type': 'pie'
    }

    # 將相關圖表物件以list方式寫入
    graphs = [
        dict(
            data=[
                pie
            ],
            layout=dict(
                width='100%',
                height='100%'
            )
        )
    ]

    # 序列化
    graphJSON = json.dumps(graphs, cls=py.utils.PlotlyJSONEncoder)

    # 回傳序列化後的資料以及當初處理好的數據
    return render_template('index.html', graphJSON=graphJSON, court_count=money_no)


if __name__ == '__main__':
    app.debug = True
    app.run()