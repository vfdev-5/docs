import streamlit as st
import altair as alt
import inspect
from vega_datasets import data

@st.experimental_memo
def get_chart_34956(use_container_width: bool):
    import altair as alt
    from vega_datasets import data
    
    source = data.iris()
    
    chart = alt.Chart(source).transform_fold(
        ['petalWidth',
         'petalLength',
         'sepalWidth',
         'sepalLength'],
        as_ = ['Measurement_type', 'value']
    ).transform_density(
        density='value',
        bandwidth=0.3,
        groupby=['Measurement_type'],
        extent= [0, 8],
        counts = True,
        steps=200
    ).mark_area().encode(
        alt.X('value:Q'),
        alt.Y('density:Q', stack='zero'),
        alt.Color('Measurement_type:N')
    ).properties(width=400, height=100)
    
    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])
    
    with tab1:
        st.altair_chart(chart, theme="streamlit", use_container_width=True)
    with tab2:
        st.altair_chart(chart, theme=None, use_container_width=True)

try:
    st.expander("See code").code(inspect.getsource(get_chart_34956))
    get_chart_34956(use_container_width=True)
except Exception as e:
    st.exception(e)

