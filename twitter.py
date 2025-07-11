import streamlit as st

st.set_page_config(page_title="Twitter Post UI", layout="centered")
st.title("🐦 Twitter Post Simulator")

st.warning("This is a Twitter demo .")

twitter_user = st.text_input("Enter Twitter Handle (@username)")
twitter_post = st.text_area("Compose your tweet")

if st.button("Simulate Tweet"):
    st.success(f"✅ Simulated post to @{twitter_user}: \"{twitter_post}\"")
