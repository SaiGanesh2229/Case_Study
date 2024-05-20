INSERT INTO Vehicle (vehicleID, make, model, year, dailyRate, status, passengerCapacity, engineCapacity) 
VALUES 
(1, 'Toyota', 'Corolla', 2019, 50.00, 'available', 5, 1.8),
(2, 'Honda', 'Accord', 2020, 60.00, 'available', 5, 2.0),
(3, 'Maruti', 'Swift', 2018, 40.00, 'available', 5, 1.2),
(4, 'Ford', 'Fusion', 2017, 55.00, 'notAvailable', 5, 2.5),
(5, 'Chevrolet', 'Cruze', 2019, 65.00, 'available', 5, 1.4),
(6, 'Hyundai', 'Elantra', 2021, 70.00, 'available', 5, 2.0),
(7, 'Tata', 'Tiago', 2020, 45.00, 'available', 5, 1.2),
(8, 'Nissan', 'Sentra', 2016, 48.00, 'notAvailable', 5, 1.6),
(9, 'BMW', '3 Series', 2020, 100.00, 'available', 5, 2.0),
(10, 'Audi', 'A4', 2021, 110.00, 'available', 5, 2.0),
(11, 'Mercedes-Benz', 'C-Class', 2019, 120.00, 'available', 5, 2.0),
(12, 'Jeep', 'Wrangler', 2020, 90.00, 'available', 5, 3.6),
(13, 'Volkswagen', 'Jetta', 2018, 75.00, 'available', 5, 1.4),
(14, 'Kia', 'Optima', 2020, 80.00, 'available', 5, 2.0),
(15, 'Renault', 'Duster', 2017, 55.00, 'available', 5, 1.5);

INSERT INTO Customer (customerID, firstName, lastName, email, phoneNumber) 
VALUES 
(1, 'John', 'Doe', 'john.doe@example.com', '1234567890'),
(2, 'Jane', 'Smith', 'jane.smith@example.com', '9876543210'),
(3, 'Amit', 'Patel', 'amit.patel@example.com', '7890123456'),
(4, 'Emily', 'Johnson', 'emily.johnson@example.com', '3456789012'),
(5, 'Rahul', 'Gupta', 'rahul.gupta@example.com', '5678901234'),
(6, 'Samantha', 'Brown', 'samantha.brown@example.com', '9012345678'),
(7, 'Priya', 'Sharma', 'priya.sharma@example.com', '2345678901'),
(8, 'Michael', 'Williams', 'michael.williams@example.com', '6789012345'),
(9, 'Sanjay', 'Singh', 'sanjay.singh@example.com', '4567890123'),
(10, 'Jennifer', 'Martinez', 'jennifer.martinez@example.com', '8901234567'),
(11, 'Ananya', 'Das', 'ananya.das@example.com', '3210987654'),
(12, 'Christopher', 'Lee', 'christopher.lee@example.com', '6543210987'),
(13, 'Aarav', 'Shah', 'aarav.shah@example.com', '0123456789'),
(14, 'Olivia', 'Brown', 'olivia.brown@example.com', '8765432109'),
(15, 'Neha', 'Kumar', 'neha.kumar@example.com', '5432109876');

INSERT INTO Lease (leaseID, vehicleID, customerID, startDate, endDate, type) 
VALUES 
(1, 1, 2, '2024-05-01', '2024-05-05', 'DailyLease'),
(2, 3, 5, '2024-05-02', '2024-05-07', 'DailyLease'),
(3, 6, 9, '2024-05-03', '2024-05-09', 'MonthlyLease'),
(4, 8, 12, '2024-05-04', '2024-05-06', 'DailyLease'),
(5, 10, 15, '2024-05-05', '2024-05-08', 'DailyLease'),
(6, 12, 3, '2024-05-06', '2024-05-10', 'MonthlyLease'),
(7, 14, 6, '2024-05-07', '2024-05-12', 'DailyLease'),
(8, 2, 8, '2024-05-08', '2024-05-11', 'DailyLease'),
(9, 5, 11, '2024-05-09', '2024-05-13', 'MonthlyLease'),
(10, 7, 14, '2024-05-10', '2024-05-15', 'DailyLease'),
(11, 9, 1, '2024-05-11', '2024-05-16', 'DailyLease'),
(12, 11, 4, '2024-05-12', '2024-05-18', 'MonthlyLease'),
(13, 13, 7, '2024-05-13', '2024-05-19', 'DailyLease'),
(14, 15, 10, '2024-05-14', '2024-05-17', 'DailyLease'),
(15, 4, 13, '2024-05-15', '2024-05-20', 'MonthlyLease');

INSERT INTO Payment (paymentID, leaseID, paymentDate, amount) 
VALUES 
(1, 1, '2024-05-05', 250.00),
(2, 3, '2024-05-09', 1200.00),
(3, 6, '2024-05-10', 800.00),
(4, 7, '2024-05-12', 350.00),
(5, 9, '2024-05-13', 1500.00),
(6, 10, '2024-05-15', 400.00),
(7, 12, '2024-05-18', 2000.00),
(8, 13, '2024-05-19', 500.00),
(9, 14, '2024-05-17', 600.00),
(10, 15, '2024-05-20', 1000.00),
(11, 2, '2024-05-11', 180.00),
(12, 4, '2024-05-06', 330.00),
(13, 5, '2024-05-08', 195.00),
(14, 8, '2024-05-10', 240.00),
(15, 11, '2024-05-16', 500.00);