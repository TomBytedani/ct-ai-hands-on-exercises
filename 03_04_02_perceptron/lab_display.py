"""Presentation helpers only. The perceptron and training loop live in the notebook."""

from html import escape

from IPython.display import HTML, SVG, display


def table(headers, rows):
    header = ''.join(f'<th scope="col">{escape(str(h))}</th>' for h in headers)
    body = ''.join('<tr>' + ''.join(f'<td>{escape(str(v))}</td>' for v in row)
                   + '</tr>' for row in rows)
    display(HTML('<div style="overflow-x:auto"><table>'
                 f'<thead><tr>{header}</tr></thead><tbody>{body}</tbody>'
                 '</table></div>'))


def show_cases(examples, weights, bias, predict, title):
    print(title)
    rows = []
    for x1, x2, target in examples:
        score = weights[0] * x1 + weights[1] * x2 + bias
        prediction = predict(x1, x2, weights, bias)
        calculation = f'{weights[0]} × {x1} + {weights[1]} × {x2} + ({bias}) = {score}'
        rows.append([(x1, x2), target, calculation, prediction,
                     'correct' if target == prediction else 'WRONG'])
    table(['Inputs (x1, x2)', 'Target', 'Score calculation', 'Prediction', 'Result'], rows)


def show_trace(trace, epoch):
    print(f'Training steps during epoch {epoch}: parameters can change after each row.')
    rows = [[r['inputs'], r['target'], r['before_weights'], r['before_bias'],
             r['score'], r['prediction'], r['error'], r['after_weights'], r['after_bias']]
            for r in trace if r['epoch'] == epoch]
    table(['Inputs', 'Target', 'Weights before', 'Bias before', 'Score',
           'Prediction', 'Error', 'Weights after', 'Bias after'], rows)


def show_history(history):
    table(['Epoch', 'Weights after pass', 'Bias after pass',
           'Updates during pass', 'Wrong after pass'],
          [[r['epoch'], r['weights'], r['bias'], r['updates'], r['wrong']]
           for r in history])
    # A small standalone SVG: no plotting package or network access required.
    width, height = 620, 245
    left, top, span_x, span_y = 60, 25, 500, 155
    count = len(history)
    points = [(left + i * span_x / max(1, count - 1),
               top + span_y * (4 - r['wrong']) / 4) for i, r in enumerate(history)]
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
             'role="img" aria-label="Wrong predictions after each epoch; exact values in table above">',
             '<rect width="100%" height="100%" fill="white"/>',
             '<g font-family="sans-serif" font-size="12" fill="#202020">']
    for wrong in range(5):
        y = top + span_y * (4 - wrong) / 4
        parts.append(f'<path d="M {left} {y} H 560" stroke="#ddd"/>')
        parts.append(f'<text x="40" y="{y + 4}">{wrong}</text>')
    coords = ' '.join(f'{x},{y}' for x, y in points)
    parts.append(f'<polyline points="{coords}" fill="none" stroke="#1565c0" stroke-width="3"/>')
    for (x, y), row in zip(points, history):
        parts.append(f'<circle cx="{x}" cy="{y}" r="4" fill="#1565c0"/>')
        parts.append(f'<text x="{x}" y="202" text-anchor="middle">{row["epoch"]}</text>')
    parts.extend(['<text x="60" y="16">Wrong predictions after pass</text>',
                  '<text x="305" y="230" text-anchor="middle">Epoch</text>', '</g></svg>'])
    display(SVG(''.join(parts)))


def show_boundary(examples, weights, bias, predict):
    """Draw score=0, clipped to the plot; show exact scores in the companion table."""
    low, high = -0.4, 1.4

    def screen(x, y):
        return 70 + (x - low) * 360 / (high - low), 395 - (y - low) * 330 / (high - low)

    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="530" height="470" '
             'role="img" aria-label="Perceptron boundary and the four AND cases; '
             'each point is labeled with its target and prediction">',
             '<rect width="100%" height="100%" fill="white"/>',
             '<g font-family="sans-serif" font-size="13" fill="#202020">',
             f'<text x="25" y="25">Score = {weights[0]} × x1 + {weights[1]} × x2 + ({bias})</text>',
             '<text x="25" y="46">Dashed line: score = 0 (prediction 1 on the line)</text>']
    for tick in (0, 1):
        px, py = screen(tick, tick)
        parts.append(f'<path d="M {px} 65 V 395 M 70 {py} H 430" stroke="#ddd"/>')
        parts.append(f'<text x="{px}" y="417" text-anchor="middle">{tick}</text>')
        parts.append(f'<text x="50" y="{py + 4}">{tick}</text>')
    parts.extend(['<path d="M 70 65 V 395 H 430" fill="none" stroke="#555"/>',
                  '<text x="225" y="442">First switch (x1)</text>',
                  '<text x="15" y="255" transform="rotate(-90 15 255)">Second switch (x2)</text>'])
    w1, w2 = weights
    intersections = []
    if w2:
        for x in (low, high):
            y = -(w1 * x + bias) / w2
            if low <= y <= high:
                intersections.append((x, y))
    if w1:
        for y in (low, high):
            x = -(w2 * y + bias) / w1
            if low <= x <= high:
                intersections.append((x, y))
    intersections = list(dict.fromkeys(intersections))
    if len(intersections) >= 2:
        ax, ay = screen(*intersections[0])
        bx, by = screen(*intersections[1])
        parts.append(f'<path d="M {ax} {ay} L {bx} {by}" stroke="#555" '
                     'stroke-width="2" stroke-dasharray="6 5"/>')
    else:
        parts.append('<text x="80" y="85">No separating line in this view.</text>')
    for x1, x2, target in examples:
        px, py = screen(x1, x2)
        prediction = predict(x1, x2, weights, bias)
        fill = '#1565c0' if target == prediction else '#b23a00'
        parts.append(f'<circle cx="{px}" cy="{py}" r="7" fill="{fill}"/>')
        parts.append(f'<text x="{px}" y="{py - 17}" text-anchor="middle">'
                     f'({x1}, {x2}): target {target}, predicted {prediction}</text>')
    parts.append('</g></svg>')
    display(SVG(''.join(parts)))
