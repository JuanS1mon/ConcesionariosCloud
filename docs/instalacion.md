# Instalación y Configuración

## Prerrequisitos
- Python 3.8+ (para backend)
- Node.js 18+ (para frontend)
- PostgreSQL (local o en la nube)
- Docker (opcional para entornos reproducibles)

## Backend
1. Clona el repo y entra en `backend/`.
2. Crea un entorno virtual: `python -m venv venv` y actívalo (`venv\Scripts\activate` en Windows).
3. Instala dependencias: `pip install -r requirements.txt`.
4. Configura la DB en `backend/app/config.py` (variables de entorno para PostgreSQL).
5. Ejecuta migraciones: `alembic upgrade head`.
6. Crea un admin inicial: `python app/utils/create_admin.py`.
7. Ejecuta el servidor: `python run_server.py` (corre en http://localhost:8000).

## Frontend
1. Entra en `frontend/`.
2. Instala dependencias: `npm install`.
3. Configura la API base en `frontend/src/lib/api.ts` (apunta a http://localhost:8000 por defecto).
4. Ejecuta en desarrollo: `npm run dev` (corre en http://localhost:3000).

## Configuración de Cloudinary
Para subir y gestionar imágenes, configura Cloudinary:
1. Crea una cuenta en [Cloudinary](https://cloudinary.com/).
2. Obtén tu `cloud_name`, `api_key`, `api_secret` y crea un `upload_preset` en el dashboard.
3. Configura via API: Usa `POST /configuracion-cloudinary` con las credenciales (requiere auth de admin).
4. Alternativamente, inserta directamente en la DB PostgreSQL en la tabla `configuracion_cloudinary`.

## Docker (opcional)
- Para backend: `docker build -t backend .` en `backend/`.
- Para frontend: `docker build -t frontend .` en `frontend/`.
- Usa `docker-compose` si tienes un archivo (no visible en el repo actual).

## Uso
- **Catálogo público**: Visita [https://concesionarios.cloud/](https://concesionarios.cloud/) para ver autos con filtros.
- **Panel admin**: Accede a https://concesionarios.cloud/admin (requiere auth, implementada en backend pero no integrada en frontend aún).
- **API**: Documentación automática en https://concesionarios.cloud/docs (Swagger UI).

## API Endpoints Principales
Basado en FastAPI. Todos los endpoints requieren auth JWT para operaciones de escritura (excepto login).

- **Auth**: `POST /auth/login` - Login de admin.
- **Autos**: `GET /autos` (lista), `POST /autos` (crear), `PUT /autos/{id}` (actualizar), `DELETE /autos/{id}` (eliminar).
- **Marcas/Modelos/Estados**: CRUD similar en `/marcas`, `/modelos`, `/estados`.
- **Cotizaciones**: `GET /cotizaciones`, `POST /cotizaciones` (crear cotización).
- **Imágenes/Configuración Cloudinary**: Endpoints para subir y gestionar imágenes.

Nota: Algunos modelos (presupuesto, solicitud_venta) existen en DB pero no están expuestos en la API aún.

## Páginas del Frontend
- **Pública**: Página principal con catálogo de autos, filtros laterales y detalles modales.
- **Admin**: Dashboard básico y secciones para gestionar autos, cotizaciones, marcas, modelos, estados y configuración de Cloudinary.