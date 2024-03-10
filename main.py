from typing import Union

from fastapi import FastAPI
import scraper
import asyncScraper

app = FastAPI()

@app.get("/")
async def root():
    return {"Zexsys API Version": "2.0.4"}

# from synchronous scraper
@app.get("/gpa/")
async def read_credentials(username: str, password: str):
    return {"gpa": f"{asyncScraper.async_get_gpa(username, password)}"}

# from synchronous scraper
@app.get("/gradeinfo/")
async def read_credentials(username: str, password: str):
    return scraper.getgradeinfo(username, password)