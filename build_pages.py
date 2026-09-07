# -*- coding: utf-8 -*-
"""
Génère les pages HTML des applications PPEI à partir d'un modèle commun.
Usage : python3 build_pages.py
Les fichiers sont écrits dans le dossier courant.
"""

TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — PPEI</title>
<meta name="description" content="{meta_desc}">
<link rel="stylesheet" href="styles.css">
</head>
<body>

<header class="site-header">
  <div class="wrap">
    <a href="index.html" class="wordmark">PPEI<span>.</span></a>
    <nav>
      <a href="index.html#registre">Les applications</a>
      <a href="index.html#a-propos">À propos</a>
    </nav>
  </div>
</header>

<section class="hero">
  <div class="wrap">
    <span class="eyebrow-tag{tag_class}">{code}</span>
    <h1>{title}</h1>
    <p class="lede">{lede}</p>
  </div>
</section>

<main class="wrap">

  <section class="content-section">
    <h2>Fonctionnalités</h2>
    <ul class="feature-list">
{features}
    </ul>
  </section>

  <section class="content-section">
    <h2>Disponibilité</h2>
    <table class="availability-table">
      <tr><th>Plateforme</th><th>Statut</th></tr>
{availability_rows}
    </table>
  </section>

  <section class="content-section">
    <h2>Captures d'écran</h2>
    <div class="screenshot-gallery">
      <div class="screenshot-placeholder">Capture à ajouter<br>(assets/screenshots/{slug}-1.png)</div>
      <div class="screenshot-placeholder">Capture à ajouter<br>(assets/screenshots/{slug}-2.png)</div>
      <div class="screenshot-placeholder">Capture à ajouter<br>(assets/screenshots/{slug}-3.png)</div>
    </div>
    <p class="note-todo">Remplacez chaque bloc pointillé par une balise &lt;img&gt; une fois vos captures d'écran ajoutées dans assets/screenshots/ — voir README.md.</p>
  </section>

  <section class="content-section">
    <h2>Télécharger</h2>
    <div class="download-block">
      <p>{download_intro}</p>
      <div class="btn-row">
{download_buttons}
      </div>
      <p class="note-todo">Liens à activer une fois les fichiers déposés dans une Release GitHub — voir README.md.</p>
    </div>
  </section>

  <a class="back-link" href="index.html">← Retour au registre des applications</a>
</main>

<footer class="site-footer">
  <div class="wrap">
    <p>PPEI — Philippe PETIT · <a href="mailto:pp.0704@orange.fr">pp.0704@orange.fr</a></p>
  </div>
</footer>

</body>
</html>
"""

def feature_items(items):
    return "\n".join(f"      <li>{item}</li>" for item in items)

def availability_rows(rows):
    return "\n".join(f"      <tr><td>{platform}</td><td>{status}</td></tr>" for platform, status in rows)

def download_buttons(buttons):
    out = []
    for label, extra_class in buttons:
        cls = "btn btn-primary" if extra_class == "primary" else "btn btn-secondary"
        out.append(f'        <a class="{cls}" href="#" aria-disabled="true">{label}</a>')
    return "\n".join(out)

PAGES = [
    dict(
        slug="artificialisation",
        code="ZAN · CEREMA",
        tag_class="",
        title="PPEI-Artificialisation",
        meta_desc="Suivi de la consommation d'espaces et de la trajectoire ZAN à partir des données CEREMA.",
        lede=(
            "Suivez la consommation d'espaces naturels, agricoles et "
            "forestiers (NAF) de votre commune ou de votre EPCI, et "
            "positionnez votre trajectoire par rapport aux objectifs "
            "de Zéro Artificialisation Nette (ZAN), à partir des "
            "millésimes publiés par le CEREMA."
        ),
        features=[
            "Chargement direct des données CEREMA (consommation d'espaces par commune)",
            "Calcul de la trajectoire ZAN et de l'écart aux objectifs de réduction",
            "Classements et comparaisons entre communes d'un même EPCI",
            "Graphiques d'évolution annuelle des flux de consommation",
            "Export des résultats (version Windows)",
        ],
        availability=[
            ("Windows", "Disponible (exécutable autonome)"),
            ("Android", "Disponible sur le Google Play Store"),
        ],
        download_intro="Téléchargements pour PPEI-Artificialisation :",
        buttons=[("Windows (.exe)", "primary"), ("Voir sur Google Play", "secondary")],
    ),
    dict(
        slug="budget-finances",
        code="M57",
        tag_class="",
        title="PPEI-Budget & Finances",
        meta_desc="Analyse des comptes communaux en nomenclature M57 : ratios, évolutions, projections.",
        lede=(
            "Analysez les comptes de votre commune en nomenclature "
            "budgétaire M57 : ratios financiers, évolution sur plusieurs "
            "exercices, et simulation de projection pour l'année à venir."
        ),
        features=[
            "9 volets d'analyse couvrant l'ensemble du compte administratif M57",
            "51 ratios financiers avec évolution N-5 → N",
            "Simulation de projection budgétaire bidirectionnelle (montant ↔ variation %)",
            "Traitement correct des spécificités M57 (chapitres 731, 68, 16...)",
            "Export PDF par volet (version Windows)",
        ],
        availability=[
            ("Windows", "Disponible (exécutable autonome)"),
            ("Android", "Disponible (version mobile simplifiée, sans export PDF)"),
        ],
        download_intro="Téléchargements pour PPEI-Budget & Finances :",
        buttons=[("Windows (.exe)", "primary"), ("Android (.apk)", "secondary")],
    ),
    dict(
        slug="emploi",
        code="URSSAF",
        tag_class="",
        title="PPEI-Emploi",
        meta_desc="Effectifs salariés et secteurs d'activité de votre territoire à partir des données URSSAF.",
        lede=(
            "Consultez les effectifs salariés et la répartition par "
            "secteur d'activité (APE) de votre commune ou de votre EPCI, "
            "à partir des données ouvertes de l'URSSAF."
        ),
        features=[
            "Vue globale des effectifs salariés du territoire",
            "Répartition par secteur d'activité (code APE)",
            "Carte par commune avec identification automatique du contour (API Géo)",
            "Filtre en cascade Département → EPCI → Commune",
            "Export CSV et PDF",
        ],
        availability=[
            ("Windows", "Disponible (exécutable autonome)"),
            ("Android", "Disponible"),
        ],
        download_intro="Téléchargements pour PPEI-Emploi :",
        buttons=[("Windows (.exe)", "primary"), ("Android (.apk)", "secondary")],
    ),
    dict(
        slug="rpls",
        code="RPLS",
        tag_class="",
        title="PPEI-RPLS",
        meta_desc="Répertoire du parc locatif social de la commune : occupation, loyers, caractéristiques.",
        lede=(
            "Explorez le Répertoire du Parc Locatif Social (RPLS) de "
            "votre commune : caractéristiques du parc, occupation, "
            "niveaux de loyers, avec une cartographie dédiée."
        ),
        features=[
            "Lecture des gros volumes RPLS filtrés par département",
            "Six volets d'analyse du parc locatif social",
            "Cartographie du parc (géocodage BAN)",
            "Export des résultats en PDF",
        ],
        availability=[
            ("Windows", "Disponible (exécutable autonome)"),
            ("Android", "Portage en cours"),
        ],
        download_intro="Téléchargements pour PPEI-RPLS :",
        buttons=[("Windows (.exe)", "primary")],
    ),
    dict(
        slug="bpe",
        code="BPE",
        tag_class="",
        title="PPEI-BPE",
        meta_desc="Équipements et services du territoire à partir de la Base Permanente des Équipements.",
        lede=(
            "Recensez les équipements et services présents sur votre "
            "territoire — commerces, écoles, santé, sport, services "
            "publics — à partir de la Base Permanente des Équipements "
            "(BPE), avec une cartographie par zonage."
        ),
        features=[
            "Import et synthèse des données BPE",
            "Sélecteur EPCI avec résolution automatique des communes membres",
            "Carte des équipements par zonage (fond de carte OpenStreetMap)",
            "Tableaux de résultats détaillés par catégorie d'équipement",
        ],
        availability=[
            ("Windows", "Disponible (exécutable autonome)"),
            ("Android", "Disponible"),
        ],
        download_intro="Téléchargements pour PPEI-BPE :",
        buttons=[("Windows (.exe)", "primary"), ("Android (.apk)", "secondary")],
    ),
    dict(
        slug="observatoire",
        code="OBSERVATOIRE",
        tag_class="",
        title="PPEI Observatoire",
        meta_desc="Vue d'ensemble du territoire en langage clair, avec indicateurs vert/orange/rouge.",
        lede=(
            "Une vue d'ensemble de votre territoire pensée pour les "
            "non-spécialistes : les mêmes indicateurs que les autres "
            "modules PPEI, présentés soit en données brutes tracées, "
            "soit en langage clair avec un indicateur d'alerte "
            "vert / orange / rouge."
        ),
        features=[
            "Double mode d'affichage : « Mode collectivité » (chiffres bruts et traçabilité) ou « Mode vulgarisation » (langage clair)",
            "Calcul de densité, d'écart à une référence, et de niveau d'alerte",
            "Base de données locale (SQLite), aucune dépendance à un serveur distant",
        ],
        availability=[
            ("Windows", "En développement"),
            ("Android", "En développement"),
        ],
        download_intro="PPEI Observatoire est encore en développement — revenez bientôt.",
        buttons=[],
    ),
    dict(
        slug="sirene",
        code="SIRENE",
        tag_class="",
        title="PPEI-SIREN/SIRET",
        meta_desc="Recherche et consultation des entreprises de la commune à partir du répertoire Sirene.",
        lede=(
            "Recherchez et consultez les entreprises implantées sur "
            "votre commune à partir des répertoires SIRENE (API "
            "DINUM « Recherche d'entreprises » et API INSEE Sirene)."
        ),
        features=[
            "Recherche d'entreprises par commune",
            "Consultation des fiches SIREN / SIRET",
            "S'intègre à l'architecture commune des modules PPEI",
        ],
        availability=[
            ("Windows", "En développement"),
            ("Android", "En développement"),
        ],
        download_intro="Ce module est encore en développement — revenez bientôt.",
        buttons=[],
    ),
    dict(
        slug="secours",
        code="SECOURS",
        tag_class=" tag-secours",
        title="Localise-moi Secours",
        meta_desc="Transmet votre position GPS et un message pré-rempli aux secours par SMS.",
        lede=(
            "Une application autonome, utile en extérieur ou en "
            "randonnée : elle géolocalise votre position et prépare un "
            "message avec vos coordonnées GPS, votre adresse "
            "administrative et une note personnelle, prêt à être "
            "envoyé aux secours par SMS."
        ),
        features=[
            "Géolocalisation GPS avec échantillonnage de la meilleure précision",
            "Adresse administrative (pays, région, département, commune) et carte",
            "Message pré-rempli et modifiable avant envoi",
            "Envoi par SMS vers un numéro modifiable (112 par défaut)",
            "Fonctionne même sans connexion internet : la géolocalisation et l'envoi du SMS ne dépendent pas des données mobiles",
            "Disponible en 5 langues (FR, EN, ES, IT, DE)",
        ],
        availability=[
            ("Android", "Disponible (.apk)"),
        ],
        download_intro="Téléchargement pour Localise-moi Secours :",
        buttons=[("Android (.apk)", "primary")],
    ),
]

for page in PAGES:
    html = TEMPLATE.format(
        title=page["title"],
        meta_desc=page["meta_desc"],
        tag_class=page["tag_class"],
        code=page["code"],
        lede=page["lede"],
        features=feature_items(page["features"]),
        availability_rows=availability_rows(page["availability"]),
        slug=page["slug"],
        download_intro=page["download_intro"],
        download_buttons=download_buttons(page["buttons"]) if page["buttons"] else '        <span class="note-todo">Aucun téléchargement disponible pour le moment.</span>',
    )
    filename = f"{page['slug']}.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Écrit : {filename}")
