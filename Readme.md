# Orders Project

This project is a simple Django-based API for managing orders. It includes endpoints to create, retrieve, update, partially update, and delete orders.

## Prerequisites

- Python 3.8+
- Django 3.2+
- Django REST Framework
- Postman (for API testing)

## Setup Instructions

### 1. Clone the repository

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


The API will be available at `http://localhost:8000/api/`.

## Running Tests

To run the automated tests, use the following command:

    python manage.py test

## Testing the API using Postman
1. To create an order
   1. http://127.0.0.1:8000/api/orders/
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
   1. http://127.0.0.1:8000/api/orders/
   2. Method: GET
3. To get information of a particular order
   1. http://127.0.0.1:8000/api/orders/:order_id/
   2. Method: GET
4. To update a full order
   1.  http://127.0.0.1:8000/api/orders/:order_id/
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
    1.  http://127.0.0.1:8000/api/orders/:order_id/
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
   1.  http://127.0.0.1:8000/api/orders/:order_id/
   2. Method: DELETE