from core.models.config import Config
import toml
import os

class ConfigManager:
    """
    ConfigManager is responsible for loading and managing the configuration settings.
    It uses the Pydantic model to validate the configuration data.
    """

    def __init__(self, config: Config):
        self.config = config

    def get_config(self) -> Config:
        return self.config
    
    def set_config(self, config: Config) -> None:
        """
        Set a new configuration.
        :param config: New configuration to set.
        """
        self.config = config

def create_config():
    config_path = os.path.join(os.path.dirname(__file__), '../../config.toml')
    if os.path.exists(config_path):
        with open(config_path, 'r', encoding='utf-8') as file:
            try:
                config_data = toml.load(file)
                return Config(**config_data)
            except toml.TomlDecodeError as e:
                raise ValueError(f"Error decoding TOML file: {e}")
    else:
        raise FileNotFoundError(f"Config file not found at {config_path}")