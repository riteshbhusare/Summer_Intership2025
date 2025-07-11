import streamlit as st

st.set_page_config(page_title="Facebook Post UI", layout="centered")
st.title("📘 Facebook Post Simulator")

st.warning("This is a UI demo. No real posting or API used.")

fb_user = st.text_input("Enter Facebook Profile/Page Name")
fb_post = st.text_area("Write your Facebook post")

if st.button("Simulate Facebook Post"):
    st.success(f"✅ Simulated post for {fb_user}: \"{fb_post}\"")