# Обрезка ссылок с помощью сервиса BIT.LY

Скрипт для создания коротких ссылок и подсчету количества переходов по коротким ссылкам.

### Как установить

Python3 должен быть уже установлен. Затем используйте `pip` для установки зависимостей.

`pip install -r requirements.txt`

### Пример использования

```
python main.py https://yandex.ru/
---
http://bit.ly/3cl1lMa
```
```
python main.py http://bit.ly/3cl1lMa
---
Количество переходов по ссылке - 3
```

### Цель проекта

Код написан в образовательных целях