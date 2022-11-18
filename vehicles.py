from abc import ABC, abstractmethod
import time

class Vehicle(ABC):

    speed = {
            
            'car' : 30,
            'bike' : 50,
            'cng' : 15
            
    }
    def __init__(self,vehicle_type,license_plate,rate,driver):
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate = rate
        self.driver = driver
        self.status = 'Available'
        self.speed = self.speed[vehicle_type]



    @abstractmethod
    def start_driving(self):
        pass


    @abstractmethod
    def trip_finished(self):
        pass



class Car(Vehicle):

    def __init__(self, vehicle_type, license_plate, rate, driver):
        super().__init__(vehicle_type, license_plate, rate, driver)



    def start_driving(self, start_des, end_des):
        self.status = 'UnAvailable'
        print(f'Vehicle: {self.vehicle_type}, License: {self.license_plate} Started!\n')
        distance = abs(start_des - end_des)
        for i in range(0,distance):
            time.sleep(0.5)
            print(f'Driving: {self.license_plate}, Current Position: {i} of {distance}\n')

        self.trip_finished()

    def trip_finished(self):
        self.status = 'Available'
        print(f'{self.vehicle_type},{self.license_plate} Completed Trip!\n')


class Bike(Vehicle):

    def __init__(self, vehicle_type, license_plate, rate, driver):
        super().__init__(vehicle_type, license_plate, rate, driver)



    def start_driving(self, start, destination):
        self.status = 'UnAvailable'
        print(self.vehicle_type,self.license_plate, 'Started!')
        distance = abs(start - destination)
        for i in range(0,distance):
            time.sleep(0.5)
            print(f'Driving: {self.license_plate}, Current Position: {i} of {distance}\n')

        self.trip_finished()

    def trip_finished(self):
        self.status = 'Available'
        print(self.vehicle_type,self.license_plate, 'Completed Trip!')


class Cng(Vehicle):

    def __init__(self, vehicle_type, license_plate, rate, driver):
        super().__init__(vehicle_type, license_plate, rate, driver)


    def start_driving(self, start, destination):
        self.status = 'UnAvailable'
        print(self.vehicle_type,self.license_plate, 'Started!')
        distance = abs(start - destination)
        for i in range(0,distance):
            time.sleep(0.5)
            print(f'Driving: {self.license_plate}, Current Position: {i} of {distance}\n')

        self.trip_finished()

    def trip_finished(self):
        self.status = 'Available'
        print(self.vehicle_type,self.license_plate, 'Completed Trip!')



