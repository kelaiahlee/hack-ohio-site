import io

from PIL import Image, UnidentifiedImageError

from app.config import IMAGE_MAX_SIDE


def shrink(data: bytes) -> tuple[bytes, str]:
    """Resize to IMAGE_MAX_SIDE and re-encode as JPEG. Also validates it's a real image."""
    try:
        img = Image.open(io.BytesIO(data))
        img.load()
    except (UnidentifiedImageError, OSError) as exc:
        raise ValueError("File is not a valid image") from exc

    img = img.convert("RGB")
    img.thumbnail((IMAGE_MAX_SIDE, IMAGE_MAX_SIDE))
    out = io.BytesIO()
    img.save(out, format="JPEG", quality=85)
    return out.getvalue(), "image/jpeg"