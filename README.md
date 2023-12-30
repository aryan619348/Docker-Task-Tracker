# Task-Tracker Project
This project is a simple Task Tracker application built to demonstrate the usage of Docker volumes.

### Deployed to Azure at : https://task-tracker.azurewebsites.net/


## Docker Image
The Docker image for this application is hosted on Docker Hub with the name aryanspillai/task-tracker. You can find it [here](https://hub.docker.com/repository/docker/aryanspillai/task-tracker/).


## Run Locally
To run the application using Docker Compose, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/aryan619348/docker-exploration.git

2. Change into the project directory:

    ```bash
    cd docker-exploration

3. Run the application using Docker Compose:

    ```bash
    docker-compose up -d

This command will start the application in detached mode, and you can access it in your web browser at http://localhost:8000.


To stop the application, use the following command:
    ```bash
    docker-compose down



