# app/main.py
import sys
import os

# プロジェクトのルートディレクトリをモジュール検索パスに追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import uvicorn
from fastapi import FastAPI
from src.api.endpoints.router import create_router
from src.frameworks.config.config_manager import create_config, ConfigManager
from src.frameworks.start_dofbot import start_dofbot

app = FastAPI()
config = create_config()
config_manager = ConfigManager(config).set_config(config)

create_router(app)
start_dofbot(ConfigManager.get_config())

if __name__ == "__main__":
    # ポート6001でサーバーを起動
    try:
        uvicorn.run("src.main:app", host="localhost", port=6001, reload=True)
    except KeyboardInterrupt:
        print("Server stopped.")