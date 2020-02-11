import re
import csv

with open("phonebook_raw.csv", encoding='utf8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
result = []
for text in contacts_list:  # list with all stings from original file!!!
    # formating one by one
    contact = []
    fio = ' '.join(text[0:2])  # getting lastname, surname and firstname in a single string(first three fields)
    employer_fio = re.findall(r'([А-Яа-я]+)', fio)  # finding all the words in russian language by findall
    while len(employer_fio) < 3:  # if fields lastname, surname and firstname < then 3 then we put the mark '-' in there
        employer_fio.append('-')
    contact += employer_fio
    # then we deal with some other field, for example organization:
    pattern_organization = re.compile(r'(Минфин|ФНС)')
    text_organization = pattern_organization.sub(r'\1', text[3])
    contact.append(text_organization)
    # after finding the position:
    pattern_position = re.compile(
        r'(главный специалист – эксперт отдела взаимодействия с федеральными органами власти Управления '
        r'налогообложения имущества и доходов физических лиц|cоветник отдела Интернет проектов Управления '
        r'информационных технологий)'
    )
    text_position = pattern_position.sub(r'\1', text[4])
    contact.append(text_position)
    pattern_phone = re.compile(r"(\+7|7|8)[\s\(]*(\d+)[\)\s]*(\d+)-?(\d+)-?(\d+)\s?(\(?доб.\s\d{1,4}\)?)?")
    # better to compile the regex on regex101.compile
    pattern_emails = re.compile(r'([^@]@[^@].ru)')  # compiling the e-mails
    text_emails = pattern_emails.sub(r'1', text[6])
    contact.append(text_emails)
    print(text_emails)
    result.append(contact)
# saving the all the regexed strings in regex and writting in new csv file
with open('phonebook.csv', 'w') as csv_file:
    the_writer = csv.writer(csv_file, delimiter=',')
    q = ['lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email']
    the_writer.writerow(q)
    for row in result:
        the_writer.writerow(row)
        
# so the job is done
