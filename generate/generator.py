from datetime import datetime
from pathlib import Path

folder = Path("generate/icons")

json_files = []

if folder.is_dir():
    for name in folder.iterdir():
        if name.suffix == ".svg":
            name.unlink()

        elif name.suffix == ".json":
            json_files.append(name.stem.replace("-", "_"))

json_files.sort(key=str.lower)

print(f"Total JSON: {len(json_files)}")


# create py enum data
python_output = "src/flet_lucid/lucid_data.py"
with open(python_output, "w") as f:
    f.write(f"# This Enum Generate by Python Script: {datetime.now()}\n\n")
    f.write("from enum import Enum\n\n\n")
    f.write("class Icons(Enum):\n")

    for name in json_files:
        enum_name = name.upper()
        f.write(f'  {enum_name} = "{name}"\n')


# create dict dart
dart_output = "src/flutter/flet_lucid/lib/src/lucid_data.dart"
with open(dart_output, "w") as f:
    f.write(f"// This Map Generate by Python Script: {datetime.now()}\n\n")
    f.write("import 'package:flutter/widgets.dart';\n")
    f.write("import 'package:flutter_lucide/flutter_lucide.dart';\n\n")
    f.write("Map<String, IconData> lucidData = {\n")

    for name in json_files:
        f.write(f'  "{name}": LucideIcons.{name},\n')
    f.write("};")
