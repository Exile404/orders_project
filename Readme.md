# Orders Project

This project is a simple Django-based API for managing orders. It includes endpoints to create, retrieve, update, partially update, and delete orders.

## Prerequisites

- Python 3.8+
- Django 3.2+
- Django REST Framework
- Postman (for API testing)

## Setup Instructions

### 1. Clone the repository
      git clone https://github.com/Exile404/orders_project.git
      cd orders_project

### 2. Create a virtual environment

    python -m venv venv
    source venv/bin/activate
    venv\Scripts\activate #On windows

### 3. Install dependencies

    pip install -r requirements.txt


### 4. Apply migrations

    python manage.py migrate

### 5. Run the development server

    python manage.py runserver

### To get all API points

      The API are available at `https://orders-project.onrender.com/api/`.
      To run in a local machine replace https://orders-project.onrender.com with http://127.0.0.1:8000/api/

### 6.  To get full API Documentation. Run:
      https://orders-project.onrender.com/redoc/
      or
      https://orders-project.onrender.com/swagger/

## Running Tests

To run the automated tests, use the following command:

    python manage.py test

## Testing the API using Postman
1. To create an order
   1. https://orders-project.onrender.com/api/orders/
   2. Method: POST
    ```json
    {
        "user_id": 2,
        "total_amount": "100.00",
        "payment_status": "Pending",
        "items": [
            {"product_id": 1, "quantity": 2, "price": "50.00"}
        ]
    }
    ```
2. To get all orders list
   1. https://orders-project.onrender.com/api/orders/
   2. Method: GET
3. To get information of a particular order
   1. https://orders-project.onrender.com/api/orders/:order_id/
   2. Method: GET
4. To update a full order
   1.  https://orders-project.onrender.com/api/orders/:order_id/
   2. Method: PUT
   ```json
    {
    "user_id": 1,
    "total_amount": "150.00",
    "payment_status": "Completed",
    "items": [
        {"id": 1, "product_id": 1, "quantity": 3, "price": "50.00"}
      ]
    }
    ```
5. To update partial of an order
   1.    https://orders-project.onrender.com/api/orders/:order_id/
    2. Method: PATCH 
    ```json
    {
    "total_amount": "120.00",
    "items": [
        {"id": 1, "product_id": 1, "quantity": 4, "price": "30.00"}
      ]
    }
    ```
6. To delete an order
   1.  https://orders-project.onrender.com/api/orders/:order_id/
   2. Method: DELETE