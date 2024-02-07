document.getElementById('send-btn').addEventListener('click', function() {
    var userInput = document.getElementById('user-input').value;
    var chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += 'You: ' + userInput + '<br>';
    document.getElementById('user-input').value = '';
});
