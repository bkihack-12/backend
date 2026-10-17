# backend
backend
POST /api/auth/register
POST /api/auth/login
GET  /api/auth/me
POST /api/auth/logout
REGISTER
curl -X POST http://localhost:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Jan Kowalski",
    "email": "jan@example.com",
    "password": "secret123"
  }'
LOGIN
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "jan@example.com",
    "password": "secret123"
  }'

USE RETURNED TOKEN
curl http://localhost:5000/api/auth/me \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"