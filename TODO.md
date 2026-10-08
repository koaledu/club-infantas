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
