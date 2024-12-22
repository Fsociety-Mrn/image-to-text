function startVideoStream() {
    const video = document.getElementById('video');
    
    if (navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(function (stream) {
                video.srcObject = stream;

                // Add event listener for when the video starts playing
                video.addEventListener('play', () => {
                    drawRectangleOnVideo();
                });
            })
            .catch(function (error) {
                console.log("Something went wrong: ", error);
            });
    }
}

function drawRectangleOnVideo() {
    const canvas = document.getElementById('canvas');
    const video = document.getElementById('video');
    const ctx = canvas.getContext('2d');

    // Wait for the video metadata to load so we can get the proper video size
    video.onloadedmetadata = function () {
        // Set the canvas size to match the video size
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;

        // Position the canvas to overlay the video
        canvas.style.left = video.offsetLeft + 'px';
        canvas.style.top = video.offsetTop + 'px';

        // Show the canvas once it's set up
        canvas.classList.remove('d-none');

        function render() {
            // Clear previous frame from the canvas
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            // Draw the current frame of the video onto the canvas
            ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

            // Draw the rectangle over the video frame (this rectangle is drawn on the canvas)
            const rectWidth = 200;  // width of the rectangle
            const rectHeight = 150; // height of the rectangle
            const rectX = (canvas.width - rectWidth) / 2;
            const rectY = (canvas.height - rectHeight) / 2;

            // Draw the rectangle
            ctx.strokeStyle = 'red';  // Color of the rectangle
            ctx.lineWidth = 2;  // Width of the rectangle's border
            ctx.strokeRect(rectX, rectY, rectWidth, rectHeight);

            // Continue rendering new frames
            requestAnimationFrame(render);
        }

        // Start the rendering loop
        render();
    }
}

document.getElementById('startScan').addEventListener('click', function () {
    document.getElementById('notice').classList.remove('d-none');
    document.getElementById('video').classList.remove('d-none');
    document.getElementById('canvas').classList.remove('d-none');  // Unhide the canvas
    document.getElementById('startScan').classList.add('d-none');

    startVideoStream();
});
