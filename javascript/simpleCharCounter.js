document.addEventListener("DOMContentLoaded", function() {
    const input = document.getElementById("textInput");
    const countDisplay = document.getElementById("charCount");

    input.addEventListener("input", function() {
        countDisplay.textContent = `Jumlah Karakter: ${input.value.length}`;
    });
});