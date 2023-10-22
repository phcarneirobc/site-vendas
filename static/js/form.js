document.addEventListener("DOMContentLoaded", function () {
    const cpfInput = document.getElementById("cpf");

    cpfInput.addEventListener("input", function () {
        const value = this.value.replace(/\D/g, ''); // Remove non-digit characters
        this.value = value; // Update the input value

        if (value.length === 9) {
            this.classList.remove("invalid");
            this.classList.add("valid");
        } else {
            this.classList.remove("valid");
            this.classList.add("invalid");
        }
    });

    document.getElementById("myForm").addEventListener("submit", function (event) {
        event.preventDefault();
        // Add your JavaScript code here to handle form submission
    });
});