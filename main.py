import sys, csv
import phonenumbers

if len(sys.argv) > 1:
    target_file = sys.argv[1]
else:
    target_file = 'example.csv'

with open (target_file) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=':')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print('\t'+'Номер :' + ' '+ str (": ".join(row))+' : '+'Телефон')
            line_count += 1
        else:
            phone = []
            phone_deduplicated = []
            for match in phonenumbers.PhoneNumberMatcher(row["Information"], "RU"):
                phone.append(str(phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164)))
            for match in phonenumbers.PhoneNumberMatcher(row["Information"], "UA"):
                phone.append(str(phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164)))

            for i in phone:
                if i not in phone_deduplicated:
                    phone_deduplicated.append(i)

            print('\t' + str (line_count)  + ' : ' + '\t'+ str(row["Група"]) + ' : ' + str(row["Особа"])+ ' : ' + str(row["Позивний"]) +' : '+str(row["Громадянство"])+' : '+str(row["Information"]) + ' : ' + ' '.join(phone_deduplicated) )

        line_count += 1
    print('Processed '+ str(line_count) + ' lines.')
