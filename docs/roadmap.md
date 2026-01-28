# Roadmap ConcesionariosCloud

## Estado Actual (Enero 2026)
- ✅ MVP básico completado: CRUD autos, catálogo público, auth JWT.
- ✅ Panel admin con gestión de entidades (autos, cotizaciones, etc.).
- Pendiente: Aislamiento multi-tenant, motor de precios, analytics.

## Fase 1 - MVP (Completado)
- ✅ CRUD completo para autos, marcas, modelos, estados.
- ✅ Catálogo público con filtros y detalles (SEO friendly).
- ✅ Autenticación básica JWT para admins.
- ✅ Gestión básica de leads via cotizaciones.
- ✅ Integración con Cloudinary para imágenes.

## Fase 2 - Producto SaaS (En Progreso)
- Implementar tenant_id para aislamiento multi-concesionaria (prioridad alta para onboarding).
- Expandir panel dealer con roles avanzados (Dealer, User).
- Mejorar gestión de leads con scoring básico.
- Agregar notificaciones para leads (email/WhatsApp).

## Fase 3 - Inteligencia Comercial (Pendiente)
- Lead scoring automático basado en datos de cotizaciones.
- Motor de precios inteligente con reglas dinámicas (demanda, stock, márgenes).
- Recomendador de autos con interconexión de inventarios entre concesionarias.
- Analytics básicos: dashboards de ventas, conversión y rendimiento.

## Fase 4 - Escalabilidad (Futuro)
- Migrar a Kubernetes/AWS para multi-tenant.
- Implementar Redis para cache de búsquedas y sesiones.
- Observabilidad: Logs, métricas y monitoreo (ej. Prometheus).
- Optimización DB: Índices, full-text search, particionamiento por tenant.

## Fase 5 - Monetización (Futuro)
- Planes SaaS: Básico (500 leads/mes), Pro (1000 autos), Enterprise (ilimitado).
- Sistema de billing con Stripe/PayPal.
- Feature flags para A/B testing y upgrades.
- API para integraciones externas (ej. financiamiento, CRM).
