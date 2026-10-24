"""Background job: image -> prompt -> sound, with status tracked in the database."""
from app.db import jobs_repo
from app.db.connections import get_connection
from app.services import audio, vision


def run(job_id: str) -> None:
    conn = get_connection()  # its own connection: the request's one is closed by now
    try:
        jobs_repo.set_processing(conn, job_id)

        image = jobs_repo.get_image(conn, job_id)
        prompt = vision.describe(image["data"])
        jobs_repo.set_prompt(conn, job_id, prompt)

        sound_bytes, content_type = audio.generate(prompt)
        jobs_repo.save_audio(conn, job_id, sound_bytes, content_type)
    except Exception as exc:  # never leave a job stuck in 'processing'
        jobs_repo.mark_failed(conn, job_id, str(exc))
    finally:
        conn.close()