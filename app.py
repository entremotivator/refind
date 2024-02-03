import csv
import json
from urllib.parse import quote
import PyPDF2
from io import BytesIO

import streamlit as st

# Function to get property information from the API
def get_property_info(api_key, address):
    # (unchanged code)

# Function to export properties to PDF using PyPDF2
def export_to_pdf(properties):
    pdf_buffer = BytesIO()
    pdf_writer = PyPDF2.PdfWriter()

    # Create PDF document
    pdf_writer.add_page()
    pdf_writer.set_font("Arial", size=12)

    # Add content to the PDF
    pdf_writer.cell(200, 10, txt="Property Information Report", ln=True, align='C')

    for property_data in properties:
        for key, value in property_data.items():
            pdf_writer.cell(200, 10, txt=f"{key}: {value}", ln=True)

    # Save PDF to buffer
    pdf_buffer.seek(0)
    pdf_writer.output(pdf_buffer)

    return pdf_buffer

# Main Streamlit app
def main():
    st.title("Realtor Property Information App")

    # Sidebar for user input
    st.sidebar.header("User Input:")
    api_key = st.sidebar.text_input("Enter your API key", help="Get it from Realty Mole API")
    address = st.sidebar.text_input("Enter the address", help="E.g., 5500 Grand Lake Dr, San Antonio, TX, 78244")

    if st.sidebar.button("Get Property Info"):
        if api_key and address:
            with st.spinner("Fetching property information..."):
                properties = get_property_info(api_key, address)
            if properties:
                # Display organized property information
                st.write("### Property Information:")
                for property_data in properties:
                    for key, value in property_data.items():
                        st.write(f"**{key}:** {value}")

                # Export options
                if st.button("Export to CSV"):
                    with open("property_info.csv", "w", newline="") as csvfile:
                        csv_writer = csv.writer(csvfile)
                        csv_writer.writerow(properties[0].keys())  # assuming all properties have the same keys
                        for property_data in properties:
                            csv_writer.writerow(property_data.values())
                    st.success("Data exported successfully to property_info.csv.")

                if st.button("Export to PDF"):
                    pdf_buffer = export_to_pdf(properties)
                    st.download_button("Download PDF", pdf_buffer, file_name="property_info_report.pdf", key="pdf")

                # CSV import option
                uploaded_file = st.file_uploader("Upload CSV for Import", type=["csv"])
                if uploaded_file:
                    imported_properties = []
                    csv_reader = csv.DictReader(uploaded_file)
                    for row in csv_reader:
                        imported_properties.append(dict(row))
                    st.write("### Imported Property Information:")
                    for property_data in imported_properties:
                        for key, value in property_data.items():
                            st.write(f"**{key}:** {value}")

            else:
                st.warning("No data available for the provided address.")
        else:
            st.warning("Please provide both API key and address.")

if __name__ == "__main__":
    main()
