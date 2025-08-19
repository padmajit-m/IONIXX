import streamlit as st
from supabase import create_client
from datetime import datetime
import config

# Supabase connection
supabase = create_client(config.SUPABASE_URL, config.SUPABASE_KEY)

st.set_page_config(page_title="Partner Onboarding Checklist", layout="wide")

st.title("✅ Partner Onboarding Checklist")

# Sidebar filters
st.sidebar.header("Filters")
partner_filter = st.sidebar.text_input("Search Partner")
status_filter = st.sidebar.selectbox("Filter by Checker Status", ["All", "Pending", "Approved", "Rejected"])
system_filter = st.sidebar.selectbox("System", ["All", "KICredit", "Encore", "Ionixx"])

# Tabs
tab1, tab2, tab3 = st.tabs(["📋 View Checklist", "➕ Add Config (Maker)", "🔎 Approve/Reject (Checker)"])

# --- VIEW CHECKLIST ---
with tab1:
    query = supabase.table("partner_configs").select("*")
    if partner_filter:
        query = query.ilike("partner_name", f"%{partner_filter}%")
    if status_filter != "All":
        query = query.eq("checker_status", status_filter)
    if system_filter != "All":
        query = query.eq("system_name", system_filter)

    data = query.execute().data
    st.write("### All Configs")
    st.dataframe(data, use_container_width=True)

# --- ADD CONFIG (MAKER) ---
with tab2:
    st.write("### Add New Config")
    partner = st.text_input("Partner Name")
    system = st.selectbox("System", ["KICredit", "Encore", "Ionixx"])
    config_item = st.text_area("Configuration Item")
    created_by = st.text_input("Maker Name")

    if st.button("Submit Config"):
        supabase.table("partner_configs").insert({
            "partner_name": partner,
            "system_name": system,
            "config_item": config_item,
            "maker_status": "Submitted",
            "checker_status": "Pending",
            "created_by": created_by
        }).execute()
        st.success("✅ Config submitted successfully!")

# --- APPROVE/REJECT (CHECKER) ---
with tab3:
    st.write("### Approve/Reject Pending Items")
    pending = supabase.table("partner_configs").select("*").eq("checker_status", "Pending").execute().data
    for item in pending:
        with st.expander(f"{item['partner_name']} | {item['system_name']}"):
            st.write(f"**Config:** {item['config_item']}")
            decision = st.radio("Decision", ["Approve", "Reject"], key=f"dec_{item['id']}")
            remarks = st.text_area("Remarks", key=f"rem_{item['id']}")
            checked_by = st.text_input("Checker Name", key=f"chk_{item['id']}")

            if st.button("Submit Decision", key=f"btn_{item['id']}"):
                status = "Approved" if decision == "Approve" else "Rejected"
                supabase.table("partner_configs").update({
                    "checker_status": status,
                    "remarks": remarks,
                    "checked_by": checked_by,
                    "updated_at": datetime.now().isoformat()
                }).eq("id", item["id"]).execute()
                st.success(f"✅ Config {status}!")
