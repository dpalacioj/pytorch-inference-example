import torch
import pytest

@pytest.fixture(scope='module')
def model():
    """
    Fixture to load the model once for all tests.

    Returns:
        torch.jit.ScriptModule: Loaded PyTorch JIT model.
    """
    return torch.jit.load('./doubleit_model.pt')

def test_inference(model):
    """
    Test the inference on a sample tensor.

    Args:
        model (torch.jit.ScriptModule): The loaded model from the fixture.

    Asserts:
        The result of the model's inference matches the expected tensor.
    """
    # Create a sample tensor
    sample_tensor = torch.tensor([1, 2, 3, 4], dtype=torch.float32)

    # Make inference
    result = model(sample_tensor)

    # Expected result
    expected = torch.tensor([2, 4, 6, 8], dtype=torch.float32)

    # Verification
    assert torch.equal(result, expected), f"Expected {expected}, but got {result}"

def test_inference_empty_tensor(model):
    """
    Test the inference on an empty tensor.

    Args:
        model (torch.jit.ScriptModule): The loaded model from the fixture.

    Asserts:
        The result of the model's inference on an empty tensor matches the expected empty tensor.
    """
    # Create an empty tensor
    sample_tensor = torch.tensor([], dtype=torch.float32)

    # Make the inference
    result = model(sample_tensor)

    # Expected result
    expected = torch.tensor([], dtype=torch.float32)

    # Verification
    assert torch.equal(result, expected), f"Expected {expected}, but got {result}"

def test_inference_negative_tensor(model):
    """
    Test the inference on a tensor with negative values.

    Args:
        model (torch.jit.ScriptModule): The loaded model from the fixture.

    Asserts:
        The result of the model's inference matches the expected tensor with doubled negative values.
    """
    # Create a tensor with negative values
    sample_tensor = torch.tensor([-1, -2, -3, -4], dtype=torch.float32)

    # Make inference
    result = model(sample_tensor)

    # Expected result
    expected = torch.tensor([-2, -4, -6, -8], dtype=torch.float32)

    # Verification
    assert torch.equal(result, expected), f"Expected {expected}, but got {result}"