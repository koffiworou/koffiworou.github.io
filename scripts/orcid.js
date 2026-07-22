document.addEventListener("DOMContentLoaded", function () {
  const navbar = document.querySelector(".navbar-nav.navbar-nav-scroll.ms-auto");

  if (!navbar) return;

  const li = document.createElement("li");
  li.className = "nav-item";

  li.innerHTML = `
    <a class="nav-link" href="https://orcid.org/0000-0002-2230-8431"
       target="_blank" aria-label="ORCID">
      <img src="../images/orcid.svg"
           alt="ORCID"
           style="height: 1.15rem; width: 1.15rem;">
    </a>
  `;

  navbar.appendChild(li);
});