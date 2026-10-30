# Anotaciones manuales (ground truth)

Las usamos para **evaluar** el sistema: comparamos lo que predice con lo que anotamos nosotras a mano.

Anotamos fragmentos de dos películas de las 17, elegidas por ser muy distintas:

- *Detour* (1945), sonora en blanco y negro: 3 minutos (de 60 a 240 s), 25 recuadros.
- *The General* (1927), muda y de baja calidad: 24 trayectorias, más las apariciones que el detector no encontró.

## Cómo anotamos

1. Procesamos el fragmento con `python -m src.pipeline` y generamos las fichas de revisión con
   `scripts/dibujar_trayectorias.py`.
2. Para cada persona añadimos una fila en `anotaciones.csv`, sin mirar antes la predicción del sistema.
3. Las personas que el sistema no detectó las apuntamos en `no_detectadas.csv`.
4. Evaluamos con `python scripts/evaluate.py`.

| Columna | Valores |
|---|---|
| `video_id` | nombre del vídeo sin `.mp4` |
| `track_id` | número de la trayectoria |
| `genero_percibido` | `mujer` / `hombre` / `no_determinado` |
| `protagonista` | `si` / `no` (nuestro juicio) |
| `notas` | observaciones, por ejemplo "de perfil todo el rato" |

## Criterios

- Anotamos **género percibido**, igual que el modelo. Si dudamos, ponemos `no_determinado`.
- No guardamos nombres de actrices ni actores: no hacen falta para evaluar.
