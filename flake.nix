{
  description = "Club Infantas Website";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs =
    { self, nixpkgs, ... }:
    let
      system = "x86_64-linux";

      pkgs = import nixpkgs {
        inherit system;
      };

      zine = pkgs.runCommand "zine-0.13.0" { } ''
        mkdir -p $out/bin
        tar -xJf ${
          pkgs.fetchurl {
            url = "https://github.com/kristoff-it/zine/releases/download/v0.13.0/x86_64-linux-musl.tar.xz";
            hash = "sha256-wlDgKdl4kBsMmjjqsKhg7524db9ob+Dwq/YfGAwoDbo=";
          }
        } -C $out/bin
      '';
    in
    {
      devShells."${system}".default =
        let
          shell-pkgs = with pkgs; [
            deno
            just
            reuse
            superhtml
            zine
          ];
        in
        pkgs.mkShell {
          packages = shell-pkgs;
        };
    };
}
