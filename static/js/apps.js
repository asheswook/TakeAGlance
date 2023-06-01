document.addEventListener("DOMContentLoaded", function () {
  var loadingMessage = document.getElementById("loading-message");
  var statusMessage = document.getElementById("status-message");
  var frame = document.getElementById("frame");
  var image = new Image();
  image.src = "/video_feed";
  image.id = "video-stream";
  image.addEventListener("load", function () {
    frame.innerHTML = "";
    frame.appendChild(image);
    loadingMessage.style.display = "none";
    statusMessage.style.display = "block";
  });
});
