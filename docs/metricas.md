# Propuesta de métricas

## Problema

Medimos automáticamente cuánto aparecen las mujeres en las películas y con qué protagonismo visual,
para que filmotecas, festivales, productoras e investigadoras puedan auditar la representación en el cine.

## Qué entendemos por protagonismo

Una persona es protagonista cuando la realización la sitúa en el centro de la atención visual:
aparece mucho tiempo, en grande, centrada, sola en plano y en los momentos de apertura o cierre.
Separamos este protagonismo de la simple presencia: salir mucho en un plano compartido no es lo mismo que ser el foco.

## Nivel 1: presencia

| Métrica | Definición | Qué responde |
|---|---|---|
| % de mujeres | mujeres distintas sobre el total de personas | cuántas mujeres aparecen |
| % de tiempo | segundos en pantalla de mujeres sobre el total | cuánto tiempo se las ve |

Las personas sin una etiqueta fiable cuentan como `no_determinado`. También calculamos el % de tiempo
de mujeres solo sobre el tiempo con género determinado, para que no dependa de cuántas quedan sin decidir.

## Nivel 2: protagonismo (por persona)

| Componente | Cálculo | Peso | Por qué |
|---|---|---|---|
| Tiempo en pantalla | segundos / máximo del vídeo | 0,30 | Es el indicador más directo de importancia en la historia |
| Tamaño | área media de la caja / área del fotograma | 0,20 | Un primer plano concentra la atención |
| En solitario | % de fotogramas en que es la única persona | 0,20 | El plano individual indica que la realización la pone en el foco |
| Centralidad | 1 − distancia al centro / distancia máxima | 0,15 | Responde a la pregunta del reto de si el centro es el protagonista, sin que lo decida todo |
| Apertura o cierre | aparece en el primer o último 10 % | 0,15 | Abrir o cerrar la historia es un rol protagonista |

El **índice de protagonismo** es la media ponderada (de 0 a 1). Contamos como protagonista a quien
tiene un índice de 0,5 o más, y medimos qué % de las protagonistas son mujeres. Los pesos están en
`config/config.yaml`.

## Validación

Comparamos el índice con nuestro juicio humano (columna `protagonista` de las anotaciones).
Analizar cómo cambian las conclusiones al variar los pesos está en la hoja de ruta.

## Limitaciones

- El género es **percibido** por un modelo y binario; usamos `no_determinado` cuando hay duda.
- La centralidad depende del estilo de cada película.
- Sin audio no sabemos quién habla: alguien puede estar en plano sin intervenir.
