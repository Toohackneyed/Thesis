import streamlit as st
import pandas as pd
import time

# Admin credentials
ADMIN_CREDENTIALS = {
    "admin": "securepass"
}

def Admin():
    # Admin login management
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        with st.form("Admin Access"):
            st.subheader("Admin Login")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submit_btn = st.form_submit_button("Login")

            if submit_btn:
                if username in ADMIN_CREDENTIALS and password == ADMIN_CREDENTIALS[username]:
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.success("Login Successfully!")

                    message_box_placeholder = st.empty()

                    message_box_placeholder.markdown(
                        f'<div style="position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); background-color: #f9f9f9; border-radius: 10px; padding: 20px 30px; border: 1px solid #ddd; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); z-index: 9999; width: auto; text-align: center;">'
                        f'<strong>Welcome, Admin!</strong></div>',
                        unsafe_allow_html=True
                    )
                    time.sleep(3)
                    message_box_placeholder.empty()

                else:
                    st.error("Invalid username or password!")

    return st.session_state.logged_in  # Return login status

def student_management_page():
    # Admin is logged in, show the student management system
    if "students_data" not in st.session_state:
        st.session_state.students_data = pd.DataFrame({
            "Student ID": [101, 102, 103],
            "Name": ["Alice", "Bob", "Charlie"],
            "Age": [20, 21, 22],
            "Course": ["Engineering", "Engineering", "Engineering"]
        })

    students_data = st.session_state.students_data  # Access data from session_state

    st.title("Student Enrollment System")

    # Display the student data table
    st.subheader("Student Information")
    st.dataframe(students_data)

    # Search for a student by ID
    st.subheader("Search Student by ID")
    student_id_search = st.text_input("Enter Student ID to search")

    if student_id_search:
        student_to_search = students_data[students_data["Student ID"] == int(student_id_search)]

        if not student_to_search.empty:
            st.write("Student Found:")
            st.write(student_to_search)

            # Edit student
            st.subheader("Edit Student")
            edited_name = st.text_input("Name", value=student_to_search["Name"].values[0])
            edited_age = st.number_input("Age", min_value=18, value=student_to_search["Age"].values[0])
            edited_course = st.text_input("Course", value=student_to_search["Course"].values[0])

            if st.button("Update Student"):
                st.session_state.students_data.loc[students_data["Student ID"] == int(student_id_search), "Name"] = edited_name
                st.session_state.students_data.loc[students_data["Student ID"] == int(student_id_search), "Age"] = edited_age
                st.session_state.students_data.loc[students_data["Student ID"] == int(student_id_search), "Course"] = edited_course
                st.success(f"Student {edited_name} updated successfully!")

            # Delete student
            if st.button("Delete Student"):
                # Remove the student from the dataframe
                st.session_state.students_data = students_data[students_data["Student ID"] != int(student_id_search)]
                st.success(f"Student with ID {student_id_search} has been deleted!")
        else:
            st.warning("No student found with this ID")

    # Add student
    st.subheader("Add Student")
    student_id = st.text_input("Student ID (for new student)")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=18)
    course = st.text_input("Course")

    if st.button("Add Student"):
        if student_id and name and age and course:
            # Add student to the DataFrame
            new_student = pd.DataFrame({"Student ID": [student_id], "Name": [name], "Age": [age], "Course": [course]})
            st.session_state.students_data = pd.concat([students_data, new_student], ignore_index=True)
            st.success(f"Student {name} added successfully!")

    # Display updated table
    st.subheader("Updated Student Information")
    st.dataframe(st.session_state.students_data)

def app():
    # Admin login check
    if not Admin():  # If admin is not logged in, show the login page
        return

    # If logged in, show the student management page
    student_management_page()

# Run the app
if __name__ == "__main__":
    app()
