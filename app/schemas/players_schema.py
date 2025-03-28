from pydantic import BaseModel

class PlayersBase(BaseModel):
    name: str
    email:str
    password:str
    phone:str
    
class PlayersCreate(PlayersBase):
    pass

class PlayersOut(PlayersBase):
    id: int
    class Config:
        orm_mode = True    