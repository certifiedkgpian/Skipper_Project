#!/usr/bin/env bash
apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libatlas-base-dev \
    liblapack-dev \
    gfortran

pip install --upgrade pip setuptools wheel
pip install --no-cache-dir -r requirements.txt
