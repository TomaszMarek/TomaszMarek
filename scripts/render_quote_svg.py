import html

SVG_WIDTH = 860
SVG_HEIGHT = 80

QUOTE = '"When you see a good move, look for a better one."'
AUTHOR = "— Emanuel Lasker (2nd World Chess Champion)"


def render_quote():
    safe_quote = html.escape(QUOTE)
    safe_author = html.escape(AUTHOR)

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SVG_WIDTH} {SVG_HEIGHT}" width="{SVG_WIDTH}" height="{SVG_HEIGHT}">
  <style>
    .card-bg {{
      fill: #0d1117;
      stroke: #30363d;
      stroke-width: 1;
      rx: 6px;
    }}
    text {{
      font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
    }}
    .chess-piece {{
      font-size: 26px;
      fill: #58a6ff;
    }}
    .quote-text {{
      font-size: 13px;
      font-weight: 600;
      fill: #f0f6fc;
      opacity: 0;
      animation: fadeIn 0.8s ease forwards 0.4s;
    }}
    .author-text {{
      font-size: 11px;
      fill: #7d8590;
      opacity: 0;
      animation: fadeIn 0.8s ease forwards 0.8s;
    }}
    .accent-bar {{
      fill: #58a6ff;
    }}
    @keyframes fadeIn {{
      to {{ opacity: 1; }}
    }}
  </style>

  <!-- Tlo ramki -->
  <rect width="100%" height="100%" class="card-bg" />

  <!-- Pasek akcentowy z lewej strony -->
  <path d="M 0 6 Q 0 0 6 0 L 6 0 L 6 {SVG_HEIGHT} L 6 {SVG_HEIGHT} Q 0 {SVG_HEIGHT} 0 {SVG_HEIGHT - 6} Z" class="accent-bar" />

  <!-- Ikona skoczka szachowego -->
  <text x="30" y="50" class="chess-piece">♞</text>

  <!-- Cytat i autor -->
  <g transform="translate(70, 0)">
    <text x="0" y="36" class="quote-text">{safe_quote}</text>
    <text x="0" y="58" class="author-text">{safe_author}</text>
  </g>
</svg>"""

    with open("chess-quote.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)

    print("Wygenerowano plik: chess-quote.svg!")


if __name__ == "__main__":
    render_quote()