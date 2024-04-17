import streamlit as st

st.set_page_config(
    page_title="Multipage App",
    page_icon="🖖"
)

st.title("Página inicial")
st.write("Este proyecto fue desarrollado por Juan Esteban Serna.")
st.markdown("El propósito es **:blue[incentivar]** el uso de **:blue[Python]**, y al mismo tiempo transmitir algunos conceptos de **:green[finanzas]**.")
st.write("#### Main page")
st.write("This project was developed by Juan Esteban Serna.")
st.markdown("The purpose is to **:blue[incentivize]** the use of **:blue[Python]**, and at the same time, to transmit some concepts of **:green[finance]**.")
st.sidebar.success("Select a page above")