# Utiliser une image Python légère
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app


# Copier le fichier de configuration Poetry et installer les dépendances
COPY pyproject.toml poetry.lock ./

# Copier le reste du code de l’application
COPY src src
RUN chmod -R 755 /app/src

# Installer Poetry et ses dépendances
RUN pip install --no-cache-dir --upgrade pip \
     && pip install --no-cache-dir poetry
 RUN poetry install --no-interaction

# RUN pip install --upgrade pip \
#     && pip install poetry
# RUN poetry install --no-interaction

# Exposer un port si c'est une API REST
EXPOSE 8000

# Lancer application Python avec poetry
CMD ["poetry", "run", "python", "src/summarizer/app.py"]
