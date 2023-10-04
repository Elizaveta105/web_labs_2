from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
    return'''
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
    <link rel="stylesheet"  href="'''+ url_for('static', filename='lab1.css')+'''">
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <h3>
        <ol>
            <li>
                <a href="/lab1" target="_blank">Лабораторная работа 1</a>
            </li>
        </ol>
        </h3>

        <br><br>
        <footer>
            &copy; Якунина Елизавета, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
'''  

@app.route("/lab1")
def lab1():
    return'''
<!doctype html>
<html>
    <head>
        <title>Якунина Елизавета Владимировна, лабораторная 1</title>
    </head>
    <body>
    <link rel="stylesheet"  href="'''+ url_for('static', filename='lab1.css')+'''">
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <br>
        <div>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов Werkzeug, 
            а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </div>

        <h1><a href="http://127.0.0.1:5000/menu">Меню</a><br></h1>

        <h2>Реализованные роуты:</h2>

        <h3>
        <ul>
            <li>
                <a href="http://127.0.0.1:5000/lab1/oak">/lab1/oak - Дуб</a><br><br>
            </li> 
            <li>
                <a href="http://127.0.0.1:5000/lab1/student">/lab1/student - Студент</a><br><br>
            </li> 
            <li>
                <a href="http://127.0.0.1:5000/lab1/python">/lab1/python - Python</a><br><br>
            </li>
            <li>
                <a href="http://127.0.0.1:5000/lab1/nsk">/lab1/nsk - Новосибирск</a><br>
            </li>
        </ul>
        </h3>        

        <br><br>
        <footer>
            &copy; Якунина Елизавета, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
'''

@app.route('/lab1/oak')
def oak():
    return'''
<!doctype html>
<html>
    <body>
    <link rel="stylesheet"  href="'''+ url_for('static', filename='lab1.css')+'''">
        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='oak.jpg') + '''">
    </body>
</html>
'''

@app.route('/lab1/student')
def student():
    return'''
<!doctype html>
<html>
    <body id="student">
    <link rel="stylesheet"  href="'''+ url_for('static', filename='lab1.css')+'''">
        <h1>Студент: Якунина Елизавета Владимировна</h1>
        <img src="''' + url_for('static', filename='logo.jpg') + '''">
    </body>
</html>
'''

@app.route('/lab1/python')
def python():
    return'''
<!doctype html>
<html>
    <body id="python">
    <link rel="stylesheet"  href="'''+ url_for('static', filename='lab1.css')+'''">
        <h1>Python</h1>

        <div>
        <b>Python</b> - это высокоуровневый язык программирования, который был разработан в конце 1980-х годов 
        Гвидо ван Россумом. Python имеет простой и понятный синтаксис, что делает его очень доступным для новичков 
        в программировании. Он также является интерпретируемым языком, что означает, что код может быть выполнен непосредственно 
        без необходимости компиляции.
        </div><br>
        
        <div>
        Python широко используется во многих областях, таких как наука о данных, машинное обучение, веб-разработка, 
        научные исследования, игровая индустрия и многое другое. Он также имеет огромное сообщество разработчиков, которые создают 
        и поддерживают множество библиотек и фреймворков, что делает его еще более универсальным и мощным.
        </div><br>

        <div>
        Этот язык поддерживает различные парадигмы программирования, включая процедурное, объектно-ориентированное и 
        функциональное программирование. Он также имеет множество встроенных функций и библиотек, которые облегчают написание кода и 
        ускоряют разработку.
        </div><br>

        <img src="''' + url_for('static', filename='python.webp') + '''">
    </body>
</html>
'''

@app.route('/lab1/nsk')
def nsk():
    return'''
<!doctype html>
<html>
    <body id="nsk">
    <link rel="stylesheet"  href="'''+ url_for('static', filename='lab1.css')+'''">
        <h1>Новосибирск</h1>

        <div>
        <b>Новосибирск</b> — третий по численности населения город России, крупнейший город её азиатской части.
        Город является центром Новосибирской агломерации. Также это рупнейший торговый, деловой, культурный, 
        транспортный, образовательный и научный центр Сибири.
        </div><br>

        <div>
        Новосибирск основан в 1893 году, статус города получил 28 декабря 1903 (10 января 1904) года. Численность населения — <b>1 635 338</b>
        человек (2023 г.), благодаря чему он является самым многонаселённым городом азиатской части России и самым большим 
        в России муниципальным образованием — городом без статуса субъекта Российской Федерации.
        </div><br>

        <div>
        Город расположен на обоих берегах <i>Оби</i> рядом с Новосибирским водохранилищем, образованным на Оби, перегороженной 
        плотиной Новосибирской ГЭС. Территория города составляет 502,7 км².
        </div><br>

        <div>Одной из культурных достопримечательностей Новосибирска являются театры, среди которых наиболее известным считается 
        <i>Оперный театр</i>, ставший одним из символов Новосибирска. Его здание строилось с 1930-х годов, закончено в 1945 и является 
        крупнейшим в России. В 2004—2005 годах он прошёл масштабную реконструкцию.
        </div><br>

        <img src="''' + url_for('static', filename='nsk.jpg') + '''">
    </body>
</html>
'''

@app.route('/lab2/example')
def example():
    name = 'Елизавета Якунина'
    group = 'ФБИ-14'
    course = '3 курс'
    lr_number = 'Лабораторная работа 2'

    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
    ]

    return render_template('example.html', name=name, group=group, 
                           course=course, lr_number=lr_number, fruits=fruits)