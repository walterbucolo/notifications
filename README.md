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

Creates a super user to access django admin.
### Django admin
```
http://localhost:8001/admin/
```
Access django admin with the credentials of the superuser created to add more notification types and rules

### Runing tests

```
make tests
```

### Seed database

```
make populate_database
```
This will trigger a command that creates some notification types with rules.

## Usage
### Sending notifications
To send a notification, follow these steps:
1. Access to:
```
http://localhost:8001/notifications/solution
```
2. Fill `User ID`, `Message`, `Notification Type`.
3. Click `Send`.
If the notification is sent correctly, the page will reload. You will see an error in case the notification is rate limited.

## Considerations
1. Additional configurations like versioning and effective dates can be added to the rule logic. This implementation is based on notification type, time window, and repetitions.
2. http://localhost:8001/notifications/solution is added for testing purposes.
3. Basic gateway implementation is also added for testing purposes. 
