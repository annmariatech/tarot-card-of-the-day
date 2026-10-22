# 🔮 Tarot Card of the Day 

Every day, one card. Same card all day. No refunds, no rerolls, no arguing with the Tower.

---

## 🪄 What does it do?

1. Calls a tarot API and politely asks for all 78 cards
2. Uses today's date as a random seed (so the cosmos stays consistent until midnight)
3. Picks one card and flips a coin to decide if it's upright or reversed
4. Draws it in a fancy coloured box in your terminal, because we have standards

Green border = upright = the universe likes you today.
Red border = reversed = the universe is *complicated* today.

## 🧙 Installation

```bash
pip install requests rich
```


## 🃏 Usage

```bash
python tarot.py
```

Run it again five minutes later and you'll get the **same card**. The card does not care that you didn't like it. Come back tomorrow.


## Troubleshooting

**"Couldn't reach the tarot API"**\
Either your Wi-Fi is down or Mercury is in retrograde. Check the Wi-Fi first.

**`KeyError: 'meaning_up'`**\
The API changed its field names without telling anyone. Rude. Add `print(cards[0])` after fetching, look at the real keys, and update the code.

**I got The Tower and I'm upset**\
Brace yourself. That's all

**I want a different card**\
Remove the seed. But you'll know what you did.


## Disclaimer

This program is for fun. Please do not quit your job, text your ex, or adopt seven cats because of a Python script. (Adopting one cat is fine.)
