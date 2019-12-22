import csv
import sys
           
        
class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        sa = locals()
     #   print('locals from CarBase',sa)
        if not (brand and photo_file_name and carrying):
            raise ValueError
            
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
    def get_photo_file_ext(self):
        _,ext = self.photo_file_name.split('.')
        if ext not in ['jpeg','png','jpg','gif']:
            raise ValueError
        return '.' + ext


class Car(CarBase):
    car_type = 'car'
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        if not int(passenger_seats_count) > 0:
            raise ValueError
        self.passenger_seats_count = int(passenger_seats_count)
#    def __str__(self):
#        return '{},{},{},{},{}'.format(Car.car_type,self.brand, self.photo_file_name, self.carrying, self.passenger_seats_count)
    def __repr__(self):
        return '{},{},{},{},{}'.format(Car.car_type,self.brand, self.photo_file_name, self.carrying, self.passenger_seats_count)
    
        


class Truck(CarBase):
    car_type = 'truck'
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl 

        try:
            x,y,z = (float(c) for c in body_whl.split("x", 2))
        except ValueError:
            x, y, z = .0, .0, .0

        self.body_length = x
        self.body_width = y
        self.body_height = z

            
    def get_body_volume(self):
              return self.body_length * self.body_width * self.body_height 
#    def __str__(self):
#        return '{},{},{},{},{},{},{},{}'.format(Truck.car_type,self.brand, self.photo_file_name, self.carrying, self.body_whl,self.body_length, self.body_width, self.body_height)
    def __repr__(self):
        return '{},{},{},{},{}'.format(Truck.car_type,self.brand, self.photo_file_name, self.carrying, self.body_whl)
    



class SpecMachine(CarBase):
    car_type = 'spec_machine'
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        if not len(extra)>0:
            raise ValueError

        self.extra = extra
#    def __str__(self):
#        return '{},{},{},{},{}'.format(SpecMachine.car_type,self.brand, self.photo_file_name, self.carrying, self.extra)
    def __repr__(self):
        return '{},{},{},{},{}'.format(SpecMachine.car_type,self.brand, self.photo_file_name, self.carrying, self.extra)
    



def get_car_list(csv_filename):
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        car_list = []

        for row in reader :
            #print('row',row)
            try:
                r = row[0]
            except IndexError:
                continue


            if r == 'car':
                try:
                    car = Car(row[1],row[3],row[5],row[2])
                except ValueError:
                    continue

                try:
                    e = car.get_photo_file_ext()
                    car_list.append(car)
                except(ValueError, IndexError):
                    pass

          
            if r == 'truck':
                try:
                    truck = Truck(row[1],row[3],row[5],row[4])
                except ValueError:
                    continue
               
                try:
                    e = truck.get_photo_file_ext()
                    car_list.append(truck)
                except(ValueError, IndexError):
                    pass
           
            if r == 'spec_machine':
                try:
                    spec_machine = SpecMachine(row[1],row[3],row[5],row[6])
                except ValueError:
                    continue

                try:
                    e = spec_machine.get_photo_file_ext()
                    car_list.append(spec_machine)
                except(ValueError, IndexError):
                    pass



  #      print('car_list',car_list)

    return car_list

if __name__ == "__main__":
    print(get_car_list(sys.argv[1]))
