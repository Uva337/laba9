#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 8.Использовать словарь, содержащий следующие ключи: название пункта назначения; номер
# поезда; время отправления. Написать программу, выполняющую следующие действия:
# ввод с клавиатуры данных в список, состоящий из словарей заданной структуры; записи должны
# быть упорядочены по номерам поездов;
# вывод на экран информации о поезде, номер которого введен с клавиатуры; если таких поездов нет,
# выдать на дисплей соответствующее сообщение.

import sys
import json


if __name__ == '__main__':

    poezd = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break
        elif command == 'add':
            name = input("Название пункта назначения: ")
            num = int(input("Номер поезда: "))
            time = input("Время отправления: ")

            poez = {
                'name': name,
                'num': num,
                'time': time,
            }

            poezd.append(poez)
            if len(poezd) > 1:
                poezd.sort(key=lambda item: item.get('num', ''))

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
                    "Номер",
                    "Пункт назначения",
                    "Номер поезда",
                    "Время отправления"
                )
            )
            print(line)

            for idx, poez in enumerate(poezd, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>17} |'.format(
                        idx,
                        poez.get('name', ''),
                        poez.get('num', ''),
                        poez.get('time', 0)
                    )
                )

            print(line)

        elif command.startswith('select '):

            parts = command.split(' ', maxsplit=2)

            number = int(parts[1])

            count = 0
            for poez in poezd:
                if poez.get('num') == number:
                    count += 1
                    print('Номер поезда:', poez.get('num', ''))
                    print('Пункт назначения:', poez.get('name', ''))
                    print('Время отправления:', poez.get('time', ''))

            if count == 0:
                print("Таких поездов нет!")

        elif command.startswith('load '):
            parts = command.split(' ', maxsplit=1)

            with open(parts[1], 'r') as f:
                poez = json.load(f)

        elif command.startswith('save '):

            parts = command.split(' ', maxsplit=1)

            with open(parts[1], 'w') as f:
                json.dump(poez, f)

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить поезд;")
            print("list - вывести список поездов;")
            print("select <номер поезда> - запросить информацию о выбранном поезде;")
            print("help - отобразить справку;")
            print("load <имя файла> - загрузить данные из файла;")
            print("save <имя файла> - сохранить данные в файл;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
