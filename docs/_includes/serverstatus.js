// Handling errors
function handleErrors(response) {
    if (!response.ok) {
        document.getElementById("serverStatus").innerHTML = "";
        document.getElementById("serverStatusM").innerHTML = "";
        document.getElementById("serverLogoName").classList.remove("hidden");
    }
    return response;
}

// Fetch API, mcstatus.io
fetch("https://api.mcstatus.io/v2/status/{% if site.useBedrockForOnlineStatus == true %}bedrock/{% endif %}java/{{ site.serverIP }}")
    .then(handleErrors)
    .then(response => {
        return response.json();
    })