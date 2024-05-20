class Payment:
    def __init__(self, paymentID, leaseID, paymentDate, amount):
        self.__paymentID = paymentID
        self.__leaseID = leaseID
        self.__paymentDate = paymentDate
        self.__amount = amount

    def getPaymentID(self):
        return self.__paymentID

    def getLeaseID(self):
        return self.__leaseID

    def getPaymentDate(self):
        return self.__paymentDate

    def getAmount(self):
        return self.__amount

    def setPaymentDate(self, paymentDate):
        self.__paymentDate = paymentDate

    def setAmount(self, amount):
        self.__amount = amount
