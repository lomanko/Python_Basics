# Задача 1

region = input('Введите регион проживания: ').lower()
far_east = ['амурская область','республика бурятия', 'еврейская автономная область', 'забайкальский край','камчатский край', 'магаданская область', 'приморский край','республика саха', 'сахалинская область', 'хабаровский край', 'чукотский автономный округ']
rate = 14
if region in far_east:
  print('Ваша базовая ставка - 2%')
else:
  children = int(input('Введите количество детей: '))
  if children > 3: rate -= 1
  salary_project = input('Есть ли у Вас зарплатный проект в банке (да/нет)? ').lower()
  if salary_project == 'да': rate -= 0.5
  insurance = input('Будет ли у Вас оформлено страхование в банке (да/нет)? ').lower()
  if insurance == 'да': rate -= 1.5
  print(f'Ваша базовая ставка - {rate}%')  


# Задача 2

month = input('Введите месяц рождения ').lower()
day = int(input('Введите день рождения '))

if (day >= 21 and month == 'март') or (day <= 20 and month == 'апрель'):
  print('Ваш знак зодиака Овен')
elif (day >= 21 and month == 'апрель') or (day <= 21 and month == 'май'):
  print('Ваш знак зодиака Телец')
elif (day >= 22 and month == 'май') or (day <= 21 and month == 'июнь'):
  print('Ваш знак зодиака Близнецы')
elif (day >= 21 and month == 'июнь') or (day <= 22 and month == 'июль'):
  print('Ваш знак зодиака Рак')
elif (day >= 23 and month == 'июль') or (day <= 23 and month == 'август'):
  print('Ваш знак зодиака Лев')
elif (day >= 24 and month == 'август') or (day <= 23 and month == 'сентябрь'):
  print('Ваш знак зодиака Дева')
elif (day >= 24 and month == 'сентябрь') or (day <= 23 and month == 'октябрь'):
  print('Ваш знак зодиака Весы')
elif (day >= 24 and month == 'октябрь') or (day <= 22 and month == 'ноябрь'):
  print('Ваш знак зодиака Скорпион')
elif (day >= 23 and month == 'ноябрь') or (day <= 21 and month == 'декабрь'):
  print('Ваш знак зодиака Стрелец')
elif (day >= 22 and month == 'декабрь') or (day <= 20 and month == 'январь'):
  print('Ваш знак зодиака Козерог')
elif (day >= 21 and month == 'январь') or (day <= 18 and month == 'февраль'):
  print('Ваш знак зодиака Водолей')
else:
  print('Ваш знак зодиака Рыбы')

  