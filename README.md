# Sample Employee Database

This is a sample PostgreSQL database for a small company's employee records.

## Table: `employees`

| Field            | Description                    |
| ---------------- | ------------------------------ |
| id               | Primary key                    |
| first_name       | Employee first name            |
| last_name        | Employee last name             |
| email            | Unique email                   |
| phone_number     | Contact phone                  |
| job_title        | Job title                      |
| department       | Department (HR, Sales, etc.)   |
| salary           | Annual salary (USD)            |
| date_hired       | Date the employee was hired    |
| employment_type  | Full-time, Part-time, Contract |
| status           | Active, On Leave, Terminated   |
| address, city... | Location information           |

## How to Use

1. Import `company_employees.sql` into your PostgreSQL database.
2. Query or connect it to your web app for demos/testing.

## License

Free to use for demo and educational purposes.
