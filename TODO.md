# TODO — Club Infantas

> **Cómo usar:** marca `[x]` al terminar. Cada bloque tiene un criterio de aceptación para saber cuándo está realmente cerrado. Prioridades: **P0** = bloquea el lanzamiento · **P1** = contenido/datos que faltan · **P2** = pulido y mantenimiento.
>
> **Última verificación:** 2026-11-10 · Build local con `zine release` ✅ · 8 páginas, 0 enlaces internos rotos ✅

## Definición de "listo para lanzar"

El sitio se puede publicar cuando **todos los P0 estén cerrados**: build reproducible desde un clon limpio, páginas de navegación con contenido real, dominio configurado y despliegue documentado.

## Resumen de estado

| Área | Estado | Prioridad |
|---|---|---|
| Build desde clon limpio | ✅ Verificado (8 PDFs versionados, 8 páginas, sin enlaces rotos) | — |
| Instalaciones | ❌ Placeholder | P0 |
| Afiliaciones | ❌ Placeholder | P0 |
| Inicio (imagen + noticias) | ❌ Placeholders | P0 |
| Dominio / despliegue | ❌ Sin configurar ni documentar | P0 |
| Metadatos / SEO | ❌ `meta description` vacío en todas las páginas | P0/P2 |
| Nosotros | 🟡 Contenido por validar | P1 |
| Escuelas | 🟡 Datos y fotos pendientes | P1 |
| Convenios | 🟡 Botones «Más» sin acción | P1 |
| Estatutos / Régimen | ✅ Contenido y PDFs listos (etiquetas de tamaño desactualizadas) | P2 |

---

## P0 — Bloqueantes de lanzamiento

### 1. Build reproducible (PDFs versionados) ✅

**Resuelto (2026-11-10):** los 8 PDFs referenciados por los layouts se agregaron a git con la estrategia **A. Versionar en git** y se quitó `/assets/documents/` de `.gitignore`. El `.zip` sin uso se eliminó. Un build desde un clon limpio (solo archivos versionados) quedó verificado.

**Contexto:** antes, un clon limpio fallaba con `missing site asset: 'documents/regimen/informe-de-gestion-2025.pdf'`, porque los PDFs solo existían en la máquina local. Ese bloqueo ya no existe.

- [x] **Estrategia elegida: A. Versionar en git** — ~57 MB total, todos los archivos < 20 MB (límite de GitHub: 100 MB por archivo).
- [x] Quitar `/assets/documents/` de `.gitignore` y agregar los 8 PDFs al repo.
- [x] Eliminar `estatutos/propuestas-estatutos-2023.zip` (272 KB, sin referencias en el sitio).
- [x] Verificar en un directorio limpio (solo archivos versionados) que `zine release` termina con éxito y genera los 8 PDFs en `public/documents/`.
- [x] Hacer commit de los PDFs y del cambio en `.gitignore`.

**Criterio de aceptación:** un clon nuevo del repo compila sin pasos manuales no documentados, y todos los enlaces a PDFs existen en `public/`. ✅

#### Inventario actual de PDFs (`assets/documents/`, versionados)

| Año | Archivo | Tamaño real | Etiqueta en `regimen.shtml` |
|---|---|---|---|
| 2025 | `regimen/informe-de-gestion-2025.pdf` | 1,2 MB | 1,1 MB ❌ |
| 2024 | `regimen/informe-de-gestion-2024.pdf` | 1,2 MB | 1,1 MB ❌ |
| 2023 | `regimen/informe-de-gestion-2023.pdf` | 15 MB | 14,2 MB ❌ |
| 2022 | `regimen/informe-de-gestion-2022.pdf` | 5,8 MB | 5,7 MB ❌ |
| 2021 | `regimen/informe-de-gestion-2021.pdf` | 6,7 MB | 6,7 MB ✅ |
| 2020 | `regimen/informe-de-gestion-2020.pdf` | 17 MB | 16,6 MB ❌ |
| 2019 | `regimen/informe-de-gestion-2019.pdf` | 9,4 MB | 9,3 MB ❌ |

- [ ] Corregir las etiquetas de tamaño en `layouts/regimen.shtml` (o quitar el tamaño del texto para no mantenerlo a mano).
- [x] Confirmar que `estatutos/propuestas-estatutos-2023.pdf` (370 KB) se publica con la misma estrategia.

**Convención de nombres:** solo minúsculas y guiones, una sola carpeta (`regimen/`, `estatutos/`). Los enlaces se generan con `$site.asset('documents/...').link()`.

### 2. Completar Instalaciones

Archivo: `layouts/instalaciones.shtml` (hoy: «Contenido de Instalaciones y Servicios.»).

- [ ] Redactar contenido real: zonas deportivas, piscinas, patinódromo, salones, kioscos, capacidad.
- [ ] Decidir si se muestran fotos o solo texto/iconos.
- [ ] Enlazar desde aquí a Servicios/Salones si esos contenidos se recuperan.
- [ ] Mantener el `<h1>` y el `container` como en el resto de páginas.

**Criterio de aceptación:** la página deja de ser placeholder, tiene `<h1>` + contenido y está enlazada correctamente desde el menú.

### 3. Completar Afiliaciones

Archivo: `layouts/afiliaciones.shtml` (hoy: «Contenido de Afiliaciones.»).

- [ ] Reunir requisitos, pasos, categorías y tarifas de afiliación.
- [ ] Decidir el canal de conversión: formulario, correo, teléfono o PDF descargable.
  - [ ] Si es formulario: elegir servicio (Formspree, Netlify Forms, etc.) y definir campos.
  - [ ] Si es PDF: agregarlo a `assets/documents/` y aplicar la estrategia del punto 1.
- [ ] Actualizar el CTA de `layouts/escuelas.shtml` si el flujo cambia.
- [ ] Revisar datos de contacto con el club (hoy: `servicioalcliente@clubinfantas.com`, `+57 313 4008227`).

**Criterio de aceptación:** un visitante entiende cómo afiliarse y tiene una acción concreta para iniciar el proceso.

### 4. Completar Inicio

Archivo: `layouts/index.shtml`.

- [ ] Reemplazar la imagen vacía del bloque «Un punto de encuentro…» (`:66`).
- [ ] Reemplazar las 3 tarjetas de Novedades que dicen `[Imagen Noticia 1/2/3]` (`:84`, `:92`, `:100`):
  - [ ] Definir noticias/eventos reales (o quitar la sección si no hay contenido vigente).
  - [ ] Añadir imágenes en `assets/images/` y texto/alt definitivos.
- [ ] Revisar los textos del carrusel y sus enlaces.
- [ ] Verificar que el carrusel sigue funcionando con `prefers-reduced-motion`.

**Criterio de aceptación:** ninguna cadena `[Imagen`, `placeholder` ni div vacío visible en la portada.

### 5. Dominio y despliegue

- [ ] Cambiar `.host_url = "https://example.com"` en `zine.ziggy` por el dominio real.
- [ ] Elegir host (Cloudflare Pages, VPS + Caddy/Nginx, contenedor, etc.).
- [ ] Definir cómo se sirve `public/` y cómo se actualiza (manual o CI).
- [ ] Si se usa CI: crear workflow que instale Zine, obtenga los PDFs (según punto 1) y publique `public/`.
- [ ] Documentar el flujo de despliegue en `README.md` (comandos, secretos, rollback).
- [ ] Verificar en producción: las 8 páginas, los 8 PDFs y los enlaces de mapas.

**Criterio de aceptación:** el sitio se publica con un procedimiento documentado y reproducible, sin depender de archivos locales no versionados.

### 6. Metadatos base

- [ ] Añadir `meta description` por página (hoy vacía en todas: `layouts/templates/base.shtml:7`).
  - [ ] Permitir que cada `.smd`/layout defina su descripción.
- [ ] Revisar títulos (`<title>`) y jerarquía de encabezados en todas las páginas.

**Criterio de aceptación:** cada página tiene una descripción única y útil (≈ 120–160 caracteres).

---

## P1 — Contenido y datos por confirmar con el club

### Nosotros (`layouts/nosotros.shtml`)

- [ ] **Año de fundación:** la línea de tiempo abre con «Fundación» sin año; reemplazarlo por el año confirmado.
- [ ] **Cargos históricos:** validar gerencia/presidencia de cada hito (Edgar Lozano Jaimes, Miguel Sampayo, Jorge Barreto Daniels, Jorge Montaño, Edilberto Mejía).
- [ ] **Cifras:** validar la capacidad de 1 500 personas y el texto «mejor club del oriente colombiano».
- [ ] Revisar el retrato y su pie de foto (Rosso L. Mantilla).

### Escuelas (`layouts/escuelas.shtml`)

- [ ] **Horarios reales** por escuela y categoría.
- [ ] **Tarifas** y forma de pago.
- [ ] **Edades/categorías** admitidas.
- [ ] **Implementos propios** que debe llevar cada alumno.
- [ ] Validar la descripción genérica de las 8 disciplinas.
- [ ] **Fotos:** reemplazar los íconos SVG por imágenes cuando estén disponibles:
  - [ ] Guardar en `assets/images/escuelas/` (p. ej. `vallenato.avif`).
  - [ ] Insertar dentro de `.school-card__banner`:
    ```html
    <img class="school-card__photo" src="$site.asset('images/escuelas/vallenato.avif').link()" alt="Escuela de vallenato">
    ```
  - [ ] Agregar la regla en `assets/styles/style.css`:
    ```css
    .school-card__photo { width: 100%; height: 100%; object-fit: cover; }
    ```

### Convenios (`layouts/convenios.shtml`)

- [ ] Decidir qué hacen los 8 botones «Más» (`:43, :82, :121, :159, :197, :251, :288, :325`):
  - [ ] Enlazarlos a una página/detalle, o
  - [ ] Eliminarlos (dejar solo «Ubicación»).
- [ ] Validar nombres, sedes y enlaces de Google Maps de los 8 aliados.
- [ ] Confirmar si faltan convenios o descuentos por publicar.

---

## P2 — Pulido y mantenimiento

- [ ] Añadir favicon y `apple-touch-icon` (se quitaron los enlaces muertos en un commit anterior).
- [ ] Añadir Open Graph / Twitter Card (título, descripción, imagen).
- [ ] Añadir `canonical` cuando `host_url` sea real.
- [ ] Generar `robots.txt` y `sitemap.xml` (o confirmar que Zine los genera).
- [ ] Crear página 404.
- [ ] Revisar accesibilidad: foco visible, orden de tabulación, contraste, `aria-*` del carrusel y menú.
- [ ] Revisar que las 8 fuentes precargadas se usen realmente (o reducir pesos para bajar transferencia).
- [ ] Decidir si los `content/*.smd` (hoy vacíos) se usan para copy o si todo queda en layouts.
- [ ] Corregir `REUSE.toml`: referencia `.zine.ziggy-schema`, que no existe en el repo.
- [ ] Confirmar licencia/atribución de las imágenes (`assets/images/*.avif`).

---

## Documentación

- [ ] Actualizar `README.md`:
  - [ ] Secciones reales: Inicio, Nosotros, Escuelas, Instalaciones, Afiliaciones, Convenios, Estatutos, Régimen.
  - [ ] Quitar Deportes / Servicios / Salones (ya no existen).
  - [ ] Documentar el despliegue y la estrategia de PDFs.
- [ ] Mantener este TODO al día: mover lo terminado a «Hecho» y actualizar la fecha de verificación.

---

## Verificación antes de cada release

```sh
# Build (con Podman)
podman build -t club-infantas .
podman run --rm -v "$PWD:/src:Z" club-infantas zine release

# Build limpio (sin PDFs locales) — debe pasar tras resolver P0.1
# git clone <repo> /tmp/club-test && cd /tmp/club-test
# podman run --rm -v "$PWD:/src:Z" club-infantas zine release
```

- [ ] `public/` contiene las 8 páginas y `documents/` con los PDFs referenciados.
- [ ] Sin enlaces internos rotos.
- [ ] Revisar portada, menú móvil, carrusel y descargas en un navegador real.
- [ ] Probar en producción tras desplegar.

---

## Hecho

- [x] Sitio migrado a Zine 0.14 con Nix + Containerfile.
- [x] Navegación reestructurada (Inicio, Nosotros, Escuelas, Instalaciones, Afiliaciones, Convenios + Estatutos/Régimen).
- [x] Portada con carrusel CSS, autoplay, dots/flechas y reduced-motion.
- [x] Nosotros con historia, línea de tiempo y misión/visión.
- [x] Escuelas con las 8 disciplinas.
- [x] Convenios con «Canjes» y «Descuentos».
- [x] Estatutos con convocatoria y PDF autoalojado.
- [x] Régimen tributario con informes 2019–2025 autoalojados.
- [x] PDFs comprimidos (de ~330 MB a ~55 MB) y los 14 enlaces actualizados.
- [x] PDFs autoalojados versionados en git (8 archivos, ~57 MB); build desde clon limpio verificado.
- [x] Eliminado el `.zip` de estatutos sin uso; `.gitignore` ya no excluye `assets/documents/`.
- [x] Tema esmeralda, modo claro/oscuro, cabecera flotante y footer.
- [x] Fuentes autoalojadas y licencias REUSE.
- [x] `public/` regenerado desde el código actual (elimina salidas viejas de Deportes/Salones/Servicios).
