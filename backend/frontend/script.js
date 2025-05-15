document.addEventListener("DOMContentLoaded", () => {
  const chatForm = document.getElementById("chat-form");
  const userInput = document.getElementById("user-input");
  const chatBox = document.getElementById("chat-box");

  chatForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const pergunta = userInput.value.trim();
    if (!pergunta) return;

    appendMessage("Você", pergunta);
    userInput.value = "";

    try {
      const response = await fetch("/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ pergunta })  // ATENÇÃO AQUI: deve ser exatamente { pergunta: "..." }
      });

      const data = await response.json();

      if (response.ok) {
        appendMessage("FURIA Bot", data.resposta);
      } else {
        appendMessage("FURIA Bot", "Erro: " + data.detail);
      }
    } catch (error) {
      appendMessage("FURIA Bot", "Erro de conexão");
      console.error("Erro na requisição:", error);
    }
  });

  function appendMessage(sender, text) {
    const message = document.createElement("div");
    message.classList.add("message");
    message.innerHTML = `<strong>${sender}:</strong> ${text}`;
    chatBox.appendChild(message);
    chatBox.scrollTop = chatBox.scrollHeight;
  }
});
