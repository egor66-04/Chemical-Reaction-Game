let selectedElements = [];

// Функция выбора элемента
function selectElement(symbol, name) {
    // Если элемент уже выбран, убираем его
    if (selectedElements.includes(symbol)) {
        selectedElements = selectedElements.filter(el => el !== symbol);
    } else {
        // Добавляем элемент, если выбрано меньше двух
        if (selectedElements.length < 2) {
            selectedElements.push(symbol);
        }
    }

    // Обновляем текст с выбранными элементами
    document.getElementById('selected-elements').textContent = selectedElements.join(' и ');

    // Активируем кнопку, если выбрано два элемента
    document.getElementById('mixButton').disabled = selectedElements.length !== 2;
}

// Функция смешивания элементов
function mixElements() {
    let resultText = '';

    if (selectedElements.includes('H') && selectedElements.includes('O')) {
        resultText = 'Вы получили Воду (H2O)';
    } else if (selectedElements.includes('Na') && selectedElements.includes('Cl')) {
        resultText = 'Вы получили Соль (NaCl)';
    } else {
        resultText = 'Реакция не удалась';
    }

    document.getElementById('result').textContent = resultText;

    // Сброс выбора
    selectedElements = [];
    document.getElementById('selected-elements').textContent = 'Пока не выбрано';
    document.getElementById('mixButton').disabled = true;
}
