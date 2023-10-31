from typing import Union

from fastapi import FastAPI
import scraper

app = FastAPI()


@app.get("/")
async def root():
    return {"Zexsys": "ALMABOT API OOP"}

@app.get("/gpa/")
async def read_credentials(username: str, password: str):
    return {"GPA": scraper.getgpa(username, password)}
