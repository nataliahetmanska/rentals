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
import interaction_with_database as interaction


def insert_data(insert_list):
    db, cursor = interaction.connection()
    Q = """INSERT INTO rental (rental_id, rental_rate, customer_id, inventory_id, staff_id, rental_date, return_date, 
    payment_deadline, create_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    # cursor.executemany(Q, insert_list)


def get_rental_rate():
    Q = "SELECT i.inventory_id, c.rental_rate FROM inventory i, car c WHERE i.car_id = c.car_id"
    result = interaction.select_data(Q)
    rental_rates = dict((x, int(y)) for x, y in result)
    return rental_rates


def get_customers():
    Q = "SELECT rental.customer_id, COUNT(rental.customer_id), customer.create_date FROM customer " \
        "JOIN rental USING(customer_id) GROUP BY customer_id"
    customers = interaction.select_data(Q)
    customers = sorted(customers, key=itemgetter(1))
    return customers


def get_new_customers(latest_date_from_db):
    Q = f'SELECT customer_id, create_date FROM customer WHERE create_date > {latest_date_from_db}'
    new_customers = interaction.select_data(Q)
    return new_customers


def get_latest_date():
    Q = "SELECT rental_date FROM rental ORDER BY rental_date DESC LIMIT 1"
    latest_date = interaction.select_data(Q)[0][0]
    return latest_date



def get_latest_index():
    Q = "SELECT rental_id FROM rental ORDER BY rental_id DESC LIMIT 1"
    latest_index = interaction.select_data(Q)[0][0]
    return latest_index


def get_free_cars(latest_date):
    Q = "SELECT r.inventory_id, r.rental_date, r.return_date FROM rental r INNER JOIN (SELECT inventory_id, " \
        "max(rental_date) as MaxRental FROM rental GROUP BY inventory_id) as r2 ON r.inventory_id = r2.inventory_id " \
        "AND r.rental_date = r2.MaxRental WHERE r.inventory_id>570;"
    rental = interaction.select_data(Q)
    free_cars = list()
    for i in rental:
        if i[2] <= latest_date:
            free_cars.append(i[0])
    return set(free_cars)


def get_rented_cars(latest_date):
    Q = "SELECT r.inventory_id, r.rental_date, r.return_date FROM rental r INNER JOIN (SELECT inventory_id, " \
        "max(rental_date) as MaxRental FROM rental GROUP BY inventory_id) as r2 on r.inventory_id = r2.inventory_id " \
        "AND r.rental_date = r2.MaxRental WHERE r.inventory_id>570;"
    rental = interaction.select_data(Q)
    rented_cars = list()
    for i in rental:
        if i[2] > latest_date:
            rented_cars.append(i[0])
    return set(rented_cars)


def generate_rentals(available, day0, daily_amt, daily_rent):
    '''
    generate a list of rentals for each day; daily rentals is a list of dictionaries
    containing car id and return day
    :param available:
    :param day0:
    :param daily_amt:
    :param daily_rent:
    :return:
    '''
    rental_list = list()
    availability_calendar = [set() for _ in range(31)]
    for day, available_cars in enumerate(availability_calendar):
        rental_perday = list()
        available.update(available_cars)
        try:
            rentals = set(rnd.sample(tuple(available), k=min(daily_amt * daily_rent[day], len(available))))
            if daily_amt >= 0 and daily_rent[day] > 0:
                rentals = set(rnd.sample(tuple(available), k=min(daily_amt * daily_rent[day], len(available))))
            else:
                raise ValueError("Daily number of rental and wages cannot be negative!")
        except IndexError:
            continue  # Ignore additions past the end of the list
        return_offsets = return_offset_fun(rentals)
        rent_date = day0 + timedelta(days=day)
        return_dates = []
        for i in range(len(rentals)):
            return_date = rent_date + timedelta(days=return_offsets[i])
            return_dates.append(return_date)
        for rental, offset, return_d in zip(rentals, return_offsets, return_dates):
            rental_perday.append(
                {"rental_date": str(datetime.combine(rent_date, datetime.min.time())), "car_id": rental,
                 "offset": offset, "return_date": str(datetime.combine(return_d, datetime.min.time()))})
            try:
                availability_calendar[day + offset].add(rental)
            except IndexError:
                continue  # Ignore additions past the end of the list
        rental_list.append(rental_perday)
        available = available - rentals
    return rental_list


def insert_data_list(rental_list, latest_index_from_db, customers, new_customers, rental_rates):
    amt = list()
    customer_id = list()
    create_date = list()

    for i in new_customers:
        customer_id.append(i[0])
        create_date.append(i[1])
        amt.append(0)

    for i in customers:
        customer_id.append(i[0])
        create_date.append(i[2])
        amt.append(i[1])

    insert_list = []
    for day in rental_list:
        possible_indx = list()
        for i in range(len(create_date)):
            if create_date[i].date() > datetime.strptime(day[0]["rental_date"], '%Y-%m-%d %H:%M:%S').date():
                possible_indx.append(i)
            else:
                continue

        available_customers = list()
        amounts = list()

        for index in possible_indx:
            available_customers.append(customer_id[index])
            amounts.append(amt[index])

        weights = amounts.reverse()
        for i, rent in enumerate(day):
            cust_id = rnd.choices(available_customers, weights=weights, k=1)
            cust_idnx = customer_id.index(cust_id[0])
            amt[cust_idnx] = amt[cust_idnx] + 1
            staff_id = rnd.randint(1, 52)
            insert_list.append((latest_index_from_db,
                                rental_rates[rent["car_id"]],
                                cust_id[0],
                                rent["car_id"],
                                staff_id,
                                rent["rental_date"],
                                rent["return_date"],
                                str(datetime.strptime(rent["rental_date"], '%Y-%m-%d %H:%M:%S') + timedelta(days=7)),
                                rent["rental_date"]))
            latest_index_from_db += 1
    return insert_list


def return_offset_fun(rentals):
    duration = [rnd.randint(1, 15) for _ in range(1, 16)]
    weights = duration.reverse()
    return_offset = [rnd.choices(duration, weights=weights, k=1) for _ in rentals]
    return_offset = sum(return_offset, [])
    return return_offset


def daily_rentals(last_date):
    if last_date.month != 12:
        next_month = last_date.month + 1
        year = last_date.year

    else:
        next_month = 1
        year = last_date.year + 1

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



if __name__ == '__main__':
    latest_date_from_db = get_latest_date()
    free_cars = get_free_cars(latest_date_from_db)
    rented_cars = get_rented_cars(latest_date_from_db)
    inv = free_cars.update(rented_cars)
    daily_rent_number = 300
    daily_rent, month = daily_rentals(latest_date_from_db)
    rental_list = generate_rentals(free_cars, latest_date_from_db, daily_rent_number, daily_rent)
    latest_index_from_db = get_latest_index() + 1
    customers = get_customers()
    new_customers = get_new_customers(latest_date_from_db)
    rental_rates = get_rental_rate()
    insert_list = insert_data_list(rental_list, latest_index_from_db, customers, new_customers, rental_rates)
