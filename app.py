import streamlit as st

def display_property_info(property_info):
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

    st.write(f"**Property ID:** {property_info.get('id', 'N/A')}")
    st.write(f"**Longitude:** {property_info.get('longitude', 'N/A')}")
    st.write(f"**Latitude:** {property_info.get('latitude', 'N/A')}")

def main():
    st.title("Realtor Property Information App")

    # Sample data (replace this with actual API response)
    sample_data = [
        {
            "addressLine1": "5500 Grand Lake Dr",
            "city": "San Antonio",
            "state": "TX",
            "zipCode": "78244",
            "formattedAddress": "5500 Grand Lake Dr, San Antonio, TX 78244",
            "assessorID": "05076-103-0500",
            "bedrooms": 3,
            "county": "Bexar",
            "legalDescription": "B 5076A BLK 3 LOT 50",
            "squareFootage": 1878,
            "subdivision": "CONV A/S CODE",
            "yearBuilt": 1973,
            "bathrooms": 2,
            "lotSize": 8843,
            "propertyType": "Single Family",
            "lastSaleDate": "2017-10-19T00:00:00.000Z",
            "features": {
                "architectureType": "Contemporary",
                "cooling": True,
                "coolingType": "Central",
                "exteriorType": "Wood",
                "floorCount": 1,
                "foundationType": "Slab",
                "garage": True,
                "garageType": "Garage",
                "heating": True,
                "heatingType": "Forced Air",
                "pool": True,
                "roofType": "Asphalt",
                "roomCount": 5,
                "unitCount": 1
            },
            "taxAssessment": {
                "2018": {
                    "value": 126510,
                    "land": 18760,
                    "improvements": 107750
                },
                "2019": {
                    "value": 135430,
                    "land": 23450,
                    "improvements": 111980
                },
                "2020": {
                    "value": 142610,
                    "land": 23450,
                    "improvements": 119160
                },
                "2021": {
                    "value": 163440,
                    "land": 45050,
                    "improvements": 118390
                },
                "2022": {
                    "value": 197600,
                    "land": 49560,
                    "improvements": 148040
                }
            },
            "propertyTaxes": {
                "2019": {
                    "total": 2997
                },
                "2021": {
                    "total": 3468
                }
            },
            "owner": {
                "names": [
                    "MICHEAL ONEAL SMITH"
                ],
                "mailingAddress": {
                    "id": "149-Weaver-Blvd,-Weaverville,-NC-28787",
                    "addressLine1": "149 Weaver Blvd",
                    "city": "Weaverville",
                    "state": "NC",
                    "zipCode": "28787"
                }
            },
            "id": "5500-Grand-Lake-Dr,-San-Antonio,-TX-78244",
            "longitude": -98.351442,
            "latitude": 29.475962
        }
    ]

    if st.button("Load Sample Data"):
        if sample_data:
            for property_info in sample_data:
                display_property_info(property_info)

if __name__ == "__main__":
    main()
