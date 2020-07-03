from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__, template_folder='./static')
CORS(app, resource=r'/*')

import os
path=os.getcwd()
print('path:    '+path)
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/car')
def car():
    return render_template("car.html")


@app.route('/show')
def show():
    return render_template("show.html")


@app.route('/about')
def about():
    return render_template("example.html")


@app.route('/price', methods=['POST'])
def price():
    model = request.form.get('model')
    brand = request.form.get('brand')
    bodytype = request.form.get('bodytype')
    fueltype = request.form.get('fueltype')
    gearbox = request.form.get('gearbox')
    power = request.form.get('power')
    kilometer = request.form.get('kilometer')
    notrepaireddamage = request.form.get('notrepaireddamage')
    seller = request.form.get('seller')
    regioncode = request.form.get('regioncode')
    offertype = request.form.get('offertype')
    createdate = request.form.get('creatdate')
    regdate = request.form.get('regdate')

    import pandas as pd
    import numpy as np
    import datetime
    csv = pd.read_csv("data_for_tree.csv")
    v_0 = csv['v_0'].mean()
    v_1 = csv['v_1'].mean()
    v_2 = csv['v_2'].mean()
    v_3 = csv['v_3'].mean()
    v_4 = csv['v_4'].mean()
    v_5 = csv['v_5'].mean()
    v_6 = csv['v_6'].mean()
    v_7 = csv['v_7'].mean()
    v_8 = csv['v_8'].mean()
    v_9 = csv['v_9'].mean()
    v_10 = csv['v_10'].mean()
    v_11 = csv['v_11'].mean()
    v_12 = csv['v_12'].mean()
    v_13 = csv['v_13'].mean()
    v_14 = csv['v_14'].mean()
    saleid = csv['SaleID'].mean()
    name = csv['name'].mean()
    csv = csv[['brand', 'brand_amount', 'brand_price_max', 'brand_price_median', 'brand_price_min', 'brand_price_sum',
               'brand_price_std', 'brand_price_average']].sort_values(by=['brand']).drop_duplicates()
    for i, row in csv.iterrows():
        if int(float(row['brand'])) == int(brand):
            brand_amount = row['brand_amount']
            brand_price_max = row['brand_price_max']
            brand_price_median = row['brand_price_median']
            brand_price_min = row['brand_price_min']
            brand_price_sum = row['brand_price_sum']
            brand_price_std = row['brand_price_std']
            brand_price_average = row['brand_price_average']
            break
    car = {"SaleID": saleid, "name": name, "model": int(model), "brand": float(brand), "bodyType": float(bodytype),
           "fuelType": float(fueltype), "gearbox": float(gearbox), "power": int(power), "kilometer": float(kilometer),
           "notRepairDamage": int(notrepaireddamage), "seller": int(seller), "offerType": int(offertype), "v_0": v_0,
           "v_1": v_1, "v_2": v_2, "v_3": v_3, "v_4": v_4, "v_5": v_5, "v_6": v_6, "v_7": v_7, "v_8": v_8, "v_9": v_9,
           "v_10": v_10, "v_11": v_11, "v_12": v_12, "v_13": v_13, "v_14": v_14, "train": 1,
           "used_time": float((datetime.datetime.strptime(str(createdate), '%Y-%m-%d') - datetime.datetime.strptime(
               str(regdate), '%Y-%m-%d')).days), "city": float(str(regioncode)[:-3]),
           "brand_amount": float(brand_amount), "brand_price_max": float(brand_price_max),
           "brand_price_median": float(brand_price_median), "brand_price_min": float(brand_price_min),
           "brand_price_sum": float(brand_price_sum), "brand_price_std": float(brand_price_std),
           "brand_price_average": float(brand_price_average), "power_bin": int(power) / 10}
    car = pd.DataFrame([car])
    print(car)

    from finalResult import predict
    pri = predict(car)[0]
    return render_template('price.html', price=int(float(pri)))


@app.route('/brand_model/<int:brand>')
def brand_model(brand):
    import csv
    csv = csv.reader(open("brand_model.csv"))
    res = dict()
    temp = dict()
    for i in range(39):
        temp[str(i)] = []
    for row in csv:
        try:
            temp[(row[1])].append(row[2])
        except Exception:
            pass
    res['brand'] = str(brand)
    res['model'] = temp[str(brand)]
    for item in range(len(res['model'])):
        res['model'][item] = str(int(float(res['model'][item])))
    return jsonify(res)


@app.route('/getcitymax')
def getcitymax():
    import csv
    csv = csv.reader(open("data_for_tree_city.csv"))
    res = []
    for row in csv:
        if row[0] != "city":
            if row[0] == "":
                row[0] = "其他"
            res.append({"city": row[0], "max": row[1]})
    return jsonify(res)


@app.route('/getcitysum')
def getcitysum():
    import csv
    csv = csv.reader(open("data_for_tree_city.csv"))
    res = []
    for row in csv:
        if row[0] != "city":
            if row[0] == "":
                row[0] = "其他"
            res.append({"city": row[0], "sum": row[2]})
    return jsonify(res)


@app.route('/getcityaverage')
def getcityaverage():
    import csv
    csv = csv.reader(open("data_for_tree_city.csv"))
    res = []
    for row in csv:
        if row[0] != "city":
            if row[0] == "":
                row[0] = "其他"
            res.append({"city": row[0], "average": row[3]})
    return jsonify(res)


@app.route('/getbrandmax')
def getbrandmax():
    import csv
    csv = csv.reader(open("data_for_tree_brand.csv"))
    res = []
    for row in csv:
        if row[0] != "brand":
            if row[0] == "":
                row[0] = "其他"
            res.append({"brand": row[0], "max": row[1]})
    return jsonify(res)


@app.route('/getbrandsum')
def getbrandsum():
    import csv
    csv = csv.reader(open("data_for_tree_brand.csv"))
    res = []
    for row in csv:
        if row[0] != "brand":
            if row[0] == "":
                row[0] = "其他"
            res.append({"brand": row[0], "sum": row[2]})
    return jsonify(res)


@app.route('/getbrandaverage')
def getbrandaverage():
    import csv
    csv = csv.reader(open("data_for_tree_brand.csv"))
    res = []
    for row in csv:
        if row[0] != "brand":
            if row[0] == "":
                row[0] = "其他"
            res.append({"brand": row[0], "average": row[3]})
    return jsonify(res)


@app.route('/getmodelmax')
def getmodelmax():
    import csv
    csv = csv.reader(open("data_for_tree_model.csv"))
    res = []
    for row in csv:
        if row[0] != "model":
            if row[0] == "":
                row[0] = "其他"
            res.append({"model": row[0], "max": row[1]})
    return jsonify(res)


@app.route('/getmodelsum')
def getmodelsum():
    import csv
    csv = csv.reader(open("data_for_tree_model.csv"))
    res = []
    for row in csv:
        if row[0] != "model":
            if row[0] == "":
                row[0] = "其他"
            res.append({"model": row[0], "sum": row[2]})
    return jsonify(res)


@app.route('/getmodelaverage')
def getmodelaverage():
    import csv
    csv = csv.reader(open("data_for_tree_model.csv"))
    res = []
    for row in csv:
        if row[0] != "model":
            if row[0] == "":
                row[0] = "其他"
            res.append({"model": row[0], "average": row[3]})
    return jsonify(res)


@app.route('/gettotal')
def total():
    import pandas
    csv = pandas.read_csv('data_for_tree.csv')['price']
    max = csv.max()
    sum = csv.sum()
    average = csv.mean()
    return {"max": max, "sum": sum, "average": average}


if __name__ == '__main__':
    app.run()
