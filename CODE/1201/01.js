// HTML 요소 선택
const input = document.querySelector("input");
const button = document.querySelector("button");

// 날씨 표시 영역
const cityNameEl = document.querySelector("h2");
const regionEl = document.querySelector("h2 + p");
const iconImg = document.querySelector("img");
const tempEl = document.querySelector("img + div");

// 상세 정보
const feelsLikeEl = document.querySelectorAll("div > div span")[1]; // 체감온도 값
const humidityEl = document.querySelectorAll("div > div span")[3]; // 습도 값
const windEl = document.querySelectorAll("div > div span")[5]; // 풍속 값
const pressureEl = document.querySelectorAll("div > div span")[7]; // 기압 값

// 에러 메시지 영역
const errorBox = document.querySelectorAll("div")[3];

// API KEY
const API_KEY = "d6d2e3bba1fb44b94edd99077225939b";


// 도시 이름으로 날씨 가져오는 함수
async function getWeatherByCity(city) {
  try {
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${API_KEY}&lang=kr&units=metric`;

    const response = await fetch(url);

    // 입력 오류 처리
    if (!response.ok) {
      throw new Error("도시 정보를 찾을 수 없습니다.");
    }

    const data = await response.json();
    console.log("현재 날씨:", data);

    // 가져온 날씨 화면에 표시
    renderWeather(data);

  } catch (error) {
    errorBox.textContent = error.message;
    errorBox.style.color = "red";
  }
}


// 화면에 날씨 데이터를 표시하는 함수
function renderWeather(w) {
  errorBox.textContent = ""; // 에러 초기화

  // 도시명 / 국가 코드
  cityNameEl.textContent = w.name;
  regionEl.textContent = w.sys.country;

  // 아이콘 변경
  const iconCode = w.weather[0].icon;
  iconImg.src = `https://openweathermap.org/img/wn/${iconCode}@2x.png`;

  // 현재 온도
  tempEl.textContent = `${Math.round(w.main.temp)}°C`;

  // 세부 정보
  feelsLikeEl.textContent = w.main.feels_like;
  humidityEl.textContent = w.main.humidity;
  windEl.textContent = w.wind.speed;
  pressureEl.textContent = w.main.pressure;
}


// 검색 버튼 클릭
button.addEventListener("click", () => {
  const city = input.value.trim();
  if (city === "") {
    alert("도시 이름을 입력하세요!");
    return;
  }
  getWeatherByCity(city);
});


// 엔터키로 검색
input.addEventListener("keypress", (e) => {
  if (e.key === "Enter") button.click();
});
