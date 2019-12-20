import csv
from functools import reduce

           
        
class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying


class Car(CarBase):
    car_type = 'car'
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        #super().__init(self, brand, photo_file_name, carrying)
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        self.passenger_seats_count = passenger_seats_count
    def __str__(self):
        return '{},{},{},{},{}'.format(Car.car_type,self.brand, self.photo_file_name, self.carrying, self.passenger_seats_count)
    def __repr__(self):
        return '{},{},{},{},{}'.format(Car.car_type,self.brand, self.photo_file_name, self.carrying, self.passenger_seats_count)
    
        


class Truck(CarBase):
    car_type = 'truck'
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        self.body_whl = body_whl 
    def get_body_volume():
        l = self.body_whl.split('x')
        s = lambda x: int(x),l
        return reduce((lambda x, y: x * y),s)   
    def __str__(self):
        return '{},{},{},{},{}'.format(Truck.car_type,self.brand, self.photo_file_name, self.carrying, self.body_whl)
    def __repr__(self):
        return '{},{},{},{},{}'.format(Truck.car_type,self.brand, self.photo_file_name, self.carrying, self.body_whl)
    



class SpecMachine(CarBase):
    car_type = 'spec_machine'
    def __init__(self, brand, photo_file_name, carrying, extra):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        self.extra = extra
    def __str__(self):
        return '{},{},{},{},{}'.format(SpecMachine.car_type,self.brand, self.photo_file_name, self.carrying, self.extra)
    def __repr__(self):
        return '{},{},{},{},{}'.format(SpecMachine.car_type,self.brand, self.photo_file_name, self.carrying, self.extra)
    



def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader :
            if len(row)>0:
                #print('row',row)

                if row[0] == 'car':
                    car = Car(row[1],row[3],row[5],row[2])
                    car_list.append(car)

                if row[0] == 'truck':
                    truck = Truck(row[1],row[3],row[5],row[4])
                    car_list.append(truck)
               
                if row[0] == 'spec_machine':
                    spec_machine = SpecMachine(row[1],row[3],row[5],row[6])
                    car_list.append(spec_machine)



                print('car_list',car_list)
 
    return car_list
