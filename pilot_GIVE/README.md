# Facebook workflow

## Voorlopige workflow

1. parse CSV (fullname +  location)
2. search Google
3. get URL's
4. scrape image url's facebook
   1. profiles ==> `get_profile` ==> `profile['profile_picture']`
   2. pages ==> `get_profile`: om onduidelijke redenen is de foto erg klein
   3. posts ==> `get_posts + id`
5. download images met wget (werkt)

## Bevindingen

1. het lijkt dat het niet nodig is om cookies te gebruiken ==> positief
2. veel politici hebben geen eigen facebookpagina, ze hebben eerder een facebookprofiel (persoonlijk). hoe gaan we hiermee om?
3. er zijn ook politici die gewoon geen facebook hebben. de moeilijkheid is dan om geen fout profiel te openen (staan meestal wel lager) ==> check doen met `places_lived`?
4. sommige politici hebben geen places_lived en worden dus niet gevonden. eventueel testen of het helpt om partij erbij te zetten?
5. er zijn ook politici die gewoon niet in een google search opduiken, ook al hebben ze wel een facebookprofiel met hun locatie erbij
6. ook bekende politici kunnen geen facebookprofiel hebben
7. provincieraadsleden zijn lastig. hier misschien eerder werken met politieke partij? probleem is dat die vaak niet vermeld zijn in de databank. zoeken op facebook zorgt ook soms voor een foute match.

## TODO met Openrefine data

1. haal alle afbeeldingen van wikidata
2. haal alle afbeeldingen van wikimedia commons
3. haal afbeeldingen via de facebookid
   1. haal de json met de profile-info
   2. ga op zoek naar de key voor de profile pic
   3. haal de url op via wget
   4. downloaden maar!
4. maak een CSV met de Twitter-mensen en geef ze aan Lode
5. haal afbeeldingen van linkedin
   1. haal de json met de tool
   2. ga op zoek in de json naar de profile pic
   3. haal de url op via wget
   4. downloaden maar!

## TODO facebook

1. zoek personen via de google search
2. scrape ze via facebook_scraper
3. controleer hun naam `["Name"]` en `["Places lived"]`
4. komen ze overeen? behou ze op de lijst en achteraf scrapen.
