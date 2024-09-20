city_temperatures = {
    "Київ": 25,
    "Львів": 22,
    "Одеса": 28,
    "Харків": 24,
    "Дніпро": 27
}


cities_input = input("Введіть назви міст, розділені комами: ").strip()


cities_list = [city.strip() for city in cities_input.split(",")]


total_temperature = 0
count = 0

for city in cities_list:
    if city in city_temperatures:
        total_temperature += city_temperatures[city]
        count += 1
    else:
        print(f"Місто {city} не знайдено у словнику")

if count > 0:
    average_temperature = total_temperature / count
    print(f"Середня температура для вказаних міст: {average_temperature:.2f}°C")
else:
    print("Жодне з вказаних міст не знайдено у словнику")


