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

  // Desktop nav dropdown — hover bridge + close delay + keyboard / outside / Escape
  (function () {
    var CLOSE_DELAY = 250;
    var items = document.querySelectorAll(".nav-desktop .nav-item");
    if (!items.length) return;

    function closeAll(except) {
      items.forEach(function (item) {
        if (except && item === except) return;
        item.classList.remove("is-open");
        var link = item.querySelector(".nav-link");
        if (link) link.setAttribute("aria-expanded", "false");
      });
    }

    items.forEach(function (item) {
      var dropdown = item.querySelector(".dropdown");
      var link = item.querySelector(".nav-link");
      if (!dropdown || !link) return;

      var closeTimer = null;
      link.setAttribute("aria-haspopup", "true");
      link.setAttribute("aria-expanded", "false");

      function openMenu() {
        clearTimeout(closeTimer);
        closeAll(item);
        item.classList.add("is-open");
        link.setAttribute("aria-expanded", "true");
      }

      function scheduleClose() {
        clearTimeout(closeTimer);
        closeTimer = setTimeout(function () {
          item.classList.remove("is-open");
          link.setAttribute("aria-expanded", "false");
        }, CLOSE_DELAY);
      }

      item.addEventListener("mouseenter", openMenu);
      item.addEventListener("mouseleave", scheduleClose);
      item.addEventListener("focusin", openMenu);
      item.addEventListener("focusout", function (e) {
        if (!item.contains(e.relatedTarget)) scheduleClose();
      });
    });

    document.addEventListener("click", function (e) {
      if (!e.target.closest(".nav-desktop .nav-item")) closeAll();
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") {
        var openItem = document.querySelector(".nav-desktop .nav-item.is-open");
        closeAll();
        if (openItem) {
          var parentLink = openItem.querySelector(".nav-link");
          if (parentLink) parentLink.focus();
        }
      }
    });
  })();

  // Next-event countdown from shared events data (assets/js/events-data.js)
  (function () {
    var root = document.querySelector("[data-next-event-countdown]");
    if (!root) return;

    var events = (window.RASRAGA_EVENTS || []).filter(function (ev) {
      return ev && ev.published !== false && ev.startAt && ev.endAt;
    });

    if (!events.length) {
      root.hidden = true;
      return;
    }

    events.sort(function (a, b) {
      return new Date(a.startAt).getTime() - new Date(b.startAt).getTime();
    });

    var titleEl = root.querySelector("[data-countdown-event-title]");
    var liveEl = root.querySelector("[data-countdown-live]");
    var unitsWrap = root.querySelector("[data-countdown-units]");
    var unitEls = {
      days: root.querySelector('[data-unit="days"]'),
      hours: root.querySelector('[data-unit="hours"]'),
      mins: root.querySelector('[data-unit="mins"]'),
      secs: root.querySelector('[data-unit="secs"]'),
    };

    function pad(n) {
      return String(n).padStart(2, "0");
    }

    function pickEvent(now) {
      for (var i = 0; i < events.length; i++) {
        var end = new Date(events[i].endAt).getTime();
        if (end > now) return events[i];
      }
      return null;
    }

    function tick() {
      var now = Date.now();
      var ev = pickEvent(now);

      if (!ev) {
        root.hidden = true;
        return;
      }

      root.hidden = false;
      if (titleEl) titleEl.textContent = ev.title || "";

      var start = new Date(ev.startAt).getTime();
      var end = new Date(ev.endAt).getTime();

      if (now >= start && now < end) {
        root.classList.add("is-live");
        if (unitsWrap) unitsWrap.hidden = true;
        if (liveEl) liveEl.hidden = false;
        return;
      }

      root.classList.remove("is-live");
      if (unitsWrap) unitsWrap.hidden = false;
      if (liveEl) liveEl.hidden = true;

      var diff = Math.max(0, start - now);
      var d = Math.floor(diff / 86400000);
      var h = Math.floor((diff % 86400000) / 3600000);
      var m = Math.floor((diff % 3600000) / 60000);
      var s = Math.floor((diff % 60000) / 1000);
      if (unitEls.days) unitEls.days.textContent = pad(d);
      if (unitEls.hours) unitEls.hours.textContent = pad(h);
      if (unitEls.mins) unitEls.mins.textContent = pad(m);
      if (unitEls.secs) unitEls.secs.textContent = pad(s);
    }

    tick();
    setInterval(tick, 1000);
  })();

  // Newsletter forms → thank-you page
  document.querySelectorAll("[data-newsletter]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var base = form.getAttribute("data-base") || "";
      window.location.href = base + "newsletter-thank-you.html";
    });
  });

  // Contact / sponsorship / feedback → mailto admin with validation + status
  function nearestStatus(form) {
    var prev = form.previousElementSibling;
    if (prev && prev.hasAttribute("data-form-status")) return prev;
    var parent = form.parentElement;
    if (parent) {
      var inParent = parent.querySelector("[data-form-status]");
      if (inParent) return inParent;
    }
    return form.querySelector("[data-form-status]");
  }

  function showStatus(el, type, message) {
    if (!el) return;
    el.hidden = false;
    el.classList.remove("is-success", "is-error");
    el.classList.add(type === "success" ? "is-success" : "is-error");
    el.textContent = message;
  }

  document.querySelectorAll("[data-mail-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var status = nearestStatus(form);
      if (!form.checkValidity()) {
        form.reportValidity();
        showStatus(status, "error", "Please complete all required fields correctly.");
        return;
      }

      var to = form.getAttribute("data-mail-to") || "hello@rasraaga.com";
      var subject = form.getAttribute("data-mail-subject") || "Website Enquiry";
      var lines = [];
      var fileNote = "";

      Array.prototype.forEach.call(form.elements, function (field) {
        if (!field.name || field.disabled) return;
        if (field.type === "file") {
          if (field.files && field.files[0]) {
            fileNote =
              "Attachment selected on website: " +
              field.files[0].name +
              " (please attach this file to this email before sending).";
          }
          return;
        }
        if (field.type === "checkbox") {
          lines.push(field.name + ": " + (field.checked ? field.value || "Yes" : "No"));
          return;
        }
        if (field.type === "radio" && !field.checked) return;
        if (field.tagName === "BUTTON") return;
        lines.push(field.name + ": " + (field.value || "").trim());
      });

      if (fileNote) lines.push("", fileNote);

      var body = lines.join("\n");
      var href =
        "mailto:" +
        encodeURIComponent(to).replace(/%40/g, "@") +
        "?subject=" +
        encodeURIComponent(subject) +
        "&body=" +
        encodeURIComponent(body);

      try {
        window.location.href = href;
        showStatus(
          status,
          "success",
          form.getAttribute("data-allow-file") === "true"
            ? "Opening your email app. Please review the message, attach your file if selected, and send. Feedback is not displayed publicly."
            : "Opening your email app. Please review and send the message to complete your submission."
        );
      } catch (err) {
        showStatus(
          status,
          "error",
          "Could not open your email app. Please email " + to + " directly."
        );
      }
    });
  });
})();
