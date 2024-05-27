# Use an official Python runtime as a parent image
FROM python:3.10

# Install dependencies
COPY requirements.txt /app/
WORKDIR /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY schedule /app/

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]