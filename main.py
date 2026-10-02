import streamlit as st
from random import randint as ri
from dice import dice_game
from rps import rps_game
from rand import rand_game
st.markdown("# Random Games!!")
# 🎲
# ✂️
# 🎰
sb = st.sidebar
pages=[
  "Rock Paper Scisssor ✂️",
  "Dice Roller 🎲"
  "Randomizer 🎰"
]
sb.title("Navigation")
rd = sb.radio("Which Game To Play", options=pages)
if rd == "Rock Paper Scisssor ✂️":
  rps_game()
elif rd == "Randomizer 🎰":
  rand_game()
else:
  dice_game()
