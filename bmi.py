import streamlit as st

st.set_page_config(page_title="BMI App", page_icon="⚖️")

menu = st.sidebar.radio("Select the Page", ["BMI Calculator", "BMI Info Chart"])

if menu == "BMI Calculator":

    st.title('⚖️ BMI (Body Mass Index) Calculator')

    # Weight input
    weight = st.number_input("Enter your weight (in kgs)", min_value=1.0)

    # Height format
    status = st.radio('Select your height format:', ('centimeter', 'meters', 'feet'))

    height = 0

    if status == 'centimeter':
        height = st.number_input('Enter height in centimeters', min_value=1.0)
        height_in_m = height / 100

    elif status == 'meters':
        height = st.number_input('Enter height in meters', min_value=0.1)
        height_in_m = height

    elif status == 'feet':
        height = st.number_input('Enter height in feet', min_value=0.1)
        height_in_m = height / 3.28

    if st.button('💡 Calculate BMI'):
        try:
            bmi = weight / (height_in_m ** 2)
            st.success(f"Your BMI Index is: **{bmi:.2f}**")

            if bmi < 16:
                st.error("🚨 You are **Extremely Underweight** 🦴")
            elif 16 <= bmi < 18.5:
                st.warning("⚠️ You are **Underweight**")
            elif 18.5 <= bmi < 25:
                st.success("✅ You are **Healthy** 💪")
            elif 25 <= bmi < 30:
                st.warning("⚠️ You are **Overweight**")
            else:
                st.error("🚨 You are **Extremely Overweight** 🍔")
        except:
            st.error("Please enter valid height and weight.")

elif menu == "BMI Info Chart":
    st.title("📊 BMI Category Chart")
    st.markdown("""
| BMI Range       | Category                |
|------------------|--------------------------|
| < 16            | Extremely Underweight   |
| 16 - 18.5       | Underweight             |
| 18.5 - 24.9     | Healthy                 |
| 25 - 29.9       | Overweight              |
| 30+             | Extremely Overweight    |
""")
    st.info("BMI = Weight (kg) / (Height (m))²")
    st.markdown("👉 Use the sidebar to go back to calculator.")
