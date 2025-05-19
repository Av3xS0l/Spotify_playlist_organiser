# Spotify_playlist_organiser  
## Uzdevums  
Klausoties mūziku bieži rodas situācijas, kad klausīšanās saraksti piepildās ar dziesmām, kuras lietotājs vairs nevēlas klausīties. Tas rada lielu sajukumu šajos sarakstos un padara sarežģītu dziesmu atrašanu. Tāpēc mēs izstrādājam risinājumu, kurš ļauj noņemt no klausīšanās sarakstiem dziesmas, kas bieži tiek pārtītas, kā arī pievienotas dziesmas, kuras šajā sarakstā neatrodas, taču tiek bieži klausītas.  

## Veidotāji
- Patrīcija Krēsliņa
- Patriks Gustavs Rinkevičs

# DEV - tiks noņemts
## Steps for developement  
1. Lietotājam jāievada savs Spotify api key+secret ja ieiet pirmo reizi   

2. API iegūtie dati:  
2.1 Lietotāja id
2.2 Atskaņojuma tips (dziesma, epizode, reklāma)  
2.3 Vai ir ieslēgts ShufflePlay (ir, nav)  
2.4 Milisekundes, cik ilgi dziesma jau ir atskaņota  
2.5 Dati par pašreiz atskaņoto playlisti (vārds, id, uri, īpašnieka id)  
2.6 Pašreiz atskaņotās playlistes dziesmu saraksts  
2.7 Dati par pašreiz atskaņoto dziesmu (vārds, id, uri, izpildītājs, ilgums, bilde)  

3. Wrapper funkcijas:   
2.1. is_users_playlist - 
progress - nosaka vai dziesma ir noklausīta vairāk kā 'treshold' 
2.2.   

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
Kods palaists terminālī:
1. Dziesma ir playlistē un tiek noklausīta vairāk kā 40% tās garuma - kods neko nedara, dziesma paliek playlistē;  
2. Dziesma ir playlistē bet netiek noklausīta vairāk kā 40% tās garuma - dziesmas id tiek saglabāts sarakstā;  
2.1. Kad dziesmas id ir saglabāts sarakstā 3 reizes - dziesma tiek izņemta no playlistes;  
3. Dziesma nav playlistē (ShufflePlay) un tiek noklausīta vismaz 80% tās garuma - dziesma tiek pievienota playlistei;

Terminālī ir redzamas pēdējās 3 veiktās darbības un attiecīgās dziesmas nosaukums.

# Dokumentācija
...
