sec = 2897820331730867
sec_value = sec % (24*3600)
hour_value = sec_value // 3600
sec_value %= 3600
min_value = sec_value // 60
sec_value %= 60
print("Часы:",hour_value,"Минуты:",min_value,"Секунды:",sec_value)


