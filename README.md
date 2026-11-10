# Club Infantas

Sitio web del Club Infantas, construido con [Zine](https://zine-ssg.io) (v0.14.0).

Secciones: Inicio · Nosotros · Escuelas · Instalaciones · Afiliaciones · Convenios · Estatutos · Régimen.

## Desarrollo

### Con Nix

Requiere [Nix](https://nixos.org):

```sh
nix develop
zine          # servidor local con live reload
zine release  # build estático en public/
```

### Con Podman o Docker

```sh
podman build -f Containerfile -t club-infantas .
podman run --rm --init -p 1990:1990 -v "$PWD:/src:Z" club-infantas
```

Abrir `http://localhost:1990/club-infantas/`. El bind mount (`-v`) es necesario para el live reload.

Para servir en la raíz (`http://localhost:1990/`), pasa `--url-path-prefix ""`:

```sh
podman run --rm --init -p 1990:1990 -v "$PWD:/src:Z" club-infantas zine --host 0.0.0.0 --url-path-prefix ""
```

La CI (`.github/workflows/build.yml`) compila el sitio y ejecuta `scripts/check_links.py` en cada push.

## Publicación

Cada push a `main` publica el sitio automáticamente en GitHub Pages:

<https://koaledu.github.io/club-infantas/>

El workflow compila, verifica enlaces y metadatos, y despliega `public/`. En pull requests solo compila y verifica.

Configuración inicial (una sola vez): en **Settings → Pages → Source**, elige **GitHub Actions**. Después, cada push a `main` publica automáticamente.

## Documentos

Los PDFs de Estatutos y Régimen están en `assets/documents/`, versionados en git, y se enlazan con `$site.asset(...).link()`.

## Licencia

El código es propietario. Terceros: normalize.css (CC0-1.0), Montserrat y Rubik (OFL-1.1). Ver `LICENSES/` y `REUSE.toml`.
