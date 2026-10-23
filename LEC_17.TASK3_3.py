class SmartDevice:
    def _init_(self, brand):
        self.brand = brand
        self.__is_on = False


    def turn_on(self):
        self.__is_on = True

    def turn_off(self):
        self.__is_on = False

    @property 
    def get_status(self):
        return self.__is_on
            

class Smartlight(SmartDevice):
    def __init__(self, brand, brightness):
        super().__init__(brand)
        self.brightness = brightness
    
    def turn_on(self):
        super().turn_on()
        print(f"brand: {self.brand}, brightness: {self.brightness} is on")

phone = Smartlight(brand="Apple", brightness=50)
phone.turn_on()
print(f"Status Chek: A phone is on. {phone.get_status}")
phone.turn_off()
print(f"Shut down: A phone is on. {phone.get_status}")