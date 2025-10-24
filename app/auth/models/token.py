from pydantic import BaseModel

class Token(BaseModel):
    access_token : str
    token_type : str
    
#Store inside the JWT
class TokenData(BaseModel):
    email : str | None = None