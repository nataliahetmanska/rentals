'''
FUNCTIONS:
generate_list_of_create_dates(num):
    creates list of num sorted dates in September with priority for weekends
generate_new_customers(num, list_of_create_date):
    creates list of num new customers with corresponding create_dates from list_of_create_dates(num)
generate_new_addresses(num, list_of_create_date):
    creates list of num new addresses with corresponding create_dates from list_of_create_dates(num)
'''


from faker import Faker
import random
import pandas as pd
import unidecode

def connection(host, user, password, database, port):
    import mysql.connector as msc
    mydb = msc.connect(host=host, port=port, user=user, password=password, database=dbname)
    cursor = mydb.cursor()
    return mydb, cursor

def getting_last_customer_id(cursor):
    last_cust_id = "SELECT max(customer_id) from customer"
    cursor.execute(last_cust_id)
    records = cursor.fetchall()
    return (records[0])[0]

def getting_last_address_id(cursor):
    last_address = "SELECT max(address_id) from address"
    cursor.execute(last_address)
    records = cursor.fetchall()
    return (records[0])[0]

def creating_list_of_tupples_containing_CityIDCountryID(cursor):
    city_query = "SELECT city_id, country_id from city"
    cursor.execute(city_query)
    records = cursor.fetchall()

    city_country = []
    for record in records:
        city_country.append(record)  # [(city_id, country_id),...]
    return city_country

def generate_list_of_create_dates(num):
    dates = []
    for i in range(num):

        weekend_date = pd.bdate_range(start="2022/08/30", end="2022/09/30", freq="C", weekmask="Sat Sun")
        weekends = weekend_date.date
        weekend_day = random.choice(weekends)

        work_days_date = pd.bdate_range(start="2022/08/30", end="2022/09/30", weekmask=None)
        work_days = work_days_date.date
        work_days_day = random.choice(work_days)

        day_date = random.choice([work_days_day, weekend_day])
        dates.append(day_date.strftime("%Y-%m-%d %H:%M:%S"))
    dates.sort()
    return dates

def generate_new_customers(cursor, num, list_of_create_date):
    
    last_customer_id = getting_last_customer_id(cursor)
    last_address_id = getting_last_address_id(cursor)-num+1

    cursor.execute("SELECT * FROM address where address_id>=(%s)", (last_address_id,))
    address_values = cursor.fetchall()
    ids_addresses = []
    for record in address_values:
        ids_addresses.append(record[0])

    customer = []
    for x in range(num):
        fake = Faker(['de_DE', 'pl_PL', 'cs_CZ', 'sv_SE', 'fi_FI', 'no_NO', 'es_ES', 'fr_FR', 'en_IE', 'sk_SK', 'de_AT'])
        customer_id = x+last_customer_id+1
        if x%28==0:
            name = fake.name().lower()
        else:
            name = fake.name()
        first_name, last_name = name.split(' ', 1)
        if x%11==0:
            email = f"{unidecode.unidecode(last_name.lower())}@{fake.domain_name()}"
        elif x%15==0:
            email = f"{last_name[:3].lower()}{unidecode.unidecode(last_name.lower())}@{fake.domain_name()}"
        else:
            email = f"{unidecode.unidecode(first_name.lower())}.{unidecode.unidecode(last_name.lower())}@{fake.domain_name()}"
        address_id = ids_addresses[x]

        create_date = list_of_create_date[x]
        birth_date = str(fake.date_of_birth(None, 24, 70))
        last_update = create_date
        customer.append((customer_id, first_name, last_name, address_id, email, birth_date, create_date, last_update))

    return customer


def generate_new_addresses(cursor, num, list_of_create_date):
   
    city_id_country_id = creating_list_of_tupples_containing_CityIDCountryID(cursor)
    last_address_id = getting_last_address_id(cursor)

    addresses = []
    for x in range(num):
        random_city_country = random.choice(city_id_country_id)
        city_id = random_city_country[0] #indeks Miasta klienta
        country_id = random_city_country[1] #indeks Kraju Klienta


        countries_dict = {1: "pl_PL", 2: "de_DE", 3: "cs_CZ", 4: "sv_SE",
                          5: "fi_FI", 6: "no_NO", 7: "es_ES", 8: "fr_FR", 9: "en_IE",
                          10: "sk_SK", 11: "de_AT", 12: "hu_HU", 13: "it_IT", 14: "el_GR"}

        country_value = countries_dict[country_id]
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

def generate_customers_and_addresses(cursor, db, num):
    create_dates = generate_list_of_create_dates(num)
    new_addresses = generate_new_addresses(cursor, num, create_dates)
    insert_addresses(cursor, db, new_addresses)
    generate_new_customers(cursor, num, create_dates)
    insert_customers(cursor, db, new_customers)
    
    
if __name__ == '__main__':
    user = keyring.get_password("username", "username")
    password = keyring.get_password("database_pass", user)
    port = keyring.get_password("database_port", user)
    database = keyring.get_password("database", user)
    host = keyring.get_password("database_host", user)
  
    db, cursor = connection(host=host, user=user, password=password, database=database, port=port)

    generate_customers_and_addresses(cursor, db, num)    
