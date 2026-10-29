# Perspectiva de género (10 % de la nota)

## Decisiones de diseño

- **Género percibido, no identidad.** El sistema no "sabe" el género de nadie; estima cómo lo
  percibiría un modelo entrenado con etiquetas humanas. Lo decimos en la demo y en los informes.
- **Categoría `no_determinado`.** Si el modelo no tiene mayoría clara (≥ 80 %) no se fuerza una etiqueta.
- **Binario como limitación explícita.** Los modelos disponibles solo predicen mujer/hombre.
  No lo presentamos como verdad, sino como limitación documentada.
- **Revisión humana.** La demo permite corregir etiquetas antes de publicar resultados.

## Evaluación de sesgos del clasificador

No hemos usado FairFace. Evaluamos el clasificador sobre fragmentos de películas anotados a mano
(anotación humana de referencia en `data/annotations/anotaciones.csv`), agrupados por tipo de película,
para ver si falla más con algún tipo de material y con algún género. Las películas se eligieron para
cubrir condiciones distintas: blanco y negro con sonido, cine mudo y cine en color.

Parámetros del sistema: `vote_threshold` = 0,8 (porcentaje mínimo de votos coincidentes para asignar
etiqueta).

| Grupo | Precisión | Recall | Sin decidir | Nº muestras |
|---|---|---|---|---|
| Detour (B/N, sonora): mujeres | sin predicciones de "mujer" | 0,00 (0 de 4) | 3 de 4 (75 %) | 4 recuadros |
| Detour (B/N, sonora): hombres | 0,93 | 0,67 (14 de 21) | 7 de 21 (33 %) | 21 recuadros |
| The General (muda) | pendiente | pendiente | pendiente | pendiente |
| Película en color | pendiente | pendiente | pendiente | pendiente |

**Muestra y cautelas.** Detour: fragmento de 3 minutos (60 a 240 s), 25 recuadros. No son 25 personas
distintas, porque una misma persona aparece con varios números. Anotación manual de referencia hecha
por una persona del equipo. En total, el sistema deja sin decidir al 40 % de los recuadros.

**Lectura.** En las tres mujeres que quedan sin decidir, la mayoría de votos del modelo era la correcta,
pero con una confianza de 0,57 a 0,61, por debajo del umbral de 0,8. El único error del fragmento
(una mujer clasificada como hombre) tiene confianza 1,0, pero se apoya en pocos fotogramas: es una
mujer que se gira de espaldas muy deprisa. Con tan pocas mujeres (4) no podemos concluir un sesgo
general. Lo presentamos como una señal que hay que validar con más películas y más muestras.

## Interpretación con perspectiva de género (lección de Karina Gibert)

Un dato puede leerse al revés si no se pone en contexto. Ejemplo: si en una película la protagonista
femenina tiene mucho tiempo en pantalla pero casi siempre en plano compartido y nunca sola, ¿es
protagonismo real o acompañamiento? Separad presencia (cuánto se las ve) de protagonismo (cómo se
las encuadra) antes de concluir.

Referente: el Geena Davis Institute (GD-IQ) midió que en las 200 películas más taquilleras de 2014–2015
los personajes masculinos tuvieron aproximadamente el doble de tiempo en pantalla que los femeninos.

<!-- TODO: comparar vuestros resultados por década con ese referente -->

## Referencias

- Formación "Perspectiva de género", Karina Gibert (14/10/2026)
- <!-- TODO: informe de sesgos de género en IA citado en la formación de ética -->
