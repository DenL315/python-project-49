### Hexlet tests and linter status:
[![Actions Status](https://github.com/DenL315/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/DenL315/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/edb7e042d81efe3c42cc/maintainability)](https://codeclimate.com/github/DenL315/python-project-49/maintainability)

«Игры разума» — набор из пяти консольных игр, построенных по принципу популярных мобильных приложений для прокачки мозга. Каждая игра задает вопросы, на которые нужно дать правильные ответы. После трех правильных ответов считается, что игра пройдена. Неправильные ответы завершают игру и предлагают пройти ее заново. Игры:
1. Калькулятор. Арифметические выражения, которые необходимо вычислить.
Запуск командой: Brain-calc
<a href="https://asciinema.org/a/FoPHtOxa8Sws5aQAuI2KW2ieT" target="_blank"><img src="https://asciinema.org/a/FoPHtOxa8Sws5aQAuI2KW2ieT.svg" /></a>
2. Определение четного числа.
Запуск командой: Brain-even
<a href="https://asciinema.org/a/Ihtbc3Huhm3l62Ws6mNO57Sgr" target="_blank"><img src="https://asciinema.org/a/Ihtbc3Huhm3l62Ws6mNO57Sgr.svg" /></a>
3. Определение наибольшего общего делителя. 
Запуск командой: Brain-gcd
<a href="https://asciinema.org/a/aThUX7cxPOdcDbAodXSCtqzAf" target="_blank"><img src="https://asciinema.org/a/aThUX7cxPOdcDbAodXSCtqzAf.svg" /></a>
4. Определение простого числа.
Запуск командой: Brain-prime
<a href="https://asciinema.org/a/88bcARkvuMXVJYjP66RdZIjwb" target="_blank"><img src="https://asciinema.org/a/88bcARkvuMXVJYjP66RdZIjwb.svg" /></a>
5. Прогрессия. Поиск пропущенных чисел в последовательности.
Запуск командой: Brain-progression
<a href="https://asciinema.org/a/CybPbJSk7AdM5ZwYbrIZHCjwr" target="_blank"><img src="https://asciinema.org/a/CybPbJSk7AdM5ZwYbrIZHCjwr.svg" /></a>

Инструкция по установке игр:
1. Скопируйте данный репозиторий на локальный компьютер: git@github.com:DenL315/python-project-49.git
2. Выполнить следующие команды:
 - make install
 - make build
 - make package-install

Системные требования для работы игр:
CPython: не ниже 3.10;
prompt:  не ниже 0.4.1;
poetry:  не ниже 1.7.1;
flake8:  не ниже 6.1.0.

Для проверки кода на наличие ошибок, проблем со стилем и сложностью необходимо выполнить команду:
 - make lint.