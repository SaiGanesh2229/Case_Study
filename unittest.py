import unittest
from dao import Carmanagement, CustomerRepository, PaymentHandler, LeaseRepository
from entity import Vehicle, Customer


class TestException(unittest.TestCase):

    def setUp(self):
        self.customer_service = CustomerRepository()
        self.car_service = Carmanagement()

    def test_customer_id(self):
        customer_id = 10002
        customer = self.customer_service.check_customerid(customer_id)
        self.assertIsNotNone(customer)

    def test_product_id(self):
        car_service = 20002
        product = self.car_service.check_productid(car_service)
        self.assertIsNotNone(product)
