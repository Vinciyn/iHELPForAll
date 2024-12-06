import subprocess
import os
import time
import json

B = '\033[35m'
R = '\033[31m'
N = '\033[0m'
A = '\033[34m'
BB = '\033[36m'

banner = f"""

{B}
................. ...................................................................... ...........
... ...... ............ ........ .........{BB}@@@@@@@@@@@@@@@@@@@{B}... ..... ..................  . .... ..
 ...... ...... .. ...................{BB}@@@@@@{B}................,{BB}@@@@@@{B}......... ... ..... ... ... ..... 
  ...  .. ..... . ....... ........{BB}@@@@{B} ..........{BB}@@@@@{B}..........,{BB}@@@@{B}.....  .. .... ............ ...
 ......... ..  .... ... .......{BB}@@@@{B}../((. .... .{BB}@@@@@@*{B}.......(//...{BB}@@@@{B}. .......... ... ..... .... 
      .  . ... ... .. ... ...{BB}@@@@{B} . .{BB}@@@{B}   .......{BB}/&{B}  ... . ..{BB}@@@{B} ....{BB}@@@@{B} ..     .  ... ..  .. ....
.   ..    . ..    . ..     ,{BB}@@@{B}  .. .{BB}@@@{B} .. . ... ... .       {BB}@@@{B}  . . .{BB}@@@{B}. ..  .  .  .....  .. .  
 ..         .   .       ..{BB}@@@{B}      ..{BB}@@@{B}  ..  {BB}@@({B}   . {BB}@@@{B}  ...{BB}@@@{B} . . .  {BB}&@@*{B}.  ..     .    .. .    
          .  .     . .. .{BB}@@@{B}     .  .{BB}@@@{B}      {BB}@@({B}    .{BB}@@@{B}     {BB}@@@{B}       . {BB}(@@{B}.  .      .  .         
                         {BB}@@#{B}         {BB}@@@{B}      {BB}@@({B}    .{BB}@@@{B}     {BB}@@@{B}          {BB}@@@{B}                     .
      .                       .               {BB}@@#{B}     {BB}@@@{B}                .                      .   
                        .. ..... ... ........ {BB}@@#{B}     {BB}@@@{B}. ..  ..  ...........      .           .   
                        {BB}@@@@@@@@@@@@@@@@@@@@@@@@({B}     {BB}@@@@@@@@@@@@@@@@@@@@@@@@{B}.                     
                                                                                                    
                         {BB}(((((((#(((((#({B}      {BB}##/{B}     {BB}(#({B}     {BB}(#(((#(((##((((({B}                      
                         {BB}/(({B}         {BB}/(({B}      {BB}((*{B}     {BB}((({B}     {BB}(/({B}         {BB}//({B}                      
                          {BB}.//*{B}       {BB}///{B}      {BB}//*{B}     {BB}///{B}     {BB}///{B}        {BB}///{B}                        
                            {BB}///{B}      {BB}***{B}      {BB}//,{B}     {BB}***{B}     {BB}***{B}       {BB}*//{B}                         
                              {BB}***{B}    {BB}*,,{B}      {BB}**,{B}     {BB}***{B}     {BB}**,{B}     {BB}***{B}                           
                                {BB}****{B}          {BB},,.{B}     {BB},,,{B}          {BB},,**{B}                             
                                   {BB},,,,.{B}                       {BB},,,,,{B}                                
                                      {BB}.,,,,,,,{B}           {BB},,,,,,,{B}                                    
                                             {BB}.,,,,,..,.,,.{B}                                          
                                                                                                                                                                           
                                                                                                   

"""




    # Charger les informations depuis le fichier JSON
file_path = 'config.json'

with open(file_path, 'r') as f:
    ids = json.load(f)

    # Récupération des informations
client_id = ids["client_id"]
client_secret = ids["client_secret"]
redirect_uri = ids["redirect_uri"]

def iTransferAll():
    import os
    import json
    import spotipy
    from spotipy.oauth2 import SpotifyOAuth
    import time

    import sys
    url = "https://linktr.ee/help.records/"
    text = f"{A}H.E.L.P Records"
    def create_clickable_link(url, text):
        # Cette séquence fonctionne dans des terminaux compatibles
        sys.stdout.write(f'                        \033]8;;{url}\033\\{text}\033]8;;\033\\')


    print(f"                        {BB}iTransferAll")
    create_clickable_link(text=text, url=url)
    print(f"{B}@2024\n                        {N}@Ver.2.0 | Patch PlaylistError\n                        {R}Coded by VinciYN\n")

    time.sleep(2)

    input(f"{B}[{BB}+{B}] {A}Veuillez ouvrir votre navigateur et vous connecter au compte spotify source. Appuyez sur Entrée une fois connecté.")


    # Scopes requis pour accéder à toutes les données nécessaires
    scope = ("user-library-read user-library-modify playlist-read-private "
            "playlist-modify-private playlist-modify-public user-follow-read user-follow-modify")

    # Nom des fichiers de cache
    source_cache = ".cache-source"
    dest_cache = ".cache-dest"
    temp_data_file = "spotify_transfer_data.json"

    # Supprimer les fichiers de cache existants
    if os.path.exists(source_cache):
        os.remove(source_cache)
    if os.path.exists(dest_cache):
        os.remove(dest_cache)

    def save_data_to_file(data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_data_from_file(filename):
        with open(filename, 'r') as f:
            return json.load(f)

    try:
        # Authentification pour le compte source
        sp_oauth_source = SpotifyOAuth(client_id=client_id,
                                    client_secret=client_secret,
                                    redirect_uri=redirect_uri,
                                    scope=scope,
                                    cache_path=source_cache)
        sp_source = spotipy.Spotify(auth_manager=sp_oauth_source)
        source_user_id = sp_source.current_user()['id']
        print(f"{B}[{BB}+{B}] {A}Authentification du compte source réussie!")

        # Collecte des données du compte source
        data = {
            "playlists": [],
            "liked_tracks": [],
            "liked_albums": [],
            "followed_artists": []
        }

        try:
            playlists_data = sp_source.current_user_playlists()
            
            # Vérification que des playlists sont retournées
            if playlists_data and 'items' in playlists_data:
                playlists = playlists_data['items']
                print(f"Nombre total de playlists trouvées : {len(playlists)}")

                valid_playlists = []  # Liste pour les playlists valides

                for playlist in playlists:
                    try:
                        # Vérification que toutes les clés nécessaires existent et ne sont pas None
                        if (playlist is not None 
                            and 'name' in playlist 
                            and 'id' in playlist 
                            and 'tracks' in playlist 
                            and playlist['tracks'] is not None
                            and 'total' in playlist['tracks']
                            and playlist['tracks']['total'] > 0):

                            # Ajouter la playlist valide
                            valid_playlists.append(playlist)
                            print(f"Playlist valide : {playlist['name']} (ID : {playlist['id']}, Total : {playlist['tracks']['total']} morceaux)")
                        else:
                            print(f"Playlist invalide ou incomplète : {playlist}")
                    except Exception as inner_e:
                        print(f"Erreur dans le traitement d'une playlist : {inner_e}")

                print(f"Nombre de playlists valides : {len(valid_playlists)}")
                
                # Récupérer les playlists et leurs morceaux
                for playlist in valid_playlists:
                    try:
                        playlist_data = {
                            "name": playlist['name'],
                            "tracks": []
                        }
                        
                        # Récupérer les morceaux de la playlist
                        playlist_tracks_data = sp_source.playlist_tracks(playlist['id'])
                        
                        # Vérification que les morceaux sont présents
                        if 'items' in playlist_tracks_data:
                            for track in playlist_tracks_data['items']:
                                # Vérification que chaque morceau contient l'URI
                                if 'track' in track and 'uri' in track['track']:
                                    playlist_data['tracks'].append(track['track']['uri'])
                                else:
                                    print(f"Track invalide ou sans URI : {track}")
                        else:
                            print(f"Aucun morceau trouvé pour la playlist : {playlist['name']}")
                        
                        # Ajouter la playlist avec ses morceaux à la structure de données
                        data['playlists'].append(playlist_data)
                    
                    except Exception as playlist_e:
                        print(f"Erreur lors de la récupération des morceaux pour la playlist {playlist['name']} : {playlist_e}")
            else:
                print("Aucune playlist trouvée ou données de playlist incorrectes.")
            
        except Exception as e:
            print(f"Erreur lors de la récupération des playlists : {e}")


        # Récupérer les morceaux likés
        liked_tracks = sp_source.current_user_saved_tracks()
        while liked_tracks:
            data['liked_tracks'].extend([item['track']['uri'] for item in liked_tracks['items']])
            liked_tracks = sp_source.next(liked_tracks) if liked_tracks['next'] else None

        # Récupérer les albums likés
        liked_albums = sp_source.current_user_saved_albums()
        while liked_albums:
            data['liked_albums'].extend([item['album']['uri'] for item in liked_albums['items']])
            liked_albums = sp_source.next(liked_albums) if liked_albums['next'] else None

        # Récupérer les artistes suivis
        liked_artists = sp_source.current_user_followed_artists()
        while liked_artists:
            data['followed_artists'].extend([artist['id'] for artist in liked_artists['artists']['items']])
            liked_artists = sp_source.next(liked_artists['artists']) if liked_artists['artists']['next'] else None

        # Sauvegarde des données dans un fichier temporaire
        save_data_to_file(data, temp_data_file)
        print(f"{B}[{BB}+{B}] {A}Données du compte source sauvegardées temporairement.")

        input(f"{B}[{BB}+{B}] {A}Déconnectez-vous du compte source. Appuyez sur Entrée une fois déconnecté.")

        # Supprimer le cache du compte source pour forcer une nouvelle authentification
        os.remove(source_cache)

        # Authentification pour le compte destination
        print(f"{B}[{BB}+{B}] {N}Veuillez maintenant vous connecter au compte destination.")
        sp_oauth_dest = SpotifyOAuth(client_id=client_id,
                                    client_secret=client_secret,
                                    redirect_uri=redirect_uri,
                                    scope=scope,
                                    cache_path=dest_cache)
        sp_dest = spotipy.Spotify(auth_manager=sp_oauth_dest)
        dest_user_id = sp_dest.current_user()['id']
        print(f"{B}[{BB}+{B}] {A}Authentification du compte destination réussie!")

        # Chargement des données depuis le fichier temporaire
        data = load_data_from_file(temp_data_file)

        # Description à ajouter à chaque playlist
        playlist_description = ("Transféré avec iTransferAll, développé par VincíYN"
                                "Rendez-vous sur https://linktr.ee/help.records pour transférer plus de musique !")

        import time

        # Fonction pour diviser une liste en morceaux de taille n
        def chunk_list(lst, n):
            for i in range(0, len(lst), n):
                yield lst[i:i + n]

        # Transférer les playlists
        for playlist in data['playlists']:
            playlist_name = playlist['name']
            track_uris = playlist['tracks']

            # Vérifier si la playlist existe déjà sur le compte destination
            existing_playlists = sp_dest.current_user_playlists()
            playlist_exists = any(pl['name'] == playlist_name for pl in existing_playlists['items'])

            if not playlist_exists:
                new_playlist = sp_dest.user_playlist_create(user=dest_user_id, name=playlist_name,
                                                            description=playlist_description)
                if track_uris:
                    # Diviser les URIs des morceaux en morceaux de 100
                    for chunk in chunk_list(track_uris, 100):
                        sp_dest.playlist_add_items(new_playlist['id'], chunk)
                        print(f"{B}[{BB}+{B}] {A}Ajout de {len(chunk)} morceaux à la playlist '{playlist_name}'.")
                        time.sleep(5)  # Attendre 5 secondes après chaque groupe de 100 morceaux
                    print(f"{B}[{BB}+{B}] {A}Playlist '{playlist_name}' transférée avec succès!")
                else:
                    print(f"{B}[{BB}-{B}] {R}Playlist '{playlist_name}' est vide, aucun morceau transféré.")
            else:
                print(f"{B}[{BB}-{B}] {B}Playlist '{playlist_name}' existe déjà sur le compte destination, elle ne sera pas dupliquée.")

        # Transférer les morceaux likés
        if data['liked_tracks']:
            for chunk in chunk_list(data['liked_tracks'], 50):
                sp_dest.current_user_saved_tracks_add(chunk)
                print(f"{B}[{BB}+{B}] {A}Ajout de {len(chunk)} morceaux likés.")
                time.sleep(5)  # Attendre 5 secondes après chaque groupe de 100 morceaux
            print(f"{B}[{BB}+{B}] {A}{len(data['liked_tracks'])} morceaux likés transférés avec succès!")

        # Transférer les albums likés
        if data['liked_albums']:
            for chunk in chunk_list(data['liked_albums'], 50):
                sp_dest.current_user_saved_albums_add(chunk)
                print(f"{B}[{BB}+{B}] {A}Ajout de {len(chunk)} albums likés.")
                time.sleep(5)  # Attendre 5 secondes après chaque groupe de 100 albums
            print(f"{B}[{BB}+{B}] {A}{len(data['liked_albums'])} albums likés transférés avec succès!")

        # Transférer les artistes suivis
        if data['followed_artists']:
            for chunk in chunk_list(data['followed_artists'], 50):
                sp_dest.user_follow_artists(chunk)
                print(f"{B}[{BB}+{B}] {A}Suivi de {len(chunk)} artistes.")
                time.sleep(5)  # Attendre 5 secondes après chaque groupe de 100 artistes
            print(f"{B}[{BB}+{B}] {A}{len(data['followed_artists'])} artistes suivis transférés avec succès!")


        # Supprimer le fichier temporaire après le transfert
        os.remove(temp_data_file)
        print("Transfert terminé! Les données temporaires ont été supprimées.")

    except spotipy.exceptions.SpotifyException as e:
        print(f"{B}[{BB}-{B}] {R}Erreur d'authentification : {e}")
        print(f"{B}[{BB}-{B}] {R}Veuillez vérifier vos identifiants et réessayer.")


def iRegroupAll():
    import os
    import json
    import spotipy
    from spotipy.oauth2 import SpotifyOAuth
    import time



    import sys
    url = "https://linktr.ee/help.records/"
    text = f"{A}H.E.L.P Records"
    def create_clickable_link(url, text):
        # Cette séquence fonctionne dans des terminaux compatibles
        sys.stdout.write(f'                        \033]8;;{url}\033\\{text}\033]8;;\033\\')


    print(f"                        {BB}iRegroupAllPlaylists")
    create_clickable_link(text=text, url=url)
    print(f"{B}@2024\n                        {N}@Ver.1.0\n                        {R}Coded by VinciYN\n")

    time.sleep(2)

    input(f"{B}[{BB}+{B}] {A}Veuillez ouvrir votre navigateur et vous connecter au compte spotify. Appuyez sur Entrée une fois connecté.")


    # Scopes requis
    scope = "playlist-read-private playlist-modify-private playlist-modify-public"

    # Authentification Spotify
    sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)
    sp = spotipy.Spotify(auth_manager=sp_oauth)
    user_id = sp.current_user()['id']

    def list_playlists(sp):
        playlists = sp.current_user_playlists()
        if not playlists or 'items' not in playlists:
            print("[!] Aucune playlist trouvée sur votre compte.")
            return []

        for idx, playlist in enumerate(playlists['items']):
            if playlist and 'name' in playlist:
                print(f"{B}{idx + 1} : {playlist['name']}{N}")
            else:
                print(f"Erreur : playlist {idx + 1} est vide ou mal formatée.")

        return playlists['items']


    def select_playlists(playlist_data):
        selected_ids = []
        print(f"\n{B}(?) Sélectionnez l'ordre des playlists pour regrouper leurs morceaux :{N}")
        for idx in range(len(playlist_data)):
            choice = input(f"{B}(?) Quelle playlist mettre en position {idx + 1} ? > {N}")
            if choice.strip() == "":
                break
            try:
                selected_ids.append(playlist_data[int(choice) - 1]['id'])
            except (ValueError, IndexError):
                print(f"{R}[!] Choix invalide, réessayez.{N}")
                continue
        return selected_ids

    def create_combined_playlist(sp, user_id, playlist_ids, new_playlist_name):
        all_tracks = []
        for playlist_id in playlist_ids:
            tracks = sp.playlist_tracks(playlist_id)['items']
            all_tracks.extend([track['track']['uri'] for track in tracks if track['track']])
        # Créer la nouvelle playlist
        new_playlist = sp.user_playlist_create(user=user_id, name=new_playlist_name, public=False)
        # Ajouter les morceaux par groupes de 100
        for i in range(0, len(all_tracks), 100):
            sp.playlist_add_items(new_playlist['id'], all_tracks[i:i + 100])
        print(f"{B}[{BB}+{B}] {A}Votre playlist '{new_playlist_name}' a été créée avec succès ! Profitez de votre écoute !{N}")

    try:
        # Lister les playlists
        playlist_data = list_playlists(sp)
        if not playlist_data:
            print(f"{R}[!] Aucune playlist trouvée sur votre compte.{N}")
            exit()

        # Sélectionner les playlists
        selected_playlist_ids = select_playlists(playlist_data)
        if not selected_playlist_ids:
            print(f"{R}[!] Aucune playlist sélectionnée. Fin du programme.{N}")
            exit()

        # Demander le nom de la nouvelle playlist
        new_playlist_name = input(f"{B}(?) Quel titre voulez-vous donner à la nouvelle playlist regroupée ? > {N}")
        if not new_playlist_name.strip():
            print(f"{R}[!] Le titre de la playlist ne peut pas être vide.{N}")
            exit()

        # Créer la nouvelle playlist regroupée
        create_combined_playlist(sp, user_id, selected_playlist_ids, new_playlist_name)

    except spotipy.exceptions.SpotifyException as e:
        print(f"{R}[!] Une erreur est survenue : {e}{N}")


def iBackupAll():
    import spotipy
    from spotipy.oauth2 import SpotifyOAuth
    import json
    import time


    SCOPE = "playlist-read-private user-library-read user-follow-read user-library-modify playlist-modify-public playlist-modify-private"

    def authenticate():
        """Authentifie l'utilisateur Spotify."""
        return spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=SCOPE
        ))

    def backup_data(sp_source, backup_file):
        """Sauvegarde les données Spotify dans un fichier."""
        print(f"{B}[{BB}+{B}] {A}Sauvegarde des données Spotify en cours...")

        data = {
            "playlists": [],
            "liked_tracks": [],
            "liked_albums": [],
            "followed_artists": []
        }

        # Sauvegarde des playlists
        playlists = sp_source.current_user_playlists()['items']
        for playlist in playlists:
            if playlist is None:
                continue
            playlist_data = {
                "name": playlist.get('name', 'Playlist Sans Nom'),
                "tracks": [track['track']['uri'] for track in sp_source.playlist_tracks(playlist['id'])['items']]
            }
            data["playlists"].append(playlist_data)

        # Sauvegarde des morceaux likés
        liked_tracks = sp_source.current_user_saved_tracks()
        while liked_tracks:
            data['liked_tracks'].extend([item['track']['uri'] for item in liked_tracks['items']])
            liked_tracks = sp_source.next(liked_tracks) if liked_tracks['next'] else None

        # Sauvegarde des albums likés
        liked_albums = sp_source.current_user_saved_albums()
        while liked_albums:
            data['liked_albums'].extend([item['album']['uri'] for item in liked_albums['items']])
            liked_albums = sp_source.next(liked_albums) if liked_albums['next'] else None

        # Sauvegarde des artistes suivis
        followed_artists = sp_source.current_user_followed_artists()['artists']['items']
        data['followed_artists'].extend([artist['id'] for artist in followed_artists])

        # Sauvegarder dans un fichier
        with open(backup_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        print(f"{B}[{BB}+{B}] {A}Données sauvegardées dans {backup_file}.{R}")

    def restore_data(sp_target, backup_file):
        """Restaure les données Spotify depuis un fichier."""
        print(f"{B}[{BB}+{B}] {A}Restauration des données Spotify...")

        with open(backup_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Restaure les playlists
        for playlist in data['playlists']:
            new_playlist = sp_target.user_playlist_create(sp_target.me()['id'], playlist['name'])
            sp_target.playlist_add_items(new_playlist['id'], playlist['tracks'])

        # Restaure les morceaux likés
        for track_uri in data['liked_tracks']:
            sp_target.current_user_saved_tracks_add([track_uri])

        # Restaure les albums likés
        for album_uri in data['liked_albums']:
            sp_target.current_user_saved_albums_add([album_uri])

        # Restaure les artistes suivis
        for artist_id in data['followed_artists']:
            sp_target.user_follow_artists([artist_id])

        print(f"{B}[{BB}+{B}] {A}Restauration terminée avec succès.{R}")

    def main_menu():
        """Affiche le menu principal et gère les interactions utilisateur."""

        import sys
        url = "https://linktr.ee/help.records/"
        text = f"{A}H.E.L.P Records"
        def create_clickable_link(url, text):
            # Cette séquence fonctionne dans des terminaux compatibles
            sys.stdout.write(f'                        \033]8;;{url}\033\\{text}\033]8;;\033\\')


        print(f"                        {BB}iBackupAll")
        create_clickable_link(text=text, url=url)
        print(f"{B}@2024\n                        {N}@Ver.1.0\n                        {R}Coded by VinciYN\n")

        time.sleep(2)

        input(f"{B}[{BB}+{B}] {A}Veuillez ouvrir votre navigateur et vous connecter au compte spotify. Appuyez sur Entrée une fois connecté.")


        print(f"{B}[{BB}1{B}] {A}Sauvegarder mes données Spotify")
        print(f"{B}[{BB}2{B}] {A}Restaurer mes données Spotify")
        print(f"{B}[{BB}3{B}] {A}Quitter")
        print()

        choice = input(f"{B}[{BB}?{B}] {A}Sélectionnez une option (1-3) : {R}")
        return choice

    def main():
        """Point d'entrée principal du programme."""

        sp = authenticate()
        backup_file = "spotify_backup.json"

        while True:
            choice = main_menu()

            if choice == "1":
                backup_data(sp, backup_file)
            elif choice == "2":
                restore_data(sp, backup_file)
            elif choice == "3":
                print(f"{B}[{BB}+{B}] {A}Merci d'avoir utilisé iHELPForAll. À bientôt !{R}")
                break
            else:
                print(f"{B}[{BB}!{B}] {A}Choix invalide. Veuillez réessayer.{R}")

    if __name__ == "__main__":
        main()

def main_menu():
    import sys
    url = "https://linktr.ee/help.records/"
    text = f"{A}H.E.L.P Records"
    def create_clickable_link(url, text):
        # Cette séquence fonctionne dans des terminaux compatibles
        sys.stdout.write(f'                        \033]8;;{url}\033\\{text}\033]8;;\033\\')


    print(banner)
    print(f"                        {BB}iHELPForAll")
    create_clickable_link(text=text, url=url)
    print(f"{B}@2024\n                        {N}@Ver.1.0 | Multitool\n                        {R}Coded by VinciYN\n")

    time.sleep(2)

    """Affiche le menu principal et retourne le choix de l'utilisateur."""
    print(f"{B}[{BB}+{B}] {A}Choisissez un software !")
    print(f"{B}[{BB}1{B}] {A}Lancer iTransferAll.py")
    print(f"{B}[{BB}2{B}] {A}Lancer iRegroupAll.py")
    print(f"{B}[{BB}3{B}] {A}Lancer iBackupAll.py")
    print("4. Quitter")
    print()

    choice = input(f"{B}[{BB}?{B}] {A}Sélectionnez une option (1-4) : {R}")
    return choice

def execute_program(program_name):
    """Exécute un fichier Python en tant que sous-processus."""
    try:
        print(f"{B}[{BB}+{B}] {A}Lancement de {program_name}...{R}")
        subprocess.run(["python", program_name], check=True)
    except FileNotFoundError:
        print(f"{B}[{BB}!{B}] {A}Erreur : {program_name} introuvable. Assurez-vous qu'il est dans le même dossier.{R}")
    except subprocess.CalledProcessError as e:
        print(f"{B}[{BB}!{B}] {A}Erreur lors de l'exécution de {program_name} : {e}{R}")

def main():
    """Point d'entrée principal du programme."""
    while True:
        choice = main_menu()

        if choice == "1":
            iTransferAll()
        elif choice == "2":
            iRegroupAll()
        elif choice == "3":
            iBackupAll()
        elif choice == "4":
            print(f"{B}[{BB}+{B}] {A}Merci d'avoir utilisé iHELPForAll. À bientôt !{R}")
            break
        else:
            print(f"{B}[{BB}!{B}] {A}Choix invalide. Veuillez réessayer.{R}")

if __name__ == "__main__":
    main()
