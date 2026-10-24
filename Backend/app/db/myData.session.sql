CREATE TABLE IF NOT EXISTS jobs (
    id           TEXT PRIMARY KEY,
    image_hash   TEXT NOT NULL,
    image_path   TEXT NOT NULL,
    status       TEXT NOT NULL DEFAULT 'pending',
    audio_prompt TEXT,
    audio_path   TEXT,
    error        TEXT,
    created_at   TEXT DEFAULT CURRENT_TIMESTAMP,
    finished_at  TEXT
);

CREATE INDEX IF NOT EXISTS idx_jobs_hash ON jobs(image_hash);