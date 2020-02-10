import re
import csv

with open("phonebook_raw.csv", encoding='utf8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
result = []
for text in contacts_list:
    pattern_phone = re.compile(r'\+7|8\s|(495)|[\s]\s|(913|983|748)\D*(\d+)\D*(\d{2})|\s(\d{4})')
    pattern_emails = re.compile(r'(\w*@\w*\.ru)')
    pattern_organization = re.compile(r'(Минфин|ФНС)')
    pattern_eployers = re.compile(r'(^[А-Яа-я]+).([А-Яа-я]+).([А-Яа-я]+)')
    pattern_position = re.compile(
        r'(главный специалист – эксперт отдела взаимодействия с федеральными органами власти Управления '
        r'налогообложения имущества и доходов физических лиц|cоветник отдела Интернет проектов Управления '
        r'информационных технологий)')
    text_phone = pattern_phone.sub(r'+7 (\1)\2-\3-\4 доб.\5', str(text))
    text_last_name = pattern_eployers.sub(r'\1' r'\2' r'\3', str(text))
    text_organization = pattern_organization.sub(r'\1', str(text))
    text_emails = pattern_emails.sub(r'1', str(text))
    text_position = pattern_position.sub(r'\1', str(text))
    result = [text_phone, text_last_name, text_organization, text_emails, text_position]
cleared_contacts = []
with open('phonebook.csv', 'a') as csv_file:
    the_writer = csv.writer(csv_file, delimiter=',')
    q = ['lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email']
    the_writer.writerow(q)
    for row in result:
        the_writer.writerow(result[1].split(','), result[2], result[4], result[0], result[3])
