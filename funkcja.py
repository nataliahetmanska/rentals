'''
Ustal datę początkową.
Utwórz listę zbiorów na każy dzień okresu generowania.
Weź Customerów - (razem z create date) razem z ilością wypożyczeń każdego
Weź inventory
Znajdź wypożyczone właśnie auta
Odejmij zbiory
Wylosuj N <= liczności zbioru, z uwzględnieniem wytycznych
Dla N aut ze zbioru dostępnych wylosuj długości wypożyczenia (oblicz daty zwrotu)
Dla każdego auta do wypożyczenia przypisz losowego customera, faworyzuj tych, którzy mają mniej wypożyczeń
    Każdemu customerowi, który dostanie wypożyczenie, zwiększ ilość wypożyczeń.
Wygeneruj inserty
Dodaj auta wg dat zwrotu do odpowiednich slotów w liście dostępnych aut
Dodaj pozostałe auta do następnego slotu w liście dostępnych aut
Powtórz dla następnego dnia
'''

from datetime import date, timedelta, datetime
import random as rnd
import mysql.connector
from calendar import monthrange
from operator import itemgetter
import keyring


def insert_data(index, cursor, rental_list):
    cursor.execute("SELECT rental.customer_id, COUNT(rental.customer_id), customer.create_date\
                    FROM customer JOIN rental USING(customer_id)\
                    GROUP BY customer_id")

    customers = cursor.fetchall()

    customers = sorted(customers, key=itemgetter(1))

    amt = list()
    customer_id = list()
    create_date = list()

    for i in customers:
        customer_id.append(i[0])
        create_date.append(i[2])
        amt.append(i[1])

    insert_list = []
    for day in rental_list:

        '''
        possible_indx = list()
        for i in range(len(create_date)):
            if create_date[i].date() >= datetime.strptime(day[0]["rental_date"], '%Y-%m-%d').date():
                possible_indx.append(i)

        available_customers = list()
        amounts = list()
        print(possible_indx)
        for index in possible_indx:
            available_customers.append(customer_id[index])
            amounts.append(amt[index])

        weights = amounts.reverse()
        '''

        for rent in day:
            insert_list.append((index,
                                rent["car_id"],
                                rnd.randint(1, 15),
                                # rnd.choices(available_customers, weights= weights, k=1),
                                rent["rental_date"],
                                rent["return_date"],
                                str(datetime.strptime(rent["rental_date"], '%Y-%m-%d') + timedelta(days=7)),
                                rent["rental_date"]))

            # print(insert_list)
            index += 1

    # Q = """INSERT INTO rental (rental_id, rental_rate, customer_id, inventory_id, staff_id, rental_date, return_date,
    #                            payment_deadline, create_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    # cursor.executemany(Q, insert_list)
    # connection.commit()

    return "Data inserted into databse"


def generate_rentals(available, day0, daily_amt, daily_rent, month):
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

        try:
            rentals = set(rnd.sample(tuple(available), k=min(daily_amt * daily_rent[day], len(available))))
        except IndexError:
            continue  # Ignore additions past the end of the list

        return_offsets = return_offset(rentals)
        # print(return_offsets)
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


def return_offset(rentals):
    duration = [rnd.randint(1, 15) for _ in range(1, 16)]
    weights = duration.reverse()
    return_offset = [rnd.choices(duration, weights=weights, k=1) for _ in rentals]
    return_offset = sum(return_offset, [])

    return return_offset


def daily_rentals(last_date):
    next_month = last_date.month + 1
    year = last_date.year
    num_days = monthrange(year, next_month)[1]

    days = [date(year, next_month, day) for day in range(1, num_days + 1)]

    if next_month in [7, 8]:
        N = 1.2
    else:
        N = 1

    n_daily = list()

    for i in days:
        if weekend_check(i):
            n_daily.append(1.5)
        else:
            n_daily.append(1)

    multi = [element * N for element in n_daily]

    return multi, num_days


def weekend_check(date):
    if date.weekday() > 4:
        return True
    else:
        return False


def connection(host, user, password, database, port):
    mydb = mysql.connector.connect(host=host, user=user, password=password, database=database, port=port)
    cursor = mydb.cursor()

    return mydb, cursor


# zmienić dla swojej bazy

def latest_date_fun(cursor):
    cursor.execute("select rental_date from rental order by rental_date DESC limit 1")

    latest_date = cursor.fetchall()
    latest_date = latest_date[0][0]

    return latest_date


def latest_index(cursor):
    cursor.execute("SELECT rental_id FROM rental ORDER BY rental_id DESC limit 1")

    latest_index = cursor.fetchall()
    latest_index = latest_index[0][0]

    return latest_index


def car_id(latest_date, cursor):
    cursor.execute("SELECT r.inventory_id, r.rental_date, r.return_date\
                    from rental r inner join (\
                    select inventory_id, max(rental_date) as MaxRental\
                    from rental\
                    group by inventory_id) as r2\
                    on r.inventory_id = r2.inventory_id and r.rental_date = r2.MaxRental\
                    where r.inventory_id>570;")

    rental = cursor.fetchall()
    free_cars = list()
    rented_cars = list()
    for i in rental:
        if i[2] <= latest_date:
            free_cars.append(i[0])

        else:
            rented_cars.append(i[0])
    return set(free_cars), set(rented_cars)


user = keyring.get_password("username", "username")
password = keyring.get_password("database_pass", user)
port = keyring.get_password("database_port", user)
database = keyring.get_password("database", user)
host = keyring.get_password("database_host", user)
db, cursor = connection(host=host, user=user, password=password, database=database, port=port)


latest_date_from_db = latest_date_fun(cursor)
available, rented = car_id(latest_date_from_db, cursor)
inv = available.update(rented)

last_index_from_db = latest_index(cursor) + 1
daily_rent, month = daily_rentals(latest_date_from_db)
rental_list = generate_rentals(available, latest_date_from_db, 300, daily_rent, month)
insert = insert_data(last_index_from_db, cursor, rental_list)
