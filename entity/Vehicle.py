# entity/vehicle.py
class Vehicle:
    def __init__(
        self,
        vehicleID,
        make,
        model,
        year,
        dailyRate,
        status,
        passengerCapacity,
        engineCapacity,
    ):
        self.__vehicleID = vehicleID
        self.__make = make
        self.__model = model
        self.__year = year
        self.__dailyRate = dailyRate
        self.__status = status
        self.__passengerCapacity = passengerCapacity
        self.__engineCapacity = engineCapacity

    def getVehicleID(self):
        return self.__vehicleID

    def getMake(self):
        return self.__make

    def getModel(self):
        return self.__model

    def getYear(self):
        return self.__year

    def getDailyRate(self):
        return self.__dailyRate

    def getStatus(self):
        return self.__status

    def getPassengerCapacity(self):
        return self.__passengerCapacity

    def getEngineCapacity(self):
        return self.__engineCapacity

    def setMake(self, make):
        self.__make = make

    def setModel(self, model):
        self.__model = model

    def setYear(self, year):
        self.__year = year

    def setDailyRate(self, dailyRate):
        self.__dailyRate = dailyRate

    def setStatus(self, status):
        self.__status = status

    def setPassengerCapacity(self, passengerCapacity):
        self.__passengerCapacity = passengerCapacity

    def setEngineCapacity(self, engineCapacity):
        self.__engineCapacity = engineCapacity
