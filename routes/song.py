import uuid

from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session

from database import get_db
from middleware.auth_middleware import auth_middleware
import cloudinary
import cloudinary.uploader

router = APIRouter()

cloudinary.config(
    cloud_name="dhzgif8ti",
    api_key="442156838817215",
    api_secret="<your_api_secret>",  # Click 'View API Keys' above to copy your API secret
    secure=True
)


@router.post("/upload")
def upload_song(song: UploadFile = File(...), thumbnail: UploadFile = File(...), artist: str = Form(...),
                song_name: str = Form(...),
                hex_code: str = Form(...), db: Session = Depends(get_db), auth_dict=Depends(auth_middleware)):
    song_id = str(uuid.uuid4())
    song_res = cloudinary.uploader.upload(song.file, resource_type='auto', folder=f'songs/{song_id}')
    print(song_res)
    thumbnail_res = cloudinary.uploader.upload(thumbnail.file, resource_type='image', folder=f'songs/{song_id}')
    print(thumbnail_res)
    # store data in db
    return 'ok'
