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
| SEO base | ❌ Meta descriptions vacías | P0 |
| Nosotros / Escuelas / Convenios | 🟡 Datos por confirmar | P1 |
| Pulido | 🟡 Favicon, 404, etc. | P2 |

## P0 — Bloqueantes

### 1. ✅ PDFs versionados

- [x] 8 PDFs (~57 MB) versionados en git (commit `aaefb23`); `.gitignore` ya no excluye `assets/documents/`.
- [x] `.zip` sin uso eliminado.
- [x] Build desde clon limpio verificado (8 páginas y 8 PDFs generados).
- [ ] Corregir etiquetas de tamaño en `layouts/regimen.shtml`: 2020 (17 vs 16,6), 2023 (15 vs 14,2), 2019 (9,4 vs 9,3), 2022 (5,8 vs 5,7), 2024/2025 (1,2 vs 1,1).

### 2. Instalaciones (`layouts/instalaciones.shtml`)

- [ ] Reemplazar «Contenido de Instalaciones y Servicios.» por contenido real: zonas deportivas, piscinas, patinódromo, salones, kioscos, capacidad.
- [ ] Decidir si lleva fotos.
- [ ] Añadir `<h1>` + `container` como el resto de páginas.

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

- [ ] `meta description` única por página (`layouts/templates/base.shtml:7`).
- [ ] Revisar títulos y jerarquía de encabezados.

## P1 — Datos por confirmar

**Nosotros** (`layouts/nosotros.shtml`)
- [ ] Año de fundación (hoy solo dice «Fundación»).
- [ ] Validar cargos históricos y la capacidad de 1 500 personas.

**Escuelas** (`layouts/escuelas.shtml`)
- [ ] Horarios, tarifas, edades/categorías e implementos por escuela.
- [ ] Fotos: guardar en `assets/images/escuelas/`, insertar `<img class="school-card__photo">` en `.school-card__banner` y añadir `.school-card__photo { width: 100%; height: 100%; object-fit: cover; }` a `style.css`.

**Convenios** (`layouts/convenios.shtml`)
- [ ] Decidir qué hacen los 8 botones «Más» (`:43, :82, :121, :159, :197, :251, :288, :325`): enlazar o eliminar.
- [ ] Validar aliados, sedes y enlaces de Google Maps.

## P2 — Pulido

- [ ] Favicon, Open Graph/Twitter y canonical.
- [ ] `robots.txt`, `sitemap.xml` y página 404.
- [ ] Revisión de accesibilidad: foco, tabulación, contraste, `aria-*` del carrusel y menú.
- [ ] Revisar fuentes precargadas (reducir pesos si no se usan).
- [ ] Decidir si `content/*.smd` se usa para copy o todo queda en layouts.
- [ ] Corregir `REUSE.toml` (referencia `.zine.ziggy-schema`, que no existe).
- [ ] Confirmar licencia/atribución de `assets/images/*.avif`.

## Documentación

- [x] Actualizar `README.md`: secciones reales, comandos de desarrollo y PDFs versionados.
- [ ] Documentar el despliegue en `README.md` cuando esté definido.
- [ ] Mantener este TODO al día.

## Verificación

```sh
podman build -t club-infantas .
podman run --rm -v "$PWD:/src:Z" club-infantas zine release
```

- [ ] 8 páginas y 8 PDFs en `public/`; sin enlaces internos rotos.
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
