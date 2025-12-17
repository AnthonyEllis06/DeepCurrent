from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import yfinance as yf
import finnhub
import pandas as pd
import os
import sys
import importlib.util
import inspect
from CartridgeInterface import IndicatorCartridge

# init fast api
app = FastAPI(title="DeepCurrent Backend API")

# init finnhub client
finnhub_client = finnhub.Client(api_key=os.getenv("FINNHUB_API_KEY"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CARTRIDGE_DIR = "./cartridges"

@app.get("/")
def health_check():
    key_status = "Loaded" if os.getenv("FINNHUB_API_KEY") else "Missing"
    return {"status": "DeepCurrent Online", "FINNHUB_API_KEY": key_status}