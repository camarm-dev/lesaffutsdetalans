# lesaffutsdetalans
Un software open source d'affut vidéo pour Raspberry Pi

## Pré-Requis
- Raspberry Pi 3B
- Caméra nocturne
- Détecteur de mouvements

## Software

Le programme `sensor.py` déclenche la caméra quand un mouvement est détecté, et sauvegarde l'enregistrement. 

Avec une connexion internet, le programme `upload.py` téléversera toutes les vidéos sur [lesaffutsdetalans.fr](https://lesaffutsdetalans.fr) (partie administration, les vidéos doivent être traitées avant d'être publiées) puis les supprimera de cet appareil.

En ligne, on peut voir :
- La vidéo
- L'heure de la prise
- Des estimations de l'espèce capturée
- L'appareil de capture et sa version

## Structure

- `records`: Dossier contenant les enregistrements
  - `affut-01_YY-MM-DD-hh-mm-ss.mp4`: Enregistrement vidéo 
  - `affut-01_YY-MM-DD-hh-mm-ss.report`: JSON contentant les métadonnées 

## Configurer

`config.json` (exemple à `config.sample.json`)
```json
{
  "version": "0.0.0",
  "key": "affut-XXXXXXXXXXXXX",
  "node": "affut-01"
}
```
