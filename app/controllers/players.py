from sqlalchemy.orm import Session
from app.models.players import Player
from app.schemas.players_schema import PlayersCreate

def create_player(db: Session, usuario: PlayersCreate):
   pass

def get_players(db: Session):
    pass

def delete_player(db: Session, player_id: int):
    pass

def update_player(db: Session, player_id: int, player: PlayersCreate):
    pass