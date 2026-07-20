/* Ras Raaga – site interactions */
(function () {
  "use strict";

  // Page loader
  window.addEventListener("load", function () {
    var loader = document.querySelector(".page-loader");
    if (loader) {
      setTimeout(function () {
        loader.classList.add("done");
      }, 280);
    }
  });

  // Sticky header shadow
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () {
      header.classList.toggle("scrolled", window.scrollY > 20);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  // Mobile menu
  var toggle = document.querySelector(".menu-toggle");
  var mobileNav = document.querySelector(".mobile-nav");
  if (toggle && mobileNav) {
    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!open));
      mobileNav.classList.toggle("open", !open);
      document.body.style.overflow = open ? "" : "hidden";
    });
    mobileNav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        toggle.setAttribute("aria-expanded", "false");
        mobileNav.classList.remove("open");
        document.body.style.overflow = "";
      });
    });
    window.addEventListener("resize", function () {
      if (window.innerWidth >= 1200) {
        toggle.setAttribute("aria-expanded", "false");
        mobileNav.classList.remove("open");
        document.body.style.overflow = "";
      }
    });
  }

  // Scroll reveal
  var reveals = document.querySelectorAll(".reveal");
  if (reveals.length && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("visible");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
    );
    reveals.forEach(function (el) {
      io.observe(el);
    });
  } else {
    reveals.forEach(function (el) {
      el.classList.add("visible");
    });
  }

  // Countdown to Aug 30, 2026 5:00 PM PT (approx UTC-7 → 2026-08-30T17:00:00-07:00)
  var countdown = document.querySelector("[data-countdown]");
  if (countdown) {
    var target = new Date("2026-08-30T17:00:00-07:00").getTime();
    var units = ["days", "hours", "mins", "secs"];
    function tick() {
      var now = Date.now();
      var diff = Math.max(0, target - now);
      var d = Math.floor(diff / 86400000);
      var h = Math.floor((diff % 86400000) / 3600000);
      var m = Math.floor((diff % 3600000) / 60000);
      var s = Math.floor((diff % 60000) / 1000);
      var vals = [d, h, m, s];
      units.forEach(function (u, i) {
        var el = countdown.querySelector('[data-unit="' + u + '"]');
        if (el) el.textContent = String(vals[i]).padStart(2, "0");
      });
    }
    tick();
    setInterval(tick, 1000);
  }

  // Newsletter forms → join page with thank-you state
  document.querySelectorAll("[data-newsletter]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var base = form.getAttribute("data-base") || "";
      window.location.href = base + "newsletter-thank-you.html";
    });
  });
})();
