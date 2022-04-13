from pathlib import Path
from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    skill_name: Optional[str]
    private_key_path: Path = 'id_rsa.pem'
    public_key_path: Path = 'id_rsa.pub'
    secret: Optional[str]
    use_encryption: bool = True
    log_level: str = 'INFO'
    app_dir: Optional[str] = None

    class Config:
        env_prefix = 'SKILLS_'
        env_file = '.env'
