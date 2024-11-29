# Словарь содержит информацию по набору url используемых в тестах
URLS = {
    'main_page_url': 'https://qa-scooter.praktikum-services.ru/',
    'order_page_url': 'https://qa-scooter.praktikum-services.ru/order'
}

# Словарь содержит информацию по ожидаемые ответы для каждого вопроса
VALID_ANSWERS = {
    0: 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
    1: 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',
    2: 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
    3: 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
    4: 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
    5: 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
    6: 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
    7: 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
}

# Словарь содержит информацию по плейсхолдерам полей заказа
PLACEHOLDER_CONTENT = {
    'name': '* Имя',
    'surname': '* Фамилия',
    'location': '* Адрес: куда привезти заказ',
    'metro_station': '* Станция метро',
    'tel_num': '* Телефон: на него позвонит курьер',
    'date': '* Когда привезти самокат',
    'comment': 'Комментарий для курьера'
}

# Словарь содержит данные по дням аренды
RENTAL_PERIOD_DICT = {
    1: 'сутки',
    2: 'двое суток',
    3: 'трое суток',
    4: 'четверо суток',
    5: 'пятеро суток',
    6: 'шестеро суток',
    7: 'семеро суток'
}

"""Словарь содержит статичные тестовые данные (идентичные для каждого из тестов), 
используемые в проверке в каждом  тесте"""
TEST_DATA = {
    'name': 'Андрей',
    'surname': 'Бубулик',
    'metro': 'Сокольники',
    'tel_num': '87771112233',
    'date': '01.12.2024',
    'comment': 'Позвонить за час'
}
