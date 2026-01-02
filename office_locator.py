"""
Service office locator based on pincode/zip code.
"""

# Database of service offices with pincode coverage
SERVICE_OFFICES = {
    "110001": {
        "office_name": "Delhi Central Service Center",
        "address": "123 Connaught Place, New Delhi",
        "pincode": "110001",
        "phone": "+91-11-2345-6789",
        "email": "delhi.central@solarrepair.in",
        "coverage_radius_km": 25,
        "working_hours": "Mon-Sat: 9:00 AM - 6:00 PM"
    },
    "400001": {
        "office_name": "Mumbai Main Service Center",
        "address": "456 Marine Drive, Mumbai",
        "pincode": "400001",
        "phone": "+91-22-3456-7890",
        "email": "mumbai.main@solarrepair.in",
        "coverage_radius_km": 30,
        "working_hours": "Mon-Sat: 9:00 AM - 6:00 PM"
    },
    "560001": {
        "office_name": "Bangalore Tech Park Service Center",
        "address": "789 MG Road, Bangalore",
        "pincode": "560001",
        "phone": "+91-80-4567-8901",
        "email": "bangalore.tech@solarrepair.in",
        "coverage_radius_km": 35,
        "working_hours": "Mon-Sat: 9:00 AM - 6:00 PM"
    },
    "700001": {
        "office_name": "Kolkata Eastern Service Center",
        "address": "321 Park Street, Kolkata",
        "pincode": "700001",
        "phone": "+91-33-5678-9012",
        "email": "kolkata.east@solarrepair.in",
        "coverage_radius_km": 28,
        "working_hours": "Mon-Sat: 9:00 AM - 6:00 PM"
    },
    "600001": {
        "office_name": "Chennai Southern Service Center",
        "address": "654 Mount Road, Chennai",
        "pincode": "600001",
        "phone": "+91-44-6789-0123",
        "email": "chennai.south@solarrepair.in",
        "coverage_radius_km": 30,
        "working_hours": "Mon-Sat: 9:00 AM - 6:00 PM"
    },
    "380001": {
        "office_name": "Ahmedabad Western Service Center",
        "address": "987 CG Road, Ahmedabad",
        "pincode": "380001",
        "phone": "+91-79-7890-1234",
        "email": "ahmedabad.west@solarrepair.in",
        "coverage_radius_km": 25,
        "working_hours": "Mon-Sat: 9:00 AM - 6:00 PM"
    },
    "500001": {
        "office_name": "Hyderabad Deccan Service Center",
        "address": "147 Hitech City, Hyderabad",
        "pincode": "500001",
        "phone": "+91-40-8901-2345",
        "email": "hyderabad.deccan@solarrepair.in",
        "coverage_radius_km": 32,
        "working_hours": "Mon-Sat: 9:00 AM - 6:00 PM"
    },
    "110092": {
        "office_name": "Delhi NCR Service Center",
        "address": "258 Sector 18, Noida",
        "pincode": "110092",
        "phone": "+91-11-9012-3456",
        "email": "delhi.ncr@solarrepair.in",
        "coverage_radius_km": 40,
        "working_hours": "Mon-Sat: 9:00 AM - 6:00 PM"
    }
}

# Pincode to office mapping (for quick lookup)
PINCODE_TO_OFFICE = {
    # Delhi and NCR
    "110001": "110001", "110002": "110001", "110003": "110001",
    "110092": "110092", "110093": "110092", "110094": "110092",
    
    # Mumbai
    "400001": "400001", "400002": "400001", "400003": "400001",
    "400004": "400001", "400005": "400001",
    
    # Bangalore
    "560001": "560001", "560002": "560001", "560003": "560001",
    "560004": "560001", "560005": "560001",
    
    # Kolkata
    "700001": "700001", "700002": "700001", "700003": "700001",
    "700004": "700001", "700005": "700001",
    
    # Chennai
    "600001": "600001", "600002": "600001", "600003": "600001",
    "600004": "600001", "600005": "600001",
    
    # Ahmedabad
    "380001": "380001", "380002": "380001", "380003": "380001",
    "380004": "380001", "380005": "380001",
    
    # Hyderabad
    "500001": "500001", "500002": "500001", "500003": "500001",
    "500004": "500001", "500005": "500001",
}


def find_nearest_office(pincode: str) -> dict:
    """
    Find the nearest service office for a given pincode.
    
    Args:
        pincode: User's pincode/zip code
        
    Returns:
        Dictionary with office information, or None if not found
    """
    # Clean pincode (remove spaces, convert to string)
    pincode = str(pincode).strip().replace(" ", "")
    
    # Direct lookup
    if pincode in PINCODE_TO_OFFICE:
        office_pincode = PINCODE_TO_OFFICE[pincode]
        return SERVICE_OFFICES.get(office_pincode)
    
    # If exact match not found, try to find closest match
    # Check if pincode starts with any known office pincode prefix
    for office_pincode, office_data in SERVICE_OFFICES.items():
        if pincode.startswith(office_pincode[:3]):  # Match first 3 digits
            return office_data
    
    # Default to first available office if no match
    if SERVICE_OFFICES:
        return list(SERVICE_OFFICES.values())[0]
    
    return None


def get_all_offices() -> list:
    """Get list of all service offices."""
    return list(SERVICE_OFFICES.values())


def format_contact_info(office: dict) -> str:
    """Format office contact information as a string."""
    if not office:
        return "No office found."
    
    return f"""
**{office['office_name']}**
📍 {office['address']}
📮 Pincode: {office['pincode']}
📞 Phone: {office['phone']}
✉️ Email: {office['email']}
🕐 {office['working_hours']}
"""

