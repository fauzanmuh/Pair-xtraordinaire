// Fungsi untuk membalik teks
function reverseText(text) {
    return text.split('').reverse().join('');
}

// Fungsi untuk membalik urutan kata
function reverseWords(text) {
    return text.split(' ').reverse().join(' ');
}

// Fungsi untuk menghasilkan teks terbalik dan kata terbalik
function generateAntiMainstreamText(text) {
    const mirroredText = reverseText(text);
    const reversedWords = reverseWords(mirroredText);
    return reversedWords;
}

// Contoh penggunaan
const inputText = "Ini adalah contoh teks anti mainstream!";
const result = generateAntiMainstreamText(inputText);

console.log(result); // Output: "!niamrets imatna sket tolpmoc halas ini"