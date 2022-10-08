from ast import Str


class Doctor:
    def BMI(weight, height):
        print("Your BMI is " + str(weight / (height ** 2)))

    def heartRate(rate):
        if rate > 60 and rate < 100:
            print(f"Your heart rate is {str(rate)}")
            print("Your heart rate is normal")
        else:
            print(f"Your heart rate is {str(rate)}")
            print("Your heart rate does not seem normal, please consult your doctor")


class Patient(Doctor):
    def __init__(self, name, weight, height, rate):
        print("Patient Name: " + name)
        print("Weight: " + str(weight))
        print("Height: " + str(height))
        Doctor.BMI(weight, height)
        Doctor.heartRate(rate)


patient1 = Patient("Michael", 30, 0.9114, 80)
patient2 = Patient("Jessica", 40, 1, 120)
