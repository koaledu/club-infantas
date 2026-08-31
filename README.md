# Club Infantas

Propuesta para el nuevo sitio web del Club Infantas, construido con [Zine](https://zine-ssg.io) (v0.13.0). Reemplaza la versión actual del sitio.

## Secciones

- **Inicio** — Página principal
- **Nosotros** — Sobre el club
- **Deportes** — Actividades deportivas
- **Servicios** — Servicios ofrecidos
- **Salones** — Espacios disponibles
- **Afiliaciones** — Cómo afiliarse
- **Estatutos** — Normativa del club
- **Régimen** — Régimen interno

## Desarrollo

Requiere [Nix](https://nixos.org). Entrar al shell de desarrollo:

```sh
nix develop
```

Para construir el sitio:

```sh
zine build
```

Para servir en local:

```sh
zine serve
```

## Licencia

El código del sitio es propietario. Fuentes de terceros: normalize.css bajo CC0-1.0, Montserrat y Rubik bajo OFL-1.1. Consulta `LICENSES/` y `REUSE.toml` para más detalles.
