import os
import re
import sys
import html

SVG_WIDTH = 860
SVG_HEIGHT = 480

AVI_FILE = "avi-ascii.svg"
if not os.path.exists(AVI_FILE):
    print(f"Brak pliku {AVI_FILE}!")
    sys.exit(1)

with open(AVI_FILE, "r", encoding="utf-8") as f:
    avi_content = f.read()

raw_lines = re.findall(r"<text[^>]*>(.*?)</text>", avi_content)
ascii_svg_elements = []
line_y = 75
for i, line in enumerate(raw_lines):
    delay = round(i * 0.02, 2)
    ascii_svg_elements.append(
        f'    <text class="type-in" x="25" y="{line_y}" xml:space="preserve" '
        f'style="animation-delay: {delay}s;">{line}</text>'
    )
    line_y += 11.2

ascii_block = "\n".join(ascii_svg_elements)

spec_lines = [
    ("USER", "tomaszmarek // workstation", "#58a6ff"),
    ("ROLE", "Software & App Developer", "#7ee787"),
    ("STACK", "Java, Android SDK, Python, C++", "#e6edf3"),
    ("PIPELINE", "Web Scraping, SQLite, JSON Parser", "#ffa657"),
    ("FOCUS", "Practical Tools & Edge-Case Hunting", "#ffa657"),
    ("ACTIVE", "Milionerzy DB [10k Question Records]", "#e3b341"),
    ("STRATEGY", "Algorithmic Logic & Chess Systems", "#d2a8ff"),
]

right_svg_elements = []
stat_y = 80
for key, val, col in spec_lines:
    safe_v = html.escape(val)
    right_svg_elements.append(f"""    <g transform="translate(380, {stat_y})">
      <text x="0" y="0" fill="#8b949e" font-weight="600" font-size="12px">{key}:</text>
      <text x="95" y="0" fill="{col}" font-size="12px">{safe_v}</text>
    </g>""")
    stat_y += 28

right_block = "\n".join(right_svg_elements)

bars_svg = """
    <g transform="translate(380, 312)">
      <text x="0" y="12" fill="#58a6ff" font-size="11px" font-weight="bold">INT</text>
      <text x="35" y="12" fill="#8b949e" font-size="11px">Web Scraping &amp; Data Extraction</text>
      <rect x="275" y="2" width="130" height="8" rx="4" fill="#21262d" />
      <rect x="275" y="2" width="118" height="8" rx="4" fill="#58a6ff" />

      <text x="0" y="44" fill="#7ee787" font-size="11px" font-weight="bold">DEX</text>
      <text x="35" y="44" fill="#8b949e" font-size="11px">Application Crafting &amp; Architecture</text>
      <rect x="275" y="34" width="130" height="8" rx="4" fill="#21262d" />
      <rect x="275" y="34" width="110" height="8" rx="4" fill="#7ee787" />

      <text x="0" y="76" fill="#ffa657" font-size="11px" font-weight="bold">PER</text>
      <text x="35" y="76" fill="#8b949e" font-size="11px">QA, Logic &amp; Edge-Case Debugging</text>
      <rect x="275" y="66" width="130" height="8" rx="4" fill="#21262d" />
      <rect x="275" y="66" width="124" height="8" rx="4" fill="#ffa657" />

      <text x="0" y="108" fill="#d2a8ff" font-size="11px" font-weight="bold">WIS</text>
      <text x="35" y="108" fill="#8b949e" font-size="11px">Chess Strategy &amp; Trivia Logic</text>
      <rect x="275" y="98" width="130" height="8" rx="4" fill="#21262d" />
      <rect x="275" y="98" width="115" height="8" rx="4" fill="#d2a8ff" />
    </g>
"""

svg_template = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SVG_WIDTH} {SVG_HEIGHT}" width="{SVG_WIDTH}" height="{SVG_HEIGHT}">
  <style>
    .bg {{ fill: #0d1117; rx: 8px; stroke: #30363d; stroke-width: 1; }}
    text {{
      font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
    }}
    .ascii-text text {{
      font-size: 8.8px;
      fill: #8b949e;
      white-space: pre;
    }}
    .type-in {{
      opacity: 0;
      animation: appear 0.1s ease forwards;
    }}
    @keyframes appear {{
      to {{ opacity: 1; }}
    }}
  </style>

  <rect width="100%" height="100%" class="bg" />

  <!-- Przyciski okna -->
  <circle cx="25" cy="22" r="5.5" fill="#ff5f56" />
  <circle cx="43" cy="22" r="5.5" fill="#ffbd2e" />
  <circle cx="61" cy="22" r="5.5" fill="#27c93f" />
  <text x="90" y="26" fill="#8b949e" font-size="12px">tomaszmarek@main-station:~ (profile.env)</text>
  <line x1="0" y1="42" x2="{SVG_WIDTH}" y2="42" stroke="#21262d" stroke-width="1" />

  <!-- Lewa sekcja: Portret ASCII -->
  <g class="ascii-text">
{ascii_block}
  </g>

  <!-- Pionowa linia podziału -->
  <line x1="355" y1="58" x2="355" y2="{SVG_HEIGHT - 22}" stroke="#21262d" stroke-width="1" />

  <!-- Prawa sekcja: Dane -->
  <g id="specs">
{right_block}
  </g>

  <!-- Pozioma linia dzieląca dane od pasków -->
  <line x1="380" y1="288" x2="825" y2="288" stroke="#21262d" stroke-width="1" />

  <!-- Paski atrybutów -->
{bars_svg}
</svg>"""

with open("dashboard.svg", "w", encoding="utf-8") as f:
    f.write(svg_template)

print("Sukces: dashboard.svg zaktualizowany z poprawnym zachowaniem spacji i geometrii.")