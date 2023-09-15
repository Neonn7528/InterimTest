import csv

def readNotes():
    with open("note.csv", "r") as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)  # Пропускаем заголовки колонок
        for row in reader:
            chapter = row[0]
            content = row[1]
            timestamp = row[2]
            print(f"Название: {chapter}")
            print(f"Содержание: {content}")
            print(f"Дата и время: {timestamp}")
            print("-" * 20)