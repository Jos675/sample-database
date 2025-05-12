-- company_employees.sql

DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    job_title VARCHAR(100),
    department VARCHAR(50),
    salary INTEGER,
    date_hired DATE,
    employment_type VARCHAR(20), -- e.g., Full-time, Part-time, Contract
    status VARCHAR(20),          -- e.g., Active, Terminated, On Leave
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    zip_code VARCHAR(20)
);

INSERT INTO employees (
    first_name, last_name, email, phone_number, job_title, department, salary,
    date_hired, employment_type, status, address, city, state, zip_code
) VALUES
('Alice', 'Johnson', 'alice.johnson@company.com', '555-1234', 'Software Engineer', 'Engineering', 90000, '2020-06-15', 'Full-time', 'Active', '123 Elm St', 'Springfield', 'IL', '62701'),
('Bob', 'Martinez', 'bob.martinez@company.com', '555-5678', 'Sales Manager', 'Sales', 75000, '2019-04-01', 'Full-time', 'Active', '456 Oak Ave', 'Columbus', 'OH', '43085'),
('Cathy', 'Nguyen', 'cathy.nguyen@company.com', '555-2345', 'HR Generalist', 'HR', 68000, '2021-01-12', 'Full-time', 'On Leave', '789 Pine Rd', 'Austin', 'TX', '73301'),
('David', 'Lee', 'david.lee@company.com', '555-8765', 'Data Analyst', 'Analytics', 72000, '2022-08-10', 'Part-time', 'Active', '321 Maple St', 'Seattle', 'WA', '98101'),
('Emma', 'Clark', 'emma.clark@company.com', '555-4321', 'Office Admin', 'Operations', 52000, '2018-11-05', 'Full-time', 'Terminated', '987 Cedar Blvd', 'Denver', 'CO', '80201');
