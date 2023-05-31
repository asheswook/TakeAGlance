document.addEventListener('DOMContentLoaded', function() {
    var loadingMessage = document.getElementById('loading-message');
    var videoStream = document.getElementById('video-stream');
    var statusMessage = document.getElementById('status-message');

    videoStream.addEventListener('load', function() {
        loadingMessage.style.display = 'none';
        
        statusMessage.style.display = 'block';
    });
    
});
