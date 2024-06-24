# Use the official Python 3.10 image as a base
FROM public.ecr.aws/lambda/python:3.10-x86_64

# Copy the requirements.txt file into the working directory
COPY requirements.txt .

# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire current directory into the working directory of the container
COPY . .

# Default command to run the Uvicorn server
CMD ["main.handler"]