from config import ETAPE_LABELS


def format_email(student, etape, review):
    """Formate le retour en email prêt à copier dans Outlook."""
    prenom = student['prenom']
    nom = student['nom']
    etape_label = ETAPE_LABELS.get(etape, etape)
    criteres = review.get('criteria_results', [])
    points_forts = review.get('points_forts', '')
    ameliorations = review.get('ameliorations', '')
    appreciation = review.get('appreciation', '')

    # Build criteria summary
    ok_count = sum(1 for c in criteres if c.get('statut') == 'OK')
    partiel_count = sum(1 for c in criteres if c.get('statut') == 'Partiel')
    non_count = sum(1 for c in criteres if c.get('statut') == 'Non')
    total = len(criteres)

    # Group criteria by category
    categories = {}
    for c in criteres:
        cat = c.get('categorie', 'Autre')
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(c)

    lines = []
    lines.append(f"Salutations {prenom},\n")
    lines.append(f"Voici mon retour sur ton travail pour l'étape « {etape_label} » de ton mémoire.\n")

    # Summary
    if total > 0:
        lines.append(f"📊 Synthèse : {ok_count} critère(s) validé(s), "
                      f"{partiel_count} partiel(s), {non_count} non rempli(s) sur {total}.\n")

    # Detailed criteria by category
    lines.append("─" * 40)
    lines.append("DÉTAIL PAR CRITÈRE")
    lines.append("─" * 40 + "\n")

    for cat, cat_criteres in categories.items():
        lines.append(f"▸ {cat}")
        for c in cat_criteres:
            statut = c.get('statut', '?')
            icon = '✅' if statut == 'OK' else '⚠️' if statut == 'Partiel' else '❌'
            lines.append(f"  {icon} {c.get('label', '')} → {statut}")
            if c.get('commentaire'):
                lines.append(f"     {c['commentaire']}")
        lines.append("")

    # Points forts
    lines.append("─" * 40)
    lines.append("✅ POINTS FORTS")
    lines.append("─" * 40)
    lines.append(points_forts + "\n")

    # Améliorations
    lines.append("─" * 40)
    lines.append("🔧 AMÉLIORATIONS PRIORITAIRES")
    lines.append("─" * 40)
    lines.append(ameliorations + "\n")

    # Appréciation
    lines.append("─" * 40)
    lines.append("💬 APPRÉCIATION GÉNÉRALE")
    lines.append("─" * 40)
    lines.append(appreciation + "\n")

    lines.append("N'hésite pas si tu as des questions.")
    lines.append("Bon courage pour la suite !\n")
    lines.append("Bien à toi,")

    return '\n'.join(lines)
