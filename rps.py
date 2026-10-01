import streamlit as st
from random import randint as ri
def rps_game():
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
