# AGENTS.md

Flet extension exposing Lucide icons. Python control + Flutter widget + generated icon enum/map.

## Setup

```bash
just sync   # uv sync (root), flutter pub get (src/flutter/flet_lucid), uv sync (example)
```

Requires Python 3.10+ (package) and 3.12 (example), Flutter SDK, `uv`, `just`.

## Commands

```bash
just generate          # regenerate icon enum + Dart map from generate/icons/*.json
just run               # run example app, default platform (linux)
just run web           # run example on web
just build linux       # build example; also apk, web
just serve             # serve built web app
```

No test suite, linter, or CI config exists. Run `dart analyze lib` in `src/flutter/flet_lucid` and verify changes by building and running the example.

## Generated code

`just generate` rewrites both generated files. Do not hand-edit them:

- `src/flet_lucid/lucid_data.py` — `Icons` enum (snake_case values)
- `src/flutter/flet_lucid/lib/src/lucid_data.dart` — `lucidData` map

Run it from the repo root. It also deletes any `.svg` files in `generate/icons/`. Output is deterministic.

`generate/icons/` holds 2071 files: 2029 canonical 1.70 icons plus 42 legacy aliases. Add an icon by dropping `<name>.json` into `generate/icons/`, then run `just generate`.

## Wiring: keep layers in sync

A property change must touch both sides, or the Flutter widget silently gets `null`:

- Python: `src/flet_lucid/flet_lucid.py` — `@ft.control("LucidIcon")` fields (snake_case).
- Dart: `src/flutter/flet_lucid/lib/src/flet_lucid.dart` — `control.getString("...")` / `getDouble(...)` keys matching the Python field names.
- Control type string `"LucidIcon"` must match in `flet_lucid.py` and `src/flutter/flet_lucid/lib/src/extension.dart`.

Rebuild the example after changing the Dart extension; hot reload is not enough for native builds.

## Rendering

`Icon(Icons.X)` is the only rendering path. It uses the `flutter_lucide` font bundled by the extension on all platforms, including web. No asset copy or `page.fonts` needed.

## Packaging notes

- `src/flet_lucid.egg-info/` is tracked; packaging commands mutate `SOURCES.txt`. Do not commit unrelated churn.
- Keep versions in `pyproject.toml` and `src/flutter/flet_lucid/pubspec.yaml` in sync.
- `flutter_lucide` is pinned to `1.70.0`. `generate/generator.py` maps 42 legacy icon names to 1.70 canonical names; update `ALIASES` before bumping it.
- Flet 1.x widgets import `package:material_ui/material_ui.dart`, not `package:flutter/material.dart`. Mixing both causes `ThemeData` type errors.
- The example consumes the package via `[tool.uv.sources]` and `[tool.flet.dev_packages]` pointing at the repo root.
