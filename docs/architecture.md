# Arquitectura de ConcesionariosCloud

## Visión general
ConcesionariosCloud es una plataforma SaaS en la nube para múltiples concesionarias, donde cada empresa tiene su propio panel, catálogo y clientes de forma aislada. El sistema permite gestión de inventarios, leads y precios inteligentes, con potencial para interconexión entre concesionarias.

## Modelo de Negocio
- **Valor para Clientes**: Las concesionarias usan la plataforma para vender autos, ofrecer financiamiento y ganar comisiones por leads/referrals, maximizando ingresos operativos.
- **Escalabilidad**: Crecer via red de concesionarias interconectadas, permitiendo referrals y comisiones cruzadas.
- **Métricas Clave**: Número de tenants activos, leads generados/mes, tasa de conversión, churn rate.

### Glosario de Términos Clave
- **Referrals**: Recomendaciones entre concesionarias para ganar comisiones por ventas referidas.
- **Tenants**: Clientes individuales (concesionarias) con datos aislados en la plataforma.
- **Leads generados/mes**: Número de prospectos interesados capturados mensualmente.
- **Tasa de conversión**: Porcentaje de leads que se convierten en ventas.
- **Churn rate**: Porcentaje de clientes que abandonan la plataforma en un período.

## Componentes

### Frontend (Next.js)
- Catálogo público con filtros y detalles de autos (SEO friendly).
- Panel admin básico para gestión de autos, cotizaciones, marcas, modelos, estados y configuración de Cloudinary (imágenes).
- Autenticación integrada via login en /admin, conectada al backend JWT.

### Backend (FastAPI)
- API REST con endpoints para CRUD de autos, marcas, modelos, estados, cotizaciones, imágenes y configuración de Cloudinary.
- Autenticación JWT para admins.
- Gestión básica de leads via cotizaciones (sin motor de precios ni analytics implementados aún).

### Base de Datos (PostgreSQL)
- Esquemas para admin, autos, marcas, modelos, estados, cotizaciones, imágenes y configuración de Cloudinary.
- Tenant_id no implementado aún (aislamiento multi-concesionaria pendiente), para multiples concecionarias.
- Sin índices avanzados ni full-text search visibles (planeados para optimización futura).

## Infraestructura
- Railway para despliegue de backend y frontend (fácil pero costoso para escala).
- PostgreSQL administrada en Railway.
- Docker no configurado aún (planeado para entornos reproducibles).
- Nginx no implementado (opcional como reverse proxy en futuras versiones).
- **Futuro**: Migrar a Kubernetes/AWS para multi-tenant, con CDN para imágenes y cache Redis para búsquedas rápidas.

## Diseño SaaS
- Multi-concesionaria planeado con aislamiento lógico (tenant_id pendiente).
- Roles actuales: Solo Admin (Dealer y User pendientes).
- Escalabilidad: Arquitectura modular, preparada para microservicios.
- **Límites por Tenant**: Máximo 1000 autos, 500 leads/mes en plan básico; escalable con upgrades.

## Flujos de Usuario y Casos de Uso
- **Cliente Público**: Busca autos en catálogo → Aplica filtros → Ve detalles → Envía cotización (genera lead).
- **Admin de Concesionaria**: Login → Gestiona inventario → Revisa cotizaciones → Configura precios (futuro) → Recibe notificaciones de leads.
- **Caso de Uso Empresarial**: Lead scoring prioriza cotizaciones altas; interconexión sugiere autos de otras sucursales para cerrar ventas.

## Seguridad y Cumplimiento
- Autenticación JWT con expiración (agregar refresh tokens).
- Encriptación de datos sensibles (ej. info de clientes).
- Cumplimiento: GDPR para datos europeos, auditorías regulares.
- **Futuro**: 2FA, logs de acceso, aislamiento de DB por tenant.

## Estado Actual vs. Futuro
- **Implementado**: Catálogo público, panel admin básico con auth integrada, CRUD completo para entidades principales, auth JWT en backend.
- **Pendiente**: Aislamiento multi-tenant, motor de precios inteligente, lead scoring, analytics, interconexión de inventarios, roles avanzados.
- **Futuro**: Microservicios, full-text search, índices optimizados, integración con WhatsApp/campañas para leads. Prioridad: Implementar tenant_id para onboarding de nuevas concesionarias y generar primeros ingresos.