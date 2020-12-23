# Flask

---

## Introduciton

Flask是Python的其中一個套件，主要是後端的框架。
後端框架意義在於，能夠協助讓Python這個語言，處理許多網頁後端傳輸資料上的規範以及操作。

而其最主要的特色就是輕量，若有接觸過其他語言的框架(ASP.NET、spring......)，Flask的輕量化特質就會非常凸顯，可以透過簡單的script，達成開發網頁後端。

當然輕量作為一個特色，他也有其優缺點，這部份就待後面大家接觸後再做說明。

## Requirements
Python3.6

Packages:
* Flask


## Basic Sample

<pre>
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
</pre>


## Plotly-js + Flask

透過運用python的視覺化套件，結合js版本，不需要自己撰寫javascript，即可簡單的將數據分析視覺化結合至flask上

