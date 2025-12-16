import streamlit as st
import pandas as pd

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Financial Performance at a Glance | Bank Jakarta",
    layout="wide"
)

st.title("📊 Financial Performance at a Glance")
st.subheader("Bank Jakarta | 2024 vs 2023")

st.markdown("---")

# =========================
# DATA
# =========================
data = [
    ["Total Aset (Rp T)", 118.14, 103.85, "+13.76%", 
     "Ekspansi agresif, perlu kontrol risiko & kualitas aset"],
    ["Total Kredit Neto (Rp T)", 73.24, 53.40, "+37.06%", 
     "Pertumbuhan tinggi → risiko NPL perlu early warning"],
    ["Dana Pihak Ketiga (Rp T)", 90.01, 78.20, "+15.10%", 
     "Likuiditas terjaga, tapi tekanan cost of fund"],
    ["Laba Bersih (Rp T)", 1.30, 1.47, "-11.56%", 
     "Margin tertekan oleh biaya & risiko kredit"],
    ["ROA (%)", 1.60, 1.87, "↓", 
     "Efektivitas aset menurun"],
    ["ROE (%)", 11.89, 13.96, "↓", 
     "Tekanan profitabilitas terhadap ekuitas"],
    ["NPL Gross (%)", 3.45, 2.49, "↑ signifikan", 
     "Kualitas kredit memburuk → perlu deteksi dini"],
    ["BOPO (%)", 81.89, 77.27, "↑", 
     "Efisiensi menurun, indikasi potensi fraud & inefisiensi"],
    ["LDR (%)", 82.05, 70.03, "↑ tajam", 
     "Penyaluran agresif, risiko likuiditas & kredit"],
    ["CAR (%)", 23.49, 25.71, "↓", 
     "Modal kuat, ruang mitigasi risiko tersedia"]
]

columns = [
    "Indikator",
    "2024",
    "2023",
    "Perubahan",
    "Implikasi Strategis"
]

df = pd.DataFrame(data, columns=columns)

# =========================
# KPI HIGHLIGHTS
# =========================
st.subheader("🔑 Key Highlights")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Aset", "Rp 118.14 T", "+13.76%")
col2.metric("Laba Bersih", "Rp 1.30 T", "-11.56%")
col3.metric("NPL Gross", "3.45%", "+0.96%")
col4.metric("CAR", "23.49%", "Strong")

st.markdown("---")

# =========================
# TABLE VIEW
# =========================
st.subheader("📌 Financial Indicators & Strategic Implications")
st.dataframe(df, use_container_width=True)

# =========================
# STRATEGIC INSIGHT
# =========================
st.markdown("---")
st.subheader("🧠 Executive Insight")

st.info(
    """
    📉 **Profitability under pressure** despite strong asset and credit growth.  
    ⚠️ **Rising NPL & BOPO** indicate increasing operational and credit risk.  
    🛡️ **Strong capital position** provides room for proactive risk mitigation.  

    👉 **Key Message:**  
    Growth must be accompanied by **early warning & fraud intelligence** to protect profitability and asset quality.
    """
)

# =========================
# FOOTNOTE
# =========================
st.caption("Source: Annual Report Bank Jakarta 2024 | Mockup Dashboard")
