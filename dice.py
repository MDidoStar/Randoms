st.markdown("# Dice Roller")
num_dice = st.number_input("How Many Dice do you want to roll?",step=1 , min_value=1)
st.divider()
for x in range(num_dice):
        st.markdown(f"## Dice #{x + 1}:")
        dice_range = st.slider("Enter The Dice's Max:", step=2 , min_value=2, key=f"dice{x}")
        st.markdown(f"### {ri(1, dice_range)}")
        st.button("Roll Again", key=f"f{x}")

