document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('form');
    const addLaborItemButton = document.getElementById('add-labor-item');
    const addPartItemButton = document.getElementById('add-part-item');
    const calculateEstimateButton = document.getElementById('calculate-estimate');
    const modal = document.getElementById('myModal');
    const span = document.getElementsByClassName("close")[0];

    let laborItemCount = 0;
    let partItemCount = 0;

    function isValidNumber(value) {
        return value !== null && value !== '' && !isNaN(value) && parseFloat(value) >= 0;
    }

    function isValidLaborItem(item) {
        const task = item.querySelector('.labor-task').value.trim();
        const hours = item.querySelector('.labor-hours').value.trim();
        const rate = item.querySelector('.labor-rate').value.trim();

        return task !== '' && isValidNumber(hours) && isValidNumber(rate);
    }

    function isValidPartItem(item) {
        const description = item.querySelector('.part-description').value.trim();
        const quantity = item.querySelector('.part-quantity').value.trim();
        const unitPrice = item.querySelector('.part-unit-price').value.trim();

        return description !== '' && isValidNumber(quantity) && isValidNumber(unitPrice);
    }

    function areAllLaborItemsValid() {
        const laborItems = document.querySelectorAll('.labor-item');
        return Array.from(laborItems).every(isValidLaborItem);
    }

    function areAllPartItemsValid() {
        const partItems = document.querySelectorAll('.part-item');
        return Array.from(partItems).every(isValidPartItem);
    }

    addLaborItemButton.addEventListener('click', function() {
        if (areAllLaborItemsValid()) {
            laborItemCount++;
            const newLaborItem = document.createElement('div');
            newLaborItem.className = 'labor-item';
            newLaborItem.innerHTML = `
                <p>
                    <label for="labor-task-${laborItemCount}">Task</label>
                    <input type="text" id="labor-task-${laborItemCount}" class="labor-task">
                </p>
                <p>
                    <label for="labor-hours-${laborItemCount}">Hours</label>
                    <input type="number" id="labor-hours-${laborItemCount}" class="labor-hours">
                </p>
                <p>
                    <label for="labor-rate-${laborItemCount}">Rate</label>
                    <input type="number" id="labor-rate-${laborItemCount}" class="labor-rate">
                </p>
                <button type="button" class="delete-item button">Delete</button>
            `;
            document.getElementById('labor-items').appendChild(newLaborItem);
        } else {
            document.getElementById("are-you-sure").classList.remove("hidden");
        }
    });

    addPartItemButton.addEventListener('click', function() {
        if (areAllPartItemsValid()) {
            partItemCount++;
            const newPartItem = document.createElement('div');
            newPartItem.className = 'part-item';
            newPartItem.innerHTML = `
                <p>
                    <label for="part-description-${partItemCount}">Description</label>
                    <input type="text" id="part-description-${partItemCount}" class="part-description">
                </p>
                <p>
                    <label for="part-quantity-${partItemCount}">Quantity</label>
                    <input type="number" id="part-quantity-${partItemCount}" class="part-quantity">
                </p>
                <p>
                    <label for="part-unit-price-${partItemCount}">Unit Price</label>
                    <input type="number" id="part-unit-price-${partItemCount}" class="part-unit-price">
                </p>
                <button type="button" class="delete-item button">Delete</button>
            `;
            document.getElementById('part-items').appendChild(newPartItem);
        } else {
            document.getElementById("are-you-sure").classList.remove("hidden");
        }
    });

    document.addEventListener('click', function(event) {
        if (event.target.classList.contains('delete-item')) {
            event.target.parentElement.remove();
        }
    });

    calculateEstimateButton.addEventListener('click', function() {
        if (areAllLaborItemsValid() && areAllPartItemsValid()) {
            const laborItems = document.querySelectorAll('.labor-item');
            const partItems = document.querySelectorAll('.part-item');

            let totalLaborCost = 0;
            let totalPartsCost = 0;

            laborItems.forEach(function(item) {
                const hours = parseFloat(item.querySelector('.labor-hours').value);
                const rate = parseFloat(item.querySelector('.labor-rate').value);
                totalLaborCost += hours * rate;
            });

            partItems.forEach(function(item) {
                const quantity = parseInt(item.querySelector('.part-quantity').value);
                const unitPrice = parseFloat(item.querySelector('.part-unit-price').value);
                totalPartsCost += quantity * unitPrice;
            });

            const totalEstimate = totalLaborCost + totalPartsCost;

            const customerName = document.getElementById('customer-name').value;
            const vehicle = document.getElementById('vehicle').value;
            const diagnosis = document.getElementById('diagnosis').value;

            document.getElementById('customer-name-output').textContent = customerName;
            document.getElementById('vehicle-output').textContent = vehicle;
            document.getElementById('diagnosis-output').textContent = diagnosis;
            document.getElementById('labor-cost').textContent = totalLaborCost.toFixed(2);
            document.getElementById('parts-cost').textContent = totalPartsCost.toFixed(2);
            document.getElementById('total-estimate').textContent = totalEstimate.toFixed(2);

            modal.style.display = "block"; // Show the modal
        } else {
            document.getElementById("are-you-sure").classList.remove("hidden");
        }
    });

    span.onclick = function() {
        modal.style.display = "none"; 
    }

    window.onclick = function(event) {
        if (event.target === modal) {
            modal.style.display = "none"; 
        }
    }
});

window.onload = () => {
    document.getElementById("close-ays").onclick = () => {
        document.getElementById("are-you-sure").classList.add("hidden");
    };

    document.getElementById("ays-ok").onclick = () => {
        document.getElementById("are-you-sure").classList.add("hidden");
    };
};