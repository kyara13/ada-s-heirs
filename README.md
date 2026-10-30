# Ada's Heirs: presencia y protagonismo de las mujeres en el cine

> Reto **"Mujeres por la IA Abierta"** (SEDIA · Comunidad IA de Código Abierto)
> Equipo: Kyara Gamarra Videla · Judith Caralt Rico · Luna Ospina Loaiza (La Salle – Universitat Ramon Llull)

Medimos automáticamente cuánto aparecen las mujeres en las películas y con qué protagonismo visual,
para que filmotecas, festivales, productoras e investigadoras puedan auditar la representación en el cine.

## 1. Descripción de la solución

Hemos construido un sistema de IA abierto que analiza películas y calcula:

- **Presencia:** % de mujeres entre las personas que aparecen y % de su tiempo en pantalla.
- **Protagonismo:** un índice por persona que combina tiempo en pantalla, tamaño en el encuadre,
  centralidad, planos en solitario y apariciones al principio o al final, y el % de protagonistas que son mujeres.

Detalle de las métricas: [`docs/metricas.md`](docs/metricas.md).

### Pipeline

```
vídeo → muestreo de fotogramas → detección de planos → detección de personas
      → seguimiento → análisis facial (género percibido) → votación por trayectoria
      → métricas → demo con revisión humana
```

| Módulo | Entrada | Salida |
|---|---|---|
| `src/shots.py` | vídeo | `planos.json` |
| `src/detection.py` | vídeo + planos | `detecciones.json` |
| `src/tracking.py` | detecciones | `tracks.json` |
| `src/faces.py` | vídeo + tracks | `caras.json` |
| `src/aggregation.py` | caras + tracks | `personas.json` |
| `src/metrics.py` | personas + tracks | `metricas.json` |

Configuramos todos los modelos en [`config/config.yaml`](config/config.yaml): cambiar de modelo es cambiar una línea.

## 2. Instalación

```bash
git clone <URL-del-repo>
cd reto-mujeres-ia-video
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env               # token de OVHcloud, solo si se usa
```

## 3. Uso

```bash
# 1. Descargar los vídeos listados en data/sources.csv
python scripts/download_videos.py

# 2. Procesar un vídeo (todas las etapas)
python -m src.pipeline --video data/videos/ejemplo.mp4

# 3. Repetir solo algunas etapas (las demás se reutilizan de outputs/)
python -m src.pipeline --video data/videos/ejemplo.mp4 --steps aggregation,metrics

# 4. Prueba rápida en un portátil sin GPU (5 minutos, sin análisis facial)
python -m src.pipeline --video data/videos/ejemplo.mp4 --config config/config_local.yaml

# 5. Demo con revisión humana
streamlit run app/app.py

# 6. Evaluar contra nuestras anotaciones manuales
python scripts/evaluate.py --annotations data/annotations/anotaciones.csv

# 7. Resumen de todas las películas por década
python scripts/resumen_corpus.py
```

## 4. Datos

**17 películas de dominio público (1925–1968)** de la colección *Feature Films* de Internet Archive,
elegidas por licencia, década, calidad de imagen y variedad de géneros y repartos (`data/sources.csv`).
No subimos los vídeos al repositorio. Criterios, licencias y limitaciones:
[`docs/datos_y_licencias.md`](docs/datos_y_licencias.md).

## 5. Resultados

**Prueba completa en portátil** (5 minutos de *Detour*, 1 fotograma por segundo, sin análisis facial):
6 planos, 300 fotogramas, 502 detecciones de personas y 33 trayectorias.

**Evaluación manual.** De las 17 películas elegimos dos muy distintas y las anotamos a mano:

| Película | Resultado |
|---|---|
| *Detour* (1945), sonora en B/N | Hombres: precisión 0,93, recall 14 de 21. Mujeres: 3 de 4 sin decidir (la mayoría de votos era correcta, pero con poca confianza) |
| *The General* (1927), muda | El modelo da un 84 % de mujeres; nuestra anotación de un fragmento cuenta 4 de 24. Marcamos la película como dudosa |

Detalle en [`docs/perspectiva_genero.md`](docs/perspectiva_genero.md). El resumen por película y década
del corpus está en `outputs/resumen_corpus.csv`.

## 6. Perspectiva de género, ética y normativa

- [`docs/perspectiva_genero.md`](docs/perspectiva_genero.md)
- [`docs/etica_y_normativa.md`](docs/etica_y_normativa.md)
- [`docs/plan_despliegue.md`](docs/plan_despliegue.md)
- [`docs/decisiones.md`](docs/decisiones.md)

## 7. Componentes de terceros y licencias

| Componente | Uso | Licencia |
|---|---|---|
| PyTorch / torchvision (Faster R-CNN) | Detección de personas | BSD-3-Clause |
| trackers (ByteTrack) | Seguimiento | Apache-2.0 |
| supervision | Estructuras de detección | MIT |
| PySceneDetect | Detección de planos | BSD-3-Clause |
| OpenCV | Lectura de vídeo | Apache-2.0 |
| InsightFace (código) | Análisis facial | MIT; **los modelos preentrenados son de uso no comercial, así que no los incluimos: se descargan aparte** |
| Streamlit | Demo | Apache-2.0 |

Elegimos el detector de torchvision en vez de YOLO de Ultralytics porque este último es AGPL-3.0,
incompatible con nuestra licencia MIT.

## 8. Declaración de uso de IA

Hemos usado asistentes de IA generativa como apoyo para programar, documentar y preparar la presentación.
Hemos revisado todo el código, los datos y los resultados.

## 9. Hoja de ruta

- [ ] Combinar con el audio (quién habla) usando Whisper y diarización
- [ ] Reconocer a la misma persona en planos distintos
- [ ] Incluir la orientación de la cara en el índice de protagonismo
- [ ] Medir la incertidumbre por persona y por vídeo
- [ ] Ampliar a cine actual, series y televisión, con los acuerdos necesarios

## 10. Licencia

[MIT](LICENSE)
