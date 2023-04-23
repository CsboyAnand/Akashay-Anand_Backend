# SteelEye
# API Developer Assessment

from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List, Set
import datetime as dt
from datetime import datetime
import random as rd
# from elasticsearch import Elasticsearch

#//////////////////////////////////////////////////////////////////////////////
# instance of module

app = FastAPI()

#//////////////////////////////////////////////////////////////////////////////
# DB Models
class TradeDetails(BaseModel):
    buySellIndicator: str = Field(description="A value of BUY for buys, SELL for sells.")
    price: float = Field(description="The price of the Trade.")
    quantity: int = Field(description="The amount of units traded.")

class Trade(BaseModel):
    trade_id: str = Field(alias="tradeId", default=None, description="The unique ID of the trade")
    trader: str = Field(description="The name of the Trader")
    asset_class: Optional[str] = Field(alias="assetClass", default=None, description="The asset class of the instrument traded. E.g. Bond, Equity, FX...etc")
    counterparty: Optional[str] = Field(default=None, description="The counterparty the trade was executed with. May not always be available")
    instrument_id: str = Field(alias="instrumentId", description="The ISIN/ID of the instrument traded. E.g. TSLA, AAPL, AMZN...etc")
    instrument_name: str = Field(alias="instrumentName", description="The name of the instrument traded.")
    trade_date_time: dt.datetime = Field(alias="tradeDateTime", description="The date-time the Trade was executed")
    trade_details: TradeDetails = Field(alias="tradeDetails", description="The details of the trade, i.e. price, quantity")

#........ Mock Database 
DBmock = [
    {
        "trade_id": "1",
        "trader": "Akashay Anand",
        "asset_class": "Equity",
        "counterparty": "Zerodha",
        "instrument_id": "TSLA",
        "instrument_name": "Tesla Inc.",
        "trade_date_time": dt.datetime(2023, 4, 20, 12, 0, 0),
        "trade_details": {
            "buySellIndicator": "BUY",
            "price": 110.0,
            "quantity": 1000
        }
    },
    {
        "trade_id": "2",
        "trader": "Auysh",
        "asset_class": "Equity",
        "counterparty": "Narnolia",
        "instrument_id": "AAPL",
        "instrument_name": "Apple Inc.",
        "trade_date_time": dt.datetime(2023, 4, 19, 11, 30, 0),
        "trade_details": {
            "buySellIndicator": "BUY",
            "price": 170.0,
            "quantity": 1000
        }
    },
    {
        "trade_id": "3",
        "trader": "Shruti",
        "asset_class": "Equity",
        "counterparty": "UPStox",
        "instrument_id": "AMZN",
        "instrument_name": "Amazon.com, Inc.",
        "trade_date_time": dt.datetime(2023, 4, 21, 13, 0, 0),
        "trade_details": {
            "buySellIndicator": "SELL",
            "price": 50.0,
            "quantity": 500
        }
    },
    {
        "trade_id": "4",
        "trader": "Pooja",
        "asset_class": "Equity",
        "counterparty": "UPStox",
        "instrument_id": "AMZN",
        "instrument_name": "Amazon.com, Inc.",
        "trade_date_time": dt.datetime(2023, 4, 22, 13, 0, 0),
        "trade_details": {
            "buySellIndicator": "BUY",
            "price": 55.0,
            "quantity": 400
        }
    }
]

#/////////////////////////////////////////////////////////////////////////////
# Routes / End Point


#////// Root path ////
@app.get('/')
def fun():
    return 'hello world // API Assingment // this API will retun data based on url'

  
#//// All List of Trade ///
@app.get("/trades")
async def Listing_trades():
    return DBmock

  
@app.get("/trades/{trade_id}")
async def Single_trade(trade_id: str):
    for trade in DBmock :
        if trade["trade_id"] == trade_id:
            return trade
    raise HTTPException(status_code=404, detail="Trade not found")

    
#///// Searching trades ////
@app.get("/filter")
async def Search_trades(search: Optional[str] = None):
    # return "hello"
    if search is None:
        return "Please provide search string through url  ex: http://127.0.0.1:8000/trades/filter?search=bob%20smith"
    else:
        filtered_trades = []
        for trade in DBmock:
            if (search.lower() in trade.get("counterparty", "").lower() 
                or search.lower() in trade.get("instrument_id", "").lower()
                or search.lower() in trade.get("instrument_name", "").lower()
                or search.lower() in trade.get("trader", "").lower()):
                filtered_trades.append(trade)
        return filtered_trades

#////// Advance filtering ////
@app.get("/Advfilter")
async def get_trades(
    assetClass: Optional[str] = Query(None, description="Asset class of the trade."),
    end: Optional[datetime] = Query(None, description="The maximum date for the tradeDateTime field."),
    maxPrice: Optional[float] = Query(None, description="The maximum value for the tradeDetails.price field."),
    minPrice: Optional[float] = Query(None, description="The minimum value for the tradeDetails.price field."),
    start: Optional[datetime] = Query(None, description="The minimum date for the tradeDateTime field."),
    tradeType: Optional[str] = Query(None, description="The tradeDetails.buySellIndicator is a BUY or SELL")
):
    # return assetClass
    # filtered_trades = DBmock.copy()
    filtered_trades = []

    # filter by asset class
    if assetClass:
        for trade in DBmock:
            if (assetClass.lower() in trade.get("asset_class", "").lower() ):
                filtered_trades.append(trade)
    
    # filter by end date // having doubt in its implementation // so commenting it for now
    # if end:
    #     for trade in DBmock:
    #         if (end >= trade.get("", "") ):
    #             filtered_trades.append(trade)

    # filter by min and max price
    if maxPrice:
        for trade in DBmock:
            if (maxPrice >= trade.get("trade_details.price", "") ):
                filtered_trades.append(trade)

    if minPrice:
        for trade in DBmock:
            if (maxPrice <= trade.get("trade_details.price", "") ):
                filtered_trades.append(trade)

    # filter by start date
    if start:
        for trade in DBmock:
            if (start <= trade.get("trade_date_time", "") ):
                filtered_trades.append(trade)

    # filter by trade type
    if tradeType:
        for trade in DBmock:
            if (tradeType.lower() in trade.get("trade_details.buySellIndicator", "").lower() ):
                filtered_trades.append(trade)        


    return filtered_trades

# ///////////////////////////////////////////////////////

