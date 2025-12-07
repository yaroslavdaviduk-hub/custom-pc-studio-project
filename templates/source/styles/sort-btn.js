const sortLabel = document.getElementById("sortLabel");
const sortOptions = document.querySelectorAll(".sort-option");

// Значение по умолчанию (можешь менять здесь)
let defaultSort = "popular";

// Установка значения по умолчанию при загрузке страницы
document.addEventListener("DOMContentLoaded", () => {
const defaultOption = document.querySelector(`.sort-option[data-value="${defaultSort}"]`);
if (defaultOption) {
    sortLabel.textContent = defaultOption.textContent;
}
});

// При клике — обновляем label
sortOptions.forEach(option => {
option.addEventListener("click", (e) => {
    sortLabel.textContent = e.target.textContent;

    // Здесь можно делать реальную сортировку:
    // sortProductsBy(e.target.dataset.value);
});
});
