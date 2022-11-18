
class RideManager:

    def __init__(self) -> None:
        print('Ride Manager Activated!')
        self.__income = 0
        self.__trip_history = []
        self.__available_cars = []
        self.__available_bikes = []
        self.__available_cngs = []


    def add_a_vehicle(self,vehicle_type,vehicle):

        if vehicle_type == 'car':
            self.__available_cars.append(vehicle)
        elif vehicle_type == 'bike':
            self.__available_bikes.append(vehicle)
        else:
            self.__available_cngs.append(vehicle)



    def get_available_cars(self):
        return self.__available_cars

    
    def total_income(self):
        return self.__income
                
    

    def trip_history(self):
        return self.__trip_history


    def find_a_vehicle(self,rider,vehicle_type,destination):
        
        if vehicle_type == 'car':
            vehicles = self.__available_cars
        elif vehicle_type == 'bike':
            vehicles = self.__available_bikes
        else:
            vehicles = self.__available_cngs

        if len(vehicles) == 0:
            print('Sorry! No car is available Now!')
            return False

        for vehicle in vehicles:

            #print('Potential', rider.location,car.driver.location)  
            if abs(rider.location - vehicle.driver.location) < 30:
                distance = abs(rider.location - destination)
                fare = distance * vehicle.rate

                if rider.balance < fare:
                    print(f"Sorry! Your Balance: {rider.balance} Ride's Fare:{fare} Balance Low!")
                    return False

                if vehicle.status == 'Available':
                    trip_info = f'We have a {vehicle_type} for {rider.name}, Fare: {fare} Tk, Driver Name: {vehicle.driver.name}, From: {rider.location} To: {destination}\n'
                    print(trip_info)
                    rider.start_a_trip(fare,trip_info)
                    vehicle.driver.start_a_trip(rider.location,destination,fare*0.8,trip_info)
                    self.__income+=fare*0.2
                    self.__trip_history.append(trip_info)
                    return True

            else:
                print(f'Currently There Is No {vehicle_type} Close To Your Location!')





uber = RideManager()
 