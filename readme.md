# Bandcamp Fan Overlap Finder 

A Python tool that helps DJs and music enthusiasts discover new music by analyzing shared fan bases across different Bandcamp tracks and albums. The tool identifies users who have purchased multiple tracks from your selection, helping you find curators with similar music taste.

## Core Features
🔍 Fan Base Analysis: Compare supporter lists between multiple Bandcamp tracks/albums  
👥 Overlap Detection: Find users who have purchased multiple tracks from your selection  
🔗 Profile Discovery: Get direct links to music collectors' public profiles  
⚡ Batch Processing: Analyze multiple tracks simultaneously  
📊 Simple Interface: Easy-to-use command line tool (with planned Streamlit UI)

## How It Works
- Input two to 5 Bandcamp track/album URLs
- The tool scrapes the "supported by" sections
- Identifies fans who appear across multiple tracks
- Returns a list of overlapping fans with their profile links

## Use Cases
- DJs looking to discover new music through dedicated collectors
- Labels researching active music buyers in their genre
- Artists finding potential fans based on similar music purchases

## Potentially Coming Later
- Web interface using Streamlit
- Export functionality for results
- Search history and saving features

## Installation

1. Clone the repository:

``
git clone https://github.com/yourusername/bandcamp-fan-finder.git
cd bandcamp-fan-finder ``

2. Create and activate a virtual environment:

`` 
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
``

3. Install required packages:

``
pip install -r requirements.txt
``

## Usage
1. Make sure your virtual environment is activated
2. Run the script:
`` 
python src/main.py 
``
3. Enter Bandcamp URLs when prompted (minimum 2, maximum 5)
- URLs should be album or track pages (e.g., artist.bandcamp.com/album/album-name or artist bandcamp.com/track/track-name)
- Type 'done' when you've entered all URLs you want to compare
- Press Ctrl+C at any time to exit

Example URLs:
https://artist.bandcamp.com/album/album-name
https://another-artist.bandcamp.com/track/track-name

*The script will:*

- Validate your URLs
- Fetch fan information from each URL
- Compare fan lists to find overlapping supporters
- Display results with links to fan profiles

### Example Output
Overlapping Fans Found:
==================================================

Fan: username1
Profile: https://bandcamp.com/username1
Found in 3 tracks:
  • Album One
  • Album Two
  • Album Three
----------------------------------------

Fan: username2
Profile: https://bandcamp.com/username2
Found in 2 tracks:
  • Album One
  • Album Two
----------------------------------------

### Requirements
- Python 3.8 or higher
- Internet connection
- Required packages (installed via requirements.txt):
    - requests
    - beautifulsoup4

### Troubleshooting
- If you get a 403 error, wait a few minutes before trying again
- Make sure URLs are valid Bandcamp album or track pages
- Check your internet connection if requests fail
- Ensure your Python version is compatible

### Licence
MIT


**Note**
This tool respects Bandcamp's terms of service and only accesses publicly available information. Please use responsibly and in accordance with Bandcamp's rate limiting guidelines.