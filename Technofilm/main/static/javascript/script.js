document.getElementById('switchButton').addEventListener('click', function() {
    // Скрываем текущий проект
document.getElementById('project1').style.display = 'none';
    // Показываем другой проект
document.getElementById('project2').style.display = 'block';
  });

const items = [
    { id: 1, name: 'Побег из Шоушенка', category: 'Film'},
    { id: 2, name: 'Зеленая миля', category: 'Film' },
    { id: 3, name: 'Форрест Гамп', category: 'Film' },
    { id: 4, name: 'Список Шиндлера', category: 'Film' },
    { id: 5, name: '1+1', category: 'Film' },
    { id: 6, name: 'Начало', category: 'Film' },
    { id: 7, name: 'Леон', category: 'Film' },
    { id: 8, name: 'Король Лев', category: 'Film' },
    { id: 9, name: 'Бойцовский клуб', category: 'Film' },
    { id: 10, name: 'Иван Васильевич меняет профессию', category: 'Film' },
    { id: 11, name: 'Жизнь прекраснa', category: 'Film' },
    { id: 12, name: 'Достучаться до небес', category: 'Film' },
    { id: 13, name: 'Крестный отец', category: 'Film' },
    { id: 14, name: 'Криминальное чтиво', category: 'Film' },
    { id: 15, name: 'Операция «Ы» и другие приключения Шурика', category: 'Film' },
    { id: 16, name: 'Престиж', category: 'Film' },
];


const searchInput = document.getElementById('searchInput');
const searchButton = document.getElementById('searchButton');
searchButton.style.backgroundColor = '#FFD700';
searchButton.style.color = '#3E2723';
searchButton.style.borderColor = '#3E2723'
;
const resultsContainer = document.getElementById('resultsContainer');

searchButton.addEventListener('click', function() {

const searchTerm = searchInput.value.trim(); 
const results = searchByName(items, searchTerm);

resultsContainer.innerHTML = '';

results.forEach(item => {
  const itemDiv = document.createElement('div');
  itemDiv.classList.add('item');

  const img = document.createElement('img');
  
   
  

  const name = document.createElement('p');
  name.textContent = item.name;

  itemDiv.appendChild(img);
  itemDiv.appendChild(name);

  resultsContainer.appendChild(itemDiv);
});
});

function searchByName(items, searchTerm) {
const term = searchTerm.toLowerCase();
return items.filter(item => item.name.toLowerCase().includes(term));
}
