# Use the official Python image as the base image
FROM python:3.8.5-slim-buster

# Set the working directory to /backend
WORKDIR /backend

# Copy the project files to the container
COPY ./requirements.txt /backend/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt

# Copy the project files to the container
COPY ./app /backend/app

# Copy the project files to the container
COPY .env /backend/.env

# Start the application
CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]