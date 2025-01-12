# Use the official Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application files into the container
COPY myapp.py .

# Install dependencies
RUN pip install flask

# Expose the port Flask will run on
EXPOSE 5000

# Command to run the application
CMD ["python", "myapp.py"]
