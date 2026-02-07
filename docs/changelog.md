# Changelog

## [Unreleased]
- Mejoras en documentación: Actualización de README, architecture.md e instalacion.md.
- Agregado glosario de términos en architecture.md para claridad en modelo de negocio.

- 539c5a5 - Inicializacion del proyecto, documentacion inicial
- def9914 - Inicializar estructura del proyecto con submodules y documentación
- 3e43686 - Actualizar submodules con implementación de gestión de clientes
- 0886e66 - docs: actualización de documentación con URLs de producción
## [1.0.0] - 2026-01-27
- **Backend (FastAPI)**:
  - Implementación de API REST con endpoints CRUD para autos, marcas, modelos, estados y cotizaciones.
  - Autenticación JWT para admins via endpoint `/auth/login`.
  - Gestión de imágenes con integración a Cloudinary (configuración y subida de imágenes).
  - Middleware CORS habilitado para comunicación con frontend.
  - Esquemas de base de datos con SQLAlchemy y migraciones via Alembic.
  - Modelo de admin para gestión de usuarios.
- **Frontend (Next.js)**:
  - Catálogo público con filtros y detalles de autos.
  - Panel admin con login integrado y gestión básica de entidades.
  - Componentes reutilizables (CarCard, FilterSidebar, etc.).
- **Base de Datos**:
  - PostgreSQL con tablas para admin, autos, marcas, modelos, estados, cotizaciones, imágenes y configuración de Cloudinary.
- **Infraestructura**:
  - Despliegue inicial en Railway.
- Lanzamiento inicial con estructura modular para SaaS multi-concesionaria.
