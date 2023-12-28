## API

APi écrite avec FastAPI.

### Schémas

`videos.db`: Base contenant les métadonnées des vidéos
- Table `videos`
  - `length`: Durée de la vidéo en secondes
  - `position`: [`lat`, `long`]: Coordonnés GPS de la vidéo, en latitude et longitude

