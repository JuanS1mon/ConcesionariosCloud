# ConcesionariosCloud

Plataforma SaaS para concesionarias con catálogo online, gestión de clientes, calificación automática de leads y motor de precios inteligente.

## Stack
- Backend: FastAPI (Python)
- Frontend: Next.js (React)
- Database: PostgreSQL
- Infraestructura: Docker, Railway

## Componentes
- `backend/`: API y lógica de negocio
- `frontend/`: aplicación web pública y panel concesionario
- `docs/`: arquitectura, roadmap, métricas y guía de instalación
- `tools/`: scripts de automatización

## Instalación y Uso
Ver [docs/instalacion.md](docs/instalacion.md) para instrucciones detalladas de instalación, configuración, uso y documentación de API/endpoints.

## Objetivo
Construir una plataforma comercial real y documentar públicamente decisiones técnicas, arquitectura y métricas de performance.

## Características Principales
### Gestión de Leads
La plataforma captura, centraliza y organiza todos los interesados en vehículos (formularios, WhatsApp, campañas), permitiendo seguimiento automático y conversión a ventas.

### Lead Scoring
El sistema asigna un puntaje a cada lead según su probabilidad de compra, priorizando automáticamente a los clientes con mayor intención.

### Intelligent Pricing
El sistema permite definir precios dinámicos según demanda, stock, margen objetivo y datos históricos, evitando pérdidas por sub o sobreprecio.

### Interconexión de Inventarios
El sistema permite interconectar inventarios entre concesionarias en la red, sugiriendo al vendedor autos disponibles en otras sucursales cuando un cliente busca un vehículo no disponible localmente.

## Roadmap (alto nivel)
- ✅ MVP catálogo de autos (implementado)
- ✅ Panel concesionario básico (implementado con auth integrada)
- Gestión de leads (cotizaciones básicas implementadas, leads pendientes)
- Motor de precios inteligente (pendiente)
- Analytics y métricas (básico en docs, implementación pendiente)
- Escalabilidad y monetización (pendiente)

## Deploy
- Backend y frontend desplegados en Railway.
- Base de datos PostgreSQL administrada.
- Ver `docs/DEPLOYMENT_GUIDE.md` para detalles de despliegue.

## Status
Desarrollo activo con actualizaciones semanales. Algunas funcionalidades (como motor de precios o analytics completos) están planificadas pero no implementadas aún.


## Licencia
[MIT](LICENSE).


## Contacto
- Repo: [GitHub](https://github.com/JuanS1mon/ConcesionariosCloud)
- Issues: Abre un issue para reportes o sugerencias.