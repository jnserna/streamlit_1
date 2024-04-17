import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math
#import numpy_financial as npf

st.title("Calculador de una anualidad vencida")
st.write("### Calculator for an ordinary annuity")
st.markdown("####  **:blue[Datos de entrada - Inputs]**")
col1, col2, col3 = st.columns(3)
principal_value = col1.number_input("Valor del Principal - Present Value", min_value=0, value=10000000)
tasa_interes_rate = col2.number_input("Tasa interés (periódica)", min_value=0.000, value=0.010)
nper = col3.number_input("Períodos", min_value=1, value=60)

pago_periodico = principal_value * ((tasa_interes_rate * (1+tasa_interes_rate)**nper)/((1+tasa_interes_rate)**nper-1))

# O puedo usar esta fórmula de numpy financials:
# Compute the payment against loan principal plus interest: npf.pmt(rate, nper, per, pv)

st.markdown("####  **:blue[Resultado]**")
col1, col2, col3 = st.columns(3)
col1.metric(label="Pago periódico - Payment per period", value=f"${pago_periodico:,.2f}")