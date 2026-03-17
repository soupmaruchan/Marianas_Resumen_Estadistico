# Reporte de Analisis - Campañas de Creatividad Digital

## 1. Descripcion del dataset

El dataset analizado contiene información de campañas de publicidad digital ejecutadas en diversas plataformas sociales. Cada registro corresponde a una campaña específica e incluye métricas clave de desempeño como impresiones, clics, conversiones, costo publicitario e ingresos generados.

El dataset principal contiene aproximadamente 180 campañas con múltiples variables tanto numéricas como categóricas. Entre las columnas más relevantes se encuentran:

- plataforma
- formato de contenido
- país de la campaña
- impresiones
- clicks
- conversiones
- costo_usd
- ingresos_usd
- fecha de ejecución

A partir de estas variables se calcularon indicadores derivados fundamentales en marketing digital:

- CTR (Click Through Rate)
- CVR (Conversion Rate)
- CPC (Costo por click)
- CPM (Costo por mil impresiones)
- ROI (Return on Investment)

Estos indicadores permiten evaluar la eficiencia de las campañas y comparar su desempeño entre plataformas, formatos y segmentos de clientes.

# 2. Hallazgos de tendencia central

El análisis de tendencia central permitió identificar los valores típicos de las principales métricas del dataset.

La media y mediana de las variables clave muestran que la mayoría de las campañas generan retornos positivos, aunque existe una variabilidad considerable entre ellas.

Entre los principales hallazgos se observa que:

- El CTR promedio se encuentra alrededor de valores cercanos al 1–2%, lo cual es consistente con campañas digitales en redes sociales.
- El ROI promedio indica que en general las campañas logran recuperar su inversión y generar beneficios adicionales.
- El costo por clic (CPC) y el costo por mil impresiones (CPM) presentan valores relativamente estables entre campañas.

La comparación entre media y mediana muestra ligeras diferencias en algunas métricas, lo cual sugiere la presencia de valores extremos que pueden afectar el promedio.

# 3. Hallazgos de dispersión

El análisis de dispersión permitió evaluar qué tan variable es el comportamiento de las campañas.

Se calcularon las siguientes métricas:

- desviación estándar
- varianza
- rango
- rango intercuartílico (IQR)

La variable con mayor variabilidad relativa es el ROI. Esto es esperado en campañas de marketing digital debido a que pequeñas variaciones en conversiones o ingresos pueden generar cambios significativos en el retorno de inversión.

Las métricas de impresiones y clics también presentan dispersión considerable, lo cual refleja la diversidad de escalas de campañas presentes en el dataset.

Este comportamiento sugiere que algunas campañas tienen un desempeño excepcionalmente alto mientras que otras tienen resultados moderados o negativos.

# 4. Outliers identificados

Se aplicó el método del rango intercuartílico (IQR) para identificar valores atípicos en dos métricas clave:

## Outliers en CTR

Se identificaron aproximadamente 3 campañas con CTR fuera de los límites esperados.

Estos valores corresponden a campañas con tasas de clic significativamente superiores al promedio, lo cual puede indicar:

- contenido altamente atractivo
- segmentación efectiva
- formatos con mayor interacción

Las plataformas que aparecen con mayor frecuencia entre estos outliers incluyen Instagram y TikTok.

## Outliers en ROI

Se detectaron alrededor de 12 campañas con ROI fuera del rango esperado.

Estos outliers corresponden principalmente a campañas con retornos extremadamente altos o extremadamente bajos.

Las campañas con ROI muy alto pueden representar casos de éxito donde la inversión publicitaria fue altamente eficiente.

# 5. Análisis posterior al merge con clientes

Para enriquecer el análisis se integró información adicional de clientes utilizando operaciones de merge entre el dataset de campañas y una tabla de clientes.

Esta tabla incluye información como:

- industria del cliente
- tamaño de la empresa
- nivel de contrato
- país de origen
- porcentaje de descuento

## ROI promedio por industria

El análisis agrupado por industria muestra que el sector **Retail** presenta el mayor ROI promedio entre las campañas analizadas.

Esto sugiere que las campañas de comercio y ventas directas tienden a convertir mejor el tráfico publicitario en ingresos.

## CTR promedio por nivel de contrato

Al analizar el CTR promedio por nivel de contrato se observa que los clientes con contrato **Enterprise** presentan el mayor CTR.

Esto puede explicarse por:

- mayor inversión en creatividad
- estrategias de segmentación más avanzadas
- campañas con mayor optimización.

## Campañas de empresas grandes

Entre las campañas pertenecientes a empresas clasificadas como **Grande**, aproximadamente el 63.8% presentan ROI positivo.

Esto indica que la mayoría de las campañas ejecutadas por empresas grandes logran generar beneficios sobre la inversión publicitaria.

# 6. Insights accionables para el equipo de marketing

A partir del análisis realizado se identifican tres insights principales:

### Insight 1 — Los formatos tipo Reel generan mayor interacción

El análisis de CTR promedio por formato muestra que los **Reels** presentan la tasa de clics más alta. Esto sugiere que los contenidos de video corto tienen mayor capacidad de captar la atención de los usuarios.

### Insight 2 — Instagram y TikTok concentran campañas de alto rendimiento

Las campañas con mejor desempeño en términos de ROI se encuentran mayoritariamente en plataformas visuales como Instagram y TikTok.

Esto indica que estas plataformas pueden ser particularmente efectivas para campañas orientadas a conversión.

### Insight 3 — Las empresas grandes mantienen mayor consistencia en ROI positivo

Más del 60% de las campañas de empresas grandes generan retorno positivo, lo cual sugiere que la experiencia, inversión y optimización continua influyen en el desempeño.

# 7. Recomendaciones estratégicas

A partir de los hallazgos del análisis se proponen las siguientes recomendaciones:

### Recomendación 1 — Priorizar formatos de video corto

Las campañas futuras deberían priorizar formatos como reels o contenido dinámico, ya que estos formatos presentan mayores tasas de interacción.

### Recomendación 2 — Optimizar campañas en plataformas de alto engagement

Instagram y TikTok muestran un desempeño superior en métricas clave, por lo que se recomienda concentrar mayor inversión en estas plataformas cuando el objetivo sea aumentar conversiones.