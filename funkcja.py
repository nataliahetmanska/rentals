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
from calendar import monthrange


def insert_data(index):
    rental_list = generate_rentals(available, latest_date)
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


def generate_rentals(available, day0):
    '''
    generate a list of rentals for each day; daily rentals is a list of dictionaries
    containing car id and return day
    :param available:
    :param daily_rentals:
    :return:
    '''
    rental_list = list()
    availability_calendar = [set() for _ in range(31)]

    daily_rent, month = daily_rentals(day0)

    for day, available_cars in enumerate(availability_calendar):

        rental_perday = list()
        available.update(available_cars)

        rentals = set(rnd.sample(tuple(available), k=min(daily_rent[day], len(available))))

        return_offsets = [return_offset() for _ in rentals]
        rent_date = day0 + timedelta(days=day)

        return_dates = []
        for i in range(len(rentals)):
            return_date = rent_date + timedelta(days=return_offsets[i])
            return_dates.append(return_date)

        print(f' Cars available {len(available)}, rental ids {rentals}')

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

def return_offset():

    duration = list()
    for i in range(1, 16):
        n = rnd.randint(1, 15)
        duration.append(n)

    weights = list()
    for i in duration:
        if i > 10:
            weights.append(1)
        elif 5 < i < 10:
            weights.append(2)
        else:
            weights.append(5)

    return_offset = rnd.choices(duration, weights=weights, k=1)
    return return_offset[0]


def daily_rentals (last_date):

    next_month = last_date.month + 1
    year = last_date.year
    num_days = monthrange(year, next_month)[1]

    days = [date(2022, 9, day) for day in range(1, num_days+ 1)]

    year_rental = 300000
    avg_month = int(year_rental/12)

    if next_month in [7, 8]:
        N = int(avg_month * 1.2)

    else:
        N = int(avg_month)

    avg_daily = int(N / num_days)

    n_daily = list()
    print(len(days))

    for i in days:
        if weekend_check(i):
            n_daily.append(int(avg_daily * 1.5))

        else:
            n_daily.append(avg_daily)

    return n_daily, num_days

def weekend_check(date):
    if date.weekday() > 4:
        return True
    else:
        return False

def connection(host, user, password, database, port):
    mydb = mysql.connector.connect(host=host, user=user, password=password, database=database, port=port)
    cursor = mydb.cursor()

    return mydb, cursor

#zmienić dla swojej bazy
db, cursor = connection(host="80.211.255.121", user="natalia", password="FiniVik6", database="wheelie", port="3396")


cursor.execute("select rental_date from rental order by rental_date DESC limit 1")

latest_date = cursor.fetchall()
latest_date = latest_date[0][0]

cursor.execute("SELECT r.inventory_id, r.rental_date, r.return_date\
                from rental r inner join (\
                select inventory_id, max(rental_date) as MaxRental\
                from rental\
                group by inventory_id) as r2\
                on r.inventory_id = r2.inventory_id and r.rental_date = r2.MaxRental\
                where r.inventory_id>570;")

rental = cursor.fetchall()

def car_id (rental, latest_date):
    free_cars = list()
    rented_cars = list()
    for i in rental:
        if i[2] <= latest_date:
            free_cars.append(i[0])

        else:
            rented_cars.append(i[0])
    return set(free_cars), set(rented_cars)

available, rented = car_id(rental, latest_date)
inv = available.update(rented)

index0 = 1
insert = insert_data(index0)


# TODO: uwzględnić customerów
