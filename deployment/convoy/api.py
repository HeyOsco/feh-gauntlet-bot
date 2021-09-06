# uvicorn api:app --host 0.0.0.0 --port 5057
import json
from config import * # current VG particpants and round dates
from fastapi import FastAPI
from pydantic import BaseModel
from secrets import *

app = FastAPI()

# Request body classes
class Bot(BaseModel):
    name: str
    # description: str = None

@app.get('/health')
def hello():
    """Test endpoint"""
    return {'status': '200'}
    

@app.get('/hello')
def hello():
    """Test endpoint"""
    return {'hello': 'world'}
    
@app.get('/units')
def get_list_of_unit_names():
    data = [round_1_unit_1,
            round_1_unit_2,
            round_1_unit_3,
            round_1_unit_4,
            round_1_unit_5,
            round_1_unit_6,
            round_1_unit_7,
            round_1_unit_8]
    return json.dumps({"unit":[{"name":value} for value in data]})

@app.get('/config/bot/discord/{bot_name}')
def get_config_for_bot_discord(bot_name: str):
    return json.dumps(
        { 
            "name": bot_name, 
            "guild": discord_guild, 
            "prefix": discord_prefix, 
            "status": discord_status[bot_name], 
            "token": DISCORD_TOKEN [bot_name]
        }
        
    )

@app.get('/config/bot/discord/guild/')
def get_guild_for_bot_discord():
    return json.dumps({"guild": discord_guild})

@app.get('/config/bot/discord/prefix')
def get_prefix_for_bot_discord():
    return json.dumps({"prefix": discord_prefix})
    
@app.get('/config/bot/discord/status/{bot_name}')
def get_status_for_bot_discord(bot_name: str):
    return json.dumps({"status": discord_status[bot_name]})

@app.get('/config/bot/discord/token/{bot_name}')
def get_token_for_bot_discord(bot_name: str):
    return json.dumps({"token": DISCORD_TOKEN [bot_name]})