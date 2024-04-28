# Todo App

This is a simple todo app built with Django.
I made a attemt of using htmx for the first time, so some code, related to that might ot be optimal.

## Improvemets

- Can benefit from use of paginationn
- Better use of class-based views

## Getting Started

To run the app, you need to have Docker installed on your machine.

### Building the Docker Image

Run the following command to build the Docker image:

```bash
docker build . -t todo
```

### Running the Docker Container

Once the image is built, you can run the Docker container with the following command:

```bash
docker run --name todo -p 8000:8000 todo
```

The app will be accessible at http://localhost:8000.

### Running tests

Assumig you have the app up and running as mentioned before, you can run the tests with command:

```bash
docker exec -it todo python3 manage.py test
```

## Usage

Once the app is running, you can access it in your web browser at the specified address. You can then register, create, update, and delete tasks as needed.
