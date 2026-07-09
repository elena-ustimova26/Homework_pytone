year = int(input("Введите год: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    is_year_leap = True
else:
    is_year_leap = False

print(is_year_leap)