import streamlit as st
from random import randint as ri
st.markdown("# Random Games!!")

pages = [
st.Page(page:"app_pages/rps.py", title="Rock Paper Scissor", icon="✂️")
st.Page(page:"app_pages/dice.py", title="Dice Roller", icon="🎲")
]

pg = st.navigation(pages, position="sidebar", expanded=True)


pg.run()
