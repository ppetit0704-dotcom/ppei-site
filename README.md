# Site PPEI — guide de déploiement

Site statique (HTML/CSS pur, aucune dépendance, aucun build à faire) pour
présenter l'ensemble de la suite PPEI et proposer le téléchargement de
chaque application.

## Structure

```
ppei-site/
├── index.html              # page d'accueil (registre des applications)
├── artificialisation.html
├── budget-finances.html
├── emploi.html
├── rpls.html
├── bpe.html
├── observatoire.html
├── sirene.html
├── secours.html
├── styles.css               # feuille de style unique, partagée par toutes les pages
├── build_pages.py           # script qui a généré les 8 pages d'application
│                             # (à relancer si vous voulez modifier le contenu
│                             # d'une page : éditez le dictionnaire PAGES puis
│                             # `python3 build_pages.py`)
└── assets/
    └── screenshots/          # dossier vide, prévu pour vos captures d'écran
```

## Mise en ligne gratuite avec GitHub Pages

1. **Créer le dépôt.** Sur github.com, créez un nouveau dépôt (public),
   par exemple nommé `ppei-site`.

2. **Déposer les fichiers.** Depuis votre ordinateur, dans le dossier
   `ppei-site` :
   ```
   git init
   git add .
   git commit -m "Premier dépôt du site PPEI"
   git branch -M main
   git remote add origin https://github.com/VOTRE-COMPTE/ppei-site.git
   git push -u origin main
   ```
   (Si vous préférez, vous pouvez aussi glisser-déposer les fichiers
   directement depuis l'interface web de GitHub, sans utiliser de ligne de
   commande — bouton "Add file" → "Upload files".)

3. **Activer GitHub Pages.** Dans le dépôt : Settings → Pages → sous
   "Build and deployment", choisissez Source = "Deploy from a branch",
   Branch = `main`, dossier `/ (root)`. Enregistrez.

4. **Votre site est en ligne** à l'adresse
   `https://VOTRE-COMPTE.github.io/ppei-site/`
   (la mise en ligne prend une à deux minutes après chaque modification).

5. **Nom de domaine personnalisé (optionnel).** Si vous possédez un jour
   un nom de domaine (ex. `ppei.fr`), un fichier `CNAME` et un réglage DNS
   suffisent — dites-moi le moment venu, je vous guide.

## Héberger les fichiers à télécharger (.exe, .apk)

GitHub Pages sert très bien des pages HTML, mais n'est pas fait pour
distribuer de gros fichiers binaires. La bonne pratique gratuite est
d'utiliser les **Releases GitHub** du même dépôt (ou d'un dépôt dédié à
chaque application) :

1. Dans le dépôt, onglet "Releases" → "Create a new release".
2. Donnez un tag de version (ex. `v1.0.0`), un titre, et **glissez vos
   fichiers** (`.exe`, `.apk`) dans la zone "Attach binaries".
3. Publiez la release. GitHub vous donne alors un lien direct et stable
   vers chaque fichier, du type :
   `https://github.com/VOTRE-COMPTE/ppei-site/releases/download/v1.0.0/PPEI-Artificialisation.exe`
4. Collez ce lien dans le `href="#"` du bouton de téléchargement
   correspondant, dans le fichier HTML de la page concernée (ou dans
   `build_pages.py` puis relancez le script).

Limite : 2 Go par fichier, largement suffisant pour un exécutable ou un
APK. Aucune limite de bande passante pour un usage raisonnable.

## Ajouter vos captures d'écran

Chaque page d'application a une section "Captures d'écran" avec 3
emplacements réservés. Pour les remplir :

1. Déposez vos images dans `assets/screenshots/`, nommées par exemple
   `secours-1.png`, `secours-2.png`, `secours-3.png`.
2. Dans le fichier HTML de la page, remplacez chaque bloc :
   ```html
   <div class="screenshot-placeholder">Capture à ajouter (...)</div>
   ```
   par :
   ```html
   <img src="assets/screenshots/secours-1.png" alt="Description de la capture">
   ```

## Mettre à jour le contenu d'une page

Toutes les pages d'application partagent le même modèle, généré par
`build_pages.py`. Pour modifier un texte, une fonctionnalité listée, ou le
statut de disponibilité d'une application :

1. Ouvrez `build_pages.py`.
2. Repérez le dictionnaire correspondant à l'application dans la liste
   `PAGES` (identifié par son `slug`).
3. Modifiez les champs (`lede`, `features`, `availability`, `buttons`...).
4. Relancez `python3 build_pages.py` — cela régénère les 8 pages HTML.
5. Republiez (git commit + push).

Si vous préférez éditer directement le HTML final sans repasser par le
script, c'est possible aussi — mais vos changements seront alors écrasés
si vous relancez `build_pages.py` un jour.
