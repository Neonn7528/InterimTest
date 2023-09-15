import csv

def deleteNote():
    note_id = input("Какую по счету заметку вы хотите удалить? ")

    with open("note.csv", "r") as file:
        reader = csv.reader(file, delimiter=';')
        notes = list(reader)

    note_found = False
    for i, note in enumerate(notes):
        if note_id == str(i+1):
            print(f"Заметка найдена. Ее заголовок: {note[0]}.")
            confirmation = input("Вы уверены, что хотите удалить эту заметку? (y/n): ")
            if confirmation.lower() == "y":
                del notes[i]
                note_found = True

    if note_found:
        with open("note.csv", "w", newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows(notes)
        print("Заметка успешно удалена!\n")
    else:
        print("Отмена удаления или нет такой заметки!\n")