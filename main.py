import os
import streamlit as st

from constant import FILE_PATH, JOLLY_ROGER_PATH, WANTED_POSTER_PATH
from lib.pirate_group import PirateGroup
from lib.pirate import Pirate
from utils.file import load_csv, add_to_csv, save_uploaded_file
from utils.currency import format_currency

def load_existing_pirates():
    if not os.path.exists(FILE_PATH):
        return []
        
    pirate_groups = {}
    for row in load_csv():
        name, occupation, bounty, poster, group_name, ship, jolly_roger = row
        new_pirate = Pirate(name, occupation, bounty, poster)

        if (group_name in pirate_groups):
            pirate_groups[group_name].add_crew(new_pirate)
        else:
            new_pirate_group = PirateGroup(group_name, ship, jolly_roger)
            new_pirate_group.add_crew(new_pirate)
            pirate_groups[group_name] = new_pirate_group

    return list(pirate_groups.values())


if "pirate_groups" not in st.session_state:
    st.session_state.pirate_groups = load_existing_pirates()

st.title("🏴‍☠️ One Piece's Pirates Database")

menu = st.sidebar.selectbox("Menu", ["⛵️ Add Pirate Group", "☠️ Add Pirate", "🏴‍☠️ All Pirates"])

if menu == "⛵️ Add Pirate Group":
    st.subheader("Add New Pirate Group")

    name = st.text_input("Name", key="group_name")
    ship = st.text_input("Ship Name",)
    jolly_roger = st.file_uploader("Upload Jolly Roger", type=["jpg", "jpeg", "png"])
    submit_btn = st.button("Submit", key="submit_pg")

    if submit_btn:
        jolly_roger_path = save_uploaded_file(jolly_roger, name.replace(' ', '_').lower(), JOLLY_ROGER_PATH)
        new_pirate_group = PirateGroup(name, ship, jolly_roger_path)
        st.session_state.pirate_groups.append(new_pirate_group)
        st.success(f"New pirate group: {new_pirate_group.name} successfully added.")


elif menu == "☠️ Add Pirate":
    st.subheader("Add New Pirate")
    
    group_options = {pg.name: pg for pg in st.session_state.pirate_groups}
    selected_group = st.selectbox("Choose Pirate Group", list(group_options.keys()))

    pirate_name = st.text_input("Name", key="pirate_name")
    occupation = st.text_input("Occupation")
    bounty = st.number_input("Bounty")
    wanted_poster = st.file_uploader("Wanted Poster", type=["jpg", "jpeg", "png"])
    submit_btn = st.button("Submit", key="submit_p")

    if submit_btn:
        wanted_poster_path = save_uploaded_file(wanted_poster, pirate_name.replace(' ', '_').lower(), WANTED_POSTER_PATH)
        new_pirate = Pirate(pirate_name, occupation, int(bounty), wanted_poster_path)
        group_options[selected_group].add_crew(new_pirate)

        add_to_csv({
            "Name": new_pirate.name,
            "Occupation": new_pirate.occupation,
            "Bounty": new_pirate.bounty,
            "Poster": new_pirate.wanted_poster,
            "Group": group_options[selected_group].name,
            "Ship": group_options[selected_group].ship,
            "Jolly Roger": group_options[selected_group].jolly_roger
        })

        st.success(f"Pirate {new_pirate.name} successfully added as crew {selected_group}")
        st.rerun()


elif menu == "🏴‍☠️ All Pirates":
    st.subheader("All Pirates")

    if st.session_state.pirate_groups:
        for index, group in enumerate(st.session_state.pirate_groups):
            with st.container():
                cols = st.columns([1, 3])

                with cols[0]:
                    if group.jolly_roger and os.path.exists(group.jolly_roger):
                        st.image(group.jolly_roger, width=150)
                    else:
                        st.image("jolly-rogers/pirate-flag.png", width=150)
                    
                    st.subheader(group.name)
                    st.write(f"**Ship**: {group.ship}")
                    st.write(f"**Total Bounty**: {format_currency(group.get_total_bounty())} Belly")
                
                with cols[1]:
                    st.write("**Crew Members**:")
                    for member in group.crew:
                        with st.expander(member.name):
                            with st.container():
                                subcols = st.columns([1, 3])

                                with subcols[0]:
                                    if member.wanted_poster and os.path.exists(member.wanted_poster):
                                        st.image(member.wanted_poster, width=100)
                                    else:
                                        st.image("jolly-rogers/pirate-flag.png", width=100)
                                
                                with subcols[1]:
                                    st.write(f"#### {member.name}")
                                    st.write(f"**Occupation**: {member.occupation}")
                                    st.write(f"**Bounty**: {format_currency(int(member.bounty))} Belly")
                
                st.markdown("---")

    else:
        st.error("No pirate data yet!")