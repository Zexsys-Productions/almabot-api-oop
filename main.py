from typing import Union

from fastapi import FastAPI
import scraper

app = FastAPI()


@app.get("/")
async def root():
    return {"Zexsys alma scraper version": "2.0.0"}

@app.get("/gpa/")
async def read_credentials(username: str, password: str):
    return {"GPA": f"{scraper.getgpa(username, password)}"}

@app.get("/gradeinfo/")
async def read_credentials(username: str, password: str):
    return getgradeinfo(username, password)