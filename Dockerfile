# Use the official Python 3.12.1 image
FROM python:3.12.1

# Set environment variables to configure tzdata non-interactively
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC

# Update and install dependencies
RUN apt-get update && apt-get install -y \
    espeak \
    python3-tk \
    default-jre \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip to the latest version
RUN python3 -m pip install --upgrade pip

# Install Cython
RUN pip install cython

# Verify the installation of espeak, java, and Python
RUN espeak --version && \
    java -version && \
    python3 --version

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy all Python scripts into the container
COPY . /app

# Set the default entrypoint to Python
ENTRYPOINT ["python3"]

