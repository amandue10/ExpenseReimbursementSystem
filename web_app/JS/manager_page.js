function logout(){
    sessionStorage.clear();
    window.location.href = "login.html";
}


const pendingTable = document.getElementById("pendingRRTable");
const pendingTableBody = document.getElementById("pendingRRTableBody");
const completedTable = document.getElementById("completedRRTable");
const completedTableBody = document.getElementById("completedRRTableBody");

async function getPendingEmployeeData(){
    let url = "http://127.0.0.1:5000/pending_requests";

    let response = await fetch(url);
    
    if (response.status === 200){
        let body = await response.json();
        populateData(body);
    } else {
        alert("There was a problem trying to get pending employee information: sorry!");
    }
}

async function getCompletedEmployeeData(){
    let url = "http://127.0.0.1:5000/completed_requests";

    let response = await fetch(url);
    
    if (response.status === 200){
        let body = await response.json();
        populateDataComp(body);
    } else {
        alert("There was a problem trying to get completed employee information: sorry!");
    }
}



function populateData(responseBody){
    for (let reimbursement_request of responseBody){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${reimbursement_request.employeeId}</td><td>${reimbursement_request.managerId}</td><td>${reimbursement_request.requestAmount}</td><td>${reimbursement_request.requestComment}</td><td>${reimbursement_request.requestComment2}</td><td>${reimbursement_request.requestStatus}<td>${reimbursement_request.rrDate}</td>`;
        pendingTableBody.appendChild(tableRow);
    }
}


function populateDataComp(responseBody){
    for (let reimbursement_request of responseBody){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${reimbursement_request.employeeId}</td><td>${reimbursement_request.managerId}</td><td>${reimbursement_request.requestAmount}</td><td>${reimbursement_request.requestComment}</td><td>${reimbursement_request.requestComment2}</td><td>${reimbursement_request.requestStatus}<td>${reimbursement_request.rrDate}</td>`;
        completedTableBody.appendChild(tableRow);
    }
}

getCompletedEmployeeData()
getPendingEmployeeData()