import streamlit as st
from random import randint as ri
def coin_game():
  st.markdown("# Coin Fliper 🪙")
  coi = ri(1,2)
  coin_faces = {1:"Heads", 2:"Tails"}
  st.markdown(f"{coin_faces[coi]}")
  st.button("Flip Again")
