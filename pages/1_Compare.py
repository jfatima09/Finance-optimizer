import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Compare Actual vs Ideal Budget")

ideal = st.file_uploader('Upload ideal budget', type=['xlsx'])
actual = st.file_uploader('Upload actual budget', type=['xlsx'])

if ideal is not None and actual is not None:
    # ideal df
    ideal_df = pd.read_excel(ideal)
    ideal_df['Proportion in %'] = ideal_df['Proportion'] * 100

    # actual df
    actual_df = pd.read_excel(actual)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.write('Ideal Proportion distribution')
        st.dataframe(ideal_df)
    with col2:
        st.write('Current Budget')
        st.dataframe(actual_df)

    # merged df
    merged_df = pd.merge(ideal_df, actual_df, on='Category', how='outer')
    merged_df.fillna(0, inplace=True)
    total_amount = merged_df['Amount'].sum()

    merged_df['Actual Proportion'] = merged_df.apply(lambda x: x['Amount'] / total_amount, axis=1)
    merged_df['Ideal Amount'] = merged_df.apply(lambda x: x['Proportion'] * total_amount, axis=1)

    order = ['Category', 'Proportion', 'Actual Proportion', 'Ideal Amount', 'Amount']
    merged_df = merged_df[order]
    merged_df.rename(columns={'Amount': 'Actual Amount', 'Proportion': 'Ideal Proportion'}, inplace=True)
    merged_df['Extra Amount Used'] = merged_df['Actual Amount'] - merged_df['Ideal Amount']

    st.markdown("<br>", unsafe_allow_html=True)

    # bar chart
    st.bar_chart(data=merged_df, x='Category', y=['Actual Amount', 'Ideal Amount'], stack=False,
                 x_label='Category', y_label='Actual vs Ideal', color=["#d4ff00", "#ff0066"], use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.write('Ideal vs Actual Spending')
    st.dataframe(merged_df)

    extra = merged_df['Ideal Amount'].sum() - merged_df['Actual Amount'].sum()

    st.markdown("<h1 style='text-align: center;'>Total Savings</h1>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: center;'>{extra:,.2f}</h3>", unsafe_allow_html=True)

    st.session_state['ideal_df'] = ideal_df
    st.session_state['actual_df'] = actual_df
