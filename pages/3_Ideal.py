import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# for spacing
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>Ideal Budget</h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

if 'ideal_df' in st.session_state:
    ideal = st.session_state['ideal_df']
    ideal['Proportion'] = ideal['Proportion'] * 100

    # bar plot
    st.bar_chart(data=ideal, x='Category', y='Proportion', x_label='Category',
                 y_label='Proportion in %', color="#9d00ff", use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns([0.5, 0.5])

    with col1:
        # pie plot
        fig, ax = plt.subplots()
        ax.pie(ideal['Proportion'], labels=ideal['Category'], autopct='%1.1f%%',
               colors=sns.color_palette('Set2'), wedgeprops=dict(width=0.2))
        ax.axis('equal')
        plt.title('Ideal Budget Distribution')
        st.pyplot(fig)

    with col2:
        # DataFrame
        ideal.rename(columns={'Proportion': 'Ideal Proportion in %'}, inplace=True)
        st.dataframe(ideal, use_container_width=True)
