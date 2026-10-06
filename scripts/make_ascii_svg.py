import os
import sys
from PIL import Image

RAMP = " .`:-=+*cs#%@"

WIDTH = 64
CHAR_ASPECT = 0.55
SVG_WIDTH = 370
SVG_HEIGHT = 380


def make_ascii_svg(image_path: str = "source-prepped.png", output_svg: str = "avi-ascii.svg"):
    if not os.path.exists(image_path):
        print(f"Błąd: Nie znaleziono pliku {image_path}. Najpierw uruchom prep_photo.py.")
        sys.exit(1)

    img = Image.open(image_path).convert("L")
    w, h = img.size

    aspect_ratio = h / w
    calc_height = int(WIDTH * aspect_ratio * CHAR_ASPECT)

    img_resized = img.resize((WIDTH, calc_height), Image.Resampling.LANCZOS)
    pixels = img_resized.load()

    lines = []
    ramp_len = len(RAMP)

    for y in range(calc_height):
        line_chars = []
        for x in range(WIDTH):
            val = pixels[x, y]
            idx = int((255 - val) / 255 * (ramp_len - 1))
            line_chars.append(RAMP[idx])
        line_str = "".join(line_chars).rstrip()
        lines.append(line_str)

    font_size = round(SVG_WIDTH / (WIDTH * 0.62), 1)
    line_spacing = font_size * 1.15
    start_y = 35

    svg_lines = []
    stagger = 0.04

    for i, line in enumerate(lines):
        y_pos = start_y + (i * line_spacing)
        delay = round(i * stagger, 2)
        safe_line = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

        line_markup = (
            f'    <text class="row" x="15" y="{y_pos:.1f}" '
            f'style="animation-delay: {delay}s;">{safe_line}</text>'
        )
        svg_lines.append(line_markup)

    rows_str = "\n".join(svg_lines)

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SVG_WIDTH} {SVG_HEIGHT}" width="{SVG_WIDTH}" height="{SVG_HEIGHT}">
  <style>
    .bg {{ fill: #0d1117; rx: 6px; }}
    text {{
      font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
      font-size: {font_size}px;
      font-weight: 500;
      fill: #c9d1d9;
      white-space: pre;
    }}
    .row {{
      opacity: 0;
      transform: translateX(-4px);
      animation: typeIn 0.15s ease forwards;
    }}
    @keyframes typeIn {{
      to {{
        opacity: 1;
        transform: translateX(0);
      }}
    }}
  </style>

  <rect width="100%" height="100%" class="bg" />

  <g id="ascii-portrait">
{rows_str}
  </g>
</svg>"""

    with open(output_svg, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"Sukces! Wygenerowano animowany portret: {output_svg}")


if __name__ == "__main__":
    make_ascii_svg()