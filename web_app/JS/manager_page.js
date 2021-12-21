function logout(){
    sessionStorage.clear();
    window.location.href = "login.html";
}



async function getPendingEmployeeData(){
    let url = "http://127.0.0.1:5000/pending_requests";

    let response = await fetch(url + result);
    
    if (response.status === 200){
        let body = await response.json();
        populateData(body);
    } else {
        alert("There was a problem trying to get pending employee information: sorry!");
    }
}

async function getCompletedEmployeeData(){
    let url = "http://127.0.0.1:5000/completed_requests";

    let response = await fetch(url + result);
    
    if (response.status === 200){
        let body = await response.json();
        populateData(body);
    } else {
        alert("There was a problem trying to get completed employee information: sorry!");
    }
}



function populateData(responseBody){
    
    

    for (let reimbursement_request of responseBody){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${reimbursement_request.employeeId}</td><td>${reimbursement_request.managerId}</td><td>${reimbursement_request.requestAmount}</td><td>${reimbursement_request.requestComment}</td><td>${reimbursement_request.requestComment2}</td><td>${reimbursement_request.requestStatus}<td>${reimbursement_request.rrDate}</td>`;
        employeeTableBody.appendChild(tableRow);
    }
}

getCompletedEmployeeData()
getPendingEmployeeData()