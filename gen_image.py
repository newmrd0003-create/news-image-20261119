#!/usr/bin/env python3
"""THE WORLD -- front page for Thursday 19 November 2026.

Draws entry.png (1024 x 1024) with Pillow only. No external images,
no network, no randomness and no timestamps: the same input always
produces the same output bytes.

Layout: dateline, masthead, one full-width lead story, then a
two-column grid with the remaining five stories, and a footer rule.
"""

import os

from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1024, 1024
PAPER = (247, 243, 232)
INK = (22, 22, 22)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

MARGIN = 44
CONTENT_RIGHT = WIDTH - MARGIN
FIT_LIMIT = 976


def load(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, font, width):
    """Greedy word wrap measured with the real font; deterministic."""
    lines = []
    current = ""
    for word in text.split():
        trial = word if not current else current + " " + word
        if draw.textlength(trial, font=font) <= width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_lines(draw, x, y, text, font, width, leading, align="left"):
    """Draw wrapped text; return the y coordinate below the block."""
    for line in wrap(draw, text, font, width):
        if align == "center":
            lx = x + (width - draw.textlength(line, font=font)) / 2.0
        else:
            lx = x
        draw.text((lx, y), line, font=font, fill=INK)
        y += leading
    return y


def rule(draw, x0, x1, y, weight=2):
    draw.line([(x0, y), (x1, y)], fill=INK, width=weight)


def draw_kicker(draw, x, y, text, size=14):
    font = load(SANS_BOLD, size)
    draw.text((x, y), text, font=font, fill=INK)
    return y + size + 6


def draw_story(draw, x, y, width, kicker, headline, body,
               head_size=26, body_size=16):
    """One grid story: kicker, headline, standfirst. Returns bottom y."""
    y = draw_kicker(draw, x, y, kicker)
    head_font = load(SERIF_BOLD, head_size)
    y = draw_lines(draw, x, y, headline, head_font, width, head_size + 7)
    y += 4
    body_font = load(SERIF, body_size)
    y = draw_lines(draw, x, y, body, body_font, width, body_size + 4)
    return y


# --- Verified stories for 19 November 2026 (checked 19 Nov 2026) ---

LEAD_KICKER = "APEC SUMMIT — SHENZHEN"
LEAD_HEADLINE = "TRUMP, XI AND PUTIN IN FIRST TRILATERAL SUMMIT"
LEAD_BODY = (
    "The leaders of the United States, China and Russia meet in Shenzhen "
    "on Thursday, on the sidelines of the APEC summit, for the first "
    "three-way talks of their kind. Trump said he would raise nuclear "
    "arms cuts, but no deal was expected."
)

GRID_STORIES_LEFT = [
    (
        "GAMES",
        "GTA VI ROLLS OUT AFTER 13-YEAR WAIT",
        "Grand Theft Auto VI launches at midnight on Thursday for "
        "PlayStation 5 and Xbox Series X|S, returning players to Vice "
        "City in Leonida.",
    ),
    (
        "WASHINGTON",
        "JEFFRIES NOMINATED FOR SPEAKER IN 251-11 VOTE",
        "House Democrats nominated Hakeem Jeffries on Wednesday to be "
        "Speaker, in a closed-door vote of 251 to 11. He would be the "
        "first Black American to hold the gavel.",
    ),
]

GRID_STORIES_RIGHT = [
    (
        "WEATHER — BAY OF BENGAL",
        "CYCLONE AKVAN NEARS INDIA'S EAST COAST",
        "Cyclone Akvan nears India's east coast. Landfall is due between "
        "Narsapur and Puri by noon on Friday, with winds of 90–100 km/h "
        "gusting to 110 km/h.",
    ),
    (
        "SPACE",
        "VOYAGER 1, A FULL LIGHT-DAY FROM HOME",
        "Voyager 1 crossed one light-day from Earth on Wednesday — 25.9 "
        "billion kilometres, a first for any human-made object. A radio "
        "signal now takes 24 hours to reach it.",
    ),
    (
        "BRUSSELS",
        "EU PLANS €45BN LOAN FOR UKRAINE",
        "Brussels proposed a €45bn loan to Ukraine on Wednesday, "
        "covering two-thirds of Kyiv's €70bn gap. Kyiv repays only "
        "once Russia pays reparations.",
    ),
]


def build():
    img = Image.new("RGB", (WIDTH, HEIGHT), PAPER)
    draw = ImageDraw.Draw(img)

    # Outer frame.
    draw.rectangle([14, 14, WIDTH - 15, HEIGHT - 15], outline=INK, width=3)

    # Dateline row.
    date_font = load(SANS_BOLD, 15)
    draw.text((MARGIN, 30), "THURSDAY, 19 NOVEMBER 2026",
              font=date_font, fill=INK)
    issue = "No. 323"
    draw.text((CONTENT_RIGHT - draw.textlength(issue, font=date_font), 30),
              issue, font=date_font, fill=INK)
    rule(draw, MARGIN, CONTENT_RIGHT, 56)

    # Masthead.
    mast_font = load(SERIF_BOLD, 96)
    draw.text((WIDTH // 2, 62), "THE WORLD", font=mast_font, fill=INK,
              anchor="ma")
    tag_font = load(SANS, 14)
    draw.text((WIDTH // 2, 158), "T H E   D A Y   I N   S I X   S T O R I E S",
              font=tag_font, fill=INK, anchor="ma")
    rule(draw, MARGIN, CONTENT_RIGHT, 184)
    rule(draw, MARGIN, CONTENT_RIGHT, 189)

    # Lead story, full width.
    y = 202
    kick_font = load(SANS_BOLD, 16)
    draw.text((WIDTH // 2, y), LEAD_KICKER, font=kick_font, fill=INK,
              anchor="ma")
    y += 24
    lead_head_font = load(SERIF_BOLD, 42)
    y = draw_lines(draw, 92, y, LEAD_HEADLINE, lead_head_font, 840, 50,
                   align="center")
    y += 6
    lead_body_font = load(SERIF, 19)
    y = draw_lines(draw, 92, y, LEAD_BODY, lead_body_font, 840, 26)
    y += 12
    rule(draw, MARGIN, CONTENT_RIGHT, y)
    grid_top = y + 14

    # Two-column grid for the other five stories.
    col_w = 456
    left_x = MARGIN
    right_x = WIDTH - MARGIN - col_w

    left_y = grid_top
    for i, (kicker, headline, body) in enumerate(GRID_STORIES_LEFT):
        if i:
            left_y += 12
            rule(draw, left_x, left_x + col_w, left_y)
            left_y += 12
        left_y = draw_story(draw, left_x, left_y, col_w,
                            kicker, headline, body)

    # Classic end mark under the shorter left column.
    end_font = load(SERIF_BOLD, 16)
    draw.text((left_x + col_w // 2, left_y + 18), "— 30 —",
              font=end_font, fill=INK, anchor="ma")

    right_y = grid_top
    for i, (kicker, headline, body) in enumerate(GRID_STORIES_RIGHT):
        if i:
            right_y += 12
            rule(draw, right_x, right_x + col_w, right_y)
            right_y += 12
        right_y = draw_story(draw, right_x, right_y, col_w,
                             kicker, headline, body)

    # Vertical divider between the columns.
    bottom = max(left_y, right_y)
    draw.line([(512, grid_top), (512, bottom)], fill=INK, width=1)

    # Footer.
    rule(draw, MARGIN, CONTENT_RIGHT, 984)
    foot_font = load(SANS, 13)
    draw.text((WIDTH // 2, 992),
              "THE WORLD  •  THURSDAY 19 NOVEMBER 2026  •  "
              "DRAWN ENTIRELY WITH PYTHON & PIL",
              font=foot_font, fill=INK, anchor="ma")

    print("grid_top:", grid_top)
    print("left column bottom:", left_y)
    print("right column bottom:", right_y)
    if bottom > FIT_LIMIT:
        print("WARNING: content bottom", bottom, "exceeds fit limit",
              FIT_LIMIT)
    return img


def main():
    img = build()
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "entry.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
