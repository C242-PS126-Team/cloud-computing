from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

SECRET_KEY = 'your_secret_key_here'

# Database setup
DATABASE_URL = "mysql+pymysql://root:password@localhost/truecolor"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Model pengguna
class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)

Base.metadata.create_all(bind=engine)

class User(BaseModel):
    username: str
    password: str

security = HTTPBearer()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route untuk pendaftaran pengguna
@app.post('/register')
def register(user: User, db: SessionLocal = Depends(get_db)):
    existing_user = db.query(UserModel).filter(UserModel.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_password = generate_password_hash(user.password, method='sha256')
    new_user = UserModel(username=user.username, password=hashed_password)
    db.add(new_user)
    db.commit()
    return {"message": "User registered successfully"}

# Route untuk login pengguna
@app.post('/login')
def login(user: User, db: SessionLocal = Depends(get_db)):
    existing_user = db.query(UserModel).filter(UserModel.username == user.username).first()
    if not existing_user or not check_password_hash(existing_user.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    token = jwt.encode({
        'username': user.username, 
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, SECRET_KEY, algorithm='HS256')

    return {"token": token}

# Route untuk validasi token
@app.get('/validate')
def validate(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return {"message": "Token is valid", "user": decoded['username']}
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)