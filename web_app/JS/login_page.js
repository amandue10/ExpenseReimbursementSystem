const employeeId = document.getElementById("idInput")
const password = document.getElementById("passwordInput")
const firstName = document.getElementById("firstNameInput")
const lastName = document.getElementById("lastNameInput")
const managerId = document.getElementById("managerIdInput")
const managerFirstName = document.getElementById("managerFirstNameInput")
const managerLastName = document.getElementById("managerLastNameInput")
const managerPassword = document.getElementById("managerPasswordInput")


async function employeeLogin(){
    let response = await fetch(
        "http://127.0.0.1:5000/employee_login", {
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
        alert("your login request failed")
    }
}

async function managerLogin(){
    let response = await fetch(
        "http://127.0.0.1:5000/manager_login", {
            method:"POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({"managerId":managerId.value, "firstName":managerFirstName.value, "lastName":managerLastName.value, "password":managerPassword.value})
        }
    )
    if (response.status === 200){
        let body = await response.json()
        if (body["validated"]){
            sessionStorage.setItem("validated", true)
            window.location.href = "manager_page.html"
        } else {
            alert("Manager login failed: please try again")
        }
    } else {
        alert("your login request failed")
    }
}