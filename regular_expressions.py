from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding='utf8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
for i in contacts_list:
    for q in i:
        text = q
        pattern_phone = re.compile(r'(\+7|8|)(\d+)|\(\d+\)|\s*\d+\s|\d+\s*\s*\d[\s-]\d+[\s-]\d+|\(доб\.\s*\d+\)|доб\.\s\d+')
        pattern_emails = re.compile(r'(\w*@\w*\.ru)')
        pattern_organization = re.compile(r'(Минфин|ФНС)')
        pattern_eployers = re.compile(r'(^[А-Яа-я]+).([А-Яа-я]+).([А-Яа-я]+)')
# TODO 2: сохраните получившиеся данные в другой файл


def csv_writer(data, path):
    with open(path, "w", newline='') as csv_file:
        '''
        csv_file - объект с данными
        delimiter - разделитель
        '''
        writer = csv.writer(csv_file, delimiter=';')
        for line in data:
            writer.writerow(line)


if __name__ == "__main__":
    data = [['lastname',',firstname','firstname','surname','organization','position','phone','email'],

    path = "output.csv"
    csv_writer(data, path)