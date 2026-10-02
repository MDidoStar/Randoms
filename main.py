import streamlit as st
from random import randint as ri
from dice import dice_game
from rps import rps_game
from rand import rand_game
from coin import coin_game
st.page_config(title="Random Games", icon=🕹️)
st.markdown("# Random Games!!")
# 🎲
# ✂️
# 🎰
# 🪙
sb = st.sidebar
pages=[
  "Rock Paper Scisssor ✂️",
  "Dice Roller 🎲",
  "Randomizer 🎰",
  "Coin Fliper 🪙"
]
sb.title("Navigation")
rd = sb.radio("Which Game To Play", options=pages)
if rd == "Rock Paper Scisssor ✂️":
  rps_game()
elif rd == "Randomizer 🎰":
  rand_game()
elif rd == "Coin Fliper 🪙":
  coin_game()
else:
  dice_game()
