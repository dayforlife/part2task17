user = "hello"
user_ = ''
while user_ != user:
    user_ = input("enter hello: ").lower()

google_office = [
    '1 - Google Kazakstan',
    '2 - Google Paris',
    '3 - Google Uar',
    '4 - Google Kyrgyzstan',
    '5 - Google San Francisco',
    '6 - Google Germany',
    '7 - Google Moscow',
    '8 - Google Sweden'
    ]
for x in google_office:
    print(x)

number_office = int(input('Enter number: '))
complaint = input('Write a complaint: ')

if number_office == 1:
    f = open('google_kazakstan.txt', 'a', encoding='utf-8')
    f.write(complaint)
    f.close()

if number_office == 2:
    f = open('google_paris.txt', 'a', encoding='utf-8')
    f.write(complaint)
    f.close()

if number_office == 3:
    f = open('google_uar', 'a', encoding='utf-8')
    f.write(complaint)
    f.close()

if number_office == 4:
    f = open('google_kyrgystan.txt', 'a', encoding='utf-8')
    f.write(complaint)
    f.close()

if number_office == 5:
    f = open('google_san_francisco.txt', 'a', encoding='utf-8')
    f.write(complaint)
    f.close()
    
if number_office == 6:
    f = open('google_germany.txt', 'a', encoding='utf-8')
    f.write(complaint)
    f.close()
    
if number_office == 7:
    f = open('google_moscow.txt', 'a', encoding='utf-8')
    f.write(complaint)
    f.close()

if number_office == 8:
    f = open('google_sweden.txt', 'a', encoding='utf-8')
    f.write(complaint)
    f.close()