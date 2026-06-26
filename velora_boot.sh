#!/data/data/com.termux/files/usr/bin/bash

clear

echo "======================================="
echo "         VELORA ENTERPRISE"
echo "======================================="

python node-agent/agent.py

python app.py
