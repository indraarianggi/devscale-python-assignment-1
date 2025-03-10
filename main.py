import streamlit as st
from lib.pirate_group import PirateGroup
from lib.pirate import Pirate

if "pirate_groups" not in st.session_state:
    st.session_state.pirate_groups = []

st.title("🏴‍☠️Pirate Database")

menu = st.sidebar.selectbox("Menu", ["⛵️ Add Pirate Group", "☠️ Add Pirate", "🏴‍☠️ View Pirates"])

if menu == "⛵️ Add Pirate Group":
    st.subheader("Add New Pirate Group")

    name = st.text_input("Name", key="group_name")
    ship = st.text_input("Ship Name",)
    submit_btn = st.button("Submit", key="submit_pg")

    if submit_btn:
        new_pirate_group = PirateGroup(name, ship)
        st.session_state.pirate_groups.append(new_pirate_group)
        st.success(f"New pirate group: {new_pirate_group.name} successfully added.")


elif menu == "☠️ Add Pirate":
    st.subheader("Add New Pirate")
    
    group_options = {pg.name: pg for pg in st.session_state.pirate_groups}
    selected_group = st.selectbox("Choose Pirate Group", list(group_options.keys()))
    pirate_name = st.text_input("Name", key="pirate_name")
    occupation = st.text_input("Occupation")
    bounty = st.number_input("Bounty")
    submit_btn = st.button("Submit", key="submit_p")

    if submit_btn:
        new_pirate = Pirate(pirate_name, occupation, bounty)
        group_options[selected_group].add_crew(new_pirate)
        st.success(f"Pirate {new_pirate.name} successfully added as crew {selected_group}")


elif menu == "🏴‍☠️ View Pirates":
    st.subheader("All Pirates")

    if st.session_state.pirate_groups:
        for index, group in enumerate(st.session_state.pirate_groups):
            st.write(f"#### {group.name}")
            st.write(f"Ship: {group.ship}")
            st.write("##### Crew Members:")
            for member in group.crew:
                st.write(f"- {member.name}")
