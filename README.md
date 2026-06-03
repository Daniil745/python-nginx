# Python Web Application with Docker and Nginx Reverse Proxy

## Tech Stack

- **Python 3.9**
- **Nginx 1.26.3**
- **Docker + Docker Compose**

## Architecture

![Architecture Diagram](https://github.com/Daniil745/python-nginx/blob/3a20be0238976a52bf3e34371038f4a3daef35e5/img/nginx-backend.jpg)

- **Nginx** listens on port 80 and proxies requests to the backend
- **Backend** listens on port 8080 inside the `app-network` and is not accessible from the host
- The application runs as a non-privileged user `appuser`

## Running the Application

```bash
# 1. Clone the repository
git clone https://github.com/Daniil745/python-nginx
cd python-nginx

# 2. Start the services
docker-compose up -d --build

# 3. Verify both containers are running
docker-compose ps
```

## Testing

```bash
# Successful request
curl http://localhost/

# Non-existent endpoint (404 error)
curl http://localhost/anything

# Backend is not accessible directly from host (Connection refused)
curl http://localhost:8080/
```

## Screenshots

![Screenshot 1](https://github.com/Daniil745/python-nginx/blob/ea3112f6f14c724efd27a7db6f0d68870f13b12d/img/screen1.png)
![Screenshot 2](https://github.com/Daniil745/python-nginx/blob/ea3112f6f14c724efd27a7db6f0d68870f13b12d/img/screen2.png)
![Screenshot 3](https://github.com/Daniil745/python-nginx/blob/ea3112f6f14c724efd27a7db6f0d68870f13b12d/img/screen3.png)
![Screenshot 4](https://github.com/Daniil745/python-nginx/blob/ea3112f6f14c724efd27a7db6f0d68870f13b12d/img/screen4.png)
![Screenshot 5](https://github.com/Daniil745/python-nginx/blob/ea3112f6f14c724efd27a7db6f0d68870f13b12d/img/screen5.png)
![Screenshot 6](https://github.com/Daniil745/python-nginx/blob/ea3112f6f14c724efd27a7db6f0d68870f13b12d/img/screen6.png)

## Stopping the Application

```bash
docker-compose down
```
