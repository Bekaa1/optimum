# # Файлды оқу үшін ашу
# input_file = open("focus.txt", "r")
#
# output_file = open('output.txt', 'a+')
# # Файлдағы әрбір жолды оқу
# for line in input_file:
#     output_file.write(line)
#
# # Файлдарды жабу
# input_file.close()
# output_file.close()





# Файлдан сандарды оқу үшін ашу
input_file = open("focus.txt", "r")

# Жаңа файлды жазу үшін ашу
output_file = open("even_numbers.txt", "w")
file = open('output.txt', 'w')
for line in input_file:
    line = int(line)
    if line % 2 == 0:
        output_file.write(str(line))
        output_file.write('\n')
    else:
        file.write(str(line))
        file.write('\n')

# Файлдарды жабу
input_file.close()
output_file.close()

