const receiveImage = async (formData) => {
    try {

        const tableBody = document.querySelector('#resultTable tbody');
        const response = await fetch("/api/receive-image", {
            method: "POST",
            body: formData,
        });
  
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        document.getElementById('loading').classList.add('d-none');
        document.getElementById('extractedTable').classList.remove('d-none');

        const result = await response.json();
        
        console.log(result);
        if (result.error) {
            return;
        }
        tableBody.innerHTML = '';
        result.data.forEach((item, index) => {
            
            const row = document.createElement('tr');
            const rowNumber = document.createElement('td');

            rowNumber.textContent = index + 1;
            const text = document.createElement('td');
            text.textContent = item.text.toLowerCase();

            row.appendChild(rowNumber);
            row.appendChild(text);

            tableBody.appendChild(row);
        });
        
    } catch (error) {
        console.error("Error sending the image:", error);
    }
}

const cameraBtn = () => {
    document.getElementById('video').classList.remove('d-none');
    document.getElementById('captureBtnGroup').classList.remove('d-none');
    document.getElementById('buttonsGroup').classList.add('d-none');

    document.getElementById('notice').innerHTML = "Please place your ID card into the box properly.";
    const video = document.getElementById('video');
    
    if (navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: {
            facingMode: "environment" 
        } })
            .then(function (stream) {
                video.srcObject = stream;
            })
            .catch(function (error) {
                console.log("Something went wrong: ", error);
            });
    }
}

const captureBtn = () => {
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

    canvas.toBlob(async (blob) => {

        const formData = new FormData();
        formData.append('file', blob, 'captured-image.png');
        receiveImage(formData);

        const stream = video.srcObject;
        if (stream) {
            const tracks = stream.getTracks();
            tracks.forEach(track => track.stop());

            document.getElementById('loading').classList.remove('d-none');
            
            document.getElementById('video').classList.add('d-none');
            document.getElementById('captureBtnGroup').classList.add('d-none');
        }

    }, 'image/png'); 
}

const uploadBtn = () => {
    document.getElementById('imageUploadGroup').classList.remove('d-none');
    document.getElementById('buttonsGroup').classList.add('d-none');
}

const sendImage = async () => {
    const fileInput = document.getElementById("imageUpload");
    const file = fileInput.files[0];
  
    if (!file) {
      alert("Please select a file before sending.");
      return;
    }

    document.getElementById('fileInputContainer').classList.add('d-none');
    document.getElementById('sendImageContainer').classList.add('d-none');
    document.getElementById('notice').classList.add('d-none');
    document.getElementById('loading').classList.remove('d-none');
  
    const formData = new FormData();
    formData.append("file", file);
    receiveImage(formData);
};
  

document.getElementById('uploadBtn').addEventListener('click', uploadBtn)
document.getElementById('cameraBtn').addEventListener('click', cameraBtn)
document.getElementById('captureBtn').addEventListener('click', captureBtn)
document.getElementById('sendImage').addEventListener('click', sendImage)