import csv
import datetime
import csv

def addingNote():
    chapter = input("Введите название заметки: ").title()
    content = input("Введите содержание заметки: ").title()

    if chapter.strip() == '' or content.strip() == '':
        print("Заметка не может быть пустой!\n")
        return
    now = datetime.datetime.now()
    timestamp = now.strftime("%d.%m.%Y %H:%M")

    with open("note.csv", "a", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([chapter, content, timestamp])

    print("Заметка успешно сохранена!\n")