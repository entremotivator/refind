import streamlit as st

def display_property_info(property_info):
    st.write("### Property Information:")
    st.write(f"**Address Line 1:** {property_info.get('addressLine1', 'N/A')}")
    st.write(f"**City:** {property_info.get('city', 'N/A')}")
    # Add more fields similarly

def main():
    st.title("Realtor Property Information App")

    # Sample data (replace this with actual API response)
    sample_data = [
        {
            "addressLine1": "5500 Grand Lake Dr",
            "city": "San Antonio",
            "state": "TX",
            "zipCode": "78244",
            # Add more fields similarly
        }
    ]

    if st.button("Load Sample Data"):
        if sample_data:
            for property_info in sample_data:
                display_property_info(property_info)

if __name__ == "__main__":
    main()
