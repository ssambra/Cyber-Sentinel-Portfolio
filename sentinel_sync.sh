#!/bin/bash
cd ~/Sovereign-Sentinel-Unified
git add .
git commit -m "Sentinel Heartbeat: Autonomous Sync $(date)"
git push origin main
