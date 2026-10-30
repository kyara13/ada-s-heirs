# Plan de puesta en producción

## Usuarios y caso de uso

| Usuario | Para qué lo usaría | Qué vería |
|---|---|---|
| Filmotecas y archivos | Analizar la representación en sus fondos por época | Informe agregado por década y género |
| Festivales y premios de cine | Ofrecer un indicador de representación de las películas presentadas | Métricas por película |
| Productoras y plataformas | Autoevaluar sus producciones antes del estreno | Informe con revisión humana |
| Investigadoras y docentes de cine y género | Estudios cuantitativos reproducibles | Datos agregados abiertos |

## Supervisión humana

1. El sistema procesa el vídeo y propone etiquetas y métricas.
2. Una persona revisa en la demo las etiquetas dudosas y las corrige.
3. Solo entonces generamos el informe final.

## Infraestructura

- Desarrollo en local, con muestras pequeñas.
- Procesamiento en GPU (piloto en OVHcloud, 2 NVIDIA V100S). En CPU, el análisis de caras tardaba unas 3 horas por película.

## Permisos y acuerdos necesarios

- Películas de dominio público: comprobamos la licencia de cada una y su situación en la UE.
- Fondos de filmotecas o catálogos comerciales: acuerdo previo con quien tenga los derechos.
- Televisiones: acuerdo previo con la cadena para acceder a su archivo por API, nunca por scraping.
- Modelos de terceros: los modelos de InsightFace son de uso no comercial; para un uso comercial los sustituiríamos por otro modelo con licencia compatible.
- Evaluación de impacto antes de ampliar a otros contextos.

## Fases

1. **Piloto** (este reto): 17 películas de dominio público, de 1925 a 1968.
2. **Validación** con una institución usuaria, como una filmoteca o un festival.
3. **Ampliación**, con los acuerdos necesarios, a cine actual, series y televisión.

## Mantenimiento

Configuramos los modelos en `config/config.yaml` y cada etapa es independiente: podemos sustituir un
modelo sin tocar el resto, así que el sistema es agnóstico respecto al modelo.
