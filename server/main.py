# app/main.py
from fastapi import FastAPI
from server.handlers import (
    player_handler,
    team_handler,
    game_handler,
    prediction_handler,
    matchup_handler,
    team_news_handler,
    injury_handler,
    form_trend_handler,
)

app = FastAPI()

# Include handlers for each entity
app.include_router(player_handler.router)
app.include_router(team_handler.router)
app.include_router(game_handler.router)
app.include_router(prediction_handler.router)
app.include_router(matchup_handler.router)
app.include_router(team_news_handler.router)
app.include_router(injury_handler.router)
app.include_router(form_trend_handler.router)
