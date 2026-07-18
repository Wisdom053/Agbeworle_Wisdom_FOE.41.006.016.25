#%%
from operator import truediv


#parent class_SmartDevice
class SmartDevice:
    def __init__(self,name,device_id):
        self.name = name
        self.device_id = device_id
        self.__power_status = False

 #device_id
    @property
    def device_id(self):
        return self.__device_id
    @device_id.setter
    def device_id(self,value):
        if value.strip == "":
            print("please enter values,device ID cannot be empty")
        else:
            self.__device_id = value

#device_status
    @property
    def power_status(self):
        return self.__power_status

    @power_status.setter
    def power_status(self,status):
        self.__power_status = status




    def turn_on(self):
        self.__power_status = True
        print(f"{self.name} has been turned ON")
    def turn_off(self):
        self.__power_status = False
        print(f"{self.name} has been turned OFF")

#display_info method
    def display_method():
        print("\n======DEVICE INFORMATION=====")
        print("device name:",self.name)
        print("device ID:",self.device_id)
        print("power status:","ON" if self.power_status else "off")
        print("==================================")


#creating sub classes
#temperature sensor
class TemperatureSensor(SmartDevice):
    def __init__(self,name,device_id,temperature=25):
        super().__init__(name,device_id)
        self.temperature = temperature

    def read_temperature(self):
        print(f"Device Temperature:={self.temperature} ֯֯֯degrees")

    def display_info(self):
        super().display_info()
        print("temperature:",self.temperature, "degrees")

#security camera
class SecurityCamera(SmartDevice):
    def __init__(self,name,device_id):
        super().__init__(name,device_id)
        self.recording_status = False

    def start_recording(self):
        if self.power_status:
            self.recording_status = True
            print("Recording started")

        else:
            print("please turn on the camera first")

    def stop_recording(self):
        self.recording_status = False
        print("Recording Stopped")

    def display_info(self):
        super().display_info()
        print("Recording:","Yes" if self.recording_status else "NO" )

#smartlight class
class SmartLight(SmartDevice):
    def __init__(self,name,device_id,brightness = 50):
        super().__init__(name,device_id)
        self.brightness = brightness

    @property
    def brightness(self):
        return self.__brightness

    @brightness.setter
    def brightness(self,value):
        if 0 <= value <= 100:
            self.__brightness = value
        else:
            print("Brightness must be between 0 and 100")
    def increase_brightness(self):
        if self.brightness < 100:
            self.brightness += 10
        print("Brightness",self.brightness)

    def decrease_brightness(self):
        if self.brightness >0:
            self.brightness -=10
        print("Brightness",self.brightness)

    def display_info(self):
        super().display_info()
        print("Brightness",self.brightness)

#Assigning variables
sensor =  TemperatureSensor("Living Room Sensor","Temp..01",23)
light = SmartLight("Bedroom Light","Light..01",40)
camera = SecurityCamera("Front Door camera","cam..01")

#menu for devices usage
while True:
    print("\n=========SMART DEVICE MNAGEMENT=========")
    print("1. Display device information")
    print("2. Turn device ON")
    print("3. Turn device OFF")
    print("4. Read Temperature")
    print("5. Adjust Brightness")
    print("6. start/stop Recording")
    print("7. Exit")


    choice = input("Please enter your choice: ")

    if choice == "1":
        sensor.display_info()
        light.display_info()
        camera.display_info()

    elif choice == "2":
        sensor.turn_on()
        light.turn_on()
        camera.turn_on()

    elif choice == "3":
        sensor.turn_off()
        light.turn_off()
        camera.turn_off()

    elif choice == "4":
        sensor.read_temperature()

    elif choice == "5":
        print("\n1. Increase Brightness")
        print("2. Decrease Brightness")

        for_light = input("Select an option:")

        if for_light == "1":
            light.increase_brightness()
        elif for_light == "2":
            light.decrease_brightness()
        else:
            print("please enter a valid option")

    elif choice == "6":
        print("\n1. Start Recording")
        print("2. Stop recording")

        for_camera = input("choice:")
        if for_camera == "1":
            camera.start_recording()
        elif for_camera == "2":
            camera.stiop_recording()
        else:
            print("Enter a valid option")

    elif choice == "7":
        print("you terminated the program")
        break

    else:
        print("Invalid choice.Try again!")
