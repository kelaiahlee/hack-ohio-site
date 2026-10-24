"""All SQL for the jobs table lives here. Nothing else writes SQL.

Rule for this file: never SELECT * and never select the BLOB columns unless the
function exists specifically to return them. Each row can hold megabytes.
"""
import uuid


def create_job(conn, image_hash: str, image_bytes: bytes, content_type: str) -> str:
    job_id = str(uuid.uuid4())
    with conn:  # commits on success, rolls back on error
        conn.execute(
            "INSERT INTO jobs (id, image_hash, image_data, image_type) VALUES (?, ?, ?, ?)",
            (job_id, image_hash, image_bytes, content_type),
        )
    return job_id


def get_job_summary(conn, job_id: str):
    """Status info only. Never touches the BLOB columns."""
    return conn.execute(
        """
        SELECT id, status, audio_prompt, error, created_at, finished_at,
               audio_type IS NOT NULL AS has_audio
        FROM jobs
        WHERE id = ?
        """,
        (job_id,),
    ).fetchone()


def find_done_by_hash(conn, image_hash: str):
    """Cache lookup: an earlier finished job for the same image."""
    return conn.execute(
        "SELECT id FROM jobs WHERE image_hash = ? AND status = 'done' LIMIT 1",
        (image_hash,),
    ).fetchone()


def get_image(conn, job_id: str):
    # AS data / AS content_type keeps the same keys the router and pipeline already use
    return conn.execute(
        "SELECT image_data AS data, image_type AS content_type FROM jobs WHERE id = ?",
        (job_id,),
    ).fetchone()


def get_audio(conn, job_id: str):
    # Returns None until the sound exists, which the router turns into a 404
    return conn.execute(
        """
        SELECT audio_data AS data, audio_type AS content_type
        FROM jobs
        WHERE id = ? AND audio_data IS NOT NULL
        """,
        (job_id,),
    ).fetchone()


def set_processing(conn, job_id: str) -> None:
    with conn:
        conn.execute("UPDATE jobs SET status = 'processing' WHERE id = ?", (job_id,))


def set_prompt(conn, job_id: str, prompt: str) -> None:
    with conn:
        conn.execute("UPDATE jobs SET audio_prompt = ? WHERE id = ?", (prompt, job_id))


def save_audio(conn, job_id: str, audio_bytes: bytes, content_type: str) -> None:
    """Store the sound and mark the job done in a single UPDATE."""
    with conn:
        conn.execute(
            """
            UPDATE jobs
            SET audio_data = ?, audio_type = ?, status = 'done', finished_at = CURRENT_TIMESTAMP
            WHERE id = ?
            """,
            (audio_bytes, content_type, job_id),
        )


def mark_failed(conn, job_id: str, error: str) -> None:
    with conn:
        conn.execute(
            "UPDATE jobs SET status = 'failed', error = ?, finished_at = CURRENT_TIMESTAMP WHERE id = ?",
            (error, job_id),
        )