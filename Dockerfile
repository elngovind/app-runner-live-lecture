FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

# Create directories for static files if they don't exist
RUN mkdir -p static/images

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8080

# Expose the port the app runs on
EXPOSE 8080

# Command to run the application
CMD gunicorn --bind 0.0.0.0:$PORT app:app