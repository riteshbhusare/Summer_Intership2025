import streamlit as st
import pywhatkit as kit
import re

# Page config
st.set_page_config(page_title="WhatsApp Message Sender", page_icon="📱", layout="centered")

# App title
st.title("📱 WhatsApp Message Sender")
st.write("Send WhatsApp messages instantly through your browser.")

# Sidebar help
with st.sidebar:
    st.header("How it works:")
    st.markdown("""
    - ✅ Make sure WhatsApp Web is open in your browser  
    - 📲 Enter full phone number with country code (e.g., +91XXXXXXXXXX)  
    - ✏ Type a message like a human would  
    """)

# Phone number validator
def is_valid_number(phone):
    return re.match(r"^\+\d{10,15}$", phone)

# Main form for instant messaging
st.subheader("Send Message Instantly")
phone = st.text_input("Phone Number", value="+91")
message = st.text_area("Your Message", placeholder="Hi! Just wanted to say hello 👋")

if st.button("Send Now"):
    if not is_valid_number(phone) or not message.strip():
        st.warning("Please enter a valid number and message.")
    else:
        try:
            st.info("Opening WhatsApp Web... please wait a few seconds.")
            kit.sendwhatmsg_instantly(
                phone_no=phone,
                message=message,
                wait_time=10,
                tab_close=True
            )
            st.success("✅ Message sent! Check your WhatsApp.")
        except Exception as e:
            st.error("Something went wrong.")
            st.text(str(e))

# Footer
st.markdown("---")
st.caption("🔒 Your messages are sent through your own WhatsApp. Nothing is stored or shared.")
