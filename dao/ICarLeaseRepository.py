from abc import ABC, abstractmethod
from entity.Vehicle import Vehicle
from entity.Customer import Customer
from entity.Lease import Lease
from entity.Payment import Payment
from datetime import datetime
from typing import List, Dict


class ICarLeaseRepository(ABC):

    @abstractmethod
    def add_car(
        self,
        vehicle_id: int,
        make: str,
        model: str,
        year: int,
        daily_rate: float,
        status: str,
        passenger_capacity: int,
        engine_capacity: float,
    ) -> None:
        pass

    @abstractmethod
    def remove_car(self, car_id: int) -> None:
        pass

    @abstractmethod
    def list_available_cars(self) -> List[dict]:
        pass

    @abstractmethod
    def find_car_by_id(self, car_id: int) -> dict:
        pass

    @abstractmethod
    def add_customer(
        self, first_name: str, last_name: str, email: str, phone_number: str
    ) -> None:
        pass

    @abstractmethod
    def remove_customer(self, customer_id: int) -> None:
        pass

    @abstractmethod
    def list_customers(self) -> List[dict]:
        pass

    @abstractmethod
    def find_customer_by_id(self, customer_id: int) -> dict:
        pass

    @abstractmethod
    def create_lease(
        self,
        customer_id: int,
        vehicle_id: int,
        start_date: datetime,
        end_date: datetime,
        lease_type: str,
    ) -> None:
        pass

    @abstractmethod
    def return_car(self, lease_id: int) -> None:
        pass

    @abstractmethod
    def list_active_leases(self) -> List[dict]:
        pass

    @abstractmethod
    def list_lease_history(self) -> List[dict]:
        pass

    @abstractmethod
    def record_payment(
        self, lease_id: int, payment_date: datetime, amount: float
    ) -> None:
        pass

    @abstractmethod
    def retrieve_payment_history(self, lease_id: int) -> List[Dict[str, any]]:
        pass

    @abstractmethod
    def calculate_total_revenue(self) -> float:
        pass

    @abstractmethod
    def list_all_payments(self) -> List[Dict[str, any]]:
        pass

    @abstractmethod
    def list_of_rented_cars(self) -> List[dict]:
        pass
