from pydantic import BaseModel
from datetime import datetime

class Postbase(BaseModel):
    
    title : str
    details: str
    creator: str
    image_url: str

class PostBaseDsplay(BaseModel):
    id : int 
    image_url : str
    title : str
    details: str
    creator: str
    timestamp: datetime
    class Config():
        orm_mode = True