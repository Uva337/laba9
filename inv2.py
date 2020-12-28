#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Использовать словарь, содержащий следующие ключи: фамилия, имя; номер телефона;
# дата рождения. Написать программу, выполняющую следующие
# действия: ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
# записи должны быть упорядочены по трем первым цифрам номера телефона; вывод на
# экран информации о человеке, чья фамилия введена с клавиатуры; если такого нет, выдать
# на дисплей соответствующее сообщение.
import sys
import json


if __name__ == '__main__':

    people = []

    while True:
        command = input("> ").lower()

        if command == 'exit':
            break
        elif command == 'add':
            name = input("Фамилия, Имя: ")
            num = int(input("Номер телефона: "))
            year = input("Дата рождения в формате дд:мм:гггг:: ")

            peop = {
                'name': name,
                'num': num,
                'year': year,
            }

            people.append(peop)
            if len(people) > 1:
                people.sort(key=lambda item: item.get('num', '3'))

        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 17
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^17} |'.format(
                    "№",
                    "Фамилия, Имя",
                    "Номер телефона",
                    "Дата рождения"
                )
            )
            print(line)

            for idx, peop in enumerate(people, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>17} |'.format(
                        idx,
                        peop.get('name', ''),
                        peop.get('num', ''),
                        peop.get('year', 0)
                    )
                )

            print(line)

        elif command.startswith('select '):

            parts = command.split(' ', maxsplit=2)

            number = int(parts[1])

            count = 0
            for peop in people:
                if peop.get('num') == number:
                    count += 1
                    print('Номер телефона:', peop.get('num', ''), sorted(key=lambda x: int(str(x)[:3])))
                    print('Фамилия, Имя:', peop.get('name', ''))
                    print('Дата рождения:', peop.get('year', ''))

            if count == 0:
                print("Таких людей нет")

        elif command.startswith('load '):
            parts = command.split(' ', maxsplit=1)

            with open(parts[1], 'r') as f:
                people = json.load(f)

        elif command.startswith('save '):

            parts = command.split(' ', maxsplit=1)

            with open(parts[1], 'w') as f:
                json.dump(people, f)

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить поезд;")
            print("list - вывести список людей;")
            print("select <номер телефона> - запросить информацию по номеру телефона;")
            print("help - отобразить справку;")
            print("load <имя файла> - загрузить данные из файла;")
            print("save <имя файла> - сохранить данные в файл;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
