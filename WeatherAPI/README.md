Это простой пакет API погоды
стэк: request, radis, ограничитель скорости

Возвращает информацию о температуре в моем прекрасном городе: максимальная/минимальная/средняя/почасовая температура

Процесс разработки:

0. .env окружение
1. Создается само АПИ:
2. Навешиваем рэдис
3. Ограничиваем скорость через рэдис
4. Тесты

key: FGYALYN7QTKBHNWV5VQF7XTTH


Запуск:

1. git clone ...
2. python -m venv venv
3. .\venv\Scripts\activate  
4. pip install -r .\WeatherAPI\requirements.txt
5. python -m WeatherAPI - enter.

P.S. Не злоупотребляйте запросами, я нарочно оставил APIkey сайта, чтобы те, кто будут смотреть могли что-то увидеть.

                
