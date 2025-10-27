# Battlesnake Python Starter Project

## Overview
This is a Battlesnake starter project written in Python using Flask. Battlesnake is a multiplayer programming game where you code a snake to compete against others. This API server responds to game events and controls snake behavior.

**Current State**: Fully configured and running in Replit environment on port 5000.

## Recent Changes (October 27, 2025)
- Imported from GitHub repository
- Installed Python 3.11 and Flask dependencies
- Modified server.py to use port 5000 (Replit requirement)
- Set up workflow "Battlesnake Server" to run `python main.py`
- Updated .gitignore to exclude Python cache and library files

## Project Architecture

### File Structure
- `main.py` - Core Battlesnake logic (info, start, move, end handlers)
- `server.py` - Flask web server that hosts the API endpoints
- `requirements.txt` - Python dependencies (Flask==2.3.2)

### API Endpoints
- `GET /` - Returns snake configuration (color, head, tail style)
- `POST /start` - Called when game starts
- `POST /move` - Called each turn to get snake's next move
- `POST /end` - Called when game ends

### How It Works
The Battlesnake game engine sends HTTP requests to your server. The snake logic in `main.py` processes game state and returns moves (up, down, left, right).

## Running Locally
The workflow "Battlesnake Server" is configured to start automatically. The server runs on port 5000 and can be accessed via the Replit webview.

## Next Steps
- Customize snake appearance in the `info()` function
- Improve snake logic to avoid walls and other snakes
- Add food-seeking behavior to survive longer
- Test at [play.battlesnake.com](https://play.battlesnake.com)
