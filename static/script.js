const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const captureBtn = document.getElementById("captureBtn");

navigator.mediaDevices.getUserMedia({
    video: true
})
.then((stream) => {
    video.srcObject = stream;
});

captureBtn.addEventListener("click", async () => {

    const ctx = canvas.getContext("2d");
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

    const image = canvas.toDataURL("image/jpeg");

    const response = await fetch("/detect", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            image: image
        })
    });

    const result = await response.json();

    alert(result.message);
});