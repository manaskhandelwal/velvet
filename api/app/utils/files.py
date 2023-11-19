import cloudinary.uploader


async def upload_file(data):
    file = cloudinary.uploader.upload(data)
    return {"url": file.get("secure_url")}
