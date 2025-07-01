from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json
from typing import Dict, Any
import xml.etree.ElementTree as ET
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document
import uvicorn

app = FastAPI()

class MCPRequest(BaseModel):
    tool: str
    parameters: Dict[str, Any]
    prompt: str

class MCPResponse(BaseModel):
    result: Dict[str, Any]
    status: str

def uniprot_search(uniprot_id: str) -> Dict[str, Any]:
    try:
        response = requests.get(f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.json")
        if response.status_code != 200:
            return {"result": {}, "status": f"UniProt API error: {response.status_code}"}
        
        data = response.json()
        # Filter the response to include only key fields
        filtered_data = {
            "primaryAccession": data.get("primaryAccession"),
            "uniProtkbId": data.get("uniProtkbId"),
            "proteinName": data.get("proteinDescription", {})
                           .get("recommendedName", {})
                           .get("fullName", {})
                           .get("value", "N/A"),
            "organism": data.get("organism", {}).get("scientificName", "N/A"),
            "function": next(
                (
                    comment["texts"][0]["value"]
                    for comment in data.get("comments", [])
                    if comment["commentType"] == "FUNCTION"
                ),
                "No function description available",
            ),
            "sequence": data.get("sequence", {}).get("value", "N/A"),
            "length": data.get("sequence", {}).get("length", 0),
        }
        return {"result": filtered_data, "status": "success"}
    
    except Exception as e:
        return {"result": {}, "status": f"Error: {str(e)}"}

@app.post("/mcp", response_model=MCPResponse)
async def mcp_endpoint(request: MCPRequest):
    try:

        if request.tool == "uniprot_search":
                    result = uniprot_search(request.parameters.get("uniprot_id"))
                    return MCPResponse(**result)

        return MCPResponse(result={}, status=f"Unknown tool: {request.tool}")

    except Exception as e:
        return MCPResponse(result={}, status=f"Error: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)