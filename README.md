# 🎵 Spotify Billboard Playlist Creator

A **Python script** that scrapes Billboard Hot 100 songs for a given date and automatically creates a **private Spotify playlist** using [Spotipy](https://spotipy.readthedocs.io/).  

---

## 🚀 Features
- Fetches Billboard Hot 100 songs for a user-specified date  
- Searches and adds songs to Spotify automatically  
- Creates a **private playlist** in your Spotify account  
- Skips songs that are not found on Spotify  

---

## 🧩 Tech Stack / Requirements
- **Python 3.x**  
- **Spotipy** library (`pip install spotipy`)  
- **Requests** and **BeautifulSoup4** for web scraping  
- **python-dotenv** to manage API credentials  
- Spotify account with **Client ID**, **Client Secret**, and **Redirect URI**  

---

## ⚙️ Setup

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/spotify-billboard.git
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Create a .env file with your Spotify API credentials:
```bash
CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
USERNAME=your_spotify_username
```
4. Make sure **token.txt** exists or will be created automatically for OAuth caching.

---

## ▶️ Usage

- Run the script with:
```bash
python main.py
```
- Enter a date in YYYY-MM-DD format when prompted.
- The script will fetch Billboard Top 100 songs for that date and create a private Spotify playlist automatically.

---

## 📝 Notes

- .env file contains your sensitive Spotify API keys; do not share publicly.

- Some songs may not exist on Spotify and will be skipped automatically.

- Make sure your Spotify app’s Redirect URI matches the one in the script (http://127.0.0.1:8888/callback).
