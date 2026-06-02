Веб-приложение на Python, развёрнутое в Docker с Nginx в качестве reverse_proxy.

## Стек

- **Python 3.9** 
- **Nginx 1.26.3** 
- **Docker + Docker Compose** 

## Архитектура

![img](https://github.com/Daniil745/python-nginx/blob/3a20be0238976a52bf3e34371038f4a3daef35e5/img/nginx-backend.jpg)

- **Nginx** принимает запросы на порту 80, проксирует на backend
- **Backend** слушает порт 8080 внутри сети `app-network`, с хоста недоступен
- Приложение запускается от непривилегированного пользователя `appuser`
  
## Запуск

```bash
# 1. Клонировать репозиторий
git clone https://github.com/Daniil745/python-nginx
cd python-nginx

# 2. Запустить сервисы
docker-compose up -d --build

# 3. Проверить, что оба контейнера запущены
docker-compose ps
```

## Проверка работоспособности

```bash
# Успешный запрос
curl http://localhost/

# Запрос несуществующего пути (ошибка 404)
curl http://localhost/anything

# Backend НЕ доступен с хоста напрямую (Connection refused)
curl http://localhost:8080/
```

![img](https://github.com/Daniil745/python-nginx/blob/ea3112f6f14c724efd27a7db6f0d68870f13b12d/img/screen1.png)
![img](https://github.com/Daniil745/python-nginx/blob/ea3112f6f14c724efd27a7db6f0d68870f13b12d/img/screen2.png)
![img](https://github.com/Daniil745/python-nginx/blob/ea3112f6f14c724efd27a7db6f0d68870f13b12d/img/screen3.png)
![img](https://github.com/Daniil745/python-nginx/blob/ea3112f6f14c724efd27a7db6f0d68870f13b12d/img/screen4.png)
![img](https://github.com/Daniil745/python-nginx/blob/ea3112f6f14c724efd27a7db6f0d68870f13b12d/img/screen5.png)
![img](https://github.com/Daniil745/python-nginx/blob/ea3112f6f14c724efd27a7db6f0d68870f13b12d/img/screen6.png)

## Остановка

```bash
docker-compose down
```
