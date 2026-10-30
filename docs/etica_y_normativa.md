# Marco ético y cumplimiento normativo

## Los 7 principios de las directrices éticas europeas para una IA fiable

| Principio | Cómo lo cumplimos |
|---|---|
| Agencia y supervisión humanas | En la demo una persona acepta o corrige las etiquetas antes de usar el informe |
| Robustez técnica y seguridad | Evaluación con anotaciones manuales, votación por trayectoria y `no_determinado` |
| Privacidad y gobernanza de datos | No guardamos recortes de caras ni embeddings; solo datos agregados; no identificamos a nadie |
| Transparencia | Métricas y pesos públicos y documentados, código abierto y uso de IA declarado |
| Diversidad, no discriminación y equidad | Medimos los errores por género y por tipo de película; hablamos de género percibido, no de identidad |
| Bienestar social y ambiental | Desarrollamos en local con muestras pequeñas y usamos la GPU solo para el corpus |
| Rendición de cuentas | Repositorio reproducible y registro de decisiones en `docs/decisiones.md` |

## Reglamento Europeo de IA

- No hacemos identificación biométrica: no reconocemos **quién** es nadie.
- Sí estimamos un atributo, el género percibido, a partir de la cara. Lo usamos solo con fines
  estadísticos y agregados sobre obras audiovisuales publicadas, nunca para tomar decisiones sobre
  personas concretas.
- Aplicamos salvaguardas: revisión humana, categoría `no_determinado`, documentación pública de las
  limitaciones y ningún almacenamiento de datos faciales.

## RGPD

- **Minimización:** procesamos las caras en memoria y solo guardamos resultados agregados.
- **Conservación:** no conservamos imágenes faciales ni embeddings.
- **Contexto:** analizamos intérpretes en obras publicadas, con un fin de investigación y de interés público.

## Datos de terceros

Usamos películas con licencia abierta declarada en Internet Archive (dominio público en EE. UU.).
No redistribuimos los vídeos ni fragmentos; solo publicamos estadísticas agregadas. Más detalle en
`datos_y_licencias.md`.

## Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| Etiquetar mal el género de una persona | `no_determinado`, revisión humana y solo resultados agregados |
| Sesgo del clasificador con cine mudo o de baja calidad | Evaluación por tipo de película y películas marcadas como dudosas |
| Que el detector pase por alto a mujeres | Anotamos las apariciones no detectadas y lo medimos por género |
| Uso del sistema para vigilar a personas concretas | Uso previsto documentado; no guardamos ninguna identidad |
| Licencias de modelos y películas | Tabla de licencias de terceros en el README; no redistribuimos vídeos |
