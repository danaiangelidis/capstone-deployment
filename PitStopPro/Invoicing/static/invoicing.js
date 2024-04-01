window.onload = () => {
    document.getElementById("download-button").onclick = () => {
        generatePDF();
    };
};

function generatePDF() {
    const { jsPDF } = window.jspdf;

    let date = document.getElementById('dateIssued').textContent;

    let companyName = document.getElementById('comName').textContent;
    let companyAddress = document.getElementById('comAddress').textContent;

    let customerName = document.getElementById('cusName').textContent;
    let customerAddress = document.getElementById('cusAddress').textContent;
    let customerEmail = document.getElementById('cusEmail').textContent;
    let customerCar = document.getElementById('cusCar').textContent;
    let customerPlate = document.getElementById('cusPlate').textContent;
    let desc1 = document.getElementById('desc1').textContent;
    let price1 = document.getElementById('price1').textContent;
    let qty1 = document.getElementById('qty1').textContent;
    let desc2 = document.getElementById('desc2').textContent;
    let price2 = document.getElementById('price2').textContent;
    let qty2 = document.getElementById('qty2').textContent;
    let desc3 = document.getElementById('desc3').textContent;
    let price3 = document.getElementById('price3').textContent;
    let qty3 = document.getElementById('qty3').textContent;
    let totalLabor = document.getElementById('totalLabor').textContent;
    let totalItems = document.getElementById('totalItems').textContent;
    let subtotal = document.getElementById('subtotal').textContent;

    let pdf = new jsPDF();

    // pdf.text('Date Issued: ' + date, 10, 10);

    pdf.text('From:', 10, 20);
    pdf.text(companyName, 15, 30);
    pdf.text(companyAddress, 15, 40);

    pdf.text('To:', 10, 60);
    pdf.text('Name: ' + customerName, 15, 70);
    pdf.text('Address: ' + customerAddress, 15, 80);
    pdf.text('Email: ' + customerEmail, 15, 90);
    pdf.text('Vehicle Information: ' + customerCar, 15, 100);
    pdf.text('LPN: ' + customerPlate, 15, 110);

    pdf.text('Itemized Costs:', 10, 130);
    pdf.text('Description', 10, 140);
    pdf.text('Price', 100, 140);
    pdf.text('Quantity', 150, 140);

    pdf.text(desc1, 10, 150);
    pdf.text(price1, 100, 150);
    pdf.text(qty1, 150, 150);
    
    pdf.text(desc2, 10, 160);
    pdf.text(price2, 100, 160);
    pdf.text(qty2, 150, 160);

    pdf.text(desc3, 10, 170);
    pdf.text(price3, 100, 170);
    pdf.text(qty3, 150, 170);

    pdf.text('Totals:', 10, 190);
    pdf.text('Total Labor Costs: ' + totalLabor, 20, 200);
    pdf.text('Total Itemized Costs: ' + totalItems, 20, 210);

    pdf.text('Subtotal: ' + subtotal, 10, 230);

    pdf.save('invoice.pdf');
};