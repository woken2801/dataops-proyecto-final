# Proyecto Final DataOps

## Flujo Implementado

GitHub -> Jenkins -> Docker -> Python -> Excel

## Tecnologías

- Jenkins
- Docker
- Python
- PostgreSQL
- Pandas

## Ejecutar localmente

### Build Docker

docker build -t dataops-app .

### Run Container

docker run --rm -v $(pwd)/output:/app/output dataops-app

## Resultado

Se genera:

output/comisiones.xlsx
prueba
