import torch
from torchvision import models
from torch import nn
from src.preprocess import preprocess_image
from pathlib import Path

device = torch.device("cpu")

# Solar panel fault types - Update number of classes if you add more
CLASS_NAMES = {
    0: "Healthy Panel",
    1: "Microcracks",
    2: "Hot Spots",
    3: "Snail Trails",
    4: "Cell Breakage",
    5: "Delamination",
    6: "Bypass Diode Failure",
    7: "PID (Potential Induced Degradation)"
}

def load_model():
    model = models.resnet18(pretrained=False)
    model.fc = nn.Linear(model.fc.in_features, len(CLASS_NAMES))

    model_path = Path("model/solar_model.pth")
    
    # Check if model file exists and is valid
    if not model_path.exists():
        raise FileNotFoundError(
            f"Model file not found at {model_path}\n"
            f"Run 'python create_model.py' to generate a model file."
        )
    
    # Check file size (should be at least 40MB for ResNet18)
    file_size_mb = model_path.stat().st_size / (1024 * 1024)
    if file_size_mb < 1:
        raise ValueError(
            f"Model file is too small ({file_size_mb:.2f} MB). "
            f"File may be corrupted or empty.\n"
            f"Run 'python create_model.py' to generate a valid model file."
        )
    
    try:
        model.load_state_dict(torch.load(model_path, map_location=device))
    except (EOFError, RuntimeError) as e:
        raise ValueError(
            f"Failed to load model: {e}\n"
            f"The model file may be corrupted or invalid.\n"
            f"Run 'python create_model.py' to generate a new model file."
        ) from e
    
    model.eval()
    return model

def predict(image, model):
    """
    Predict fault type from solar panel image.
    
    Args:
        image: PIL Image of solar panel
        model: Loaded PyTorch model
        
    Returns:
        Dictionary with prediction results including:
        - fault_type: Name of detected fault
        - confidence: Prediction confidence score
        - probabilities: All class probabilities
    """
    image_tensor = preprocess_image(image)

    with torch.no_grad():
        output = model(image_tensor)
        probabilities = torch.softmax(output, dim=1)[0].cpu()  # Get probabilities and move to CPU
        pred_class = torch.argmax(output, dim=1).item()
        confidence = float(probabilities[pred_class])
    
    # Get all probabilities as dictionary
    prob_dict = {
        CLASS_NAMES[i]: float(probabilities[i])
        for i in range(len(CLASS_NAMES))
    }
    
    return {
        "fault_type": CLASS_NAMES[pred_class],
        "confidence": confidence,
        "probabilities": prob_dict
    }
