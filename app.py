import streamlit as st
import csv
import json
from urllib.parse import quote

# Function to get property information from the API
def get_property_info(api_key, address):
    # Your existing code for making API requests

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
                property_data = properties[0]

                # Basic property details
                st.subheader("Basic Details:")
                st.write(f"**Address:** {property_data['formattedAddress']}")
                st.write(f"**Assessor ID:** {property_data['assessorID']}")
                st.write(f"**Bedrooms:** {property_data['bedrooms']}")
                st.write(f"**Bathrooms:** {property_data['bathrooms']}")
                st.write(f"**Square Footage:** {property_data['squareFootage']} sq. ft.")
                st.write(f"**Year Built:** {property_data['yearBuilt']}")
                st.write(f"**Property Type:** {property_data['propertyType']}")

                # Features
                st.subheader("Features:")
                features = property_data['features']
                for feature, value in features.items():
                    st.write(f"**{feature}:** {value}")

                # Tax Assessment
                st.subheader("Tax Assessment:")
                tax_assessment = property_data['taxAssessment']
                for year, details in tax_assessment.items():
                    st.write(f"**Year {year}:** Value: {details['value']}, Land: {details['land']}, Improvements: {details['improvements']}")

                # Property Taxes
                st.subheader("Property Taxes:")
                property_taxes = property_data['propertyTaxes']
                for year, details in property_taxes.items():
                    st.write(f"**Year {year}:** Total: {details['total']}")

                # Owner Information
                st.subheader("Owner Information:")
                owner = property_data['owner']
                st.write(f"**Owner Name(s):** {', '.join(owner['names'])}")
                mailing_address = owner['mailingAddress']
                st.write(f"**Mailing Address:** {mailing_address['addressLine1']}, {mailing_address['city']}, {mailing_address['state']} {mailing_address['zipCode']}")

                # Geographical Information
                st.subheader("Geographical Information:")
                st.write(f"**Longitude:** {property_data['longitude']}")
                st.write(f"**Latitude:** {property_data['latitude']}")

                # Export to CSV
                if st.button("Export to CSV"):
                    with open("property_info.csv", "w", newline="") as csvfile:
                        csv_writer = csv.writer(csvfile)
                        csv_writer.writerow(property_data.keys())
                        csv_writer.writerow(property_data.values())
                    st.success("Data exported successfully to property_info.csv.")
            else:
                st.warning("No data available for the provided address.")
        else:
            st.warning("Please provide both API key and address.")

if __name__ == "__main__":
    main()
