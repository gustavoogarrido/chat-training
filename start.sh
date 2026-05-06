#!/bin/bash

# Iniciar o backend em background
uvicorn src.app.main:app --host 0.0.0.0 --port 8000 --reload &

# Iniciar o frontend no processo principal
streamlit run src/ui.py --server.port=8501 --server.address=0.0.0.0
