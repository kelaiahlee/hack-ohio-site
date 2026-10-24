"""Step 1: image bytes -> text prompt describing the sound to generate.

PLACEHOLDER: derives a prompt from the image's average color and brightness so the
pipeline works with no API key. Replace describe() with a real vision-model call
(Claude, GPT-4o, Gemini...) that returns a short audio prompt, e.g.
"gentle ocean waves, distant seagulls, light wind".
"""
import io

from PIL import Image


def describe(image_bytes: bytes) -> str:
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB").resize((1, 1))
    r, g, b = img.getpixel((0, 0))
    brightness = (r + g + b) / 3

    mood = "bright, airy" if brightness > 150 else "dark, low and rumbling" if brightness < 80 else "calm, mellow"
    dominant = max(("red", r), ("green", g), ("blue", b), key=lambda c: c[1])[0]
    texture = {"red": "warm", "green": "organic", "blue": "cool"}[dominant]
    return f"{mood} {texture} ambient tone (avg color rgb({r},{g},{b}))"