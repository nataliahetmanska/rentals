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

from datetime import date, timedelta, datetime
import random as rnd
import mysql.connector

day0 = date.fromisoformat("2022-08-30")
ord_day0 = day0.toordinal()

inv = set(range(30))
rented = set(rnd.sample(range(30), k=20))
daily_rentals = 5
available = inv - rented

index0 = 1


def insert_data(index):
    rental_list = generate_rentals(available, daily_rentals)
    # dodac customer_id
    insert_list = []
    for day in rental_list:
        for rent in day:
            insert_list.append((index,
                                rent["car_id"],
                                rnd.randint(1, 15),
                                rent["rental_date"],
                                rent["return_date"],
                                str(datetime.strptime(rent["rental_date"], '%Y-%m-%d') + timedelta(days=7)),
                                rent["rental_date"]))
            index += 1

    # Q = """INSERT INTO rental (rental_id, rental_rate, customer_id, inventory_id, staff_id, rental_date, return_date,
    #                            payment_deadline, create_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    # cursor.executemany(Q, insert_list)
    # connection.commit()

    return "Data inserted into databse"


def generate_rentals(available, daily_rentals):
    '''
    generate a list of rentals for each day; daily rentals is a list of dictionaries
    containing car id and return day
    :param available:
    :param daily_rentals:
    :return:
    '''
    day0 = date(2022, 8, 31)
    rental_list = list()
    availability_calendar = [set() for _ in range(31)]
    for day, available_cars in enumerate(availability_calendar):

        rental_perday = list()
        available.update(available_cars)
        rentals = set(rnd.sample(tuple(available), k=min(daily_rentals, len(available))))
        return_offsets = [rnd.randint(1, 10) for _ in rentals]
        rent_date = day0 + timedelta(days=day)

        return_dates = []
        for i in range(len(rentals)):
            return_date = rent_date + timedelta(days=return_offsets[i])
            return_dates.append(return_date)

        # print(f' Cars available {len(available)}, rental ids {rentals}')

        for rental, offset, return_d in zip(rentals, return_offsets, return_dates):

            rental_perday.append(
                {"rental_date": str(rent_date), "car_id": rental, "offset": offset, "return_date": str(return_d)})
            try:
                availability_calendar[day + offset].add(rental)
            except IndexError:
                continue  # Ignore additions past the end of the list
        rental_list.append(rental_perday)
        available = available - rentals

    return rental_list


insert = insert_data(index0)



# TODO: zmodyfikować gnerate_rentals tak żeby uwzględniała rozkłady przy losowaniu
