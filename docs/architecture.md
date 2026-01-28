# Arquitectura de ConcesionariosCloud

## Visión general
ConcesionariosCloud es una plataforma en la nube para múltiples concesionarias, donde cada empresa tiene su propio panel, catálogo y clientes de forma aislada.

## Componentes

### Frontend (Next.js)
- Catálogo público SEO friendly
- Panel concesionario (dashboard)
- Autenticación y roles

### Backend (FastAPI)
- API REST
- Autenticación JWT
- Gestión de autos, concesionarias y leads
- Motor de reglas de precios
- Servicios de analytics

### Base de Datos (PostgreSQL)
- Esquema multi-concesionaria (tenant_id)
- Índices para búsqueda rápida
- Full-text search en catálogos

## Infraestructura
- Docker para entornos reproducibles
- Railway para despliegue
- Nginx como reverse proxy

## Diseño SaaS
- Multi-concesionaria con aislamiento lógico
- Roles: Admin, Dealer, User
- Escalable a microservicios en futuras versiones
