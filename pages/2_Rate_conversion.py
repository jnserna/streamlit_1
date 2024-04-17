import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math

st.write("### Encuentre su tasa - De periódica a Efeciva Anual (EA)")
st.markdown("#####  **:gray[Convert your interest rate (IR) - From periodic (IR) to Effective Annual (EIR)]**")
col1, col2 = st.columns(2)
with col1:
    interes_rate_input1 = col1.number_input("Seleccione Tasa de interés periódica en %", min_value=0.01, value=1.0)

with col2:
    chosen1 = st.selectbox("Seleccione Frecuencia de capitalización o cobro", ("Anual", "Semestral","Trimestral", "Mensual","Quincenal"),index=3,
                       placeholder="Selecciona la frecuencia")

npers = {"Anual":1,"Semestral":2,"Trimestral":4,"Mensual":12,"Quincenal":24}

pers = npers[chosen1]

tasa_nominal1 = interes_rate_input1 * pers
tasa_EA1 = ((((interes_rate_input1/100)+1)**(pers)) - 1)*100

#TEM = [ ( 1+TEA ) ** (1/n) ] - 1
#TEA = [ ( TEM + 1 ) **(n) ] - 1

#iv = ia / (1-ia)
#ia = iv / (1+iv)

col1, col2, col3 = st.columns(3)
with col1:
    st.write("### Resultado:")
col2.metric(label="Tasa nominal", value=f"{tasa_nominal1:,.2f}%")
col3.metric(label="Tasa EA - EIR", value=f"{tasa_EA1:,.2f}%")

st.markdown("#####  **:orange[Tasas equivalentes (Teq) - Vencidas periódicas]**")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric(label="Anual", value=f"{tasa_EA1:,.2f}%")

tasa_semestral_vencida = (((1+(tasa_EA1/100))**(1/2))-1)*100
col2.metric(label="Semestral", value=f"{tasa_semestral_vencida:,.2f}%")

tasa_trimestral_vencida = (((1+(tasa_EA1/100))**(1/4))-1)*100
col3.metric(label="Trimestral", value=f"{tasa_trimestral_vencida:,.2f}%")

tasa_mensual_vencida = (((1+(tasa_EA1/100))**(1/12))-1)*100
col4.metric(label="Mensual", value=f"{tasa_mensual_vencida:,.2f}%")

tasa_quincenal_vencida = (((1+(tasa_EA1/100))**(1/24))-1)*100
col5.metric(label="Quincenal", value=f"{tasa_quincenal_vencida:,.3f}%")

st.markdown("#####  **:orange[Teq - Vencidas nominales]**")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric(label="Anual", value=f"{tasa_EA1:,.2f}%")

tasa_nominal_sem_ven = tasa_semestral_vencida*2
col2.metric(label="Semestral", value=f"{tasa_nominal_sem_ven:,.2f}%")

tasa_nominal_trim_ven = tasa_trimestral_vencida*4
col3.metric(label="Trimestral", value=f"{tasa_nominal_trim_ven:,.2f}%")

tasa_nominal_mes_ven = tasa_mensual_vencida*12
col4.metric(label="Mensual", value=f"{tasa_nominal_mes_ven:,.2f}%")

tasa_nominal_quin_ven = tasa_quincenal_vencida*24
col5.metric(label="Quincenal", value=f"{tasa_nominal_quin_ven:,.2f}%")

st.markdown("#####  **:blue[Teq - Anticipadas periódicas]**")
col1, col2, col3, col4, col5 = st.columns(5)
tasa_EA1_ant = (tasa_EA1/100)/(1+(tasa_EA1/100))*100
col1.metric(label="Anual", value=f"{tasa_EA1_ant:,.2f}%")

tasa_per_sem_ant = ((tasa_semestral_vencida/100)/(1+(tasa_semestral_vencida/100)))*100
col2.metric(label="Semestral", value=f"{tasa_per_sem_ant:,.2f}%")

tasa_per_trim_ant = ((tasa_trimestral_vencida/100)/(1+(tasa_trimestral_vencida/100)))*100
col3.metric(label="Trimestral", value=f"{tasa_per_trim_ant:,.2f}%")

tasa_per_mes_ant = ((tasa_mensual_vencida/100)/(1+(tasa_mensual_vencida/100)))*100
col4.metric(label="Mensual", value=f"{tasa_per_mes_ant:,.2f}%")

tasa_per_quin_ant = ((tasa_quincenal_vencida/100)/(1+(tasa_quincenal_vencida/100)))*100
col5.metric(label="Quincenal", value=f"{tasa_per_quin_ant:,.3f}%")

st.markdown("#####  **:blue[Teq - Anticipadas nominales]**")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric(label="Anual", value=f"{tasa_EA1_ant:,.2f}%")

tasa_nominal_sem_ant = tasa_per_sem_ant*2
col2.metric(label="Semestral", value=f"{tasa_nominal_sem_ant:,.2f}%")

tasa_nominal_trim_ant = tasa_per_trim_ant*4
col3.metric(label="Trimestral", value=f"{tasa_nominal_trim_ant:,.2f}%")

tasa_nominal_mes_ant = tasa_per_mes_ant*12
col4.metric(label="Mensual", value=f"{tasa_nominal_mes_ant:,.2f}%")

tasa_nominal_quin_ant = tasa_per_quin_ant*24
col5.metric(label="Quincenal", value=f"{tasa_nominal_quin_ant:,.2f}%")

# Acá voy a crear el dataframe para el gráfico

data_total = [[1,'1-Anual', tasa_EA1,tasa_EA1_ant],
            [2,'2-Semestral',tasa_nominal_sem_ven,tasa_nominal_sem_ant],
            [4,'3-Trimestral', tasa_nominal_trim_ven,tasa_nominal_trim_ant],
            [12,'4-Mensual', tasa_nominal_mes_ven,tasa_nominal_mes_ant],
            [24,'5-Quincenal', tasa_nominal_quin_ven,tasa_nominal_quin_ant]]
 
# Create the pandas DataFrame

df_total = pd.DataFrame(data_total, columns=['nper','Pers', 'Nominal Vencida', 'Nominal Antipada'])
df_total = df_total.sort_values(by='nper')

col1, col2 = st.columns(2)
with col1:
    st.markdown("####  **:green[La convergencia de tasas para]**")

col2.metric(label="", value=f"{tasa_EA1:,.2f}% EA, es:")
st.line_chart(df_total,y=["Nominal Vencida","Nominal Antipada"],x="Pers")