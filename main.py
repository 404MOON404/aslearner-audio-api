import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

# Cargar variables del archivo .env
load_dotenv()

# Obtener la clave de forma segura
API_KEY_ELEVEN = os.getenv("ELEVENLABS_API_KEY")
VOZ_ID_GRATIS = "JBFqnCBsd6RMkjVDRZzb" 

app = FastAPI(title="ASLearner Audio API")
client = ElevenLabs(api_key=API_KEY_ELEVEN)

class AudioRequest(BaseModel):
    texto: str

@app.get("/")
def home():
    return {"mensaje": "API lista para producción."}

@app.post("/generar-audio")
async def generar_audio(request: AudioRequest):
    try:
        audio_generator = client.text_to_speech.convert(
            text=request.texto,
            voice_id=VOZ_ID_GRATIS,
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128"
        )
        
        nombre_archivo = "asl_audio.mp3"
        with open(nombre_archivo, "wb") as f:
            for chunk in audio_generator:
                if chunk:
                    f.write(chunk)
                
        return FileResponse(
            path=nombre_archivo, 
            media_type="audio/mpeg",
            filename="leccion_asl.mp3"
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")