import streamlit as st
from random import randint as ri
def rand_game():
  st.markdown("## Randomizer")
  rand_range = st.number_input("Enter The max number that is the max of randomization from 1 till itself",step=1,min_value=2)
  st.markdown(f"### {ri(1,rand_range)}")
