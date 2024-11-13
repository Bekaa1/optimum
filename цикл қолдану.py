# Файлды оқу үшін ашу
file = open('input.txt', 'a')
file.close()
input_file = open("input.txt", "r")

# Файлдағы барлық жолдарды оқу және экранға шығару
for line in input_file:
    print(line.strip())  # Жолдың соңындағы бос орындарды жоямыз
# Файлды жабу
input_file.close()


# # Файлды оқу үшін ашу
input_file = open("numbers.txt", "r")

# Сандардың қосындысын сақтау үшін айнымалы
total_sum = 0

# Файлдағы барлық сандарды оқып, қосындысын есептеу
for line in input_file:
    number = int(line.strip())  # Жолды санға айналдыру
    total_sum += number  # Қосындыға қосу

# Нәтижені басып шығару
print(total_sum)

# Файлды жабу
input_file.close()


