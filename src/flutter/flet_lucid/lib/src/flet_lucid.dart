import 'package:flet/flet.dart';
import 'package:flutter/material.dart';

import './lucid_data.dart';

class FletLucidControl extends StatelessWidget {
  final Control control;

  const FletLucidControl({
    super.key,
    required this.control,
  });

  @override
  Widget build(BuildContext context) {
    return LayoutControl(
      control: control,
      child: Icon(
        lucidData[control.getString("icon")], // parsing map
        size: control.getDouble("size"),
        color: control.getColor("color", context),
        blendMode: control.getBlendMode("blend_mode"),
        semanticLabel: control.getString("semantics_label"),
        applyTextScaling: control.getBool("apply_text_scaling"),
        fill: control.getDouble("fill"),
        grade: control.getDouble("grade"),
        weight: control.getDouble("weight"),
        opticalSize: control.getDouble("optical_size"),
        shadows: control.getBoxShadows("shadows", Theme.of(context)),
      ),
    );
  }
}
