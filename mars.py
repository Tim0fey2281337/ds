from flask import Flask, url_for

app = Flask(__name__, static_folder='static')


@app.route('/')
@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return """<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    Человечество вырастает из детства.<br>

                    <br>Человечеству мала одна планета.<br>

                    <br>Мы сделаем обитаемыми безжизненные пока планеты.<br>

                    <br>И начнем с Марса!<br>

                    <br>Присоединяйся!
                  </body>
                </html>"""


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>

                    <img src="{url_for('static', filename='im/mars.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">

                    <p>Вот она какая, красная планета.</p>
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <p><h1>Жди нас, Марс!</h1></p>
                    
                    <img src="{url_for('static', filename='img/mars.jpg')}" 
                        alt="здесь должна была быть картинка, но не нашлась">
                    
                    <div class="alert alert-primary" role="alert">
                        Человечество вырастает из детства
                    </div>
                    
                    <div class="alert alert-success" role="alert">
                        Человечеству мала одна планета.
                    </div>
                    
                    <div class="alert alert-danger" role="alert">
                        Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    
                    <div class="alert alert-warning" role="alert">
                        И начнем с Марса!
                    </div>
                    
                    <div class="alert alert-info" role="alert">
                        Присоединяйся!
                    </div>    
                  </body>
                </html>"""

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')