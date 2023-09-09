from typing import List, Optional

from pydantic import BaseModel


    
class LoginSchema(BaseModel):
    email: str
    password: str
