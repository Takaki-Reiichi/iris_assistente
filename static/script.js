function enviarMensagem() {  
    const mensagem = document.getElementById("mensagem").value;  
    const chatBox = document.getElementById("chat-box");  

    // Mostra sua mensagem  
    chatBox.innerHTML += `<p><strong>Você:</strong> ${mensagem}</p>`;  

    // Envia pro servidor  
    fetch("/chat", {  
        method: "POST",  
        headers: { "Content-Type": "application/x-www-form-urlencoded" },  
        body: `mensagem=${encodeURIComponent(mensagem)}`  
    })  
    .then(response => response.json())  
    .then(data => {  
        // Mostra a resposta + toca o áudio  
        chatBox.innerHTML += `<p><strong>Íris:</strong> ${data.resposta}</p>`;  
        const audio = new Audio(data.audio);  
        audio.play();  
    });  
}  
