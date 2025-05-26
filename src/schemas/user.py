from pydantic import BaseModel, EmailStr, constr, field_validator

class UserCreate(BaseModel):
    """Pydantic schema for user signup"""
    email: EmailStr
    password: constr(min_length=8, max_length=128)

    @field_validator("password")
    def validate_password(cls, v):
        if not any(c.isupper() for c in v) or not any(c.isdigit() for c in v):
            raise ValueError("Password must contain at least one uppercase letter and one digit")
        return v

class UserLogin(BaseModel):
    """Pydantic schema for user login"""
    email: EmailStr
    password: constr(min_length=8, max_length=128)
