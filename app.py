import os
import sys
import streamlit as st
import tooth_reconstruction
import display_app as udisp
import Pulp_Segmentation
import fracture_tooth_detection
import flurosis_tooth_detection

MENU = {
    "Tooth Fracture Reconstruction" : tooth_reconstruction,
    "Fracture Tooth Detection" : fracture_tooth_detection,
    "Pulp Segmentation" : Pulp_Segmentation,
    "Flurosis Detection" : flurosis_tooth_detection,		
}

st.sidebar.title("Choose A Use Case")
menu_selection = st.sidebar.radio("Use Case", list(MENU.keys()))
menu = MENU[menu_selection]

with st.spinner(f"Loading {menu_selection} ..."):
      udisp.render_page(menu)
