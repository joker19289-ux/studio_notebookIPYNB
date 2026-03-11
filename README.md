# Studio-NoteBookIPYNB

A Jupyter notebook viewer and manager for browsing and exploring `.ipynb` files directly in your browser.

## 📁 Project Structure

```
Studio-NoteBookIPYNB/
├── notebooks/          # Place your .ipynb files here
├── datasets/          # Data files for notebooks
├── scripts/           # Utility scripts
├── outputs/           # Generated outputs (figures, reports)
├── static/            # CSS, JavaScript, images
├── templates/         # HTML templates
├── config/            # Configuration files
├── app.py             # Flask application
├── requirements.txt   # Python dependencies
└── README.md          # This file
```

## 🚀 Getting Started

1. **Upload Notebooks**: Place your Jupyter `.ipynb` files in the `notebooks/` folder
2. **Run the Server**: The application starts automatically
3. **View Notebooks**: Open the app in your browser and select a notebook to view

## ✨ Features

- Browse and view Jupyter notebooks in the browser
- Clean, responsive UI with gradient design
- Support for markdown and code cells
- Fast notebook loading and rendering
- Configuration management via `config/settings.json`

## 📋 Requirements

- Python 3.8+
- Flask 3.0.0
- nbconvert 7.16.0
- nbformat 5.10.0

## 🔧 Configuration

Edit `config/settings.json` to customize:
- Application name
- Notebooks directory
- Output directories
- Server port

## 📝 Changelog

### v1.0.0 (March 2026)

✨ **New**
- Notebook folder structure
- Support for .ipynb file uploads
- Browser-based notebook viewer interface
- Automatic project initialization

⚡ **Improvements**
- Fast .ipynb loading
- Improved UI for notebook lists
- File sorting support

🐛 **Fixes**
- Fixed notebook opening errors
- Fixed markdown cell display
- Fixed large file loading

## 💡 Tips

- Organize notebooks in subfolders within `notebooks/`
- Store data files in the `datasets/` folder
- Use `outputs/` for saving generated figures and reports
- Customize styling in `static/style.css`
