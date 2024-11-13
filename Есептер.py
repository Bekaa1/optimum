#Файлда әр жолда бір сан жазылған. Сізге файлдағы барлық сандардың қосындысын есептеу керек
#file = open('focus.txt', 'r+')
# a = file.readlines()
# print(a)
#
# summa = 0

# for i in a:
#     san = int(i)
#     summa += san
# print(summa)
#Файлдағы сандарды оқып, жұп және тақ сандарды бөлек файлдарға жазыңыз.


#Файлдан мәтінді оқып, онда қанша сөз бар екенін анықтаңыз. Әрбір жолды оқып, сөздерді санап шығыңыз
# file = open('focus.txt', 'r+')
#
# a = file.read()
# summa_symbol = 0
# for i in a:
#     summa_symbol += 1
# print(summa_symbol)
#
# file.close()


#Файлдан әрбір жолды оқып, егер жол бос болса (ешқандай символ болмаса), оны есептеп, жалпы қанша бос жол бар екенін анықтаңыз

file = open('focus.txt', 'r+')
result = file.readlines()

count = 0
for i in result:
    if i == '\n':
        count += 1

print(count)
