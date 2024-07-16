def brutto_netto_rechner(brutto, steuerklasse=1, kinderfreibetrag=0, kirchensteuer=True):
    # Sozialversicherungsbeiträge (2024)
    rentenversicherung = 0.093  # 9.3%
    arbeitslosenversicherung = 0.013  # 1.3%
    krankenversicherung = 0.073 + 0.0155  # 7.3% + 1.55% Zusatzbeitrag
    pflegeversicherung = 0.023  # 2.3%

    # Berechnung der Sozialversicherungsbeiträge
    rv_beitrag = brutto * rentenversicherung
    av_beitrag = brutto * arbeitslosenversicherung
    kv_beitrag = brutto * krankenversicherung
    pv_beitrag = brutto * pflegeversicherung

    sozialabgaben = rv_beitrag + av_beitrag + kv_beitrag + pv_beitrag

    # Steuerfreibetrag pro Monat
    steuerfreibetrag_monatlich = 10347 / 12

    # Zu versteuerndes Einkommen
    zu_versteuerndes_einkommen = brutto - sozialabgaben - steuerfreibetrag_monatlich

    # Einkommensteuer nach Grundtabelle 2024 (vereinfachtes Modell)
    if zu_versteuerndes_einkommen <= 0:
        einkommensteuer = 0
    elif zu_versteuerndes_einkommen <= 10908 / 12:
        einkommensteuer = (zu_versteuerndes_einkommen - 10347 / 12) * 0.14
    elif zu_versteuerndes_einkommen <= 14254 / 12:
        einkommensteuer = (zu_versteuerndes_einkommen - 10908 / 12) * 0.2397 + 24 / 12
    elif zu_versteuerndes_einkommen <= 57918 / 12:
        einkommensteuer = (zu_versteuerndes_einkommen - 14254 / 12) * 0.42 + 1024 / 12
    else:
        einkommensteuer = (zu_versteuerndes_einkommen - 57918 / 12) * 0.45 + 8790 / 12

    # Solidaritätszuschlag (5.5% der Einkommensteuer, nur wenn Einkommensteuer > 972 EUR im Jahr)
    soli = 0 if einkommensteuer <= 81 else einkommensteuer * 0.055

    # Kirchensteuer (8% der Einkommensteuer in Hessen)
    kirchensteuer_betrag = einkommensteuer * 0.08 if kirchensteuer else 0

    steuern = einkommensteuer + soli + kirchensteuer_betrag

    # Netto Berechnung
    netto = brutto - sozialabgaben - steuern

    return netto, rv_beitrag, av_beitrag, kv_beitrag, pv_beitrag, einkommensteuer, soli, kirchensteuer_betrag

# Benutzer-Eingabe für das Brutto-Gehalt
brutto_gehalt = float(input("Bitte geben Sie Ihr Brutto-Gehalt ein: "))
netto_gehalt, rv_beitrag, av_beitrag, kv_beitrag, pv_beitrag, einkommensteuer, soli, kirchensteuer_betrag = brutto_netto_rechner(brutto_gehalt)

print(f"Brutto-Gehalt: {brutto_gehalt:.2f} EUR")
print(f"Netto-Gehalt: {netto_gehalt:.2f} EUR")

# Details
print("\nDetails:")
print(f"Rentenversicherung: {rv_beitrag:.2f} EUR")
print(f"Arbeitslosenversicherung: {av_beitrag:.2f} EUR")
print(f"Krankenversicherung: {kv_beitrag:.2f} EUR")
print(f"Pflegeversicherung: {pv_beitrag:.2f} EUR")
print(f"Lohnsteuer: {einkommensteuer:.2f} EUR")
print(f"Solidaritätszuschlag: {soli:.2f} EUR")
print(f"Kirchensteuer: {kirchensteuer_betrag:.2f} EUR")
