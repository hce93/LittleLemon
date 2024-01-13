API paths:
Bookings:
restaurant/booking/tables (for authorised users to view the model view set)
restaurant/book (for clients to create new bookings)

Menu:
restaurant/menu (view menu)
restaurant/menu/<int:pk> (view individual menu items, authorized users only, can retrieve, update and destroy)

User registration:
auth/users (to create a new user)
auth/token/login (generate auth token, need to send POST request with details created in previous url)
restaurant/api-token-auth/ (equivalent to above)
