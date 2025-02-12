# Utiliser une image Python légère
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app


# Copier le fichier de configuration Poetry et installer les dépendances
COPY pyproject.toml poetry.lock ./

# Installer les dépendances avec Poetry
# RUN poetry install --no-interaction --no-root
# Copier le reste du code de l’application
COPY ui ui
RUN chmod -R 755 /app/ui

# Installer Poetry et ses dépendances
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir poetry
RUN poetry install --no-interaction

# Exposer un port si c'est une API REST
EXPOSE 8501

# Lancer application Python avec poetry
CMD ["poetry", "run", "streamlit", "run", "ui/webapp.py", "--server.port", "8501", "--server.address", "0.0.0.0", "--server.enableCORS", "false", "--server.enableXsrfProtection", "false"]

