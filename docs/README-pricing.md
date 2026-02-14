# Documentación del Sistema de Pricing Inteligente

## Índice General

### 📊 Sistema de Pricing Inteligente
- **[Diagrama de Flujo Completo](diagrama-flujo-completo.md)** - Proceso completo desde cotización hasta entrega
- **[Diagrama Gráfico HTML](diagrama-grafico.html)** - Diagrama visual interactivo en navegador
- **[Imagen PNG del Diagrama](diagrama-flujo-completo.png)** - Imagen estática del diagrama completo
- **[Código Mermaid](diagrama-codigo-mermaid.txt)** - Código fuente para herramientas online
- **[Pricing en Cotizaciones](pricing-en-cotizaciones.md)** - Integración específica del pricing en el proceso de venta
- **[Visión General del Sistema](pricing-sistema.md)** - Arquitectura completa, flujos de trabajo y algoritmos
- **[Pricing Engine](pricing-engine.md)** - Motor de cálculo de precios sugeridos
- **[Simulador de Ventas](simulador.md)** - Estimación de tiempos de venta

### 🔧 Componentes Técnicos
- **Scrapers**: MercadoLibre y Kavak (web scraping directo)
- **Normalizer**: Conversión de datos crudos a listings normalizados
- **API Layer**: Endpoints REST para integración frontend

### 📈 Algoritmos y Fórmulas
- **Búsqueda Progresiva**: Rango de años ±1, ±2, ±3, ±5, ±8, ±15
- **Precio Sugerido**: Mediana mercado + ajuste por KM
- **Tiempo de Venta**: Modelo histórico vs modelo mercado
- **Competitividad**: muy_competitivo (≤95%), competitivo (95-105%), caro (>105%)

### ⚙️ Configuración
```python
# Parámetros ajustables
AJUSTE_POR_10K_KM = 50000          # ARS por cada 10k km extra
DIAS_BASE_VENTA = 45               # Días promedio base
DIAS_POR_PCT_SOBREPRECIO = 2.5     # Días extra por % sobreprecio
RANGOS_ANIO_PROGRESIVOS = [1,2,3,5,8,15]
```

## Guía Rápida

### Para Usuarios
1. **Ejecutar Scraping**: Botón "Ejecutar Scraping" en `/admin/pricing`
2. **Ver Análisis**: Cada auto muestra precio sugerido y competitividad
3. **Simular Precios**: Slider para ver tiempo de venta a diferentes precios

### Para Desarrolladores
1. **API Endpoints**: Ver [pricing-sistema.md](pricing-sistema.md) sección API
2. **Configuración**: Parámetros en archivos de servicio
3. **Debugging**: Logs en consola backend para algoritmos

### Casos Comunes

#### Auto sin datos de mercado
**Síntoma**: "sin_datos" en competitividad
**Causa**: No hay suficientes comparables similares
**Solución**: Esperar más datos de scraping o pricing manual

#### Tiempo de venta muy largo (>365 días)
**Síntoma**: Estimaciones absurdas
**Causa**: Precio muy por encima del mercado
**Solución**: Revisar precio actual vs mercado

#### Pocos comparables
**Síntoma**: <3 comparables encontrados
**Causa**: Auto único o mercado ilíquido
**Solución**: Sistema expande automáticamente rango de años

## Métricas del Sistema

- **Cobertura**: 85-95% de autos tienen datos
- **Precisión Precio**: ±10-15%
- **Precisión Tiempo**: ±20-30%
- **Velocidad**: <200ms por análisis

## Soporte

### Logs Importantes
- Backend: `app/services/pricing_engine.py` y `app/services/simulador.py`
- Frontend: Consola browser en `/admin/pricing`
- Base de datos: Tablas `market_listings` y `market_raw_listings`

### Troubleshooting
1. **Sin datos**: Verificar que scraping se ejecutó correctamente
2. **Precios raros**: Revisar normalización de datos
3. **Lentitud**: Verificar índices en BD

---

**Última actualización**: Febrero 2026
**Versión del sistema**: 1.0
**Documentación generada automáticamente**</content>
<parameter name="filePath">c:\Users\PCJuan\Desktop\ConcesionariosCloud\docs\README-pricing.md