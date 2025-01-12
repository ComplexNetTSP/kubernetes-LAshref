# Use the official Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /challenge3

# Define build argument for app type
ARG APP_TYPE=with_db

# Copy the appropriate myapp.py file based on the APP_TYPE argument
COPY myapp_${APP_TYPE}.py myapp.py

# Copy templates
COPY templates/ ./templates/

# Install dependencies
RUN pip install flask pymongo

# Expose the port Flask will run on
EXPOSE 5000

# Command to run the application
CMD ["python", "myapp.py"]
