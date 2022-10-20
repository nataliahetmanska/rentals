'''
FUNCTIONS:
generate_list_of_create_dates(num):
    creates list of num sorted dates in September with priority for weekends
generate_new_customers(num, list_of_create_date):
    creates list of num new customers with corresponding create_dates from list_of_create_dates(num)
generate_new_addresses(num, list_of_create_date):
    creates list of num new addresses with corresponding create_dates from list_of_create_dates(num)
'''

import interaction_with_database as interaction
from faker import Faker
import random
import pandas as pd
import unidecode
from datetime import timedelta


def getting_last_customer_id():
    query = "SELECT max(customer_id) from customer"
    last_cust_id = interaction.select_data(query)
    return last_cust_id[0][0]

def getting_last_address_id():
    query = "SELECT max(address_id) from address"
    last_address_id = interaction.select_data(query)[0][0]
    return last_address_id

def creating_list_of_tupples_containing_CityIDCountryID():
    query = "SELECT city_id, country_id from city"
    city_country = interaction.select_data(query)
    return city_country

def getting_latest_date_from_customer():
    Q = "SELECT create_date FROM customer ORDER BY create_date DESC LIMIT 1"
    latest_date = interaction.select_data(Q)[0][0]
    return latest_date

def generate_list_of_create_dates(num, last_date):
    start_date = last_date + timedelta(days=1)
    end_date = start_date + timedelta(days=31)
    start_date = start_date.strftime("%Y/%m/%d")
    end_date = end_date.strftime("%Y/%m/%d")
    dates = []
    for i in range(num):

        weekend_date = pd.bdate_range(start=start_date, end=end_date, freq="C", weekmask="Sat Sun")
        wknd = []
        for j in range(len(weekend_date)):
            wknd.append(str(weekend_date[j]))
        weekend_day = random.choice(wknd)
        
        work_days_date = pd.bdate_range(start=start_date, end=end_date, weekmask=None)
        wrk = []
        for j in range(len(work_days_date)):
            wrk.append(str(work_days_date[j]))
        work_days_day = random.choice(wrk)
        
        day_date = random.choice([work_days_day, weekend_day])
        dates.append(day_date)
        
    dates.sort()
    return dates

def getting_addresses(last_address_id):
    query = f"SELECT * FROM address where address_id>={last_address_id}"
    result = interaction.select_data(query)
    ids_addresses = []
    for record in result:
        ids_addresses.append(record[0])
    return ids_addresses

def choosing_random_country(city_id_country_id):
    random_city_country = random.choice(city_id_country_id)
    city_id = random_city_country[0]  # indeks Miasta klienta
    country_id = random_city_country[1]  # indeks Kraju Klienta

    countries_dict = {1: "pl_PL", 2: "de_DE", 3: "cs_CZ", 4: "sv_SE",
                      5: "fi_FI", 6: "no_NO", 7: "es_ES", 8: "fr_FR", 9: "en_IE",
                      10: "sk_SK", 11: "de_AT", 12: "hu_HU", 13: "it_IT", 14: "el_GR"}

    country_value = countries_dict[country_id]
    return country_value, city_id


def generate_new_customers(num, list_of_create_date, last_customer_id, ids_addresses):
    customer = []
    for x in range(num):
        fake = Faker(['de_DE', 'pl_PL', 'cs_CZ', 'sv_SE', 'fi_FI', 'no_NO', 'es_ES', 'fr_FR', 'en_IE', 'sk_SK', 'de_AT'])
        customer_id = x+last_customer_id+1
        if x%7==0:
            name = fake.name().lower()
        else:
            name = fake.name()
        first_name, last_name = name.split(' ', 1)
        if x%4==0:
            email = f"{unidecode.unidecode(last_name.lower())}@{fake.domain_name()}"
        elif x%9==0:
            email = f"{first_name[:3].lower()}{unidecode.unidecode(last_name.lower())}@{fake.domain_name()}"
        else:
            email = f"{unidecode.unidecode(first_name.lower())}.{unidecode.unidecode(last_name.lower())}@{fake.domain_name()}"
        address_id = ids_addresses[x]

        create_date = list_of_create_date[x]
        birth_date = str(fake.date_of_birth(None, 24, 70))
        last_update = create_date
        customer.append((customer_id, first_name, last_name, address_id, email, birth_date, create_date, last_update))

    return customer


def generate_new_addresses(num, list_of_create_date, last_address_id, city_id_country_id):
    addresses = []
    for x in range(num):
        country_value, city_id = choosing_random_country(city_id_country_id)
        fake = Faker(country_value)
        address_id = x+last_address_id+1
        full_address = fake.street_name() + ' ' + fake.building_number()
        address = full_address[:50]
        address2 = full_address[50:]
        postal_code = fake.postcode()
        last_update = list_of_create_date[x]
        addresses.append((address_id, address, address2, city_id, postal_code, last_update))

    return addresses

def insert_addresses(cursor, db, new_addresses):
    insert_addresses = """INSERT INTO  address (address_id, address, address2, city_id, postal_code, last_update) 
                VALUES (%s, %s, %s, %s, %s, %s)"""

    cursor.executemany(insert_addresses, new_addresses)
    db.commit()

def insert_customers(cursor, db, new_customers):
    insert_customer = """ INSERT INTO customer (customer_id, first_name, last_name, address_id, email, birth_date, create_date, last_update)
                        VALUES (%s, %s, %s, %s, %s, %s, %s,%s)  """

    cursor.executemany(insert_customer, new_customers)
    db.commit()

    
    
if __name__ == '__main__':

    num = input("Enter the number of new customers: ")
    num = int(num)
    last_date = getting_latest_date_from_customer()
    list_of_create_dates = generate_list_of_create_dates(num, last_date)
    
    city_id_country_id = creating_list_of_tupples_containing_CityIDCountryID()
    last_address_id = getting_last_address_id()
    new_addresses = generate_new_addresses(num, list_of_create_dates, last_address_id, city_id_country_id)
    
    #insert_addresses(cursor, db, new_addresses)

    last_customer_id = getting_last_customer_id()
    last_address_id1 = getting_last_address_id() - num + 1
    ids_addresses = getting_addresses(last_address_id1)
    new_customers = generate_new_customers(num, list_of_create_dates, last_customer_id, ids_addresses)

    #insert_customers(cursor, db, new_customers)
