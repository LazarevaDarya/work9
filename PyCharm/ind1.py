#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
from datetime import date

import sys


if __name__ == '__main__':
    workers = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            surname = input("Фамилия: ")
            name = input("Имя: ")
            number = int(input("Номер телефона: "))
            date_obj = input("Дата рождения: ").split('.')

            worker = {
                'surname': surname,
                'name': name,
                'number': number,
                'date_obj': date_obj,
            }

            workers.append(worker)
            if len(workers) > 1:
                workers.sort(key=lambda item: item.get('name', ''))

        elif command == 'list':
            for num, elem in enumerate(workers):
                print(f"{num+1}.\n{str(elem['surname'])} {str(elem['name'])}\n"
                          f"Номер телефона: {str(elem['number'])}\nДата рождения: {elem['date_obj']}")

        elif command.startswith('select'):
            surname = input("Введите фамилию: ")
            for elem in workers:
                if elem['surname'] == surname:
                    print(f"Имя {str(elem['name'])}\nНомер телефона: {str(elem['number'])}\n"
                          f"Дата рождения: {elem['date_obj']}")
                    break
                else:
                    print("Фамилии не найдено")

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить человека;")
            print("list - вывести список всех людей;")
            print("select - найти данные по фамилии;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
