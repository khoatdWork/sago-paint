const products = {
  "Sơn Nội Thất": [
    {name: "S60 Pro", badge: "Khuyên dùng", href: "../son-sagopaint-noi-that-lau-chui-hieu-qua-anaclean-be-mat-bong-mo.html", img: "https://cdn.sagopaint.vn/assets/products/son-sagopaint-noi-that-lau-chui-hieu-qua-anaclean-be-mat-bong-mo.png", features: "Bề mặt mịn, dễ lau chùi, phù hợp phòng khách và phòng ngủ.", coverage: "10m²/lít/lớp", primary: true},
    {name: "Sơn Nội Thất Cao Cấp", badge: "Nội thất", href: "../son-noi-that-lau-chui-hieu-qua-anaclean-be-mat-ban-bong.html", img: "https://cdn.sagopaint.vn/assets/products/son-noi-that-lau-chui-hieu-qua-anaclean-be-mat-ban-bong.png", features: "Màng sơn đẹp, che phủ tốt, dùng cho căn hộ và nhà phố.", coverage: "10m²/lít/lớp"},
    {name: "Sơn Siêu Mịn", badge: "Mịn đẹp", href: "../son-sagopaint-not-that-mang-son-min-ep-v-2000.html", img: "https://cdn.sagopaint.vn/assets/products/son-sagopaint-not-that-mang-son-min-ep-v-2000.png", features: "Hoàn thiện bề mặt tường mịn, tối ưu chi phí thi công.", coverage: "10m²/lít/lớp"}
  ],
  "Sơn Ngoại Thất": [
    {name: "ANA Satin Bề Mặt Bán Bóng", badge: "Ngoại thất", href: "../son-ngoai-that-ana-satin-be-mat-ban-bong.html", img: "https://cdn.sagopaint.vn/assets/products/son-ngoai-that-ana-satin-be-mat-ban-bong.png", features: "Bền màu, chống rêu mốc, phù hợp mặt tiền và tường ngoài.", coverage: "10m²/lít/lớp", primary: true},
    {name: "ANA Satin Bề Mặt Siêu Bóng", badge: "Bền thời tiết", href: "../son-ngoai-that-ana-satin-be-mat-sieu-bong.html", img: "https://cdn.sagopaint.vn/assets/products/son-ngoai-that-ana-satin-be-mat-sieu-bong.png", features: "Bề mặt sáng, dễ vệ sinh, chống chịu môi trường ngoài trời.", coverage: "10m²/lít/lớp"},
    {name: "Anashield Bóng Mờ", badge: "Chống phai", href: "../son-sagopaint-ngoai-that-chong-phai-mau-anashield-be-mat-bong-mo.html", img: "https://cdn.sagopaint.vn/assets/products/son-sagopaint-ngoai-that-chong-phai-mau-anashield-be-mat-bong-mo.png", features: "Hỗ trợ chống phai màu cho tường ngoại thất hiện đại.", coverage: "10m²/lít/lớp"}
  ],
  "Sơn Chống Thấm": [
    {name: "SAGO S68 Pro", badge: "Chống thấm cao cấp", href: "../sago-s-68-pro-chong-tham-a-nang-lo-thien-cao-cap.html", img: "../assets/products/sago-s68-pro-preview.webp", features: "Chống thấm lộ thiên, bền UV, phù hợp sân thượng và ban công.", coverage: "Theo bề mặt thực tế", primary: true},
    {name: "Aqua Shield 5 in 1", badge: "Chống thấm màu", href: "../son-chong-tham-mau-aqua-shield-5-in1.html", img: "https://cdn.sagopaint.vn/assets/products/son-chong-tham-mau-aqua-shield-5-in1.png", features: "Bảo vệ tường khỏi nước xâm nhập, dùng được cho tường ngoài.", coverage: "10m²/lít/lớp"},
    {name: "BT-11A Pha Xi Măng", badge: "Xử lý nền", href: "../chat-chong-tham-bt-11a-pha-xi-mang.html", img: "https://cdn.sagopaint.vn/assets/products/chat-chong-tham-bt-11a-pha-xi-mang.png", features: "Giải pháp chống thấm cho bề mặt xi măng và bê tông.", coverage: "Theo hạng mục"}
  ]
};

const prices = {
  "Sơn Nội Thất": {primer: 65000, finish: 95000},
  "Sơn Ngoại Thất": {primer: 75000, finish: 125000},
  "Sơn Chống Thấm": {primer: 85000, finish: 145000}
};

const inputs = document.querySelectorAll(".calculator-panel input, .calculator-panel select");
const tabs = document.querySelectorAll(".calculator-tab");
let mode = "room";
let validEstimate = true;

function value(id) {
  const number = Number(document.getElementById(id).value);
  return Number.isFinite(number) ? Math.max(0, number) : 0;
}

function money(number) {
  return new Intl.NumberFormat("vi-VN").format(Math.round(number)) + " VNĐ";
}

function currentType() {
  return mode === "room" ? document.getElementById("paintTypeRoom").value : document.getElementById("paintTypeArea").value;
}

function calculate() {
  const activeInputs = document.querySelectorAll(`#panel-${mode} input`);
  const invalidInput = [...activeInputs].find(input => !input.validity.valid);
  activeInputs.forEach(input => input.setAttribute("aria-invalid", String(!input.validity.valid)));
  let paintableArea = 0;
  let coats = 2;
  if (mode === "room") {
    const wallArea = (value("length") + value("width")) * 2 * value("height");
    const doorArea = value("doors") * 2;
    const windowArea = value("windows") * 1.5;
    paintableArea = Math.max(0, wallArea - doorArea - windowArea);
    coats = Math.max(1, value("coatsRoom"));
  } else {
    paintableArea = value("manualArea");
    coats = Math.max(1, value("coatsArea"));
  }

  const finalArea = paintableArea * coats;
  const liters = Math.ceil(finalArea / 10);
  const buckets = Math.ceil(liters / 18);
  const type = currentType();
  const primerCost = Math.ceil(paintableArea / 10) * prices[type].primer;
  const finishCost = liters * prices[type].finish;
  validEstimate = !invalidInput && Number.isSafeInteger(primerCost + finishCost);
  document.getElementById("calculationMessage").textContent = validEstimate
    ? "" : invalidInput
      ? `${invalidInput.labels[0].textContent}: ${invalidInput.validationMessage}`
      : "Giá trị quá lớn để tính chính xác. Vui lòng giảm diện tích hoặc số lớp sơn.";
  if (!validEstimate) {
    ["paintableArea", "coatResult", "paintNeeded", "bucketResult", "primerCost", "finishCost", "totalCost"]
      .forEach(id => document.getElementById(id).textContent = "—");
    return;
  }

  document.getElementById("paintableArea").textContent = Math.round(paintableArea) + " m²";
  document.getElementById("coatResult").textContent = coats + " lớp";
  document.getElementById("paintNeeded").textContent = liters + " L";
  document.getElementById("bucketResult").textContent = buckets + " thùng 18L";
  document.getElementById("primerCost").textContent = money(primerCost);
  document.getElementById("finishCost").textContent = money(finishCost);
  document.getElementById("totalCost").textContent = money(primerCost + finishCost);
  renderProducts(type);
}

function renderProducts(type) {
  document.getElementById("productRecommendations").innerHTML = products[type].map((product) => `
    <div class="col-md-6 col-xl-4">
      <article class="product-card ${product.primary ? "recommended" : ""} d-flex flex-column">
        <a class="product-image-link" href="${product.href}" aria-label="Xem ${product.name}">
        <img src="${product.img}" alt="${product.name}" loading="lazy" width="600" height="600">
        </a>
        <div class="product-card-body d-flex flex-column flex-grow-1">
          <span class="product-badge">${product.badge}</span>
          <h3 class="h5">${product.name}</h3>
          <p>${product.features}</p>
          <p><strong>Độ phủ:</strong> ${product.coverage}</p>
          <div class="d-flex flex-wrap gap-2 mt-auto">
            <a class="btn btn-sm btn-outline-primary" href="${product.href}">Xem Chi Tiết</a>
            <a class="btn btn-sm btn-primary" href="#tu-van">Liên Hệ Tư Vấn</a>
          </div>
        </div>
      </article>
    </div>
  `).join("");
}

tabs.forEach((tab) => {
  tab.addEventListener("click", () => {
    mode = tab.dataset.tab;
    tabs.forEach((item) => {
      item.classList.toggle("active", item === tab);
      item.setAttribute("aria-selected", item === tab ? "true" : "false");
      item.tabIndex = item === tab ? 0 : -1;
    });
    document.querySelectorAll(".calculator-panel").forEach((panel) => {
      panel.classList.toggle("active", panel.id === `panel-${mode}`);
      panel.hidden = panel.id !== `panel-${mode}`;
    });
    calculate();
  });
});

tabs.forEach((tab, index) => {
  tab.addEventListener("keydown", (event) => {
    let next;
    if (event.key === "ArrowRight") next = (index + 1) % tabs.length;
    else if (event.key === "ArrowLeft") next = (index + tabs.length - 1) % tabs.length;
    else if (event.key === "Home") next = 0;
    else if (event.key === "End") next = tabs.length - 1;
    else return;
    event.preventDefault();
    tabs[next].click();
    tabs[next].focus();
  });
});

document.querySelectorAll("[data-preset]").forEach((button) => {
  button.addEventListener("click", () => {
    const preset = button.dataset.preset;
    const presets = {
      bedroom: {mode: "room", length: 4, width: 3.5, height: 3, doors: 1, windows: 1},
      living: {mode: "room", length: 6, width: 4, height: 3.2, doors: 1, windows: 2},
      apt60: {mode: "area", area: 150},
      apt80: {mode: "area", area: 200},
      house100: {mode: "area", area: 280},
      house150: {mode: "area", area: 420}
    };
    const data = presets[preset];
    document.querySelector(`[data-tab="${data.mode}"]`).click();
    if (data.mode === "room") {
      ["length", "width", "height", "doors", "windows"].forEach((id) => document.getElementById(id).value = data[id]);
    } else {
      document.getElementById("manualArea").value = data.area;
    }
    calculate();
  });
});

inputs.forEach((input) => input.addEventListener("input", calculate));
inputs.forEach((input) => input.addEventListener("change", calculate));

document.getElementById("consultForm").addEventListener("submit", (event) => {
  event.preventDefault();
  const form = event.currentTarget;
  const message = document.getElementById("formMessage");
  document.getElementById("fullName").value = document.getElementById("fullName").value.trim();
  if (!form.checkValidity()) {
    form.classList.add("was-validated");
    message.textContent = "Vui lòng nhập họ tên, số điện thoại và loại công trình.";
    form.querySelector(":invalid")?.focus();
    return;
  }
  calculate();
  if (!validEstimate) {
    message.textContent = "Vui lòng điều chỉnh giá trị tính sơn trước khi soạn email, hoặc gọi điện để được tư vấn.";
    (document.querySelector(`#panel-${mode} input:invalid`)
      || document.getElementById(mode === "room" ? "length" : "manualArea")).focus();
    return;
  }
  const field = (id) => document.getElementById(id).value.trim();
  const body = [
    "Tôi cần tư vấn sơn cho công trình:",
    `Họ tên: ${field("fullName")}`,
    `Điện thoại: ${field("phone")}`,
    `Email: ${field("email")}`,
    `Loại công trình: ${field("projectType")}`,
    `Hệ sơn: ${currentType()}`,
    ...["paintableArea", "coatResult", "paintNeeded", "bucketResult", "totalCost"]
      .map(id => document.getElementById(id).textContent),
    "Kết quả trên là ước tính; vui lòng tư vấn định mức và báo giá thực tế."
  ].join("\n");
  const mailto = "mailto:info.sagopaint@gmail.com?subject="
    + encodeURIComponent("Tư vấn sơn nhà — " + field("projectType"))
    + "&body=" + encodeURIComponent(body);
  message.textContent = "Đang mở ứng dụng email. Vui lòng kiểm tra và tự gửi email; nếu không mở được, hãy gọi +8428 6681 5050. Thông tin của bạn vẫn được giữ trên trang.";
  window.location.href = mailto;
});

calculate();
