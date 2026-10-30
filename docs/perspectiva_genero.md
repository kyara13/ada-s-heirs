# Perspectiva de género

## Decisiones de diseño

- **Género percibido, no identidad.** El sistema no sabe el género de nadie: estima cómo lo percibiría
  un modelo entrenado con etiquetas humanas. Lo decimos en la demo y en los informes.
- **Categoría `no_determinado`.** Si el modelo no tiene una mayoría clara, no forzamos ninguna etiqueta.
- **Binario como limitación.** Los modelos disponibles solo predicen mujer u hombre. No lo presentamos
  como verdad, sino como una limitación documentada.
- **Revisión humana.** En la demo una persona puede corregir las etiquetas antes de publicar resultados.
- **Presencia frente a protagonismo.** Siguiendo la formación de Karina Gibert, separamos cuánto se ve
  a las mujeres de cómo se las encuadra: una protagonista con mucho tiempo en pantalla, pero siempre en
  plano compartido y nunca sola, puede estar acompañando más que protagonizando.

## Evaluación de errores por grupo

No usamos FairFace. Evaluamos el clasificador sobre fragmentos de películas anotados a mano
(`data/annotations/anotaciones.csv`) para ver si falla más con algún tipo de película o con algún género.
Elegimos dos películas muy distintas: una sonora en blanco y negro y una muda.

En esta evaluación usamos un umbral de votación de 0,8; después lo bajamos a 0,7.

| Grupo | Precisión | Recall | Sin decidir | Muestras |
|---|---|---|---|---|
| *Detour* (B/N, sonora): mujeres | sin predicciones de "mujer" | 0,00 (0 de 4) | 3 de 4 (75 %) | 4 recuadros |
| *Detour* (B/N, sonora): hombres | 0,93 | 0,67 (14 de 21) | 7 de 21 (33 %) | 21 recuadros |

**Muestra.** *Detour*: fragmento de 3 minutos (de 60 a 240 s), 25 recuadros. No son 25 personas
distintas, porque una misma persona puede aparecer con varios números. En total, el sistema deja
sin decidir el 40 % de los recuadros.

**Lectura.** En las tres mujeres sin decidir, la mayoría de votos del modelo era correcta, pero con una
confianza de 0,57 a 0,61, por debajo del umbral de 0,8. El único error (una mujer clasificada como
hombre) tiene confianza 1,0 pero se apoya en pocos fotogramas: es una mujer que se gira de espaldas muy
deprisa. Con solo 4 mujeres no podemos concluir un sesgo general; lo tratamos como una señal que hay
que validar con más películas.

**The General.** En esta película muda el modelo da un 84 % de mujeres, mientras que en nuestra
anotación de un fragmento solo 4 de 24 personas son mujeres. Además, de 26 apariciones que el detector
no encontró, 8 eran de mujeres. Con cine mudo de baja calidad el modelo falla, y por eso marcamos la
película como dudosa.

## Referente

El Geena Davis Institute (GD-IQ) midió que en las 200 películas más taquilleras de 2014–2015 los
personajes masculinos tuvieron aproximadamente el doble de tiempo en pantalla que los femeninos.

## Referencias

- Formación "Perspectiva de género", Karina Gibert (14/10/2026).
