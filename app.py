from flask import Flask, render_template, request
from bard_stocks import bardStocks

app = Flask(__name__)


@app.route('/intro')
def Introduce():
    return render_template('intro.html')

@app.route('/')
def DON():
    return render_template('DON.html')

@app.route('/result', methods = ['POST'])
def Result():
    if request.method == 'POST':
        item = request.form['Stocks']
        type = request.form['type']
        result = bardStocks(item, type)
        res1 = result[2].split('. ')
        res2 = result[-1].split('. ')
        return render_template("result.html",  stock = result[0], option= result[1], res1 = res1, res2 = res2)




if __name__ == '__main__':
    app.run()

# flsk --debug run 으로 디버그 모드로 실행
