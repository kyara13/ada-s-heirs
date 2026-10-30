# Datos y licencias

## Corpus: cine clásico de dominio público (Internet Archive)

- Fuente: colección *Feature Films* de Internet Archive (https://archive.org/details/feature_films).
- Selección: **17 largometrajes de 1925 a 1968**, listados en `data/sources.csv` y repartidos por décadas.

### Cómo las elegimos

1. **Cumplen la licencia:** licencia abierta declarada y películas estadounidenses anteriores a 1970,
   cuando el dominio público es más fiable. Comprobamos la ficha de cada una (`licencia_verificada = si`).
2. **Son variadas:** distintas décadas, mudas y sonoras, en blanco y negro y en color, y géneros y repartos
   distintos (comedia, drama, cine negro, terror, western, musical), incluida *The Blood of Jesus* (1941),
   de cineasta y reparto afroamericanos.
3. **Con condiciones:** sin protagonistas menores de edad (los clasificadores fallan con niñas y niños)
   y sin documentales, propaganda, animación ni cine de explotación.

El motivo de cada película está en la columna `motivo_seleccion`.

### Qué significa "dominio público" aquí

- La licencia la **declara quien sube** la película a Internet Archive; no es una garantía.
- Casi siempre significa dominio público **en EE. UU.** En la UE una película está protegida hasta
  70 años después de la muerte del último de sus autores principales, así que alguna podría seguir
  protegida aquí.
- Por eso **no redistribuimos los vídeos** (no están en el repositorio) ni fragmentos: solo publicamos
  estadísticas agregadas, en el marco de la excepción de minería de textos y datos de la Directiva (UE) 2019/790.
- Atribución: columna `atribucion` (título, año y URL de Internet Archive).

### Limitaciones del corpus

- **No representa todo el cine:** es cine clásico estadounidense de dominio público, con mucha serie B y
  repartos mayoritariamente blancos. Presentamos los resultados como un **estudio de caso exploratorio**.
- Muchas películas son en blanco y negro y de baja resolución, y ahí el modelo rinde peor.
- Hay estereotipos sexistas y racistas de la época: los analizamos, porque es parte del objetivo,
  pero los contextualizamos y no los mostramos en la demo sin explicación.

## Anotación propia

`data/annotations/anotaciones.csv` y `data/annotations/no_detectadas.csv`: anotadas a mano por el equipo
para evaluar el sistema (más detalle en el README de esa carpeta).
