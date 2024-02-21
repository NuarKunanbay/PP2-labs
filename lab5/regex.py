import re as chert
#1
pat = chert.compile('^[a]{1}[b]*$')

with open('row.txt', encoding='utf-8') as mycop:
    cont = mycop.read()
    print(pat.search(cont))
#в общем файл на русском, а паттерны на англе, поэтому лучше буду писать вручную кейсы
print(pat.search('abbbb'))

#2
pattern2 = chert.compile("^[a]{1}[b]{2,3}$")
print(pattern2.search("abbb"))
#3
pattern3 = chert.compile("[a-z]+[_]{1}")
print(pattern3.search("GFHBJKLUYTaoiinfsdj_hjcjkas"))
#4
pattern4 = chert.compile("[A-Z]{1}[a-z]+")
print(pattern4.search("Chetam"))
#5
pattern5 = chert.compile("^[a]{1}.+[b]{1}$")
print(pattern5.search("avjdfhjisgvhisdu$W^#%^#%&^&3b"))
#6
string = 'chet,am che.tam'
print(string.replace(' ', ':').replace('.', ':').replace(',', ':'))
#7
def snake_to_camel(snake):
    return chert.sub('_(.)', lambda x: x.group(1).upper(), snake)
print(snake_to_camel('salam_aleikum'))
#8
pattern8 = chert.compile('(?=[A-Z])')
print(chert.split(pattern8, 'SalamAleykum'))
#9
pattern = chert.compile('(?=[A-Z])')
print(pattern.sub(' ', 'SalamAleykum'))