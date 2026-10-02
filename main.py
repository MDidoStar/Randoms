import streamlit as st
from random import randint as ri
from dice import dice_game
from rps import rps_game
from rand import rand_game
from coin import coin_game


st.set_page_config(
    page_title="Random Games",
    page_icon="🕹️",
    layout="wide",
    initial_sidebar_state="expanded",
    # menu_items={
      #  'Get Help': 'https://extremelycoolapp.com',
       # 'Report a bug': "https://extremelycoolapp.com",
        #'About': "# This is a header\nAnd this is a custom about box!"
    #}
)

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
