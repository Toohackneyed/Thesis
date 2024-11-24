import streamlit as st
import gspread
from google.oauth2 import service_account
import pandas as pd
import time
import json
import os

CREDENTIALS_FILE = 'admin_credentials.json'

def load_credentials():
    """Load admin credentials from the JSON file."""
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, 'r') as file:
            return json.load(file)
    st.error(f"Credentials file not found: {os.path.abspath(CREDENTIALS_FILE)}")  # Debugging line
    return {}

def save_credentials(credentials):
    """Save the updated admin credentials to the JSON file."""
    with open(CREDENTIALS_FILE, 'w') as file:
        json.dump(credentials, file, indent=4)

def authenticate_google_sheets():
    try:
        # Define the scope
        scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

        # Load the credentials from Streamlit secrets
        credentials = service_account.Credentials.from_service_account_info(
            st.secrets["connections"]["gsheets"],  # This gets the service account info
            scopes=scope
        )

        # Authorize and access the Google Sheets
        client = gspread.authorize(credentials)
        sheet = client.open_by_url(st.secrets["connections"]["gsheets"]["spreadsheet"]).sheet1
        return sheet
    except KeyError as e:
        st.error(f"Missing key in Streamlit secrets: {e}")
        st.stop()
    except Exception as e:
        st.error(f"Failed to connect to Google Sheets: {e}")
        st.stop()
# Fetch data from Google Sheets and return as DataFrame
def fetch_data_from_sheets(sheet):
    try:
        data = sheet.get_all_records()
        return pd.DataFrame(data)
    except Exception as e:
        st.error(f"Failed to fetch data from Google Sheets: {e}")
        st.stop()

def update_sheet(sheet, df):
    sheet.clear()
    sheet.update([df.columns.values.tolist()] + df.values.tolist())

def authenticate_admin():
    """Authenticates the admin using credentials loaded from the JSON file."""
    credentials = load_credentials()
    return credentials

def Admin():
    # Initialize session state for admin login
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    # Admin Login
    if not st.session_state.logged_in:
        with st.form("Admin Login"):
            st.subheader("Admin Login")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submit_btn = st.form_submit_button("Login", help="Log in with your admin credentials")

            # Authentication Check
            credentials = load_credentials()
            if submit_btn:
                if username in credentials and password == credentials[username]:
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.success("Login successful!")
                    time.sleep(1)
                else:
                    st.error("Invalid username or password!")
        return False 
    return True

def logout():
    """Handles admin logout."""
    st.session_state.logged_in = False
    st.session_state.username = None
    st.success("Logged out successfully!")

def change_password():
    """Allows the admin to change their password."""
    st.subheader("Change Password")
    with st.form("Change Password"):
        current_password = st.text_input("Current Password", type="password")
        new_password = st.text_input("New Password", type="password")
        confirm_password = st.text_input("Confirm New Password", type="password")
        change_btn = st.form_submit_button("Change Password")
        
        if change_btn:
            credentials = load_credentials()
            username = st.session_state.get("username")
            if username and current_password == credentials.get(username):
                if new_password == confirm_password:
                    credentials[username] = new_password
                    save_credentials(credentials)  # Save the updated credentials
                    st.success("Password changed successfully!")
                else:
                    st.error("New password and confirmation do not match!")
            else:
                st.error("Incorrect current password!")

def refresh_data(sheet):
    st.session_state.students_data = fetch_data_from_sheets(sheet)
# Student Management Page
def student_management_page(sheet):
    if "students_data" not in st.session_state:
        st.session_state.students_data = fetch_data_from_sheets(sheet)

    students_data = st.session_state.students_data

    if "toggle_change_password" not in st.session_state:
        st.session_state.toggle_change_password = False

    col1, col2, col3 = st.columns([1, 4, 1])
    with col3:
        if st.button("Logout", help="Log out of the admin account"):
            logout()
            return
        change_password_btn = st.button("Change Password", help="Change your admin password")
        if change_password_btn:
            st.session_state.toggle_change_password = not st.session_state.toggle_change_password

    if st.session_state.toggle_change_password:
        change_password()
        return 

    st.header("Student Enrollment System")
    st.subheader("Student Information")

    columns_to_display = ["RFID", "STUDENT ID", "NAME", "SUBJECTS", "UNITS"]
    st.dataframe(students_data[columns_to_display].head(5)) # Display only the first 5 rows

    st.subheader("Search Student by ID")
    student_id_search = st.text_input("Enter STUDENT ID to search")

    if student_id_search:
        # Gamitin ang `str.contains` para sa paghahanap ng bahaging tumutugma
        student_to_search = students_data[students_data["STUDENT ID"].astype(str).str.contains(student_id_search, na=False, case=False)]
        if not student_to_search.empty:
            st.write("Matching Students Found:")
            st.write(student_to_search[columns_to_display])  # Tanging mga napiling kolum lang ang ipapakita

            # Delete Option
            delete_btn = st.button(f"Delete Student {student_id_search}")
            if delete_btn:
                st.session_state.students_data = st.session_state.students_data[students_data["STUDENT ID"] != int(student_id_search)]
                update_sheet(sheet, st.session_state.students_data)
                refresh_data(sheet) 
                st.success(f"Student ID {student_id_search} deleted successfully!")
                return

            st.subheader("Edit Student")
            with st.form("Edit Student"):
                col1, col2, col3 = st.columns(3)
                with col1:
                    edited_rfid = st.number_input("RFID", min_value=1, value=student_to_search["RFID"].values[0])
                with col2:
                    edited_name = st.text_input("NAME", value=student_to_search["NAME"].values[0])
                with col3:
                    edited_units = st.number_input("UNITS", min_value=1, value=student_to_search["UNITS"].values[0])

                col4, col5 = st.columns(2)
                with col4:
                    edited_subjects = st.text_input("SUBJECTS", value=student_to_search["SUBJECTS"].values[0])
                with col5:
                    edited_course = st.text_input("COURSE", value=student_to_search["COURSE"].values[0])

                update_btn = st.form_submit_button("Update Student")
                if update_btn:
                    st.session_state.students_data.loc[students_data["STUDENT ID"] == int(student_id_search), "RFID"] = edited_rfid
                    st.session_state.students_data.loc[students_data["STUDENT ID"] == int(student_id_search), "NAME"] = edited_name
                    st.session_state.students_data.loc[students_data["STUDENT ID"] == int(student_id_search), "UNITS"] = edited_units
                    st.session_state.students_data.loc[students_data["STUDENT ID"] == int(student_id_search), "SUBJECTS"] = edited_subjects
                    st.session_state.students_data.loc[students_data["STUDENT ID"] == int(student_id_search), "COURSE"] = edited_course
                    update_sheet(sheet, st.session_state.students_data)
                    st.success(f"Student {edited_name} updated successfully!")

        else:
            st.warning("No student found with this ID")

    st.subheader("Add Student")
    with st.form("Add Student"):
        col1, col2, col3 = st.columns(3)
        with col1:
            rfid = st.number_input("RFID", min_value=1)
        with col2:
            student_id = st.text_input("STUDENT ID (for new student)")
        with col3:
            name = st.text_input("NAME")

        col4, col5 = st.columns(2)
        with col4:
            units = st.number_input("UNITS", min_value=1)
        with col5:
            subjects = st.text_input("SUBJECTS")

        course = st.text_input("COURSE")

        add_btn = st.form_submit_button("Add Student")
        if add_btn:
            if rfid and student_id and name and units and subjects and course:
                new_student = pd.DataFrame({"RFID": [rfid], "STUDENT ID": [student_id], "NAME": [name], "UNITS": [units], "SUBJECTS": [subjects], "COURSE": [course]})
                st.session_state.students_data = pd.concat([students_data, new_student], ignore_index=True)
                update_sheet(sheet, st.session_state.students_data)
                st.success(f"Student {name} added successfully!")

    st.subheader("Updated Student Information")
    columns_to_display = ["RFID", "STUDENT ID", "NAME", "SUBJECTS", "UNITS"]
    st.dataframe(st.session_state.students_data[columns_to_display].head(5))

# Main App
def app():
    sheet = authenticate_google_sheets()

    if not Admin():
        return
    student_management_page(sheet)

if __name__ == "__main__":
    app()
