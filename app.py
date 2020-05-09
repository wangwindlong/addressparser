# -*- coding: utf-8 -*-
import json

from flask import Flask, request
import addressparser

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    return "Hello World"


@app.route('/parse', methods=['POST'])
def parseaddress():
    data = request.get_json()
    result = []
    # print("parseaddress data={}".format(data))
    try:
        df = addressparser.transform(data)
    except Exception as e:
        print("parseaddress exception", e)
        return json.dumps(result, ensure_ascii=False)
    for map_key in zip(df["省"], df["市"], df["区"], df["地址"]):
        result.append(list(map_key))
    return json.dumps(result, ensure_ascii=False)


if __name__ == '__main__':
    app.run(debug=False)
