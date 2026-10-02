import streamlit as st
from random import randint as ri
def dice_game():
        dice_ranges = []
        st.markdown("## Dice Roller 🎲")
        num_dice = st.number_input("How Many Dice do you want to roll?",step=1 , min_value=1)
        dice_ran = st.number_input("Set all dice maxes to",step=1 , min_value=1)
        for t in dice_ranges:
                dice_ranges[t] = dice_ran
        st.divider()
        for x in range(num_dice):
                st.markdown(f"### Dice #{x + 1}:")
                dice_range = st.number_input("Enter The Dice's Max:", step=2 , min_value=2, key=f"dice{x}")
                dice_ranges.append(dice_range)
                st.markdown(f"#### {ri(1, dice_ranges[x])}")
                st.button("Roll Again", key=f"f{x}")
