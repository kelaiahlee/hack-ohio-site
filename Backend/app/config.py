import os
import pathlib as path
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass
BASE_DIR = path.Path(__file__).resolve().parent.parent

# One SQLite file. SQLTools / SQLite Viewer in VS Code point at this path.
DB_PATH = path.Path(os.getenv("DB_PATH", BASE_DIR / "data" / "app.db"))

MAX_IMAGE_BYTES = int(os.getenv("MAX_IMAGE_MB", "10")) * 1024 * 1024
ALLOWED_IMAGE_TYPES = {"image/jpeg", "image/png", "image/webp"}

# Images are shrunk before storing (smaller DB, cheaper vision calls)
IMAGE_MAX_SIDE = int(os.getenv("IMAGE_MAX_SIDE", "1024"))

VISION_API_KEY = os.getenv("VISION_API_KEY", "")
AUDIO_API_KEY = os.getenv("AUDIO_API_KEY", "")