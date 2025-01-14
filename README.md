# Projects-from-Simplon-Lyon
## Docker et Docker-Compose : Création d’une chaîne complète de données
### Partie 1 : Découverte de Docker (Création d’une image Docker basique)
### Partie 2 : Découverte de Docker-Compose (Architecture multi-conteneurs)
### Partie 3 : Projet final (Chaîne complète de traitement de données)



Setting up Docker for MongoDB, Flask, and Streamlit
I started by configuring a docker-compose.yml file to orchestrate MongoDB, Flask, and Streamlit in separate containers. Initially, I had some issues with the services communicating with each other, particularly Flask not connecting to MongoDB.
I ensured:
MongoDB was properly running in its container.
Flask and Streamlit could connect to MongoDB via the Docker network.
I set the MONGO_URI environment variable in Flask to point to the MongoDB service by its Docker service name (mongodb) instead of localhost.


Loading JSON Data into MongoDB
After setting up MongoDB, I needed to import a JSON file (listing_sql.json) into the database. To do this, I:

Copied the JSON file from my local machine into the MongoDB container:

## docker cp /path/to/listing_sql.json mongodb:/listing_sql.json
Imported the file into the db_listing database and listing_sql collection using mongoimport:

## mongoimport --db db_listing --collection listing_sql --file listing_sql.json --jsonArray
After importing, I confirmed that the data was successfully loaded using both mongosh and MongoDB Compass.

Debugging Flask and Streamlit
Flask:

I verified Flask was running and accessible at http://localhost:5000.
Fixed errors related to database queries by ensuring Flask connected properly to MongoDB and that the queries were structured correctly.
Streamlit:
I confirmed Streamlit was pulling data from MongoDB and displaying it on its interface.
Streamlit is now accessible at http://localhost:8501 and visualizes the MongoDB data as expected.
Ensuring Data Persistence Across Container Restarts
I was concerned that the data in MongoDB would be lost if the containers were stopped. I verified that the MongoDB volume (mongodb_data) was correctly set up in docker-compose.yml. This ensures the data persists across container restarts.


Stopping the containers doesn’t delete the data since it’s stored in the Docker volume.
The volume automatically reconnects to MongoDB when the containers are restarted.
Managing Docker Images
I reviewed my Docker images and asked what would happen if I deleted them. I learned:
Deleting images would require rebuilding them with docker-compose build.
The MongoDB data is safe because it’s stored in the volume, even if I delete and rebuild the MongoDB image.
Also another small pro  installing docker image of Jupyter notebook with all requirements and needed data
1. Processing CSV Files
I worked with three CSV files (ventes.csv, clients.csv, produits.csv) using Python and libraries like pandas. I transformed and cleaned the data, preparing it for storage in MongoDB.
2. Dockerizing the ETL Process
I created a Dockerfile to run the ETL script and everything goes well
Configured Python as the base image and installed dependencies (pandas, pymongo).
Packaged the ETL script and CSV files into the Docker container



Part 1: Discovering Docker (Building a Basic Docker Image)
1. Steps to Build a Docker Image from a Dockerfile

Write a Dockerfile: Create a file named Dockerfile and specify instructions to build your image.
Define the Base Image: Use the FROM instruction to specify the base image.
Add Application Files: Use COPY or ADD instructions to include files from your local directory into the image.
Set Working Directory: Use WORKDIR to set the directory in the container where commands will be executed.
Install Dependencies: Use RUN to execute shell commands to install required dependencies or configure the environment.
Specify the Entrypoint: Use CMD or ENTRYPOINT to define the default command that runs when a container starts.
Build the Image: Use the docker build command to create the image from the Dockerfile.

2. Role of the docker build Command
The docker build command processes the instructions in the Dockerfile to create a Docker image.
Syntax Example:
##### docker build -t my_image_name:latest .
-t tags the image with a name and optionally a version.
. specifies the build context (directory containing the Dockerfile).
3. Differences Between FROM, WORKDIR, and CMD in a Dockerfile

FROM: Specifies the base image to use (e.g., FROM python:3.10).
WORKDIR: Sets the working directory inside the container where subsequent instructions (like RUN or CMD) will execute.
CMD: Specifies the default command to run when the container starts (e.g., CMD ["python", "app.py"]).
4. Importance of Specifying a Base Image in the Dockerfile

A base image serves as the foundation of your container, providing a pre-configured environment (e.g., a specific OS or runtime) to simplify application deployment.
5. Running a Container Based on the Image

Use the docker run command:
#### docker run -d --name my_container -p 5000:5000 my_image_name
-d runs the container in detached mode.
--name assigns a name to the container.
-p maps a host port to the container port.
6. Reflecting Changes in the Source Code

If the source file (e.g., a Python script) is modified:
Rebuild the image:
#### docker build -t my_image_name:latest .
Stop and remove the old container:
#docker stop my_container && docker rm my_container
Start a new container with the updated image.




Docker-Compose is a tool designed to simplify the management of multi-container applications. When an application requires multiple services, such as a database, a web server, and an API, Docker-Compose provides a single configuration file (docker-compose.yml) to define and orchestrate all these services. Here's a deeper explanation of its key aspects:

1. What Does Docker-Compose Do?
Docker-Compose allows you to:

Define Services: In a single file, you describe all the containers your application needs, including their images, configurations, environment variables, and volumes.
Manage Dependencies: Specify the relationships between services. 

For example, you can declare that your API should wait for the database to start before running.
Automate Networking: 
Compose automatically creates a shared network so that containers can communicate using simple service names instead of IP addresses.
Simplify Deployment: 
A single command (docker-compose up) can bring up the entire application stack, making it easy to replicate the environment on any machine.

2. Key Features of Docker-Compose
Centralized Configuration: All services and their dependencies are declared in a human-readable YAML file.
Consistency Across Environments:
 The same docker-compose.yml file works in development, testing, and production with minimal adjustments.
Service Isolation:
Each container runs independently but can communicate with others as needed, ensuring modularity.
Volume Management:
Compose makes it easy to persist data across container restarts or updates, essential for databases like PostgreSQL.
Scaling:
You can scale specific services up or down with a simple command, such as running multiple instances of your API for better performance.
4. Why Use Docker-Compose Instead of Running Containers Manually?
Ease of Use:
Instead of writing and managing multiple docker run commands with complex options, you define everything once in a docker-compose.yml file.
Automation: 
Start, stop, or rebuild all containers with single commands like docker-compose up or docker-compose down.
Service Dependencies:
Compose understands the relationships between services, ensuring they start in the correct order. For example, your API won’t start until the database is ready.
Collaboration: 
Sharing the docker-compose.yml file allows teams to work in identical environments without worrying about individual setups.
6. How Does Docker-Compose Improve Multi-Container Applications?
Imagine an application that requires:

A SQL database to store data.
A Flask API to handle requests and interact with the database.
A React frontend to provide a user interface.
Using Docker-Compose:

You define all three services in a single file, including their configurations, ports, and shared networks.
You can start the entire application stack with one command, and Docker-Compose will ensure that:
The database starts first.
