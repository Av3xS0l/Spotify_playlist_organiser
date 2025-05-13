# Spotify_playlist_organiser  
## Uzdevums  
Klausoties mūziku bieži rodas situācijas, kad klausīšanās saraksti piepildās ar dziesmām, kuras lietotājs vairs nevēlas klausīties. Tas rada lielu sajukumu šajos sarakstos un padara sarežģītu dziesmu atrašanu. Tāpēc mēs izstrādājam risinājumu, kurš ļauj noņemt no klausīšanās sarakstiem dziesmas, kas bieži tiek pārtītas, kā arī pievienotas dziesmas, kuras šajā sarakstā neatrodas, taču tiek bieži klausītas.  

## Veidotāji
- Patrīcija Krēsliņa
- Patriks Gustavs Rinkevičs

# DEV - tiks noņemts
## Steps for developement  
1. Lietotājam jāievada savs Spotify api key+secret ja ieiet pirmo reizi   
2. Wrapper funkcijas:   
2.1. Iegūst dziesmu, kas pašreiz skan.  
2.2. Iegūt playlisti, kas pašreiz skan  
2.3. Iegūst, vai šobrīd skan shuffle  
2.4. Iegūst pēdējās N dziesmas  
2.5. determines if skiped  

# Uzstādīšana
> ⚠️Programmas lietošanai ir nepieciešams *Spotify* konts⚠️
## *Spotify* Web Api konta izveide
1. Dodieties uz saiti [https://developer.spotify.com/]() un spiediet uz **Log in** augšējā labajā stūrī.  
2. Pierakstieties izmantojot savu *Spotify* kontu
3. Izvēloties savu profilu dodieties uz sadaļu *Dashboard*  
4. Izveidojiet jaunu aplikāciju (var vadīties pēc [https://developer.spotify.com/documentation/web-api/tutorials/getting-started]())
5. Izveidojot aplikāciju pievērsiet uzmanību ***redirect URI***

## Vides uzstādīšana
1. Projekta mapē izveidojiet jaunu failu ar nosaukumu `.env`.
2. Atveriet šo failu un pievienojiet tam sekojošos parametrus no *Spotify* izveidotās aplikācijas:  

    `SPOTIPY_CLIENT_ID = '...'`  
    `SPOTIPY_CLIENT_SECRET = '...'`    
    `SPOTIPY_REDIRECT_URI = '...'`  
    Daudzpunktes vietā liekot attiecīgo vērtību no *Spotify* Dashborad sadaļas.
3. Pārliecinieties, ka iekārtā ir instalēta `python` versija >= **3.13.X**
4. Lai instalētu visas nepieciešamās bibliotēkas projekta mapē izpildiet komandu:  
`pip install -r requirements.txt`

# Lietošana  
...

# Dokumentācija
...
