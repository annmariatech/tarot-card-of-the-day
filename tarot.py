import requests
import random
from datetime import date
from rich.console import Console
from rich.panel import Panel

URL = "https://tarotapi.dev/api/v1/cards"
console = Console()

def fetch_cards():
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    return response.json()["cards"]

def pick_card(cards):
    rng=random.Random(str(date.today()))
    card= rng.choice(cards)
    is_reversed = rng.choice([True, False])
    return card, is_reversed
def show_card(card, is_reversed):
    orientation = "Reversed" if is_reversed else "Upright"
    meaning = card["meaning_rev"] if is_reversed else card["meaning_up"]
    colour = "red" if is_reversed else "green"
    body = f"[bold]{orientation}[/bold]\n\n{meaning}\n\n[dim]{card['desc']}[/dim]"  # [bold] and [dim] are rich markup; \n = new line
    console.print(Panel(body, title=card["name"], subtitle=str(date.today()), border_style=colour))  # draw the box

def main():
    try:
        cards = fetch_cards()
    except requests.RequestException as error: 
        console.print(f"[red]Couldn't reach the tarot API: {error}[/red]")
        return
    card, is_reversed = pick_card(cards)
    show_card(card, is_reversed)
if __name__ == "__main__":
    main()