version: '2'
services:
  web:
    build: .
    ports:
      - "5000:5000"
  redis:
    image: redis:bitnami
