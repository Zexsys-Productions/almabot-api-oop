from typing import Union

from fastapi import FastAPI
import scraper
import asyncScraper
import asyncio

app = FastAPI()

@app.get("/")
async def root():
    return {"Zexsys API Version": "2.0.5"}

# from synchronous scraper
@app.get("/gpa")
async def read_credentials(username: str, password: str):
    gpa = await asyncScraper.async_get_gpa(username, password)
    return {"gpa": f"{gpa}"}

# from synchronous scraper
@app.get("/gradeinfo")
async def read_credentials(username: str, password: str):
    return scraper.get_grade_info(username, password)
