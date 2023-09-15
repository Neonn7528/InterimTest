import csv
import datetime

def editNote():
    note_id = input("Какую по счету заметку вы хотите отредактировать? ")

    with open("note.csv", "r") as file:
        reader = csv.reader(file, delimiter=';')
        notes = list(reader)

    note_found = False
    for i, note in enumerate(notes):
        if note_id == str(i+1):
            print(f"Заметка найдена. Ее заголовок: {note[0]}.")
            new_chapter = input("Введите новый заголовок заметки: ").title()
            new_content = input("Введите новое содержание заметки: ").title()
            note[0] = new_chapter
            note[1] = new_content
            note[2] = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
            note_found = True
            break

    if note_found:
        with open("note.csv", "w", newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows(notes)
        print("Заметка успешно отредактирована!\n")
    else:
        print("Заметка с указанным идентификатором не найдена!\n")