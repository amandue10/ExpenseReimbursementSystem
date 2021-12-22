function logout(){
    sessionStorage.clear();
    window.location.href = "login.html";
}


const pendingTable = document.getElementById("pendingRRTable");
const pendingTableBody = document.getElementById("pendingRRTableBody");
const completedTable = document.getElementById("completedRRTable");
const completedTableBody = document.getElementById("completedRRTableBody");


const reimbursementId = document.getElementById("reimbursementIdInput")
const employeeId = document.getElementById("employeeIdInput")
const managerId = document.getElementById("managerIdInput")
const requestAmount = document.getElementById("requestAmountInput")
const employeeComment = document.getElementById("employeeCommentInput")
const managerComment = document.getElementById("managerCommentInput")
const status = document.getElementById("statusBoxInput")
const requestDate = document.getElementById("requestDateInput")

// const results = sessionStorage.getItem("value");

// function transfer1(reimbursementId){
//     sessionStorage.setItem("value",reimbursementId.value);
//     window.location.href = "manager_page.html";
//     }



// Update Request Data -----------------------------------------

async function managerUpdateRequest(){
   
   
    let response = await fetch(
        "http://127.0.0.1:5000/manager/request_decision/", {
            method:"PATCH",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({"employeeId":employeeId.value, "managerId":managerId.value, "requestAmount":requestAmount.value, "requestComment":employeeComment.value,"requestComment2":managerComment.value, "requestId":reimbursementId.value, "requestStatus":status.value, "rrDate":requestDate.value })
        }
    )

    if (response.status === 200){
        let body = await response.json()

     
    } else {
        alert("your Employee update request failed")
    }
}

// Get Pending Employee Data -----------------------------------------

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

// Get Completed Employee Data -----------------------------------------

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