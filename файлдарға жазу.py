"""
Файлға мәлімет жазу үшін файлды "w" немесе "a" режимінде ашамыз.
"w" режимі файлдың бар мазмұнын өшіреді, ал "a" файлдың соңына жазады.
"""

# file = open("example.txt", "w")  # Файлды жазу режимінде ашамыз
# file.write("New text")

"""
Бинарлы файлдарды оқу немесе жазу үшін "rb" немесе 
"wb" режимдерін қолданамыз. Мысалы, сурет файлдарын оқу"""

file =  open("C:/Users/user/PycharmProjects/28-29 ПС файлдармен жұмыс/images/output (4).png", "ab")
content = file.read()
print(content)
file.close()

