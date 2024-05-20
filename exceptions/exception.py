class CustomerManagementException(Exception):
    def __init__(self, message="Customer management issue"):
        self.message = message
        super().__init__(self.message)


class AddCustomerException(Exception):
    def __init__(self, message="Error adding customer"):
        super().__init__(message)


class UpdateCustomerException(Exception):
    def __init__(self, message="Error updating customer information"):
        super().__init__(message)


class RetrieveCustomerException(Exception):
    def __init__(self, message="Error retrieving customer details"):
        super().__init__(message)


class CarManagementException(Exception):
    def __init__(self, message="Car management issue"):
        self.message = message
        super().__init__(self.message)


class AddCarException(Exception):
    def __init__(self, message="Error adding car"):
        super().__init__(message)


class UpdateCarException(Exception):
    def __init__(self, message="Error updating car availability"):
        super().__init__(message)


class RetrieveCarException(Exception):
    def __init__(self, message="Error retrieving car information"):
        super().__init__(message)


class LeaseManagementException(Exception):
    def __init__(self, message="Lease management issue"):
        self.message = message
        super().__init__(self.message)


class CreateLeaseException(Exception):
    def __init__(self, message="Error creating lease"):
        super().__init__(message)


class CalculateLeaseCostException(Exception):
    def __init__(self, message="Error calculating lease cost"):
        super().__init__(message)


class PaymentHandlingException(Exception):
    def __init__(self, message="Payment handling issue"):
        self.message = message
        super().__init__(self.message)


class RecordPaymentException(Exception):
    def __init__(self, message="Error recording payment"):
        super().__init__(message)


class RetrievePaymentHistoryException(Exception):
    def __init__(self, message="Error retrieving payment history"):
        super().__init__(message)


class CalculateRevenueException(Exception):
    def __init__(self, message="Error calculating revenue"):
        super().__init__(message)
