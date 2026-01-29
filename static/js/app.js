// ================= EMAIL =================
function sendMail() {
  let parms = {
    name: document.getElementById("name")?.value || "",
    email: document.getElementById("email")?.value || "",
    message: document.getElementById("message")?.value || "",
  };

  emailjs
    .send("service_5t7zdwm", "template_17axzim", parms)
    .then(() => alert("Your Email Has Been Received!\nThanks for your query!"))
    .catch((err) => console.error("Email error:", err));
}

// ================= HELPERS =================
const BASE_URL = "";

async function safeFetch(url) {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`API failed: ${url}`);
  return res.json();
}

// ================= PROJECTS =================
async function loadProjects() {
  const container = document.getElementById("projects-container");
  if (!container) return;

  try {
    const data = await safeFetch(`${BASE_URL}/api/projects/`);

    if (!Array.isArray(data) || data.length === 0) {
      container.innerHTML = "<p>No projects available.</p>";
      return;
    }

    let html = "";

    data.forEach((p) => {
      const img = p.image
        ? `${BASE_URL}${p.image}`
        : "./assets/images/fallback.png";

      html += `
        <div class="project">
          <figure class="project-figure">
            <img src="${img}" alt="${p.title || "project"}" />
          </figure>

          <div class="project-info">
            <h2>${p.title || ""}</h2>
            <h4>${p.description || ""}</h4>

            <a href="${p.live || p.github || "#"}" target="_blank">
              <button>View Project</button>
            </a>
          </div>
        </div>
      `;
    });

    container.innerHTML = html;
  } catch (err) {
    console.error("Project Load Error:", err);
    container.innerHTML = "<p>Failed to load projects.</p>";
  }
}
loadProjects();

// ================= LOGO =================
async function loadLogo() {
  const logo = document.getElementById("logo-link");
  if (!logo) return;

  try {
    const data = await safeFetch(`${BASE_URL}/api/logo/`);
    let html = "";

    data.forEach((l) => {
      html += `<h1 class="logo">${l.logoTitle || ""}</h1>`;
    });

    logo.innerHTML = html || "<h1 class='logo'>Portfolio</h1>";
  } catch (err) {
    console.error("Logo Load Error:", err);
  }
}
loadLogo();

// ================= PROFILE IMAGE =================
async function loadProfilePicture() {
  const imageContainer = document.getElementById("img-container");
  if (!imageContainer) return;

  try {
    const data = await safeFetch(`${BASE_URL}/api/profilepicture/`);
    let html = "";

    data.forEach((p) => {
      const sketch = p.sketch ? `${BASE_URL}${p.sketch}` : "";
      const original = p.original ? `${BASE_URL}${p.original}` : "";

      if (sketch || original) {
        html += `
          ${sketch ? `<img src="${sketch}" class="sketch" />` : ""}
          ${original ? `<img src="${original}" class="original" />` : ""}
        `;
      }
    });

    imageContainer.innerHTML = html || "<p>No profile image</p>";
  } catch (err) {
    console.error("Profile Picture Error:", err);
  }
}
loadProfilePicture();

// ================= WELCOME =================
async function loadWelcome() {
  const welcomeContainer = document.getElementById("welcome");
  if (!welcomeContainer) return;

  try {
    const data = await safeFetch(`${BASE_URL}/api/welcomenote/`);
    let html = "";

    data.forEach((w) => {
      html += `
        <p class="welcome-note">
          Hey, I'm <span class="name">${w.name || ""}</span> 👋 <br />
          ${w.line1 || ""}<br />
          ${w.line2 || ""}<br />
        </p>
        <button class="hire-me type-1" id="hire-btn"></button>
      `;
    });

    welcomeContainer.innerHTML = html;

    const btn = document.getElementById("hire-btn");
    if (btn)
      btn.addEventListener("click", () => btn.classList.toggle("active"));
  } catch (err) {
    console.error("Welcome Load Error:", err);
  }
}
loadWelcome();

// ================= MORE LIST =================
async function loadMoreItems() {
  const moreList = document.getElementById("more-list");
  if (!moreList) return;

  try {
    const data = await safeFetch(`${BASE_URL}/api/morelist/`);
    let html = "";

    data.forEach((m) => {
      // Use Absolute File Paths
      html += `
        <li class="more-item">
          <a href="/${m.file}" class="more-link">${m.more}</a>
        </li>
      `;
    });

    moreList.innerHTML = html || "<li>No items</li>";
  } catch (err) {
    console.error("More List Error:", err);
  }
}
loadMoreItems();

// ================= EXPERIENCE =================
async function loadExperience() {
  const container = document.getElementById("cards-container");
  if (!container) return;

  try {
    const data = await safeFetch(`${BASE_URL}/api/experience/`);
    let html = "";

    data.forEach((e) => {
      html += `
        <div class="card">
          <h2>${e.title || ""}</h2>
          <p>${e.description || ""}</p>
        </div>
      `;
    });

    container.innerHTML = html || "<p>No experience added.</p>";
  } catch (err) {
    console.error("Experience Error:", err);
  }
}
loadExperience();

// ================= EDUCATION =================
async function loadEducation() {
  const educationContainer = document.getElementById(
    "education-card-container",
  );
  if (!educationContainer) return;

  try {
    const data = await safeFetch(`${BASE_URL}/api/education/`);
    let html = "";

    data.forEach((e) => {
      html += `
        <div class="card-panel">
          <span class="panel-title">${e.instiitute || ""}</span>
          <div class="panel-content">
            <h3>${e.degree || ""}</h3>
            <p>${e.description || ""}</p>
          </div>
        </div>
      `;
    });

    educationContainer.innerHTML = html || "<p>No education records.</p>";
  } catch (err) {
    console.error("Education Error:", err);
  }
}
loadEducation();

// ================= SKILL PROGRESS =================
async function loadSkillProgress() {
  const progressContainer = document.getElementById("skill-progress-id");
  if (!progressContainer) return;

  try {
    const data = await safeFetch(`${BASE_URL}/api/skillsprogress/`);
    let html = "";

    data.forEach((p) => {
      html += `
        <div class="skill-box">
          <span class="skill-title">${p.name || ""}</span>
          <div class="skill-bar">
            <span class="skill-per fed"
              style="width:${p.percentage || 0}%; animation-delay:0.${p.id || 1}s;">
              <span class="tooltip">${p.percentage || 0}%</span>
            </span>
          </div>
        </div>
      `;
    });

    progressContainer.innerHTML = html || "<p>No skills yet.</p>";
  } catch (err) {
    console.error("Skill Progress Error:", err);
  }
}
loadSkillProgress();

// ================= SKILLS LEARNED =================
async function loadSkillLearned() {
  const learnContainer = document.getElementById("skills-learned-id");
  if (!learnContainer) return;

  try {
    const data = await safeFetch(`${BASE_URL}/api/skillslearned/`);
    let html = "";

    data.forEach((l) => {
      html += `
        <div class="skill-item">
          <img class="skill-icon" width="50" height="50"
            src="${l.svg || "./assets/images/skill.png"}"
            alt="${l.name || ""}">
          <p class="skill-name">${l.name || ""}</p>
        </div>
      `;
    });

    learnContainer.innerHTML = html || "<p>No skills added.</p>";
  } catch (err) {
    console.error("Skill Learned Error:", err);
  }
}
loadSkillLearned();
