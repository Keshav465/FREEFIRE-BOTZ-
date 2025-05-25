import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from main import start_bot

start_bot()
