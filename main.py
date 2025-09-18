import streamlit as st
import pandas as pd
from io import BytesIO


st.set_page_config(page_title='Budget Optimizer', page_icon='💰', layout='centered')

st.title('Budget Optimizer 💵')

st.markdown('### Welcome to your personal budgeting assistent!')

st.markdown("""
<div class="instructions">

👋 **How to Use the Optimizer**
            
1. 📊 **Compare**  
   The app will show where you over or under spent compared to your ideal plan.  
   You'll also see charts and summaries to help you improve your budgeting.

2. 📄 **Actual Budget**  
   Upload another Excel file with your actual spending per category. The app will automatically give you the proportion you used across the categories. 
  
3. 📄 **Ideal Budget**  
   Upload an Excel file with your ideal budget **proportions** (e.g., 30% Rent, 20% Food, etc.).  

---

🔒 *No data is stored, everything is processed locally in your browser.*

✅ *Make sure your Excel files are well formatted (Category + Proportion or Amount).
   Check the following excel sheets for refrence.*

</div>
""", unsafe_allow_html=True)

# Read Example Excel files For Users To Download
excel1 = pd.read_excel('actual budget.xlsx')
excel2 = pd.read_excel('ideal finance.xlsx')

# Convert DataFrame to Excel bytes
def to_excel_bytes(df):
    buffer = BytesIO()
    df.to_excel(buffer, index=False, engine='openpyxl')
    buffer.seek(0)
    return buffer

col1, col2 = st.columns(2)
with col1:
   # Download buttons
   st.download_button("Download Actual Budget", to_excel_bytes(excel1), "actual_budget.xlsx", 
                        mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
   
with col2:
   # Download button
   st.download_button("Download Ideal Budget", to_excel_bytes(excel2), "ideal_budget.xlsx", 
                   mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")