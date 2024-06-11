from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/v1/<word>')
def about(word):
    definition = word.upper()
    return {
        "definition": definition,
        "word": word
    }

# 确保当这个脚本文件被直接运行时，才会执行 app.run(debug=True) 这行代码
# 而在被导入时，这段启动代码不会执行 可导入这个脚本的其他方法使用
if __name__ == '__main__':
    app.run(debug=True)