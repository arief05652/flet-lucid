default:
    @just --list

generate:
    @uv run generate/generator.py

# build app {apk, linux, web}
build platform:
    @cd examples/flet_lucid_example && \
    uv run flet build {{ platform }}
    @echo build success to {{ platform }}!

# run result build app {apk, web} default is linux
run platform="":
    @cd examples/flet_lucid_example && \
    uv run flet run {{ platform }} -d -r

# serve web after build app to web
serve:
    @cd examples/flet_lucid_example && \
    uv run flet serve

sync:
    # main directory
    uv sync

    # flutter
    @cd src/flutter/flet_lucid && \
    flutter pub get

    # example python
    @cd examples/flet_lucid_example && \
    uv sync
