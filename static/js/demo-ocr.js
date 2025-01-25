

function cameraBtn() {
    document.getElementById('video').classList.remove('d-none');
    document.getElementById('captureBtnGroup').classList.remove('d-none');
    document.getElementById('buttonsGroup').classList.add('d-none');

    // document.getElementById('notice').innerHTML = "Please place your ID card into the box properly.";
    // const video = document.getElementById('video');
    
    // if (navigator.mediaDevices.getUserMedia) {
    //     navigator.mediaDevices.getUserMedia({ video: true })
    //         .then(function (stream) {
    //             video.srcObject = stream;
    //         })
    //         .catch(function (error) {
    //             console.log("Something went wrong: ", error);
    //         });
    // }
}

function uploadBtn(){
    document.getElementById('imageUploadGroup').classList.remove('d-none');
    document.getElementById('buttonsGroup').classList.add('d-none');
}

const sendImage = async () => {

    const tableBody = document.querySelector('#resultTable tbody');
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
  
    try {

        const response = await fetch("http://127.0.0.1:5000/api/receive-image", {
            method: "POST",
            body: formData,
        });
  
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        document.getElementById('loading').classList.add('d-none');
        document.getElementById('extractedTable').classList.remove('d-none');

        const result = await response.json();

        if (result.error) {
            return;
        }
        tableBody.innerHTML = '';
        result.data.forEach((item, index) => {
            
            const row = document.createElement('tr');
            const rowNumber = document.createElement('td');

            rowNumber.textContent = index + 1;
            const text = document.createElement('td');
            text.textContent = item.text;

            row.appendChild(rowNumber);
            row.appendChild(text);

            tableBody.appendChild(row);
        });
        
    } catch (error) {
        console.error("Error sending the image:", error);
    }
  };
  

document.getElementById('uploadBtn').addEventListener('click', uploadBtn)
document.getElementById('cameraBtn').addEventListener('click', cameraBtn)
document.getElementById('sendImage').addEventListener('click', sendImage)