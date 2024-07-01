# Use an official Ubuntu as a parent image
FROM ubuntu:22.04

# Set environment variables to configure tzdata non-interactively
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC

# Update and install dependencies
RUN apt-get update && apt-get install -y \
    espeak=1.48.15+dfsg-3 \
    python3-tk=3.10.8-1~22.04 \
    default-jre=2:1.11-72build2 \
    python3-pip \
    build-essential \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install cython using pip
RUN pip install cython

# Verify the installation of espeak and java
RUN espeak --version && \
    java -version

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the start script into the container
COPY start_script.sh /app
RUN chmod +x /app/start_script.sh

# Define the entrypoint command
ENTRYPOINT ["/app/start_script.sh"]

