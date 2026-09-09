FROM alpine:3.20

ARG ZINE_VERSION=0.13.0

RUN apk add --no-cache curl xz

RUN curl -fsSL "https://github.com/kristoff-it/zine/releases/download/v${ZINE_VERSION}/x86_64-linux-musl.tar.xz" \
    | tar -xJ -C /usr/local/bin

WORKDIR /src

EXPOSE 1990

CMD ["sh", "-c", "printf '\\n  → http://localhost:1990\\n\\n' && zine --host 0.0.0.0"]
