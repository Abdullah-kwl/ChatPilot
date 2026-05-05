from pydantic import BaseModel
from dataclasses import dataclass
from pydantic_settings import BaseSettings, SettingsConfigDict

class Secrets(BaseSettings):
    GROQ_API_KEY: str
    GEMINI_API_KEY: str

    # load vars from .env file
    model_config = SettingsConfigDict(env_file=".env",
                                      env_file_encoding="utf-8",
                                      case_sensitive=True,
                                      extra="ignore")
    

class OtherConfig(BaseModel):
  foo: str = 'bar'


@dataclass
class Config:
    model: str = "llama-3.3-70b-versatile"
    temperature: float = 0.7
    max_tokens: int = 1000

secrets = Secrets()
config = Config()
other = OtherConfig()


# if __name__ == "__main__":
#     print(secrets.GROQ_API_KEY)
#     print(secrets.GEMINI_API_KEY)
#     print(config.model)
#     print(other.foo)