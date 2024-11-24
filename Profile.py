import gspread
from google.oauth2 import service_account
import streamlit as st
import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io

def app():  # Access credentials from Streamlit's secrets
    secrets = st.secrets["connections"]["gsheets"]

    # Define the scope for Google Sheets API and Google Drive API
    scope = ["https://www.googleapis.com/auth/spreadsheets", 
             "https://www.googleapis.com/auth/drive.file", 
             "https://www.googleapis.com/auth/drive"]

    # Create credentials using the secrets
    creds_dict = {
        "type": secrets["type"],
        "project_id": secrets["project_id"],
        "private_key_id": secrets["private_key_id"],
        "private_key": secrets["private_key"].replace("\\n", "\n"),
        "client_email": secrets["client_email"],
        "client_id": secrets["client_id"],
        "auth_uri": secrets["auth_uri"],
        "token_uri": secrets["token_uri"],
        "auth_provider_x509_cert_url": secrets["auth_provider_x509_cert_url"],
        "client_x509_cert_url": secrets["client_x509_cert_url"]
    }

    # Use google-auth for authentication
    credentials = service_account.Credentials.from_service_account_info(creds_dict, scopes=scope)

    # Use gspread with the credentials to access Google Sheets
    client = gspread.authorize(credentials)

    # Open the Google Sheet using the URL or spreadsheet ID from secrets
    spreadsheet_url = secrets["spreadsheet"]
    spreadsheet = client.open_by_url(spreadsheet_url)

    # Get the desired worksheet (replace "Sheet1" with your actual sheet name or GID)
    worksheet = spreadsheet.worksheet(secrets["worksheet"])

    # Fetch all records from the sheet
    data = worksheet.get_all_records()

    # Convert to DataFrame for easier display
    df = pd.DataFrame(data)

    # Streamlit title and header
    st.title("Profile Page")
    st.header("Real-time Attendance Data")

    # Add a text input for the user to search by Student ID
    search_id = st.text_input("Enter Student ID to search:")

    # Function to fetch image from Google Drive by File ID
    def fetch_image_from_drive(file_id):
        drive_service = build('drive', 'v3', credentials=credentials)
        request = drive_service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
        fh.seek(0)
        return fh

    # If a search ID is entered, filter the data
    if search_id:
        filtered_df = df[df['STUDENT ID'].astype(str) == search_id]
        if not filtered_df.empty:
            # Display the profile of the matching student
            profile = filtered_df.iloc[0]  # Since we expect only one match
            st.subheader(f"Profile for Student ID: {profile['STUDENT ID']}")

            with st.form(key="student_profile_form"):
                col1, col2 = st.columns([1, 3])

                with col1:
                    st.text_input("Student ID", value=profile['STUDENT ID'], disabled=True)
                    st.text_input("RFID", value=profile['RFID'], disabled=True)
                    st.text_input("Name", value=profile['NAME'], disabled=True)
                    st.text_area("Subjects", value=profile['SUBJECTS'], disabled=True)

                with col2:
                    # Displaying Picture
                    if profile.get('PICTURE_FILE_ID'):
                        try:
                            image_file = fetch_image_from_drive(profile['PICTURE_FILE_ID'])
                            st.image(image_file, use_column_width=True)
                        except Exception as e:
                            st.write("Failed to load picture.")
                            st.write(f"Error: {e}")
                    else:
                        st.write("No picture available.")

                # Submit button (if you want to add any actions to the form)
                submit_button = st.form_submit_button(label="Submit")
                if submit_button:
                    st.success("Profile loaded successfully.")
        else:
            st.warning(f"No profile found for Student ID: {search_id}")
