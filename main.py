
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import torch
from typing import List, Dict

class InputData(BaseModel):
    values: list[float]

app = FastAPI()

# Load the model
ts = torch.jit.load('./doubleit_model.pt')

@app.get('/')
def index():
    return {'message': 'This model returns a 1-dim tensor multiplied by 2'}

@app.post("/infer", response_model=Dict[str, List[float]])
async def infer(data: InputData) -> Dict[str, List[float]]:
    """
    Endpoint to perform inference using the pre-trained model.

    Args:
        data (InputData): Input data containing a list of integers.

    Returns:
        dict: A dictionary containing the result of the inference.
    """
    try:
        # Create a tensor from the input data
        sample_tensor = torch.tensor(data.values)
        
        # Perform inference
        result = ts(sample_tensor)
        
        # Convert the result to a list and return it
        return {"result": result.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))