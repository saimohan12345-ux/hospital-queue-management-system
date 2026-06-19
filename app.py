import streamlit as st

if "queue" not in st.session_state:
    st.session_state.queue = []

st.title("🏥 Hospital Queue Management System")

st.header("Add Patient")

name = st.text_input("Patient Name")
age = st.number_input("Age", min_value=1, max_value=120)

token = st.number_input(
    "Token Number",
    min_value=1,
    step=1
)

priority = st.selectbox(
    "Priority",
    [1, 2, 3, 4]
)

department = st.selectbox(
    "Department",
    ["ICU", "OPD", "General"]
)

if st.button("Add Patient"):

    patient = {
        "name": name,
        "age": age,
        "token": token,
        "priority": priority,
        "department": department
    }

    st.session_state.queue.append(patient)

    st.session_state.queue.sort(
        key=lambda x: x["priority"]
    )

    st.success("Patient Added Successfully")

st.header("Current Queue")

if st.session_state.queue:
    st.table(st.session_state.queue)

if st.button("Treat Patient"):

    if st.session_state.queue:

        treated = st.session_state.queue.pop(0)

        st.success(
            f"Patient Treated: {treated['name']}"
        )