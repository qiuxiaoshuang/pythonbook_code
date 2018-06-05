class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odomater_reading=0
        self.tank=0

    def get_descriptive_name(self):
        long_time=str(self.year)+' '+self.make+' '+self.model
        return long_time.title()

    def read_odomater(self):
        print("This car has "+str(self.odomater_reading)+" miles on it.")

    def update_odomater(self,mileage):
        if mileage>=self.odomater_reading:
            self.odomater_reading=mileage
        else:
            print("You can not roll back an odometer")

    def increment_odometer(self,miles):
        self.odomater_reading+= miles

    def fill_gas_tank(self,tank):
        self.tank=tank


class Battery():
    def __init__(self,battery_size=70):
        self.battery_size=battery_size

    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+".")

    def get_range(self):
        if self.battery_size==70:
            range=240
        elif self.battery_size==85:
            range=270
        message="This car can go approximately"+str(range)
        message+="mile on a full charge"
        print(message)



class ElectricCar(Car):
    def __init__(self,make,model,year):
        super(ElectricCar, self).__init__(make,model,year)
        self.battery=Battery()

    # def describe_battery(self):
    #     print("This car has a "+str(self.battery_size)+".")


    def fill_gas_tank(self):
        print("There is no gas tank")