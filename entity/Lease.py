class Lease:
    def __init__(self, leaseID, vehicleID, customerID, startDate, endDate, leaseType):
        self.__leaseID = leaseID
        self.__vehicleID = vehicleID
        self.__customerID = customerID
        self.__startDate = startDate
        self.__endDate = endDate
        self.__leaseType = leaseType

    def getLeaseID(self):
        return self.__leaseID

    def getVehicleID(self):
        return self.__vehicleID

    def getCustomerID(self):
        return self.__customerID

    def getStartDate(self):
        return self.__startDate

    def getEndDate(self):
        return self.__endDate

    def getLeaseType(self):
        return self.__leaseType

    def setStartDate(self, startDate):
        self.__startDate = startDate

    def setEndDate(self, endDate):
        self.__endDate = endDate

    def setLeaseType(self, leaseType):
        self.__leaseType = leaseType
