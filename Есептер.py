#Файлда әр жолда бір сан жазылған. Сізге файлдағы барлық сандардың қосындысын есептеу керек
#
# summa = 0
# for i in file:
#     san = int(i)
#     summa += san
# print(summa)
#


#Файлдағы сандарды оқып, жұп және тақ сандарды бөлек файлдарға жазыңыз.
# file_taktar = open('taktar', 'w')
# file_zhuptar = open('zhuptar', 'w')
#
# for i in file:
#     san = int(i)
#
#     if san % 2 == 0:
#         file_zhuptar.write(str(f"{san}\n"))
#     else:
#         file_taktar.write(str(san))
#


#
# file_zhuptar.close()
# file_taktar.close()


#Файлдан мәтінді оқып, онда қанша сөз бар екенін анықтаңыз. Әрбір жолды оқып, сөздерді санап шығыңыз

# sozder_somasy = 0
# for i in file:
#     soz = i.split(',')
#     sozder_somasy += len(soz)
# print(sozder_somasy)
#Файлдан әрбір жолды оқып, егер жол бос болса (ешқандай символ болмаса), оны есептеп, жалпы қанша бос жол бар екенін анықтаңыз


# bos_oryn_sany = 0
# for i in file:
#     if i.strip() == '':
#         bos_oryn_sany += 1
# print(bos_oryn_sany)


file = open('focus_online')



file.close()
