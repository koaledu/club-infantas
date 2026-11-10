# TODO — Club Infantas

> Prioridades: **P0** bloquea el lanzamiento · **P1** contenido por confirmar · **P2** pulido.
> Marca `[x]` al terminar. Última verificación: 2026-11-10 · build limpio ✅ (8 páginas, 8 PDFs, 0 enlaces rotos).

**Listo para lanzar** = todos los P0 cerrados.

## Estado

| Área | Estado | Prioridad |
|---|---|---|
| Build limpio + PDFs | ✅ | — |
| Instalaciones / Afiliaciones | ❌ Placeholders | P0 |
| Inicio | ❌ Imagen y noticias placeholder | P0 |
| Dominio / despliegue | ❌ Sin configurar | P0 |
| SEO base | ✅ Descripciones y metadatos sociales | — |
| Nosotros / Escuelas / Convenios | 🟡 Datos por confirmar | P1 |
| Pulido | 🟡 Favicon, 404, etc. | P2 |

## P0 — Bloqueantes

### 1. ✅ PDFs versionados

- [x] 8 PDFs (~57 MB) versionados en git (commit `aaefb23`); `.gitignore` ya no excluye `assets/documents/`.
- [x] `.zip` sin uso eliminado.
- [x] Build desde clon limpio verificado (8 páginas y 8 PDFs generados).
- [x] Etiquetas de tamaño corregidas en `layouts/regimen.shtml` según los archivos reales.

### 2. Instalaciones (`layouts/instalaciones.shtml`)

- [ ] Reemplazar «Contenido de Instalaciones y Servicios.» por contenido real: zonas deportivas, piscinas, patinódromo, salones, kioscos, capacidad.
- [ ] Decidir si lleva fotos.
- [x] Añadido `container` y `<main>` como el resto de páginas.

### 3. Afiliaciones (`layouts/afiliaciones.shtml`)

- [ ] Requisitos, pasos, categorías y tarifas.
- [ ] Elegir canal: formulario, correo, teléfono o PDF.
- [ ] Actualizar el CTA de Escuelas y validar datos de contacto.

### 4. Inicio (`layouts/index.shtml`)

- [ ] Imagen real en el bloque «Un punto de encuentro…» (`:66`).
- [ ] Reemplazar las 3 tarjetas `[Imagen Noticia 1/2/3]` (`:84`, `:92`, `:100`) o quitar la sección.
- [ ] Revisar el carrusel y sus enlaces.

### 5. Dominio y despliegue

- [ ] `host_url` real en `zine.ziggy` (hoy `https://example.com`).
- [ ] Elegir host y definir cómo se publica `public/` (manual o CI).
- [ ] Documentar el flujo en `README.md` y verificar producción (8 páginas + 8 PDFs).

### 6. Metadatos base

- [x] `meta description` única en las 9 páginas, definida en `content/*.smd` y renderizada por `base.shtml`.
- [x] Open Graph, Twitter Card y `theme-color` añadidos.
- [x] Jerarquía de encabezados revisada (cada página tiene un solo `<h1>`).

## P1 — Datos por confirmar

**Nosotros** (`layouts/nosotros.shtml`)
- [ ] Año de fundación (hoy solo dice «Fundación»).
- [ ] Validar cargos históricos y la capacidad de 1 500 personas.

**Escuelas** (`layouts/escuelas.shtml`)
- [ ] Horarios, tarifas, edades/categorías e implementos por escuela.
- [ ] Fotos: guardar en `assets/images/escuelas/` e insertar `<img class="school-card__photo">` en `.school-card__banner`.
- [x] Regla `.school-card__photo` añadida a `style.css`.

**Convenios** (`layouts/convenios.shtml`)
- [ ] Decidir qué hacen los 8 botones «Más» (`:43, :82, :121, :159, :197, :251, :288, :325`): enlazar o eliminar.
- [ ] Validar aliados, sedes y enlaces de Google Maps.

## P2 — Pulido

- [ ] Favicon y `canonical` (este último requiere el dominio real).
- [x] `robots.txt` y página 404 (`public/404.html`, con `noindex`).
- [ ] `sitemap.xml` (requiere el dominio real).
- [x] Accesibilidad: skip link, landmark `<main>`, foco visible y jerarquía de encabezados.
- [x] Fuentes precargadas reducidas a 4 pesos; itálicas sin uso eliminadas (~330 KB menos).
- [ ] Decidir si `content/*.smd` se usa para copy o todo queda en layouts.
- [x] `REUSE.toml` corregido y ampliado a los archivos nuevos.
- [ ] Confirmar licencia/atribución de `assets/images/*.avif`.

## Documentación

- [x] Actualizar `README.md`: secciones reales, comandos de desarrollo y PDFs versionados.
- [ ] Documentar el despliegue en `README.md` cuando esté definido.
- [ ] Mantener este TODO al día.

## Verificación

```sh
podman build -t club-infantas .
podman run --rm -v "$PWD:/src:Z" club-infantas zine release
python3 scripts/check_links.py public
```

El workflow `.github/workflows/build.yml` ejecuta estos pasos en cada push y PR.

- [ ] 9 páginas y 8 PDFs en `public/`; sin enlaces internos rotos.
- [ ] Revisar portada, menú móvil, carrusel y descargas en un navegador real.
- [ ] Probar producción tras desplegar.

## Hecho

- [x] Sitio en Zine 0.14 con Nix + Containerfile, tema esmeralda, modo claro/oscuro, footer y fuentes autoalojadas.
- [x] Navegación actual (Inicio, Nosotros, Escuelas, Instalaciones, Afiliaciones, Convenios, Estatutos, Régimen).
- [x] Portada con carrusel CSS (autoplay, dots, flechas y reduced-motion).
- [x] Nosotros con historia, timeline y misión/visión.
- [x] Escuelas con 8 disciplinas y Convenios con Canjes/Descuentos.
- [x] Estatutos y Régimen con PDFs autoalojados, comprimidos y versionados en git (`aaefb23`); build limpio verificado.
- [x] `public/` regenerado desde el código actual; salidas viejas de Deportes/Salones/Servicios eliminadas.
- [x] Descripciones, Open Graph, Twitter Card y `theme-color` en las 9 páginas.
- [x] Skip link, landmark `<main>`, foco visible y un solo `<h1>` por página.
- [x] Página 404 (`public/404.html`) y `robots.txt` instalado vía `static_assets`.
- [x] Fuentes itálicas sin uso eliminadas; solo quedan 4 pesos y 4 preloads.
- [x] CI de build y checker de enlaces (`.github/workflows/build.yml`, `scripts/check_links.py`).
- [x] Regla `.school-card__photo` añadida y `REUSE.toml` actualizado.
