# Elasticsearch

---

## Introduction

Elasticsearch簡單來說，是一套開源式的分散式搜尋引擎。搜尋引擎，顧名思義就是可以幫忙處理搜尋的演算法；Elasticsearch主要包含了： 1. 儲存 2. 搜尋這兩項主要功能。
說到這邊大家一定會想說，SQL類型或NOSQL資料庫，不是也可以有儲存以及搜尋兩個功能。這邊要特別提的是，elasticsearch他的搜尋功能，是基於Apache lucene，並且符合RESTFUL格式，因此搜尋的效能與方式皆是非常優秀的。

而除了效能上的優越，elasticsearch建構以及使用上也非常友善，具有可擴充性 (scalability) 與可用性 (availability)。
可擴充性在筆者的想法是，因為作為一個開源程式碼，elasticsearch有許多可以擴充的plugin，架構上也是非常適合擴充規模；可用性則是前面提到，因為其建構及使用上的簡單且符合規範，一般有接觸過NOSQL或是RESTFUL API的使用者都可以很快的使用。

## API

透過API，我們可以操作幾乎所有的Elasticsearch，不管是建構資料、系統設定等等。
其中API，可以參考官方的[API文件](https://www.elastic.co/guide/en/elasticsearch/reference/current/rest-apis.html)



## Python Client

python的elasticsearch client，其實透過python，去進行API的request。

這部分其實可以透過自己撰寫，或是利用別人寫好的[套件](https://elasticsearch-py.readthedocs.io/en/7.10.0/)