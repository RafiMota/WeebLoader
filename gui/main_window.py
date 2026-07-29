"""
Main Window for WeebCentral Downloader.
Tabbed interface with a centered bottom navigation bar.
"""

from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QStackedWidget, QMessageBox
)

from gui.theme import Colors, Spacing
from gui.config import get_settings, save_settings
from gui.components.bottom_nav import BottomNavBar
from gui.tabs import UrlInputTab, MangaInfoTab, DownloadsTab, SettingsTab, LibraryTab
from gui.workers import ScraperWorker, DownloadWorker, ConversionWorker
from gui.components.download_card import DownloadStatus
from flaresolverr_client import is_flaresolverr_running


class MainWindow(QMainWindow):
    """
    Main application window with tabbed navigation.
    Features a centered bottom pill navigation bar and page transitions.
    """
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self._scraper_worker = None
        self._download_worker = None
        self._conversion_worker = None
        self._current_manga_url = ""
        self._cover_data = None
        
        self._setup_window()
        self._setup_ui()
        self._connect_signals()
        

    
    def _setup_window(self):
        """Configure window properties."""
        self.setWindowTitle("WeebCentral Downloader")
        self.setMinimumSize(1000, 700)
        
        # Restore window geometry from settings
        settings = get_settings()
        if settings.window_width > 0 and settings.window_height > 0:
            self.resize(settings.window_width, settings.window_height)
        
        if settings.window_x >= 0 and settings.window_y >= 0:
            self.move(settings.window_x, settings.window_y)
        
        # Always start maximized
        self.showMaximized()
    
    def _setup_ui(self):
        """Initialize UI components."""
        # Central widget
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # ─────────────────────────────────────────────────────────────
        # Content Area (Stacked Pages)
        # ─────────────────────────────────────────────────────────────
        self._stack = QStackedWidget()
        self._stack.setStyleSheet(f"""
            QStackedWidget {{
                background-color: {Colors.BG_DARKEST};
            }}
        """)

        # Create tabs
        self._url_tab = UrlInputTab()
        self._info_tab = MangaInfoTab()
        self._downloads_tab = DownloadsTab()
        self._library_tab = LibraryTab()
        self._settings_tab = SettingsTab()

        self._stack.addWidget(self._url_tab)
        self._stack.addWidget(self._info_tab)
        self._stack.addWidget(self._downloads_tab)
        self._stack.addWidget(self._library_tab)
        self._stack.addWidget(self._settings_tab)

        main_layout.addWidget(self._stack, 1)

        # ─────────────────────────────────────────────────────────────
        # Bottom Navigation Bar (centered pill)
        # ─────────────────────────────────────────────────────────────
        nav_container = QWidget()
        nav_layout = QHBoxLayout(nav_container)
        nav_layout.setContentsMargins(Spacing.XL, 0, Spacing.XL, Spacing.XL)
        nav_layout.addStretch()

        self._nav_bar = BottomNavBar(
            ["Enter URL", "Manga Info", "Downloads", "Library", "Settings"]
        )
        nav_layout.addWidget(self._nav_bar)

        nav_layout.addStretch()
        main_layout.addWidget(nav_container)
    
    def _connect_signals(self):
        """Connect all signals and slots."""
        # Navigation
        self._nav_bar.tabChanged.connect(self._on_nav_clicked)
        
        # URL Tab
        self._url_tab.fetchRequested.connect(self._on_fetch_requested)
        
        # Manga Info Tab
        self._info_tab.downloadRequested.connect(self._on_download_requested)
        
        # Downloads Tab
        self._downloads_tab.cancelDownload.connect(self._on_cancel_download)
        self._downloads_tab.retryChapter.connect(self._on_retry_chapter)
        self._downloads_tab.retryAllFailed.connect(self._on_retry_all_failed)
        
        # Library Tab
        self._library_tab.downloadMissingChapters.connect(self._on_download_missing_chapters)
        self._library_tab.convertToPDF.connect(self._on_convert_to_pdf)
        self._library_tab.convertToEPUB.connect(self._on_convert_to_epub)
        self._library_tab.convertToCBZ.connect(self._on_convert_to_cbz)
        
        # Settings Tab
        self._settings_tab.settingsChanged.connect(self._on_settings_changed)
    
    def _on_nav_clicked(self, index: int):
        """Handle navigation button click."""
        self._stack.setCurrentIndex(index)
    
    def _switch_to_tab(self, index: int):
        """Switch to a specific tab programmatically."""
        self._stack.setCurrentIndex(index)
        self._nav_bar.set_current(index)

        # Refresh library when switching to it
        if index == 3:  # Library tab
            self._library_tab.refresh()
    
    # ═════════════════════════════════════════════════════════════════
    # Fetch Manga Info
    # ═════════════════════════════════════════════════════════════════
    
    def _on_fetch_requested(self, url: str):
        """Handle manga URL fetch request."""
        self._current_manga_url = url
        self._cover_data = None
        
        # Create and start scraper worker
        self._scraper_worker = ScraperWorker()
        self._scraper_worker.set_url(url)
        
        self._scraper_worker.progress.connect(self._on_scraper_progress)
        self._scraper_worker.manga_info_ready.connect(self._on_manga_info_ready)
        self._scraper_worker.chapters_ready.connect(self._on_chapters_ready)
        self._scraper_worker.cover_ready.connect(self._on_cover_ready)
        self._scraper_worker.error.connect(self._on_scraper_error)
        self._scraper_worker.finished_signal.connect(self._on_scraper_finished)
        
        self._scraper_worker.start()
    
    def _on_scraper_progress(self, message: str):
        """Handle scraper progress updates."""
        # Could update a status bar here
        pass
    
    def _on_manga_info_ready(self, info: dict):
        """Handle manga info received."""
        self._manga_info = info
    
    def _on_chapters_ready(self, chapters: list):
        """Handle chapters list received."""
        self._chapters = chapters
    
    def _on_cover_ready(self, data: bytes):
        """Handle cover image data received."""
        self._cover_data = data
    
    def _on_scraper_error(self, message: str):
        """Handle scraper error."""
        self._url_tab.show_error(message)
    
    def _on_scraper_finished(self, success: bool):
        """Handle scraper completion."""
        if success and hasattr(self, '_manga_info'):
            # Update manga info tab
            self._info_tab.set_manga_info(
                url=self._current_manga_url,
                title=self._manga_info.get("title", "Unknown"),
                cover_url=self._manga_info.get("cover_url"),
                cover_data=self._cover_data,
                description=self._manga_info.get("description", ""),
                metadata=self._manga_info.get("metadata", {}),
                tags=self._manga_info.get("tags", []),
                chapters=getattr(self, '_chapters', [])
            )
            
            self._url_tab.show_success("Manga info loaded!")
            
            # Switch to info tab
            self._switch_to_tab(1)
        
        self._url_tab.set_loading(False)
        self._scraper_worker = None
    
    # ═════════════════════════════════════════════════════════════════
    # Download Chapters
    # ═════════════════════════════════════════════════════════════════
    
    def _on_download_requested(self, chapters: list):
        """Handle download request from manga info tab."""
        if self._download_worker and self._download_worker.is_running:
            QMessageBox.warning(
                self, 
                "Download in Progress",
                "Please wait for the current download to finish."
            )
            return
        
        # Convert ChapterItem objects to dicts
        chapter_dicts = [
            {"name": ch.name, "url": ch.url}
            for ch in chapters
        ]
        
        # Add download cards
        for ch in chapters:
            self._downloads_tab.add_download(ch.name)
        
        # Switch to downloads tab
        self._switch_to_tab(2)
        
        # Start download worker
        self._download_worker = DownloadWorker()
        self._download_worker.set_download_params(
            manga_url=self._current_manga_url,
            chapters=chapter_dicts,
            manga_title=self._manga_info.get("title", "Unknown"),
            manga_info=self._manga_info,
            cover_data=self._cover_data
        )
        
        # Connect with QueuedConnection for cross-thread safety (ThreadPoolExecutor -> main thread)
        self._download_worker.chapter_started.connect(self._on_chapter_started)
        self._download_worker.chapter_progress.connect(self._on_chapter_progress)
        self._download_worker.chapter_finished.connect(self._on_chapter_finished)
        self._download_worker.error.connect(self._on_download_error)
        self._download_worker.finished_signal.connect(self._on_download_finished)
        
        self._download_worker.start()
    
    def _on_chapter_started(self, chapter_name: str):
        """Handle chapter download started."""
        self._downloads_tab.set_status(chapter_name, DownloadStatus.DOWNLOADING)
    
    def _on_chapter_progress(self, chapter_name: str, progress: int, current: int, total: int):
        """Handle chapter download progress."""
        self._downloads_tab.update_progress(chapter_name, progress, current, total)
    
    def _on_chapter_finished(self, chapter_name: str, success: bool):
        """Handle chapter download finished."""
        if success:
            self._downloads_tab.mark_completed(chapter_name)
        else:
            self._downloads_tab.mark_error(chapter_name)
    
    def _on_download_error(self, chapter_name: str, message: str):
        """Handle download error."""
        if chapter_name:
            self._downloads_tab.mark_error(chapter_name)
    
    def _on_download_finished(self, success: bool):
        """Handle all downloads finished."""
        # Wait for thread to fully finish before clearing reference
        if self._download_worker:
            self._download_worker.wait()
        self._download_worker = None
        
        if success:
            QMessageBox.information(
                self,
                "Download Complete",
                "All chapters have been downloaded successfully!"
            )
    
    def _on_cancel_download(self, chapter_name: str):
        """Handle download cancel request."""
        # For now, we can't cancel individual chapters easily
        # This would require more complex worker management
        pass
    
    def _on_retry_chapter(self, chapter_name: str):
        """Handle retry request for a single failed chapter."""
        if not self._download_worker or not hasattr(self._download_worker, 'scraper'):
            QMessageBox.warning(
                self,
                "Cannot Retry",
                "No active download session. Please start a new download."
            )
            return
        
        # Reset the card to queued state
        self._downloads_tab.set_status(chapter_name, DownloadStatus.QUEUED)
        
        # Retry the chapter using the scraper
        # This would need to be implemented in the download worker
        # For now, show a message
        QMessageBox.information(
            self,
            "Retry",
            f"Retrying {chapter_name}..."
        )
    
    def _on_retry_all_failed(self):
        """Handle retry all failed downloads."""
        if not self._download_worker or not hasattr(self._download_worker, 'scraper'):
            QMessageBox.warning(
                self,
                "Cannot Retry",
                "No active download session. Please start a new download."
            )
            return
        
        QMessageBox.information(
            self,
            "Retry All",
            "Retrying all failed downloads..."
        )
    
    def _on_download_missing_chapters(self, manga_url: str, missing_chapters: list):
        """Handle download missing chapters from library."""
        # Fetch manga info first
        self._on_fetch_requested(manga_url)
    
    def _on_convert_to_pdf(self, manga_path: str):
        """Handle convert to PDF request from library."""
        self._start_conversion(manga_path, 'pdf')
    
    def _on_convert_to_epub(self, manga_path: str):
        """Handle convert to EPUB request from library."""
        self._start_conversion(manga_path, 'epub')
    
    def _on_convert_to_cbz(self, manga_path: str):
        """Handle convert to CBZ request from library."""
        self._start_conversion(manga_path, 'cbz')
    
    def _start_conversion(self, manga_path: str, conversion_type: str):
        """Start conversion process with progress shown in Downloads tab."""
        from pathlib import Path
        import json
        
        manga_path_obj = Path(manga_path)
        if not manga_path_obj.exists():
            QMessageBox.warning(self, "Error", "Manga folder not found!")
            return
        
        # Get all chapter directories with natural sorting
        import re
        
        def natural_sort_key(path):
            """Natural sort key for paths."""
            def atoi(text):
                return int(text) if text.isdigit() else text
            return [atoi(c) for c in re.split(r'(\d+)', str(path.name))]
        
        chapter_dirs = sorted(
            [d for d in manga_path_obj.iterdir() if d.is_dir() and not d.name.startswith('.')],
            key=natural_sort_key
        )
        
        if not chapter_dirs:
            QMessageBox.warning(self, "Error", "No chapters found!")
            return
        
        # Check if conversion already running
        if self._conversion_worker and self._conversion_worker.is_running:
            QMessageBox.warning(
                self,
                "Conversion in Progress",
                "Please wait for the current conversion to finish."
            )
            return
        
        # Get manga title from metadata or folder name
        manga_title = manga_path_obj.name
        metadata_file = manga_path_obj / '.metadata.json'
        if metadata_file.exists():
            try:
                with open(metadata_file, 'r', encoding='utf-8') as f:
                    metadata = json.load(f)
                    manga_title = metadata.get('title', manga_title)
            except:
                pass
        
        # Ask for confirmation
        type_name = conversion_type.upper()
        reply = QMessageBox.question(
            self,
            f"Convert to {type_name}",
            f"Convert {len(chapter_dirs)} chapters to {type_name}?\n\nProgress will be shown in the Downloads tab.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.No:
            return
        
        # Add conversion cards to downloads tab in correct order
        for chapter_dir in chapter_dirs:
            chapter_name = f"{chapter_dir.name} ({type_name})"
            self._downloads_tab.add_download(chapter_name)
        
        # Switch to downloads tab
        self._switch_to_tab(2)
        
        # Start conversion worker
        self._conversion_worker = ConversionWorker()
        self._conversion_worker.set_conversion_params(
            manga_path=str(manga_path_obj),
            manga_title=manga_title,
            conversion_type=conversion_type
        )
        
        # Connect signals
        self._conversion_worker.chapter_started.connect(self._on_conversion_chapter_started)
        self._conversion_worker.chapter_progress.connect(self._on_conversion_chapter_progress)
        self._conversion_worker.chapter_finished.connect(self._on_conversion_chapter_finished)
        self._conversion_worker.error.connect(self._on_conversion_error)
        self._conversion_worker.finished_signal.connect(self._on_conversion_finished)
        
        self._conversion_worker.start()
    
    def _on_conversion_chapter_started(self, chapter_name: str):
        """Handle conversion chapter started."""
        type_suffix = ""
        if self._conversion_worker:
            type_suffix = f" ({self._conversion_worker._conversion_type.upper()})"
        full_name = f"{chapter_name}{type_suffix}"
        self._downloads_tab.set_status(full_name, DownloadStatus.DOWNLOADING)
    
    def _on_conversion_chapter_progress(self, chapter_name: str, progress: int, current: int = 0, total: int = 0):
        """Handle conversion chapter progress."""
        type_suffix = ""
        if self._conversion_worker:
            type_suffix = f" ({self._conversion_worker._conversion_type.upper()})"
        full_name = f"{chapter_name}{type_suffix}"
        self._downloads_tab.update_progress(full_name, progress, current, total)
    
    def _on_conversion_chapter_finished(self, chapter_name: str, success: bool):
        """Handle conversion chapter finished."""
        type_suffix = ""
        if self._conversion_worker:
            type_suffix = f" ({self._conversion_worker._conversion_type.upper()})"
        full_name = f"{chapter_name}{type_suffix}"
        
        if success:
            self._downloads_tab.mark_completed(full_name)
        else:
            self._downloads_tab.mark_error(full_name)
    
    def _on_conversion_error(self, chapter_name: str, message: str):
        """Handle conversion error."""
        if chapter_name:
            type_suffix = ""
            if self._conversion_worker:
                type_suffix = f" ({self._conversion_worker._conversion_type.upper()})"
            full_name = f"{chapter_name}{type_suffix}"
            self._downloads_tab.mark_error(full_name)
    
    def _on_conversion_finished(self, success: bool):
        """Handle all conversions finished."""
        if self._conversion_worker:
            self._conversion_worker.wait()
        self._conversion_worker = None
        
        if success:
            QMessageBox.information(
                self,
                "Conversion Complete",
                "Conversion finished! Check the Downloads tab for details."
            )
    
    def _on_settings_changed(self):
        """Handle settings change."""
        # Settings are auto-saved, nothing special needed here
        pass
    
    # ═════════════════════════════════════════════════════════════════
    # Window Events
    # ═════════════════════════════════════════════════════════════════
    
    def closeEvent(self, event):
        """Handle window close - save geometry."""
        settings = get_settings()
        settings.window_width = self.width()
        settings.window_height = self.height()
        settings.window_x = self.x()
        settings.window_y = self.y()
        save_settings()
        
        # Stop any running workers
        if self._scraper_worker:
            self._scraper_worker.stop()
        if self._download_worker:
            self._download_worker.stop()
        if self._conversion_worker:
            self._conversion_worker.stop()
        
        event.accept()
