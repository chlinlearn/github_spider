from flask import Flask,render_template,request

from spider import *

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'GET':
        language = 'python'
        # 获取github热门项目
        items, names = Spider().get_githubItems(language)
        return render_template('home.html', items=items,language = language)
    elif request.method == 'POST':
        language = request.form.get('inputLanguage')
        repoType = request.values.get('repoType')
        print(repoType)
        try:
            items, names = Spider().get_githubItems(language)
            return render_template('home.html', items=items,language = language)
        except:
            return render_template('home.html', msg = '未找到或者输入不符合规范！',language = language)


if __name__ == '__main__':
    app.run()
