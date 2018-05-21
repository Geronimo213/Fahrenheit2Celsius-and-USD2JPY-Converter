import os.path
from pathlib import Path
import urllib.request
import json
from math import floor
rates = json.load(urllib.request.urlopen(
    "https://openexchangerates.org/api/latest.json?app_id=b1755bf091904bb195771e4dd874c356&symbols=JPY"))

EXCHANGE_RATE = float(rates.get("rates").get("JPY")) #Get rate from internet
rate_file_path = Path("rate.dat")


def f2c():
    x = int(input("What is the temperature in fahrenheit?\n"))
    celsius = (x-32) * (5/9)
    return celsius


def c2f():
    x = int(input("What is the temperature in celsius?\n"))
    fahrenheit = x * (9/5) + 32
    return fahrenheit


def usd2jpy():
    x = float(input("What is the amount of USD?\n"))
    jpy = EXCHANGE_RATE * x
    jpy = floor(jpy * 100) / 100.0
    return jpy


def jpy2usd():
    x = float(input("What is the amount of JPY?\n"))
    usd = x / EXCHANGE_RATE
    usd = floor(usd * 100) / 100.0
    return usd
