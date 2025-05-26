# AWS Courses Marketplace

A web application for purchasing AWS certification courses, designed to be deployed on AWS App Runner.

## Features

- Browse AWS certification courses
- View detailed course information
- Add courses to shopping cart
- Checkout process
- Responsive design

## Tech Stack

- Python 3.9
- Flask web framework
- Docker containerization
- AWS App Runner for deployment

## Local Development

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   cd src
   python app.py
   ```
4. Access the application at http://localhost:5000

## Docker Build

Build the Docker image:
```
docker build -t aws-courses-app .
```

Run the container locally:
```
docker run -p 8080:8080 aws-courses-app
```

## Deployment to AWS App Runner

1. Push the Docker image to Amazon ECR
2. Create a new AWS App Runner service using the ECR image
3. Configure the service with appropriate settings
4. Deploy the application

## Environment Variables

- `PORT`: The port the application runs on (default: 8080)
- `SECRET_KEY`: Secret key for session management
- `DEBUG`: Set to 'True' for development mode

## Sample Images

For the demo, you'll need to add course images to the `src/static/images/` directory:
- sa-associate.jpg
- developer.jpg
- sysops.jpg
- sa-pro.jpg
- devops.jpg
- about-us.jpg
- hero-bg.jpg