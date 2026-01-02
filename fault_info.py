"""
Fault information and repair instructions for solar panel faults.
"""

FAULT_DATABASE = {
    "Healthy Panel": {
        "description": "No faults detected. Panel is operating normally.",
        "severity": "None",
        "repair_steps": [
            "No action required. Continue regular maintenance.",
            "Monitor panel performance monthly.",
            "Keep panel surface clean."
        ],
        "prevention": [
            "Regular cleaning and inspection",
            "Proper installation and mounting",
            "Avoid physical damage"
        ]
    },
    "Microcracks": {
        "description": "Small cracks in solar cells that can reduce efficiency and lead to cell failure over time.",
        "severity": "Medium",
        "symptoms": [
            "Reduced power output",
            "Visible hairline cracks in cells",
            "Hot spots may develop"
        ],
        "repair_steps": [
            "Inspect all cells for crack patterns",
            "Replace individual cracked cells if possible",
            "If multiple cells affected, consider panel replacement",
            "Apply protective coating to prevent further cracking",
            "Ensure proper mounting to reduce mechanical stress"
        ],
        "prevention": [
            "Handle panels carefully during installation",
            "Use proper mounting hardware",
            "Avoid thermal stress from rapid temperature changes",
            "Regular EL testing to catch early cracks"
        ],
        "cost_estimate": "Low to Medium (cell replacement) or High (panel replacement)"
    },
    "Hot Spots": {
        "description": "Localized overheating in cells, often caused by shading, cell defects, or bypass diode failure.",
        "severity": "High",
        "symptoms": [
            "Localized heating visible in thermal imaging",
            "Reduced panel efficiency",
            "Potential fire hazard if severe"
        ],
        "repair_steps": [
            "Immediately reduce panel load or disconnect if severe",
            "Identify and remove shading sources",
            "Check and replace faulty bypass diodes",
            "Replace affected cells if damaged",
            "Clean panel surface to remove debris causing shading",
            "Verify proper wiring and connections"
        ],
        "prevention": [
            "Regular cleaning to prevent shading",
            "Proper system design with bypass diodes",
            "Avoid partial shading situations",
            "Regular thermal inspections"
        ],
        "cost_estimate": "Medium (diode/cell replacement)"
    },
    "Snail Trails": {
        "description": "Dark lines or trails on cells caused by moisture ingress and silver paste degradation.",
        "severity": "Low to Medium",
        "symptoms": [
            "Dark lines or trails on cell surface",
            "Gradual efficiency loss",
            "Visible discoloration"
        ],
        "repair_steps": [
            "Clean panel surface thoroughly",
            "Apply protective sealant to prevent moisture ingress",
            "Replace affected cells if degradation is severe",
            "Improve panel encapsulation",
            "Ensure proper panel sealing"
        ],
        "prevention": [
            "Use high-quality panel encapsulation",
            "Ensure proper installation sealing",
            "Regular maintenance and cleaning",
            "Protect from excessive moisture"
        ],
        "cost_estimate": "Low to Medium"
    },
    "Cell Breakage": {
        "description": "Complete breakage or shattering of solar cells, often due to mechanical damage or extreme stress.",
        "severity": "High",
        "symptoms": [
            "Visible broken or shattered cells",
            "Significant power loss",
            "Potential safety hazard"
        ],
        "repair_steps": [
            "Disconnect panel from system immediately",
            "Replace broken cells or entire panel",
            "Inspect mounting system for issues",
            "Check for impact damage sources",
            "Verify proper installation and support"
        ],
        "prevention": [
            "Careful handling during transport and installation",
            "Proper mounting and support structure",
            "Protection from hail and debris",
            "Regular structural inspections"
        ],
        "cost_estimate": "High (panel replacement usually required)"
    },
    "Delamination": {
        "description": "Separation of layers in the panel, allowing moisture ingress and reducing efficiency.",
        "severity": "Medium to High",
        "symptoms": [
            "Visible separation of panel layers",
            "Moisture ingress",
            "Reduced efficiency",
            "Potential for further damage"
        ],
        "repair_steps": [
            "Assess extent of delamination",
            "Apply specialized adhesive/sealant if minor",
            "Replace panel if delamination is extensive",
            "Improve panel encapsulation",
            "Ensure proper environmental protection"
        ],
        "prevention": [
            "Use high-quality panel materials",
            "Proper installation and sealing",
            "Protect from extreme weather",
            "Regular inspection for early signs"
        ],
        "cost_estimate": "Medium to High"
    },
    "Bypass Diode Failure": {
        "description": "Failure of bypass diodes that protect cells from reverse current, causing hot spots and reduced output.",
        "severity": "Medium",
        "symptoms": [
            "Hot spots in panel",
            "Reduced power output",
            "Visible diode junction box issues"
        ],
        "repair_steps": [
            "Disconnect panel from system",
            "Open junction box carefully",
            "Test diodes with multimeter",
            "Replace faulty diodes",
            "Re-seal junction box properly",
            "Test panel output after repair"
        ],
        "prevention": [
            "Use quality diodes in system design",
            "Proper junction box sealing",
            "Regular electrical testing",
            "Protect from moisture and overheating"
        ],
        "cost_estimate": "Low to Medium"
    },
    "PID (Potential Induced Degradation)": {
        "description": "Performance degradation caused by voltage potential between cells and ground, common in high-voltage systems.",
        "severity": "Medium to High",
        "symptoms": [
            "Gradual efficiency loss",
            "Not visible in EL images but affects performance",
            "More common in high-voltage arrays"
        ],
        "repair_steps": [
            "Install PID recovery boxes if applicable",
            "Ground array properly",
            "Use PID-resistant panels",
            "Consider panel replacement if severe",
            "Optimize system voltage"
        ],
        "prevention": [
            "Use PID-resistant panel technology",
            "Proper system grounding",
            "Optimize system design",
            "Regular performance monitoring"
        ],
        "cost_estimate": "Medium to High"
    }
}


def get_fault_info(fault_name: str) -> dict:
    """
    Get detailed information about a specific fault type.
    
    Args:
        fault_name: Name of the fault type
        
    Returns:
        Dictionary with fault information, or default if not found
    """
    return FAULT_DATABASE.get(fault_name, {
        "description": "Unknown fault type.",
        "severity": "Unknown",
        "repair_steps": ["Consult a professional solar technician."],
        "prevention": ["Regular maintenance and inspection."]
    })


def get_all_fault_types() -> list:
    """Get list of all available fault types."""
    return list(FAULT_DATABASE.keys())

