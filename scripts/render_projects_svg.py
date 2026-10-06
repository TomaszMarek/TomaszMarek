import html

SVG_WIDTH = 860
SVG_HEIGHT = 260

PROJECTS = [
    (
        "YouTube-Downloader",
        "Media Extraction & Desktop GUI",
        "STABLE",
        "#238636",
        "https://github.com/TomaszMarek/YouTube-Downloader",
    ),
    (
        "Android-PaintApp",
        "Mobile Touch Canvas Engine",
        "DEPLOYED",
        "#1f6feb",
        "https://github.com/TomaszMarek/Android-PaintApp",
    ),
    (
        "ImageOverlay",
        "Pixel Manipulation & Masking",
        "COMPLETE",
        "#8957e5",
        "https://github.com/TomaszMarek/ImageOverlay",
    ),
    (
        "BiurkowyAsystent-ESP32",
        "Firmware & Hardware I/O",
        "ARCHIVED",
        "#6e7681",
        "https://github.com/TomaszMarek/BiurkowyAsystent-ESP32",
    ),
    (
        "Milionerzy DB Engine",
        "Web Scraping & 10k Records Dataset",
        "IN PROGRESS",
        "#d29922",
        "",
    ),
]


def render_projects():
    rows_svg = []
    y = 85

    for name, role, status, badge_col, url in PROJECTS:
        safe_name = html.escape(name)
        safe_role = html.escape(role)
        safe_status = html.escape(status)

        name_svg = (
            f'<a href="{url}" target="_blank"><text x="35" y="{y}" fill="#58a6ff" font-weight="bold" font-size="12px" class="proj-link">{safe_name}</text></a>'
            if url
            else f'<text x="35" y="{y}" fill="#e6edf3" font-weight="bold" font-size="12px">{safe_name}</text>'
        )

        row = f"""    <!-- Row: {safe_name} -->
    <g class="row">
      {name_svg}
      <rect x="235" y="{y - 12}" width="345" height="18" rx="3" fill="#161b22" />
      <text x="245" y="{y}" fill="#8b949e" font-size="11px">{safe_role}</text>

      <rect x="630" y="{y - 12}" width="105" height="18" rx="9" fill="{badge_col}" opacity="0.2" />
      <rect x="630" y="{y - 12}" width="105" height="18" rx="9" fill="none" stroke="{badge_col}" stroke-width="1" />
      <text x="682" y="{y}" fill="{badge_col}" font-size="10px" font-weight="bold" text-anchor="middle">{safe_status}</text>
    </g>
    <line x1="35" y1="{y + 14}" x2="{SVG_WIDTH - 35}" y2="{y + 14}" stroke="#21262d" stroke-width="1" />"""
        rows_svg.append(row)
        y += 33

    rows_block = "\n".join(rows_svg)

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SVG_WIDTH} {SVG_HEIGHT}" width="{SVG_WIDTH}" height="{SVG_HEIGHT}">
  <style>
    .bg {{ fill: #0d1117; rx: 8px; stroke: #30363d; stroke-width: 1; }}
    text {{
      font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
    }}
    .header-text {{
      fill: #8b949e;
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.5px;
    }}
    .proj-link:hover {{
      text-decoration: underline;
      fill: #79c0ff;
    }}
  </style>

  <rect width="100%" height="100%" class="bg" />

  <!-- Nagłówek okna / folderu -->
  <text x="35" y="32" fill="#e3b341" font-size="13px">📁</text>
  <text x="58" y="31" fill="#e6edf3" font-size="12px" font-weight="bold">~/projects-inventory</text>
  <line x1="0" y1="46" x2="{SVG_WIDTH}" y2="46" stroke="#21262d" stroke-width="1" />

  <!-- Kolumny nagłówka -->
  <text x="35" y="62" class="header-text">PROJECT</text>
  <text x="245" y="62" class="header-text">ARCHITECTURE / ROLE</text>
  <text x="682" y="62" class="header-text" text-anchor="middle">STATUS</text>
  <line x1="35" y1="70" x2="{SVG_WIDTH - 35}" y2="70" stroke="#30363d" stroke-width="1" />

{rows_block}
</svg>"""

    with open("projects-inventory.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)

    print("Sukces: projects-inventory.svg wygenerowany.")


if __name__ == "__main__":
    render_projects()