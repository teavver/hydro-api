# Setup app

Clone the repo: `git clone https://github.com/teavver/hydro-api && cd hydro-api`

## Run using Docker:

1. `docker-compose up` (`-d` for detached mode)

## Running Locally (venv)

1. Create a virtual environment: `python3 -m venv venv`

2. Activate the environment:

   - On Unix/macOS: `. venv/bin/activate`
   - On Windows: `.\venv\Scripts\activate`

3. Install the dependencies: `pip install -r requirements.txt && cd hydro`

4. Set `ENV` to `local`:

   - On Unix/macOS: `ENV=local`
   - On Windows (PowerShell): `setx ENV "local"`

5. Run database migrations: `python manage.py migrate`
6. Run the development server: `python manage.py runserver 0.0.0.0:8000`
7. Access the application at `http://localhost:8000`.

# Running tests

Test an app with: `docker-compose exec web python manage.py test <app>`. Replace `<app>` with the app's name, e.g: `users_api` to run the tests inside [users_api/tests.py](hydro/users_api/tests.py)

# Migrations

Makemigrations: `docker-compose exec web python manage.py makemigrations`
Migrate changes: `docker-compose exec web python manage.py migrate`

# API

## Users API

Create a User account in order to access the Systems API

### Register a User

#### Methods: `POST`

#### URL: `/api/users/register/`

#### Request body:

```json
{
  "username": "string",
  "password": "string"
}
```

### Login as a User

#### Methods: `POST`

#### URL: `/api/users/login/`

#### Request body:

```json
{
  "username": "string",
  "password": "string"
}
```

Returns the authentication `token` in response body on success

## Systems API

## Systems

### Model:

```json
{
  "name": "string",
  "type": "string",
  "created_at": "datetime",
  "owner": "userId"
}
```

The systems API provides endpoints for managing hydroponic systems and their measurements.
**All system endpoints require the auth `token`.**

### List and Create Systems

#### Methods: `GET`, `POST`

#### URL: `api/systems/system-list-create`

List all systems owned by an authenticated User or create a new System

#### Example Response (`GET`):

```json
[
  {
    "id": 8,
    "measurement_count": 0,
    "name": "testSystem2",
    "created_at": "2024-06-02T19:22:24.887014Z",
    "owner": 8
  },
  {
    "id": 7,
    "measurement_count": 0,
    "name": "testSystem1",
    "created_at": "2024-06-02T19:22:24.886759Z",
    "owner": 8
  }
]
```

#### Request body (`POST`):

```json
{
  "name": "NameOfNewSystem"
}
```

### Retrieve, Update, Delete a System

Get information about a specific System, update it, or delete it permanently. Deleting a System will delete all Measurements inside it.

#### Methods: `GET`, `PUT`, `DELETE`

#### URL: `api/systems/{id}`

#### Example Response (`GET`):

```json
{
  "id": 7,
  "measurement_count": 0,
  "name": "testSystem1",
  "created_at": "2024-06-02T19:22:24.886759Z",
  "owner": 8
}
```

#### Request body (`PUT`):

```json
{
  "name": "UpdatedSystemName"
}
```

## Measurements

### Model:

```json
{
  "id": "uniqueId",
  "system": "systemId",
  "temperature": "float",
  "pH": "float",
  "TDS": "float",
  "created_at": "datetime"
}
```

### List and Create Measurements

#### Methods: `GET`, `POST`

#### URL: `api/systems/measurements/`

List all measurements for the authenticated user's systems or create a new measurement. Supports filtering and sorting by date, temperature, pH, and TDS.

#### Filters and Sorting

- Filtering: You can filter measurements by date, temperature, pH, and TDS.
- Sorting: You can sort measurements by created_at, temperature, pH, and TDS.

#### Example Query Parameters for Filtering and Sorting (GET):

- `api/systems/measurements/?created_at=2024-06-01`: Filter by date.
- `api/systems/measurements/?temperature__gte=20`: Filter by temperature greater than or equal to 20.
- `api/systems/measurements/?pH__lte=7`: Filter by pH less than or equal to 7.
- `?ordering=temperature`: Sort by temperature.

#### Example Response (`GET`):

```json
[
  {
    "id": 1,
    "system": 7,
    "temperature": 22.5,
    "pH": 6.8,
    "TDS": 500,
    "created_at": "2024-06-02T19:22:24.887014Z"
  },
  {
    "id": 2,
    "system": 7,
    "temperature": 21.0,
    "pH": 6.5,
    "TDS": 550,
    "created_at": "2024-06-02T19:22:24.886759Z"
  }
]
```

#### Request Body (`POST`):

```json
{
  "system": "system_id",
  "temperature": 22.5,
  "pH": 6.8,
  "TDS": 500
}
```

### Latest Measurements

#### Methods: `GET`

#### URL: `api/systems/{id}/latest-measurements/`

Retrieve the 10 latest measurements for a specific hydroponic system owned by the authenticated user.

### Pagination:

All list endpoints use page number pagination (`10` by default)
