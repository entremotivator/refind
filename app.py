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
        st.write(f"**Address Line 1:** {property_info.get('addressLine1', 'N/A')}")
        st.write(f"**City:** {property_info.get('city', 'N/A')}")
        st.write(f"**State:** {property_info.get('state', 'N/A')}")
        st.write(f"**Zip Code:** {property_info.get('zipCode', 'N/A')}")
        st.write(f"**Formatted Address:** {property_info.get('formattedAddress', 'N/A')}")
        st.write(f"**Assessor ID:** {property_info.get('assessorID', 'N/A')}")
        st.write(f"**Bedrooms:** {property_info.get('bedrooms', 'N/A')}")
        st.write(f"**County:** {property_info.get('county', 'N/A')}")
        st.write(f"**Legal Description:** {property_info.get('legalDescription', 'N/A')}")
        st.write(f"**Square Footage:** {property_info.get('squareFootage', 'N/A')}")
        st.write(f"**Subdivision:** {property_info.get('subdivision', 'N/A')}")
        st.write(f"**Year Built:** {property_info.get('yearBuilt', 'N/A')}")
        st.write(f"**Bathrooms:** {property_info.get('bathrooms', 'N/A')}")
        st.write(f"**Lot Size:** {property_info.get('lotSize', 'N/A')}")
        st.write(f"**Property Type:** {property_info.get('propertyType', 'N/A')}")
        st.write(f"**Last Sale Date:** {property_info.get('lastSaleDate', 'N/A')}")

        st.write("#### Features:")
        features = property_info.get('features', {})
        st.write(f"**Architecture Type:** {features.get('architectureType', 'N/A')}")
        st.write(f"**Cooling:** {features.get('cooling', 'N/A')}")
        st.write(f"**Cooling Type:** {features.get('coolingType', 'N/A')}")
        st.write(f"**Exterior Type:** {features.get('exteriorType', 'N/A')}")
        st.write(f"**Floor Count:** {features.get('floorCount', 'N/A')}")
        st.write(f"**Foundation Type:** {features.get('foundationType', 'N/A')}")
        st.write(f"**Garage:** {features.get('garage', 'N/A')}")
        st.write(f"**Garage Type:** {features.get('garageType', 'N/A')}")
        st.write(f"**Heating:** {features.get('heating', 'N/A')}")
        st.write(f"**Heating Type:** {features.get('heatingType', 'N/A')}")
        st.write(f"**Pool:** {features.get('pool', 'N/A')}")
        st.write(f"**Roof Type:** {features.get('roofType', 'N/A')}")
        st.write(f"**Room Count:** {features.get('roomCount', 'N/A')}")
        st.write(f"**Unit Count:** {features.get('unitCount', 'N/A')}")

        st.write("#### Tax Assessment:")
        tax_assessment = property_info.get('taxAssessment', {})
        for year, values in tax_assessment.items():
            st.write(f"**{year}:**")
            st.write(f"  - Value: {values.get('value', 'N/A')}")
            st.write(f"  - Land: {values.get('land', 'N/A')}")
            st.write(f"  - Improvements: {values.get('improvements', 'N/A')}")

        st.write("#### Property Taxes:")
        property_taxes = property_info.get('propertyTaxes', {})
        for year, values in property_taxes.items():
            st.write(f"**{year}:** Total: {values.get('total', 'N/A')}")

        st.write("#### Owner Information:")
        owner = property_info.get('owner', {})
        st.write(f"**Owner Name(s):** {', '.join(owner.get('names', ['N/A']))}")
        mailing_address = owner.get('mailingAddress', {})
        st.write("**Mailing Address:**")
        st.write(f"  - ID: {mailing_address.get('id', 'N/A')}")
        st.write(f"  - Address Line 1: {mailing_address.get('addressLine1', 'N/A')}")
        st.write(f"  - City: {mailing_address.get('city', 'N/A')}")
        st.write(f"  - State: {mailing_address.get('state', 'N/A')}")
        st.write(f"  - Zip Code: {mailing_address.get('zipCode', 'N/A')}")

        st.write(f"**ID:** {property_info.get('id', 'N/A')}")
        st.write(f"**Longitude:** {property_info.get('longitude', 'N/A')}")
        st.write(f"**Latitude:** {property_info.get('latitude', 'N/A')}")

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
