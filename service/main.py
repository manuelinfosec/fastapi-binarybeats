from colorama import init

# from database import setup_database
from dotenv import load_dotenv
from fastapi import FastAPI

# add terminal color
init()
load_dotenv()


# create fastapi instance
app = FastAPI()


# acquire and dispose database connection
# setup_database(app)


@app.get("/")
def index():
    """Base endpoint"""
    # return {"message": "API Works!"}
