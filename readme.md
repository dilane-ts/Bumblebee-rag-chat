# Bumblebee : Un Système de Modèle de Langage Augmenté par recuperation

Bumblebee est un système de modèle de langage augmenté par recuperation conçu pour répondre à des questions en combinant la recherche de documents basée sur des vecteurs et un modèle de langage. Il prend en charge les réponses en streaming et maintient le contexte conversationnel grâce à l'historique des interactions.

## Fonctionnalités

- **Recherche de Documents** : Utilise FAISS pour une recherche efficace basée sur des vecteurs.
- **Intégration de Modèles de Langage** : Prend en charge les modèles Hugging Face et ChatOllama pour générer des réponses.
- **Réponses en Streaming** : Fournit des réponses en temps réel.
- **Conversations Contextuelles** : Maintient l'historique des interactions pour un contexte conversationnel fluide.
- **Personnalisable** : Facilement configurable pour différents modèles et paramètres de recherche.

---

## Installation

### 1. Cloner le Dépôt
```bash
git clone https://github.com/votre-utilisateur/bumblebee.git
cd bumblebee
```

### 2. Configurer un Environnement Virtuel
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les Dépendances
```bash
pip install -r requirements.txt
```

### 4. Installer Tesseract OCR (si nécessaire pour le traitement des PDF)
```bash
sudo apt-get install tesseract-ocr
```

---

## Utilisation

### 1. Préparer Vos Documents
Placez vos fichiers PDF dans un dossier nommé `documents` à la racine du projet.

### 2. Créer le Store de Vecteurs
Exécutez le script suivant pour traiter les documents et créer un index FAISS :
```bash
python create_vectorstore.py
```

### 3. Lancer le Système Bumblebee
Exécutez le script principal pour interagir avec le système :
```bash
python bumblebee.py
```

### 4. Exemple de Requête
Le système traitera votre requête et renverra une réponse :
```plaintext
Entrée : "Qu'est-ce qu'un compilateur ?"
Sortie : "Un compilateur est un programme qui traduit le code source en code machine..."
```

---

## Structure du Projet

```
bumblebee/
├── create_vectorstore.py   # Script pour créer le store de vecteurs FAISS
├── bumblebee.py            # Script principal du système Bumblebee
├── requirements.txt        # Dépendances Python
├── documents/              # Dossier pour stocker les documents PDF
├── venv/                   # Environnement virtuel (optionnel)
└── readme.md               # Documentation du projet
```

---

## Composants Clés

### 1. `create_vectorstore.py`
- Charge les documents PDF à l'aide de `PyPDFDirectoryLoader`.
- Divise les documents en morceaux avec `RecursiveCharacterTextSplitter`.
- Génère des embeddings avec `HuggingFaceEmbeddings`.
- Sauvegarde l'index FAISS localement.

### 2. `bumblebee.py`
- Charge le store de vecteurs FAISS.
- Intègre un modèle de langage (par exemple, ChatOllama ou modèles Hugging Face).
- Fournit des réponses en streaming et maintient le contexte conversationnel.

---

## Dépendances

- Python 3.8+
- [LangChain](https://github.com/hwchase17/langchain)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Hugging Face Hub](https://huggingface.co/)
- Tesseract OCR (optionnel, pour l'extraction d'images des PDF)

Installez toutes les dépendances avec :
```bash
pip install -r requirements.txt
```

---

## Exemple de Flux de Travail

1. **Préparer les Documents** : Ajoutez vos fichiers PDF dans le dossier `documents/`.
2. **Créer le Store de Vecteurs** : Exécutez `create_vectorstore.py` pour traiter les documents.
3. **Poser des Questions** : Utilisez `bumblebee.py` pour interroger le système.


---

## Améliorations Futures

- Ajouter la prise en charge de formats de documents supplémentaires (par exemple, Word, HTML).
- Améliorer la gestion des erreurs et la journalisation.
- Intégrer des modèles de langage plus avancés.
- Ajouter une interface web pour une interaction plus facile.

---

## Licence

Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus de détails.

---

## Remerciements

- [LangChain](https://github.com/hwchase17/langchain) pour le framework.
- [Hugging Face](https://huggingface.co/) pour les modèles de langage.
- [FAISS](https://github.com/facebookresearch/faiss) pour la recherche vectorielle efficace.

---

## Contact

Pour toute question ou suggestion, veuillez contacter [lefakongdilane@gmail.com].