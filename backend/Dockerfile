# Use official Python slim image as base
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py ./

# Optionally copy SQL init script (for documentation/reference)
COPY init.sql ./

# Expose port 5000 for Flask app
EXPOSE 5000

# Set environment variable for production-like config
ENV PORT=5000

# Run the Flask app
CMD ["python", "app.py"]

# ---
# FROM: Sets the base image (lightweight Python)
# WORKDIR: Sets working directory in container
# COPY: Copies files into container
# RUN: Installs dependencies
# EXPOSE: Documents port used by app
# ENV: Sets environment variable for port
# CMD: Default command to run app
