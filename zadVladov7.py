class ElectricAppliance:
    def turn_IN(self):
        print(f"{self.__class__.__name__} is turning on.")
    def turn_off(self):
        print(f"{self.__class__.__name__} is turning off.")

class SmartDevice:
    def connect_to_wifi(self):
        print(f"{self.__class__.__name__} is connecting to Wi-Fi.")
    def disconnect_from_wifi(self):
        print(f"{self.__class__.__name__} is disconnecting from Wi-Fi.")

class SmartTV(ElectricAppliance, SmartDevice):
    pass

if __name__ == "__main__":
    tv = SmartTV()
    tv.turn_IN()
    tv.connect_to_wifi()
