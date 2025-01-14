# Projects-from-Simplon-Lyon
## Docker et Docker-Compose : Création d’une chaîne complète de données
### Partie 1 : Découverte de Docker (Création d’une image Docker basique)
### Partie 2 : Découverte de Docker-Compose (Architecture multi-conteneurs)
### Partie 3 : Projet final (Chaîne complète de traitement de données)



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
# docker build -t my_image_name:latest .
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
# docker run -d --name my_container -p 5000:5000 my_image_name
-d runs the container in detached mode.
--name assigns a name to the container.
-p maps a host port to the container port.
6. Reflecting Changes in the Source Code

If the source file (e.g., a Python script) is modified:
Rebuild the image:
# docker build -t my_image_name:latest .
Stop and remove the old container:
#docker stop my_container && docker rm my_container
Start a new container with the updated image.
