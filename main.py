# from collections import namedtuple
# users = [
#     (1, "Toxir", "Toxirov", 12),
#     (2, "Sobir", "Sobirov", 15)
# ]
# Person = namedtuple("Person", ["id", "name", "lastname", "age"])
#
# for user in users:
#     person = Person(*user)
#     print(f"ID: {person.id} Name: {person.name} {person.lastname} Age: {person.age}")


# users = [
#     {"id": 1, "name": "Toxir","age": 12, "lastname": "Toxirov"},
#     {"id": 2, "name": "Sobir", "lastname": "Sobirov", "age": 15}
# ]
#
# Person = namedtuple("Person", ["id", "name", "lastname", "age"])
# for user in users:
#     person = Person(**user)
#     print(f"ID: {person.id} Name: {person.name} {person.lastname} Age: {person.age}")


#=========================================================================================
# 10.12.2024 4 OY 6 DASR UYGA VAZIFASI

# 1 vazifa

# from collections import namedtuple
#
# Talabalar = []
# Person = namedtuple("Person", ["id", "name", "lastname", "age"])
# count = 0
# for i in range(1,4):
#     count += 1
#     name = input(f"{count}. Talabani ismni kiriting: ")
#     lastname = input(f"{count}.Talabani familiyasini kiriting: ")
#     age = input(f"{count}.Talabani yoshini kiriting: ")
#     Talabalar.append({"id": count, "name": name, "lastname": lastname, "age": age })
#     print(Talabalar)
# for talaba in Talabalar:
#     person = Person(**talaba)
#     print(f"ID: {person.id} Name: {person.name} {person.lastname} Age: {person.age}")


#--------------------------------------------------------------------------------------------------

# 2 vazifa
#
# from collections import namedtuple
#
# Maxsulotlar = []
# Person = namedtuple("Person", ["id", "product_name", "price", "quantity"])
# count = 0
# for i in range(1,4):
#     count += 1
#     product_name = input(f"{count}. Mahsulotni nomini kiriting: ")
#     price = input(f"{count}.Mahsulotni narxini kiriting: ")
#     quantity = input(f"{count}.Mahsulotni miqdorini kiriting: ")
#     Maxsulotlar.append({"id": count, "product_name": product_name, "price": price, "quantity": quantity })
#     print(Maxsulotlar)
# for mahsulot in Maxsulotlar:
#     person = Person(**mahsulot)
#     print(f"{person.id}. Nomi: {person.product_name}, Narxi: {person.price} Miqdori: {person.quantity}")


#--------------------------------------------------------------------------------------------------

# 3 vazifa

# from collections import namedtuple
#
# Shaharlar = []
# Person = namedtuple("Person", ["id", "city_name", "country", "population"])
# count = 0
# for i in range(1,4):
#     count += 1
#     city_name = input(f"{count}. Shaxarizni nomini kiriting: ")
#     country = input(f"{count}.Davlatizdi nomi kiriting: ")
#     population = input(f"{count}. Aholi soni kiriting: ")
#     Shaharlar.append({"id": count, "city_name": city_name, "country": country, "population": population })
#
# max_population_city = Shaharlar[0]
#
# for shahar in Shaharlar:
#     if shahar['population'] > max_population_city['population']:
#         max_population_city = shahar
#
# largest_city = Person(**max_population_city)
# print(f"Eng katta aholi punktiga ega shahar:")
# print(f"Shahar: {largest_city.city_name}, Davlat: {largest_city.country}, Aholi: {largest_city.population}")



#--------------------------------------------------------------------------------------------------

# 4 vazifa

# from collections import namedtuple
#
# Avtomobillar = []
# Person = namedtuple("Person", ["id", "make", "model", "year"])
# count = 0
# for i in range(1,4):
#     count += 1
#     make = input(f"{count}. Make: ")
#     model = input(f"{count}. Model: ")
#     year = input(f"{count}. Year: ")
#     Avtomobillar.append({"id": count, "make": make, "model": model, "year": year })
#
# max_year = Avtomobillar[0]
#
# for moshina in Avtomobillar:
#     if moshina['year'] > max_year['year']:
#         max_year = moshina
#
# person = Person(**max_year)
# print(f"Eng yangi aftomabil")
# print(f"make: {person.make}, Davlat: {person.model}, Aholi: {person.year}")



#--------------------------------------------------------------------------------------------------

# 5 vazifa

# def ab(a):
#     def bc(b):
#         print(a + b)
#     return bc
# c = ab(7)
# c(2)


#--------------------------------------------------------------------------------------------------

# 6 vazifa

# def ab(ism):
#     def bc():
#         return f"Salom, {ism}!"
#     return bc
# ism = input("Ismdi kiriting: ")
# a = ab(ism)
# print(a())


#--------------------------------------------------------------------------------------------------

# 7 vazifa

# def ab(a):
#     def bc(b):
#         print(f"Javobi: {a + b}")
#     return bc
# a = int(input("Birinchi soni kiriting: "))
# b = int(input("Ikkinchi soni kiriting: "))
# c = ab(a)
# c(b)


#--------------------------------------------------------------------------------------------------

# 8 vazifa

# def ab():
#     count = 0
#     def bc():
#         nonlocal count
#         count += 1
#         print(f"Funksiya {count} martta ishlatildi")
#     return bc
# a = ab()
#
# a()
# a()
# a()


#--------------------------------------------------------------------------------------------------

# 9 vazifa

# import math
# def ab(son):
#     def bc():
#         print(f"Sonning kvadrati: {math.pow(son, 2)}")
#     return bc
# son = int(input("Soni kiriting: "))
# a = ab(son)
# a()


#--------------------------------------------------------------------------------------------------

# 10 vazifa
#
# royxat = []
#
# def ab(ism):
#     global royxat
#     royxat.append(ism)
#     def bc():
#         global royxat
#         print(royxat)
#     return bc
# while True:
#     ism = input("Ismdi kiriting: ")
#     if ism == "stop":
#         break
#     else:
#         a = ab(ism)
#         a()



#--------------------------------------------------------------------------------------------------

# 11 vazifa

# def ab(narx):
#     def bc(foiz):
#         print(f"Maxsulotning narxi: {narx}\n"
#               f"Chegirma narxi: {narx * foiz / 100}\n"
#               f"Chegirmadan keyingi narxi: {narx - narx * foiz / 100}")
#     return bc
# narx = int(input("Mahsulot narxni kiriting: "))
# foiz = int(input("Chegirma foizni kiriting: "))
# a = ab(narx)
# a(foiz)


#--------------------------------------------------------------------------------------------------

# 12 vazifa

# def ab(b):
#     count = 1
#     def bc():
#         """
#             This function helps to increment the product by the same amount each time it is called.
#             For example, if we enter the number of products as 2,
#             it will be 4 the first time it runs, and 6 the second time it runs.
#         """
#         nonlocal count
#         count += 1
#         print(f"Mahsulot soni: {b * count}")
#     return bc
# b = int(input("Mahsulot soni: "))
# a = ab(b)
# a()
# a()


#--------------------------------------------------------------------------------------------------

# 13 vazifa

# def ab(a):
#     def bc(b):
#         return a + b
#     return bc
#
# add_to_string = ab("Boshlang'ich qator. ")
#
# print(add_to_string("Asilbek. "))
# print(add_to_string("Rustamov. "))


#--------------------------------------------------------------------------------------------------

# 14 vazifa

# def ab(son):
#     def bc():
#         if son % 2 == 0:
#             print("Kiritilgan son juft !")
#         else:
#             print("Kiritilgan son toq !")
#     return bc
# a = int(input("Son kiriting: "))
# c = ab(a)
# c()


#--------------------------------------------------------------------------------------------------

# 15 vazifa

# import math
# from idlelib.editor import darwin
#
#
# def ab(son):
#     def bc(daraja):
#         print(f"Javob: {math.pow(son, daraja)}")
#     return bc
# son = int(input("Sonni kiriting: "))
# daraja = int(input("Darajani kiriting: "))
# a = ab(son)
# a(daraja)


#--------------------------------------------------------------------------------------------------

# 16 vazifa

# def ab(text):
#     def bc():
#         nonlocal text
#         print(text[::-1])
#     return bc
# text = input("String kiriting: ")
# a = ab(text)
# a()


#--------------------------------------------------------------------------------------------------

# 17 vazifa

# maxsulotlar = []
# narxlar = 0
# def ab(name):
#     def bc(narx):
#         global maxsulotlar
#         global narxlar
#         maxsulotlar.append(name)
#         narxlar += narx
#         print(f"Maxsulotlar ro'yxati: {maxsulotlar}, Va umumiy summa: {narxlar}")
#     return bc
# while True:
#     name = input("Maxsulot nomini kiriting: ")
#     narx = int(input("Maxsulot narxini kiriting: "))
#     if name == "stop":
#         break
#     else:
#         a = ab(name)
#         a(narx)


#--------------------------------------------------------------------------------------------------

# 18 vazifa

# narxlar = []
# def ab(narx):
#     def korish():
#         global narxlar
#         narxlar.append(int(narx))
#     return korish
#
#
# while True:
#     a = input(f"1 -> qoshish\n"
#               f"2 -> korish\n"
#               f"3 -> stop\n"
#               f"4 -> umumiy summa\n"
#               f"Buyruq kiriting: ")
#     if a == "3" :
#         print("Bizda bilan bolganingizdan hursandmiz !!!")
#         break
#     if a == "2" :
#         print(narxlar)
#     if a == "1" :
#         while True:
#             narx = input("Narxdi kiriting(stop -> toxtash): ")
#             if narx == "stop":
#                 break
#             elif narx.isdigit():
#                 a = ab(narx)
#                 a()
#     if a == "4" :
#         print(f"Kiritgan sonlar yeg'indisi: {sum(narxlar)}")

#====================================================================================================