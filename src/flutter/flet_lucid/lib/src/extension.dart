import 'package:flutter/widgets.dart';
import 'package:flet/flet.dart';

import 'flet_lucid.dart';

class Extension extends FletExtension {
  @override
  Widget? createWidget(Key? key, Control control) {
    switch (control.type) {
      case "LucidIcon":
        return FletLucidControl(key: key, control: control);
      default:
        return null;
    }
  }
}
