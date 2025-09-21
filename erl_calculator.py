import streamlit as st

def calculate_erl_net_share(total_gross_revenue, vat_on_revenue, bad_debt_100, clawback_100):
    distributable_rate = 13.04 / 100
    distributable_revenue = total_gross_revenue * distributable_rate

    vat_rate = 7.5 / 100
    vat_deduction = distributable_revenue * vat_rate

    net_distributable_value = distributable_revenue - vat_deduction

    erl_percentage = 19.5 / 100
    erl_share_of_revenue = (net_distributable_value * erl_percentage) + vat_on_revenue

    bad_debt_rate = 86.96 / 100
    total_bad_debt = bad_debt_100 * bad_debt_rate

    clawback_rate = 86.96 / 100
    total_erl_clawback = clawback_100 * clawback_rate

    final_value = erl_share_of_revenue - total_bad_debt + total_erl_clawback

    return {
        "Total Gross Revenue": total_gross_revenue,
        "Distributable Revenue": distributable_revenue,
        "VAT Deduction": vat_deduction,
        "Net Distributable Value": net_distributable_value,
        "ERL Share of Revenue": erl_share_of_revenue,
        "Total Bad Debt": total_bad_debt,
        "Total ERL Clawback": total_erl_clawback,
        "Final Value": final_value
    }

st.title("📊 ERL Net Share Calculator")
st.write("Distributable revenue fixed @ 13.04%")

# User Inputs
total_gross_revenue = st.number_input("Enter Total Gross Revenue (₦):", min_value=0.0, step=1000.0)
vat_on_revenue = st.number_input("Enter VAT on Revenue (₦):", min_value=0.0, step=100.0)
bad_debt_100 = st.number_input("Enter Bad Debt (100%) (₦):", min_value=0.0, step=100.0)
clawback_100 = st.number_input("Enter Clawback (100%) (₦):", min_value=0.0, step=100.0)

if st.button("Calculate"):
    results = calculate_erl_net_share(total_gross_revenue, vat_on_revenue, bad_debt_100, clawback_100)

    st.subheader("📋 Calculation Breakdown")
    st.write(f"**Total Gross Revenue:** ₦{results['Total Gross Revenue']:,.2f}")
    st.write(f"**Distributable Revenue (13.04%):** ₦{results['Distributable Revenue']:,.2f}")
    st.write(f"**Less VAT (7.5%):** ₦{results['VAT Deduction']:,.2f}")
    st.write(f"**Net Distributable Value:** ₦{results['Net Distributable Value']:,.2f}")

    st.write(f"**ERL's Share of Revenue:** ₦{results['ERL Share of Revenue']:,.2f}")
    st.write(f"**Total Bad Debt (86.96%):** ₦{results['Total Bad Debt']:,.2f}")
    st.write(f"**Total ERL Clawback (86.96%):** ₦{results['Total ERL Clawback']:,.2f}")

    st.success(f"✅ **Final Value (Net Payout to ERL): ₦{results['Final Value']:,.2f}**")
