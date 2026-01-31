from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home():
    return '<a href="/random_fact">Посмотреть случайный факт!</a>'\
    '<p></p>'\
    '<a href="/image">Котики и Царь Пушка!</a>'\
    '<p></p>'\
    '<a href="/secret">ЪI</a>'


@app.route("/random_fact")
def facts():
    facts_list=['Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.', 'Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.', 'Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время.', 'Согласно исследованию, проведенному в 2019 году, более 60% людей отвечают на рабочие сообщения в своих смартфонах в течение 15 минут после того, как они вышли с работы.', 'Один из способов борьбы с технологической зависимостью - это поиск занятий, которые приносят удовольствие и улучшают настроение.', 'Илон Маск утверждает, что социальные сети созданы для того, чтобы удерживать нас внутри платформы, чтобы мы тратили как можно больше времени на просмотр контента.', 'Илон Маск также выступает за регулирование социальных сетей и защиту личных данных пользователей. Он утверждает, что социальные сети собирают огромное количество информации о нас, которую потом можно использовать для манипулирования нашими мыслями и поведением.', 'Социальные сети имеют как позитивные, так и негативные стороны, и мы должны быть более осознанными в использовании этих платформ.']
    return f'<p>Интересный факт: {random.choice(facts_list)}</p>'\
    '<a href="/">На главную</a>'

@app.route("/image")
def img():
    return '<a href="/">На главную</a>'\
    '<p></p>'\
    '<img src="https://img.freepik.com/free-photo/adorable-looking-kitten-with-keyboard_23-2150886358.jpg?semt=ais_hybrid&w=740&q=80" alt="Image 1" />'\
    '<p></p>'\
    '<img src="https://gala-cat.ru/_nw/1/60257453.jpg" alt="Image 2">'\
    '<p></p>'\
    '<img src="https://s0.bloknot-voronezh.ru/thumb/850x0xcut/upload/iblock/509/0d1587dc21_7605080_8213488.jpg" alt="Image 3" />'\
    '<p></p>'\
    '<img src="https://image-thumbs.shafastatic.net/2192874035_310_430" alt="Image 3" />'\
    '<p></p>'\
    '<img src="https://www.ptichka.ru/data/cache/2018jan/13/00/49871_47205.jpg" alt="Image 3">'\
    '<p></p>'\
    '<img src="https://miska.ru/upload/resize_cache/iblock/61c/585_410_1/8jkzab3negar9ik9nhivpi2fs2k9s5iu.jpg" alt="Image 3">'\
    '<h3>Царь пушка!</h3>'\
    '<h4>Yandex</h4>'\
    '<iframe src="https://yandex.ru/map-widget/v1/?ll=37.618148%2C55.751524&mode=poi&poi%5Bpoint%5D=37.617918%2C55.751435&poi%5Buri%5D=ymapsbm1%3A%2F%2Forg%3Foid%3D97047998234&z=20.36" width="600" height="450" frameborder="1" allowfullscreen="true" style="position:relative;"></iframe>'\
    '<h5>Google</h5>'\
    '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d642.3441204038286!2d37.61804308730174!3d55.751523322806825!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x46b54a56d650b0d9%3A0xbd45ef206e0683d0!2z0KbQsNGA0Ywt0L_Rg9GI0LrQsA!5e0!3m2!1sru!2sru!4v1768932094857!5m2!1sru!2sru" width="600" height="450" frameborder="1" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'

@app.route("/secret")
def secret():
    def gen_pass(pass_length):
        elements = "+-/*!&$#?=@<>123456789"
        password = ""
        for i in range(pass_length):
            password += random.choice(elements)
        return password
    text_password = gen_pass(10)
    return "<h1>Ты нашёл тайную страницу!</h1>"\
    '<p>Ты молодец! Я тебе сделаю случайный пароль...'\
    f'<p>{text_password}</p>'\
    '<a href="/">На главную</a>'
  


app.run(debug=True)