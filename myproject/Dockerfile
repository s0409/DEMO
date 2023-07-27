# Use the official Python image as the base image
FROM python:3.9

# Set environment variables for Python and Docker
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory in the container
WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the Django project code into the container
COPY . /app/


# Run the Django development server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

