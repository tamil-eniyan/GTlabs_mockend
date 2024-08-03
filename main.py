from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import os
import json

app = FastAPI()

# Assuming the JSON files are in a directory named "json_data" at the same level as the script
JSON_DIR = os.path.join(os.path.dirname(__file__), "json_data")

@app.get("/")
def read_root():
    return {"message": "Welcome to the GTLabs mockend server!"}

@app.get("/json/{filename}")
def read_json(filename: str):
    file_path = os.path.join(JSON_DIR, f"{filename}.json")
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    with open(file_path, "r") as json_file:
        data = json.load(json_file)
    return JSONResponse(content=data)
