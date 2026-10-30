# Registro de decisiones

Apuntamos cada decisión importante con su fecha y el motivo.

| Fecha | Decisión | Por qué |
|---|---|---|
| 24/10/2026 | Modalidad: vídeo | Nos permite medir el protagonismo visual: tamaño, centralidad y planos en solitario |
| 24/10/2026 | Corpus: 17 películas de dominio público (1925–1968) de Internet Archive | Licencia abierta declarada, comparación entre épocas y tema de interés del equipo |
| 24/10/2026 | 17 películas | Es un estudio exploratorio; así ajustamos el coste de GPU y el tiempo de anotación |
| 24/10/2026 | Detector de torchvision (BSD) en vez de YOLO de Ultralytics (AGPL) | Compatibilidad con la licencia MIT del repositorio |
| 24/10/2026 | Votación por trayectoria con umbral del 80 % y clase `no_determinado` | El clasificador falla en fotogramas sueltos |
| 26/10/2026 | Detección de planos solo por brillo (`luma_only`, AdaptiveDetector) | Con color no detectaba ningún corte en películas en blanco y negro |
| 27/10/2026 | Análisis de caras en GPU con onnxruntime-gpu 1.22.0 | La versión para CUDA 13 no soporta las V100S; en CPU tardaba unas 3 horas por película |
| 27/10/2026 | Votación: umbral del 70 % y mínimo de 2 caras (antes 80 % y 3) | Con 6 películas, el tiempo sin determinar baja entre 6 y 11 puntos y el % de mujeres cambia menos de 2 puntos |
| 27/10/2026 | *The General* marcada como dudosa | El modelo da un 84 % de mujeres en una película con un solo papel femenino relevante; nuestra anotación cuenta 4 mujeres de 24 personas |

## Ideas para después

- Audio: quién habla (Whisper y diarización), cruzado con quién sale en plano.
- Reconocer a la misma persona en planos distintos.
- Incluir la orientación de la cara (frontal o de perfil) en el índice.
- Intervalos de incertidumbre para cada porcentaje.
