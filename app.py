from flask import Flask
from flask import request
import json
import flask
from flask import render_template
from flask import session

# to create an Application object
# we can also set routes for static files
app = Flask(
    __name__,
    static_folder = 'static', 
    static_url_path = '/static' 
) 
# static_folder 是放置靜態檔案的資料夾名稱，實務上這個資料夾名稱也常常被命名為 public

# static_url_path 是靜態檔案對應的網址路徑
# 所有在 static_folder 資料夾內的檔案，都對應到：路徑網址/檔案名稱

app.secret_key ="any thing but secret"
# 設定 session 秘鑰



@app.route("/en")
def index_english():
    return json.dumps({
            'status':'ok',
            'text':'hello world'
    })

@app.route("/zh")
def index_chinese():
    return json.dumps({
            'status':'ok',
            'text':'您好，歡迎光臨'
        },ensure_ascii=False)
# ensure_ascii=False->不要用ascii 處理中文


@app.route('/')
def index():
    # print('請求方法', request.method)
    # print('通訊協定', request.scheme)
    # print('主機名稱', request.host)
    # print('路徑', request.path)
    # print('完整網址', request.url)
    print('作業系統和瀏覽器', request.headers['user-agent'])
    # print('語言偏好', request.headers['accept-language'])
    # print('引薦網址', request.headers.get('referrer'))
    

    # 類似多語系的設定，依據使用者瀏覽器的語言偏好，回應不同內容
    lang=request.headers.get('accept-language')
    if lang.startswith('en'):
        return flask.redirect('/en')
    else:
        return flask.redirect('/zh')



# 建立路徑 /getSum 對應的處理函式
# 藉由 Query String 提供彈性
# 利用 request.headers.get() 來取得前端請求的參數值
@app.route('/getSum')
def getSum():
    maxNumber = request.args.get('max',100)
    maxNumber = int(maxNumber)

    minNumber = request.args.get('min',1)
    minNumber = int(minNumber)

    result=0
    for n in range(minNumber, maxNumber+1):
        result+=n
    return 'result '+str(result)



@app.route('/data')
def handle_data():
    return 'my data'

# dynamic routes
# note: use '< >' instead of '{ }'
@app.route('/user/<username>')
def handle_user(username):
    if username=='archer':
        return '你好'+ username
    else:
        return 'hello'+ username




# 使用樣版引擎
# 之所以要用樣板引擎，是因為要動態帶入資料
# 利用"{{variable}}"，帶入資料

@app.route('/example')
def handle_example():
    return render_template('example', name='ARCHER')
# 注意：render_template() 內放的參數就是
# templates資料夾內的檔案名稱


@app.route('/home')
def handle_home():
    
    return render_template('index.html', guest='ARCHER')

@app.route('/second')
def handle_second():
   
    return render_template('second.html')




@app.route('/calculate')
def handle_calculate():
    max_number= request.args.get('max','')
    max_number=int(max_number)
    result=0
    for n in range(1,max_number+1):
        result+=n
    return 'The result is ' +str(result)
# 記得要把 result 轉為字串，否則會出錯，數字無法和字串串接


# 利用 POST 方法來保護使用者傳送的機密資訊
# 如果不是機密資訊，則 POST/ GET 方法都可以，
# 團隊可以討論，看tech lead 怎麼決定
@app.route('/signup', methods=['POST'])
def handle_signup():
    first_name = request.form['first']
    print(first_name)
    return "Welcome " + first_name


@app.route('/hello')
def handle_hello():
    name=request.args.get('name','')
    session['username']=name
    
    return 'hello '+ name

@app.route('/talk')
def handle_talk():
    name=session['username']
     
    return name + ', nice to meet you '


# 啟動伺服器
# 可以利用參數 port 來指定阜號
app.run(port=3000)





