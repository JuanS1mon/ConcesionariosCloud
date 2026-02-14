# Diagrama de Flujo: Proceso Completo de Cotización y Venta

## Visión General del Proceso

Este diagrama muestra el flujo completo desde que un cliente solicita una cotización hasta la entrega final del vehículo, incluyendo todos los módulos del sistema que intervienen.

```mermaid
flowchart TD
    %% Clientes y Canales de Entrada
    A[Cliente] --> B{¿Cómo contacta?}
    B -->|Sitio Web| C[Formulario Web]
    B -->|WhatsApp| D[Chat WhatsApp]
    B -->|Llamada| E[Atención Telefónica]
    B -->|Presencial| F[Showroom]

    %% Recepción de Consulta
    C --> G[Recepción de Consulta]
    D --> G
    E --> G
    F --> G

    G --> H{¿Auto específico?}
    H -->|Sí| I[Buscar Auto en Inventario]
    H -->|No| J[Mostrar Catálogo/General]

    %% Búsqueda y Pricing
    I --> K{¿Auto encontrado?}
    K -->|Sí| L[Obtener Datos del Auto]
    K -->|No| M[Buscar en Mercado/Proveedores]

    L --> N[Pricing Engine]
    N --> O[Calcular Precio Sugerido]
    O --> P[Obtener Comparables]
    P --> Q[Simulador de Ventas]
    Q --> R[Estimar Tiempo de Venta]

    %% Generación de Cotización
    O --> S[Generar Cotización]
    R --> S
    M --> S

    S --> T[Crear Registro Cotización]
    T --> U[(Base de Datos<br/>cotizaciones)]

    %% Comunicación con Cliente
    S --> V{¿Canal original?}
    V -->|Web| W[Enviar Email + PDF]
    V -->|WhatsApp| X[Enviar mensaje + PDF]
    V -->|Teléfono| Y[Llamar y explicar]
    V -->|Presencial| Z[Entregar físicamente]

    %% Seguimiento y Negociación
    W --> AA[Cliente Recibe Cotización]
    X --> AA
    Y --> AA
    Z --> AA

    AA --> BB{¿Interesado?}
    BB -->|Sí| CC[Negociación]
    BB -->|No| DD[Fin - No interesado]

    CC --> EE{¿Negociar precio?}
    EE -->|Sí| FF[Simulador Interactivo]
    EE -->|No| GG[Proceder con precio original]

    FF --> HH[Cliente ajusta precio]
    HH --> II[Recalcular tiempo/márgen]
    II --> JJ[Mostrar impacto]
    JJ --> KK{¿Acepta nuevo precio?}
    KK -->|Sí| GG
    KK -->|No| LL[Negociación continúa]

    %% Reserva y Compra
    GG --> MM[Cliente decide comprar]
    MM --> NN{¿Reserva o compra directa?}

    NN -->|Reserva| OO[Crear Reserva]
    OO --> PP[(Base de Datos<br/>reservas)]
    PP --> QQ[Enviar confirmación]
    QQ --> RR[Esperar pago inicial]

    NN -->|Compra Directa| SS[Proceder a venta]

    RR --> TT{Pago realizado?}
    TT -->|Sí| SS
    TT -->|No| UU[Recordatorio pago]

    %% Proceso de Venta
    SS --> VV[Crear Registro Venta]
    VV --> WW[(Base de Datos<br/>ventas)]

    VV --> XX[Generar Documentación]
    XX --> YY[Factura]
    YY --> ZZ[Contrato]
    ZZ --> AAA[Documentos Legales]

    XX --> BBB[Actualizar Inventario]
    BBB --> CCC[Marcar auto como vendido]
    CCC --> DDD[(Base de Datos<br/>autos)]

    %% Entrega
    AAA --> EEE[Coordinar Entrega]
    EEE --> FFF{¿Entrega inmediata?}
    FFF -->|Sí| GGG[Entregar vehículo]
    FFF -->|No| HHH[Agendar fecha entrega]

    HHH --> III[Fecha programada]
    III --> GGG

    GGG --> JJJ[Cliente recibe auto]
    JJJ --> KKK[Actualizar estado venta]
    KKK --> LLL[Completado]

    %% Sistema de Seguimiento
    subgraph "Sistema de Seguimiento"
        MMM[Dashboard Admin]
        MMM --> NNN[Ver todas cotizaciones]
        MMM --> OOO[Ver reservas pendientes]
        MMM --> PPP[Ver ventas completadas]
        MMM --> QQQ[Métricas de conversión]
    end

    %% Integraciones
    subgraph "Integraciones Externas"
        RRR[Cloudinary<br/>Imágenes]
        SSS[WhatsApp API<br/>Mensajes]
        TTT[Email Service<br/>Notificaciones]
        UUU[CRM<br/>Historial cliente]
    end

    %% Conexiones del sistema
    U --> MMM
    PP --> MMM
    WW --> MMM
    DDD --> MMM

    XX --> RRR
    X --> SSS
    W --> TTT
    AA --> UUU
```

## Descripción Detallada del Flujo

### 1. Entrada del Cliente
- **Múltiples canales**: Web, WhatsApp, teléfono, presencial
- **Captura inicial**: Información básica del cliente y auto de interés

### 2. Búsqueda y Pricing
- **Verificación de inventario**: Buscar auto específico solicitado
- **Pricing inteligente**: Si el auto existe, calcular precio sugerido
- **Comparables**: Obtener datos de mercado similares
- **Simulación**: Estimar tiempo de venta y probabilidad

### 3. Generación de Cotización
- **PDF personalizado**: Con precio, características, comparables
- **Múltiples formatos**: Email, WhatsApp, físico
- **Registro en BD**: Historial completo de cotizaciones

### 4. Negociación Interactiva
- **Simulador en tiempo real**: Cliente puede probar diferentes precios
- **Impacto visual**: Ver cómo cambia tiempo de venta y margen
- **Negociación guiada**: Sistema sugiere precios óptimos

### 5. Reserva y Compra
- **Reserva temporal**: Mantener auto apartado
- **Pago inicial**: Confirmación de seriedad del cliente
- **Transición a venta**: Una vez confirmado el pago

### 6. Proceso de Venta
- **Documentación legal**: Facturas, contratos, transferencias
- **Actualización de inventario**: Marcar auto como vendido
- **Coordinación de entrega**: Fecha y logística

### 7. Seguimiento y Analytics
- **Dashboard administrativo**: Visión completa de todas las etapas
- **Métricas de conversión**: De cotización → reserva → venta
- **Historial completo**: Seguimiento de cada lead

## Módulos del Sistema Involucrados

### Backend (FastAPI)
- **API de Autos**: Búsqueda y detalles de inventario
- **API de Pricing**: Análisis inteligente de precios
- **API de Cotizaciones**: Gestión de leads y seguimiento
- **API de Ventas**: Procesamiento de transacciones

### Base de Datos
- **autos**: Inventario disponible
- **clientes**: Información de compradores
- **cotizaciones**: Historial de consultas
- **reservas**: Autos apartados temporalmente
- **ventas**: Transacciones completadas
- **market_listings**: Datos de mercado para pricing

### Frontend (Next.js)
- **Catálogo público**: Búsqueda de autos
- **Formulario de cotización**: Captura de leads
- **Dashboard admin**: Gestión completa del proceso
- **Simulador interactivo**: Negociación en tiempo real

### Servicios Externos
- **Cloudinary**: Gestión de imágenes de autos
- **WhatsApp API**: Comunicación automatizada
- **Email Service**: Notificaciones formales
- **CRM**: Historial completo de interacciones

## Puntos Críticos del Proceso

### Conversiones Clave
1. **Cotización → Reserva**: Tasa objetivo >20%
2. **Reserva → Venta**: Tasa objetivo >80%
3. **Tiempo promedio**: Cotización → venta en <30 días

### Automatización
- **Cotizaciones**: 100% automatizadas con pricing inteligente
- **Seguimiento**: Recordatorios automáticos
- **Documentación**: Generación automática de PDFs

### Métricas de Éxito
- **Tasa de respuesta**: <2 horas a consultas
- **Conversión total**: >15% cotizaciones → ventas
- **Satisfacción**: >4.5/5 en encuestas post-venta

## Casos Especiales

### Auto No Disponible
```
Cliente pide auto X
    ↓
No encontrado en inventario
    ↓
Buscar en proveedores/mercado
    ↓
Generar cotización "bajo pedido"
    ↓
Coordinar importación/compra
```

### Negociación Compleja
```
Cliente quiere precio especial
    ↓
Usar simulador interactivo
    ↓
Mostrar impacto en tiempo de venta
    ↓
Ofrecer alternativas (trade-in, financiamiento)
    ↓
Negociación guiada por sistema
```

### Reserva Expirada
```
Reserva creada
    ↓
Pago no realizado en plazo
    ↓
Sistema envía recordatorios automáticos
    ↓
Después de 7 días: liberar reserva
    ↓
Auto vuelve a disponible
```

Este diagrama representa el flujo completo del sistema de concesionario, desde la primera consulta del cliente hasta la entrega final del vehículo, integrando todos los módulos desarrollados (pricing inteligente, simulador, inventario, etc.).</content>
<parameter name="filePath">c:\Users\PCJuan\Desktop\ConcesionariosCloud\docs\diagrama-flujo-completo.md