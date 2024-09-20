clients = [
    ['Василина Микитюк', 'провулок Петра Лещенка, буд. 523 кв. 70, Кременець, 88741', 41, 1],
    ['Єлисей Архимович', "узвіз Грецька, буд. 91, Зимогір'я, 91927", 54, 2],
    ['Ярослава Нестайко', 'парк Польовий 1-й, буд. 736, Бурштин , 41479', 23, 3],
    ['Богуслава Адамчук', 'вулиця Овідіопольська дорога, буд. 67 кв. 841, Ірміно, 07762', 53, 4],
    ['Анжела Уманець', 'вулиця Шахтинський, буд. 5, Бібрка, 10886', 46, 5],
    ['Бабко Тереза Веніяминівна', 'шосе Бригадна, буд. 603, Харків, 32057', 36, 6],
    ['Єва Шутько', 'парк Першотравневий 2-й, буд. 626 кв. 2, Часів Яр, 75588', 45, 7],
    ['Коваленко Прохір Єфремович', "узвіз Гагаріна, буд. 199 кв. 102, Куп'янськ, 85166", 51, 8],
    ['Герман Гаврюшенко', 'шосе Амурський 4-й, буд. 830 кв. 60, Теребовля, 53150', 26, 9],
    ['Наталія Величко', 'вулиця Утьосова, буд. 850 кв. 40, Андрушівка, 83872', 34, 10],
    ['Трохим Доценко', 'парк Вокзальний, буд. 75 кв. 8, Чернігів, 44698', 56, 11],
    ['Амалія Затула', 'провулок Грецький, буд. 36 кв. 9, Стебник, 20012', 28, 12],
    ['Валентин Петренко', 'сквер Олександра Невського, буд. 79, Благовіщенське, 87501', 23, 13],
    ['Альбіна Штепа', 'шосе Джерельна, буд. 41, Могилів-Подільський, 52248', 46, 14],
    ['Вікторія Алексійчук', 'узвіз Рівності, буд. 7, Мена , 89476', 21, 15],
    ['Богданна Василенко', 'узвіз Станційна 1-ша, буд. 02 кв. 0, Ічня, 55112', 56, 16],
    ['Ярина Піддубний', 'набережна Анни Ахматової, буд. 4 кв. 067, Бунге , 06871', 40, 17],
    ['Семен Закусило', 'площа Пересипська 8-ма, буд. 013, Лутугине, 93047', 23, 18],
    ['Данна Дерегус', 'вулиця Садова 6-та, буд. 639 кв. 52, Хуст, 88000', 56, 19],
    ['Мазепа Оксана Орестівна', 'набережна Азербайджан, буд. 529 кв. 15, Устилуг, 97729', 24, 20],
    ['Мілена Дубас', 'парк Героїв оборони Одеси, буд. 1 кв. 042, Бобровиця, 96367', 44, 21],
    ['Георгій Дейнека', 'шосе Троїцька, буд. 4 кв. 997, Чуднів, 52554', 32, 22],
    ['Галина Колісниченко', 'парк Савицький, буд. 67 кв. 410, Устилуг, 40922', 49, 23],
    ['Анастасія Архипенко', 'парк 1-ша Лінія Марії Демченко, буд. 9 кв. 387, Новодружеськ, 13148', 40, 24],
    ['Клавдія Гоголь-Яновський', 'площа Покровський, буд. 47 кв. 28, Кодима, 53683', 29, 25],
    ['Михайлина Закусило', 'площа Аркадіївський, буд. 569 кв. 142, Бахчисарай, 06061', 41, 26],
    ['Яків Дуплій', 'шосе Князівський, буд. 06, Шепетівка, 82791', 47, 27],
    ['Алла Засядько', 'шосе Світлий, буд. 3 кв. 5, Нетішин, 71634', 46, 28],
    ['Вікторія Байдак', 'узвіз Морський 2-й, буд. 0, Балта, 59419', 50, 29],
    ['Мирослав Власенко', 'набережна Мічманський 2-й, буд. 61, Борщів, 57881', 28, 30],
    ['Єлисавета Авраменко', 'узвіз Лобачевського, буд. 748 кв. 554, Шумськ, 43845', 39, 31],
    ['Шеремет Антон Омелянович', 'парк Пестеля, буд. 9, Червоноград, 06815', 21, 32],
    ['Ватаманюк Галина Русланівна', 'набережна Бородінська, буд. 39 кв. 64, Сєвєродонецьк, 67809', 59, 33],
    ['Юстина Ярош', 'сквер Прокатна, буд. 946 кв. 5, Луцьк, 70868', 24, 34],
    ['Василина Шамрай', 'парк Золотий берег, буд. 60 кв. 221, Южноукраїнськ, 09745', 49, 35],
    ['Юстина Рудько', 'набережна Ключовий 1-й, буд. 1 кв. 859, Зеленодольськ, 20582', 37, 36],
    ['Пріска Орлик', 'парк Міцкевича, буд. 44 кв. 32, Ялта, 41973', 28, 37],
    ['Данило Яремчук', 'проспект 5-та Суворовська, буд. 3 кв. 4, Жданівка, 24388', 51, 38],
    ['Богодар Перебийніс', 'узвіз Семінарська, буд. 22, Буча, 35788', 35, 39],
    ['Дмитро Гаврилишин', 'шосе Аптекарський, буд. 0 кв. 83, Синельникове, 06821', 58, 40],
    ['Ватаманюк Марія Аркадіївна', 'провулок Книжковий, буд. 233, Красилів, 57426', 56, 41],
    ['Чуйко Петро Петрович', 'площа Ткачова, буд. 3 кв. 79, Алупка, 86736', 29, 42],
    ['Світлана Стельмах', 'шосе Манежний, буд. 34 кв. 02, Калинівка , 85284', 33, 43],
    ['Амалія Данькевич', 'шосе Поперечний, буд. 996, Батурин, 51683', 32, 44],
    ['Марко Вовк', 'шосе Скляний 1-й, буд. 61, Перечин, 30237', 46, 45],
    ['Віра Данилюк', 'парк Ямчитського, буд. 393 кв. 0, Бібрка, 02567', 24, 46],
    ['Валерій Непорожній', 'вулиця Лінія 33-тя, буд. 77, Марганець , 35926', 51, 47],
    ['Одарка Талан', 'площа Богдана Хмельницького, буд. 9, Іллінці, 16593', 57, 48],
    ['Симон Ященко', 'узвіз Дальній, буд. 129, Переяслав, 63109', 50, 49],
    ['Ярослава Демʼяненко', 'набережна Чайковського, буд. 8, Зіньків, 69453', 51, 50]
 ]

rating_customers = []

commands = [
    "0. Вийти з програми",
    "1. Показати актуальний список клієнтів",
    "2. Клієнт виїжджає з номеру (надає оцінку обслуговування)",
    "3. Клієнт переїжджає в інший номер",
    "4. Новий клієнт",
    "5. Змінити дані користувача",
    "6. Відсортувати список клієнтів за ім'ям",
    "7. Відсортувати список клієнтів за віком",
    "8. Хто перебуває в номері",
    "9. Показати відгуки",
    "10. Показати вільні номери",
    "11. Забронювати номер"
]

while True:
    for command in commands:
        print(command)

    command = input("Введіть номер команди: ")

    if command == "0":
        print("Дякую за Вашу роботу. До побачення")
        break

    elif command == "1":
        for client in clients:
            print(f"Клієнт '{client[0]}' перебуває у кімнаті № {client[-1]}")

        input("\nНатисніть enter для продовження \n")

    elif command == "2":
        client_output = input("Введіть ім'я та призвіще клієнта: ")
        rating = input("Введіть рейтинг від користувача в діапазоні 0-5: ")

        for client in clients:
            if client_output in client[0]:
                break

        