window.onload = () => {
    const showDetails = document.getElementById("showDetails");
    document.getElementById("show").onclick = () => {
        showDetails.classList.remove("hidden");
        showPricing();
    };

    document.getElementById("close-x").onclick = () => {
        showDetails.classList.add("hidden");
    };
};

const showPricing = () => {
    const details = document.getElementById("details");
    details.innerHTML = ""

    const diagTitle = document.createElement("h3");
    diagTitle.innerHTML = "Diagnosis"
    details.append(diagTitle);

    const diagnosis = document.createElement("p");
    diagnosis.innerHTML = form.elements["diagnosis"].value;
    details.append(diagnosis);

    const hoursTitle = document.createElement("h3");
    hoursTitle.innerHTML = "Estimated Working Hours"
    details.append(hoursTitle);

    const hours = document.createElement("p");
    hours.innerHTML = form.elements["time"].value;
    details.append(hours);

    const costTitle = document.createElement("h3");
    costTitle.innerHTML = "Estimated Cost"
    details.append(costTitle);

    const cost = document.createElement("p");
    cost.innerHTML = form.elements["cost"].value;
    details.append(cost);
};