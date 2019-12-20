from sol_car  import *
cars = get_car_list('cars.csv')
len(cars)

for car in cars:
    print(type(car))

cars[0].passenger_seats_count

cars[1].get_body_volume()
