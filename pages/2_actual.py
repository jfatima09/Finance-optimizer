import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>Current Budget Distribution</h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

if 'actual_df' in st.session_state:
    df_a = st.session_state['actual_df']

    def prop_used(row):
        total = df_a['Amount'].sum()
        return (row['Amount'] / total) * 100

    df_a['Proportion used in %'] = df_a.apply(prop_used, axis=1)

    # barplot
    st.bar_chart(data=df_a, x='Category', y='Amount', x_label='Category', y_label='Amount',
                 color="#fb00ff", use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # DataFrame view
    st.dataframe(df_a, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # pie chart
    fig, ax = plt.subplots()
    ax.pie(df_a['Proportion used in %'], labels=df_a['Category'], autopct='%1.1f%%',
           colors=sns.color_palette('Set2'), wedgeprops=dict(width=0.2))
    ax.axis('equal')
    plt.title('Ideal Budget Distribution')
    st.pyplot(fig)
