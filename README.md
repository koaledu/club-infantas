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

### Con Nix

Requiere [Nix](https://nixos.org). Entrar al shell de desarrollo:

```sh
nix develop
```

Para construir el sitio:

```sh
zine release
```

Para servir en local:

```sh
zine
```

### Con Docker o Podman

Requiere [Podman](https://podman.io) o [Docker](https://docker.com).

Construir la imagen:

```sh
podman build -t club-infantas .
```

Ejecutar el servidor de desarrollo con live reload:

```sh
podman run --rm --init -p 1990:1990 -v "$(pwd):/src:Z" club-infantas
```

El bind mount (`-v`) sincroniza los archivos del host al contenedor, permitiendo live reload. Sin `-v`, los cambios no se reflejan.

Abrir `http://localhost:1990`. Ctrl+C para detener.

## Licencia

El código del sitio es propietario. Fuentes de terceros: normalize.css bajo CC0-1.0, Montserrat y Rubik bajo OFL-1.1. Consulta `LICENSES/` y `REUSE.toml` para más detalles.
