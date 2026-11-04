# Customer Management System

A Streamlit web application with a MySQL backend for managing customers, products, orders and reviews. It has separate panels for admin users and customers, plus a dashboard with key business metrics.

## Features

- **User (Admin) Panel** – login, then manage Users, Customers, Products, purchased/returned items and reviews (view, search, add, edit, delete)
- **Customer Panel** – login, view products, buy a product, return a product
- **Reviews** – view all reviews and write a review (rating 1–5, max 200 characters)
- **Dashboard** – total customers, products, today's purchases and returns, total reviews, average rating

## Tech Stack

Python · Streamlit · MySQL · Pandas

## Project Structure

```
CustomerManagementSystem/
├── main.py             # Streamlit app
├── backend.py          # Script to insert a user directly into the database
├── CMS.sql             # Database schema + sample data
├── requirements.txt    # Dependencies
├── .gitignore
└── README.md
```

## Database Tables

`Users`, `Customer`, `Product`, `PurchaseItems`, `ReturnItems`, `Review`

## How to Run

1. Clone the repository
   ```bash
   git clone https://github.com/aaryanthakur133/CustomerManagementSystem.git
   cd CustomerManagementSystem
   ```
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the database – open MySQL and run the `CMS.sql` file. It creates the `CustomerManagement` database with sample data.
4. Set your MySQL password as an environment variable (the password is not stored in the code)
   ```bash
   set DB_PASSWORD=your_mysql_password            # Windows (cmd)
   $env:DB_PASSWORD="your_mysql_password"         # Windows (PowerShell)
   export DB_PASSWORD=your_mysql_password         # macOS / Linux
   ```
5. Start the app
   ```bash
   streamlit run main.py
   ```

## Sample Login (from CMS.sql)

| Panel    | ID | Password |
|----------|----|----------|
| User     | 1  | Admin@12 |
| Customer | 1  | shy@1    |

## Author

**Aaryan** – MCA graduate and Python developer
