## Partie serveur

Ce dossier contient le code de l'`api` et du frontend (`web`).

## Configurer
- `web/.env`: Personnaliser l'URL de l'api
- `api/.env`: Personnaliser la destination des vidéos

## Docker

Vous pouvez installer et lancer votre propre instance de l'API et du site web avec docker.

```shell
docker compose up -d
```

L'api sur `localhost:8080` et le web sur `localhost:5173`
