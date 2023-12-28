# Les affuts d'Étalans
Un software open source d'affut vidéo pour Raspberry Pi, mais aussi un site web pour retrouver les captures et un guide pour construire son propre affut vidéo !

## Buts
- [ ] Enregistrer des vidéos
- [ ] Avoir une API fonctionnelle
  - [ ] Authentification
  - [ ] Upload de vidéo
  - [ ] Récupération de vidéos, ordonnées, triées
- [ ] Avoir un site fonctionnel
  - [ ] Sur [lesaffutsdetalans.fr](https://lesaffutsdetalans.fr) 
- [ ] Pouvoir uploader ses vidéos sur le site avec `upload.py`

## Pré-Requis
- Raspberry Pi 3B
  - Caméra nocturne
  - Détecteur de mouvements sur le GPIO27 (modèle `HC SR501`: [SENSOR.md]())
  - Led sur le GPIO18 ([SENSOR.md]())
- Batterie ?
- Boîtier ?

## Software

Le programme `sensor.py` déclenche la caméra quand un mouvement est détecté, et sauvegarde l'enregistrement.
- La LED allumée indique que le capteur a été initialisé et est fonctionnel
- La LED clignotante indique qu'un enregistrement est en cour

Avec une connexion internet, le programme `upload.py` téléversera toutes les vidéos sur [lesaffutsdetalans.fr](https://lesaffutsdetalans.fr) (partie administration, les vidéos doivent être traitées avant d'être publiées publiquement) puis les supprimera de cet appareil.

En ligne, on peut voir :
- La vidéo
- L'heure de la prise
- Des estimations de l'espèce capturée
- L'appareil de capture et sa version

## Structure

- `records`: Dossier contenant les enregistrements
  - `affut-01_YYYY-MM-DD_hh.mm.ss.mp4`: Enregistrement vidéo 
  - `affut-01_YYYY-MM-DD_hh.mm.ss.report`: JSON contentant les métadonnées 

## Configurer

`config.json` (exemple à `config.sample.json`)
```json
{
  "version": "0.0.0",
  "key": "affut-XXXXXXXXXXXXX",
  "node": "affut-01",
  "position": [47.13768, 6.25941]
}
```

- `version`: Ne pas modifier
- `key`: La clé d'API pour envoyer les vidéos avec `upload.py` (optionnel)
- `node`: Le nom de ce noeud (préférable de suivre le schéma `affutJeanDupont-01`, `affutJeanDupont-02` ou `affut-01`, `affut-02`)
- `position`: La position de l'affut, latitude, longitude
