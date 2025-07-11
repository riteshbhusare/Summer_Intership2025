import streamlit as st
from twilio.rest import Client
import os
import requests

ACCOUNT_SID = "ACxxxxxxxxxxxxxxxxxxxxxxxxx6f"
AUTH_TOKEN = "b9xxxxxxxxxxxxxxxxxxxxxxxxxx2e"
TWILIO_PHONE = "+xxxxxxxxxxxxxx10"  

st.set_page_config(page_title="📞Call Sender", page_icon="📱", layout="centered")
st.title("📞Voice Caller")
st.markdown("Send a real voice call.")

to_number = st.text_input("Recipient Phone Number", "+91XXXXXXXXXX")
voice_message = st.text_area("What do you want the call to say?", "Hello! This is a test call using Python.")

if st.button("📞 Call Now"):
    if not to_number.strip() or not voice_message.strip():
        st.warning("Please enter both phone number and message.")
    else:
        twiml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Say voice="alice">{voice_message}</Say>
</Response>"""

        fallback_twiml_url = "http://demo.twilio.com/docs/voice.xml"

        try:
            client = Client(ACCOUNT_SID, AUTH_TOKEN)

            call = client.calls.create(
                to=to_number,
                from_=TWILIO_PHONE,
                url=fallback_twiml_url  
            )

            st.success(f"✅ Call initiated! Call SID: {call.sid}")
        except Exception as e:
            st.error(f"❌ Failed to initiate call: {e}")

