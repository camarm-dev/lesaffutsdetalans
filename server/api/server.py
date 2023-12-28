import uvicorn
from fastapi import FastAPI
import dotenv

dotenv.load_dotenv()
config = dotenv.dotenv_values()
DEST = config['DESTINATION_FOLDER']
app = FastAPI(title="Les affuts d'Étalans API", description="Gestion et récupération des vidéos (et de leurs métadonnées) prisent par 'Les Affuts d'Étalans'")


@app.get('/')
def root():
    return {
        "message": "Welcome on API, visit /docs for swagger !"
    }


@app.get('/videos')
def get_videos_data():
    return {
        "data": [
            {
                ""
            }
        ]
    }


@app.get('/video/:name')
def stream_video():
    return


if __name__ == '__main__':
    uvicorn.run(app)
