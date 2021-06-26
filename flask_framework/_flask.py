import json
from datetime import timedelta

from flask import jsonify ,Flask,request
from flask import render_template

# with open('static/json/data1.json', 'r', encoding='utf-8-sig') as load_f:
#    data1 = json.load(load_f)
# with open('static/json/data2.json', 'r', encoding='utf-8-sig') as load_f:
#    data2 = json.load(load_f)
# with open('static/json/data3.json', 'r', encoding='utf-8-sig') as load_f:
#    data3 = json.load(load_f)
# with open('static/json/data4.json', 'r', encoding='utf-8-sig') as load_f:
#    data4 = json.load(load_f)
# with open('static/json/data5.json', 'r', encoding='utf-8-sig') as load_f:
#    data5 = json.load(load_f)
app = Flask (__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
@app.route('/', methods=["GET"])
def index():
     return render_template("echart.html")

# @app.route('/myChart1', methods=["GET"]) #echarts 名字可以改为任意，但一定要与HTML文件中一至
# def echarts1():
#    return jsonify(data1 = data1)
#
# @app.route('/myChart2', methods=["GET"]) #echarts 名字可以改为任意，但一定要与HTML文件中一至
# def echarts2():
#    return jsonify(data2 = data2)
#
# @app.route('/myChart3', methods=["GET"]) #echarts 名字可以改为任意，但一定要与HTML文件中一至
# def echarts3():
#    return jsonify(data3 = data3)
#
# @app.route('/myChart4', methods=["GET"]) #echarts 名字可以改为任意，但一定要与HTML文件中一至
# def echarts4():
#    return jsonify(data4 = data4)
#
# @app.route('/myChart5', methods=["GET"]) #echarts 名字可以改为任意，但一定要与HTML文件中一至
# def echarts5():
#    return jsonify(data5 = data5)

# @app.route('/echarts', methods=["GET"])

app.run()