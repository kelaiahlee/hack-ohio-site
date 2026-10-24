from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, Response, UploadFile

from app.config import ALLOWED_IMAGE_TYPES, MAX_IMAGE_BYTES
from app.db import jobs_repo
from app.db.connections import get_db
from app.services import pipeline
from app.utils.hashing import sha256_bytes
from app.utils.images import shrink

router = APIRouter()


@router.post("", status_code=202)
async def create_job(file: UploadFile, background: BackgroundTasks, db=Depends(get_db)):
    if file.content_type not in ALLOWED_IMAGE_TYPES:
        raise HTTPException(400, f"Unsupported type. Use one of: {sorted(ALLOWED_IMAGE_TYPES)}")

    data = await file.read()
    if len(data) > MAX_IMAGE_BYTES:
        raise HTTPException(413, "Image too large")

    image_hash = sha256_bytes(data)

    cached = jobs_repo.find_done_by_hash(db, image_hash)
    if cached:
        return {"job_id": cached["id"], "status": "done", "cached": True}

    try:
        small, content_type = shrink(data)
    except ValueError as exc:
        raise HTTPException(400, str(exc))

    job_id = jobs_repo.create_job(db, image_hash, small, content_type)
    background.add_task(pipeline.run, job_id)
    return {"job_id": job_id, "status": "pending", "cached": False}


@router.get("/{job_id}")
def get_job(job_id: str, db=Depends(get_db)):
    row = jobs_repo.get_job_summary(db, job_id)
    if row is None:
        raise HTTPException(404, "Job not found")
    return dict(row)


@router.get("/{job_id}/image")
def get_image(job_id: str, db=Depends(get_db)):
    row = jobs_repo.get_image(db, job_id)
    if row is None:
        raise HTTPException(404, "Image not found")
    return Response(content=row["data"], media_type=row["content_type"])


@router.get("/{job_id}/audio")
def get_audio(job_id: str, db=Depends(get_db)):
    row = jobs_repo.get_audio(db, job_id)
    if row is None:
        raise HTTPException(404, "Audio not ready")
    return Response(content=row["data"], media_type=row["content_type"])