import streamlit as st
from random import randint as ri
from dice import dice_game
from rps import rps game
st.markdown("# Random Games!!")
# 🎲
# ✂️

sb = st.sidebar
pages=[
  "Rock Paper Scisssor ✂️",
  "Dice Roller 🎲"
]
sb.title("Navigation")
rd = sb.radio("Which Game To Play", options=pages)
if rd == "Rock Paper Scisssor ✂️":
  rps_game()
else:
  dice_game()
