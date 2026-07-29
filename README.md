<div align="center">

# 📚 WeebCentral Downloader — Personal Edition

**A fork of [Yui007/weebcentral_downloader](https://github.com/Yui007/weebcentral_downloader), reworked with a redesigned interface and quality-of-life features for everyday personal use**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![PyQt6](https://img.shields.io/badge/PyQt6-GUI-41CD52?style=for-the-badge&logo=qt&logoColor=white)](https://pypi.org/project/PyQt6/)
[![License](https://img.shields.io/badge/License-MIT-00D4AA?style=for-the-badge)](LICENSE)
[![Fork of](https://img.shields.io/badge/Fork%20of-Yui007%2Fweebcentral__downloader-6e5494?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Yui007/weebcentral_downloader)

</div>

---

## 🍴 About This Fork

This project started as a fork of [WeebCentral Downloader](https://github.com/Yui007/weebcentral_downloader) by [Yui007](https://github.com/Yui007). All credit for the original scraping engine, chapter/download pipeline, and the initial GUI concept goes to the upstream project — that core is unchanged here.

What this fork focuses on instead:

- **A redesigned interface** — the sidebar navigation was replaced with a centered, pill-shaped bottom navigation bar, and the whole app now runs on a warmer, custom design system (colors, typography, spacing) instead of the original Neon Noir look.
- **A more personalized workflow** — features aimed at everyday, single-user usage rather than general distribution: a Library tab for browsing what you've already downloaded, missing-chapter detection, and batch conversion.

If you're looking for the original, more broadly-maintained project (or its browser extension), head to [Yui007/weebcentral_downloader](https://github.com/Yui007/weebcentral_downloader).

---

<div align="center">

## ✨ Features

</div>

<table align="center">
<tr>
<td width="50%">

### 🎨 Redesigned GUI
- Centered, pill-shaped bottom navigation
- Warm, custom color palette and typography
- Animated buttons/inputs with glow effects
- **Per-chapter progress bars** with live image counts (e.g., 12/55)

</td>
<td width="50%">

### ⚡ Performance
- **Parallel chapter downloads** (1-8 concurrent)
- **Parallel image downloads** (1-10 per chapter)
- Automatic rate-limit handling with retry/backoff
- Checkpoint system for resume

</td>
</tr>
<tr>
<td width="50%">

### 📖 Chapter Selection
- Download a single chapter: `5` or `23.5`
- Download a range: `1-50` or `5.5-15.5`
- Quick range input: `1,5,10-20`
- Select all with one click

</td>
<td width="50%">

### 📦 Library & Export
- **Library tab** to browse everything you've downloaded
- Detect and fetch **missing chapters** for a series
- Batch-convert to **PDF**, **EPUB**, or **CBZ**
- Auto-delete images after conversion

</td>
</tr>
</table>

---

## ☁️ Google Colab

Run directly in your browser — no installation needed!

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RafiMota/WeebLoader/blob/main/colab/WeebCentral_Downloader.ipynb)

1. Click the badge above to open the notebook
2. Run **Cell 1** to install dependencies and clone the repository
3. Run **Cell 2** — paste your manga URL, select chapters & format
4. Optionally run **Cell 3** to zip and download to your PC

**Output formats:** `pdf`, `cbz` (with ComicInfo.xml for Kavita/Komga), `images`, or `all`

---

## 🚀 Quick Start

### Requirements

- Python 3.8+
- [FlareSolverr](https://github.com/FlareSolverr/FlareSolverr) (**Optional** — only needed if the site enables Cloudflare protection)

### Setup

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/RafiMota/WeebLoader.git
    cd WeebLoader
    ```

2.  **Install FlareSolverr (Optional)**

    > **Note:** FlareSolverr is **not required** for normal use. The downloader connects directly to the site. FlareSolverr is only used as an automatic fallback if Cloudflare protection is detected (e.g., 403/503 challenge pages). You can skip this step entirely unless you encounter Cloudflare blocks.

    *   Download the latest release from [FlareSolverr Releases](https://github.com/FlareSolverr/FlareSolverr/releases).
    *   Extract and run the executable (`flaresolverr.exe` on Windows).
    *   Ensure it is running on the default port `8191`.

3.  **Install Python Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Downloader**
    *   **GUI Mode:**
        ```bash
        python run_gui.py
        ```
    *   **CLI Mode:**
        ```bash
        python weebcentral_scraper.py
        ```

---

## 🎮 GUI Overview

| Tab | Description |
|-----|-------------|
| 🔗 **Enter URL** | Paste a manga URL, view recent history, fetch manga info |
| 📖 **Manga Info** | View cover, metadata, tags, and select chapters to download |
| ⬇️ **Downloads** | Real-time, per-chapter progress bars with image counts |
| 📚 **Library** | Browse downloaded manga, track missing chapters, and batch convert |
| ⚙️ **Settings** | Configure threads, delay, output folder, conversion options |

### Settings Available

| Setting | Range | Description |
|---------|-------|-------------|
| Concurrent Chapters | 1-8 | How many chapters download in parallel |
| Concurrent Images | 1-10 | Images per chapter downloaded simultaneously |
| Request Delay | 0.5-5.0s | Delay between requests |
| Convert to PDF | ✓/✗ | Auto-convert chapters to PDF |
| Convert to EPUB | ✓/✗ | Auto-convert chapters to EPUB |
| Convert to CBZ | ✓/✗ | Auto-convert chapters to CBZ |
| Delete After | ✓/✗ | Remove images after conversion |

---

## 📁 Project Structure

```
WeebLoader/
├── run_gui.py                       # GUI entry point
├── weebcentral_scraper.py           # CLI & core scraper
├── flaresolverr_client.py           # Optional Cloudflare bypass client
├── update_library_metadata.py       # Library metadata maintenance script
├── gui/
│   ├── __init__.py                  # App initialization
│   ├── main_window.py               # Main window & bottom nav wiring
│   ├── theme.py                     # Design system (colors, fonts, QSS)
│   ├── config.py                    # JSON settings manager
│   ├── animations.py                # Glow & fade effects
│   ├── components/                  # Reusable widgets
│   │   ├── animated_button.py
│   │   ├── animated_input.py
│   │   ├── bottom_nav.py            # Centered pill navigation bar
│   │   ├── chapter_list.py
│   │   ├── conversion_progress_dialog.py
│   │   ├── download_card.py
│   │   └── manga_info_card.py
│   ├── tabs/                        # Tab views
│   │   ├── url_input_tab.py
│   │   ├── manga_info_tab.py
│   │   ├── downloads_tab.py
│   │   ├── library_tab.py
│   │   └── settings_tab.py
│   └── workers/                     # Background threads
│       ├── scraper_worker.py
│       ├── download_worker.py
│       └── conversion_worker.py
├── colab/                           # Google Colab notebook & helpers
└── downloads/                       # Default output folder
```

---

## 📋 Requirements

```
Python >= 3.8
requests
beautifulsoup4
tqdm
PyQt6
fpdf2
Pillow
ebooklib
```

---

## 🤝 Contributing

This is a personal fork focused on my own workflow, but feedback and pull requests are welcome:

- 🐛 Report bugs
- 💡 Suggest UI or personalization features
- 🔧 Submit pull requests

If you're after a feature more suited to the original project's broader scope, consider contributing upstream at [Yui007/weebcentral_downloader](https://github.com/Yui007/weebcentral_downloader) instead.

### ✨ Credits

- **[Yui007](https://github.com/Yui007)** — creator of the original WeebCentral Downloader this fork is based on.
- **[TheHappyAkita](https://github.com/TheHappyAkita)** — upstream contribution with PR #15 (Library Tab, improved rate limiting, and core stability), carried into this fork.

---

## ⚠️ Disclaimer

This tool is for **educational purposes only**. Please respect the terms of service of the websites you interact with.

---

<div align="center">

**Fork maintained by [RafiMota](https://github.com/RafiMota)** · based on **[WeebCentral Downloader](https://github.com/Yui007/weebcentral_downloader)** by [Yui007](https://github.com/Yui007)

</div>
