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

      zine = pkgs.runCommand "zine-0.14.0" { } ''
        mkdir -p $out/bin
        tar -xJf ${
          pkgs.fetchurl {
            url = "https://github.com/kristoff-it/zine/releases/download/v0.14.0/x86_64-linux-musl.tar.xz";
            hash = "sha256-iXZC9Gw4cqYxHyqz1MYi9fhiW/7o4d4tDeQll8E4Vik=";
          }
        } -C $out/bin
      '';
    in
    {
      devShells."${system}".default =
        let
          shell-pkgs = with pkgs; [
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
