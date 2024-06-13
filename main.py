from flask import Flask, render_template
import  pandas as pd

app = Flask(__name__)

stations = pd.read_csv('data_small/stations.txt', skiprows=17,)
# 只需要前两项
stations = stations[['STAID', 'STANAME                                 ']]
@app.route('/')
def home():
    return render_template('home.html', data = stations.to_html())

@app.route('/api/v1/<station>/<date>')
def about(station, date):
    filename = 'data_small/TG_STAID' + str(station).zfill(6) + '.txt'
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10

    return {
        "station": station,
        "date": date,
        "temperature": temperature
    }

@app.route('/translate')
def translate():
    return render_template('translate.html')

@app.route('/api/v1/<word>')
def api(word):
    df = pd.read_csv('dictionary.csv')
    definition = df.loc[df['word'] == word]['definition'].squeeze()
    result_dictionary = {'word': word, 'definition': definition}
    return result_dictionary

# 确保当这个脚本文件被直接运行时，才会执行 app.run(debug=True) 这行代码
# 而在被导入时，这段启动代码不会执行 可导入这个脚本的其他方法使用
if __name__ == '__main__':
    app.run(debug=True)