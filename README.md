

# Late Show API

A Flask REST API for managing a Late Night TV show system with PostgreSQL, JWT authentication, and MVC architecture.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<username>/late-show-api-challenge.git
   cd late-show-api-challenge
   ```

2. **Install Dependencies**:
   ```bash
   pipenv install
   pipenv shell
   ```

3. **Set Up PostgreSQL**:
   ```sql
   CREATE DATABASE late_show_db;
   ```

4. **Configure Environment**:
   Update `server/config.py` with your PostgreSQL credentials:
   ```python
   SQLALCHEMY_DATABASE_URI = 'postgresql://<user>:<password>@localhost:5432/late_show_db'
   ```

5. **Run Migrations and Seed Data**:
   ```bash
   export FLASK_APP=server/app.py
   flask db init
   flask db migrate -m "initial migration"
   flask db upgrade
   python server/seed.py
   ```

6. **Run the Application**:
   ```bash
   python server/app.py
   ```

## Authentication Flow

1. **Register**: Create a user with `POST /register`.
   ```json
   {
       "username": "testuser",
       "password": "testpass"
   }
   ```
   Response:
   ```json
   {"message": "User registered successfully"}
   ```

2. **Login**: Get a JWT token with `POST /login`.
   ```json
   {
       "username": "testuser",
       "password": "testpass"
   }
   ```
   Response:
   ```json
   {"access_token": "<jwt-token>"}
   ```

3. **Use Token**: Include the token in the `Authorization` header for protected routes:
   ```
   Authorization: Bearer <jwt-token>
   ```

## Routes

| Route                  | Method | Auth Required? | Description                          |
|------------------------|--------|----------------|--------------------------------------|
| `/register`            | POST   | ❌             | Register a user                      |
| `/login`               | POST   | ❌             | Log in and return JWT                |
| `/episodes`            | GET    | ❌             | List all episodes                    |
| `/episodes/<id>`       | GET    | ❌             | Get episode details with appearances |
| `/episodes/<id>`       | DELETE | ✅             | Delete episode and its appearances   |
| `/guests`              | GET    | ❌             | List all guests                      |
| `/appearances`         | POST   | ✅             | Create a new appearance              |

### Sample Request/Response

**POST /appearances**:
```json
{
    "rating": 4,
    "guest_id": 1,
    "episode_id": 1
}
```
Response:
```json
{
    "message": "Appearance created",
    "id": 1
}
```

## Postman Usage

1. Import `challenge-4-lateshow.postman_collection.json` into Postman.
2. Set the `baseUrl` variable to `http://localhost:5000`.
3. Register and login to obtain a JWT token.
4. Copy the token to the `token` variable in Postman.
5. Use the token for protected routes (`DELETE /episodes/<id>`, `POST /appearances`).

## GitHub Repository

[https://github.com/<username>/late-show-api-challenge](https://github.com/<username>/late-show-api-challenge)

