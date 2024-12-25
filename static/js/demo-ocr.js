
document.getElementById('uploadBtn').addEventListener('click', uploadBtn)
document.getElementById('cameraBtn').addEventListener('click', cameraBtn)

function cameraBtn() {
    document.getElementById('video').classList.remove('d-none');
    document.getElementById('captureBtnGroup').classList.remove('d-none');
    document.getElementById('buttonsGroup').classList.add('d-none');

    document.getElementById('notice').innerHTML = "Please place your ID card into the box properly.";
    const video = document.getElementById('video');
    
    if (navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(function (stream) {
                video.srcObject = stream;
            })
            .catch(function (error) {
                console.log("Something went wrong: ", error);
            });
    }
}

function uploadBtn(){
    document.getElementById('imageUploadGroup').classList.remove('d-none');
    document.getElementById('buttonsGroup').classList.add('d-none');
}

