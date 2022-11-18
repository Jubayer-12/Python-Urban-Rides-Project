import hashlib
import threading
from random import randint, choice
from brta import BRTA
from vehicles import Car,Bike,Cng
from ride_manager import uber



license_authority = BRTA()


class User:

    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()

        isExist = False
        with open('user_info.txt','r') as file:
            if email in file.read():
                isExist = True
        file.close()

        if isExist == False:
            with open('user_info.txt', 'a') as file:
               file.write(f'{email} {pwd_encrypted}\n')
            file.close()




class Driver(User):

    def __init__(self, name, email, password, location, license) -> None:
        super().__init__(name, email, password)
        self.location = location
        self.__trip_history = []
        self.license = license
        self.valid_driver = license_authority.validate_license(email, license)
        self.vehicle = None 
        self.earning = 0

    def take_driving_test(self):
        result = license_authority.take_driving_test(self.email)
        if result == False:
            self.license = None    
        else: 
            self.license = result
            self.valid_driver = True


    def register_a_vehicle(self,vehicle_type,license_plate,rate):
        
        if self.valid_driver is True:
            if vehicle_type == 'car':
                self.vehicle = Car(vehicle_type,license_plate,rate,self)
                uber.add_a_vehicle(vehicle_type,self.vehicle)
            elif vehicle_type == 'bike':
                self.vehicle = Bike(vehicle_type,license_plate,rate,self)
                uber.add_a_vehicle(vehicle_type,self.vehicle)
            else:
                self.vehicle = Cng(vehicle_type,license_plate,rate,self)     
                uber.add_a_vehicle(vehicle_type,self.vehicle)



    def start_a_trip(self, start, destination, fare, trip_info):

        self.earning += fare
        # Start Thread
        trip_thread = threading.Thread(target=self.vehicle.start_driving, args=(start,destination,))
        trip_thread.start()
        #self.vehicle.start_driving(start,destination)
        self.location = destination
        self.__trip_history.append(trip_info)



class Rider(User):

    def __init__(self, name, email, password, location, balance) -> None:
        super().__init__(name, email, password)
        self.location = location
        self.__trip_history = []
        self.balance = balance

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location


    def start_a_trip(self, fare, trip_info):
        print(f'A Trip Started For {self.name}\n')
        self.balance -= fare
        self.__trip_history.append(trip_info)

    def get_trip_history(self):
        return self.__trip_history






vehicle_types = ['car','bike','cng']


for i in range(0,100):
    driver1 = Driver(f'driver{i}',f'driver{i}@gmail.com',f'driver{i}23',randint(0,100),randint(1000,9999))
    driver1.take_driving_test()
    driver1.register_a_vehicle(choice(vehicle_types),randint(10000,99999),10)



rider1 = Rider('rider1','rider1@gmail.com','rider123',randint(0,100),1000)
rider2 = Rider('rider2','rider2@gmail.com','rider223',randint(0,100),5000)
rider3 = Rider('rider3','rider3@gmail.com','rider323',randint(0,100),5000)
rider4 = Rider('rider4','rider4@gmail.com','rider423',randint(0,100),5000)
rider5 = Rider('rider5','rider5@gmail.com','rider523',randint(0,100),5000)



uber.find_a_vehicle(rider1,choice(vehicle_types),randint(1,99))
uber.find_a_vehicle(rider2,choice(vehicle_types),randint(1,99))
uber.find_a_vehicle(rider3,choice(vehicle_types),randint(1,99))
uber.find_a_vehicle(rider4,choice(vehicle_types),randint(1,99))
uber.find_a_vehicle(rider5,choice(vehicle_types),randint(1,99))


print(uber.total_income())




