# Spotify_playlist_organiser  
## Uzdevums  

## Dalībnieki
- Patrīcija Krēsliņa
- Patriks Gustavs Rinkevičs

# DEV
## Steps for developement  
1. Lietotājam jāievada savs Spotify api key+secret ja ieiet pirmo reizi  
2. Wrapper funkcijas:  
2.1. Iegūst dziesmu, kas pašreiz skan.  
2.2. Iegūt playlisti, kas pašreiz skan  
2.3. Iegūst, vai šobrīd skan shuffle  
2.4. Iegūst pēdējās N dziesmas
2.5. determines if skiped

# To set up
## Steps for app use
1. reģistrējies developer.spotify 
2. atver pie 'Dashboard' app "tas ka mes vinu nosaucam' 
3. atrodi savu ID, secret, redirect URI 
4. Izveido savu .env failu kurā definē šādi:
4.1. SPOTIPY_CLIENT_ID = ' ' 
4.2. SPOTIPY_CLIENT_SECRET = ' ' 
4.3. SPOTIPY_REDIRECT_URI = 'http://...' 
