'''
ustal datę początkową
utwórz listę zbiorów na każy dzień okresu generowania
Weź Customerów - (razem z create date) razem z ilością wypożyczeń każdego
Weź inventory
Znajdź wypożyczone właśnie auta
Odejmij zbiory
Wylosuj N <= liczności zbioru, z uwzgl. wytycznych
Dla N aut ze zbioru dostepnych wylosuj długości wypożyczenia (oblicz daty zwortu)
Dla każdego auta do wypozyczenia przypisz losowego customera, faworyzuj tych, którzy mają mniej wypożyczeń
    Każdemu customerowi, który dostanie wypożyczenie zwiększ ilość wypożyczeń.
Wygeneruj inserty
Dodaj auta wg dat zwrotu do odpowiednich slotów w liście dostępnych aut
Dodaj pozostałe auta do następnego slotu w liście dostępnych aut
Powtórz dla nastepnego dnia
'''

from datetime import date
import random as rnd

day0 = date.fromisoformat("2022-08-30")
ord_day0 = day0.toordinal()

inv = set(range(30))
rented = set(rnd.sample(range(30), k=20))
daily_rentals = 5
available = inv - rented


def generate_rentals (available, daily_rentals):
    '''
    generate a list of rentals for each day; daily rentals is a list of dictionaries
    containing car id and return day
    :param available:
    :param daily_rentals:
    :return:
    '''

    rental_list = list()
    availability_calendar = [set() for _ in range(31)]
    for day, available_cars in enumerate(availability_calendar):

        rental_perday = list()
        available.update(available_cars)
        rentals = set(rnd.sample(tuple(available), k=min(daily_rentals, len(available))))
        return_offsets = [rnd.randint(1, 10) for _ in rentals]
        print(f' Cars available {len(available)}, rental ids {rentals}')

        for rental, offset in zip(rentals, return_offsets):

            rental_perday.append({"car_id": rental, "offset": offset})
            try:
                availability_calendar[day + offset].add(rental)
            except IndexError:
                continue  # Ignore additions past the end of the list

        rental_list.append(rental_perday)
        available = available - rentals

    return rental_list

#TODO: napisać funkcję, która przelicza offsety na konkretne daty
#TODO: funkcja, która generuje inserty do bazy
#TODO: zmodyfikować gnerate_rentals tak żeby uwzględniała rozkłady przy losowaniu