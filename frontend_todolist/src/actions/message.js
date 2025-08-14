// invalid → dispara quando o campo obrigatório está vazio ou inválido e mostra sua mensagem personalizada.
// mensagem → dispara quando o usuário digita algo e limpa a mensagem personalizada para não ficar presa.

document.addEventListener("DOMContentLoaded", function () {
    const mensagem = document.getElementById("tasktitle");

    mensagem.addEventListener("invalid", function () {
        this.setCustomValidity("Preencha o título da tarefa.");
    });

    mensagem.addEventListener("mensagem", function () {
        this.setCustomValidity(""); // limpa mensagem personalizada
    });
});
