#!/bin/bash


# Build da Imagen
docker build --no-cache -t sonarlab:1.0 .

# Rodando a stack
docker-compose up -d 

# Listar a Stack
docker-compose ps 