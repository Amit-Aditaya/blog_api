#!/bin/bash
gunicorn -k uvicorn.workers.UvicornWorker blog.main:app --bind 0.0.0.0:$PORT
