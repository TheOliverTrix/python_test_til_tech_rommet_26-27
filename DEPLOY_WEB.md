# Pikselfinner på GitHub og Vercel

Appen er en statisk nettside uten byggesteg eller eksterne biblioteker. Kameraet ber om tillatelse først når brukeren trykker **Start kamera**. Kamera- og bildepiksler behandles lokalt i nettleseren.

## Test lokalt

Kamera krever en sikker tilkobling. Bruk `localhost` i stedet for å åpne HTML-filen direkte:

1. Åpne terminalen i prosjektmappen.
2. Kjør `python -m http.server 8000`.
3. Åpne `http://localhost:8000` i nettleseren.

## Publiser med GitHub og Vercel

1. Push `index.html` til GitHub.
2. I Vercel velger du **Add New → Project** og importerer GitHub-repoet.
3. Velg **Other** som Framework Preset. Det trengs ikke build-kommando eller avhengigheter; la Vercel publisere prosjektroten.
4. Trykk **Deploy**. Vercel gir appen en HTTPS-adresse, som trengs for kameratilgang.

På første kamerabruk må brukeren tillate tilgang i nettleseren. Hvis tilgang avslås, kan den endres via ikonet ved adresselinjen.
