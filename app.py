import streamlit as st
import http.client
import json
from urllib.parse import quote

# Function to make the API request
def make_api_request(api_key, address):
    try:
        conn = http.client.HTTPSConnection("realty-mole-property-api.p.rapidapi.com")
        headers = {
            'X-RapidAPI-Key': api_key,
            'X-RapidAPI-Host': 'realty-mole-property-api.p.rapidapi.com'
        }

        encoded_address = quote(address)
        conn.request("GET", f"/properties?address={encoded_address}", headers=headers)
        res = conn.getresponse()

        if 'application/json' in res.getheader('Content-Type', ''):
            data = res.read().decode("utf-8")
            return json.loads(data)
        else:
            return None

    except Exception as e:
        return None

    finally:
        conn.close()

# Function to handle API response
def handle_api_response(api_key, address):
    properties = make_api_request(api_key, address)
    
    if properties:
        return properties
    else:
        st.warning("Failed to fetch property information. Please check your API key and address.")
        return None

# Function to display property information with improved formatting
def display_property_info(property_data):
    st.write("### Property Information:")
    st.write(f"**Address:** {property_data['formattedAddress']}")
    st.write(f"**Assessor ID:** {property_data['assessorID']}")
    st.write(f"**Bedrooms:** {property_data['bedrooms']}")
    st.write(f"**Bathrooms:** {property_data['bathrooms']}")
    st.write(f"**Square Footage:** {property_data['squareFootage']}")
    st.write(f"**Year Built:** {property_data['yearBuilt']}")
    st.write(f"**Lot Size:** {property_data['lotSize']}")
    st.write(f"**Property Type:** {property_data['propertyType']}")
    st.write(f"**Last Sale Date:** {property_data['lastSaleDate']}")
    st.write(f"**Last Sale Price:** {property_data['lastSalePrice']}")
    st.write(f"**Owner Occupied:** {'Yes' if property_data['ownerOccupied'] else 'No'}")
    
    st.write("#### Features:")
    for key, value in property_data['features'].items():
        st.write(f"**{key}:** {value}")

    st.write("#### Tax Assessment:")
    for year, data in property_data['taxAssessment'].items():
        st.write(f"**Year {year}:** {data['value']} (Land: {data['land']}, Improvements: {data['improvements']})")

    st.write("#### Owner:")
    st.write(f"**Name(s):** {', '.join(property_data['owner']['names'])}")
    st.write(f"**Mailing Address:** {property_data['owner']['mailingAddress']['addressLine1']}, {property_data['owner']['mailingAddress']['city']}, {property_data['owner']['mailingAddress']['state']} {property_data['owner']['mailingAddress']['zipCode']}")

    st.write("#### Property Taxes:")
    for year, data in property_data['propertyTaxes'].items():
        st.write(f"**Year {year}:** {data['total']}")

    st.write(f"**ID:** {property_data['id']}")
    st.write(f"**Longitude:** {property_data['longitude']}")
    st.write(f"**Latitude:** {property_data['latitude']}")

# Function to generate a 200-word letter with custom information
def generate_letter(property_data, buyer_name, buyer_contact, personalized_message):
    return f"Dear {property_data['owner']['names'][0]},\n\nI hope this letter finds you well. My name is {buyer_name}, and I am interested in purchasing your property located at {property_data['formattedAddress']}. Having learned about its features, including {property_data['features']}, and considering its {property_data['propertyType']} type, I believe it would be an ideal fit for me.\n\nI am impressed by the {property_data['squareFootage']} square footage, {property_data['bedrooms']} bedrooms, and {property_data['bathrooms']} bathrooms. The {property_data['yearBuilt']} property with a lot size of {property_data['lotSize']} offers a unique opportunity.\n\nI am genuinely interested in making this property my home, and I would appreciate the opportunity to discuss a potential sale. Please feel free to contact me at {buyer_contact} to arrange a convenient time for us to connect.\n\n{personalized_message}\n\nThank you for considering my inquiry. I look forward to the possibility of becoming the new owner of your property.\n\nSincerely,\n{buyer_name}"

# Main Streamlit app
def main():
    st.title("Realtor Property Information App")
    st.sidebar.header("User Input:")
    
    api_key = st.sidebar.text_input("Enter your API key", help="Get it from Realty Mole API")
    address = st.sidebar.text_input("Enter the address", help="E.g., 5500 Grand Lake Dr, San Antonio, TX, 78244")

    if st.sidebar.button("Get Property Info"):
        if api_key and address:
            with st.spinner("Fetching property information..."):
                properties = handle_api_response(api_key, address)
            
            if properties:
                display_property_info(properties[0])

                # Custom Information Inputs
                buyer_name = st.text_input("Your Name", help="Enter your full name")
                buyer_contact = st.text_input("Your Contact Information", help="Enter your email or phone number")
                personalized_message = st.text_area("Personalized Message", help="Enter any additional message or specific details you'd like to convey (optional)")

                # Generate Letter
                if st.button("Generate Letter"):
                    if buyer_name and buyer_contact:
                        letter = generate_letter(properties[0], buyer_name, buyer_contact, personalized_message)
                        st.write(f"### Generated Letter:")
                        st.write(letter)
                    else:
                        st.warning("Please provide your name and contact information.")

if __name__ == "__main__":
    main()
