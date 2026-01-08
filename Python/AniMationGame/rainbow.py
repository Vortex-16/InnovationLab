from rich.console import Console
from rich.text import Text
import time

console = Console()
while True:
    console.print(Text("🌈 AMAZING TERMINAL", style="bold magenta on black"))
    time.sleep(0.5)
    console.clear()
  