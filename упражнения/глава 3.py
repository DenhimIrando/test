#1
# number = int(input("Введите число от 1 до 7: "))
# if number == 1:
#     print("Понедельник")
# elif number == 2:
#     print("Вторник")
# elif number == 3:
#     print("Среда")
# elif number == 4:
#     print("Четверг")
# elif number == 5:
#     print("Пятница")
# elif number == 6:
#     print("Суббота")
# elif number == 7:
#     print("Воскресенье")
# else:
#     print("Ошибка: введенное число находится вне диапазона от 1 до 7.")

#2
# length1 = float(input("Введите длину первого прямоугольника: "))
# width1 = float(input("Введите ширину первого прямоугольника: "))
# length2 = float(input("Введите длину второго прямоугольника: "))
# width2 = float(input("Введите ширину второго прямоугольника: "))
# area1 = length1 * width1
# area2 = length2 * width2
# if area1 > area2:
#     print("Площадь первого прямоугольника больше.")
# elif area2 > area1:
#     print("Площадь второго прямоугольника больше.")
# else:
#     print("Площади прямоугольников одинаковы.")

#3
# age = float(input("Введите возраст человека: "))
# if age <= 1:
#     print("Этот человек — младенец.")
# elif age < 13:
#     print("Этот человек — ребенок.")
# elif age < 20:  #в условии несказано про ровно 20, так что чуть отклонился от него
#     print("Этот человек — подросток.")
# else:
#     print("Этот человек — взрослый.")

#4
# number = int(input("Введите число от 1 до 10: "))
# if number == 1:
#     print("Римская цифра: I")
# elif number == 2:
#     print("Римская цифра: II")
# elif number == 3:
#     print("Римская цифра: III")
# elif number == 4:
#     print("Римская цифра: IV")
# elif number == 5:
#     print("Римская цифра: V")
# elif number == 6:
#     print("Римская цифра: VI")
# elif number == 7:
#     print("Римская цифра: VII")
# elif number == 8:
#     print("Римская цифра: VIII")
# elif number == 9:
#     print("Римская цифра: IX")
# elif number == 10:
#     print("Римская цифра: X")
# else:
#     print("Ошибка: введенное число находится вне диапазона от 1 до 10.")

#5
# mass = float(input())
# weight = mass * 9.8
# print(f"Вес: {weight:.2f} Н")
# if weight > 500:
#     print("Тело слишком тяжелое.")
# elif weight < 100:
#     print("Тело слишком легкое.")

#6
# month = int(input("Введите месяц: "))
# day = int(input("Введите день: "))
# year = int(input("Введите год: "))
# if day * month == year:
#     print("Введенная дата является магической.")
# else:
#     print("Дата не является магической.")

#7
# color1 = input("Введите первый основной цвет: ")
# color2 = input("Введите второй основной цвет: ")
# if color1 != "красный" and color1 != "синий" and color1 != "желтый":
#     print("Ошибка: введены некорректные названия цветов.")
# elif color2 != "красный" and color2 != "синий" and color2 != "желтый":
#     print("Ошибка: введены некорректные названия цветов.")
# elif color1 == color2:
#     print("При смешивании одинаковых цветов получится тот же цвет.")
# elif (color1 == "красный" and color2 == "синий") or (color1 == "синий" and color2 == "красный"):
#     print("Получится фиолетовый.")
# elif (color1 == "красный" and color2 == "желтый") or (color1 == "желтый" and color2 == "красный"):
#     print("Получится оранжевый.")
# elif (color1 == "синий" and color2 == "желтый") or (color1 == "желтый" and color2 == "синий"):
#     print("Получится зеленый.")

#8
# people = int(input("Введите количество участников: "))
# hotdogs_per_person = int(input("Введите количество хот-догов на человека: "))
# total_needed = people * hotdogs_per_person
# sausage_packages = total_needed // 10
# if total_needed % 10 != 0:
#     sausage_packages = sausage_packages + 1
# sausage_leftovers = (sausage_packages * 10) - total_needed
# bun_packages = total_needed // 8
# if total_needed % 8 != 0:
#     bun_packages = bun_packages + 1
# bun_leftovers = (bun_packages * 8) - total_needed
# print("Минимальное количество упаковок с сосисками:", sausage_packages)
# print("Минимальное количество упаковок с булочками:", bun_packages)
# print("Количество оставшихся сосисок:", sausage_leftovers)
# print("Количество оставшихся булочек:", bun_leftovers)

#9
# number = int(input("Введите номер кармана от 0 до 36: "))
# if number<0 or number>36:
#     print("Ошибка: введенное число находится вне диапазона от 0 до 36.")
# elif number==0:
#     print("Зеленый")
# elif 1<=number<=10:
#     if number%2!= 0:
#         print("Красный")
#     else:
#         print("Черный")
# elif 11<=number<=18:
#     if number%2!=0:
#         print("Черный")
#     else:
#         print("Красный")
# elif 19<=number<=28:
#     if number%2!=0:
#         print("Красный")
#     else:
#         print("Черный")
# elif 29<=number<=36:
#     if number%2!=0:
#         print("Черный")
#     else:
#         print("Красный")

#10
# coins_5 = int(input("Введите количество монет достоинством 5 копеек: "))
# coins_10 = int(input("Введите количество монет достоинством 10 копеек: "))
# coins_50 = int(input("Введите количество монет достоинством 50 копеек: "))
# total_kopeek = (coins_5 * 5) + (coins_10 * 10) + (coins_50 * 50)
# if total_kopeek == 100:
#     print("Поздравляем! Вы выиграли! Получился ровно один рубль.")
# elif total_kopeek > 100:
#     print("Введенная сумма больше одного рубля.")
# else:
#     print("Введенная сумма меньше одного рубля.")

#11
# books = int(input("Введите количество книг, приобретенных в этом месяце: "))
# if books < 0:
#     print("Ошибка: количество книг не может быть отрицательным.")
# elif books < 2:
#     print("Присуждено очков: 0")
# elif books < 4:
#     print("Присуждено очков: 5")
# elif books < 6:
#     print("Присуждено очков: 15")
# elif books < 8:
#     print("Присуждено очков: 30")
# else:
#     print("Присуждено очков: 60")

#12
# quantity = int(input("Введите количество приобретенных пакетов: "))
# price_per_packet = 99
# total_before_discount = quantity * price_per_packet
# if quantity < 0:
#     print("Ошибка: количество не может быть отрицательным.")
# else:
#     if quantity >= 100:
#         discount_percent = 40
#     elif quantity >= 50:
#         discount_percent = 30
#     elif quantity >= 20:
#         discount_percent = 20
#     elif quantity >= 10:
#         discount_percent = 10
#     else:
#         discount_percent = 0
#     discount_amount = total_before_discount * (discount_percent / 100)
#     total_after_discount = total_before_discount - discount_amount
#     print(f"Сумма скидки: {discount_amount:.2f} долларов")
#     print(f"Общая сумма покупки: {total_after_discount:.2f} долларов")

#13
# weight = float(input("Введите массу пакета в граммах: "))
# if weight <= 0:
#     print("Ошибка: масса должна быть больше нуля.")
# else:
#     if weight <= 200:
#         rate = 150
#     elif weight <= 600:
#         rate = 300
#     elif weight <= 1000:
#         rate = 400
#     else:
#         rate = 475
#     cost = (weight / 100) * rate
#     print(f"Плата за доставку: {cost:.2f} рублей")

#14
# weight = float(input("Введите массу тела в килограммах: "))
# height = float(input("Введите рост в метрах: "))
# bmi = weight / (height ** 2)
# print(f"Индекс массы тела (ИМТ): {bmi:.2f}")
# if bmi < 18.5:
#     print("Человек весит ниже нормы (недостаточная масса).")
# elif bmi <= 25:
#     print("Человек имеет оптимальную массу тела.")
# else:
#     print("Человек весит больше нормы (избыточная масса).")

#15
# total_seconds = int(input("Введите количество секунд: "))
# if total_seconds < 0:
#     print("Ошибка: количество секунд должно быть неотрицательным.")
# else:
#     days = total_seconds // 86400
#     remainder = total_seconds % 86400
#     hours = remainder // 3600
#     remainder = remainder % 3600
#     minutes = remainder // 60
#     seconds = remainder % 60
#     if total_seconds >= 86400:
#         print(f"Результат: {days} дн., {hours} ч., {minutes} мин., {seconds} сек.")
#     elif total_seconds >= 3600:
#         print(f"Результат: {hours} ч., {minutes} мин., {seconds} сек.")
#     elif total_seconds >= 60:
#         print(f"Результат: {minutes} мин., {seconds} сек.")
#     else:
#         print(f"Результат: {seconds} сек.")

#16
# year = int(input("Введите год: "))
# if year % 100 == 0:
#     if year % 400 == 0:
#         days = 29
#     else:
#         days = 28
# else:
#     if year % 4 == 0:
#         days = 29
#     else:
#         days = 28
# print(f"В {year} году в феврале {days} дней.")

#17
# print("Перезагрузите компьютер и попробуйте подключиться.")
# answer = input("Вы исправили проблему? ")
# if answer == "нет":
#     print("Перезагрузите маршрутизатор и попробуйте подключиться.")
#     answer = input("Вы исправили проблему? ")    
#     if answer == "нет":
#         print("Убедитесь, что кабели между маршрутизатором и модемом прочно подсоединены.")
#         answer = input("Вы исправили проблему? ")
#         if answer == "нет":
#             print("Переместите маршрутизатор на новое место.")
#             answer = input("Вы исправили проблему? ")
#             if answer == "нет":
#                 print("Возьмите новый маршрутизатор.")

#18
# is_veg = input("Будет ли на ужине вегетарианец? ")
# is_vegan = input("Будет ли на ужине веганец? ")
# is_gf = input("Будет ли на ужине приверженец безглютеновой диеты? ")
# print("Вот ваши варианты ресторанов:")
# if is_veg == "нет" and is_vegan == "нет" and is_gf == "нет":
#     print("Изысканные гамбургеры от Джо")
# if is_vegan == "нет":
#     print("Центральная пиццерия")
# print("Кафе за углом")
# if is_vegan == "нет" and is_gf == "нет":
#     print("Блюда от итальянской мамы")
# print("Кухня шеф-повара")

#19
# import turtle

# SCREEN_WIDTH = 600
# SCREEN_HEIGHT = 600
# TARGET_LLEFT_X = 100
# TARGET_LLEFT_Y = 250
# TARGET_WIDTH = 25
# FORCE_FACTOR = 30
# PROJECTILE_SPEED = 1
# NORTH = 90
# SOUTH = 270
# EAST = 0
# WEST = 180

# turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# turtle.hideturtle()
# turtle.speed(0)
# turtle.penup()
# turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
# turtle.pendown()
# turtle.setheading(EAST)
# turtle.forward(TARGET_WIDTH)
# turtle.setheading(NORTH)
# turtle.forward(TARGET_WIDTH)
# turtle.setheading(WEST)
# turtle.forward(TARGET_WIDTH)
# turtle.setheading(SOUTH)
# turtle.forward(TARGET_WIDTH)
# turtle.penup()

# turtle.goto(0, 0)
# turtle.setheading(EAST)
# turtle.showturtle()
# turtle.speed(PROJECTILE_SPEED)

# angle = float(input("Введите угол выстрела снаряда: "))
# force = float(input("Введите пусковую силу (1-10): "))

# distance = force * FORCE_FACTOR

# turtle.setheading(angle)

# turtle.pendown()
# turtle.forward(distance)

# if (turtle.xcor() >= TARGET_LLEFT_X and
#     turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
#     turtle.ycor() >= TARGET_LLEFT_Y and
#     turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
#     print("Цель поражена!")
# else:
#     print("Вы промахнулись.")
    
#     if turtle.ycor() < TARGET_LLEFT_Y:
#         print("Попробуйте угол побольше.")
#     elif turtle.ycor() > (TARGET_LLEFT_Y + TARGET_WIDTH):
#         print("Попробуйте угол поменьше.")
        
#     if turtle.xcor() < TARGET_LLEFT_X:
#         print("Примените силу побольше.")
#     elif turtle.xcor() > (TARGET_LLEFT_X + TARGET_WIDTH):
#         print("Примените силу поменьше.")
