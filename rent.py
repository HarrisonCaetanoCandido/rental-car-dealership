from user import User
from vehicle import Vehicle

class Rent:
    def __init__(self, user: User):
        self.owner = user
        self.owner.set_rent_list(self)
        self.rented_vehicle: Vehicle = []

    def add_vehicle(self, vehicle, date_it_was_rented, date_it_will_be_returned):
        vehicle.set_rental_date(date_it_was_rented, date_it_will_be_returned)
        self.rented_vehicle.append(vehicle)

    def remove_vehicle(self, plate):
        for index in range(0, len(self.rented_vehicle)):
            if self.rented_vehicle[index].plate == plate:
                self.rented_vehicle[index].reset_vehicle_rent_data()
                del(self.rented_vehicle[index])
            
    def get_rented_vehicles(self):
        return [self.rented_vehicle, len(self.rented_vehicle)]