from typing import Union

from fastapi import FastAPI
import scraper

app = FastAPI()


@app.get("/")
async def root():
    return {"Zexsys API Version": "2.0.3"}

@app.get("/gpa/")
async def read_credentials(username: str, password: str):
    return {"gpa": f"{scraper.getgpa(username, password)}"}

@app.get("/gradeinfo/")
async def read_credentials(username: str, password: str):
    return scraper.getgradeinfo(username, password)