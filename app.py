import streamlit as st
from pymongo import MongoClient
from datetime import datetime

# ---------------- DATABASE ----------------
MONGO_URI = "mongodb+srv://manitridev7890_db_user:admin123@cluster0.pshh6gw.mongodb.net/user_form_db?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
db = client["user_form_db"]
collection = db["citizen_survey"]

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Citizen Survey", layout="wide")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
.section-card {
    background: white;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.05);
}
h1, h2, h3 {
    color: #1f2937;
}
.stButton>button {
    background-color: #2563eb;
    color: white;
    border-radius: 8px;
    height: 45px;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.title("🌍 Urban Public Issues & Citizen Feedback Survey")
st.caption("Help improve your city by sharing your valuable feedback")

# ---------------- FORM ----------------
with st.form("survey_form"):

    col_left, col_right = st.columns(2)

    # -------- LEFT SIDE --------
    with col_left:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.subheader("👤 Basic Information")

        name = st.text_input("Full Name")
        age = st.number_input("Age", 15, 100)
        gender = st.radio("Gender", ["Male", "Female", "Other"])
        city = st.text_input("City")
        state = st.selectbox("State", ["Karnataka", "Telangana", "Tamil Nadu", "Other"])
        occupation = st.selectbox("Occupation", ["Student", "Employee", "Business", "Other"])

        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.subheader("🚧 Infrastructure")

        road_quality = st.slider("Road Quality", 1, 5)
        transport = st.radio("Public Transport", ["Good", "Average", "Poor"])

        issues = st.multiselect("Major Issues", [
            "Traffic", "Pollution", "Water shortage", "Waste management", "Power cuts"
        ])

        st.markdown('</div>', unsafe_allow_html=True)

    # -------- RIGHT SIDE --------
    with col_right:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.subheader("🌱 Environment")

        cleanliness = st.slider("Cleanliness Level", 1, 5)
        green_spaces = st.checkbox("Access to Parks/Green Spaces")

        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.subheader("🚓 Safety")

        safety = st.slider("Safety Level", 1, 5)
        crime = st.radio("Crime Rate", ["High", "Moderate", "Low"])

        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.subheader("💡 Suggestions")

        priority = st.selectbox("Top Priority", [
            "Infrastructure", "Environment", "Safety", "Employment"
        ])

        participate = st.checkbox("Willing to participate in community programs")
        feedback = st.text_area("Additional Suggestions")

        agree = st.checkbox("I confirm the information is accurate")

        st.markdown('</div>', unsafe_allow_html=True)

    # -------- SUBMIT BUTTON --------
    submit = st.form_submit_button(" Submit Survey")

# ---------------- VALIDATION + SAVE ----------------
if submit:
    errors = []

    if not name:
        errors.append("Name is required")
    if not city:
        errors.append("City is required")
    if not issues:
        errors.append("Select at least one issue")
    if not agree:
        errors.append("Please confirm accuracy")

    if errors:
        for e in errors:
            st.error(e)
    else:
        collection.insert_one({
            "name": name,
            "age": age,
            "gender": gender,
            "city": city,
            "state": state,
            "occupation": occupation,
            "road_quality": road_quality,
            "transport": transport,
            "issues": issues,
            "cleanliness": cleanliness,
            "green_spaces": green_spaces,
            "safety": safety,
            "crime": crime,
            "priority": priority,
            "participate": participate,
            "feedback": feedback,
            "timestamp": datetime.now()
        })

        st.success("✅ Thank you! Your response has been recorded.")