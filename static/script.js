document.addEventListener('DOMContentLoaded', function() {
    const notebooksList = document.getElementById('notebooks-list');
    const notebookViewer = document.getElementById('notebook-viewer');
    const backBtn = document.getElementById('back-btn');
    const notebookContent = document.getElementById('notebook-content');

    // Load and display notebooks
    fetch('/api/notebooks')
        .then(response => response.json())
        .then(data => {
            if (data.notebooks.length === 0) {
                notebooksList.innerHTML = '<p class="loading">No notebooks found. Upload .ipynb files to the notebooks/ folder.</p>';
                return;
            }
            
            notebooksList.innerHTML = '';
            data.notebooks.forEach(notebook => {
                const card = document.createElement('div');
                card.className = 'notebook-card';
                card.innerHTML = `
                    <div class="notebook-card-title">${escapeHtml(notebook.name)}</div>
                    <div class="notebook-card-meta">Click to view</div>
                `;
                card.addEventListener('click', () => loadNotebook(notebook.name));
                notebooksList.appendChild(card);
            });
        })
        .catch(error => {
            console.error('Error loading notebooks:', error);
            notebooksList.innerHTML = '<p class="loading">Error loading notebooks</p>';
        });

    function loadNotebook(filename) {
        fetch(`/api/notebook/${filename}`)
            .then(response => response.json())
            .then(notebook => {
                displayNotebook(notebook, filename);
                document.getElementById('notebooks-list').parentElement.classList.add('hidden');
                notebookViewer.classList.add('active');
            })
            .catch(error => {
                console.error('Error loading notebook:', error);
                notebookContent.innerHTML = '<p>Error loading notebook</p>';
            });
    }

    function displayNotebook(notebook, filename) {
        notebookContent.innerHTML = `<h3>${escapeHtml(filename)}</h3>`;
        
        if (notebook.cells) {
            notebook.cells.forEach((cell, index) => {
                const cellDiv = document.createElement('div');
                cellDiv.className = `cell cell-${cell.cell_type}`;
                
                if (cell.cell_type === 'markdown') {
                    cellDiv.innerHTML = `<div class="cell-content markdown">${escapeHtml(cell.source.join(''))}</div>`;
                } else if (cell.cell_type === 'code') {
                    const source = cell.source.join('');
                    cellDiv.innerHTML = `<pre class="code-cell"><code>${escapeHtml(source)}</code></pre>`;
                    
                    if (cell.outputs && cell.outputs.length > 0) {
                        const outputDiv = document.createElement('div');
                        outputDiv.className = 'cell-output';
                        cell.outputs.forEach(output => {
                            if (output.text) {
                                outputDiv.innerHTML += `<pre>${escapeHtml(output.text.join(''))}</pre>`;
                            } else if (output.data && output.data['text/plain']) {
                                outputDiv.innerHTML += `<pre>${escapeHtml(output.data['text/plain'].join(''))}</pre>`;
                            }
                        });
                        cellDiv.appendChild(outputDiv);
                    }
                }
                
                notebookContent.appendChild(cellDiv);
            });
        }
    }

    backBtn.addEventListener('click', () => {
        document.getElementById('notebooks-list').parentElement.classList.remove('hidden');
        notebookViewer.classList.remove('active');
        notebookContent.innerHTML = '';
    });

    function escapeHtml(text) {
        const map = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#039;'
        };
        return text.replace(/[&<>"']/g, m => map[m]);
    }
});
