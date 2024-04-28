# Todo App

This is a simple todo app built with Django.

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
docker run -p 8000:8000 todo
```

The app will be accessible at http://localhost:8000.

## Usage

Once the app is running, you can access it in your web browser at the specified address. You can then register, create, update, and delete tasks as needed.
