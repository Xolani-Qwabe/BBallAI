# app/services/player_service.py
from server.models.player import PlayerIn, PlayerOut
from server.data_store.mongodb import db

def create_player(player_in: PlayerIn) -> PlayerOut:
    player = db.players.insert_one(player_in.dict())
    return PlayerOut(**db.players.find_one({"_id": player.inserted_id}))

def get_player_by_id(player_id: str) -> PlayerOut:
    return PlayerOut(**db.players.find_one({"player_id": player_id}))
