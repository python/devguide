from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, Image, KeepTogether, HRFlowable
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.shapes import Drawing, Rect, String, Circle, Line, Polygon
from reportlab.lib.colors import HexColor
from PIL import Image as PILImage
import os, glob, math, textwrap, random

# ---------- Fonts ----------
font_candidates = {
    "regular": ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"],
    "bold": ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"],
    "italic": ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf"],
}
for key, candidates in font_candidates.items():
    for p in candidates:
        if os.path.exists(p):
            pdfmetrics.registerFont(TTFont("DV"+key.title(), p))
            break

REG = "DVRegular"
BOLD = "DVbold"
ITAL = "DVitalic"

# ---------- Palette TURQUOISE PASTEL ----------
NAVY = HexColor("#1B4B6A")  # Bleu foncé pour les titres
BLUE = HexColor("#4F8FC9")
TURQ = HexColor("#5CC5C4")  # Turquoise principal
PALE_BLUE = HexColor("#E6F3F7")  # Bleu pastel clair
PALE_TURQ = HexColor("#E2F5F5")  # Turquoise pastel
PALE_PINK = HexColor("#F9EAF1")
PALE_LAV = HexColor("#EEE9FA")
PALE_YELLOW = HexColor("#FFF5D9")
PALE_GREEN = HexColor("#E8F5EA")
TEXT = HexColor("#243447")
MUTED = HexColor("#66788A")
WHITE = colors.white
LIGHT = HexColor("#F7FAFC")

# Couleurs de modules harmonisées avec le thème turquoise
MODULE_COLORS = [
    HexColor("#2D89C8"),  # Bleu
    HexColor("#5CC5C4"),  # Turquoise
    HexColor("#4A9B8E"),  # Vert d'eau
    HexColor("#3B7D8A"),  # Bleu-vert
    HexColor("#5BA3B8"),  # Bleu grisé
    HexColor("#4A8C9C"),  # Bleu profond
    HexColor("#6CB4B3"),  # Turquoise doux
]

# ---------- Styles ----------
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="BodyDV",
    fontName=REG,
    fontSize=9.5,
    leading=13.5,
    textColor=TEXT,
    spaceAfter=5,
    alignment=TA_JUSTIFY
))
styles.add(ParagraphStyle(
    name="SmallDV",
    fontName=REG,
    fontSize=7.5,
    leading=10.5,
    textColor=MUTED,
    spaceAfter=3
))
styles.add(ParagraphStyle(
    name="TitleDV",
    fontName=BOLD,
    fontSize=22,
    leading=26,
    textColor=NAVY,
    alignment=TA_CENTER,
    spaceAfter=10
))
styles.add(ParagraphStyle(
    name="H1DV",
    fontName=BOLD,
    fontSize=16,
    leading=20,
    textColor=NAVY,
    spaceAfter=8
))
styles.add(ParagraphStyle(
    name="H2DV",
    fontName=BOLD,
    fontSize=12,
    leading=15,
    textColor=NAVY,
    spaceBefore=5,
    spaceAfter=6
))
styles.add(ParagraphStyle(
    name="CardDV",
    fontName=REG,
    fontSize=8.5,
    leading=12,
    textColor=TEXT
))
styles.add(ParagraphStyle(
    name="CardBoldDV",
    fontName=BOLD,
    fontSize=8.8,
    leading=12,
    textColor=NAVY
))
styles.add(ParagraphStyle(
    name="CenterSmallDV",
    fontName=REG,
    fontSize=8.5,
    leading=11.5,
    textColor=TEXT,
    alignment=TA_CENTER
))
styles.add(ParagraphStyle(
    name="QuoteDV",
    fontName=ITAL,
    fontSize=10,
    leading=14.5,
    textColor=NAVY,
    leftIndent=15,
    rightIndent=15,
    spaceAfter=8
))
styles.add(ParagraphStyle(
    name="CoverDV",
    fontName=BOLD,
    fontSize=36,
    leading=42,
    textColor=WHITE,
    alignment=TA_CENTER
))
styles.add(ParagraphStyle(
    name="CoverSubDV",
    fontName=REG,
    fontSize=14,
    leading=19,
    textColor=WHITE,
    alignment=TA_CENTER
))

# ---------- Helpers ----------
def P(text, style="BodyDV"):
    return Paragraph(text, styles[style])

def title_bar(title, subtitle=None, color=NAVY):
    data = [[P(title, "H1DV")]]
    t = Table(data, colWidths=[17.5*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), PALE_TURQ),
        ("BOX", (0,0), (-1,-1), 0.8, color),
        ("LEFTPADDING", (0,0), (-1,-1), 12),
        ("RIGHTPADDING", (0,0), (-1,-1), 12),
        ("TOPPADDING", (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ]))
    out = [t]
    if subtitle:
        out += [Spacer(1, 4), P(subtitle, "SmallDV")]
    return out

def card_grid(items, cols=2, bg=WHITE):
    cells = []
    for item in items:
        if isinstance(item, tuple):
            head, body = item
            content = [P(head, "CardBoldDV"), P(body, "CardDV")]
        else:
            content = [P(item, "CardDV")]
        cells.append(content)

    while len(cells) % cols:
        cells.append([P("", "CardDV")])

    rows = []
    for i in range(0, len(cells), cols):
        row = []
        for c in cells[i:i+cols]:
            row.append(c)
        rows.append(row)

    table = Table(rows, colWidths=[8.65*cm]*cols, hAlign="LEFT")
    ts = [
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("BOX", (0,0), (-1,-1), 0.5, HexColor("#C5DEE5")),
        ("INNERGRID", (0,0), (-1,-1), 0.4, HexColor("#D5E8EF")),
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("LEFTPADDING", (0,0), (-1,-1), 9),
        ("RIGHTPADDING", (0,0), (-1,-1), 9),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ]
    table.setStyle(TableStyle(ts))
    return table

def mindmap(title, center, branches, color=TURQ):
    d = Drawing(510, 220)
    cx, cy = 255, 110

    # Cercle central
    d.add(Circle(cx, cy, 54, fillColor=PALE_TURQ, strokeColor=color, strokeWidth=2.5))
    d.add(String(cx, cy+5, center, fontName=BOLD, fontSize=10.5, fillColor=NAVY, textAnchor="middle"))
    d.add(String(cx, cy-9, "IDÉE-CLÉ", fontName=REG, fontSize=7, fillColor=MUTED, textAnchor="middle"))

    positions = [(90,175), (420,175), (65,75), (445,75), (255,35)]
    branch_colors = [PALE_TURQ, PALE_LAV, PALE_PINK, PALE_YELLOW, PALE_GREEN]

    for i, b in enumerate(branches[:5]):
        x, y = positions[i]
        d.add(Line(cx, cy, x, y, strokeColor=color, strokeWidth=1.2))
        d.add(Rect(x-65, y-24, 130, 48, rx=10, ry=10, fillColor=branch_colors[i], strokeColor=color, strokeWidth=0.8))

        words = b.split()
        lines = []
        cur = ""
        for w in words:
            if len(cur) + len(w) + 1 > 22:
                lines.append(cur)
                cur = w
            else:
                cur = (cur + " " + w).strip()
        if cur:
            lines.append(cur)

        for j, line in enumerate(lines[:3]):
            d.add(String(x, y+10-j*10, line, fontName=REG, fontSize=7.2, fillColor=TEXT, textAnchor="middle"))

    return d

def exercise_page(title, exercises, color):
    story = [P(title, "H1DV"),
             P("Consigne : réponds d'abord sans regarder la correction. Justifie quand la question le demande.", "SmallDV"),
             Spacer(1, 5)]
    items = []
    for i, e in enumerate(exercises, 1):
        items.append((f"{i}.", e))
    story.append(card_grid(items, cols=1, bg=LIGHT))
    return story

def correction_page(title, corrections, color):
    story = [P(title, "H1DV"),
             P("Correction expliquée : la réponse attendue est suivie d'un rappel de méthode.", "SmallDV"),
             Spacer(1, 5)]
    for i, (ans, why) in enumerate(corrections, 1):
        story.append(P(f"{i}. Réponse : {ans}", "CardDV"))
        story.append(P(f"Pourquoi ? {why}", "SmallDV"))
        story.append(Spacer(1, 2))
    return story

def text_questions(text, qs):
    return [
        P("TEXTE ORIGINAL — entraînement", "H2DV"),
        P(text, "QuoteDV"),
        P("Compréhension — 6 points", "H2DV"),
        card_grid([(f"Question {i+1}", q) for i, q in enumerate(qs)], cols=1, bg=PALE_BLUE)
    ]

def production_page(prompt, tips, model=None):
    out = [P("PRODUCTION ÉCRITE", "H1DV"),
           P(prompt, "H2DV")]
    out.append(P("Plan conseillé : " + tips, "BodyDV"))
    out.append(P("Boîte à expressions : Au début…, Ensuite…, Cependant…, Finalement…, À mon avis…, En conclusion…", "SmallDV"))
    if model:
        out.append(P("Modèle possible :", "H2DV"))
        out.append(P(model, "BodyDV"))
    else:
        out.append(P("Défi : utilise au moins 3 connecteurs, 2 mots du champ lexical et une phrase complexe.", "CardDV"))
    return out

def devoir_page(module, num, text, lang_ex, prod):
    story = [P(f"DEVOIR PILOTE {num} — {module['title']}", "H1DV"),
             P("Barème : Compréhension 6 pts • Langue 6 pts • Production 7 pts • Total 20 pts", "SmallDV"),
             P("A. Compréhension — 6 points", "H2DV"),
             P(text, "QuoteDV")]

    qs = [
        "Donne le thème du texte et justifie par deux indices.",
        "Relève une information précise et reformule-la.",
        "Explique le sentiment ou le point de vue du personnage principal.",
        "Relève un élément de description ou d'argumentation.",
    ]
    story.append(card_grid([(f"{i+1} — 1,5 pt", q) for i, q in enumerate(qs)], cols=1, bg=PALE_BLUE))

    story += [
        P("B. Langue — 6 points", "H2DV"),
        card_grid([(f"{i+1} — 1,5 pt", e) for i, e in enumerate(lang_ex)], cols=1, bg=PALE_YELLOW),
        P("C. Production — 7 points", "H2DV"),
        P(prod, "BodyDV"),
        P("Conseil : organise ton texte en introduction, développement et conclusion lorsque le sujet s'y prête.", "SmallDV")
    ]
    return story

def devoir_correction(module, num, answers, prod_model):
    story = [P(f"CORRIGÉ DU DEVOIR PILOTE {num}", "H1DV"),
             P("Les réponses sont proposées comme modèle. D'autres formulations correctes sont possibles.", "SmallDV")]
    for i, (a, e) in enumerate(answers, 1):
        story.append(P(f"{i}. {a}", "CardDV"))
        story.append(P(f"Explication : {e}", "SmallDV"))
        story.append(Spacer(1, 2))
    story.append(P("Production — exemple corrigé", "H2DV"))
    story.append(P(prod_model, "BodyDV"))
    story.append(P("Pourquoi cette production fonctionne : elle respecte la consigne, progresse logiquement, emploie des connecteurs et reprend le vocabulaire du module.", "SmallDV"))
    return story

# ---------- Données des modules ----------
modules = [
    {
        "title": "MODULE 1 — RENCONTRES",
        "objective": "Lire des récits de fiction • Raconter une histoire vraie ou imaginaire",
        "texts": "Un enfant venu d'ailleurs • Au hasard d'une rencontre • Le Loup et l'Agneau • Naissance d'une amitié",
        "vocab_title": "La rencontre, les émotions et le récit",
        "vocab": [
            ("rencontrer", "faire la connaissance de quelqu'un"),
            ("apercevoir", "voir rapidement"),
            ("trouble", "émotion qui déstabilise"),
            ("timide", "qui manque d'assurance devant les autres"),
            ("ému", "fortement touché par une émotion"),
            ("surpris", "étonné par quelque chose d'inattendu"),
            ("sympathie", "sentiment positif envers quelqu'un"),
            ("méfiance", "attitude de prudence ou de doute"),
            ("complicité", "relation fondée sur une bonne entente"),
            ("hasard", "événement imprévu, sans intention préalable"),
            ("amitié", "affection durable entre personnes"),
            ("récit", "texte qui raconte une suite d'événements"),
        ],
        "lexical": ["regard", "sourire", "voix", "geste", "silence", "émotion", "surprise", "admiration", "peur", "joie", "trouble", "confiance"],
        "expressions": [
            "Au premier regard…",
            "Dès que je l'ai aperçu(e),…",
            "Je fus immédiatement frappé(e) par…",
            "Cette rencontre changea…",
            "Peu à peu, nous avons appris à…",
            "À partir de ce jour-là,…",
            "Je n'oublierai jamais ce moment.",
            "Cette rencontre restera gravée dans ma mémoire."
        ],
        "language": [
            ("Les temps du récit", "présent, imparfait, passé composé, passé simple, plus-que-parfait", "Choisir le temps selon le rôle de l'action : cadre/habitude à l'imparfait ; action achevée au passé composé ou au passé simple ; action antérieure au plus-que-parfait."),
            ("Les subordonnées de temps", "quand, lorsque, dès que, avant que, après que, tandis que, pendant que", "Elles situent une action par rapport à une autre et permettent d'exprimer la simultanéité, l'antériorité ou la postériorité.")
        ],
        "productions": [
            "Raconter une première rencontre qui a changé ta vie.",
            "Modifier le début d'un récit en imaginant une autre rencontre.",
            "Inventer une rencontre inattendue dans un lieu public.",
            "Raconter la naissance d'une amitié entre deux élèves.",
            "Écrire une fable dont la morale porte sur l'amitié.",
            "Raconter une rencontre imaginaire avec un personnage venu d'ailleurs."
        ],
        "visual": "Une scène de rencontre : deux élèves se découvrent dans une cour, avec des bulles de dialogue et une ligne du temps."
    },
    {
        "title": "MODULE 2 — SCÈNES DE LA VIE EN FRANCE",
        "objective": "Découvrir une autre culture • Décrire un site, une scène de la vie courante",
        "texts": "Le train de banlieue • L'alpage • Les voilà ! • Le pont Mirabeau",
        "vocab_title": "La ville, les lieux, la localisation et la description",
        "vocab": [
            ("banlieue", "zone située autour d'une grande ville"),
            ("quartier", "partie d'une ville"),
            ("alpage", "pâturage de montagne utilisé en été"),
            ("monument", "construction remarquable d'une ville"),
            ("quai", "espace aménagé au bord d'un fleuve ou d'une gare"),
            ("itinéraire", "chemin suivi pour aller d'un lieu à un autre"),
            ("animé", "qui est vivant, fréquenté et dynamique"),
            ("pittoresque", "qui présente un aspect original et agréable à observer"),
            ("désert", "qui est presque sans habitants ou sans activité"),
            ("majestueux", "qui impressionne par sa grandeur"),
            ("décrire", "présenter les caractéristiques d'un lieu ou d'une personne"),
            ("localiser", "indiquer où se trouve quelque chose"),
        ],
        "lexical": ["centre-ville", "périphérie", "rue", "place", "gare", "pont", "fleuve", "montagne", "immeuble", "commerce", "transport", "paysage"],
        "expressions": [
            "À droite/à gauche de…",
            "Au premier plan…",
            "À l'arrière-plan…",
            "Au centre de l'image…",
            "On peut observer…",
            "Le lieu se caractérise par…",
            "Ce qui attire surtout l'attention, c'est…",
            "L'ambiance semble…"
        ],
        "language": [
            ("Les expansions du nom", "épithète, complément du nom, apposition, proposition relative", "Elles enrichissent le groupe nominal et permettent de préciser une personne, un objet ou un lieu."),
            ("La nominalisation et les verbes attributifs", "former un nom à partir d'un verbe/adjectif ; être, sembler, paraître, devenir, rester", "La nominalisation rend le style plus informatif. Les verbes attributifs relient le sujet à une caractéristique.")
        ],
        "productions": [
            "Décrire une rue française à partir d'une image.",
            "Présenter un monument ou un site touristique.",
            "Décrire une scène de la vie quotidienne dans une grande ville.",
            "Décrire un quartier en indiquant ses qualités et ses défauts.",
            "Rédiger un petit reportage sur une ville française.",
            "Insérer une description dans un récit de voyage."
        ],
        "visual": "Une carte simplifiée de ville avec gare, pont, quartier, parc et fleuve ; chaque élément est légendé."
    },
    {
        "title": "MODULE 3 — JEUNESSE SANS FRONTIÈRES",
        "objective": "Communiquer avec l'autre • Écrire différents types de lettres",
        "texts": "Quelle carrière ? • Les Papous • Le Schpountz • Les idoles de la chanson",
        "vocab_title": "Les jeunes, la communication, les métiers et les loisirs",
        "vocab": [
            ("orientation", "choix d'une direction scolaire ou professionnelle"),
            ("carrière", "parcours professionnel d'une personne"),
            ("talent", "aptitude particulière"),
            ("loisir", "activité pratiquée pendant le temps libre"),
            ("idole", "personne admirée par un grand nombre de personnes"),
            ("correspondance", "échange de lettres ou de messages"),
            ("destinataire", "personne à qui une lettre est adressée"),
            ("expéditeur", "personne qui envoie une lettre"),
            ("invitation", "message par lequel on propose à quelqu'un de venir"),
            ("réclamation", "message qui signale un problème et demande une solution"),
            ("dialogue", "échange de paroles entre deux personnes ou plus"),
            ("prospectus", "document bref destiné à informer ou promouvoir"),
        ],
        "lexical": ["école", "métier", "avenir", "projet", "passion", "musique", "cinéma", "sport", "réseau", "message", "lettre", "rencontre"],
        "expressions": [
            "Je me permets de vous écrire afin de…",
            "Je souhaiterais vous demander…",
            "Merci d'avance pour votre réponse.",
            "Dans l'attente de votre réponse…",
            "Cher/Chère…",
            "Bien cordialement.",
            "Salut ! Comment vas-tu ?",
            "À bientôt !"
        ],
        "language": [
            ("Les temps du discours", "présent, passé composé, futur", "Ils permettent de parler de la situation actuelle, d'un événement passé ou d'un projet à venir."),
            ("Le discours rapporté et la concordance", "discours direct, indirect ; changements de pronoms, temps et repères", "Au discours indirect, on adapte la phrase au verbe introducteur et au contexte : « Il dit qu'il vient » / « Il a dit qu'il venait ».")
        ],
        "productions": [
            "Écrire une lettre personnelle à un ami.",
            "Rédiger une lettre pour demander des informations.",
            "Écrire une invitation à un événement scolaire.",
            "Écrire une réclamation polie à un service.",
            "Créer un prospectus pour un club de jeunes.",
            "Transformer un dialogue en récit au discours indirect."
        ],
        "visual": "Un tableau « Qui ? À qui ? Pourquoi ? » avec enveloppe, message, téléphone et bulles de dialogue."
    },
    {
        "title": "MODULE 4 — LA SOCIÉTÉ DE CONSOMMATION",
        "objective": "Lire un message publicitaire • Exprimer une prise de position favorable/défavorable",
        "texts": "La création des besoins • La télévision et les jeunes • La publicité emprisonne l'homme…",
        "vocab_title": "La publicité, les médias, la consommation et l'opinion",
        "vocab": [
            ("consommer", "acheter ou utiliser un bien ou un service"),
            ("besoin", "ce qui est nécessaire ou ressenti comme nécessaire"),
            ("désir", "envie de posséder ou de faire quelque chose"),
            ("publicité", "message destiné à promouvoir un produit, un service ou une idée"),
            ("marque", "nom ou signe qui identifie un produit"),
            ("slogan", "phrase courte et mémorable d'une campagne"),
            ("cible", "public auquel un message est destiné"),
            ("influence", "action qui modifie une opinion ou un comportement"),
            ("persuader", "amener quelqu'un à adopter une idée"),
            ("convaincre", "faire accepter une idée grâce à des arguments"),
            ("critique", "qui examine les défauts et les limites"),
            ("substitut", "élément qui remplace un autre élément"),
        ],
        "lexical": ["achat", "prix", "promotion", "produit", "client", "marque", "média", "écran", "réseau", "influence", "opinion", "argument"],
        "expressions": [
            "À mon avis,…",
            "Je suis favorable à…",
            "Je suis plutôt contre…",
            "Je reconnais que…, cependant…",
            "Il ne faut pas oublier que…",
            "Cette publicité cherche à…",
            "Le message met l'accent sur…",
            "En réalité,…"
        ],
        "language": [
            ("Les substituts et la reprise nominale", "pronoms, synonymes, groupes nominaux, périphrases", "Ils évitent les répétitions et assurent la cohérence du texte."),
            ("Accord du participe passé et modes", "verbes pronominaux ; indicatif, conditionnel, subjonctif", "L'accord dépend de la construction du verbe. Le conditionnel exprime souvent l'hypothèse ou l'atténuation ; le subjonctif apparaît après certaines expressions de volonté, doute, nécessité ou sentiment.")
        ],
        "productions": [
            "Commenter une publicité et expliquer son objectif.",
            "Écrire un texte pour/contre la publicité destinée aux jeunes.",
            "Rédiger un message informatif sur un produit.",
            "Protester contre une publicité trompeuse.",
            "Créer une publicité responsable et expliquer ses choix.",
            "Défendre une opinion nuancée sur les réseaux sociaux et la consommation."
        ],
        "visual": "Une affiche publicitaire déconstruite : image, slogan, logo, cible, argument, émotion et appel à l'action."
    },
    {
        "title": "MODULE 5 — SAUVONS LA PLANÈTE TERRE",
        "objective": "Défendre une cause • Expliquer • Prescrire",
        "texts": "Dévastation • Le chant du rossignol • Docilité",
        "vocab_title": "L'environnement, la protection et l'argumentation",
        "vocab": [
            ("déforestation", "destruction importante des forêts"),
            ("pollution", "dégradation de l'environnement par des substances ou activités nuisibles"),
            ("biodiversité", "diversité des êtres vivants et des milieux"),
            ("déchet", "objet ou matière dont on veut se débarrasser"),
            ("recycler", "transformer un déchet pour le réutiliser"),
            ("préserver", "protéger pour maintenir en bon état"),
            ("économiser", "utiliser une ressource avec modération"),
            ("gaspillage", "utilisation inutile ou excessive d'une ressource"),
            ("urgence", "situation qui demande une action rapide"),
            ("interdiction", "règle qui empêche une action"),
            ("prescription", "consigne qui recommande ou impose une action"),
            ("cause", "raison qui explique un fait"),
            ("conséquence", "résultat produit par un fait"),
        ],
        "lexical": ["climat", "forêt", "océan", "eau", "air", "énergie", "déchet", "animal", "plante", "recyclage", "protection", "écologie"],
        "expressions": [
            "Il est urgent de…",
            "Il faut absolument…",
            "Il est interdit de…",
            "Nous devons…",
            "Pour éviter que…",
            "Grâce à…",
            "À cause de…",
            "Par conséquent,…",
            "Ainsi,…",
            "Afin de…"
        ],
        "language": [
            ("Cause, conséquence et but", "parce que, puisque, grâce à, à cause de ; donc, ainsi, par conséquent ; pour, afin de", "Choisir le connecteur selon le sens : expliquer la raison, montrer le résultat ou présenter l'objectif."),
            ("Prescription et interdiction", "il faut, il est nécessaire de, devoir, il est interdit de, défense de", "Ces formes servent à donner une consigne claire et adaptée au destinataire.")
        ],
        "productions": [
            "Rédiger une requête pour protéger un espace naturel.",
            "Écrire un plaidoyer en faveur du recyclage.",
            "Proposer des solutions contre le gaspillage de l'eau.",
            "Créer une campagne écologique pour le collège.",
            "Rédiger un texte cause-conséquence sur la pollution.",
            "Écrire un règlement écologique pour une classe."
        ],
        "visual": "Le cycle « problème → cause → conséquence → solution » avec icônes d'eau, arbre, énergie et déchets."
    },
    {
        "title": "MODULE 6 — PASSIONS",
        "objective": "Lire une œuvre intégrale • Rendre compte de sa lecture",
        "texts": "Confessions d'une femme • Un aveugle au piano",
        "vocab_title": "Les passions, les sentiments, les registres et le style",
        "vocab": [
            ("passion", "sentiment très intense qui pousse fortement à agir"),
            ("jalousie", "peur ou mécontentement liés à l'attention accordée à autrui"),
            ("admiration", "sentiment de respect ou d'émerveillement"),
            ("rivalité", "opposition entre personnes qui cherchent le même objectif"),
            ("souvenir", "image ou événement conservé dans la mémoire"),
            ("aveu", "fait de reconnaître ou révéler quelque chose"),
            ("émotion", "réaction affective provoquée par une situation"),
            ("registre", "manière de s'exprimer selon l'effet recherché"),
            ("comparaison", "rapprochement de deux éléments avec un outil comparatif"),
            ("métaphore", "image qui rapproche deux réalités sans outil comparatif"),
            ("hyperbole", "exagération volontaire destinée à produire un effet"),
            ("ironie", "manière de dire quelque chose en laissant entendre une autre idée"),
        ],
        "lexical": ["amour", "colère", "joie", "tristesse", "peur", "admiration", "jalousie", "souvenir", "désir", "espoir", "regret", "émotion"],
        "expressions": [
            "J'ai particulièrement apprécié…",
            "Ce qui m'a marqué(e), c'est…",
            "À mon sens,…",
            "Je recommande cette œuvre parce que…",
            "Le personnage m'a surpris(e) par…",
            "L'auteur met en valeur…",
            "Cette image souligne…",
            "Le texte produit un effet de…"
        ],
        "language": [
            ("Champs lexicaux et registres", "repérer les mots dominants ; familier, courant, soutenu", "Le champ lexical aide à identifier le thème. Le registre renseigne sur le ton et l'effet produit."),
            ("Figures de style", "comparaison, métaphore, hyperbole, personnification, ironie", "Les figures donnent une image plus expressive et permettent de comprendre l'intention de l'auteur.")
        ],
        "productions": [
            "Rendre compte d'une nouvelle lue.",
            "Justifier une préférence pour un personnage.",
            "Exprimer un point de vue sur une passion.",
            "Rédiger une critique simple d'une œuvre.",
            "Décrire l'effet d'une figure de style dans un passage.",
            "Écrire la quatrième de couverture d'une nouvelle."
        ],
        "visual": "Une carte « sentiment → mots → image → effet » avec exemples de comparaison, métaphore et hyperbole."
    },
    {
        "title": "MODULE 7 — PROGRÈS ET BONHEUR",
        "objective": "Porter un regard critique sur la science • Exprimer une prise de position nuancée",
        "texts": "La télématique • Science et avenir • Matière à rire",
        "vocab_title": "Science, technologie, progrès, bonheur et débat",
        "vocab": [
            ("progrès", "amélioration ou développement dans un domaine"),
            ("innovation", "nouvelle idée, méthode ou technologie"),
            ("télématique", "ensemble des techniques associant informatique et télécommunications"),
            ("robotique", "domaine consacré à la conception et à l'utilisation des robots"),
            ("découverte", "fait de trouver ou de mettre au jour quelque chose"),
            ("avantage", "élément favorable"),
            ("limite", "ce qui réduit la portée ou l'efficacité de quelque chose"),
            ("risque", "possibilité qu'un événement négatif se produise"),
            ("bonheur", "état durable de satisfaction et de bien-être"),
            ("nuancé", "qui présente plusieurs aspects et évite une opinion trop absolue"),
            ("modalisateur", "mot ou expression qui montre le degré de certitude ou le point de vue"),
            ("concession", "reconnaissance d'un argument adverse avant de défendre sa propre idée"),
        ],
        "lexical": ["science", "technologie", "ordinateur", "internet", "robot", "médecine", "énergie", "recherche", "avenir", "innovation", "risque", "bonheur"],
        "expressions": [
            "Il me semble que…",
            "Je suis convaincu(e) que…",
            "On peut certes…, mais…",
            "Même si…",
            "Bien que…",
            "D'un côté…, de l'autre…",
            "Il est possible que…",
            "En définitive,…"
        ],
        "language": [
            ("Prise de position et modalisateurs", "certainement, probablement, peut-être, à mon avis, il semble que", "Les modalisateurs permettent de doser la certitude et de rendre l'opinion plus précise."),
            ("Condition, opposition et concession", "si, à condition que, mais, pourtant, cependant, bien que, même si", "La condition présente une situation nécessaire ; l'opposition rapproche deux idées différentes ; la concession reconnaît un fait tout en maintenant une autre position.")
        ],
        "productions": [
            "Défendre ou réfuter une thèse sur le progrès.",
            "Écrire un
