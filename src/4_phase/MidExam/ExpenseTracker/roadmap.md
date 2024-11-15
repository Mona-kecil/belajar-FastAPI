There are 3 main parts in this project:
1. Resource Server
2. Auth Server
3. Database

## Client

The client is a simple web application that allows users to log in, view their expenses, and add new expenses.

## Resource Server
The resource server is responsible for handling the requests from the client and interacting with the database.

## Auth Server
The auth server is responsible for handling the authentication and authorization of users.

## Database
The database is a simple PostgreSQL database that stores the user's expenses and other information.

# Roadmap
- [ ] Database schema design
    - [ ] Create user model
    - [ ] Create transaction model
- [ ] Auth
    - [ ] Implement user registration feature: **Stores user information in the database**
    - [ ] Implement login feature: **Checks if the user exists in the database and returns a JWT token**
- [ ] Resource Server
    - [ ] Implement POST /expenses endpoint: **Authenticates the user and gives authorization to create a new expense that belongs to them**
    - [ ] Implement GET /expenses endpoint: **Authenticates the user and returns all expenses that belong to them**
    - [ ] Implement GET /expenses/:id endpoint: **Authenticates the user and returns the expense with the specified ID**
    - [ ] Implement PUT /expenses/:id endpoint: **Authenticates the user and updates the expense with the specified ID**
    - [ ] Implement DELETE /expenses/:id endpoint: **Authenticates the user and deletes the expense with the specified ID**
