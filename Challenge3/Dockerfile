# Use the official Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /challenge3

# Copy the application files into the container
COPY myapp.py .
COPY templates/ ./templates/

# Install dependencies
RUN pip install flask pymongo

# Expose the port Flask will run on
EXPOSE 5000

# Command to run the application
CMD ["python", "myapp.py"]
