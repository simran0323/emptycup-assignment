# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend files
COPY . .

# Initialize the database
# RUN python database.py

# Expose the port Flask will run on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]