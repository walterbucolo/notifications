# Notifications
Notification service built with Django. It laverages Redis for rate limiting and PostgreSQL for persistant storage. The service protects recipients from getting too many emails, either due to system errors or due to abuse by implementing a rate-limit based on a time windows and the number of repetitions.

## Setting up the project

### Dependencies

Ensure to Install

*   Docker
*   Dockercompose
*   make

### Copy the .env.template to .env

```
cp .env.template .env
```
The .env file is copied into the container to access env vars like database configuration

### Run the initial migrations

```
make migrate
```

This command will create the empty tables on the DB

### Creates a superuser

```
make superuser
```

Creates a super user to access django admin

### Django admin

http://localhost:8001/admin/

### Runing tests

```
make tests
```


