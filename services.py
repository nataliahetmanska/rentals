import interaction_with_database as interaction
from datetime import datetime, timedelta


def get_cars_in_stock(service_date):
    Q = "SELECT inventory_id, create_date, last_update FROM inventory"
    inventory = interaction.select_data(Q)
    buy_and_sell_date = []
    for i in inventory:
        if i[1] != i[2]:
            if i[2] >= service_date >= i[1]:
                buy_and_sell_date.append(i[0])
        else:
            if service_date >= i[1]:
                buy_and_sell_date.append(i[0])
    return buy_and_sell_date


def get_rented_cars(service_date):
    Q = f"SELECT inventory_id, rental_date, return_date FROM rental"
    result = interaction.select_data(Q)
    rented_cars = []
    service_date = service_date.date()
    for i in result:
        if i[2] > service_date >= i[1]:
            rented_cars.append({i[0]: i[2]})
    return rented_cars


def check_if_car_is_rented(inv_id, service_date):
    car_is_rented = (inv_id, service_date)
    rented_cars = get_rented_cars(service_date)
    for dictionary in rented_cars:
        for key, return_date in dictionary.items():
            if inv_id == key:
                car_is_rented = (inv_id, return_date)
    return car_is_rented


def get_service_dates():
    service_dates = []
    start_date = datetime.strptime('2016-07-01 00:00:00', '%Y-%m-%d %H:%M:%S')
    today = datetime.today()

    while start_date < today:
        service_dates.append(start_date)
        start_date += timedelta(days=31 * 6)
    return service_dates


def get_tire_change_dates():
    tire_dates = []
    start_date_summer = datetime.strptime('2016-03-15 00:00:00', '%Y-%m-%d %H:%M:%S')
    start_date_winter = datetime.strptime('2016-11-15 00:00:00', '%Y-%m-%d %H:%M:%S')
    today = datetime.today()
    while start_date_summer < today or start_date_winter < today:
        tire_dates.append(start_date_summer)
        tire_dates.append(start_date_winter)
        start_date_summer += timedelta(days=365)
        start_date_winter += timedelta(days=365)
    return tire_dates


def generate_services(service_dates, service_type, service_cost):
    service_table = []

    indeks = 1
    for s_date in service_dates:
        cars_stock = get_cars_in_stock(s_date)
        for stock_id in cars_stock:
            (inv_id, return_date) = check_if_car_is_rented(stock_id, s_date)
            if return_date == s_date:
                service_table.append((indeks, inv_id, service_type, s_date, service_cost))
            else:
                service_table.append((indeks, inv_id, service_type, return_date, service_cost))
            indeks += 1
    return service_table


def services_list():
    service_dates = get_service_dates()
    services = generate_services(service_dates, 'service', 500)
    return services


def tire_change_list():
    service_dates = get_tire_change_dates()
    tire_change = generate_services(service_dates, 'tire_change', 200)
    return tire_change


if __name__ == "__main__":
    services_list()
    tire_change_list()
