
commands = ["/help", "/lowprice", "/highprice", "/bestdeal", "/history"]


res_ru = {
    "questions" : {
        "city": "Введите название города",
        "index": "По вашему запросу найдено несколько вариантов, выберите номер",
        "guests": "Укажите количество гостей",
        "check_in": "Выберите дату заезда",
        "check_out": "Выберите дату выезда",
        "count_hotels": "Количество отелей, которые необходимо вывести в результате (не больше 25)",
        "need_photo": "Выводить фотографии для каждого отеля? ('Да'/'Нет')",
        "count_photos": "Введите количество фотографий для каждого отеля (не больше 10)",
        "repeat_query": "Повторить запрос? (Да/Нет)",
        "price": "Введите диапазон цен в $ ('мин'-'макс')",
        "distance": "Введите диапазон расстояний от центра (км.) ('от'-'до')"
    },
    "error_msgs": {
        "ERROR_DATE": "Не правильно введена дата. Повторите попытку.",
        "ERROR_CITY_NOT_FOUND": "Введённый город не найден. Введите другой город.",
        "ERROR_NUMBER": "Не правильно выбран номер. Повторите попытку.",
        "ERROR_ADULTS": "Не правильно указано количество гостей! Повторите попытку.",
        "ERROR_HOTELS_COUNT": "Не правильно указано количество отелей! Повторите попытку.",
        "ERROR_PHOTOS_COUNT": "Не правильно указано количество фотографий! Повторите попытку.",
        "ERROR_COMMAND": "Не известная команда.",
        "ERROR_CITY": "Произошла ошибка при запросе данных о {0}",
        "ERROR_HOTELS": "Произошла ошибка при запросе данных об отелях!",
        "ERROR_PRICE": "Не правильно указан диапазон цен! Повторите попытку.",
        "ERROR_DISTANCE": "Не правильно указан диапазон расстояний! Повторите попытку.",
        "ERROR_CONNECTION": "Ошибка соединение с сервисом! Повторите попытку позже.",
        "ERROR_TIMEOUT": "Превышено время ошидания ответа от сервиса.",
        "ERROR_SEND_PHOTO": "Ошибка отправки фотографии {0} - {1}.",
    },
    "msgs": {
        "COMMANDS_LIST": "Возможные команды:\n{0}",
        "WELCOME": "Добрый день, {0} {1}\nВас приветствует бот покупки валюты... ",
        "SEARCHING": "Идёт поиск ... ",
        "CITY": "Город",
        "NAME": "Название",
        "PLACE": "Место",
        "HOTEL_NAME": "Наименование отеля",
        "ADDRESS": "Адрес",
        "DISTANCE_FROM_CENTER": "Удалённость от центра",
        "PRICE": "Цена за ночь",
        "TOTAL_PRICE": "Стоимость {0}{1} за {2} ночей",
        "KM": "км.",
        "HOTELS": "Отели",
        "CHECK_IN": "Дата заезда",
        "CHECK_OUT": "Дата выезда",
        "DATES": "Даты",
        "NO_INFO": "По вашему запросу ничего не найдейно!",
    }
}

res_en = {
    "questions": {
        "city": "Enter the name of the city",
        "index": "Multiple properties found for your search, please select a number",
        "guests": "Enter the number of guests",
        "check_in": "Select your check in date",
        "check_out": "Select the check out date",
        "count_hotels": "Number of hotels to display as a result (no more than 25)",
        "need_photo": "Whether to display photos for each hotel ('Да'/'Нет')",
        "count_photos": "Enter the number of photos for each hotel (no more than 10)",
        "repeat_query": "Repeate query? (Yes/No)",
        "price": "Enter price interval $ ('min'-'max')",
        "distance": "Enter distance interval from center (km.) ('low'-'high')"

    },
    "error_msgs" : {
        "ERROR_DATE": "Date entered incorrectly. Try again.",
        "ERROR_CITY_NOT_FOUND": "The entered city was not found. Enter another city.",
        "ERROR_NUMBER": "Number selected incorrectly. Try again.",
        "ERROR_ADULTS": "The number of guests is incorrect! Try again.",
        "ERROR_HOTELS_COUNT": "The number of hotels is incorrect! Try again.",
        "ERROR_PHOTOS_COUNT": "The number of photos is not correct! Try again.",
        "ERROR_COMMAND": "Unknown command.",
        "ERROR_CITY": "An error occurred while requesting information about {0}",
        "ERROR_HOTELS": "An error occurred while requesting hotels data",
        "ERROR_PRICE": "The price interval is incorrect! Try again.",
        "ERROR_DISTANCE": "The distance interval is incorrect! Try again.",
        "ERROR_CONNECTION": "Service connection error! Please try again later.",
        "ERROR_TIMEOUT": "Timed out waiting for a response from the service.",
        "ERROR_SEND_PHOTO": "Photo upload error {0} - {1}."
    },
    "msgs": {
        "COMMANDS_LIST": "Possible commands:",
        "WELCOME": "Hello, {0} {1}\nWelcome to the currency exchange bot... ",
        "SEARCHING": "Searching ... ",
        "CITY": "City",
        "NAME": "Name",
        "PLACE": "Place",
        "HOTEL_NAME": "Hotel name",
        "ADDRESS": "Address",
        "DISTANCE_FROM_CENTER": "Distance from the center",
        "PRICE": "Price per night",
        "TOTAL_PRICE": "Total price {0}{1} per {2} nights",
        "KM": "km.",
        "HOTELS": "Hotels",
        "CHECK_IN": "Check in date",
        "CHECK_OUT": "Check out date",
        "DATES": "Dates",
        "NO_INFO": "Nothing found for your request!",
    }
}

res = {"ru": res_ru, "en": res_en}
