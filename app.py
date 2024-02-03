import streamlit as st
import requests

def get_property_info(api_key, address):
    api_url = f'https://api.propertymole.com/v1/property?address={address}&apikey={api_key}'

    try:
        response = requests.get(api_url)
        data = response.json()
        return data  # Now returning a list of properties
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None

def display_property_info(properties):
    for property_info in properties:
        st.write("### Property Information:")
        st.write(f"**Address:** {property_info['formattedAddress']}")
        st.write(f"**City:** {property_info['city']}")
        st.write(f"**State:** {property_info['state']}")
        st.write(f"**Zip Code:** {property_info['zipCode']}")
        st.write(f"**Assessor ID:** {property_info['assessorID']}")
        st.write(f"**Bedrooms:** {property_info['bedrooms']}")
        st.write(f"**County:** {property_info['county']}")
        st.write(f"**Legal Description:** {property_info['legalDescription']}")
        st.write(f"**Square Footage:** {property_info['squareFootage']}")
        st.write(f"**Subdivision:** {property_info['subdivision']}")
        st.write(f"**Year Built:** {property_info['yearBuilt']}")
        st.write(f"**Bathrooms:** {property_info['bathrooms']}")
        st.write(f"**Lot Size:** {property_info['lotSize']}")
        st.write(f"**Property Type:** {property_info['propertyType']}")
        st.write(f"**Last Sale Date:** {property_info['lastSaleDate']}")

        st.write("#### Features:")
        features = property_info['features']
        for key, value in features.items():
            st.write(f"**{key}:** {value}")

        st.write("#### Tax Assessment:")
        tax_assessment = property_info['taxAssessment']
        for year, values in tax_assessment.items():
            st.write(f"**{year}:**")
            st.write(f"  - Value: {values['value']}")
            st.write(f"  - Land: {values['land']}")
            st.write(f"  - Improvements: {values['improvements']}")

        st.write("#### Property Taxes:")
        property_taxes = property_info['propertyTaxes']
        for year, values in property_taxes.items():
            st.write(f"**{year}:** Total: {values['total']}")

        st.write("#### Owner Information:")
        owner = property_info['owner']
        st.write(f"**Owner Name(s):** {', '.join(owner['names'])}")
        st.write("**Mailing Address:**")
        st.write(f"  - Address Line 1: {owner['mailingAddress']['addressLine1']}")
        st.write(f"  - City: {owner['mailingAddress']['city']}")
        st.write(f"  - State: {owner['mailingAddress']['state']}")
        st.write(f"  - Zip Code: {owner['mailingAddress']['zipCode']}")

        st.markdown("---")  # Add a horizontal line between properties

def main():
    st.title("Realtor Property Information App")

    # Sidebar for user input
    st.sidebar.header("User Input:")
    api_key = st.sidebar.text_input("Enter your API key:")
    address = st.sidebar.text_input("Enter the address:")

    if st.sidebar.button("Get Property Info"):
        if api_key and address:
            properties = get_property_info(api_key, address)
            if properties:
                display_property_info(properties)
            else:
                st.warning("No data available for the provided address.")

if __name__ == "__main__":
    main()
