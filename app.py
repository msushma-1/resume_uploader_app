import streamlit as st

st.title("Resume Upload App")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    st.success("✓ Resume Uploaded Successfully")


    st.write("Filename:")
    st.write(uploaded_file.name)

    st.write("File Type:")
    st.write(uploaded_file.type)

    st.write("File Size:")
    st.write(f"{uploaded_file.size / 1024:.2f} KB")

  
