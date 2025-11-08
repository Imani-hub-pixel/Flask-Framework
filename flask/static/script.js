const apiUrl = 'http://127.0.0.1:5000/items';

async function fetchItems() {
    const res = await fetch(apiUrl);
    const items = await res.json();
    const list = document.getElementById('itemList');
    list.innerHTML = '';
    items.forEach(item => {
        const li = document.createElement('li');
        li.textContent = `${item.id}: ${item.name} - ${item.description} `;
        
        // Update button
        const updateBtn = document.createElement('button');
        updateBtn.textContent = 'Update';
        updateBtn.onclick = () => updateItem(item.id);
        li.appendChild(updateBtn);
        
        // Delete button
        const deleteBtn = document.createElement('button');
        deleteBtn.textContent = 'Delete';
        deleteBtn.onclick = () => deleteItem(item.id);
        li.appendChild(deleteBtn);

        list.appendChild(li);
    });
}

async function createItem() {
    const name = document.getElementById('name').value;
    const description = document.getElementById('description').value;

    const res = await fetch(apiUrl, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({name, description})
    });

    document.getElementById('name').value = '';
    document.getElementById('description').value = '';
    fetchItems();
}

async function updateItem(id) {
    const name = prompt("Enter new name:");
    const description = prompt("Enter new description:");
    if (!name && !description) return;

    await fetch(`${apiUrl}/${id}`, {
        method: 'PUT',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({name, description})
    });

    fetchItems();
}

async function deleteItem(id) {
    await fetch(`${apiUrl}/${id}`, { method: 'DELETE' });
    fetchItems();
}

// Load items on page load
fetchItems();
