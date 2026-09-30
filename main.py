import streamlit as st
from random import randint as ri

st.warning("You Can Only Play One Game at a Time")

st.markdown("# Random Games!!")

st.markdown("## Rock Paper Scissor Shoot!!!")

mx = 0
choices = ["Rock", "Paper", "Scissor"]
player = st.selectbox("Choose One:", options=choices, accept_new_options=False)
comp = choices[(ri(1,3) - 1)]
if player == "Rock":
    if comp == "Paper":
        st.error("Computer Wins: 'Paper wins Rock' ")
    elif comp == "Scissor":
        st.success("You Win: 'Rock smashes Scissor'")
    else:
        st.warning("Tie: Rock vs. Rock")

elif player == "Paper":
    if comp == "Rock":
        st.success("You Win: 'Paper wins Rock' ")
    elif comp == "Scissor":
        st.error("Computer Wins: 'Scissor cuts Paper'")
    else:
        st.warning("Tie: Paper vs. Paper")

elif player == "Scissor":
    if comp == "Rock":
        st.error("Computer Wins: 'Rock smashes Scissor' ")
    elif comp == "Paper":
        st.success("You Win: 'Scissor cuts Paper'")
    else:
        st.warning("Tie: Scissor vs. Scissor")

mx += 1

st.button("Try again With Same One", key=mx)

st.divider()

st.markdown("## Dice Roller")
num_dice = st.number_input("How Many Dice do you want to roll?",step=1 , min_value=1)
st.divider()
for x in range(num_dice):
        st.markdown(f"### Dice #{x + 1}:")
        dice_range = st.slider("Enter The Dice's Max:", step=2 , min_value=2)
        st.markdown(f"##### {ri(1, dice_range)}")
        st.button("Roll Again", key=x)

