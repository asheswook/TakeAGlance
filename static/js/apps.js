document.addEventListener("DOMContentLoaded", function () {
  var loadingMessage = document.getElementById("loading-message");
  var statusMessage = document.getElementById("status-message");
  var frame = document.getElementById("frame");
  var image = new Image();
  image.src = "/video_feed";
  image.id = "video-stream";
  image.style.width = "80%";
  image.addEventListener("load", function () {
    frame.innerHTML = "";
    frame.appendChild(image);
    loadingMessage.style.display = "none";
    statusMessage.style.display = "block";
  });
});

function stopVideoStreaming() {
  var video = document.getElementById("video-stream"); // video 태그의 id를 적절히 수정해야 합니다.
  video.src = ""; // 비디오 소스를 비워서 스트리밍 중지
}

// 페이지 이동 시 비디오 스트리밍 중지
window.onbeforeunload = function () {
  stopVideoStreaming();
};
