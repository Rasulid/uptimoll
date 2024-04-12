import os
import shutil
import uuid

from fastapi import UploadFile, File


async def upload_img(img: UploadFile = File(...)):
    img.filename = f"{uuid.uuid4()}.jpg"
    with open(f"static/image/{img.filename}", "wb") as buffer:
        shutil.copyfileobj(img.file, buffer)
    return img.filename


async def delete_old_image(image_name: str):
    if image_name:
        old_image_path = os.path.join("static", "image", image_name)
        if os.path.exists(old_image_path):
            os.remove(old_image_path)
