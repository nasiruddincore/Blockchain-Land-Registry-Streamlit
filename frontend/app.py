import sys
import os
import streamlit as st

# Add backend to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.registry_logic import load_data, register_property, verify_property, transfer_ownership

st.set_page_config(page_title="Blockchain Land Registry", page_icon="🏢", layout="wide")

st.title("🏢 Blockchain-Based Land Registry & Property Ownership System")
st.markdown("---")

# Sidebar Role Navigation
st.sidebar.header("🔐 Portal Access")
role = st.sidebar.selectbox("Select Role", ["Public Verification Portal", "Property Owner Dashboard", "Land Authority / Admin"])

data = load_data()
properties = data["properties"]

if role == "Public Verification Portal":
    st.subheader("🔍 Public Property & Title Search")
    search_id = st.text_input("Enter Property ID (e.g., P-001):")
    
    if search_id:
        if search_id in properties:
            p = properties[search_id]
            col1, col2 = st.columns(2)
            with col1:
                st.success("Property Record Found on Ledger")
                st.write(f"**Property Number:** {p['propertyNumber']}")
                st.write(f"**Location:** {p['location']}")
                st.write(f"**Area:** {p['area']}")
                st.write(f"**Type:** {p['propertyType']}")
                st.write(f"**Current Owner:** {p['currentOwner']}")
            with col2:
                st.write(f"**Status:** {p['status']}")
                st.write(f"**Verified:** {'Yes ✅' if p['verified'] else 'No ❌'}")
                st.write(f"**Document Hash (SHA-256):** `{p['documentHash']}`")
                st.write(f"**Registered At:** {p['registeredAt']}")
            
            st.markdown("### 📜 On-Chain Audit & Transaction History")
            for h in p["history"]:
                st.text(f"[{h['timestamp']}] Event: {h['event']} (Actor: {h['actor']})")
        else:
            st.error("Property ID not found in registry.")

elif role == "Property Owner Dashboard":
    st.subheader("👤 Owner Portal: Transfer Ownership")
    prop_ids = list(properties.keys())
    
    if prop_ids:
        selected_prop = st.selectbox("Select Your Property ID", prop_ids)
        p = properties[selected_prop]
        
        st.info(f"Current Owner of {selected_prop}: **{p['currentOwner']}**")
        
        with st.form("transfer_form"):
            owner_input = st.text_input("Confirm Your Wallet Address (Current Owner):")
            new_owner_input = st.text_input("New Buyer Wallet Address:")
            submit_transfer = st.form_submit_button("Initiate Secure Ownership Transfer")
            
            if submit_transfer:
                success, msg = transfer_ownership(selected_prop, owner_input, new_owner_input)
                if success:
                    st.success(msg)
                    st.rerun()
                else:
                    st.error(msg)
    else:
        st.warning("No properties available.")

elif role == "Land Authority / Admin":
    st.subheader("🛡️ Land Authority Admin Control")
    
    tab1, tab2 = st.tabs(["Register New Property", "Verify Pending Properties"])
    
    with tab1:
        with st.form("reg_form"):
            pid = st.text_input("Property ID (e.g., P-002)")
            pnum = st.text_input("Property / Survey Number")
            loc = st.text_input("Location / Address")
            area = st.text_input("Area (e.g., 1800 sq.ft)")
            ptype = st.selectbox("Property Type", ["Residential", "Commercial", "Agricultural"])
            owner = st.text_input("Initial Owner Wallet Address")
            dhash = st.text_input("Document Hash (SHA-256 Mock)")
            
            submit_reg = st.form_submit_button("Register Property on Ledger")
            if submit_reg:
                if pid and pnum and owner:
                    success, msg = register_property(pid, pnum, loc, area, ptype, owner, dhash)
                    if success:
                        st.success(msg)
                        st.rerun()
                    else:
                        st.error(msg)
                else:
                    st.warning("Please fill in all mandatory fields.")
                    
    with tab2:
        st.markdown("### Pending Verification Queue")
        unverified = [pid for pid, p in properties.items() if not p["verified"]]
        
        if unverified:
            v_prop = st.selectbox("Select Property to Verify", unverified)
            if st.button("Approve & Verify Property"):
                success, msg = verify_property(v_prop)
                if success:
                    st.success(msg)
                    st.rerun()
                else:
                    st.error(msg)
        else:
            st.success("All properties in the registry are verified.")