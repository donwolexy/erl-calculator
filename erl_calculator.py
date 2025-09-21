{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b46c9a1a-a3ba-4bcc-8528-a1333d915f07",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-09-21 20:08:23.049 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run /Applications/anaconda3/lib/python3.11/site-packages/ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "\n",
    "st.title(\"📊 ERL Net Share Detailed Calculator\")\n",
    "st.caption(\"Distributable revenue fixed @ 13.04%\")\n",
    "\n",
    "def calculate_erl_net_share():\n",
    "    # Step 1: Inputs\n",
    "    total_gross_revenue = st.number_input(\"Enter Total Gross Revenue (₦)\", min_value=0.0, step=1000.0, format=\"%.2f\")\n",
    "    vat_on_revenue = st.number_input(\"Enter VAT on Revenue (₦)\", min_value=0.0, step=100.0, format=\"%.2f\")\n",
    "    bad_debt_100 = st.number_input(\"Enter Bad Debt (100%) (₦)\", min_value=0.0, step=100.0, format=\"%.2f\")\n",
    "    clawback_100 = st.number_input(\"Enter Clawback (100%) (₦)\", min_value=0.0, step=100.0, format=\"%.2f\")\n",
    "\n",
    "    if st.button(\"Calculate\"):\n",
    "        # Step 2: Distributable revenue fixed @ 13.04%\n",
    "        distributable_rate = 13.04 / 100\n",
    "        distributable_revenue = total_gross_revenue * distributable_rate\n",
    "\n",
    "        # Step 3: VAT on distributable revenue @ 7.5%\n",
    "        vat_rate = 7.5 / 100\n",
    "        vat_deduction = distributable_revenue * vat_rate\n",
    "\n",
    "        # Step 4: Net Distributable Value\n",
    "        net_distributable_value = distributable_revenue - vat_deduction\n",
    "\n",
    "        # Step 5: ERL’s Share of Revenue\n",
    "        erl_percentage = 19.5 / 100\n",
    "        erl_share_of_revenue = (net_distributable_value * erl_percentage) + vat_on_revenue\n",
    "\n",
    "        # Step 6: Bad Debt\n",
    "        bad_debt_rate = 86.96 / 100\n",
    "        total_bad_debt = bad_debt_100 * bad_debt_rate\n",
    "\n",
    "        # Step 7: Clawback\n",
    "        clawback_rate = 86.96 / 100\n",
    "        total_erl_clawback = clawback_100 * clawback_rate\n",
    "\n",
    "        # Step 8: Final Calculation\n",
    "        final_value = erl_share_of_revenue - total_bad_debt + total_erl_clawback\n",
    "\n",
    "        # Display results\n",
    "        st.subheader(\"🔎 Calculation Breakdown\")\n",
    "        st.write(f\"**Total Gross Revenue:** ₦{total_gross_revenue:,.2f}\")\n",
    "        st.write(f\"**Distributable Revenue @13.04%:** ₦{distributable_revenue:,.2f}\")\n",
    "        st.write(f\"**Less VAT (7.5%):** ₦{vat_deduction:,.2f}\")\n",
    "        st.write(f\"**Net Distributable Value:** ₦{net_distributable_value:,.2f}\")\n",
    "\n",
    "        st.markdown(\"---\")\n",
    "        st.success(f\"ERL’s Share of Revenue = ₦{erl_share_of_revenue:,.2f}\")\n",
    "\n",
    "        st.write(f\"**Total Bad Debt:** ₦{total_bad_debt:,.2f}\")\n",
    "        st.write(f\"**Total ERL Clawback:** ₦{total_erl_clawback:,.2f}\")\n",
    "\n",
    "        st.markdown(\"---\")\n",
    "        st.subheader(f\"✅ Final Value (Net Payout to ERL): ₦{final_value:,.2f}\")\n",
    "\n",
    "calculate_erl_net_share()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bf52991b-1936-4dfb-84a2-11862a79835b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
