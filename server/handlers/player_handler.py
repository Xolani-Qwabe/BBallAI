# app/handlers/player_handler.py
from fastapi import APIRouter, HTTPException
from app.services.player_service import create_player, get_player_by_id
from app.models.player import PlayerIn, PlayerOut

router = APIRouter()

@router.post("/players/", response_model=PlayerOut)
async def create_new_player(player_in: PlayerIn):
    player = create_player(player_in)
    if not player:
        raise HTTPException(status_code=400, detail="Failed to create player")
    return player

@router.get("/players/{player_id}/", response_model=PlayerOut)
async def get_player(player_id: str):
    player = get_player_by_id(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player
