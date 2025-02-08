const canvas = document.getElementById("particle-bg");
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const particles = [];

class Particle {
    constructor(x, y, size, speedX, speedY) {
        this.x = x; this.y = y; this.size = size;
        this.speedX = speedX; this.speedY = speedY;
    }
    update() {
        this.x += this.speedX; this.y += this.speedY;
        if (this.x > canvas.width || this.x < 0) this.speedX *= -1;
        if (this.y > canvas.height || this.y < 0) this.speedY *= -1;
    }
    draw() {
        ctx.fillStyle = "rgba(255, 204, 0, 0.7)";
        ctx.beginPath(); ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.closePath(); ctx.fill();
    }
}

function createParticles() {
    for (let i = 0; i < 50; i++) {
        let size = Math.random() * 3 + 1;
        let x = Math.random() * canvas.width; let y = Math.random() * canvas.height;
        let speedX = (Math.random() - 0.5) * 2; let speedY = (Math.random() - 0.5) * 2;
        particles.push(new Particle(x, y, size, speedX, speedY));
    }
}

function animateParticles() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles.forEach(particle => { particle.update(); particle.draw(); });
    requestAnimationFrame(animateParticles);
}

createParticles();
animateParticles();

window.addEventListener("resize", () => {
    canvas.width = window.innerWidth; canvas.height = window.innerHeight;
    particles.length = 0; createParticles();
});
