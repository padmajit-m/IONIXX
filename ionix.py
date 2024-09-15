import streamlit as st

# Sidebar for selecting stages of BC Partner Onboarding Process
st.sidebar.title("BC Partner Onboarding Process")
st.sidebar.header("Select Stage")

stage = st.sidebar.selectbox("Choose a stage to demo:", [
    "BC Creation", 
    "Branch Office Creation", 
    "Area Management", 
    "Product Code Creation", 
    "Ledger Assignment"
])

# Header for the selected stage
st.header(f"Demo: {stage}")

# Display process details based on the selected stage
if stage == "BC Creation":
    st.subheader("BC Creation Details:")
    st.write("""
        1. Enter BC Name
        2. Enter BC Short Name
        3. Enter BC Address
        4. Configure Workflow and Ledger
    """)
    st.text_input("BC Name", "")
    st.text_input("BC Short Name", "")
    st.text_area("BC Address", "")
    st.button("Create BC")

elif stage == "Branch Office Creation":
    st.subheader("Branch Office Creation Details:")
    st.write("""
        1. Define office level and parent office
        2. Enter branch details (Name, Address, Contact, etc.)
        3. Select Credit Analysis, Guarantor Credit Check
    """)
    st.text_input("Office Name", "")
    st.text_input("Office Short Name", "")
    st.text_area("Office Address", "")
    st.button("Create Branch Office")

elif stage == "Area Management":
    st.subheader("Area Management Details:")
    st.write("""
        1. Define area for branch office
        2. Ensure population sum matches total
    """)
    st.text_input("Area Name", "")
    st.number_input("Population", min_value=1)
    st.number_input("Total Population", min_value=1)
    st.button("Create Area")

elif stage == "Product Code Creation":
    st.subheader("Product Code Creation Details:")
    st.write("""
        1. Enter product particulars (e.g., Interest Rate, Code)
        2. Refer to page 4 of the document for details
    """)
    st.text_input("Product Name", "")
    st.text_input("Product Code", "")
    st.number_input("Interest Rate", min_value=0.0, max_value=100.0)
    st.button("Create Product Code")

elif stage == "Ledger Assignment":
    st.subheader("Ledger Assignment Details:")
    st.write("""
        1. Create General Ledger Account
        2. Assign Ledger to Branch Offices
    """)
    st.text_input("General Ledger Code", "")
    st.text_input("General Ledger Name", "")
    st.button("Assign Ledger to Branch")

# Footer for demo
st.write("This is a basic demo of the BC Partner Onboarding Process.")
