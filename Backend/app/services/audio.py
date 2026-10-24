"""Step 2: text prompt -> sound bytes.

PLACEHOLDER: synthesizes a short WAV tone whose pitch depends on the prompt, using only
the standard library. Replace generate() with a real text-to-audio call (ElevenLabs,
Stable Audio, MusicGen...) that returns (audio_bytes, content_type).
"""
import hashlib
import io
import math
import struct
import wave

SAMPLE_RATE = 22050
DURATION_S = 3


def generate(prompt: str) -> tuple[bytes, str]:
    digest = hashlib.sha256(prompt.encode()).digest()
    freq = 220 + digest[0] * 2          # 220-730 Hz, varies per prompt
    n = SAMPLE_RATE * DURATION_S

    buf = io.BytesIO()
    with wave.open(buf, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SAMPLE_RATE)
        frames = bytearray()
        for i in range(n):
            fade = min(1.0, i / 2000, (n - i) / 2000)   # avoid clicks at start/end
            sample = int(12000 * fade * math.sin(2 * math.pi * freq * i / SAMPLE_RATE))
            frames += struct.pack("<h", sample)
        w.writeframes(bytes(frames))
    return buf.getvalue(), "audio/wav"