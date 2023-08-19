#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = Int(os.environ.get("16950780"))

API_HASH = os.environ.get("b2cc1795a8537e3e848fa8d0cb1fd503")

BOT_TOKEN = os.environ.get("6306004178:AAHzRxpdw2LO1qJYqOZxGDrSzaVCW2cwrIQ")

DB_URI = os.environ.get("mongodb+srv://nyinyit279:123nyiynit279@cluster0.vjisd19.mongodb.net/?retryWrites=true&w=majority")

USER_SESSION = os.environ.get("BQECpfwAP6OQBs4q5ov8iMgOlB3ptQC8gnG7fM9X9qvUJgnwASGyvC3Tb92lKzJDpg1SAMTKzNirNolIP8DJzBgTr5Mnqslqzig6PKXHMZaE32DNvXE1a8zMZzeWy-zoP098Yjrs_oBf5X8rDzfdNh2iR5BRpLmNZPHy0FI0RGPme31U6Kk6AwsISxgLenkz5SCxpIWlERHnVLJQLJ_Ggzgn-dbw5isgqs2_2lZ3TlLyfkUpNbYlsUg9266XaGreE5uYBGe298mZ3FKE8sdfq5e9q2lfv5SR-x0-P0AloYoTZlUWFozvf6cnSJY77FErPvgD8WZTyQqAUxu9JX_xbI2FKsVixAAAAABp7VTbAA")

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
