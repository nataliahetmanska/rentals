
import interaction_with_database as interaction
import random as rnd
from datetime import timedelta, date

def get_latest_date():
    Q = "SELECT rental_date FROM rental ORDER BY rental_date DESC LIMIT 1"
    latest_date = interaction.select_data(Q)[0][0]
    return latest_date


def payment_id(amount):
    list_id = list(range(1, amount + 1))
    return list_id


def pay_amount(rental_rate, rental_date, return_date):
    amount = list()
    for i in range(len(rental_rate)):
        amt = abs(rental_rate[i] * (return_date[i] - rental_date[i]).days)
        amount.append(amt)

    return amount


def payment_date(payment_ddl, amt):
    payment = list()
    diff = list()
    for i in range(1, amt + 1):
        n = rnd.randint(-3, 3)
        diff.append(n)
    for i in range(len(payment_ddl)):
        payment.append(payment_ddl[i] + timedelta(days=diff[i]))
    return payment


def last_update(rental_date):
    update = list()
    for i in rental_date:
        time_between_dates = date.today() - i
        days_between_dates = time_between_dates.days
        random_number_of_days = rnd.randint(1, days_between_dates + 1)
        random_date = i + timedelta(days=random_number_of_days)
        update.append(random_date)
    return update


def get_rentals(latest_date):

    
    query = f'SELECT rental_id, rental_rate, customer_id, rental_date, return_date, payment_deadline FROM rental\
                    WHERE rental_date > {latest_date}'
    rentals = interaction.select_data(query)
    rental = [list(t) for t in zip(*rentals)]


    rental_id = rental[0]
    rental_rate = rental[1]
    customer_id = rental[2]
    rental_date = rental[3]
    return_date = rental[4]
    payment_deadline = rental[5]
    amount = len(rental[5])

    return rental_id, rental_rate, customer_id, rental_date, return_date, payment_deadline, amount


def max_payment_id():

    query = "SELECT payment_id FROM payment"
    previous_id = interaction.select_data(query)

    unzipped = list(zip(*previous_id))
    max_payment_id = max(unzipped[0])
    return max_payment_id


def insert_payment(payment):
    try:

        db, cursor = interaction.connection()
        sql = "INSERT INTO payment (payment_id, customer_id, rental_id, amount, payment_date, last_update) VALUES (%s, %s, %s,%s,%s, %s) "
        cursor.executemany(sql, payment)

        db.commit()

    except Exception as e:
        print("Exception occurred: {}".format(e))


def data_to_insert(payment_id, customer_id, rental_id, pay_amount, payment_date, last_updt):
    return list(zip(payment_id, customer_id, rental_id, pay_amount, payment_date, last_updt))


if __name__ == '__main__':

    
    latest_date_from_db = get_latest_date()
    max_payment_id = max_payment_id()
    rental_id, rental_rate, customer_id, rental_date, return_date, payment_deadline, amount = get_rentals(latest_date_from_db)
    payment_id = list(range(max_payment_id, max_payment_id + amount + 1))
    pay_amount = pay_amount(rental_rate, rental_date, return_date)
    payment_date = payment_date(payment_deadline, amount)
    last_updt = last_update(rental_date)
    payment = data_to_insert(payment_id, customer_id, rental_id, pay_amount, payment_date, last_updt)
    # insert_payment(payment)
