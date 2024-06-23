# Use the official Python 3.10 image as a base
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file into the working directory
COPY requirements.txt .

# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire current directory into the working directory of the container
COPY . .

# Expose port 8000 to allow access to the API
EXPOSE 8000

# Default command to run the Uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]