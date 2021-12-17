// const header = document.createElement("h1");
// header.textContent = `you logged in successfully`;
// document.body.appendChild(header);

function logout(){
    sessionStorage.clear();
    window.location.href = "login.html";
}

// need to do constants for body to post
async function employeeCreateRequest(){
    let response = await fetch(
        "http://127.0.0.1:5000//reimbursement_request", {
            method:"POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({"employeeId":employeeId.value, "firstName":firstName.value, "lastName":lastName.value, "password":password.value})
        }
    )
    if (response.status === 200){
        let body = await response.json()
        if (body["validated"]){
            sessionStorage.setItem("validated", true)
            window.location.href = "employee_page.html"
        } else {
            alert("Employee login failed: please try again")
        }
    } else {
        alert("your Employee login request failed")
    }
}


async function getEmployeeData(){
    let url = "http://127.0.0.1:5000/reimbursement_requests/<employee_id>";

    let response = await fetch(url);
    
    if (response.status === 200){
        let body = await response.json();
        populateData(body);
    } else {
        alert("There was a problem trying to get the employee information: sorry!");
    }
}

function populateData(responseBody){
    
    

    for (let player of responseBody){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${employee.employeeId}</td><td>${employee.managerId}</td><td>${employee.requestAmount}</td><td>${employee.requestComment}</td><td>${employee.requestComment2}</td><td>${employee.requestStatus}<td>${employee.rrDate}</td></td>`;
        EmployeeTableBody.appendChild(tableRow);
    }
}

getEmployeeData()