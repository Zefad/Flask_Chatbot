const chatContainer = document.getElementById('chatContainer');
const chatForm = document.getElementById('chatForm');

chatForm.addEventListener('submit', function(e) {
  if (chatContainer.classList.contains('inactive')) {
    e.preventDefault();
    chatContainer.classList.remove('inactive');
    chatContainer.classList.add('active');
    setTimeout(function() {
      chatForm.submit();
    }, 600);
  }});
document.addEventListener("DOMContentLoaded", function(){
  var chatWindow = document.querySelector('.chat-window');
  if (chatWindow) {
    chatWindow.scrollTop = chatWindow.scrollHeight;
  }
});
window.onbeforeunload = function() {
  navigator.sendBeacon("/clear");
};
