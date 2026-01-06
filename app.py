import streamlit as st
from datetime import datetime

st.set_page_config(page_title="A.E.R.I.S", layout="centered")

st.title("🚨 A.E.R.I.S")
st.subheader("Automated Emergency Recognition & Integration System")

st.write(
    "An AI-powered surveillance system that detects violent activities "
    "and medical emergencies from CCTV footage and triggers automated alerts."
)

st.divider()

camera = st.selectbox(
    "📹 Select Camera Location",
    ["Main Lobby - Sector 4", "Parking Area", "Corridor - Floor 2"]
)

event = st.selectbox(
    "🧠 Simulated AI Detection Output",
    ["Normal Activity", "Violence Detected", "Medical Emergency (Fall)"]
)

if st.button("Run Detection"):
    st.info("Analyzing CCTV feed...")

    if event == "Normal Activity":
        st.success("✅ No emergency detected.")

    else:
        st.error(f"🚨 ALERT: {event}")
        st.write("📍 **Location:**", camera)
        st.write("🕒 **Time:**", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

        st.warning("🎥 Evidence clip captured (simulated)")
        st.warning("📞 Automated call triggered (simulated)")
        st.warning("📧 Automated email sent (simulated)")

st.divider()
st.caption("Demo version • AI model and real alerts can be integrated")
