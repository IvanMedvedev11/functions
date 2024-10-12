def dollars_to_rubles(dollars):
    return round(dollars * 100, 2)
def bats_to_rubles(bats):
    return round(bats * 3, 2)
def wons_to_rubles(wons):
    return round(wons * 0.07, 2)
try:
    currency_count = float(input("Введите кол-во единиц валюты: "))
except ValueError:
    print("Ты И Д И О Т")
    quit()
currency =  input("Выберите валюту: доллар, тайский бат и корейская вона: ")
if currency == "доллар":
    print(dollars_to_rubles(currency_count))
elif currency == "тайский бат":
    print(bats_to_rubles(currency_count))
elif currency == "корейская вона":
    print(wons_to_rubles(currency_count))
