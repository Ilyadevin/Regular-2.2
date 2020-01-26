from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv

import pattern as pattern

with open("phonebook_raw.csv", encoding='utf8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)
# TODO 1: выполните пункты 1-3 ДЗ
for index in contacts_list:
    for text in index:
        pattern_phone = re.compile(r'\+7|8\s|(495)|[\s]\s|(913|983|748)\D*(\d+)\D*(\d{2})|\s(2926|0792)')
        pattern_emails = re.compile(r'(\w*@\w*\.ru)')
        pattern_organization = re.compile(r'(Минфин|ФНС)')
        pattern_eployers = re.compile(r'(^[А-Яа-я]+).([А-Яа-я]+).([А-Яа-я]+)')
        pattern_position = re.compile(r'(главный специалист – эксперт отдела взаимодействия с федеральными органами '
                                      r'власти Управления налогообложения имущества и доходов физических лиц|cоветник '
                                      r'отдела Интернет проектов Управления информационных технологий)')
        text_phone = pattern_phone.sub(r'+7 (\1)\2-\3-\4 доб.\5', text)
        text_last_name = pattern_eployers.sub(r'\1', text)
        text_fist_name = pattern_eployers.sub(r'\2', text)
        text_surname_name = pattern_eployers.sub(r'\3', text)
        text_organization = pattern_organization.sub(r'\1', text)
        text_emails = pattern_emails.sub(r'1', text)
        text_position = pattern_position.sub(r'\1', text)
# TODO 2: сохраните получившиеся данные в другой файл
        with open("phonebook.csv", "w") as f:
            tittle_names = ['lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email']
            the_writer = csv.DictWriter(f, fieldnames=tittle_names)
            the_writer.writeheader()
            the_writer.writerow({'lastname': text_last_name,
                                 'firstname': text_fist_name,
                                 'surname': text_surname_name,
                                 'organization': text_organization,
                                 'position': text_position,
                                 'phone': text_phone,
                                 'email': text_emails})

