import uuid

from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session

from database import get_db
from middleware.auth_middleware import auth_middleware
import cloudinary
import cloudinary.uploader

router = APIRouter()


@router.post('/upload', status_code=201)
def upload_song(song: UploadFile = File(...),
                thumbnail: UploadFile = File(...),
                artist: str = Form(...),
                song_name: str = Form(...),
                hex_code: str = Form(...),
                db: Session = Depends(get_db),
                auth_dict=Depends(auth_middleware)):
    song_id = str(uuid.uuid4())
    print(song_id)
    song_res = cloudinary.uploader.upload(song.file, resource_type='auto', folder=f'songs/{song_id}')
    print(song_res['url'])
    thumbnail_res = cloudinary.uploader.upload(thumbnail.file, resource_type='image', folder=f'songs/{song_id}')
    print(thumbnail_res['url'])
    # store data in db
    return 'ok'
