document.addEventListener("DOMContentLoaded", function () {
    function applyMask(input, maskFunction) {
        if (input) {
            input.addEventListener('input', function () {
                input.value = maskFunction(input.value);
            });
        }
    }

    function cpfMask(value) {
        return value
            .replace(/\D/g, '') // Remove todos os caracteres não numéricos
            .replace(/(\d{3})(\d)/, '$1.$2') // Adiciona um ponto após os primeiros 3 dígitos
            .replace(/(\d{3})(\d)/, '$1.$2') // Adiciona um ponto após os segundos 3 dígitos
            .replace(/(\d{3})(\d{1,2})$/, '$1-$2'); // Adiciona um traço antes dos últimos 2 dígitos
    }

    function phoneMask(value) {
        return value
            .replace(/\D/g, '') // Remove todos os caracteres não numéricos
            .replace(/(\d{2})(\d)/, '($1) $2') // Adiciona parênteses ao redor do código de área
            .replace(/(\d{4})(\d)/, '$1-$2') // Adiciona um traço após os primeiros 4 dígitos
            .replace(/(\d{4})(\d{1,2})$/, '$1$2'); // Mantém os últimos 4 ou 5 dígitos
    }

    const cpfInput = document.getElementById('cpf');
    const phoneInput = document.getElementById('telefone');

    applyMask(cpfInput, cpfMask);
    applyMask(phoneInput, phoneMask);
});