# TODO

## PDFs de Régimen Tributario — autoalojados en el repo (ignorados por git)

Los PDFs se sirven desde `assets/documents/regimen/` mediante `$site.asset(...).link()` en `layouts/regimen.shtml`.
Están en `.gitignore` (`/assets/documents/`): no se suben al repo, cada despliegue debe proveerlos (copiar desde `Descargas/regimen-tributario/` o descargarlos según abajo).

### Convención de nombres

Solo minúsculas + guiones, en una sola carpeta:

- `informe-de-gestion-2025.pdf`
- `informe-de-gestion-2024.pdf`
- `informe-de-gestion-2023.pdf`
- `informe-de-gestion-2022.pdf`
- `informe-de-gestion-2021.pdf`
- `informe-de-gestion-2020.pdf`
- `informe-de-gestion-2019.pdf`

### Pendientes antes de autoalojar

- Total ~330 MB; 2019 (122 MB) y 2020 (147 MB) superan el límite de 100 MB por archivo de GitHub — comprimir primero (meta < 50 MB cada uno, ideal < 10 MB).
- 2023 (~37 MB) y 2021 (~16 MB) también deberían comprimirse.
- Tras comprimir, descargar desde WordPress con los nombres de arriba a `assets/documents/regimen/` y actualizar los 14 enlaces en `layouts/regimen.shtml`.

## PDFs de Estatutos — autoalojados en el repo (ignorados por git)

Servidos desde `assets/documents/estatutos/` mediante `$site.asset(...).link()` en `layouts/estatutos.shtml`. Misma convención: minúsculas + guiones (`propuestas-estatutos-2023.pdf`, 370 KB, ya optimizado).

## Nosotros — datos por confirmar

- **Año de fundación**: la línea de tiempo abre con el distintivo «Fundación» sin año; conviene reemplazarlo por el año real que confirme el club.
- **Cifras y cargos**: se mantienen los nombres y años históricos que ya publicaba el sitio; validar cargos (gerencia/presidencia) y la cifra de aforo (1 500 personas).

## Escuelas — datos por confirmar

La página `layouts/escuelas.shtml` se armó con contenido descriptivo genérico (qué se entrena en cada disciplina). Lo que falta definir con el club:

- **Horarios reales**, **tarifas** y **edades/categorías** de cada escuela (hoy no se muestran en la página; se resuelven por contacto).
- **Implementos propios** que pide cada escuela.

### Fotos

Hoy las 8 tarjetas usan un ícono SVG sobre un fondo con gradiente (sin imágenes). Para reemplazar el ícono por una foto, guardar en `assets/images/escuelas/` (p. ej. `vallenato.avif`) e insertar dentro de `.school-card__banner`:

```html
<img class="school-card__photo" src="$site.asset('images/escuelas/vallenato.avif').link()" alt="Escuela de vallenato">
```

(requiere agregar la regla `.school-card__photo` en `assets/styles/style.css`: `width: 100%; height: 100%; object-fit: cover;`).
