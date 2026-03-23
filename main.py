import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
import edge_tts

app = FastAPI(title="ASLearner Audio API (Free Version)")

class AudioRequest(BaseModel):
    texto: str

@app.get("/")
def home():
    return {"mensaje": "API de Audio con Edge TTS activa en Render."}

@app.post("/generar-audio")
async def generar_audio(request: AudioRequest):
    try:
        
        voz = "es-MX-DaliaNeural" 
        
        nombre_archivo = "asl_audio.mp3"
        
        
        communicate = edge_tts.Communicate(request.texto, voz)
        await communicate.save(nombre_archivo)
                
        
        return FileResponse(
            path=nombre_archivo, 
            media_type="audio/mpeg",
            filename="leccion_asl.mp3"
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")