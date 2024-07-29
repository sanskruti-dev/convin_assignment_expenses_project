# Convin Assignmment - Expenses Management Project - Python Django

# Tech Stack
- Python 3.12.4
- Django 5.x
- db sqlite
- DRF ( Django Rest Framework )
- JWT Authentication
# Setup
1) Git clone
2) Goto the directory and create virtual environment `python3 -m venv venv` and activate `source venv/bin/activate`
3) Install Django `pip3 install django djangorestframework`
4) Create Migrations `python3 manage.py makemigration` and Execute them `python3 manage.py migrate`
5) Run Server `python3 manage.py runserver`
6) Import this Postman Collection https://github.com/sanskruti-dev/convin_assignment_expenses_project/blob/main/Expense-Management-Convin-Assignment.postman_collection.json 

# Run and Test
1) User Creation API
<img width="1291" alt="image" src="https://github.com/user-attachments/assets/3fc54ea3-3e55-4da1-8514-eb8ee1bac8e7">

2) Get JWT API
`Case 1: If wrong email`
<img width="1356" alt="image" src="https://github.com/user-attachments/assets/6c2dfa76-6a9f-48d6-ae35-b27a02042823">
`Case 2: Valid user`
 <img width="1306" alt="image" src="https://github.com/user-attachments/assets/023c0ba8-6f7d-45e0-9eb1-ea5f6a341bdd">

4) All Users Fetch API
<img width="1271" alt="image" src="https://github.com/user-attachments/assets/199aeba1-e531-4b5a-b31c-c2d8067c03bb">

5) Get User By Id
<img width="1359" alt="image" src="https://github.com/user-attachments/assets/cd06b5fc-cad9-4aba-8d0b-6a79658d72a7">

6) Create Expense API
`Case 1: Without JWT token`
<img width="1357" alt="image" src="https://github.com/user-attachments/assets/dd76d93c-cfc7-43bf-a85d-b04b9850a7ed">

`Case 2: With invalid/expired JWT token`
<img width="1352" alt="image" src="https://github.com/user-attachments/assets/694cda98-762e-43c4-9354-5abda8fc3569">

`Case 3: With Equal Share Method`
<img width="1359" alt="image" src="https://github.com/user-attachments/assets/97a9955f-2e6a-40d2-bd37-ad334e6556ab">

`Case 4: With Exact amount Share Method`
<img width="1317" alt="image" src="https://github.com/user-attachments/assets/7e1e6e03-017e-4672-8afb-59844e3f7aea">

`Case 5: With Percentage Share Meethod`
<img width="1337" alt="image" src="https://github.com/user-attachments/assets/094756c6-3fa7-4583-b704-6aaefa9566bc">

`Case 6: With percentage sum going beyond 100`
<img width="1341" alt="image" src="https://github.com/user-attachments/assets/8f03746e-4891-4aac-a403-5779896578c8">

8) Fetch All Expenses API
<img width="1347" alt="image" src="https://github.com/user-attachments/assets/c2cdf496-38dd-4dbd-90cd-0b719f679dd3">

9) Fetch Expense by User API
<img width="1307" alt="image" src="https://github.com/user-attachments/assets/363dc66d-9808-4c7a-b6eb-baffcde05c84">

10) Fetch Expense by Expense Id API
    <img width="1304" alt="image" src="https://github.com/user-attachments/assets/019403e0-6eec-46b1-8f31-a1e6a4e30790">

11) Download Balance Sheet in CSV format API
<img width="1363" alt="image" src="https://github.com/user-attachments/assets/9a0b644d-9351-4b56-834b-e44a1385ffcd">
<img width="650" alt="image" src="https://github.com/user-attachments/assets/846260a2-6539-4eca-b623-31f59c8f1bfe">


