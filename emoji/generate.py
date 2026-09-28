#!/usr/bin/env python3
"""Generate Channel Kit Telegram emoji PNGs (100x100 and 512x512)."""
from __future__ import annotations

import math
import os
from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT100 = os.path.join(ROOT, "pack-100")
OUT512 = os.path.join(ROOT, "pack-512")

INK = (28, 28, 36, 255)
WHITE = (255, 255, 255, 255)
YELLOW = (255, 206, 60, 255)
CORAL = (255, 82, 92, 255)
LIME = (92, 210, 72, 255)
SKY = (64, 164, 255, 255)
SKY_D = (40, 130, 220, 255)
ORANGE = (255, 146, 48, 255)
SOFT = (248, 249, 252, 255)
GOLD = (255, 196, 40, 255)
GRAY = (170, 174, 186, 255)


def circle(d, cx, cy, r, fill):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=fill)


def thick_line(d, p1, p2, thickness, color):
    x1, y1 = p1
    x2, y2 = p2
    dx, dy = x2 - x1, y2 - y1
    length = math.hypot(dx, dy) or 1
    nx, ny = -dy / length, dx / length
    t = thickness / 2
    d.polygon(
        [
            (x1 + nx * t, y1 + ny * t),
            (x2 + nx * t, y2 + ny * t),
            (x2 - nx * t, y2 - ny * t),
            (x1 - nx * t, y1 - ny * t),
        ],
        fill=color,
    )
    circle(d, x1, y1, t, color)
    circle(d, x2, y2, t, color)


def save_both(name, draw_fn):
    for size, folder in [(100, OUT100), (512, OUT512)]:
        os.makedirs(folder, exist_ok=True)
        im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        draw_fn(im, size)
        im.save(os.path.join(folder, f"{name}.png"), "PNG")


def draw_like(im, s):
    d = ImageDraw.Draw(im)
    sc = s / 100.0
    d.rounded_rectangle([36 * sc, 42 * sc, 90 * sc, 86 * sc], radius=16 * sc, fill=SKY)
    for x in [42, 56, 70]:
        d.ellipse([x * sc, 30 * sc, (x + 16) * sc, 50 * sc], fill=SKY)
    d.ellipse([36 * sc, 58 * sc, 58 * sc, 88 * sc], fill=SKY)
    d.rounded_rectangle([14 * sc, 10 * sc, 42 * sc, 58 * sc], radius=14 * sc, fill=SKY)
    d.ellipse([14 * sc, 8 * sc, 42 * sc, 36 * sc], fill=SKY)
    d.ellipse([20 * sc, 46 * sc, 48 * sc, 74 * sc], fill=SKY)
    d.ellipse([22 * sc, 14 * sc, 34 * sc, 26 * sc], fill=(160, 210, 255, 180))
    for x in [50, 64, 78]:
        d.line([(x * sc, 52 * sc), (x * sc, 76 * sc)], fill=SKY_D, width=max(1, int(2.5 * sc)))
    d.ellipse([34 * sc, 48 * sc, 46 * sc, 60 * sc], fill=SKY_D)


def draw_heart(im, s):
    px = im.load()
    for y in range(s):
        for x in range(s):
            nx = (x / (s - 1) - 0.5) * 2.4
            ny = (0.42 - y / (s - 1)) * 2.5
            a = nx * nx + ny * ny - 1
            if a * a * a - nx * nx * ny * ny * ny <= 0:
                dist = math.hypot(nx + 0.35, ny - 0.25)
                hl = 0.75 + 0.25 * (dist / 0.35) if dist < 0.35 else 1.0
                r = int(CORAL[0] + (255 - CORAL[0]) * (1 - hl) * 0.35)
                g = int(CORAL[1] + (255 - CORAL[1]) * (1 - hl) * 0.35)
                b = int(CORAL[2] + (255 - CORAL[2]) * (1 - hl) * 0.35)
                px[x, y] = (r, g, b, 255)


def draw_fire(im, s):
    d = ImageDraw.Draw(im)
    sc = s / 100
    d.ellipse([28 * sc, 28 * sc, 72 * sc, 88 * sc], fill=ORANGE)
    d.ellipse([34 * sc, 18 * sc, 66 * sc, 70 * sc], fill=ORANGE)
    d.polygon([(50 * sc, 6 * sc), (68 * sc, 40 * sc), (32 * sc, 40 * sc)], fill=ORANGE)
    d.ellipse([18 * sc, 40 * sc, 42 * sc, 72 * sc], fill=ORANGE)
    d.ellipse([34 * sc, 38 * sc, 66 * sc, 86 * sc], fill=CORAL)
    d.ellipse([38 * sc, 28 * sc, 62 * sc, 70 * sc], fill=CORAL)
    d.polygon([(50 * sc, 20 * sc), (62 * sc, 44 * sc), (38 * sc, 44 * sc)], fill=CORAL)
    d.ellipse([40 * sc, 52 * sc, 60 * sc, 86 * sc], fill=YELLOW)
    d.ellipse([42 * sc, 46 * sc, 58 * sc, 74 * sc], fill=YELLOW)


def draw_check(im, s):
    d = ImageDraw.Draw(im)
    sc = s / 100
    d.ellipse([4 * sc, 4 * sc, 96 * sc, 96 * sc], fill=LIME)
    w = max(9 * sc, 3)
    thick_line(d, (28 * sc, 52 * sc), (44 * sc, 70 * sc), w, WHITE)
    thick_line(d, (44 * sc, 70 * sc), (74 * sc, 32 * sc), w, WHITE)


def draw_cross(im, s):
    d = ImageDraw.Draw(im)
    sc = s / 100
    d.ellipse([4 * sc, 4 * sc, 96 * sc, 96 * sc], fill=CORAL)
    w = max(9 * sc, 3)
    thick_line(d, (32 * sc, 32 * sc), (68 * sc, 68 * sc), w, WHITE)
    thick_line(d, (68 * sc, 32 * sc), (32 * sc, 68 * sc), w, WHITE)


def draw_clap(im, s):
    d = ImageDraw.Draw(im)
    sc = s / 100
    d.ellipse([8 * sc, 30 * sc, 55 * sc, 85 * sc], fill=YELLOW)
    for x, y in [(14, 22), (26, 16), (38, 18)]:
        d.ellipse([x * sc, y * sc, (x + 18) * sc, (y + 28) * sc], fill=YELLOW)
    d.ellipse([45 * sc, 22 * sc, 92 * sc, 78 * sc], fill=ORANGE)
    for x, y in [(52, 10), (64, 6), (76, 12)]:
        d.ellipse([x * sc, y * sc, (x + 18) * sc, (y + 28) * sc], fill=ORANGE)
    for ang in range(0, 360, 45):
        rad = math.radians(ang)
        thick_line(
            d,
            (50 * sc + math.cos(rad) * 40 * sc, 48 * sc + math.sin(rad) * 40 * sc),
            (50 * sc + math.cos(rad) * 47 * sc, 48 * sc + math.sin(rad) * 47 * sc),
            max(2.5 * sc, 2),
            CORAL,
        )


def draw_think(im, s):
    d = ImageDraw.Draw(im)
    sc = s / 100
    d.ellipse([6 * sc, 10 * sc, 78 * sc, 82 * sc], fill=YELLOW)
    circle(d, 30 * sc, 42 * sc, 5 * sc, INK)
    circle(d, 54 * sc, 42 * sc, 5 * sc, INK)
    thick_line(d, (20 * sc, 30 * sc), (38 * sc, 26 * sc), max(3 * sc, 2), INK)
    thick_line(d, (46 * sc, 30 * sc), (64 * sc, 30 * sc), max(3 * sc, 2), INK)
    d.arc([34 * sc, 52 * sc, 58 * sc, 68 * sc], 10, 170, fill=INK, width=max(3, int(3.5 * sc)))
    circle(d, 74 * sc, 72 * sc, 5 * sc, SOFT)
    circle(d, 84 * sc, 60 * sc, 7 * sc, SOFT)
    d.ellipse([70 * sc, 18 * sc, 96 * sc, 48 * sc], fill=SOFT)
    d.arc([76 * sc, 24 * sc, 90 * sc, 38 * sc], 180, 80, fill=INK, width=max(3, int(3 * sc)))
    thick_line(d, (83 * sc, 36 * sc), (83 * sc, 40 * sc), max(3 * sc, 2), INK)
    circle(d, 83 * sc, 44 * sc, 2.2 * sc, INK)


def draw_rocket(im, s):
    d = ImageDraw.Draw(im)
    sc = s / 100
    d.ellipse([34 * sc, 6 * sc, 66 * sc, 40 * sc], fill=SKY)
    d.rectangle([34 * sc, 24 * sc, 66 * sc, 68 * sc], fill=SKY)
    d.ellipse([34 * sc, 52 * sc, 66 * sc, 72 * sc], fill=SKY)
    circle(d, 50 * sc, 32 * sc, 10 * sc, WHITE)
    circle(d, 50 * sc, 32 * sc, 6 * sc, (40, 120, 220, 255))
    d.rectangle([34 * sc, 48 * sc, 66 * sc, 54 * sc], fill=CORAL)
    d.polygon([(34 * sc, 52 * sc), (12 * sc, 78 * sc), (34 * sc, 70 * sc)], fill=CORAL)
    d.polygon([(66 * sc, 52 * sc), (88 * sc, 78 * sc), (66 * sc, 70 * sc)], fill=CORAL)
    d.polygon([(38 * sc, 70 * sc), (50 * sc, 96 * sc), (62 * sc, 70 * sc)], fill=ORANGE)
    d.polygon([(43 * sc, 70 * sc), (50 * sc, 88 * sc), (57 * sc, 70 * sc)], fill=YELLOW)


def draw_idea(im, s):
    d = ImageDraw.Draw(im)
    sc = s / 100
    for ang in list(range(-60, 61, 30)) + list(range(120, 241, 30)):
        rad = math.radians(ang - 90)
        thick_line(
            d,
            (50 * sc + math.cos(rad) * 32 * sc, 40 * sc + math.sin(rad) * 32 * sc),
            (50 * sc + math.cos(rad) * 44 * sc, 40 * sc + math.sin(rad) * 44 * sc),
            max(3 * sc, 2),
            ORANGE,
        )
    d.ellipse([22 * sc, 10 * sc, 78 * sc, 66 * sc], fill=YELLOW)
    d.polygon(
        [(38 * sc, 58 * sc), (62 * sc, 58 * sc), (58 * sc, 70 * sc), (42 * sc, 70 * sc)],
        fill=YELLOW,
    )
    d.rounded_rectangle([40 * sc, 68 * sc, 60 * sc, 82 * sc], radius=3 * sc, fill=SOFT)
    d.rounded_rectangle([42 * sc, 82 * sc, 58 * sc, 90 * sc], radius=3 * sc, fill=GRAY)
    thick_line(d, (42 * sc, 38 * sc), (50 * sc, 50 * sc), max(3 * sc, 2), ORANGE)
    thick_line(d, (58 * sc, 38 * sc), (50 * sc, 50 * sc), max(3 * sc, 2), ORANGE)


def draw_lol(im, s):
    d = ImageDraw.Draw(im)
    sc = s / 100
    d.ellipse([4 * sc, 4 * sc, 96 * sc, 96 * sc], fill=YELLOW)
    thick_line(d, (22 * sc, 40 * sc), (34 * sc, 32 * sc), max(4 * sc, 2), INK)
    thick_line(d, (34 * sc, 32 * sc), (46 * sc, 40 * sc), max(4 * sc, 2), INK)
    thick_line(d, (54 * sc, 40 * sc), (66 * sc, 32 * sc), max(4 * sc, 2), INK)
    thick_line(d, (66 * sc, 32 * sc), (78 * sc, 40 * sc), max(4 * sc, 2), INK)
    d.ellipse([24 * sc, 48 * sc, 76 * sc, 86 * sc], fill=INK)
    d.ellipse([34 * sc, 64 * sc, 66 * sc, 84 * sc], fill=CORAL)
    d.ellipse([10 * sc, 44 * sc, 22 * sc, 62 * sc], fill=SKY)
    d.ellipse([78 * sc, 44 * sc, 90 * sc, 62 * sc], fill=SKY)


def draw_star(im, s):
    d = ImageDraw.Draw(im)
    sc = s / 100
    cx, cy = 50 * sc, 52 * sc
    outer, inner = 44 * sc, 18 * sc
    pts = []
    for i in range(10):
        ang = math.radians(-90 + i * 36)
        r = outer if i % 2 == 0 else inner
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    d.polygon(pts, fill=GOLD)
    circle(d, cx, cy - 2 * sc, 8 * sc, (255, 230, 140, 200))


def draw_pin(im, s):
    d = ImageDraw.Draw(im)
    sc = s / 100
    d.ellipse([20 * sc, 8 * sc, 80 * sc, 68 * sc], fill=CORAL)
    circle(d, 50 * sc, 38 * sc, 12 * sc, WHITE)
    circle(d, 50 * sc, 38 * sc, 6 * sc, CORAL)
    d.polygon([(44 * sc, 62 * sc), (56 * sc, 62 * sc), (50 * sc, 94 * sc)], fill=GRAY)
    d.ellipse([32 * sc, 18 * sc, 44 * sc, 30 * sc], fill=(255, 255, 255, 140))


EMOJIS = [
    ("01-like", draw_like),
    ("02-heart", draw_heart),
    ("03-fire", draw_fire),
    ("04-check", draw_check),
    ("05-cross", draw_cross),
    ("06-clap", draw_clap),
    ("07-think", draw_think),
    ("08-rocket", draw_rocket),
    ("09-idea", draw_idea),
    ("10-lol", draw_lol),
    ("11-star", draw_star),
    ("12-pin", draw_pin),
]


def main():
    for name, fn in EMOJIS:
        save_both(name, fn)
        print("wrote", name)
    print(f"Done: {len(EMOJIS)} emojis → {OUT100} and {OUT512}")


if __name__ == "__main__":
    main()
